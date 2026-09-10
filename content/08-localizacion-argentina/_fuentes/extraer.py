"""Extract workbook topics and static Git evidence. Never imports Odoo or changes the source repo."""
import argparse
import ast
import hashlib
import json
import posixpath
import re
import subprocess
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTENT = HERE.parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--repo', type=Path, default=CONTENT.parents[1] / 'l10n_ar_eynes')
args = parser.parse_args()

def git(*args_):
    return subprocess.check_output(['git', '-C', str(args.repo), *args_], text=True)

def save(name, obj):
    (HERE / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

workbook = CONTENT / 'temas localización.xlsx'
ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
topics = []
sheets = []
with zipfile.ZipFile(workbook) as z:
    strings = []
    if 'xl/sharedStrings.xml' in z.namelist():
        strings = [''.join(el.itertext()) for el in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', ns)]
    rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    for sheet in ET.fromstring(z.read('xl/workbook.xml')).findall('m:sheets/m:sheet', ns):
        name = sheet.get('name')
        rid = sheet.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        path = posixpath.normpath(posixpath.join('xl', rels[rid])).lstrip('/')
        rows = []
        for row in ET.fromstring(z.read(path)).findall('m:sheetData/m:row', ns):
            values = {}
            for cell in row:
                v = cell.find('m:v', ns)
                value = v.text if v is not None else ''
                if cell.get('t') == 's':
                    value = strings[int(value)]
                elif cell.get('t') == 'inlineStr':
                    value = ''.join(cell.find('m:is', ns).itertext())
                if value:
                    values[cell.get('r')] = value
            if values:
                rows.append({'fila': int(row.get('r')), 'celdas': values})
                topics.append({'id': f'{name}-{row.get("r")}', 'hoja': name, 'fila': int(row.get('r')), 'texto_original': values.get('A'+row.get('r'), ''), 'nota_original': values.get('B'+row.get('r'), '')})
        sheets.append({'nombre': name, 'filas': rows})
save('excel.json', {'archivo': workbook.name, 'sha256': hashlib.sha256(workbook.read_bytes()).hexdigest(), 'hojas': sheets})

branches = {}
texts = {}
for version in ['15.0', '17.0', '19.0']:
    ref = 'origin/' + version
    commit = git('rev-parse', ref).strip()
    files = git('ls-tree', '-r', '--name-only', commit).splitlines()
    source = {}
    for path in files:
        if path.endswith(('.py', '.xml', '.csv', '.js', '.md', '.rst')) and not path.startswith('setup/'):
            source[path] = git('show', commit + ':' + path)
    texts[version] = source
    modules = {}
    for path, text in source.items():
        if path.endswith('/__manifest__.py'):
            data = ast.literal_eval(text)
            modules[path.split('/')[0]] = {k: data.get(k) for k in ['name', 'version', 'depends', 'external_dependencies', 'installable', 'data', 'assets']}
    inventory = []
    for path, text in source.items():
        if not path.endswith('.py') or '/migrations/' in path:
            continue
        try:
            tree = ast.parse(text)
            symbols = [{'nombre': n.name, 'linea': n.lineno} for n in ast.walk(tree) if isinstance(n, (ast.ClassDef, ast.FunctionDef))]
            fields = [{'nombre': ast.unparse(n.targets[0]), 'linea': n.lineno} for n in ast.walk(tree) if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute) and isinstance(n.value.func.value, ast.Name) and n.value.func.value.id == 'fields']
            inventory.append({'archivo': path, 'simbolos': symbols, 'campos': fields})
        except SyntaxError as e:
            inventory.append({'archivo': path, 'error_parseo': str(e)})
    branches[version] = {'ref': ref, 'commit': commit, 'fecha_commit': git('show', '-s', '--format=%cI', commit).strip(), 'archivos': files, 'modulos': modules}
    save('inventario-' + version + '.json', inventory)
save('ramas.json', branches)

# Each selector is a path plus a symbol/text pattern, not a claim of a passing runtime test.
M = 'l10n_ar_eynes/models/'
W = 'l10n_ar_eynes/wizard/'
R = 'l10n_ar_eynes/report/'
D = 'l10n_ar_eynes/data/'
P = 'l10n_ar_pos_wsfe/'
selector = {}
def assign(sheet, nums, category, *refs):
    for num in nums:
        selector[f'{sheet}-{num}'] = (category, refs)

def c(nums, category, *refs): assign('Comprobantes', nums, category, *refs)
c([1], 'datos-fiscales-y-padrones', (M+'res_partner.py', 'document_type_id'))
c([2], 'datos-fiscales-y-padrones', (M+'res_partner.py', 'nro_insc_iibb'))
c([3,4,5,6,50], 'datos-fiscales-y-padrones', (M+'res_partner.py', 'exclusion_certificate|excluded_percent|ex_date_from|percent ='))
c([7,8,54], 'facturacion-y-comprobantes', (M+'account_journal.py', 'fiscal_type =|sequence_id =|get_sequence_from_invoice'))
c([9], 'facturacion-y-comprobantes', (W+'account_debit_note.py', '_prepare_default_values'))
c([10,11,59], 'multimoneda-y-diferencias', (M+'account_move.py', 'currency_rate ='), (W+'account_change_currency.py', 'def change_currency'))
c([12,17], 'cobros-y-pagos', (M+'account_payment_order.py', 'payment_mode_line_ids ='))
c([13,18], 'cobros-y-pagos', (M+'account_payment_order.py', 'invoice_ids =|line_ids ='))
c([14,19,20], 'cobros-y-pagos', (M+'account_payment_order.py', 'third_party_check|issued_check_ids ='))
c([15], 'cheques-y-conciliacion', (M+'account_check.py', 'checkbook_format ='))
c([16], 'retenciones-y-percepciones', (M+'account_payment_order.py', 'retention_ids =|certificate_no ='))
c([21], 'retenciones-y-percepciones', (M+'account_payment_order.py', 'def calculate_retentions'))
c([22], 'retenciones-y-percepciones', (M+'account_payment_order.py', 'def apply_retention_sequence|def validate_retentions_sequence'))
c([23,66], 'retenciones-y-percepciones', (M+'retention.py', 'def _compute_amount_via_scale|def get_period_base_amount'))
c([24,29,52], 'datos-fiscales-y-padrones', ('l10n_ar_padron_ws_consumer/models/res_partner.py', 'def do_update_from_padron|def _update_partner_ret'))
c([25], 'retenciones-y-percepciones', (M+'retention.py', 'suss|vat|def apply_retention'))
c([26,27,28], 'cobros-y-pagos', (M+'account_payment_order.py', 'def send_email|def render_report'), (R+'retention_certificate.xml', '<template'))
c([30,60], 'retenciones-y-percepciones', (M+'account_move.py', 'def _automatic_perception_calculation|def add_perceptions|def compute_perceptions'))
c([31], 'facturacion-y-comprobantes', (M+'account_move.py', 'def _get_mail_template'), (D+'mail_template.xml', 'account.move'))
c([32], 'multimoneda-y-diferencias', (W+'account_debit_note.py', 'def _prepare_default_values'), (W+'account_move_reversal.py', 'def '))
c([33], 'multimoneda-y-diferencias', (M+'account_payment_order.py', 'payment_rate =|payment_rate_currency_id ='))
c([34], 'retenciones-y-percepciones', (M+'account_move.py', 'def _automatic_internal_taxes_calculation'), (M+'internal_taxes.py', 'class '))
c([35,49], 'cierre-contable-e-inflacion', (M+'fiscal_year_closing.py', 'create_recpam =|create_closing_move ='), (W+'fiscal_year_closing_operation_wizard.py', 'def create_closing_move'))
c([36,37], 'remitos-y-transporte', ('l10n_ar_remito_r/report/remito_r.xml', 'autoimpresor|<template'))
c([38], 'remitos-y-transporte', (R+'stock_picking_report_qweb.xml', '<h1>X'))
c([39], 'cierre-contable-e-inflacion', (M+'account_move.py', 'def _check_closed_journal_moves'))
c([40,41,42,43], 'punto-de-venta', (P+'models/pos_order.py', 'def _generate_pos_order_invoice|def compute_perceptions'), (P+'views/account_report.xml', '<template'))
c([44], 'datos-fiscales-y-padrones', (D+'res_document_type_data.xml', '<record'))
c([45], 'facturacion-y-comprobantes', (D+'res_voucher_type_data.xml', '<record'))
c([46], 'datos-fiscales-y-padrones', (D+'fiscal_position_data.xml', '<record'))
c([47], 'datos-fiscales-y-padrones', (D+'iibb_situation_data.xml', '<record'))
c([48], 'datos-fiscales-y-padrones', (D+'res_city_data.xml', '<record'), (M+'res_country_state.py', 'class '))
c([51], 'datos-fiscales-y-padrones', (M+'res_partner.py', 'def get_data_from_padron_afip'))
c([53,69], 'remitos-y-transporte', (M+'stock_picking.py', 'express_id =|truck_license_plate ='), (M+'res_partner.py', 'express_id ='))
c([55], 'facturacion-y-comprobantes', (W+'account_move_reversal.py', 'def '))
c([56], 'facturacion-y-comprobantes', (M+'account_journal.py', 'def _check_denomination_not_m'), (M+'account_move.py', 'inform_cbu ='))
c([57], 'facturacion-y-comprobantes', (M+'wsfex.py', 'def send_invoice_to_afip|def _get_export_type_tables'))
c([58], 'facturacion-y-comprobantes', (M+'account_move.py', 'def _ensure_fce_values|def _check_must_be_fce'), (M+'wsfecred.py', 'def check_partner_obliged_to_FCE'))
c([61], 'facturacion-y-comprobantes', (M+'account_move.py', 'def _generate_qr_afip_url'))
c([62,63], 'cobros-y-pagos', (M+'account_payment_order.py', 'def compute_advance_payment_retentions|def _prepare_advanced_payment_retention'))
c([64,65], 'cobros-y-pagos', (M+'account_payment_order.py', 'concept_line_ids =|writeoff_amount =|def writeoff_move_line_get'))
c([67,68], 'retenciones-y-percepciones', (M+'retention.py', 'class Retention'), (M+'perception.py', 'class Perception'))
c([70], 'remitos-y-transporte', (W+'cancel_picking_done.py', 'def '), (M+'stock_picking.py', 'renum_pick_id ='))
c([71], 'cierre-contable-e-inflacion', (M+'inflation_index.py', 'coefficient =|date ='))
assign('POS',[1,2,3,4], 'punto-de-venta', (P+'models/pos_order.py','def _generate_pos_order_invoice|def _prepare_invoice_vals'))
assign('POS',[5,9], 'punto-de-venta', (P+'models/pos_order.py','def compute_perceptions'))
assign('POS',[6], 'punto-de-venta', (P+'views/account_report.xml','report_type'), (P+'static/src/js/models.js','get_invoice_report_action'))
assign('POS',[7,8], 'punto-de-venta', (P+'models/pos_config.py','default_invoice_mode'), (P+'static/src/js/payment.js','toggleIsManualInvoice|By default set electronic'))
assign('POS',[10], 'punto-de-venta', (P+'models/pos_config.py','block_invoice_offline'))
assign('POS',[11], 'punto-de-venta', (P+'models/pos_order.py','fiscal_position'))
assign('POS',[12], 'punto-de-venta', (P+'models/pos_order.py','[Ff][Cc][Ee]'), (M+'account_move.py','def _ensure_fce_values'))
assign('POS',[13], 'punto-de-venta', (P+'models/pos_session.py','receivable_account|def _validate_session'))
assign('Cheques',[1,3,6], 'cheques-y-conciliacion', (W+'create_checkbook_wizard.py','checkbook_format =|def create_checkbook'))
assign('Cheques',[2], 'cheques-y-conciliacion', (M+'account_check.py','class AccountCheckConfig'))
assign('Cheques',[4,5,7,8], 'cheques-y-conciliacion', (M+'account_check.py','issued_check_state =|third_party_check_state =|internal_type =|type ='))
assign('Cheques',[9,10,11], 'cheques-y-conciliacion', (M+'account_check.py','def create_debit_note_from_rejected_check|def check_delivered'), (W+'deposit_check_wizard.py','def action_deposit'), (W+'reject_check_wizard.py','def action_reject'))
assign('Cheques',[12], 'cheques-y-conciliacion', (W+'debit_check_wizard.py','active_ids'), (W+'account_check_change_state.py','len\(check_id\)'))
assign('Cheques',[13], 'cheques-y-conciliacion', ('l10n_ar_eynes/views/account_check_views.xml','<calendar'))
assign('Cheques',[14], 'cheques-y-conciliacion', (M+'account_check.py','currency_rate =|currency_id ='))
assign('Cheques',[15], 'cheques-y-conciliacion', ('l10n_ar_reconciliation/models/account_full_reconcile.py','def _update_checks_on_reconcile'), ('l10n_ar_reconciliation/models/account_move_line.py','def '))
assign('Cheques',[16], 'cheques-y-conciliacion', ('print_check/wizard/print_check_wizard.py','class PrintCheckWizard'), ('custom_print_check/wizard/print_check_wizard.py','class PrintCheckWizard'))
assign('Reportes',[1], 'reportes-contables', (W+'account_tax_subjournal.py','grouped =|perception_retention_grouped ='))
assign('Reportes',[2], 'reportes-contables', (W+'sales_by_jurisdiction.py',"'report_type': 'xlsx'"))
assign('Reportes',[3], 'reportes-contables', (R+'libro_diario_report.xml','report_type'))
assign('Reportes',[4], 'reportes-contables', (R+'purchase_vat_report.xml','report_type'))
assign('Reportes',[5], 'reportes-contables', (R+'sale_vat_report.xml','report_type'))
assign('Reportes',[6], 'reportes-contables', (W+'account_tax_subjournal_apportionable.py','class '))
assign('Reportes',[7], 'reportes-contables', (M+'account_move.py','def _generate_qr_afip_url'), (R+'account_move_report.xml','report_type'))
for num,file in [(1,'create_arciba_file'),(2,'arba_retention_exporter'),(3,'create_libro_iva'),(4,'create_libro_iva'),(5,'create_sicore_file'),(6,'create_sifere_file'),(7,'arba_retention_exporter'),(8,'create_iva_per_ret_files')]:
 assign('Exportadores',[num], 'exportadores-impositivos', (W+file+'.py','is_simple_vat' if num==4 else 'class '))
assign('Webservice',[1], 'servicios-arca-y-arba', (M+'wsfe.py','def send_invoice_to_afip'))
assign('Webservice',[2], 'servicios-arca-y-arba', (M+'wsfex.py','def send_invoice_to_afip'))
assign('Webservice',[3,4], 'servicios-arca-y-arba')
assign('Webservice',[5], 'servicios-arca-y-arba', (M+'ws_padron.py','def '))
assign('Webservice',[6], 'servicios-arca-y-arba', (M+'wsfecred.py','def check_partner_obliged_to_FCE'))
assign('Webservice',[7], 'servicios-arca-y-arba', (W+'afip_sinchronize_voucher.py','def '), (W+'wsfe_massive_sinchronize.py','def '))
assign('Webservice',[8], 'servicios-arca-y-arba', (M+'wsfe.py','def get_afip_tables'))
assign('Webservice',[9], 'servicios-arca-y-arba', (M+'arba_a122r.py','def sync_retention_line|def get_comprobante_pdf'))

notes = {
 'Comprobantes-34': 'Motor específico internal_taxes.py localizado en 17 y 19; no en 15. El tratamiento alternativo con impuestos estándar en 15 requiere validación.',
 'POS-8': '15 fija por código la factura electrónica inicial; 17 y 19 incorporan default_invoice_mode configurable.',
 'POS-10': 'block_invoice_offline por posición fiscal localizado en 17 y 19; no en 15. No equivale a facturación electrónica sin conexión.',
 'POS-13': 'La validación explícita de cuentas por método al cierre se localizó en 19; no se verificó un control equivalente en 15 o 17.',
 'Reportes-3': 'Reporte PDF específico localizado en 17 y 19; no en 15 en este repositorio.',
 'Reportes-4': 'Reporte PDF específico localizado en 17 y 19; no en 15. En 19 el menú depende de apportionable_vat.',
 'Reportes-5': 'Reporte PDF específico localizado en 17 y 19; no en 15. En 19 el menú depende de apportionable_vat.',
 'Reportes-6': 'Asistente específico de prorrateo localizado en 17 y 19; no en 15.',
 'Comprobantes-32': 'Se encontraron notas de débito/crédito y multimoneda, pero no un asistente específico de ND/NC por diferencia de cambio. Confirmar flujo o módulo externo.',
 'Comprobantes-37': 'Existe plantilla QWeb de remito R. La modalidad sobre formulario preimpreso requiere definición; no equivale automáticamente a un editor de plantillas.',
 'Comprobantes-48': 'Localidades en datos propios; provincias también dependen de los datos base de Odoo. No se auditó exhaustividad geográfica.',
 'Comprobantes-52': 'Consumidor de un servidor de padrones configurable; tarea cron incluida pero desactivada de fábrica. No implica acceso automático a todos los padrones.',
 'Comprobantes-56': 'Las tres ramas bloquean denominación M en diarios y comprobantes. Separar registro histórico, emisión actual y A con leyenda; no ofrecer emisión M.',
 'Comprobantes-58': 'Hay circuito FCE, pero wsfecred.py no está importado en models/__init__.py de ninguna rama. Verificar consulta de obligatoriedad y alternativa ABC en entorno real.',
 'Comprobantes-59': 'Asistente de recálculo de moneda; no interpretarlo como permiso de alterar una factura ya autorizada por ARCA.',
 'Cheques-12': 'Hay operaciones sobre selecciones múltiples; el asistente genérico de cambio de estado exige un cheque. Evitar prometer todo cambio de estado masivo.',
 'Cheques-15': 'Módulo de conciliación presente en 15 y 19; ausente en 17 en este repositorio. No demuestra ausencia de solución externa.',
 'Cheques-16': 'custom_print_check en 17 y print_check en 19; dependen de sign_oca. No se encontró addon de impresión equivalente en 15.',
 'POS-12': 'El POS usa el circuito de facturación/FCE; aplica el pendiente de WSFECRED. Probar el caso completo antes de anunciarlo por versión.',
 'Reportes-2': 'El Excel dice PDF; la acción encontrada exporta XLSX en las tres ramas. Publicar formato XLSX salvo evidencia adicional.',
 'Webservice-3': 'WSLP figura en Excel. No se encontró implementación o registro de servicio en las tres ramas inspeccionadas.',
 'Webservice-4': 'CAEA figura en Excel. No se encontró implementación o registro de servicio en las tres ramas inspeccionadas. No confundir con CAE.',
 'Webservice-6': 'Existe wsfecred.py y una llamada desde account_move.py, pero falta importarlo en models/__init__.py en las tres ramas. Evidencia parcial.',
}
for topic in topics:
    category, refs = selector[topic['id']]
    topic['ficha'] = category + '.md'
    topic['observacion'] = notes.get(topic['id'], '')
    topic['ramas'] = {}
    for version, source in texts.items():
        evidence = []
        for path, pattern in refs:
            text = source.get(path)
            if text is None:
                continue
            hits = [(i,l.strip()) for i,l in enumerate(text.splitlines(),1) if re.search(pattern,l)]
            for line, fragment in hits[:3]:
                evidence.append({'archivo': path, 'linea': line, 'referencia': fragment})
        topic['ramas'][version] = {'estado': 'referencia_estatica' if evidence else 'sin_evidencia_en_selectores', 'evidencia': evidence}
    if topic['id'] in notes:
        topic['revision_editorial'] = True
save('catalogo-temas.json', topics)

lines = ['# Matriz de los 124 temas del Excel', '', 'Texto original conservado, incluidos duplicados entre hojas. Cada tema apunta a una ficha y a referencias por rama. **Referencia estática** significa que se localizó código relacionado; no certifica funcionamiento, instalación ni cumplimiento normativo. Los pendientes y contradicciones prevalecen sobre la presencia de una referencia.', '', 'Los commits exactos están en [ramas.json](_fuentes/ramas.json). La evidencia completa con archivos y líneas está en [catalogo-temas.json](_fuentes/catalogo-temas.json).', '']
for sheet in sheets:
    lines += ['## ' + sheet['nombre'], '', '| ID / celda | Tema original | Ficha | 15.0 | 17.0 | 19.0 | Observación |', '|---|---|---|---|---|---|---|']
    for t in [t for t in topics if t['hoja']==sheet['nombre']]:
        cols = [t['id'] + ' / A' + str(t['fila']), t['texto_original'].strip(), f"[Ver ficha]({t['ficha']})"]
        for v in branches:
            ev=t['ramas'][v]['evidencia']
            cols.append(('Ref. `' + ev[0]['archivo'].split('/')[-1] + ':' + str(ev[0]['linea']) + '`') if ev else 'Sin localizar')
        cols.append(' '.join([t['nota_original'],t['observacion']]).strip() or 'Referencia estática; validar configuración del caso.')
        lines.append('| ' + ' | '.join(c.replace('|','\\|').replace('\n',' ') for c in cols) + ' |')
    lines.append('')
(HERE.parent/'matriz-excel.md').write_text('\n'.join(lines)+'\n')
print(f'{len(topics)} temas; '+', '.join(f'{v}: {len(b["modulos"])} módulos' for v,b in branches.items()))
for t in topics:
    missing = [v for v in branches if not t['ramas'][v]['evidencia']]
    if missing: print(t['id'], 'sin evidencia en selectores:', ', '.join(missing))

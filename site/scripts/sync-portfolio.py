"""Generate site content from the authoritative workbook using Python's standard library."""
import json
import re
import unicodedata
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / 'content'
SOURCE = CONTENT / 'eynes_portfolio_rubros_consolidado.xlsx'
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def slug(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')

with zipfile.ZipFile(SOURCE) as archive:
    strings = []
    if 'xl/sharedStrings.xml' in archive.namelist():
        strings = [''.join(el.itertext()) for el in ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('m:si', NS)]
    rows = []
    for row in ET.fromstring(archive.read('xl/worksheets/sheet1.xml')).findall('m:sheetData/m:row', NS)[1:]:
        values = dict.fromkeys('ABCDEFGHIJKLMNOPQRS', '')
        for cell in row:
            column = re.sub(r'\d', '', cell.attrib['r'])
            value = cell.find('m:v', NS)
            value = value.text if value is not None else ''
            if cell.get('t') == 's':
                value = strings[int(value)]
            elif cell.get('t') == 'inlineStr':
                value = ''.join(cell.find('m:is', NS).itertext())
            values[column] = value or ''
        if values['A'].strip():
            rows.append(values)

notes = []
def clean(value, row, column):
    if '[REVISAR]' not in value:
        return value.strip()
    notes.append({'empresa': row['A'], 'columna': column, 'texto': value})
    if column == 'S':
        return '\n\n'.join(block for block in re.split(r'\n\s*\n', value) if '[REVISAR]' not in block)
    # Pending instructions occupy the rest of the cell; keep the confirmed prefix.
    return value.split('[REVISAR]')[0].strip().removesuffix('Resultado:').strip()

raw_rows = rows
rows = [{key: clean(value, row, key) for key, value in row.items()} for row in rows]

def faqs(value):
    result = []
    for item in re.split(r'(?:^|\n)\s*\d+\s*[-.)]\s*', value):
        if not item.strip():
            continue
        question, sep, answer = item.strip().partition('\n')
        if not sep or not answer.strip():
            notes.append({'empresa': 'FAQ', 'columna': 'S', 'texto': item})
            continue
        result.append({'pregunta': question.strip(), 'respuesta': answer.strip()})
    return result

def section(number, title, body):
    return f'\n## {number} — {title}\n\n{body}\n' if body else ''

# The 4 module pages that actually exist under content/03-modulos — keywords
# are matched against the free-text "Módulos relevantes" column to link only
# to real pages (order fixed so the resulting list reads consistently).
MODULE_KEYWORDS = [
    ('ventas-y-crm', ('venta', 'crm')),
    ('inventario', ('inventario', 'stock')),
    ('compras', ('compra',)),
    ('contabilidad-y-finanzas', ('contabilidad', 'facturaci', 'finanza')),
]

def modulo_slugs(text):
    lowered = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().lower()
    return [slug for slug, keywords in MODULE_KEYWORDS if any(k in lowered for k in keywords)]

def integracion_labels(members, columns, limit=6):
    labels = []
    for row in members:
        for column in columns:
            value = row[column]
            if not value:
                continue
            label = value.split('.', 1)[0].strip().rstrip('.')
            if label and label.lower() not in (l.lower() for l in labels):
                labels.append(label)
    return labels[:limit]

def write(folder, name, meta, body):
    path = CONTENT / folder / (name + '.md')
    path.write_text('---\n' + '\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in meta.items()) + '\n---\n' + body)
    generated.add(str(path.relative_to(CONTENT)))

generated = set()
groups = {}
for row in rows:
    groups.setdefault(row['B'], []).append(row)
    name = slug(row['A'])
    testimony = re.split(r'EL DESAFÍO\s*|LA SOLUCIÓN\s*|EL RESULTADO\s*', row['R'])
    result = testimony[3].strip().strip('"') if len(testimony) == 4 else ''
    meta = dict(title=row['A'] + ': Odoo para ' + row['B'], seo_title=row['A'] + ' | Casos de Odoo | Eynes', meta_description=row['D'][:155], slug=name, estado='publicado', schema_type='Article', cliente=row['A'], rubro=row['B'], pais='', usuarios='', modulos_implementados=[], resultado_clave=result, agrupador=row['C'], portfolio=True)
    body = section('03', 'El problema', row['D'])
    body += section('04', 'La implementación', row['P'])
    body += section('05', 'Testimonio', row['R'])
    body += section('06', 'Módulos relevantes para el rubro', row['K'])
    body += section('07', 'Integraciones del rubro', '\n\n'.join(row[k] for k in 'LMNO' if row[k]))
    body += section('08', 'Otros casos del rubro', row['Q'])
    body += section('09', 'Problemas específicos del rubro', '\n\n'.join('### ' + row[a] + '\n\n' + row[b] for a,b in [('E','F'),('G','H'),('I','J')] if row[a] or row[b]))
    meta['faqs'] = faqs(row['S'])
    write('04-casos-de-exito', name, meta, body)

for rubro, members in groups.items():
    first = members[0]
    modulos_text = ' '.join(dict.fromkeys(r['K'] for r in members if r['K']))
    meta = dict(title=rubro, seo_title='Odoo para ' + rubro + ' | Eynes', meta_description='Problemas, módulos, integraciones y experiencias de implementación de Odoo para ' + rubro + '.', slug=slug(rubro), estado='publicado', schema_type='Service', agrupador=first['C'], portfolio=True, casos_relacionados=[slug(r['A']) for r in members], modulos_relevantes=modulo_slugs(modulos_text), integraciones_destacadas=integracion_labels(members, 'LMNO'), faqs=[])
    for row in members:
        for faq in faqs(row['S']):
            if faq not in meta['faqs']:
                meta['faqs'].append(faq)
    def unique_values(columns):
        return list(dict.fromkeys(r[k] for r in members for k in columns if r[k]))
    problems = list(dict.fromkeys('### ' + r[a] + '\n\n' + r[b] for r in members for a,b in [('E','F'),('G','H'),('I','J')] if r[a] or r[b]))
    body = section('01', 'Hero', '**Subtítulo:** ' + first['C'].capitalize())
    body += section('02', 'Problemas específicos del rubro', '\n\n'.join(problems))
    body += section('03', 'Módulos relevantes', '\n\n'.join(unique_values('K')))
    body += section('03a', 'Integraciones', '\n\n'.join(unique_values('LMNO')))
    write('02-verticales', slug(rubro), meta, body)

# Keep previous editorial pages for reference, but remove them from public listings.
for folder in ['02-verticales', '04-casos-de-exito']:
    for path in (CONTENT / folder).glob('*.md'):
        if path.name.startswith('_') or str(path.relative_to(CONTENT)) in generated:
            continue
        text = path.read_text()
        text = re.sub(r'^estado:.*', 'estado: "borrador"', text, count=1, flags=re.M)
        path.write_text(text)

(CONTENT / 'portfolio-revision.json').write_text(json.dumps(notes, ensure_ascii=False, indent=2) + '\n')
(CONTENT / 'portfolio-fuente.json').write_text(json.dumps(raw_rows, ensure_ascii=False, indent=2) + '\n')
print(f'Portfolio: {len(rows)} empresas, {len(groups)} rubros, {len(notes)} campos pendientes de revisión.')

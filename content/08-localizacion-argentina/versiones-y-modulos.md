# Versiones, módulos y dependencias

Comparación estática de referencias locales al 10 de septiembre de 2026. No se hizo fetch ni se ejecutó Odoo. “Presente” describe el repositorio; no una instalación certificada.

## Commits inspeccionados

| Rama | Commit | Fecha del commit | Módulos con manifiesto |
|---|---|---|---|
| `origin/15.0` | `a465fcca8a04432a93a16afcc8d231ea10b4e942` | 2026-09-10T14:20:09Z | 5 |
| `origin/17.0` | `8d4124ac509f8506591de30658c3f737744aab72` | 2026-09-09T18:24:41Z | 8 |
| `origin/19.0` | `9db4fefd896a6cc9353d2d32c7c6f0a947a1572c` | 2026-09-10T14:35:35Z | 7 |

## Módulos por rama

Si no se declara `installable`, se indica expresamente. No se interpreta esa omisión como una prueba de instalación.

| Módulo | 15.0 | 17.0 | 19.0 |
|---|---|---|---|
| `custom_print_check` | No localizado | `17.0.0.0.2` · installable no declarado | No localizado |
| `customer_balance_history` | No localizado | `17.0.1.0.0` · instalable en manifiesto | No localizado |
| `l10n_ar_eynes` | `15.0.2.13.1` · instalable en manifiesto | `17.0.4.7.6` · instalable en manifiesto | `19.0.0.2.0` · instalable en manifiesto |
| `l10n_ar_padron_ws_consumer` | `15.0.2.0.6` · instalable en manifiesto | `17.0.0.0.0` · instalable en manifiesto | `19.0.0.0.0` · instalable en manifiesto |
| `l10n_ar_pos_wsfe` | `15.0.2.2.0` · instalable en manifiesto | `17.0.1.3.0` · instalable en manifiesto | `19.0.1.3.0` · instalable en manifiesto |
| `l10n_ar_reconciliation` | `15.0.0.0.1` · instalable en manifiesto | No localizado | `19.0.0.0.1` · instalable en manifiesto |
| `l10n_ar_remito_cai` | No localizado | `17.0.1.0.0` · instalable en manifiesto | No localizado |
| `l10n_ar_remito_r` | `15.0.1.0.0` · instalable en manifiesto | `17.0.1.0.0` · instalable en manifiesto | `19.0.1.0.0` · instalable en manifiesto |
| `l10n_ar_taxes_report` | No localizado | `17.0.1.0.1` · instalable en manifiesto | `19.0.1.0.0` · no instalable |
| `print_check` | No localizado | No localizado | `19.0.0.0.0` · installable no declarado |

## Qué aporta cada módulo

| Módulo | Función localizada |
|---|---|
| `l10n_ar_eynes` | Núcleo fiscal, comprobantes, tesorería, impuestos, cheques, reportes, exportadores, cierre y servicios |
| `l10n_ar_padron_ws_consumer` | Consulta a servidor de padrones y actualización de información fiscal por contacto |
| `l10n_ar_pos_wsfe` | Facturación e impuestos dentro del POS |
| `l10n_ar_remito_r` | Plantilla R y datos de autoimpresor y bultos |
| `l10n_ar_reconciliation` | Actualización contable/de estado de cheques ligada a conciliación |
| `l10n_ar_remito_cai` | Talonarios, rangos, vencimientos y asignación CAI a remitos en 17 |
| `l10n_ar_taxes_report` | Reportes DDJJ IVA e IIBB; no instalable en 19 |
| `customer_balance_history` | Cuenta corriente y composición de saldos de clientes/proveedores en 17 |
| `custom_print_check` / `print_check` | Impresión de cheques sobre plantilla en 17/19 respectivamente |

## Diferencias funcionales localizadas

| Capacidad | 15.0 | 17.0 | 19.0 |
|---|---|---|---|
| WSFE / WSFEX / CAE / QR | Código presente | Código presente | Código presente |
| WSFECRED | Archivo sin import de modelo | Archivo sin import de modelo | Archivo sin import de modelo |
| WSLP / CAEA | Sin implementación localizada | Sin implementación localizada | Sin implementación localizada |
| ARBA A122R Digital | Presente | Presente | Presente |
| Exportador TXT de retenciones ARBA: bloqueo por `arba_a122r_enforced` | No localizado en ese asistente | No localizado en ese asistente | Presente |
| Composición de saldos pendientes | Módulo no localizado | Residuales actuales, PDF y XLS/HTML | Módulo no localizado |
| Confirmación de cierre sin asiento RECPAM | `action_confirm` exige RECPAM | `action_confirm` exige RECPAM | `action_confirm` exige RECPAM |
| Impuestos internos: motor específico | No localizado | Presente | Presente |
| Libro Diario e IVA Compras/Ventas PDF | No localizados aquí | Presentes, revisar visibilidad de menús de IVA | Presentes, revisar visibilidad de menús de IVA |
| IVA prorrateable: asistente específico | No localizado | Presente | Presente |
| Subdiario IVA XLSX / jurisdicciones XLSX | Presentes | Presentes | Presentes |
| Libro IVA / IVA Simple | Modalidad en asistente | Modalidad en asistente | Modalidad en asistente |
| Libro IVA: selector TXT/XLSX | No localizado | Presente | Presente |
| SIRCAR / SIPOT / SIRETPER / Misiones | No localizados | Presentes y registrados | No localizados |
| POS: selección electrónica/interna | Presente | Presente | Presente |
| POS: modalidad inicial | Electrónica fijada en JS | Configurable | Configurable |
| POS: bloqueo offline por posición | Campo no localizado | Presente | Presente |
| POS: control específico de cuentas al cierre | No localizado | No localizado | Presente |
| Denominación M para nueva emisión | Bloqueada por restricción | Bloqueada por restricción | Bloqueada por restricción |

## Dependencias declaradas

Estas listas identifican piezas requeridas por el código. No son una guía de instalación validada ni una garantía de disponibilidad de esas dependencias para la rama. No reducir el producto a “sin terceros”: los manifiestos incluyen componentes de Odoo, OCA y otros addons.

### 15.0

- `l10n_ar_eynes`: `account`, `account_debit_note`, `base`, `contacts`, `date_range`, `delivery`, `hr`, `mail`, `month_year_widget`, `multi_step_wizard`, `om_fiscal_year`, `popup_messages`, `purchase`, `report_xlsx`, `report_xlsx_helper`, `sale`, `stock`, `uom`, `web_domain_field`, `web_notify`, `report_qweb_element_page_visibility`.
- `l10n_ar_padron_ws_consumer`: `base`, `contacts`, `l10n_ar_eynes`, `month_year_widget`.
- `l10n_ar_pos_wsfe`: `l10n_ar_eynes`, `point_of_sale`.
- `l10n_ar_reconciliation`: `l10n_ar_eynes`, `account_reconciliation_widget`.
- `l10n_ar_remito_r`: `base`, `contacts`, `stock`, `l10n_ar_eynes`.

Bibliotecas Python declaradas por el núcleo: `M2Crypto`, `OpenSSL`, `qrcode`, `httplib2`, `future`, `pysimplesoap`, `pyafipws`.

### 17.0

- `custom_print_check`: `l10n_ar_eynes`, `sign_oca`.
- `customer_balance_history`: `account`, `contacts`, `sale`, `l10n_ar_eynes`.
- `l10n_ar_eynes`: `account`, `account_debit_note`, `base`, `base_address_extended`, `base_import`, `contacts`, `delivery`, `hr`, `mail`, `multi_step_wizard`, `om_fiscal_year`, `popup_messages`, `purchase`, `report_xlsx`, `report_xlsx_helper`, `sale`, `stock_delivery`, `uom`, `web_notify`, `report_qweb_element_page_visibility`.
- `l10n_ar_padron_ws_consumer`: `base`, `contacts`, `l10n_ar_eynes`.
- `l10n_ar_pos_wsfe`: `l10n_ar_eynes`, `point_of_sale`.
- `l10n_ar_remito_cai`: `l10n_ar_eynes`, `l10n_ar_remito_r`, `stock`.
- `l10n_ar_remito_r`: `base`, `contacts`, `stock`, `l10n_ar_eynes`.
- `l10n_ar_taxes_report`: `l10n_ar_eynes`.

Bibliotecas Python declaradas por el núcleo: `M2Crypto`, `OpenSSL`, `qrcode`, `httplib2`, `future`, `pysimplesoap`, `pyafipws`, `beautifulsoup4`.

### 19.0

- `l10n_ar_eynes`: `account`, `account_debit_note`, `base`, `base_address_extended`, `base_import`, `contacts`, `delivery`, `hr`, `mail`, `month_year_widget`, `multi_step_wizard`, `om_fiscal_year`, `popup_messages`, `purchase`, `report_xlsx`, `report_xlsx_helper`, `sale`, `stock_delivery`, `uom`, `web_notify`, `report_qweb_element_page_visibility`.
- `l10n_ar_padron_ws_consumer`: `base`, `contacts`, `l10n_ar_eynes`.
- `l10n_ar_pos_wsfe`: `l10n_ar_eynes`, `point_of_sale`.
- `l10n_ar_reconciliation`: `l10n_ar_eynes`.
- `l10n_ar_remito_r`: `base`, `contacts`, `stock`, `l10n_ar_eynes`.
- `l10n_ar_taxes_report`: `l10n_ar_eynes`.
- `print_check`: `l10n_ar_eynes`, `sign_oca`.

Bibliotecas Python declaradas por el núcleo: `M2Crypto`, `OpenSSL`, `qrcode`, `httplib2`, `future`, `pysimplesoap`, `pyafipws`.

## Evidencia adicional que no figura como tema aislado en el Excel

| Capacidad | Rama / fuente | Uso documental |
|---|---|---|
| COT y datos de traslado | Tres ramas: `l10n_ar_eynes/models/stock_picking.py`, `cot_remit`, `do_cot_file` | Ampliar remitos con condición de configuración/prueba del servicio |
| Certificados y autenticación | Tres ramas: `models/certificate_request.py`, `models/wsaa.py` del núcleo | Explicar requisitos de conexión; no copiar certificados ni claves |
| Diagnóstico y reproceso ARBA | Tres ramas: `wizard/arba_a122r_diagnostic_wizard.py`, `wizard/arba_a122r_reprocess_wizard.py` | Explicar trazabilidad y recuperación de operaciones |
| Recuperación de PDF ARBA | Tres ramas: `models/arba_a122r.py` | Separar comprobante remoto de certificado local |
| Exclusiones y límites temporales | Tres ramas: `models/res_partner.py`, `models/retention.py` | Explicar cálculo basado en datos del contacto/período |
| Mapeo de cuentas de cierre | Tres ramas: `models/account_mapping_fiscal_year_closing.py` | Explicar configuración contable del proceso |

## Uso correcto de la comparación

No interpretar “no localizado” como imposibilidad: la funcionalidad puede vivir en otro repositorio o módulo no inspeccionado. Tampoco interpretar que una función esté en 17 como prueba de que ya esté portada a 19. Para una propuesta comercial, seleccionar rama, commit y módulos y validar el circuito completo.

Las rutas, imports, campos y métodos se pueden contrastar en los índices de `_fuentes`. Los manifiestos completos en forma estructurada están en [ramas.json](_fuentes/ramas.json).

---
title: "Remitos y datos de transporte en Odoo"
seo_title: "Remitos y datos de transporte en Odoo | Eynes"
meta_description: "Generá la documentación de entrega desde el movimiento de stock, con numeración, transportista y datos de la mercadería."
slug: "remitos-y-transporte"
url: "/localizacion-argentina/remitos-y-transporte"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Operar y cerrar"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿El remito toma los productos de la entrega?", "respuesta": "Las plantillas se generan sobre la transferencia de stock y sus datos asociados."}, {"pregunta": "¿El sistema obtiene la autorización de autoimpresor?", "respuesta": "No se acreditó esa gestión. La plantilla utiliza datos de autorización configurados en la empresa."}, {"pregunta": "¿Los talonarios CAI están en todas las versiones?", "respuesta": "El addon específico de rangos y vigencias se encontró en 17. Su disponibilidad en otras versiones debe confirmarse."}]
---

## 01 — Texto para el sitio

Generá la documentación de entrega desde el movimiento de stock, con numeración, transportista y datos de la mercadería.

## 02 — El problema que resuelve

Preparar el remito por fuera del depósito obliga a volver a escribir destinatario, productos y transporte. La localización extiende la transferencia de stock para que la documentación use los datos de la entrega.

## 03 — Alcance funcional

- Remito X desde el núcleo de localización, con plantilla de impresión propia.
- Remito R mediante `l10n_ar_remito_r`, con bultos y datos de autoimpresor, autorización y vencimiento configurados en la empresa.
- Expreso/transportista, patente de camión y remolque, valor declarado, fechas y otros datos del traslado.
- Cancelación y renumeración mediante asistente, conservando campos de número original y referencia a otro movimiento.
- Gestión de talonarios CAI por rangos, vencimiento y diario en el módulo adicional de 17; asignación al remito y controles de rangos superpuestos.
- Funciones para construir y enviar el archivo COT, con campos de respuesta y configuración del servicio, encontradas en el núcleo.

## 04 — Diferencias por versión

Remito R y X aparecen en las tres ramas. `l10n_ar_remito_cai` se encontró solamente en 17, depende de la localización, Remito R y stock. El COT está en `stock_picking.py`; no se probó el servicio externo ni el formato contra un organismo.

## 05 — Condiciones y límites del mensaje

“Remito R sobre plantilla” en el Excel requiere aclarar si significa formulario preimpreso, diseño QWeb o editor de formularios. No prometer las tres variantes. El módulo no otorga autorización de autoimpresor. Los campos de autorización se cargan; su validez no se comprueba por encontrar la plantilla. El COT requiere una prueba específica de conexión y datos.

## 06 — Demostración sugerida

Validar una entrega de prueba, revisar bultos y transportista e imprimir R/X. En 17, asignar un talonario CAI vigente y mostrar el control ante un rango agotado. Preparar un escenario COT separado.

## 07 — Temas del Excel vinculados

- `Comprobantes-36` · Impresión remito R autoimpresores
- `Comprobantes-37` · Impresión remito R sobre plantilla (ver bien como describir esto)
- `Comprobantes-38` · Impresión remito X
- `Comprobantes-53` · Transportistas y expresos en la ficha del contacto
- `Comprobantes-69` · Datos de transporte en el remito
- `Comprobantes-70` · Cancelación y renumeración de remitos validados

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/res_partner.py:84`
- `l10n_ar_eynes/models/stock_picking.py:27`
- `l10n_ar_eynes/report/stock_picking_report_qweb.xml:59`
- `l10n_ar_eynes/wizard/cancel_picking_done.py:35`
- `l10n_ar_remito_r/report/remito_r.xml:250`

### Rama 17.0

- `l10n_ar_eynes/models/res_partner.py:83`
- `l10n_ar_eynes/models/stock_picking.py:27`
- `l10n_ar_eynes/report/stock_picking_report_qweb.xml:59`
- `l10n_ar_eynes/wizard/cancel_picking_done.py:37`
- `l10n_ar_remito_r/report/remito_r.xml:251`

### Rama 19.0

- `l10n_ar_eynes/models/res_partner.py:82`
- `l10n_ar_eynes/models/stock_picking.py:27`
- `l10n_ar_eynes/report/stock_picking_report_qweb.xml:59`
- `l10n_ar_eynes/wizard/cancel_picking_done.py:37`
- `l10n_ar_remito_r/report/remito_r.xml:250`

**Ampliación de código:** `l10n_ar_eynes/models/stock_picking.py` (`cot_remit`, `get_remit_vals`, `cot_product`, `do_cot_file`) en las tres ramas; `l10n_ar_remito_cai/models/account_journal.py` y `models/stock_picking.py` en 17.

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

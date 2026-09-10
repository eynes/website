---
title: "Reportes contables e impositivos argentinos"
seo_title: "Reportes contables e impositivos argentinos | Eynes"
meta_description: "Prepará libros y reportes desde los comprobantes registrados, con detalle de impuestos y opciones de agrupación para revisar la información."
slug: "reportes-contables"
url: "/localizacion-argentina/reportes-contables"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Operar y cerrar"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿El reporte por jurisdicción se descarga en PDF?", "respuesta": "La implementación localizada genera XLSX. El PDF mencionado en el Excel queda pendiente de evidencia adicional."}, {"pregunta": "¿Puedo agrupar facturas B?", "respuesta": "El subdiario incluye agrupación por día e impuesto, con un umbral configurable de importe."}, {"pregunta": "¿Generar el reporte presenta la declaración?", "respuesta": "No. Reportes, archivos exportables y envío a un organismo son pasos distintos."}]
---

## 01 — Texto para el sitio

Prepará libros y reportes desde los comprobantes registrados, con detalle de impuestos y opciones de agrupación para revisar la información.

## 02 — El problema que resuelve

La preparación de IVA suele terminar en varias planillas para separar alícuotas, percepciones y operaciones por jurisdicción. Los reportes reúnen la información de los comprobantes y permiten elegir períodos y criterios de presentación.

## 03 — Alcance funcional

- Subdiario IVA Compras/Ventas en XLSX con detalle de impuestos y opciones de agrupación de percepciones/retenciones.
- Agrupación de facturas B por día e impuesto, con límite de importe configurable; no una consolidación incondicional de todas las facturas B.
- Compras y ventas por jurisdicción en XLSX, con período y compañías.
- Libro Diario e IVA Compras/Ventas en PDF en 17 y 19.
- Subdiario con IVA prorrateable en 17 y 19, asociado a configuración de la compañía.
- PDF de factura y QR desde el circuito de facturación.
- Reportes de DDJJ IVA e IIBB en módulo separado: presentes en 17 y 19, pero no instalables en el manifiesto de 19.
- Reportes de cuenta corriente por período y composición de saldos pendientes actuales en el módulo de 17 documentado en su propia ficha.

## 04 — Diferencias por versión

El XLSX de subdiario y el de jurisdicciones están en las tres ramas. No se localizaron los reportes PDF específicos de Libro Diario, IVA Compras/Ventas ni el asistente de prorrateo en 15. `l10n_ar_taxes_report` es instalable en 17 y está marcado `installable: False` en 19.

## 05 — Condiciones y límites del mensaje

La fila “Compras y ventas por jurisdicción PDF” del Excel contradice el formato XLSX encontrado: usar XLSX en la descripción. En 17 y 19, `ir_ui_menu.py` oculta menús de IVA Compras/Ventas si la compañía no activa IVA prorrateable. Generar un reporte no equivale a presentar una declaración jurada.

## 06 — Demostración sugerida

Exportar un período con facturas A/B, percepciones y notas de crédito. Comparar detalle y agrupación. Mostrar el reporte por jurisdicción en XLSX. Demostrar prorrateo y PDFs sobre una compañía y versión configuradas para ese circuito.

## 07 — Temas del Excel vinculados

- `Reportes-1` · Excel subdiario de IVA Compras / IVA Ventas con detalle de percepciones y otros impuestos - con agrupamiento de tipo de impuestos - Agrupamiento de facturas B por día
- `Reportes-2` · Compras y ventas por jurisdicción PDF
- `Reportes-3` · Libro Diario PDF
- `Reportes-4` · Libro IVA Compras PDF
- `Reportes-5` · Libro IVA Ventas PDF
- `Reportes-6` · Subdiario de IVA con prorrateo
- `Reportes-7` · Factura legal en PDF con QR de AFIP

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/account_move.py:2037`
- `l10n_ar_eynes/report/account_move_report.xml:23`
- `l10n_ar_eynes/wizard/account_tax_subjournal.py:43`
- `l10n_ar_eynes/wizard/sales_by_jurisdiction.py:59`

### Rama 17.0

- `l10n_ar_eynes/models/account_move.py:1993`
- `l10n_ar_eynes/report/account_move_report.xml:23`
- `l10n_ar_eynes/report/libro_diario_report.xml:23`
- `l10n_ar_eynes/report/purchase_vat_report.xml:23`
- `l10n_ar_eynes/report/sale_vat_report.xml:23`
- `l10n_ar_eynes/wizard/account_tax_subjournal.py:70`
- `l10n_ar_eynes/wizard/account_tax_subjournal_apportionable.py:47`
- `l10n_ar_eynes/wizard/sales_by_jurisdiction.py:65`

### Rama 19.0

- `l10n_ar_eynes/models/account_move.py:1952`
- `l10n_ar_eynes/report/account_move_report.xml:23`
- `l10n_ar_eynes/report/libro_diario_report.xml:23`
- `l10n_ar_eynes/report/purchase_vat_report.xml:23`
- `l10n_ar_eynes/report/sale_vat_report.xml:23`
- `l10n_ar_eynes/wizard/account_tax_subjournal.py:70`
- `l10n_ar_eynes/wizard/account_tax_subjournal_apportionable.py:47`
- `l10n_ar_eynes/wizard/sales_by_jurisdiction.py:65`

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

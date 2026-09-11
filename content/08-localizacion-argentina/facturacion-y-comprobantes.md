---
title: "Facturación argentina integrada con Odoo"
seo_title: "Facturación argentina integrada con Odoo | Eynes"
meta_description: "Emití comprobantes desde tu operación de ventas, con puntos de venta, numeración y datos fiscales conectados a la contabilidad."
slug: "facturacion-y-comprobantes"
url: "/localizacion-argentina/facturacion-y-comprobantes"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Facturar y vender"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿Cada punto de venta tiene su numeración?", "respuesta": "La localización define secuencias por diario y clase de comprobante, incluyendo notas y documentos FCE."}, {"pregunta": "¿Se pueden emitir comprobantes de exportación?", "respuesta": "El repositorio contiene integración WSFEX y datos específicos de exportación. La operación requiere configurar ese servicio y sus catálogos."}, {"pregunta": "¿Una factura interna ya está autorizada por ARCA?", "respuesta": "No. El sistema distingue comprobantes internos de los que se envían al servicio de autorización electrónica."}]
---

## 01 — Texto para el sitio

Emití comprobantes desde tu operación de ventas, con puntos de venta, numeración y datos fiscales conectados a la contabilidad.

## 02 — El problema que resuelve

Facturar por fuera del sistema obliga a volver a cargar clientes, importes y comprobantes. También separa la autorización electrónica del documento que ve administración. La localización incorpora ese circuito dentro de Odoo.

## 03 — Alcance funcional

- Diarios y puntos de venta para comprobantes electrónicos e internos, con secuencias independientes para facturas, notas de crédito, notas de débito y documentos FCE.
- Autorización electrónica por WSFE, almacenamiento de CAE y vencimiento, solicitudes y respuestas vinculadas al comprobante.
- PDF de factura con datos fiscales y QR; selección de plantilla para envío por correo.
- Exportaciones mediante WSFEX: tipo de exportación, país de destino, CUIT de destino, permisos de embarque y catálogos auxiliares según la operación.
- Circuito de Factura de Crédito Electrónica MiPyME: tipos, secuencias, datos bancarios y opcionales. La consulta de obligatoriedad por WSFECRED tiene un pendiente técnico específico.
- Catálogo de documentos históricos y campos para leyendas y datos bancarios; no todos los tipos del catálogo son admisibles para nueva emisión.


## 04 — Diferencias por versión

WSFE, WSFEX, CAE, QR, notas y lógica FCE están localizados en las tres ramas. Todas incluyen la restricción `_check_denomination_not_m`. En las tres existe `wsfecred.py`, pero no figura en `models/__init__.py`: la presencia del archivo no alcanza para afirmar que la consulta WSFECRED esté operativa.

## 05 — Condiciones y límites del mensaje

Un comprobante interno no equivale a una factura electrónica autorizada. No ofrecer emisión M: el código la bloquea. Tampoco describir CAEA como disponible a partir del soporte de CAE. La impresión de un PDF y su autorización son pasos diferentes. Para FCE, validar el circuito con la configuración real y el mecanismo de consulta de obligatoriedad antes de publicarlo como demostración.

## 06 — Demostración sugerida

Crear una factura desde una venta, mostrar punto de venta y numeración, autorizarla en homologación y revisar CAE, QR y PDF. Generar una nota asociada. Demostrar WSFEX y FCE como escenarios separados, con sus datos específicos.

## 07 — Temas del Excel vinculados

- `Comprobantes-7` · Puntos de venta para facturas electrónicas
- `Comprobantes-8` · Puntos de venta para carga de facturas internas
- `Comprobantes-9` · Gestión de notas de débito
- `Comprobantes-31` · Envío de facturas por mail
- `Comprobantes-45` · Tipos de comprobante de AFIP precargados
- `Comprobantes-54` · Numeración independiente por punto de venta y tipo de comprobante
- `Comprobantes-55` · Gestión de notas de crédito
- `Comprobantes-56` · Facturas M y facturas A con leyenda
- `Comprobantes-57` · Facturas y notas de exportación
- `Comprobantes-58` · Factura de Crédito Electrónica MiPyME (FCE)
- `Comprobantes-61` · Código QR de AFIP en la factura

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/data/mail_template.xml:139`
- `l10n_ar_eynes/data/res_voucher_type_data.xml:20`
- `l10n_ar_eynes/models/account_journal.py:242`
- `l10n_ar_eynes/models/account_move.py:2037`
- `l10n_ar_eynes/models/wsfecred.py:40`
- `l10n_ar_eynes/models/wsfex.py:686`
- `l10n_ar_eynes/wizard/account_debit_note.py:23`
- `l10n_ar_eynes/wizard/account_move_reversal.py:26`

### Rama 17.0

- `l10n_ar_eynes/data/mail_template.xml:135`
- `l10n_ar_eynes/data/res_voucher_type_data.xml:20`
- `l10n_ar_eynes/models/account_journal.py:243`
- `l10n_ar_eynes/models/account_move.py:1993`
- `l10n_ar_eynes/models/wsfecred.py:40`
- `l10n_ar_eynes/models/wsfex.py:686`
- `l10n_ar_eynes/wizard/account_debit_note.py:29`
- `l10n_ar_eynes/wizard/account_move_reversal.py:26`

### Rama 19.0

- `l10n_ar_eynes/data/mail_template.xml:135`
- `l10n_ar_eynes/data/res_voucher_type_data.xml:20`
- `l10n_ar_eynes/models/account_journal.py:234`
- `l10n_ar_eynes/models/account_move.py:1952`
- `l10n_ar_eynes/models/wsfecred.py:40`
- `l10n_ar_eynes/models/wsfex.py:686`
- `l10n_ar_eynes/wizard/account_debit_note.py:29`
- `l10n_ar_eynes/wizard/account_move_reversal.py:26`

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

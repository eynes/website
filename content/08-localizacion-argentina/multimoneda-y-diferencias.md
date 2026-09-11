---
title: "Comprobantes y pagos en moneda extranjera"
seo_title: "Comprobantes y pagos en moneda extranjera | Eynes"
meta_description: "Trabajá con moneda y cotización por comprobante, y conservá la relación entre lo facturado, lo cobrado y su expresión contable."
slug: "multimoneda-y-diferencias"
url: "/localizacion-argentina/multimoneda-y-diferencias"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Operar y cerrar"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿Puedo indicar un tipo de cambio por factura?", "respuesta": "La localización incluye cotización en comprobantes de clientes y proveedores, y en recibos y órdenes de pago."}, {"pregunta": "¿El cambio de moneda recalcula los importes?", "respuesta": "El asistente recalcula al cambiar de moneda. Si mantenés la misma moneda, retorna sin actualizar su cotización. Los estados permitidos requieren validar el circuito de facturación."}, {"pregunta": "¿Esto equivale a llevar dos contabilidades completas?", "respuesta": "No se puede concluir eso a partir de los campos de segunda moneda. Ese alcance debe definirse y validarse por separado."}]
---

## 01 — Texto para el sitio

Trabajá con moneda y cotización por comprobante, y conservá la relación entre lo facturado, lo cobrado y su expresión contable.

## 02 — El problema que resuelve

Una factura en moneda extranjera y un pago posterior pueden usar cotizaciones distintas. Si esa información vive fuera del sistema, resulta difícil reconstruir el saldo y explicar las diferencias. La localización agrega datos y recálculos específicos al comprobante y al pago.

## 03 — Alcance funcional

- Cotización en facturas de clientes y proveedores; validación de tipo de cambio antes de confirmar.
- Moneda y cotización en recibos y órdenes de pago, con importes de líneas expresados en la moneda correspondiente.
- Campos de segunda moneda y totales convertidos en los comprobantes.
- Asistente para cambiar la moneda de una factura y recalcular importes usando las cotizaciones de origen y destino. Si la moneda elegida es la misma, retorna sin cambios; no sirve para actualizar solo su cotización.
- El Excel incluye ND/NC por diferencia de cambio; se conservó como alcance declarado pendiente de localizar un flujo específico.


## 04 — Diferencias por versión

Cotización de comprobantes, pagos y asistente de cambio de moneda están presentes en 15, 17 y 19. No se certificó equivalencia entre sus cálculos. El campo de segunda moneda no demuestra por sí solo contabilidad completa en dos monedas funcionales.

## 05 — Condiciones y límites del mensaje

No anunciar “contabilidad bimonetaria completa” ni generación automática de ND/NC por diferencia de cambio con esta evidencia. La edición de cotización en el comprobante y el asistente de cambio de moneda son mecanismos distintos. En las tres ramas, `change_currency` retorna cuando `inv_currency == new_currency`. No sugerir que una factura autorizada puede modificarse libremente mediante el asistente. Documentar estados permitidos y tratamiento de documentos electrónicos en una prueba antes de explicar el flujo de modificación.

## 06 — Demostración sugerida

Facturar en moneda extranjera, registrar un cobro con otra cotización y mostrar importes y saldo. Usar un borrador para demostrar el asistente de recálculo. Dejar las ND/NC por diferencia de cambio fuera de la demo hasta identificar el circuito.

## 07 — Temas del Excel vinculados

- `Comprobantes-10` · Carga de tipo de cambio en la emisión de facturas de clientes
- `Comprobantes-11` · Carga de tipo de cambio en la emisión de facturas de proveedores
- `Comprobantes-32` · Creación de ND/NC a partir de diferencia de cambio
- `Comprobantes-33` · Carga Cobros / pagos en pesos o moneda extranjera con tipo de cambio por comprobante
- `Comprobantes-59` · Cambio o actualizacion de moneda de un comprobante ya cargado

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/account_move.py:819`
- `l10n_ar_eynes/models/account_payment_order.py:1242`
- `l10n_ar_eynes/wizard/account_change_currency.py:122`
- `l10n_ar_eynes/wizard/account_debit_note.py:22`
- `l10n_ar_eynes/wizard/account_move_reversal.py:26`

### Rama 17.0

- `l10n_ar_eynes/models/account_move.py:2881`
- `l10n_ar_eynes/models/account_payment_order.py:872`
- `l10n_ar_eynes/wizard/account_change_currency.py:105`
- `l10n_ar_eynes/wizard/account_debit_note.py:28`
- `l10n_ar_eynes/wizard/account_move_reversal.py:26`

### Rama 19.0

- `l10n_ar_eynes/models/account_move.py:840`
- `l10n_ar_eynes/models/account_payment_order.py:889`
- `l10n_ar_eynes/wizard/account_change_currency.py:105`
- `l10n_ar_eynes/wizard/account_debit_note.py:28`
- `l10n_ar_eynes/wizard/account_move_reversal.py:26`

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

---
title: "Facturación argentina desde el punto de venta"
seo_title: "Facturación argentina desde el punto de venta | Eynes"
meta_description: "Conectá el cobro en caja con la facturación argentina, los impuestos y el comprobante que recibe el cliente."
slug: "punto-de-venta"
url: "/localizacion-argentina/punto-de-venta"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Facturar y vender"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿Puedo elegir factura electrónica o interna desde caja?", "respuesta": "La interfaz incorpora ambas modalidades cuando los diarios correspondientes están configurados."}, {"pregunta": "¿El POS calcula percepciones?", "respuesta": "El módulo llama al cálculo de percepciones de la orden y muestra sus importes. Deben estar configuradas las reglas y los datos fiscales del cliente."}]
---

## 01 — Texto para el sitio

Conectá el cobro en caja con la facturación argentina, los impuestos y el comprobante que recibe el cliente.

## 02 — El problema que resuelve

Si la caja vende y la factura se genera después en otro circuito, el operador debe duplicar datos y corregir diferencias. El módulo de POS incorpora la selección de modalidad, el cálculo impositivo y la generación de factura dentro del proceso de venta.

## 03 — Alcance funcional

- Facturas electrónicas e internas desde el POS, vinculadas a diarios configurados.
- Circuito de devolución y preparación del comprobante correspondiente; probar notas electrónicas e internas como escenarios distintos.
- Cálculo de percepciones desde los datos de la orden y visualización de sus importes en la interfaz.
- Selección de modalidad manual/interna o electrónica desde el pago; documentos y datos del cliente vinculados a la posición fiscal.
- Uso del circuito FCE a través de la facturación, sujeto a los pendientes de verificación de ese circuito.


## 04 — Diferencias por versión

`l10n_ar_pos_wsfe` depende de `point_of_sale` y de la localización en las tres ramas. En 15 la interfaz establece electrónica como opción inicial por código; 17/19 agregan `default_invoice_mode`. El campo `block_invoice_offline` está en 17/19. El control explícito de cuentas al cierre se encontró en 19.

## 05 — Condiciones y límites del mensaje

El bloqueo offline evita operar bajo determinadas condiciones; no equivale a autorización electrónica sin conexión ni a soporte CAEA. El alcance FCE en POS requiere demostrar emisión completa, no solo encontrar llamadas compartidas. La carga de impuestos y el comprobante legal deben validarse con los métodos de pago y posiciones fiscales del comercio.

## 06 — Demostración sugerida

Vender a dos clientes con posiciones fiscales distintas, revisar las percepciones y cambiar modalidad. Emitir e imprimir el comprobante. Probar devolución, pérdida de conectividad y cierre con un medio de pago sin cuenta configurada en la versión que incorpora ese control.

## 07 — Temas del Excel vinculados

- `Comprobantes-40` · Emisión de facturas electrónicas desde punto de venta
- `Comprobantes-41` · Emisión de facturas internas desde punto de venta
- `Comprobantes-42` · Cálculo automatizado de percepciones e impuestos desde punto de venta
- `Comprobantes-43` · Impresión de factura legal desde punto de venta
- `POS-1` · Emisión de facturas electrónicas desde punto de venta
- `POS-2` · Emisión de facturas internas desde punto de venta
- `POS-3` · Emisión de notas de crédito electrónicas desde punto de venta
- `POS-4` · Emisión de notas de crédito internas desde punto de venta
- `POS-5` · Cálculo de percepciones desde el punto de venta
- `POS-6` · Impresión de la factura legal desde el punto de venta
- `POS-7` · Elección entre factura electrónica y manual en la pantalla de pago
- `POS-8` · Modo de facturación por defecto
- `POS-9` · Impuestos y percepciones a la vista en la pantalla de pago
- `POS-10` · Bloqueo de facturación offline por posición fiscal
- `POS-11` · Selección de la posición fiscal del pedido
- `POS-12` · Factura de Crédito Electrónica MiPyME desde el punto de venta
- `POS-13` · Control de cuentas contables al cerrar la caja

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/account_move.py:2235`
- `l10n_ar_pos_wsfe/models/pos_order.py:44`
- `l10n_ar_pos_wsfe/static/src/js/models.js:53`
- `l10n_ar_pos_wsfe/static/src/js/payment.js:76`

### Rama 17.0

- `l10n_ar_eynes/models/account_move.py:2322`
- `l10n_ar_pos_wsfe/models/pos_config.py:11`
- `l10n_ar_pos_wsfe/models/pos_order.py:132`
- `l10n_ar_pos_wsfe/views/account_report.xml:8`

### Rama 19.0

- `l10n_ar_eynes/models/account_move.py:2290`
- `l10n_ar_pos_wsfe/models/pos_config.py:11`
- `l10n_ar_pos_wsfe/models/pos_order.py:60`
- `l10n_ar_pos_wsfe/models/pos_session.py:38`
- `l10n_ar_pos_wsfe/static/src/js/payment.js:59`
- `l10n_ar_pos_wsfe/views/account_report.xml:7`

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

---
title: "Recibos y órdenes de pago en Odoo"
seo_title: "Recibos y órdenes de pago en Odoo | Eynes"
meta_description: "Reuní facturas, medios de pago, cheques y retenciones en un mismo recibo u orden de pago, con su registro contable y documentación."
slug: "cobros-y-pagos"
url: "/localizacion-argentina/cobros-y-pagos"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Cobrar y pagar"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿Puedo combinar una transferencia y un cheque?", "respuesta": "Sí. La orden admite líneas de distintos medios y cheques, con sus importes."}, {"pregunta": "¿Puedo pagar varias facturas juntas?", "respuesta": "Sí. El comprobante incorpora partidas de varias facturas y permite definir el importe aplicado a cada una."}, {"pregunta": "¿Puedo emitir los certificados desde el pago?", "respuesta": "La localización incluye numeración, reporte y envío por correo de certificados asociados a las retenciones de la orden."}]
---

## 01 — Texto para el sitio

Reuní facturas, medios de pago, cheques y retenciones en un mismo recibo u orden de pago, con su registro contable y documentación.

## 02 — El problema que resuelve

Cuando un pago combina transferencia, cheques y retenciones, cargar cada parte por separado dificulta saber qué deuda canceló y qué certificado corresponde enviar. El circuito de recibos y órdenes de pago reúne esos componentes.

## 03 — Alcance funcional

- Cobro o pago de varias facturas en un comprobante, con importes aplicados y saldos pendientes.
- Múltiples medios de cobro o pago; cheques propios y de terceros según la operación.
- Registro de retenciones sufridas y cálculo de retenciones emitidas dentro de la orden.
- Cobros y pagos a cuenta, con configuración de retenciones para anticipos.
- Otros cobros y pagos por concepto, con cuenta y asignación analítica.
- Tratamiento de diferencias mediante cuenta de ajuste o saldo pendiente, según la opción seleccionada.
- Numeración, fecha, moneda y cotización del comprobante; creación de movimientos contables y conciliación de partidas.
- Impresión y envío de órdenes de pago y certificados de retención por correo.

## 04 — Diferencias por versión

El modelo `account.payment.order` y sus líneas de medios, deuda, cheques y retenciones existen en 15, 17 y 19. El comportamiento contable y los asistentes se adaptan a cada versión. El complemento que actualiza estados de cheques al conciliar tiene otra matriz de versiones.

## 05 — Condiciones y límites del mensaje

No prometer liberación de crédito instantánea ni conciliación bancaria automática universal a partir de estas clases: esos resultados dependen del circuito comercial y de módulos adicionales. El ajuste contable de un pago tampoco prueba emisión automática de ND/NC por diferencia de cambio.

## 06 — Demostración sugerida

Seleccionar dos facturas de un proveedor, pagar con transferencia y cheque, calcular retenciones y revisar el saldo final. Mostrar la orden, los certificados y las partidas contables resultantes. Repetir con un anticipo para explicar sus reglas propias.

## 07 — Temas del Excel vinculados

- `Comprobantes-12` · Multiples métodos de cobro en un recibo
- `Comprobantes-13` · Cobro de múltiples facturas en un recibo
- `Comprobantes-14` · Carga de multiples cheques de terceros en un recibo
- `Comprobantes-17` · Multiples métodos de pago en una orden de pago a proveedores
- `Comprobantes-18` · Pago de múltiples facturas en un recibo
- `Comprobantes-19` · Carga de multiples cheques de terceros en una orden de pago
- `Comprobantes-20` · Carga de cheques propios y de terceros en una orden de pago
- `Comprobantes-26` · Impresión de orden de pago
- `Comprobantes-27` · Impresión de certificados de retenciones
- `Comprobantes-28` · Envío de certificados de retenciones y ordenes de pago por mail
- `Comprobantes-62` · Cobros y pagos a cuenta
- `Comprobantes-63` · Retenciones sobre pagos a cuenta
- `Comprobantes-64` · Otros pagos y cobros por concepto
- `Comprobantes-65` · Ajuste por diferencia en cobros y pagos

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/account_payment_order.py:907`
- `l10n_ar_eynes/report/retention_certificate.xml:3`

### Rama 17.0

- `l10n_ar_eynes/models/account_payment_order.py:897`
- `l10n_ar_eynes/report/retention_certificate.xml:3`

### Rama 19.0

- `l10n_ar_eynes/models/account_payment_order.py:914`
- `l10n_ar_eynes/report/retention_certificate.xml:3`

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

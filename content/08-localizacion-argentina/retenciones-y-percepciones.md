---
title: "Retenciones y percepciones en Odoo"
seo_title: "Retenciones y percepciones en Odoo | Eynes"
meta_description: "Aplicá las reglas impositivas configuradas en cada factura y pago, conservando el detalle de bases, alícuotas, exclusiones y acumulados."
slug: "retenciones-y-percepciones"
url: "/localizacion-argentina/retenciones-y-percepciones"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Cobrar y pagar"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿El cálculo considera pagos anteriores?", "respuesta": "El motor de retenciones dispone de cálculo de bases y pagos del período; su aplicación depende del concepto y la regla configurada."}, {"pregunta": "¿Puedo cargar retenciones que me practicó un cliente?", "respuesta": "Sí. El recibo permite registrar retenciones y números de certificados sufridos."}, {"pregunta": "¿Las percepciones de compras se tratan igual que las de ventas?", "respuesta": "Son circuitos diferentes: las de ventas tienen cálculo de aplicación y las sufridas en compras se registran en el comprobante del proveedor."}]
---

## 01 — Texto para el sitio

Aplicá las reglas impositivas configuradas en cada factura y pago, conservando el detalle de bases, alícuotas, exclusiones y acumulados.

## 02 — El problema que resuelve

Calcular a mano una retención exige revisar concepto, actividad, pagos anteriores y situación del proveedor. Las percepciones suman otra revisión al facturar. El motor de reglas permite que esos datos participen del cálculo dentro de la operación.

## 03 — Alcance funcional

- Retenciones configurables por concepto, actividad, tipo de impuesto y compañía.
- Ganancias con escalas, importes no sujetos, mínimos y acumulados del período según la regla configurada.
- IIBB con jurisdicción, situación del contacto y alícuotas alimentadas desde padrones o configuradas manualmente.
- Tipos de retención para IVA y SUSS, con reglas de base y aplicación.
- Percepciones en ventas y carga de percepciones sufridas en compras; conceptos, bases, porcentajes y mínimos.
- Certificados de exclusión y vigencias del contacto utilizados al determinar la aplicación.
- Registro del detalle de las retenciones: base, porcentaje, acumulado y certificado; líneas de percepciones vinculadas a factura y cuenta contable.


## 04 — Diferencias por versión

Los motores de retención y percepción están en las tres ramas, con una evolución de la configuración: 15 utiliza más lógica vinculada a diarios y 17/19 a impuestos. El modelo independiente `internal.tax.line` y el archivo `internal_taxes.py` se localizaron en 17 y 19, no en 15.

## 05 — Condiciones y límites del mensaje

La existencia del motor no asegura que todos los regímenes estén configurados ni que cada alícuota esté vigente. No convertir datos de ejemplo, códigos de cálculo o comentarios normativos en una tabla fiscal pública. La revisión por jurisdicción debe distinguir retención, percepción, padrones y exportadores: son capacidades distintas.

## 06 — Demostración sugerida

Usar un proveedor con actividad, concepto y pagos previos en el mes. Comparar base del pago, acumulado y retención propuesta. Mostrar después una venta con percepción y cómo cambia al existir una exclusión vigente.

## 07 — Temas del Excel vinculados

- `Comprobantes-16` · Carga de multiples certificados de retenciones emitidos por clientes
- `Comprobantes-21` · Cálculo automatizado de retenciones en ordenes de pago
- `Comprobantes-22` · Numeración de certificados de retenciones en ordenes de pago
- `Comprobantes-23` · Cálculo automatizado de retenciones de ganancias a partir de escalas, conceptos y actividades
- `Comprobantes-25` · Cálculo automatizado de retenciones de IVA y SUSS
- `Comprobantes-30` · Cálculo automátizado de percepciones en facturas de clientes
- `Comprobantes-34` · Impuestos internos en compras y ventas
- `Comprobantes-60` · Percepciones sufridas en facturas de proveedor
- `Comprobantes-66` · Control del acumulado del período
- `Comprobantes-67` · Consulta de retenciones y percepciones aplicadas y sufridas
- `Comprobantes-68` · Conceptos y actividades de retención y percepción configurables

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/account_move.py:1957`
- `l10n_ar_eynes/models/account_payment_order.py:2755`
- `l10n_ar_eynes/models/perception.py:303`
- `l10n_ar_eynes/models/retention.py:96`

### Rama 17.0

- `l10n_ar_eynes/models/account_move.py:1403`
- `l10n_ar_eynes/models/account_payment_order.py:2696`
- `l10n_ar_eynes/models/internal_taxes.py:14`
- `l10n_ar_eynes/models/perception.py:225`
- `l10n_ar_eynes/models/retention.py:82`

### Rama 19.0

- `l10n_ar_eynes/models/account_move.py:1346`
- `l10n_ar_eynes/models/account_payment_order.py:2778`
- `l10n_ar_eynes/models/internal_taxes.py:13`
- `l10n_ar_eynes/models/perception.py:227`
- `l10n_ar_eynes/models/retention.py:82`

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

---
title: "Mayorista de Ferretería y Bulonería"
seo_title: "Odoo para Mayorista de Ferretería y Bulonería | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Mayorista de Ferretería y Bulonería."
slug: "mayorista-de-ferreteria-y-buloneria"
estado: "publicado"
schema_type: "Service"
agrupador: "COMERCIO MAYORISTA Y MINORISTA"
portfolio: true
casos_relacionados: ["rc-distribuciones"]
faqs: [{"pregunta": "Mis viajantes cobran en la calle, ¿puedo dejar de cargar la cobranza dos veces?", "respuesta": "Sí. El vendedor carga el recibo provisorio con su medio de pago y su comprobante contra la cuenta corriente real del cliente; administración controla contra el banco y lo convierte en recibo definitivo. Se termina la planilla por mail y la recarga manual."}, {"pregunta": "Doy descuento por pronto pago, ¿el sistema lo calcula solo?", "respuesta": "Sí. Se configura la escala y el cálculo de días promedio ponderado por fecha e importe de cada valor; el sistema propone el descuento al registrar la cobranza y emite la nota de crédito con CAE en el mismo acto."}, {"pregunta": "Tengo dos listas, ofertas por depósito y descuento por bulto cerrado, ¿entra en Odoo?", "respuesta": "Sí, con configuración más desarrollo a medida. Las listas se calculan como costo más markup con moneda y tipo de cambio; la oferta se define a nivel de producto y sólo se aplica si el depósito de la cotización es el habilitado; el bulto cerrado se controla por producto y depósito. Si no coincide, el sistema avisa y sugiere cambiar de depósito en vez de facturar mal."}, {"pregunta": "¿Puedo pagar comisión distinta según el precio al que vendió cada línea?", "respuesta": "Sí. La comisión se calcula línea por línea según el precio efectivamente aplicado —lista plena, oferta o bulto cerrado—, no sobre el total del pedido, y sale el informe legal de comisiones de viajantes de la Ley 14.546."}, {"pregunta": "Tengo tres depósitos y estoy poniendo un WMS, ¿se pisan?", "respuesta": "No. El WMS maneja posiciones y movimientos físicos y es la fuente de verdad del stock; Odoo consolida venta, compra, facturación y contabilidad, y recibe las cantidades realmente preparadas y los datos de la guía de despacho."}]
---

## 01 — Hero

**Subtítulo:** Comercio mayorista y minorista

## 02 — Problemas específicos del rubro

### Cobranza de la fuerza de venta cargada dos veces

El vendedor cobra durante la gira y extiende un recibo provisorio en una plataforma ajena al sistema de gestión. El lunes siguiente deposita y manda una planilla resumen por mail; administración baja recibo por recibo, lo busca en el banco y recién entonces emite el recibo oficial. La registración nunca es simultánea: dos o tres días de desfase por el clearing bancario. Y en un mismo recibo conviven efectivo, cheques, e-cheq, transferencias, depósitos en cuentas recaudadoras y retenciones de IIBB, Ganancias, Seguridad Social e IVA, con los gastos de la gira descontados de la cobranza en efectivo de esa misma semana.

### Descuento por pronto pago calculado a mano

El descuento —escala de 5%, 3% y 2%— se determina por días promedio de pago, ponderando cada valor por su fecha y su importe, y se formaliza con una nota de crédito con CAE en el mismo acto de registrar la cobranza. Como el descuento se aplica sobre la factura, la cobranza física que trae el vendedor nunca coincide con el total facturado, y cada caso se resolvía a criterio de administración.

### Precios, ofertas y bulto cerrado condicionados por depósito

Lista 1 y Lista 2 son costo más markup, con el costo en dólares o en pesos. La oferta no es una lista: es un porcentaje sobre Lista 2 o un importe fijo, y sólo vale si se despacha desde el depósito habilitado. El descuento por bulto cerrado depende del producto y también del depósito. Y la comisión del vendedor cambia línea por línea según el precio efectivo: 4% a Lista 1, 3,5% a Lista 2, 2,5% con oferta o bulto cerrado aplicado. Con 18.000 productos y 280 categorías sin estructura, actualizar precios era trabajo de días. Aparte, el control de fletes de transportistas y la gestión de cheques rechazados vivían fuera del sistema, en manos de una sola persona.

## 03a — Integraciones

ARCA/AFIP nativo, en reemplazo del middleware. Facturación electrónica nativa, en reemplazo del middleware que se usaba antes.

WMS como única fuente de verdad del stock. Gestión avanzada de almacenes como única fuente de verdad del stock: maneja posiciones y movimientos físicos, y devuelve a Odoo las cantidades realmente preparadas y los datos de la guía de despacho.

Plataforma de catálogo de los viajantes. Plataforma de catálogo de los viajantes conectada directamente al ERP, para que el pedido y la cobranza de la gira no se carguen dos veces.

Extractos y modelos de conciliación bancaria. Extractos y modelos de conciliación bancaria, indispensables cuando en un mismo registro de cobranza conviven cheques, e-cheqs, transferencias, retenciones y gastos de gira.

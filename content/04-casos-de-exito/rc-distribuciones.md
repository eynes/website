---
title: "RC Distribuciones: Odoo para Mayorista de Ferretería y Bulonería"
seo_title: "RC Distribuciones | Casos de Odoo | Eynes"
meta_description: "Gestión de la información descentralizada, dependencia de un desarrollador local, problemas continuos de stock"
slug: "rc-distribuciones"
estado: "publicado"
schema_type: "Article"
cliente: "RC Distribuciones"
rubro: "Mayorista de Ferretería y Bulonería"
pais: ""
usuarios: ""
modulos_implementados: []
resultado_clave: "Logramos eliminar la doble carga de datos. Hoy el viajante registra el cobro en la calle y la cuenta corriente del cliente se actualiza de inmediato; administración simplemente controla contra el banco y emite el recibo definitivo. El sistema ahora determina el descuento por pronto pago y emite la nota de crédito con CAE en el mismo acto. Estandarizamos el cálculo de comisiones cumpliendo con la Ley 14.546, dejando de depender de procesos manuales. Centralizar nuestros 18.000 artículos, la logística de fletes y la gestión de cheques rechazados en una única plataforma nos permitió alcanzar una operación mucho más ágil y ordenada."
agrupador: "COMERCIO MAYORISTA Y MINORISTA"
portfolio: true
faqs: [{"pregunta": "Mis viajantes cobran en la calle, ¿puedo dejar de cargar la cobranza dos veces?", "respuesta": "Sí. El vendedor carga el recibo provisorio con su medio de pago y su comprobante contra la cuenta corriente real del cliente; administración controla contra el banco y lo convierte en recibo definitivo. Se termina la planilla por mail y la recarga manual."}, {"pregunta": "Doy descuento por pronto pago, ¿el sistema lo calcula solo?", "respuesta": "Sí. Se configura la escala y el cálculo de días promedio ponderado por fecha e importe de cada valor; el sistema propone el descuento al registrar la cobranza y emite la nota de crédito con CAE en el mismo acto."}, {"pregunta": "Tengo dos listas, ofertas por depósito y descuento por bulto cerrado, ¿entra en Odoo?", "respuesta": "Sí, con configuración más desarrollo a medida. Las listas se calculan como costo más markup con moneda y tipo de cambio; la oferta se define a nivel de producto y sólo se aplica si el depósito de la cotización es el habilitado; el bulto cerrado se controla por producto y depósito. Si no coincide, el sistema avisa y sugiere cambiar de depósito en vez de facturar mal."}, {"pregunta": "¿Puedo pagar comisión distinta según el precio al que vendió cada línea?", "respuesta": "Sí. La comisión se calcula línea por línea según el precio efectivamente aplicado —lista plena, oferta o bulto cerrado—, no sobre el total del pedido, y sale el informe legal de comisiones de viajantes de la Ley 14.546."}, {"pregunta": "Tengo tres depósitos y estoy poniendo un WMS, ¿se pisan?", "respuesta": "No. El WMS maneja posiciones y movimientos físicos y es la fuente de verdad del stock; Odoo consolida venta, compra, facturación y contabilidad, y recibe las cantidades realmente preparadas y los datos de la guía de despacho."}]
---

## 03 — El problema

Gestión de la información descentralizada, dependencia de un desarrollador local, problemas continuos de stock

## 04 — La implementación

RC DISTRIBUCIONES. Situación inicial: información descentralizada, dependencia de un desarrollador local y problemas continuos de stock. El circuito de cobranza de los viajantes obligaba a cargar todo dos veces, el descuento por pronto pago se calculaba a mano ponderando días e importes, y con 18.000 productos la actualización de precios y la liquidación de comisiones consumía días de trabajo. Qué se hizo: reemplazo del middleware por Odoo, conexión de la plataforma de catálogo de los viajantes al ERP, WMS como única fuente de verdad del stock, estructuración de 280 categorías, modelos de conciliación bancaria avanzada y parametrización del motor de reglas de descuentos y comisiones según depósito y nivel de precio. Resultado: se eliminó la doble carga; el viajante registra el cobro en la calle y la cuenta corriente se actualiza de inmediato; el sistema determina el descuento por pronto pago y emite la nota de crédito con CAE en el mismo acto; el cálculo de comisiones quedó estandarizado cumpliendo la Ley 14.546.

## 05 — Testimonio

EL DESAFÍO
"Operábamos con un sistema de un desarrollador local y la información estaba completamente descentralizada. Nuestro mayor cuello de botella era el circuito de cobranza de los viajantes: el vendedor cobraba durante la gira usando una plataforma externa y recién el lunes enviaba una planilla resumen. Administración debía ingresar todo nuevamente, recibo por recibo, luchando con el desfasaje de días del clearing bancario. En un mismo registro convivían cheques, e-cheqs, transferencias, retenciones impositivas y los gastos propios de la gira. Además, calcular el descuento por pronto pago era un proceso sumamente manual —ponderando días e importes— y las comisiones de los vendedores requerían un análisis línea por línea, dependiendo de si se aplicaba Lista 1, Lista 2, ofertas por depósito o bulto cerrado. Al manejar 18.000 productos, la actualización de precios y la liquidación de comisiones nos consumía días enteros de trabajo."

LA SOLUCIÓN
"Decidimos dar el salto para unificar nuestra operación. Reemplazamos el middleware e implementamos Odoo. Conectamos la plataforma de catálogo de los viajantes directamente al ERP y establecimos nuestro nuevo WMS como la única fuente de verdad para el stock. Paralelamente, estructuramos nuestras 280 categorías, configuramos modelos de conciliación bancaria avanzada y parametrizamos el motor de reglas para que los descuentos y las comisiones se calculen automáticamente según el depósito de origen y el nivel de precio aplicado."

EL RESULTADO
"Logramos eliminar la doble carga de datos. Hoy el viajante registra el cobro en la calle y la cuenta corriente del cliente se actualiza de inmediato; administración simplemente controla contra el banco y emite el recibo definitivo. El sistema ahora determina el descuento por pronto pago y emite la nota de crédito con CAE en el mismo acto. Estandarizamos el cálculo de comisiones cumpliendo con la Ley 14.546, dejando de depender de procesos manuales. Centralizar nuestros 18.000 artículos, la logística de fletes y la gestión de cheques rechazados en una única plataforma nos permitió alcanzar una operación mucho más ágil y ordenada."

## 07 — Integraciones del rubro

ARCA/AFIP nativo, en reemplazo del middleware. Facturación electrónica nativa, en reemplazo del middleware que se usaba antes.

WMS como única fuente de verdad del stock. Gestión avanzada de almacenes como única fuente de verdad del stock: maneja posiciones y movimientos físicos, y devuelve a Odoo las cantidades realmente preparadas y los datos de la guía de despacho.

Plataforma de catálogo de los viajantes. Plataforma de catálogo de los viajantes conectada directamente al ERP, para que el pedido y la cobranza de la gira no se carguen dos veces.

Extractos y modelos de conciliación bancaria. Extractos y modelos de conciliación bancaria, indispensables cuando en un mismo registro de cobranza conviven cheques, e-cheqs, transferencias, retenciones y gastos de gira.

## 09 — Problemas específicos del rubro

### Cobranza de la fuerza de venta cargada dos veces

El vendedor cobra durante la gira y extiende un recibo provisorio en una plataforma ajena al sistema de gestión. El lunes siguiente deposita y manda una planilla resumen por mail; administración baja recibo por recibo, lo busca en el banco y recién entonces emite el recibo oficial. La registración nunca es simultánea: dos o tres días de desfase por el clearing bancario. Y en un mismo recibo conviven efectivo, cheques, e-cheq, transferencias, depósitos en cuentas recaudadoras y retenciones de IIBB, Ganancias, Seguridad Social e IVA, con los gastos de la gira descontados de la cobranza en efectivo de esa misma semana.

### Descuento por pronto pago calculado a mano

El descuento —escala de 5%, 3% y 2%— se determina por días promedio de pago, ponderando cada valor por su fecha y su importe, y se formaliza con una nota de crédito con CAE en el mismo acto de registrar la cobranza. Como el descuento se aplica sobre la factura, la cobranza física que trae el vendedor nunca coincide con el total facturado, y cada caso se resolvía a criterio de administración.

### Precios, ofertas y bulto cerrado condicionados por depósito

Lista 1 y Lista 2 son costo más markup, con el costo en dólares o en pesos. La oferta no es una lista: es un porcentaje sobre Lista 2 o un importe fijo, y sólo vale si se despacha desde el depósito habilitado. El descuento por bulto cerrado depende del producto y también del depósito. Y la comisión del vendedor cambia línea por línea según el precio efectivo: 4% a Lista 1, 3,5% a Lista 2, 2,5% con oferta o bulto cerrado aplicado. Con 18.000 productos y 280 categorías sin estructura, actualizar precios era trabajo de días. Aparte, el control de fletes de transportistas y la gestión de cheques rechazados vivían fuera del sistema, en manos de una sola persona.

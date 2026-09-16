---
title: "Calzado / Marroquinería"
seo_title: "Odoo para Calzado / Marroquinería | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Calzado / Marroquinería."
slug: "calzado-marroquineria"
estado: "publicado"
schema_type: "Service"
agrupador: "AGROINDUSTRIA Y MANUFACTURA"
portfolio: true
casos_relacionados: ["ferraro"]
modulos_relevantes: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
integraciones_destacadas: ["Facturación electrónica", "Medios de pago y promociones bancarias", "Canales de venta online", "Logística y transferencias"]
faqs: [{"pregunta": "¿Cómo maneja Odoo los talles y colores?", "respuesta": "Con variantes: un modelo con sus atributos genera cada combinación como ítem con stock, código y precio propios, manteniendo el análisis a nivel modelo cuando conviene y a nivel variante cuando hace falta decidir la reposición."}, {"pregunta": "¿Puedo ver el resultado de cada local por separado?", "respuesta": "Sí. Cada punto de venta se analiza por ventas, margen y rotación, y también permite comparar qué producto funciona en un local y no en otro, que es la base para redistribuir en lugar de liquidar."}, {"pregunta": "¿Sirve para vender mayorista y minorista a la vez?", "respuesta": "Sí, con listas de precios y condiciones distintas por canal sobre un mismo catálogo y un mismo stock, incluyendo pedidos mayoristas por curva de talles."}, {"pregunta": "¿Puedo detectar el stock que no rota antes del cierre de temporada?", "respuesta": "Sí, con reportes de antigüedad y rotación por variante, que permiten actuar durante la temporada, cuando el producto todavía se vende a precio de lista."}]
---

## 01 — Hero

**Subtítulo:** Agroindustria y manufactura

## 02 — Problemas específicos del rubro

### Stock inmovilizado por falta de análisis por variante

Un modelo se multiplica por talle y por color, y esa matriz de variantes es la que termina definiendo si la temporada cierra bien o mal. Si el análisis se hace por modelo y no por variante, el problema queda escondido: los talles extremos y los colores que no salieron se acumulan en depósito, mientras se pierden ventas porque faltan justo las curvas centrales. Y al cierre de temporada, ese stock inmovilizado solo se recupera liquidando.

### Locales desconectados de la administración central

Si cada local manda sus ventas y su stock por planilla o por WhatsApp, la casa central siempre está mirando datos de ayer. Eso frena tres cosas al mismo tiempo: reponer a tiempo, mover mercadería entre locales según lo que rota en cada uno, y saber el resultado real de cada punto de venta.

### Compra y reposición por temporada sin historial confiable

El calzado se compra o se produce contra temporada, con meses de anticipación y casi nada de margen para corregir sobre la marcha. Sin un historial confiable de ventas por variante, esa proyección termina haciéndose a ojo, y el error se paga dos veces: primero en quiebre de stock durante el pico de ventas, después en liquidación al final de la temporada.

## 03 — Módulos relevantes

Inventario (variantes por talle y color, stock por local y depósito, transferencias entre locales) · Punto de Venta (locales en tiempo real contra stock y contabilidad centrales) · Ventas (canal mayorista, listas por canal, pedidos por curva de talles) · Compras / Fabricación (reposición y producción por temporada, listas de materiales, importación) · eCommerce (mismo catálogo de variantes y mismo stock) · Contabilidad + Localización Argentina (facturación electrónica, resultado por local, regímenes provinciales) · Informes de Inventario (rotación por variante, antigüedad de stock, cobertura por talle).

## 03a — Integraciones

Facturación electrónica. ARCA (ex AFIP) desde el POS de cada local y desde la venta mayorista, sin doble carga.

Medios de pago y promociones bancarias. Tarjetas, billeteras y planes de cuotas con conciliación de liquidaciones, que en retail de indumentaria y calzado son una porción central de la venta.

Canales de venta online. Tienda propia y marketplaces sincronizando stock y precios por variante, evitando vender un talle que ya no está.

Logística y transferencias. Envíos a cliente final y movimientos entre locales, con trazabilidad de la mercadería en tránsito.

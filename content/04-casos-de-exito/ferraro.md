---
title: "Ferraro: Odoo para Calzado / Marroquinería"
seo_title: "Ferraro | Casos de Odoo | Eynes"
meta_description: "Stock inmovilizado en depósitos y gestión de locales no integrada con la administración central."
slug: "ferraro"
estado: "publicado"
schema_type: "Article"
cliente: "Ferraro"
rubro: "Calzado / Marroquinería"
pais: ""
usuarios: ""
modulos_implementados: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
resultado_clave: "Sabemos qué rota y qué no, y podemos mover mercadería entre locales antes de que se convierta en liquidación."
agrupador: "AGROINDUSTRIA Y MANUFACTURA"
portfolio: true
faqs: [{"pregunta": "¿Cómo maneja Odoo los talles y colores?", "respuesta": "Con variantes: un modelo con sus atributos genera cada combinación como ítem con stock, código y precio propios, manteniendo el análisis a nivel modelo cuando conviene y a nivel variante cuando hace falta decidir la reposición."}, {"pregunta": "¿Puedo ver el resultado de cada local por separado?", "respuesta": "Sí. Cada punto de venta se analiza por ventas, margen y rotación, y también permite comparar qué producto funciona en un local y no en otro, que es la base para redistribuir en lugar de liquidar."}, {"pregunta": "¿Sirve para vender mayorista y minorista a la vez?", "respuesta": "Sí, con listas de precios y condiciones distintas por canal sobre un mismo catálogo y un mismo stock, incluyendo pedidos mayoristas por curva de talles."}, {"pregunta": "¿Puedo detectar el stock que no rota antes del cierre de temporada?", "respuesta": "Sí, con reportes de antigüedad y rotación por variante, que permiten actuar durante la temporada, cuando el producto todavía se vende a precio de lista."}]
---

## 03 — El problema

Stock inmovilizado en depósitos y gestión de locales no integrada con la administración central.

## 04 — La implementación

FERRARO. Situación inicial: stock inmovilizado en depósitos y gestión de locales desconectada de la administración central. Qué se hizo: implementación de Odoo unificando POS de locales, inventario por variante y administración central, con reportes de rotación por talle y color.

## 05 — Testimonio

[EL DESAFÍO
Teníamos plata quieta en el depósito y no terminábamos de ver dónde. Los locales manejaban su información por su lado y a la administración central le llegaba tarde.

LA SOLUCIÓN
Implementamos Odoo con Eynes integrando los locales con el stock y la administración. Empezamos a ver el inventario por modelo, talle y color. Además, unificamos el control de las cajas.

EL RESULTADO
Sabemos qué rota y qué no, y podemos mover mercadería entre locales antes de que se convierta en liquidación.

## 06 — Módulos relevantes para el rubro

Inventario (variantes por talle y color, stock por local y depósito, transferencias entre locales) · Punto de Venta (locales en tiempo real contra stock y contabilidad centrales) · Ventas (canal mayorista, listas por canal, pedidos por curva de talles) · Compras / Fabricación (reposición y producción por temporada, listas de materiales, importación) · eCommerce (mismo catálogo de variantes y mismo stock) · Contabilidad + Localización Argentina (facturación electrónica, resultado por local, regímenes provinciales) · Informes de Inventario (rotación por variante, antigüedad de stock, cobertura por talle).

## 07 — Integraciones del rubro

Facturación electrónica. ARCA (ex AFIP) desde el POS de cada local y desde la venta mayorista, sin doble carga.

Medios de pago y promociones bancarias. Tarjetas, billeteras y planes de cuotas con conciliación de liquidaciones, que en retail de indumentaria y calzado son una porción central de la venta.

Canales de venta online. Tienda propia y marketplaces sincronizando stock y precios por variante, evitando vender un talle que ya no está.

Logística y transferencias. Envíos a cliente final y movimientos entre locales, con trazabilidad de la mercadería en tránsito.

## 09 — Problemas específicos del rubro

### Stock inmovilizado por falta de análisis por variante

Un modelo se multiplica por talle y por color, y esa matriz es la que define si la temporada cierra bien. Sin visibilidad por variante, el análisis se hace por modelo y esconde el problema real: quedan los talles extremos y los colores que no salieron, inmovilizados en depósito, mientras se pierden ventas por faltante de las curvas centrales. Al cierre de temporada, ese stock solo se recupera con liquidación.

### Locales desconectados de la administración central

Cuando cada local reporta ventas y stock por planilla o por mensaje, la casa central trabaja siempre con información de ayer. Eso impide reponer a tiempo, mover mercadería entre locales según lo que rota en cada uno, y conocer el resultado real por punto de venta.

### Compra y reposición por temporada sin historial confiable

El calzado trabaja contra temporada, con decisiones de compra o producción tomadas con meses de anticipación y poco margen para corregir. Sin historial confiable de ventas por variante, la proyección se hace por intuición, y el error se paga dos veces: en quiebre durante el pico y en liquidación al final.

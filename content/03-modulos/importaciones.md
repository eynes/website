---
title: "Importaciones"
seo_title: "Importaciones con Odoo: Costeo Real | Eynes"
meta_description: "Costeo de importación con flete, seguro y aranceles prorrateados al producto, y seguimiento de embarques desde Odoo. Implementación con Eynes."
slug: "importaciones"
url: "eynes.com.ar/modulos/importaciones"
schema_type: "Product"
estado: "publicado"
og_image: ""

faqs:
  - pregunta: "¿Qué es un 'costo de importación' en Odoo y por qué me importa?"
    respuesta: "Es el costeo adicional (flete, seguro, aranceles, gastos de despacho) que se prorratea sobre el costo de cada producto importado, según peso, volumen o valor. Sin eso, tu costo de producto queda subestimado y tu margen real termina siendo distinto al que muestra el sistema."
  - pregunta: "¿Puedo seguir el estado de un embarque antes de que llegue a depósito?"
    respuesta: "Sí, la orden de compra al proveedor del exterior queda vinculada al recibo de mercadería y podés registrar su estado (en tránsito, en aduana, recibido) sin depender de una planilla aparte para saber dónde está cada pedido."
  - pregunta: "¿Esto reemplaza a mi despachante de aduana?"
    respuesta: "No, y no debería — el despachante sigue gestionando la parte aduanera. Lo que hace este módulo es que, una vez que tenés los costos reales de flete, seguro y derechos, los cargués al costo del producto en vez de dejarlos como un gasto general que nadie prorratea."

modulos_integrados:
  - "compras"
  - "inventario"
  - "contabilidad-y-finanzas"
  - "comercio-exterior"
---

## 01 — Hero de módulo

**H1:** Importaciones
**Subtítulo:** Flete, seguro y aranceles prorrateados al costo real de cada producto, con seguimiento del embarque hasta que llega a depósito.

## 02 — Features con impacto

| Feature | Beneficio |
|---|---|
| Costeo de importación por producto | El flete, el seguro y los aranceles se prorratean al costo real, no quedan como un gasto suelto que nadie reparte |
| Seguimiento de embarques desde la compra | Sabés en qué estado está cada pedido al exterior sin pedirle la novedad al despachante por mail |
| Proveedores del exterior en el mismo flujo de compras | No armás un circuito paralelo para lo que se compra afuera |

## 03 — Captura / demo visual

<!-- GUÍA: screenshot real del módulo en uso pendiente. -->

## 04 — Integraciones relacionadas

Ver `modulos_integrados` en el frontmatter.

## 04b — Preguntas frecuentes del módulo

Ver `faqs` en el frontmatter.

## 05 — CTA

"Quiero ver este módulo en acción" → Agendar demo (`/demo`)

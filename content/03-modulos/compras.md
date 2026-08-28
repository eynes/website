---
title: "Compras"
seo_title: "Compras con Odoo: Retenciones Automáticas | Eynes"
meta_description: "Calculá retenciones a proveedores y liquidaciones automáticamente, sin planillas sueltas. Implementación de Odoo para compras con Eynes."
slug: "compras"
url: "eynes.com.ar/modulos/compras"
schema_type: "Product"
estado: "publicado"
og_image: ""

faqs:
  - pregunta: "¿Calcula automáticamente las retenciones de Ganancias e IIBB al pagar a un proveedor?"
    respuesta: "Sí, el sistema se integra con los padrones de las entidades de control (ARCA, ARBA, AGIP, etc.) y calcula y contabiliza automáticamente las retenciones correspondientes al emitir una orden de pago."
  - pregunta: "¿Puedo automatizar la liquidación a proveedores o productores según tarifas variables?"
    respuesta: "Sí, una vez que el sistema registra lo recibido en un período (con sus descuentos de calidad, si aplica), calcula automáticamente el importe a pagar según las tarifas vigentes."
  - pregunta: "¿Las compras se generan solas según lo que realmente se vende?"
    respuesta: "Sí, cuando Compras está integrado con Inventario, las reglas de reabastecimiento generan borradores de orden de compra automáticos según el historial real de ventas."

modulos_integrados:
  - "inventario"
  - "contabilidad-y-finanzas"

caso_relacionado:
  slug: "manolo"
  resultado: "Certificados de retención a proveedores emitidos sin intervención manual"
---

## 01 — Hero de módulo

**H1:** Compras
**Subtítulo:** Retenciones a proveedores y liquidaciones automáticas, sin planillas sueltas ni exposición a multas por cálculos manuales.

## 02 — Features con impacto

| Feature | Beneficio |
|---|---|
| Cálculo automático de retenciones a proveedores | → Sin errores manuales que te expongan a multas |
| Liquidación automática a proveedores/productores | → Pagos ágiles, sin planillas sueltas |
| Reglas de reabastecimiento conectadas a Inventario | → Comprás lo que realmente rota, no lo que "parece que se vende" |

## 03 — Captura / demo visual

<!-- GUÍA: screenshot real del módulo en uso pendiente. -->

## 04 — Integraciones relacionadas

Ver `modulos_integrados` en el frontmatter.

## 04b — Preguntas frecuentes del módulo

Ver `faqs` en el frontmatter.

## 05 — CTA

"Quiero ver este módulo en acción" → Agendar demo (`/demo`)

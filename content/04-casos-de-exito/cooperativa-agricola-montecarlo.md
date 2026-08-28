---
# Fuente de todos los datos de este caso: Excel "portfolio de proyectos
# realizados.xlsx", hojas "Casos" y "Verticales" (fila Cooperativa Agrícola
# Montecarlo).

cliente: "Cooperativa Agrícola Montecarlo"
logo: ""
rubro: "agroindustria"
# GUÍA: "agroindustria" todavía no tiene página de vertical propia en
# 02-verticales/ — campo de referencia, no link válido todavía.
pais: "Argentina"
usuarios: 15
modulos_implementados:
  - "inventario"
  - "compras"
  # GUÍA: el cliente usa además Fabricación, que hoy no tiene módulo
  # propio en 03-modulos/.
resultado_clave: "Peso neto de camiones ingresado automáticamente al sistema desde las básculas, sin intervención humana ni errores de tipeo. (Sin cifra porcentual dicha por el cliente; ver voz-y-tono.md regla 3.)"

title: "Cómo la Cooperativa Agrícola Montecarlo eliminó los errores de pesaje conectando sus básculas a Odoo"
seo_title: "Caso Coop. Agrícola Montecarlo — Odoo Agro | Eynes"
meta_description: "La Cooperativa Agrícola Montecarlo integró básculas de camiones y liquidación a productores con Odoo y Eynes, sin errores de tipeo."
slug: "cooperativa-agricola-montecarlo"
url: "eynes.com.ar/casos/cooperativa-agricola-montecarlo"
schema_type: "Article"
estado: "publicado"
og_image: ""
---

## 01 — Hero del caso

Logo del cliente + "El camión sube a la báscula y el peso neto ingresa al sistema sin intervención humana"

## 02 — Ficha rápida

| Rubro | País | Usuarios | Módulos implementados |
|---|---|---|---|
| Agroindustria (acopio y molienda de yerba mate, fécula de mandioca) | Argentina | 15 (Odoo Community, 250 empleados) | Inventario, Fabricación, Compras (Liquidación a productores) |

Entidad cooperativa de Misiones, reconocida nacionalmente por las marcas de yerba mate Aguantadora y Pampa, integrada por productores locales.

## 03 — El problema

> "El corazón de nuestra cooperativa es el cultivo y almacenamiento de productos primarios —yerba, mandioca, leña— pero teníamos un cuello de botella en la integración de los distintos periféricos con el sistema de gestión. El peso de los camiones salía impreso de la balanza, un operario lo anotaba en un papel y horas después alguien lo pasaba al sistema. Los errores de tipeo generaban diferencias muy grandes en kilos, y los productores se quejaban por las demoras para recibir sus liquidaciones de pago."

Además, había una desconexión total entre el control de calidad en la recepción (por ejemplo, nivel de humedad) y la clasificación del inventario en los almacenes.

## 04 — La solución

> "Decidimos conectar el hardware directamente al software. Integramos las básculas industriales de camiones y los sensores de calidad (humedad) para que se comuniquen en tiempo real con el módulo de inventario y producción del ERP."

Se integraron básculas electrónicas de camiones (puerto serie/TCP), periféricos de laboratorio (humedímetros), ARCA (liquidación primaria) y un portal de autogestión para socios/productores. Módulos relacionados: [Inventario](../03-modulos/inventario.md), [Compras](../03-modulos/compras.md).

## 05 — El resultado

> "Hoy, el camión sube a la báscula, se presiona un botón y el peso neto ingresa directamente al sistema sin intervención humana. El margen de error es cero. Al automatizar este paso, podemos emitir las liquidaciones a nuestros socios productores de forma periódica, mejorando drásticamente nuestra relación con ellos."
>
> — Cooperativa Agrícola Montecarlo

## 06 — CTA

"Quiero un resultado similar en mi empresa" → Agendar demo (`/demo`)

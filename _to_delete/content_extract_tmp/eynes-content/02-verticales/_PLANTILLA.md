---
# ============================================================
# PLANTILLA — PÁGINA DE VERTICAL
# Para crear un rubro nuevo: copiá este archivo, renombralo
# "nombre-del-rubro.md" (minúsculas, guiones, sin tildes/ñ),
# y completá todos los campos. Cuando esté listo, agregalo a
# la grilla de 02-verticales/_hub.md y al selector de rubros
# en 01-paginas-unicas/home.md.
# ============================================================

title: "[COMPLETAR H1 — ej: 'Software de gestión para distribuidoras y mayoristas']"
# GUÍA: usar "software de gestión para [rubro]", NO "Odoo para [rubro]".
# El research mostró que quien busca por rubro específico casi nunca
# menciona "Odoo" — ahí compite Tango, Bejerman, Flexxus. Mencionamos
# Odoo en el cuerpo, no en el título.

seo_title: "[COMPLETAR ~60 caracteres]"
meta_description: "[COMPLETAR ~155 caracteres]"
slug: "[nombre-del-rubro]"
url: "eynes.com.ar/verticales/[nombre-del-rubro]"
schema_type: "Service"
estado: "borrador"
og_image: "[COMPLETAR]"

faqs:
  # GUÍA: 3-5 preguntas ESPECÍFICAS de este rubro — nunca genéricas ni
  # recicladas de otra vertical. Resuelven la objeción justo antes de que
  # el visitante decida, y con schema FAQPage suman a "la gente también
  # pregunta" en Google.
  - pregunta: "[COMPLETAR, ej: '¿Se integra con Mercado Libre/Mercado Pago?']"
    respuesta: "[COMPLETAR]"
  - pregunta: "[COMPLETAR, ej: '¿Cumple con la facturación ARCA para este rubro?']"
    respuesta: "[COMPLETAR]"
  - pregunta: "[COMPLETAR, ej: '¿Qué pasa si crecemos y necesitamos más usuarios?']"
    respuesta: "[COMPLETAR]"
  - pregunta: "[COMPLETAR, ej: '¿Puedo migrar mi lista de proveedores/clientes actual?']"
    respuesta: "[COMPLETAR]"

modulos_relevantes:
  # slugs de 03-modulos/ que aplican a este rubro (3-4)
  - "[COMPLETAR ej: ventas-y-crm]"
  - "[COMPLETAR ej: inventario]"
  - "[COMPLETAR]"
  - "[COMPLETAR]"

casos_relacionados:
  # slugs de 04-casos-de-exito/ de clientes de este mismo rubro (1-2)
  - "[COMPLETAR]"

integraciones_destacadas:
  # 3-4 logos de herramientas que este rubro ya usa y con las que Odoo se
  # integra de forma real y probada — varía según el rubro (ver GUÍA
  # sección 03a más abajo)
  - "[COMPLETAR]"
  - "[COMPLETAR]"
  - "ARCA / AFIP"
  - "[COMPLETAR]"
---

## 01 — Hero de rubro

**Badge:** (tomado de `00-config/site.md → badge_partner` — se repite acá
porque esta página es una entrada frecuente vía búsqueda directa, no todos
pasan primero por el Home)

**H1:** [COMPLETAR — ver campo `title`]

**Subtítulo:** [COMPLETAR — el problema #1 de este sector, en una frase]

## 02 — Problemas específicos del rubro

<!-- GUÍA: este es el contenido que más convierte — el visitante se ve
reflejado en su propio dolor, no en features genéricas. -->

- [COMPLETAR problema típico 1]
- [COMPLETAR problema típico 2]
- [COMPLETAR problema típico 3]

## 02b — Comparador directo

<!-- GUÍA: se nombran competidores directos (ej. Tango, Bejerman) porque
son las marcas que esta audiencia ya conoce y usa — nombrarlas ayuda a que
el salto se entienda de inmediato, en vez de comparar contra un "sistema
genérico" abstracto. Los puntos de comparación cambian según qué usa
realmente este rubro (para ferreterías puede ser distinto que para
servicios). Comparar por hechos observables, nunca con adjetivos
negativos hacia la competencia (ver 00-config/voz-y-tono.md). -->

**Título:** "Odoo vs. [competidor típico del rubro] para [rubro]"

| Con [competidor] | Con Odoo (Eynes) |
|---|---|
| [COMPLETAR hecho observable] | [COMPLETAR alivio correspondiente] |
| [COMPLETAR] | [COMPLETAR] |
| [COMPLETAR] | [COMPLETAR] |

## 03 — Módulos relevantes para este rubro

Ver `modulos_relevantes` en el frontmatter — listar acá los 3-4 módulos con link a `03-modulos/`.

## 03a — Se integra con lo que ya usás

<!-- GUÍA: responde a la objeción tácita de "¿voy a tener que dejar de
usar lo que ya tengo?" con prueba concreta, no una promesa. Deben ser
integraciones reales y probadas de Eynes — pesa mucho más que una lista
de features. El set de logos varía según el rubro (ej: para servicios,
calendarios/facturación de horas en vez de Mercado Libre). -->

**Título:** "No tenés que abandonar tus herramientas"

Ver `integraciones_destacadas` en el frontmatter.

## 04 — Casos de éxito del rubro

Ver `casos_relacionados` en el frontmatter — 1-2 casos con logo + métrica, linkeando a `04-casos-de-exito/`.

## 05 — Testimonio

> "[COMPLETAR cita textual del cliente]"
> — [COMPLETAR nombre / cargo / empresa]

## 05b — Preguntas frecuentes del rubro

Ver `faqs` en el frontmatter (se renderiza con schema FAQPage).

## 06 — CTA calificador

"Agendar demo para [rubro]" — mismo formulario que `/demo`, prellenado con este rubro.

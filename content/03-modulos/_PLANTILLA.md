---
# ============================================================
# PLANTILLA — PÁGINA DE MÓDULO
# Para crear un módulo nuevo: copiá este archivo, renombralo
# "nombre-del-modulo.md", completá los campos, y agregalo a la
# grilla de 03-modulos/_hub.md.
# ============================================================

title: "[COMPLETAR — nombre del módulo + qué resuelve en una frase]"
seo_title: "[COMPLETAR ~60 caracteres]"
meta_description: "[COMPLETAR ~155 caracteres]"
slug: "[nombre-del-modulo]"
url: "eynes.com.ar/modulos/[nombre-del-modulo]"
schema_type: "Product"
estado: "borrador"
og_image: "[COMPLETAR]"

faqs:
  # GUÍA: preguntas específicas de ESTE módulo, no genéricas.
  - pregunta: "[COMPLETAR, ej: '¿Necesito otro módulo para que esto funcione?']"
    respuesta: "[COMPLETAR]"
  - pregunta: "[COMPLETAR, ej: '¿Cuánto tarda el equipo en aprender a usarlo?']"
    respuesta: "[COMPLETAR]"
  - pregunta: "[COMPLETAR, ej: '¿Se puede personalizar a mi flujo actual?']"
    respuesta: "[COMPLETAR]"

modulos_integrados:
  # otros módulos con los que este se integra (para la sección 04)
  - "[COMPLETAR slug]"
  - "[COMPLETAR slug]"

caso_relacionado:
  # UN caso de éxito real que demuestre el resultado cuantificado de este
  # módulo — nunca inventar un número acá, siempre linkear al caso real.
  slug: "[COMPLETAR]"
  resultado: "[COMPLETAR, ej: '-40% en tiempo de facturación']"
---

## 01 — Hero de módulo

**Badge:** (tomado de `00-config/site.md → badge_partner`)

**H1:** [COMPLETAR nombre del módulo]

**Subtítulo:** [COMPLETAR qué resuelve en una frase]

## 02 — Features con impacto

<!-- GUÍA: no hay métricas propias por feature — en vez de inventar un
número, cada feature se describe por el beneficio cualitativo (qué deja
de ser un problema). El número real y verificable vive en la página del
caso de éxito, con link directo (ver `caso_relacionado` en el frontmatter).
Así el dato duro no se inventa nunca, pero el visitante igual llega a él
en un clic. -->

| Feature | Beneficio |
|---|---|
| [COMPLETAR feature 1] | → [COMPLETAR beneficio cualitativo] |
| [COMPLETAR feature 2] | → [COMPLETAR beneficio cualitativo] |
| [COMPLETAR feature 3] | → [COMPLETAR beneficio cualitativo] |

> "Mirá el resultado real de [cliente] con este módulo →" (link a `caso_relacionado`)

## 03 — Captura / demo visual

[COMPLETAR — screenshot real del módulo funcionando, nunca ilustración genérica. El visitante técnico (gerente de sistemas, contador) quiere ver el producto real, no una promesa abstracta.]

## 04 — Integraciones relacionadas

Se integra con: ver `modulos_integrados` en el frontmatter.

## 04b — Preguntas frecuentes del módulo

Ver `faqs` en el frontmatter (schema FAQPage).

## 05 — CTA

"Quiero ver este módulo en acción" → Agendar demo (`/demo`)

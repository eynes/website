---
# ============================================================
# PLANTILLA — NOTA DE BLOG
# Copiá este archivo a 05-blog/posts/, renombralo con el slug de
# la nota, completá los campos y sumala a 05-blog/_hub.md y al
# teaser de blog del Home si corresponde (01-paginas-unicas/home.md,
# sección 08b).
# ============================================================

title: "[COMPLETAR H1 — una sola vez, con el término que buscamos rankear]"
seo_title: "[COMPLETAR ~60 caracteres]"
meta_description: "[COMPLETAR ~155 caracteres]"
slug: "[slug-de-la-nota]"
url: "eynes.com.ar/blog/[slug-de-la-nota]"
categoria: "[COMPLETAR — una sola, de las 4 fijas: localizacion-ar | comparativas | por-rubro | guias-de-uso]"
schema_type: "Article"
estado: "borrador"

autor: "[COMPLETAR nombre]"
fecha_publicacion: "[COMPLETAR AAAA-MM-DD]"
fecha_actualizacion: "[COMPLETAR AAAA-MM-DD]"
# GUÍA: la fecha de "última actualización" visible importa — Google
# prioriza contenido vigente, sobre todo en temas normativos como ARCA
# que cambian seguido. Actualizar la nota es más barato que escribir una
# nueva; actualizar esta fecha cada vez que se edite el cuerpo.

tiempo_lectura_min: "[COMPLETAR, ej: 5]"
og_image: "[COMPLETAR — imagen destacada real, evitar banco de imágenes genérico si se puede]"
og_image_alt: "[COMPLETAR alt text descriptivo]"

origen_linkedin: "[COMPLETAR URL del hilo original si esta nota nació como post de LinkedIn, o null]"
# GUÍA: conecta con el pipeline de LinkedIn — la nota larga vive en el
# blog (indexable) y LinkedIn funciona como versión corta + distribución;
# cada post de LinkedIn linkea a la nota completa.

relacionados:
  # 2-3 slugs de otras notas del mismo pilar
  - "[COMPLETAR]"
  - "[COMPLETAR]"

enlaces_internos_sugeridos:
  # GUÍA: cada nota debe linkear hacia adentro (a un módulo, vertical o
  # caso de éxito relacionado) — así el tráfico frío del blog "cae" en
  # páginas que sí venden, no se queda aislado.
  - "[COMPLETAR ej: modulos/contabilidad-y-finanzas]"
  - "[COMPLETAR ej: localizacion-argentina]"

indice:
  # GUÍA: índice ("En esta nota") con anclas a cada subtítulo — mejora
  # tiempo en página y puede generar "sitelinks" en el resultado de
  # Google. Mantener sincronizado con los H2/H3 del cuerpo.
  - "[COMPLETAR H2 1]"
  - "[COMPLETAR H2 2]"
  - "[COMPLETAR H2 3]"
---

<!-- Breadcrumb se genera automáticamente: Blog / [categoría] / [Título]
     — solo categoría-pilar, sin tags en la URL. -->

## [COMPLETAR H2 1]

[COMPLETAR — subtema real, no solo para "meter keywords". Sumar ejemplos concretos o capturas de Odoo cuando aplique.]

## [COMPLETAR H2 2]

[COMPLETAR]

## [COMPLETAR H2 3]

[COMPLETAR]

<!-- GUÍA: dentro del cuerpo, agregar enlaces internos naturales hacia
los módulos/verticales de `enlaces_internos_sugeridos`, no solo dejarlos
listados en el frontmatter. -->

---

**CTA de cierre:** [COMPLETAR — reutilizar copy de `00-config/ctas-reutilizables.md`, ej. "Agendar demo" o link al módulo relacionado]

**Notas relacionadas:** ver `relacionados` en el frontmatter.

<!-- ============================================================
GUÍA TÉCNICA (no es contenido visual, pero define el SEO de la nota):
- Title tag y meta description únicos (campos seo_title / meta_description arriba)
- URL con slug corto y legible
- Schema.org Article con autor y fecha (se genera desde el frontmatter)
- Canonical apuntando a la propia nota
- Imagen con alt text descriptivo (campo og_image_alt)
- Velocidad de carga: imágenes optimizadas, sin scripts pesados
============================================================ -->

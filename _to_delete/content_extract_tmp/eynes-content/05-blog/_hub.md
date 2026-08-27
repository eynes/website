---
title: "Recursos y novedades"
seo_title: "[COMPLETAR ~60 caracteres, ej: 'Blog de Odoo Argentina: Guías y Novedades | Eynes']"
meta_description: "[COMPLETAR ~155 caracteres]"
slug: "blog"
url: "eynes.com.ar/blog"
schema_type: "Blog"
estado: "borrador"

categorias:
  # ============================================================
  # GUÍA CRÍTICA: mantener SIEMPRE estas 4 categorías fijas, sin
  # agregar un sistema de tags libres. Con pocas notas al arrancar,
  # cada tag genera una página casi vacía que Google lee como
  # contenido delgado/duplicado y puede afectar la percepción de
  # calidad de todo el sitio. Si el CMS que se elija genera tags
  # automáticamente, se marcan `noindex`. Esta lista es la
  # arquitectura de silos de SEO del blog: cada pilar agrupa notas
  # relacionadas que se linkean entre sí, lo que ayuda a rankear el
  # conjunto y no solo notas sueltas.
  # ============================================================
  - slug: "localizacion-ar"
    nombre: "Localización AR"
    descripcion: "ARCA, AFIP, IIBB — cruza directo con la página `01-paginas-unicas/localizacion-argentina.md`, que funciona como hub temático de este pilar."
  - slug: "comparativas"
    nombre: "Comparativas"
    descripcion: "Odoo vs SAP / Tango / Bejerman y similares."
  - slug: "por-rubro"
    nombre: "Por rubro"
    descripcion: "Casos y guías organizados por vertical — cruza con `02-verticales/`."
  - slug: "guias-de-uso"
    nombre: "Guías de uso"
    descripcion: "Cómo hacer X en Odoo."
---

## 01 — Encabezado + buscador

"Recursos y novedades" — buscador interno + filtro por categoría.

<!-- GUÍA: el buscador interno ayuda a SEO on-site (reduce rebote) y a que
el propio equipo encuentre notas viejas para reciclar en LinkedIn. -->

## 02 — Categorías / pilares de contenido

Ver `categorias` en el frontmatter — son las 4 fijas, no agregar más sin revisar el impacto en SEO.

## 03 — Nota destacada + grilla

- Nota destacada: [COMPLETAR — la más nueva o la de mejor performance]
- Grilla de notas recientes: listar cada post publicado en `05-blog/posts/` con título, categoría, fecha y tiempo de lectura.

## 04 — CTA lateral / de cierre

<!-- GUÍA: el blog trae tráfico frío; sin un CTA constante ese tráfico lee
la nota y se va. Cada nota individual también debe repetir este CTA (ver
`_PLANTILLA-post.md`, sección 05). -->

"¿Querés ver esto funcionando en tu empresa? Agendá una demo" → `/demo`

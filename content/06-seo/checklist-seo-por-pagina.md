# Checklist SEO antes de publicar cualquier página

Pasar esta checklist sobre cualquier archivo antes de cambiar su `estado` de `borrador` a `publicado`. Tomada y generalizada de la sección "Técnico" que el wireframe define para las notas de blog (página 10), aplicada a todo tipo de página.

## Contenido y metadatos

- [ ] `title` (H1) es único en todo el sitio y no repite el de otra página.
- [ ] `seo_title` tiene la keyword principal (ver `06-seo/mapa-de-keywords.md`) y no supera ~60 caracteres.
- [ ] `meta_description` es única, tiene un beneficio concreto y no supera ~155 caracteres.
- [ ] `slug` es corto, legible, en minúsculas, sin tildes ni caracteres especiales.
- [ ] No quedó ningún `[COMPLETAR]` sin resolver en el cuerpo ni en el frontmatter.
- [ ] Ningún número o métrica fue inventado — todo dato cuantitativo sale de un caso real documentado en `04-casos-de-exito/`.
- [ ] Si hay comparación con un competidor, es por hechos observables, sin adjetivos negativos (ver `00-config/voz-y-tono.md`).

## Estructura y enlaces internos

- [ ] Jerarquía de encabezados correcta: un solo H1, H2/H3 en orden lógico (no saltar de H2 a H4).
- [ ] Al menos un enlace interno hacia una página que "venda" (módulo, vertical o caso), no solo enlaces salientes o ninguno.
- [ ] Si la página tiene FAQ, son preguntas específicas de este contenido — no genéricas ni copiadas de otra página.
- [ ] Breadcrumb reflejando la jerarquía real (ver `06-seo/schema-org-referencia.md`).

## Datos estructurados

- [ ] `schema_type` está definido y corresponde al tipo de página (ver `06-seo/schema-org-referencia.md`).
- [ ] Canonical apunta a la propia página.
- [ ] Si hay `faqs` en el frontmatter, están completas (sin `respuesta: "[COMPLETAR]"`) antes de generar el FAQPage.

## Imágenes y performance

- [ ] Toda imagen tiene alt text descriptivo (no genérico tipo "imagen1.jpg").
- [ ] Ninguna imagen es de banco de imágenes genérico si existe alternativa real (producto, equipo, oficinas) — ver `07-media/convenciones-de-archivos.md`.
- [ ] Imágenes optimizadas en tamaño antes de subir (ver convenciones de `07-media/`).

## Específico de blog

- [ ] `categoria` es una de las 4 fijas (`localizacion-ar`, `comparativas`, `por-rubro`, `guias-de-uso`) — nunca un tag libre nuevo.
- [ ] `fecha_actualizacion` refleja la última edición real del cuerpo, no solo la fecha de creación del archivo.
- [ ] El índice (`indice` en el frontmatter) está sincronizado con los H2/H3 reales del cuerpo.

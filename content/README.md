# Base documental — sitio web Eynes

Esta carpeta es la **fuente única de contenido** del sitio nuevo de Eynes. La idea es simple: vos (o quien produzca contenido) edita, agrega o quita archivos acá — en Markdown, sin tocar código — y esa base documental es lo que después se usa para construir el sitio, sea cual sea el framework final (Next.js, Astro, WordPress headless, etc.). Ningún archivo de acá es el sitio; son los **insumos** del sitio.

Está armada 1:1 sobre el wireframe `eynes-wireframe_7.html` (12 páginas). Cada carpeta corresponde a un tipo de página del wireframe.

## Cómo está organizada

```
00-config/            → datos globales que se repiten en todo el sitio (empresa, nav, CTAs, tono de voz)
01-paginas-unicas/    → las 4 páginas que existen una sola vez: home, nosotros, contacto, localización AR
02-verticales/        → hub de verticales + una página por rubro (plantilla repetible)
03-modulos/           → hub de módulos + una página por módulo (plantilla repetible)
04-casos-de-exito/    → hub de casos + una página por cliente (plantilla repetible)
05-blog/              → hub de blog + una nota por post (plantilla repetible)
06-seo/               → mapa de keywords, referencia de schema.org, checklist técnico
07-media/             → convenciones de nombres de archivo y alt text para imágenes
```

Las carpetas `02` a `05` son las que vas a tocar más seguido: para agregar un rubro, un módulo, un caso de éxito o una nota de blog nuevos, copiás el archivo `_PLANTILLA.md` de esa carpeta, lo renombrás con el slug correspondiente, y completás los campos. Para dar de baja una página, borrás el archivo (o le poné `estado: borrador` / `publicar: false` en el frontmatter si preferís no publicarla pero conservar el trabajo).

## Cómo se completa cada archivo

Todos los archivos de contenido (menos los de `00-config` y `06-seo`) siguen la misma forma:

```markdown
---
# frontmatter: metadatos estructurados (SEO, schema.org, relaciones entre páginas)
campo: valor
---

<!-- GUÍA: instrucciones de para qué sirve cada sección y qué objetivo de marketing/SEO cumple -->

## Cuerpo en Markdown con el contenido real de la página
```

- El **frontmatter** (entre `---`) es metadata que un script de build puede leer directo: título de la pestaña, meta description, slug de URL, imagen social, preguntas frecuentes estructuradas (para schema FAQPage), enlaces relacionados, etc. No se borra ningún campo aunque quede vacío — se deja `""` o `[]` y se completa después, así ningún build se rompe por un campo faltante.
- El **cuerpo** es el contenido real: lo que un visitante lee. Usa Markdown estándar (`##` para subtítulos, `**negrita**`, listas, links `[texto](url)`).
- Los bloques `<!-- GUÍA: ... -->` son comentarios de Markdown — no se muestran nunca en el sitio final. Explican el *por qué* de la sección (tomado de las notas de razonamiento del wireframe) para que quien escribe entienda el objetivo, no solo el espacio a llenar. Se pueden dejar o borrar una vez que el contenido está terminado; no rompen nada si quedan.
- Todo lo marcado `[COMPLETAR]` es un dato real de la empresa que falta (una métrica, un nombre, una dirección) — no un texto de relleno para inventar.

## Reglas de contenido que ya se definieron (no re-discutir en cada página)

Estas decisiones ya se tomaron durante el research de SEO/marketing y aplican a **todo** el sitio; están repetidas como recordatorio en cada plantilla relevante, pero acá está el resumen:

1. **Tono:** rioplatense, con "vos", directo, cero jerga corporativa vacía. Ver `00-config/voz-y-tono.md`.
2. **Vender el problema, no la feature.** Cada beneficio se redacta como "dolor → alivio", nunca como lista fría de funcionalidades.
3. **FAQs específicas por página, nunca genéricas ni recicladas.** Cada vertical, módulo y la página de Localización tienen su propia FAQ con 3-5 preguntas reales de ese tema puntual. Esto es intencional para SEO ("la gente también pregunta") y para schema FAQPage — una FAQ copada y pegada en todas las páginas no suma.
4. **Sin tags libres en el blog.** Solo 4 categorías/pilares fijos (ver `05-blog/_hub.md`). Si el CMS que se elija genera tags automáticos, se marcan `noindex`.
5. **Nunca inventar números.** Todo dato cuantitativo (ej. "-40% en tiempo de facturación") tiene que salir de un caso de éxito real y documentado en `04-casos-de-exito/`. Si una página de módulo quiere mostrar una métrica, linkea al caso real en vez de inventar una cifra propia.
6. **No publicar precios.** La página de contacto explica qué variables definen el costo, nunca un número o rango.
7. **Comparación por hechos, no por adjetivos.** Cuando se compara con competidores (Tango, Bejerman, SAP), se listan diferencias observables, nunca calificativos negativos hacia la competencia.
8. **Cada oficina es una entidad de SEO local propia** (Google Business Profile / schema LocalBusiness) — ver `00-config/site.md`.

## Flujo de trabajo sugerido

1. Alguien escribe o edita un `.md` acá (a mano, o con ayuda de un asistente de IA usando este mismo repo de contenido como contexto).
2. Se revisa contra la sección "Checklist antes de publicar" de `06-seo/checklist-seo-por-pagina.md`.
3. Se hace commit/versionado del cambio (recomendado: este directorio como repo git propio, o como carpeta dentro del repo del sitio).
4. El proceso de build del sitio (a definir cuando se elija el stack técnico) lee estos archivos y genera las páginas reales.

## Glosario de campos de frontmatter más comunes

| Campo | Qué es | Ejemplo |
|---|---|---|
| `title` | H1 de la página (lo que lee el visitante, no la pestaña del navegador) | `"Software de gestión para distribuidoras y mayoristas"` |
| `seo_title` | Title tag / pestaña del navegador. Máx. ~60 caracteres, con la keyword principal | `"Odoo para Distribución y Mayoristas \| Eynes"` |
| `meta_description` | Meta description. Máx. ~155 caracteres, con un beneficio + llamado a la acción implícito | `"Gestión de stock, ventas y facturación ARCA en un solo sistema para distribuidoras. Implementación con Eynes, partner oficial de Odoo."` |
| `slug` | Última parte de la URL | `"distribucion-y-mayoristas"` |
| `url` | URL completa de referencia (informativa, no se usa para generar la ruta) | `"eynes.com.ar/verticales/distribucion-y-mayoristas"` |
| `schema_type` | Tipo de schema.org que le corresponde a esta página (ver `06-seo/schema-org-referencia.md`) | `"Service"`, `"Article"`, `"FAQPage"`, `"LocalBusiness"` |
| `estado` | `borrador` \| `revision` \| `publicado` — controla si el build la incluye | `"borrador"` |
| `faqs` | Lista estructurada de preguntas/respuestas específicas de esta página, para JSON-LD FAQPage | ver cualquier plantilla |
| `relacionados` | Slugs de otras páginas del sitio a linkear (módulos, verticales, casos) | `["modulos/contabilidad-y-finanzas"]` |

Cada plantilla trae además sus propios campos específicos (ej. `rubro`, `usuarios`, `resultado_clave` en casos de éxito). Están documentados con un comentario arriba de cada uno la primera vez que aparecen.

## Nombres de archivo

- Todo en minúsculas, con guiones medios, sin tildes ni ñ: `localizacion-argentina.md`, `distribucion-y-mayoristas.md`.
- El nombre del archivo (sin `.md`) es el `slug` por convención — si no coinciden, gana el campo `slug` del frontmatter.
- Los archivos que empiezan con `_` (como `_hub.md` o `_PLANTILLA.md`) son estructurales/de referencia, no páginas de contenido — un build correcto los debe ignorar como página individual.

# Referencia de schema.org por tipo de página

Qué tipo de datos estructurados (JSON-LD) le corresponde a cada tipo de página. El campo `schema_type` del frontmatter de cada archivo indica cuál usar; esta tabla explica el porqué y qué otros schemas se combinan en la misma página.

| Tipo de página | `schema_type` | Se combina con | Notas |
|---|---|---|---|
| Home | `Organization` | `WebSite` (con `SearchAction` si hay buscador global) | Incluye datos de `00-config/site.md`: razón social, logo, redes, oficinas. |
| Nosotros | `AboutPage` | `Organization` | |
| Contacto/Demo | `ContactPage` | — | No confundir con `LocalBusiness` — eso va en cada oficina, no en esta página. |
| Cada oficina (dentro de Nosotros o de una página de contacto local, si se crea) | `LocalBusiness` | `Organization` (como `parentOrganization`) | Una entidad por ciudad — clave para SEO local y Google Business Profile. |
| Verticales (hub) | `CollectionPage` | `ItemList` (listando cada vertical) | |
| Vertical (página individual) | `Service` | `FAQPage` (desde el campo `faqs` del frontmatter) | |
| Módulos (hub) | `CollectionPage` | `ItemList` | |
| Módulo (página individual) | `Product` o `Service` | `FAQPage` | Usar `Product` si se quiere habilitar rich snippets de producto; `Service` si se prioriza consistencia con las páginas de vertical. Definir un criterio único y no mezclar entre módulos. |
| Localización Argentina | `Service` | `FAQPage` | Página única, no forma parte del `ItemList` de módulos. |
| Casos de éxito (hub) | `CollectionPage` | `ItemList` | |
| Caso de éxito (individual) | `Article` | — | Evaluar `Review`/`Testimonial` adicional si el formato lo amerita más adelante. |
| Blog (hub) | `Blog` | `ItemList` | |
| Nota de blog | `Article` | `FAQPage` (si la nota incluye preguntas frecuentes), `BreadcrumbList` | Autor y fechas (`fecha_publicacion`, `fecha_actualizacion`) se toman del frontmatter. |

## Reglas generales

- **FAQPage solo si el contenido de `faqs` es real y específico de esa página** — no generar FAQPage vacío ni con preguntas genéricas recicladas (ver regla de contenido #3 en el `README.md` raíz).
- **Un canonical por página**, siempre apuntando a sí misma salvo que exista una razón explícita de consolidación.
- **BreadcrumbList en toda página que no sea el Home**, reflejando la jerarquía real: `Blog / [categoría] / [Título]`, `Verticales / [rubro]`, `Módulos / [módulo]`, etc.
- **Ninguna página de tag/etiqueta debe llevar schema indexable** — si el CMS elegido genera tags automáticos, van `noindex` (ver `05-blog/_hub.md`).

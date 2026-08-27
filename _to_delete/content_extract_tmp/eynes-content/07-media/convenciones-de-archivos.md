# Convenciones para imágenes y archivos multimedia

Esta carpeta documental no aloja las imágenes en sí (eso vive en un storage/CDN a definir con el stack técnico), pero sí las reglas que hay que seguir para que cada imagen referenciada desde el frontmatter (`og_image`, capturas, logos) sea consistente y ayude al SEO en vez de restarle.

## Nomenclatura de archivos

- Minúsculas, guiones medios, sin espacios ni tildes: `factura-arca-odoo-eynes.jpg`, no `Factura ARCA (Odoo) 1.jpg`.
- El nombre del archivo describe el contenido, no un código interno: preferir `dashboard-inventario-odoo.png` a `img_final_v3.png`.
- Prefijo por sección cuando ayude a ordenar en el storage: `home-`, `caso-[cliente]-`, `blog-[slug]-`.

## Alt text

- Descriptivo y específico, nunca genérico ("imagen") ni relleno de keywords.
- Ejemplo correcto: `alt="Factura electrónica ARCA emitida desde Odoo"`.
- Ejemplo incorrecto: `alt="odoo argentina software erp implementacion"`.
- Todo campo `og_image` debe tener su `og_image_alt` correspondiente completo antes de publicar (ver checklist en `06-seo/checklist-seo-por-pagina.md`).

## Qué imagen usar en cada caso

<!-- GUÍA: repetida en varios lugares del wireframe — el visitante técnico
(gerente de sistemas, contador) quiere ver el producto real, no una
promesa abstracta ni una ilustración de banco de imágenes. -->

- **Screenshots de producto:** siempre capturas reales de Odoo funcionando (con datos de ejemplo, nunca datos reales de un cliente sin autorización). Nunca mockups ni ilustraciones genéricas.
- **Fotos de equipo/oficinas:** siempre fotos reales del equipo de Eynes. Nunca stock photos de "gente de oficina genérica".
- **Logos de clientes:** solo con autorización expresa de uso de marca — dejar constancia de esa autorización antes de publicar.
- **Imágenes destacadas de blog:** preferir una imagen propia o una captura relevante por sobre banco de imágenes genérico, salvo que el tema sea puramente conceptual.

## Tamaños de referencia

| Uso | Proporción / tamaño sugerido |
|---|---|
| `og_image` (social/compartir) | 1200×630px |
| Imagen destacada de blog | 1600×900px (16:9) |
| Logo de cliente en grilla | Altura fija ~60px, fondo transparente (PNG/SVG) |
| Screenshot de producto | Ancho mínimo 1280px, comprimido sin perder legibilidad de texto en pantalla |

## Performance

- Formatos livianos: WebP o JPG comprimido para fotos; SVG o PNG para logos.
- Ninguna imagen debería pesar más de ~300KB sin una razón justificada (galería de alta fidelidad, por ejemplo).

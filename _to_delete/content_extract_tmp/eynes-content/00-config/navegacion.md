---
# Fuente única del menú principal y del footer. Si se agrega/saca un item
# de nav, se edita ACÁ y no en cada página — así el nav nunca queda
# desincronizado entre páginas.

nav_principal:
  - etiqueta: "Verticales"
    url: "/verticales"
  - etiqueta: "Módulos"
    url: "/modulos"
  - etiqueta: "Localización"
    url: "/localizacion-argentina"
    # GUÍA: tiene entidad propia en el nav (no cuelga de "Módulos") porque
    # es una página única, no una plantilla más — así lo definimos en el wireframe.
  - etiqueta: "Casos"
    url: "/casos"
  - etiqueta: "Blog"
    url: "/blog"
  - etiqueta: "Nosotros"
    url: "/nosotros"

cta_nav:
  etiqueta: "Agendar demo"
  url: "/demo"

footer_columnas:
  - titulo: "Oficinas"
    # GUÍA: se completa automáticamente desde 00-config/site.md → oficinas.
    # No hace falta duplicar direcciones acá.
    tipo: "dinamico_oficinas"
  - titulo: "Enlaces rápidos"
    links:
      - { etiqueta: "Verticales", url: "/verticales" }
      - { etiqueta: "Módulos", url: "/modulos" }
      - { etiqueta: "Localización Argentina", url: "/localizacion-argentina" }
      - { etiqueta: "Casos de éxito", url: "/casos" }
      - { etiqueta: "Blog", url: "/blog" }
      - { etiqueta: "Nosotros", url: "/nosotros" }
      - { etiqueta: "Agendar demo", url: "/demo" }
  - titulo: "Redes"
    tipo: "dinamico_redes"
    # se completa desde 00-config/site.md → redes
  - titulo: "Legal"
    links:
      - { etiqueta: "Política de privacidad", url: "/legal/privacidad" }
      - { etiqueta: "Términos y condiciones", url: "/legal/terminos" }
---

<!-- Sin cuerpo — configuración estructurada. -->

---
# Datos globales de la empresa. Estos campos se usan en TODO el sitio:
# footer, schema.org Organization/LocalBusiness, Google Business Profile,
# firma de emails, badges de confianza, etc. Es la "fuente única de verdad"
# de estos datos — si algo cambia (teléfono, dirección), se cambia UNA vez acá.

razon_social: "Eynes S.R.L."
nombre_comercial: "Eynes"
tagline_corto: "Tu empresa, conectada para crecer."
dominio: "eynes.com.ar"

badge_partner:
  texto: "Silver Partner Oficial de Odoo"
  # GUÍA: este badge aparece repetido en el hero de Home, Vertical, Módulo
  # y Localización — es la señal de confianza más rápida de leer para
  # alguien que no sabe distinguir un partner serio de uno improvisado.
  # Si el nivel de partnership cambia (ej. a Gold), se actualiza acá y
  # se propaga solo a las páginas que referencien este campo.
  icono: "🛡"
  link_verificacion: "https://www.odoo.com/es/partners/eynes-srl-17274725?country_id=11"

antiguedad:
  anio_fundacion: "2006"
  anios_operando: "20+ años"

paises_operacion:
  - "Argentina"
  - "España"
  - "Holanda"
  - "Uruguay"
  - "Colombia"
  - "Chile"

prueba_social_home:
  # GUÍA: banda de confianza que va justo debajo del hero del Home
  # (sección "02 — Prueba social inmediata" del wireframe).
  empresas_clientes: "+100 empresas"
  anios_experiencia: "+20 años"
  paises: "6 países"
  logos_clientes_destacados:
    - "YPF"
    - "Lario (Rafaela Alimentos)"
    - "Ivess (El Jumillano)"

oficinas:
  # GUÍA: cada oficina con dirección real habilita un Google Business Profile
  # propio → abre SEO local ("Odoo Mendoza", "implementación Odoo Uruguay").
  # Completar una entrada por ciudad. No dejar oficinas "de relleno": si no
  # hay dirección real y atención en esa ciudad, no se lista como oficina.
  - ciudad: "Buenos Aires"
    pais: "Argentina"
    direccion: "[COMPLETAR dirección completa]"
    telefono: "[COMPLETAR]"
    email: "[COMPLETAR]"
    es_sede_principal: true
  - ciudad: "Santa Fe"
    pais: "Argentina"
    direccion: "[COMPLETAR]"
    telefono: "[COMPLETAR]"
    email: "[COMPLETAR]"
    es_sede_principal: false
  - ciudad: "Mendoza"
    pais: "Argentina"
    direccion: "[COMPLETAR]"
    telefono: "[COMPLETAR]"
    email: "[COMPLETAR]"
    es_sede_principal: false
  - ciudad: "Montevideo"
    pais: "Uruguay"
    direccion: "[COMPLETAR]"
    telefono: "[COMPLETAR]"
    email: "[COMPLETAR]"
    es_sede_principal: false
  # [COMPLETAR: agregar oficina de España si corresponde a "paises_operacion"]

contacto_general:
  email_comercial: "info@eynes.com.ar]"
  email_soporte: "soporte@eynes.com.ar"
  whatsapp_comercial: "+54 9 11 4528-1900"

redes:
  linkedin: "https://www.linkedin.com/company/eynes-odoo-argentina"
  instagram: ""

legal:
  politica_privacidad_url: "/legal/privacidad"
  terminos_url: "/legal/terminos"
---

<!-- Este archivo no tiene cuerpo de Markdown — es puramente configuración
     estructurada (frontmatter). Se referencia desde el build para el footer,
     schema.org y cualquier lugar del sitio que muestre estos datos. -->

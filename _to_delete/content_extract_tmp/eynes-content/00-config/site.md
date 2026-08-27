---
# Datos globales de la empresa. Estos campos se usan en TODO el sitio:
# footer, schema.org Organization/LocalBusiness, Google Business Profile,
# firma de emails, badges de confianza, etc. Es la "fuente única de verdad"
# de estos datos — si algo cambia (teléfono, dirección), se cambia UNA vez acá.

razon_social: "[COMPLETAR] Eynes S.A. / Eynes S.R.L. (nombre legal completo)"
nombre_comercial: "Eynes"
tagline_corto: "[COMPLETAR] frase de una línea que resume qué hace Eynes (para <meta> og:description del home y bio de redes)"
dominio: "eynes.com.ar"

badge_partner:
  texto: "Silver Partner Oficial de Odoo"
  # GUÍA: este badge aparece repetido en el hero de Home, Vertical, Módulo
  # y Localización — es la señal de confianza más rápida de leer para
  # alguien que no sabe distinguir un partner serio de uno improvisado.
  # Si el nivel de partnership cambia (ej. a Gold), se actualiza acá y
  # se propaga solo a las páginas que referencien este campo.
  icono: "🛡"
  link_verificacion: "[COMPLETAR] URL al listado oficial de partners de Odoo donde figura Eynes, si existe"

antiguedad:
  anio_fundacion: "[COMPLETAR ej. 2004]"
  anios_operando: "[COMPLETAR ej. 20+] años"
  # usado en H1/subtítulos de Nosotros y Home ("20+ años implementando Odoo")

paises_operacion:
  - "Argentina"
  - "Uruguay"
  - "España"
  # [COMPLETAR: confirmar lista exacta y agregar si falta algún país]

prueba_social_home:
  # GUÍA: banda de confianza que va justo debajo del hero del Home
  # (sección "02 — Prueba social inmediata" del wireframe).
  empresas_clientes: "[COMPLETAR ej. +150] empresas"
  anios_experiencia: "[COMPLETAR ej. 20] años"
  paises: "[COMPLETAR ej. 5] países"
  logos_clientes_destacados:
    - "[COMPLETAR nombre/logo cliente 1 — pedir autorización de uso de marca]"
    - "[COMPLETAR nombre/logo cliente 2]"
    - "[COMPLETAR nombre/logo cliente 3]"

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
  email_comercial: "[COMPLETAR ej. ventas@eynes.com.ar]"
  email_soporte: "[COMPLETAR]"
  whatsapp_comercial: "[COMPLETAR número con código de país, ej. +54 9 11 xxxx-xxxx]"
  # GUÍA: el botón de WhatsApp aparece en Contacto y en el CTA final del
  # Home como canal alternativo al formulario — es el canal preferido
  # para el lead argentino que "quiere resolver ya".

redes:
  linkedin: "[COMPLETAR URL]"
  instagram: "[COMPLETAR URL, si aplica]"
  # GUÍA: LinkedIn es el canal de distribución primario hoy (ver notas de
  # blog) — el botón de compartir en cada post de blog prioriza LinkedIn.

legal:
  politica_privacidad_url: "/legal/privacidad"
  terminos_url: "/legal/terminos"
  # [COMPLETAR: confirmar si hace falta política de cookies separada]
---

<!-- Este archivo no tiene cuerpo de Markdown — es puramente configuración
     estructurada (frontmatter). Se referencia desde el build para el footer,
     schema.org y cualquier lugar del sitio que muestre estos datos. -->

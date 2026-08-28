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
  # Cifra actualizada según el dato publicado hoy en eynes.com.ar ("+150 clientes").
  empresas_clientes: "+150 empresas"
  anios_experiencia: "+20 años"
  paises: "6 países"
  logos_clientes_destacados:
    - "YPF"
    - "Lario (Rafaela Alimentos)"
    - "Ivess (El Jumillano)"
    - "La Guitarrita"

oficinas:
  # GUÍA: cada oficina con dirección real habilita un Google Business Profile
  # propio → abre SEO local ("Odoo Mendoza", "implementación Odoo Uruguay").
  # No dejar oficinas "de relleno": si no hay dirección real y atención en
  # esa ciudad, no se lista acá como oficina — va en `zonas_de_cobertura`
  # más abajo. Confirmado con el equipo (27/08/2026): la única sede física
  # de Eynes es Buenos Aires; Santa Fe, Mendoza, Montevideo y España son
  # zonas de atención telefónica/remota, sin oficina propia.
  - ciudad: "Buenos Aires"
    pais: "Argentina"
    direccion: "Lima 131, Piso 1, CABA (C1073)"
    telefono: "+54 9 11 4528-1900"
    email: "info@eynes.com.ar"
    es_sede_principal: true

zonas_de_cobertura:
  # GUÍA: ciudades/países donde Eynes atiende clientes y tiene un teléfono
  # dedicado, pero sin oficina física propia — no habilitan Google Business
  # Profile por sí solas. Se muestran igual en Nosotros/Contacto para dejar
  # claro que hay atención local, pero no se les arma SEO local de
  # "oficina" (ver checklist-seo-por-pagina.md).
  - ciudad: "Santa Fe"
    pais: "Argentina"
    telefono: "+54 9 3492 56-2199"
    email: "info@eynes.com.ar"
  - ciudad: "Mendoza"
    pais: "Argentina"
    telefono: "+54 9 2615 12-1045"
    email: "info@eynes.com.ar"
  - ciudad: "Montevideo"
    pais: "Uruguay"
    telefono: "+54 9 11 4528-1900"
    email: "info@eynes.com.ar"
  - ciudad: "Valencia / Castellón"
    pais: "España"
    telefono: "+34 622 65 99 89"
    email: "info@eynes.com.ar"

contacto_general:
  email_comercial: "info@eynes.com.ar"
  email_soporte: "soporte@eynes.com.ar"
  whatsapp_comercial: "+54 9 11 4528-1900"

redes:
  linkedin: "https://www.linkedin.com/company/eynes-odoo-argentina"
  instagram: "https://www.instagram.com/eynesarg/"

legal:
  politica_privacidad_url: "/legal/privacidad"
  terminos_url: "/legal/terminos"
---

<!-- Este archivo no tiene cuerpo de Markdown — es puramente configuración
     estructurada (frontmatter). Se referencia desde el build para el footer,
     schema.org y cualquier lugar del sitio que muestre estos datos. -->

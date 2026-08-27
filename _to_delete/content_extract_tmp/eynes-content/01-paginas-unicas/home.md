---
title: "[COMPLETAR H1 — propuesta de valor centrada en el PROBLEMA, no en 'implementamos Odoo']"
seo_title: "[COMPLETAR ~60 caracteres, ej: 'Odoo en Argentina | Implementación y soporte — Eynes']"
meta_description: "[COMPLETAR ~155 caracteres. Beneficio + señal de confianza + CTA implícito]"
slug: "home"
url: "eynes.com.ar"
schema_type: "Organization"
estado: "borrador"
og_image: "[COMPLETAR ruta a imagen social 1200x630]"
---

<!-- GUÍA GENERAL: esta es la página con más tráfico y más peso de conversión
del sitio. Sigue el orden de secciones definido en el wireframe (PÁGINA 01).
No reordenar sin revisar el razonamiento de cada sección abajo. -->

## 01 — Hero

<!-- GUÍA: el hero de la competencia (Adhoc) vende "el sistema que integra
todo". Nosotros diferenciamos por el problema + el soporte humano, que es
la ventaja competitiva real de Eynes frente a jugadores más grandes. El
badge de Silver Partner va arriba del H1: es la señal de confianza más
rápida de leer para alguien que no distingue un partner serio de uno
improvisado (badge centralizado en 00-config/site.md). -->

- **Badge:** (tomado de `00-config/site.md → badge_partner`)
- **H1:** [COMPLETAR — propuesta de valor centrada en el problema]
- **Subtítulo:** [COMPLETAR — a quién ayuda y cómo: rápido, sin fricción, soporte real]
- **CTA primario:** Agendar demo → `/demo`
- **CTA secundario:** Ver módulos → `/modulos`
- **Imagen/animación:** [COMPLETAR — dashboard real de Odoo en uso, nunca foto de stock]

## 02 — Prueba social inmediata

<!-- GUÍA: reduce la fricción de entrada del visitante frío. Va justo
debajo del hero, antes de pedir cualquier esfuerzo de lectura. Los datos
(empresas, años, países, logos) se completan en 00-config/site.md →
prueba_social_home para no duplicarlos. -->

`+[empresas] EMPRESAS · [años] AÑOS · [países] PAÍSES` — fila de logos de clientes (marquee o grilla estática).

## 03 — Selector de verticales

<!-- GUÍA: patrón central que también usa Adhoc y funciona porque el
visitante se identifica con su industria antes que con un módulo técnico.
Cada card linkea a su página en 02-verticales/. Mantener solo los rubros
que ya tienen página propia con contenido real — no linkear a un rubro
sin página. -->

**Título de sección:** "Elegí tu rubro" / "Trabajamos con empresas como la tuya"

- Distribución y mayoristas → `/verticales/distribucion-y-mayoristas`
- Materiales eléctricos y ferreterías → `/verticales/materiales-electricos-y-ferreterias`
- Servicios / consultoría / IT → `/verticales/servicios-consultoria-it`
- Ver todos los rubros → `/verticales`

## 04 — Problemas → Solución

<!-- GUÍA: vende dolor → alivio, no feature → feature. Banco de frases
reutilizable en 00-config/ctas-reutilizables.md. Cada tarjeta linkea al
módulo correspondiente. -->

| Dolor | Alivio | Link |
|---|---|---|
| "Facturo en un sistema y vendo en otro" | Ventas + Facturación ARCA integradas | `/modulos/ventas-y-crm` |
| "No sé qué stock tengo en tiempo real" | Inventario centralizado | `/modulos/inventario` |
| "Mis reportes tardan días" | Reporting en vivo | `/modulos/contabilidad-y-finanzas` |

## 04b — Banner de Localización Argentina

<!-- GUÍA: como es "un gran módulo en sí mismo" y tiene página propia con
jerarquía de nav, en el Home NO puede quedar como una card chiquita igual
a Ventas o Compras — necesita un banner propio que la distinga del resto
antes de entrar a la grilla genérica de módulos. -->

> **La localización argentina más completa del mercado:** ARCA, IIBB, percepciones y más → `/localizacion-argentina`

## 05 — Grilla completa de módulos (resumen)

<!-- GUÍA: se mantiene porque ya existe hoy en el sitio, pero como resumen
visual, no como el contenido principal — cada card linkea a su página de
módulo propia. Localización queda afuera de esta grilla porque ya tiene
su banner propio arriba (04b). Actualizar esta lista si se suma o saca un
módulo de 03-modulos/. -->

- Ventas y CRM
- Contabilidad
- Compras
- Marketing
- Manufactura
- Inventario
- Punto de venta
- RRHH

## 06 — Caso de éxito destacado

<!-- GUÍA: un caso real con números vale más que 10 features listadas.
Formato tomado de Adhoc (país, usuarios, módulos, resultado). Elegir acá
el caso de 04-casos-de-exito/ con mejor resultado cuantificado y
mantenerlo actualizado; no dejar siempre el mismo caso "para siempre". -->

- **Cliente destacado:** [COMPLETAR — referenciar slug de `04-casos-de-exito/`]
- **Resumen:** "[rubro] — [usuarios] usuarios — [país]"
- **Resultado cuantificado:** [COMPLETAR ej. "-40% tiempo de facturación"]
- Link: → Ver caso completo

## 07 — Por qué Eynes

<!-- GUÍA: sección explícita de objeciones ("¿por qué Eynes y no otro
partner de Odoo?"). La competencia no la tiene tan clara — es una
oportunidad de diferenciación real, siempre que los tres puntos sean
verificables (no marketing vacío). -->

- [COMPLETAR — confirmar "20+ años de experiencia" contra `00-config/site.md → antiguedad`]
- Soporte humano, no ticket genérico
- Equipo local en [COMPLETAR cantidad] ubicaciones

## 08 — CTA final calificador

<!-- GUÍA: doble canal — el formulario calificador alimenta al CRM con
datos de segmentación (rubro, cantidad de usuarios); WhatsApp para el que
quiere resolver ya, típico en Argentina. Copy centralizado en
00-config/ctas-reutilizables.md. -->

"Contanos tu proyecto" + beneficios de la demo (sin compromiso, 1 hora, te llevás un presupuesto) → botón **Agendar demo** + **WhatsApp directo**.

## 08b — Teaser de blog

<!-- GUÍA: mantiene el Home "vivo" para Google (contenido que se actualiza
seguido) y le da a las notas del blog una segunda puerta de entrada además
del buscador y LinkedIn. Actualizar manualmente con las 3 notas más
recientes o de mejor performance de 05-blog/posts/. -->

**Título de sección:** "Últimas notas" / "Recursos para tu empresa"

- [COMPLETAR — nota 1, título + tiempo de lectura]
- [COMPLETAR — nota 2]
- [COMPLETAR — nota 3]

## Footer

Contenido dinámico desde `00-config/navegacion.md` y `00-config/site.md` (oficinas, enlaces rápidos, redes, legal). No duplicar acá.

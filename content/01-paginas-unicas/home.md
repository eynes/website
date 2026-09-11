---
title: "¿Facturás en un sistema y vendés en otro?"
seo_title: "Odoo en Argentina | Implementación y Soporte Local — Eynes"
meta_description: "Centralizá ventas, stock y facturación ARCA en un solo sistema. Implementación de Odoo con soporte humano real: +150 clientes, +20 años, 6 países."
slug: "home"
url: "eynes.com.ar"
schema_type: "Organization"
estado: "publicado"
og_image: ""
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
- **H1:** ¿Facturás en un sistema y vendés en otro?
<!-- GUÍA copy: H1 reformulado como pregunta retórica que usa la frase
textual del banco de "dolor" ya validado en 00-config/ctas-reutilizables.md
→ "Dolor → alivio". Lenguaje del cliente, no de la empresa: es más
específico que una afirmación abstracta tipo "centralizá tu información". -->
- **Subtítulo:** Con Odoo, vendés, facturás con ARCA y controlás el stock desde un solo sistema — implementado por un equipo con 20+ años y soporte humano real, no un ticket genérico.
- **CTA primario:** Agendar demo → `/demo`
- **CTA secundario:** Ver módulos → `/modulos`
<!-- GUÍA: imagen/animación pendiente — dashboard real de Odoo en uso,
nunca foto de stock. Candidatos reales: pantalla de Portal de Clientes
(caso Supply Parts) o de facturación ARCA (caso Clínica IMA). Hasta
tener esa captura, el hero del sitio queda a una columna, sin placeholder
visual que parezca "en construcción". -->

## 02 — Prueba social inmediata

<!-- GUÍA: reduce la fricción de entrada del visitante frío. Va justo
debajo del hero, antes de pedir cualquier esfuerzo de lectura. Los datos
(empresas, años, países, logos) se completan en 00-config/site.md →
prueba_social_home para no duplicarlos. -->

`+[empresas] EMPRESAS · [años] AÑOS · [países] PAÍSES` — fila de logos de clientes (marquee o grilla estática).

## 03 — Selector de verticales

<!-- GUÍA: patrón central que también usa Adhoc y funciona porque el
visitante se identifica con su industria antes que con un módulo técnico.
Ya no es una selección manual de 3-4 rubros: los 23 rubros vienen del
Excel fuente (content/eynes_portfolio_rubros_consolidado.xlsx) vía
site/scripts/sync-portfolio.py, agrupados por "Agrupador principal" (10
grupos) con el mismo color por grupo que usa el mega-menú y /sectores —
ver site/src/lib/sectorGroups.ts. Sumar un rubro nuevo es agregar su fila
al Excel, no editar esta página. -->

**Título de sección:** "Trabajamos con empresas como la tuya"

Lista agrupada por rubro (10 grupos, 23 rubros en total) + "Ver todos los rubros" → `/sectores`

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

<!-- GUÍA: resumen visual, no el contenido principal — cada card linkea a
su página de módulo propia (fuente: content/03-modulos/_hub.md). Hoy solo
hay 4 módulos con página propia; no listar acá Marketing, Manufactura,
Punto de venta ni RRHH hasta que tengan su .md real en 03-modulos/ (evita
un link roto). Localización queda afuera de esta grilla porque ya tiene
su banner propio arriba (04b). -->

- Ventas y CRM
- Contabilidad y finanzas
- Inventario
- Compras

## 06 — Caso de éxito destacado

<!-- GUÍA: un caso real con números vale más que 10 features listadas.
Formato tomado de Adhoc (país, usuarios, módulos, resultado). Elegir acá
el caso de 04-casos-de-exito/ con mejor resultado cuantificado y
mantenerlo actualizado; no dejar siempre el mismo caso "para siempre". -->

- **Cliente destacado:** Supply Parts (`04-casos-de-exito/supply-parts`)
- **Resumen:** "Repuestos y autopartes" (los campos `pais` y `usuarios` quedan vacíos hoy — el Excel fuente no trae esos dos datos por cliente; si se consiguen, se cargan en `eynes_portfolio_rubros_consolidado.xlsx` y se propagan solos vía `sync-portfolio.py`, no hace falta tocar el template).
- **Resultado cuantificado:** Sin cifra porcentual verificada por el cliente — el resultado real y documentado es cualitativo: "las cuentas corrientes y el cupo de crédito se liberan al instante cuando el distribuidor reporta su pago, sin carga manual" (antes tardaba días). No inventamos un % que el cliente no dijo.
- Link: → Ver caso completo

<!-- GUÍA cumplida: de los 29 casos del Excel fuente, ninguno trae un
porcentaje de mejora dicho por el cliente — todos son resultados
cualitativos verificados (`resultado_clave` en cada .md, generado por
sync-portfolio.py). Si en el futuro se consigue una cifra real
(ej. "reducimos X días a Y horas"), se carga en el Excel, no acá. -->

## 07 — Por qué Eynes

<!-- GUÍA: sección explícita de objeciones ("¿por qué Eynes y no otro
partner de Odoo?"). La competencia no la tiene tan clara — es una
oportunidad de diferenciación real, siempre que los tres puntos sean
verificables (no marketing vacío). -->

- **20+ años y +150 clientes.** Fundada en 2006, Silver Partner Oficial de Odoo — no un revendedor de un mes.
- **Soporte humano, no ticket genérico.** Hablás con la misma gente que te implementó el sistema.
- **Presencia real en 5 ciudades.** Oficina en Buenos Aires y atención local con teléfono dedicado en Santa Fe, Mendoza, Montevideo y Valencia/Castellón.

## 08 — CTA final

<!-- GUÍA: doble canal, sin formulario — el botón lleva directo al
calendario (Google Calendar) para reservar horario; WhatsApp para el que
quiere resolver ya, típico en Argentina. La calificación del lead (rubro,
cantidad de usuarios) ya no se hace con un formulario previo: se hace en
vivo durante la reunión. Copy centralizado en
00-config/ctas-reutilizables.md. -->

"Contanos tu proyecto" + beneficios de la demo (sin compromiso, 30 minutos, te llevás un presupuesto) → botón **Agendar reunión** + **WhatsApp directo**.

## Footer

Contenido dinámico desde `00-config/navegacion.md` y `00-config/site.md` (oficinas, enlaces rápidos, redes, legal). No duplicar acá.

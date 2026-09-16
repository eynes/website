---
title: "Soluciones por rubro"
seo_title: "Odoo por Rubro: Soluciones para tu Industria | Eynes"
meta_description: "Descubrí cómo Odoo se adapta a tu industria: agroindustria, salud, energía, tecnología y otros 19 rubros más, con casos reales de implementación de Eynes."
slug: "verticales"
url: "eynes.com.ar/sectores"
schema_type: "CollectionPage"
estado: "publicado"
---

<!-- GUÍA (actualizada — el Excel ya no genera contenido; ver nota abajo):
esta página lista los 23 rubros reales del portfolio de Eynes, agrupados
en 10 categorías ("Agrupador principal"). El contenido de cada rubro
(problemas, módulos, integraciones, FAQs) vive directamente en
content/02-verticales/*.md y se edita a mano ahí — sumar un rubro nuevo
es crear su .md siguiendo _PLANTILLA.md. El agrupador y su color
(site/src/lib/sectorGroups.ts) son los mismos en el mega-menú de Nav,
acá y en la home.

GUÍA — Excel desconectado (16/09/2026): content/eynes_portfolio_rubros_consolidado.xlsx
ya NO alimenta el sitio. site/scripts/sync-portfolio.py sigue en el repo
como referencia histórica pero no corre en predev/prebuild (ver
site/package.json). Los .md de esta carpeta son ahora la única fuente de
verdad — se editan directamente. -->

## 01 — Encabezado

"Sectores" (H1 corto) — sin intro larga, la grilla agrupada de abajo ya comunica la variedad de rubros de un vistazo.

## 02 — Grilla de rubros

Lista agrupada por categoría (`sector-columns` en el template), 10 grupos con 23 rubros en total. Cada rubro linkea a `/sectores/[slug]`.

## 03 — CTA

"¿No encontrás tu rubro? Contanos tu caso igual" → Agendar demo (`/demo`)

<!-- GUÍA: evita perder al visitante cuyo rubro no está entre los 23 ya documentados. -->

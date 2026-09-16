---
title: "Casos de éxito"
seo_title: "Casos de Éxito con Odoo en Argentina | Eynes"
meta_description: "Más de 150 empresas ya centralizaron ventas, stock y facturación ARCA con Odoo y Eynes. Conocé los casos reales, por rubro y resultado."
slug: "casos"
url: "eynes.com.ar/casos"
schema_type: "CollectionPage"
estado: "publicado"
---

## 01 — Filtros

<!-- GUÍA (actualizada): nunca se implementaron. La página hoy es una
grilla estática con los 29 casos (`site/src/pages/casos/index.astro`),
sin filtro de rubro/usuarios/país. Si se prioriza, implementar client-side
sobre los mismos datos (`rubro`, `usuarios`, `pais` de cada ficha) en vez
de agregar un backend. -->

Sin filtros implementados hoy.

## 02 — Grilla de casos

<!-- GUÍA (actualizada — el Excel ya no genera contenido): ya no hay una
lista de "7 casos completos + 23 pendientes" — los 29 clientes tienen su
ficha completa (problema, solución, testimonio EL DESAFÍO/LA SOLUCIÓN/EL
RESULTADO, módulos, FAQs) en content/04-casos-de-exito/*.md, editada a
mano. Sumar un cliente nuevo es crear su .md siguiendo _PLANTILLA.md — no
tocar un Excel. El listado real y sus datos por cliente viven en las 29
fichas de esta carpeta (una por `slug`), no acá.

Los campos `pais` y `usuarios` quedan vacíos en algunas fichas porque
ese dato nunca se relevó para ese cliente — completar a mano en el
frontmatter de la ficha correspondiente cuando se consiga.

GUÍA — Excel desconectado (16/09/2026): content/eynes_portfolio_rubros_consolidado.xlsx
ya NO alimenta el sitio. site/scripts/sync-portfolio.py sigue en el repo
como referencia histórica pero no corre en predev/prebuild (ver
site/package.json). -->

Formato de ficha (rubro, país, usuarios, módulos y UN resultado
cualitativo verificado — nunca un % que el cliente no dijo) sigue siendo
el estándar; ninguno de los 29 casos trae una cifra porcentual de mejora
dicha por el cliente. -->

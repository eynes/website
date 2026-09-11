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

<!-- GUÍA (actualizada): ya no hay una lista de "7 casos completos + 23
pendientes" — los 29 clientes del Excel fuente
(content/eynes_portfolio_rubros_consolidado.xlsx) tienen hoy su ficha
completa (problema, solución, testimonio EL DESAFÍO/LA SOLUCIÓN/EL
RESULTADO, módulos, FAQs), generada automáticamente por
site/scripts/sync-portfolio.py. Sumar un cliente nuevo es agregar su fila
al Excel y correr el sync — no crear un .md a mano ni editar esta lista,
que quedaría desactualizada de nuevo. El listado real y sus datos por
cliente viven en las 29 fichas de esta carpeta (una por `slug`), no acá.

Los campos `pais` y `usuarios` quedan vacíos en todas las fichas porque
el Excel fuente no trae esas dos columnas por cliente — si se consiguen,
se cargan en el Excel y se propagan solas.

Formato de ficha (rubro, país, usuarios, módulos y UN resultado
cualitativo verificado — nunca un % que el cliente no dijo) sigue siendo
el estándar; ninguno de los 29 casos trae una cifra porcentual de mejora
dicha por el cliente. -->

---
title: "Exportadores impositivos para Argentina"
seo_title: "Exportadores impositivos para Argentina | Eynes"
meta_description: "Generá archivos impositivos desde las operaciones registradas, con formatos y controles específicos para cada régimen y versión."
slug: "exportadores-impositivos"
url: "/localizacion-argentina/exportadores-impositivos"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Operar y cerrar"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿IVA Simple tiene un asistente distinto?", "respuesta": "En el código revisado es una modalidad del asistente de Libro IVA, activada mediante is_simple_vat."}, {"pregunta": "¿Exportar equivale a presentar ante el organismo?", "respuesta": "No. Los exportadores generan archivos; el envío digital solo debe describirse cuando se identifica y valida un servicio específico."}, {"pregunta": "¿Los formatos son iguales en todas las versiones?", "respuesta": "No. Hay exportadores adicionales en 17 y diferencias en formatos y opciones del asistente."}]
---

## 01 — Texto para el sitio

Generá archivos impositivos desde las operaciones registradas, con formatos y controles específicos para cada régimen y versión.

## 02 — El problema que resuelve

Volver a armar los comprobantes para cada aplicativo fiscal duplica trabajo y puede perder el vínculo con el dato contable. Los exportadores seleccionan operaciones por período y generan las estructuras del régimen configurado.

## 03 — Alcance funcional

- ARCIBA y ARBA, con asistentes y estructuras de archivos para retenciones/percepciones según cada formato.
- Libro IVA Digital e IVA Simple: comparten el asistente `create_libro_iva`, con una opción `is_simple_vat` que cambia el tratamiento de determinadas operaciones.
- SICORE y SIFERE con configuraciones, asistentes y formatos de longitud fija.
- Archivos de percepciones y retenciones de IVA sufridas.
- A122R Digital de ARBA: envío de retenciones y comprobantes remotos. El rótulo del Excel “Lotes A122R” requiere precisar si se refiere a envío múltiple o a un formato de archivo; el exportador TXT general no prueba un formato de lote A122R.
- En 17 se encontraron exportadores adicionales para SIRCAR, SIPOT (percepciones de Salta), SIRETPER (Tucumán) e IIBB Misiones; sus imports y vistas están declarados en el módulo.
- En 17/19 el asistente de Libro IVA incorpora elección TXT/XLSX; 15 debe describirse con el formato efectivamente disponible en su asistente.

## 04 — Diferencias por versión

Los exportadores principales del Excel aparecen en 15, 17 y 19. Los cuatro exportadores provinciales adicionales citados se encontraron en 17 y no en las otras dos ramas. A122R Digital aparece en las tres; no es una novedad exclusiva de 19. En 19, el exportador TXT de retenciones ARBA se bloquea si `arba_a122r_enforced` está activo. No se localizó esa comprobación en el mismo asistente de 15/17.

## 05 — Condiciones y límites del mensaje

No afirmar que un archivo fue aceptado por el organismo sin una prueba del período y formato. No confundir exportación con presentación automática ni atribuir un régimen a todas las provincias. Las alícuotas y fechas comentadas en el código no se usan como guía normativa pública.

## 06 — Demostración sugerida

Elegir compañía y período, generar Libro IVA/IVA Simple, revisar comprobantes y archivos. Mostrar un exportador provincial con su configuración y comparar sus datos con las retenciones/percepciones del sistema. Para ARBA Digital, usar la ficha de servicios.

## 07 — Temas del Excel vinculados

- `Exportadores-1` · Exportador arciba
- `Exportadores-2` · Exportador ARBA
- `Exportadores-3` · Exportador Libro IVA Digital
- `Exportadores-4` · Exportador IVA Simple
- `Exportadores-5` · Exportador SICORE
- `Exportadores-6` · Exportador SIFERE
- `Exportadores-7` · Lotes A122R de ARBA
- `Exportadores-8` · Archivos de percepciones y retenciones de IVA sufridas

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/wizard/arba_retention_exporter.py:27`
- `l10n_ar_eynes/wizard/create_arciba_file.py:720`
- `l10n_ar_eynes/wizard/create_iva_per_ret_files.py:230`
- `l10n_ar_eynes/wizard/create_libro_iva.py:907`
- `l10n_ar_eynes/wizard/create_sicore_file.py:44`
- `l10n_ar_eynes/wizard/create_sifere_file.py:131`

### Rama 17.0

- `l10n_ar_eynes/wizard/arba_retention_exporter.py:27`
- `l10n_ar_eynes/wizard/create_arciba_file.py:669`
- `l10n_ar_eynes/wizard/create_iva_per_ret_files.py:222`
- `l10n_ar_eynes/wizard/create_libro_iva.py:884`
- `l10n_ar_eynes/wizard/create_sicore_file.py:44`
- `l10n_ar_eynes/wizard/create_sifere_file.py:142`

### Rama 19.0

- `l10n_ar_eynes/wizard/arba_retention_exporter.py:27`
- `l10n_ar_eynes/wizard/create_arciba_file.py:680`
- `l10n_ar_eynes/wizard/create_iva_per_ret_files.py:222`
- `l10n_ar_eynes/wizard/create_libro_iva.py:884`
- `l10n_ar_eynes/wizard/create_sicore_file.py:44`
- `l10n_ar_eynes/wizard/create_sifere_file.py:140`

**Ampliación de código en 17:** `l10n_ar_eynes/wizard/sircar_exporter.py`, `sipot_perception_exporter.py`, `siretper_exporter.py`, `create_misiones_iibb_file.py`; revisar sus imports en `wizard/__init__.py` y las vistas declaradas en `__manifest__.py`.

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

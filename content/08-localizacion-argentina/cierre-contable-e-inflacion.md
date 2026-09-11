---
title: "Cierre contable y ajuste por inflación"
seo_title: "Cierre contable y ajuste por inflación | Eynes"
meta_description: "Organizá el cierre del ejercicio con controles de movimientos, asientos de cierre y apertura, e índices para el cálculo de RECPAM."
slug: "cierre-contable-e-inflacion"
url: "/localizacion-argentina/cierre-contable-e-inflacion"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Operar y cerrar"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿El sistema descarga los índices automáticamente?", "respuesta": "No se encontró evidencia de descarga automática en el modelo de índices revisado; dispone de fecha y coeficiente para su carga."}, {"pregunta": "¿Puedo revisar los asientos del cierre?", "respuesta": "El proceso conserva referencias a movimientos de cierre, apertura, resultados y RECPAM según sus opciones."}, {"pregunta": "¿El cierre usa configuración contable propia de la empresa?", "respuesta": "Sí. Incluye cuentas, diarios y opciones que deben definirse para el ejercicio y el tratamiento requerido."}]
---

## 01 — Texto para el sitio

Organizá el cierre del ejercicio con controles de movimientos, asientos de cierre y apertura, e índices para el cálculo de RECPAM.

## 02 — El problema que resuelve

El cierre necesita reunir saldos, detectar movimientos pendientes y aplicar criterios consistentes de ajuste. La localización incorpora un proceso de cierre con configuración y movimientos identificables.

## 03 — Alcance funcional

- Configuración de ejercicio fiscal y períodos, apoyada en la dependencia `om_fiscal_year`.
- Opciones para detectar movimientos en borrador y asientos desbalanceados antes de continuar.
- Generación de movimientos de resultados, cierre y apertura según las opciones del proceso.
- Mapeo de cuentas y configuración de diarios y descripciones de los asientos resultantes.
- Carga de índices de inflación por fecha, cálculo de coeficientes y generación del movimiento RECPAM.
- Opciones y estados del proceso de cierre, incluyendo recuperación/cancelación y referencias a los asientos generados.
- Validación de períodos y restricciones de movimientos en diarios cerrados.


## 04 — Diferencias por versión

El modelo de cierre, índices y asistente de operaciones está en 15, 17 y 19. Esto respalda documentar el proceso, pero no certifica todos los caminos de cierre con y sin RECPAM. En las tres ramas, `action_confirm` exige un movimiento RECPAM si se utiliza esa transición: probar el flujo sin ajuste que se pretende ofrecer.

## 05 — Condiciones y límites del mensaje

No afirmar descarga automática de índices: el modelo inspeccionado contiene fecha y coeficiente. No prometer estados contables completos ni cumplimiento universal de todas las normas profesionales. El alcance se define con las cuentas, índices, fechas y criterios que configura el equipo contable.

## 06 — Demostración sugerida

Preparar un ejercicio de prueba con movimientos pendientes y comprobar los controles. Cargar índices, ejecutar el proceso, inspeccionar los asientos y sus cuentas. Repetir un cierre sin RECPAM y verificar qué transiciones permite la versión.

## 07 — Temas del Excel vinculados

- `Comprobantes-35` · Generación de asientos de cierre de ejercicio - con/sin RECPAM
- `Comprobantes-39` · Bloqueo de diarios por fecha de cierre
- `Comprobantes-49` · Ejercicios fiscales y períodos contables
- `Comprobantes-71` · Carga de índices de inflación

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/account_move.py:1417`
- `l10n_ar_eynes/models/fiscal_year_closing.py:58`
- `l10n_ar_eynes/models/inflation_index.py:21`
- `l10n_ar_eynes/wizard/fiscal_year_closing_operation_wizard.py:208`

### Rama 17.0

- `l10n_ar_eynes/models/account_move.py:1689`
- `l10n_ar_eynes/models/fiscal_year_closing.py:58`
- `l10n_ar_eynes/models/inflation_index.py:21`
- `l10n_ar_eynes/wizard/fiscal_year_closing_operation_wizard.py:208`

### Rama 19.0

- `l10n_ar_eynes/models/account_move.py:1636`
- `l10n_ar_eynes/models/fiscal_year_closing.py:58`
- `l10n_ar_eynes/models/inflation_index.py:21`
- `l10n_ar_eynes/wizard/fiscal_year_closing_operation_wizard.py:208`

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

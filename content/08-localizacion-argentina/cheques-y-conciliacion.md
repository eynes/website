---
title: "Gestión de cheques propios y de terceros"
seo_title: "Gestión de cheques propios y de terceros | Eynes"
meta_description: "Seguí cada cheque desde su emisión o recepción hasta su entrega, depósito, acreditación, débito o rechazo, con sus movimientos contables."
slug: "cheques-y-conciliacion"
url: "/localizacion-argentina/cheques-y-conciliacion"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Cobrar y pagar"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿Puedo usar un cheque recibido para pagar a un proveedor?", "respuesta": "El circuito admite entregar cheques de terceros y conservar los vínculos de origen y destino."}, {"pregunta": "¿El sistema se conecta al banco para emitir eCheqs?", "respuesta": "El código revisado acredita registro y gestión del instrumento. No se encontró evidencia suficiente para anunciar emisión bancaria por API."}, {"pregunta": "¿Se pueden imprimir cheques?", "respuesta": "Hay módulos de impresión por plantilla en 17 y 19. Requieren configuración y dependencias adicionales."}]
---

## 01 — Texto para el sitio

Seguí cada cheque desde su emisión o recepción hasta su entrega, depósito, acreditación, débito o rechazo, con sus movimientos contables.

## 02 — El problema que resuelve

Una cartera de cheques mantenida en una planilla pierde fácilmente el vínculo con el cliente, el proveedor y el asiento. El sistema conserva esos vínculos y permite consultar las fechas y el estado del instrumento.

## 03 — Alcance funcional

- Configuración contable de cheques, cuentas de diferidos y rechazos, diarios y productos para notas por rechazo.
- Varias chequeras y asistente de creación; formatos físico, electrónico y virtual registrados en el sistema.
- Cheques propios y de terceros, comunes y diferidos, con moneda, cotización, fechas y datos del firmante.
- Estados para cartera, entrega a proveedor, depósito, acreditación y rechazo de terceros; estados de emisión y débito para propios, además de cancelación y vencimiento donde corresponda.
- Operaciones y asientos asociados a depósito, débito, acreditación y rechazo; generación de nota de débito por cheque rechazado con configuración previa.
- Endoso/entrega de cheques de terceros a proveedores y calendarios de seguimiento.
- Operaciones sobre varios cheques en asistentes específicos. El cambio genérico de estado no admite cualquier selección masiva.
- Impresión sobre plantillas mediante addon adicional en 17 y 19.
- Complemento de conciliación para actualizar estados de cheque en 15 y 19.

## 04 — Diferencias por versión

El núcleo de cheques está en las tres ramas. `l10n_ar_reconciliation` existe en 15 y 19, con implementaciones diferentes, y no está en 17. La impresión usa `custom_print_check` en 17 y `print_check` en 19, ambos con dependencia de `sign_oca`; no se encontró un equivalente en 15.

## 05 — Condiciones y límites del mensaje

Registrar un eCheq no demuestra conexión con una API bancaria para emitirlo o endosarlo. La impresión requiere plantilla, campos y dependencias. En 19 la conciliación completa actualiza los estados y utiliza el asiento de conciliación; no sumar un segundo asiento manual sin revisar el circuito. No prometer cualquier transición masiva.

## 06 — Demostración sugerida

Recibir un cheque, verlo en cartera y calendario, entregarlo a un proveedor o depositarlo. Mostrar un rechazo con su documento asociado. Demostrar la actualización por conciliación y la impresión como circuitos opcionales según versión.

## 07 — Temas del Excel vinculados

- `Comprobantes-15` · Creación de cheques de distintos tipos (echeq, físico, virtual)
- `Cheques-1` · Gestión de tipos de chequeras (echeq, virtuales, físicos)
- `Cheques-2` · Configuración de la contabilidad a utilizar en chequeres
- `Cheques-3` · Gestión de multiples chequeras
- `Cheques-4` · Gestión de cheques propios y de terceros
- `Cheques-5` · Cheques comunes y diferidos
- `Cheques-6` · Asistente de creación de chequeras
- `Cheques-7` · Estados del cheque propio
- `Cheques-8` · Estados del cheque de terceros
- `Cheques-9` · Depósito, acreditación, débito y rechazo de cheques
- `Cheques-10` · Nota de débito automática por cheque rechazado
- `Cheques-11` · Endoso de cheques de terceros a proveedores
- `Cheques-12` · Cambio de estado masivo de cheques
- `Cheques-13` · Calendarios de cheques
- `Cheques-14` · Cheques en moneda extranjera
- `Cheques-15` · Actualización del estado del cheque al conciliar
- `Cheques-16` · Impresión de cheques

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/account_check.py:173`
- `l10n_ar_eynes/views/account_check_views.xml:629`
- `l10n_ar_eynes/wizard/account_check_change_state.py:50`
- `l10n_ar_eynes/wizard/create_checkbook_wizard.py:32`
- `l10n_ar_eynes/wizard/debit_check_wizard.py:26`
- `l10n_ar_eynes/wizard/deposit_check_wizard.py:110`
- `l10n_ar_eynes/wizard/reject_check_wizard.py:196`
- `l10n_ar_reconciliation/models/account_move_line.py:7`

### Rama 17.0

- `custom_print_check/wizard/print_check_wizard.py:11`
- `l10n_ar_eynes/models/account_check.py:171`
- `l10n_ar_eynes/views/account_check_views.xml:559`
- `l10n_ar_eynes/wizard/account_check_change_state.py:81`
- `l10n_ar_eynes/wizard/create_checkbook_wizard.py:49`
- `l10n_ar_eynes/wizard/debit_check_wizard.py:26`
- `l10n_ar_eynes/wizard/deposit_check_wizard.py:110`
- `l10n_ar_eynes/wizard/reject_check_wizard.py:196`

### Rama 19.0

- `l10n_ar_eynes/models/account_check.py:173`
- `l10n_ar_eynes/views/account_check_views.xml:569`
- `l10n_ar_eynes/wizard/account_check_change_state.py:51`
- `l10n_ar_eynes/wizard/create_checkbook_wizard.py:49`
- `l10n_ar_eynes/wizard/debit_check_wizard.py:26`
- `l10n_ar_eynes/wizard/deposit_check_wizard.py:149`
- `l10n_ar_eynes/wizard/reject_check_wizard.py:196`
- `l10n_ar_reconciliation/models/account_full_reconcile.py:20`
- `print_check/wizard/print_check_wizard.py:10`

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

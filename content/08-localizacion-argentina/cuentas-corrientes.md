---
title: "Cuenta corriente y composición de saldos"
seo_title: "Cuenta corriente y composición de saldos | Eynes"
meta_description: "Consultá la cuenta corriente por período y la composición de los saldos pendientes actuales de clientes y proveedores."
slug: "cuentas-corrientes"
url: "/localizacion-argentina/cuentas-corrientes"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Cobrar y pagar"
fuente_principal: "origin/17.0:customer_balance_history (commit registrado en _fuentes/ramas.json)"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿Puedo consultar clientes y proveedores?", "respuesta": "El módulo incluye asistentes y reportes para ambos tipos de cuenta."}, {"pregunta": "¿Puedo obtener el informe en PDF?", "respuesta": "Sí. Los asistentes ofrecen PDF y una exportación .xls construida como tabla HTML; esta última no es XLSX nativo."}]
---

## 01 — Texto para el sitio

Consultá la cuenta corriente por período y la composición de los saldos pendientes actuales de clientes y proveedores.

## 02 — El problema que resuelve

La cuenta corriente permite revisar movimientos de un período. La composición muestra qué partidas siguen pendientes al momento de la consulta. El módulo ofrece ambos reportes, pero no reconstruye las partidas abiertas a una fecha histórica: utiliza el residual y la conciliación actuales.

## 03 — Alcance funcional

- Asistentes separados para clientes y proveedores.
- Selección de contactos, fechas y tipo de reporte.
- Estado de cuenta corriente con movimientos y saldos.
- Composición de partidas actualmente no conciliadas y su importe residual actual, filtradas por fecha de emisión. Los días de atraso se calculan respecto de hoy.
- Salida PDF y exportación `.xls` basada en una tabla HTML, mediante acciones de los asistentes. No es un archivo XLSX nativo. Acceso desde el contacto o los menús del módulo.
- Dependencias de contabilidad, contactos, ventas y localización.


## 04 — Diferencias por versión

`customer_balance_history`, versión `17.0.1.0.0`, se encontró únicamente en `origin/17.0`, con `installable: True`. No está en las referencias 15 o 19 de este repositorio; no inferir que la funcionalidad esté portada.

## 05 — Condiciones y límites del mensaje

La composición consulta `reconciled=False` y `amount_residual` actuales; no deshace conciliaciones posteriores al corte elegido. Una factura totalmente pagada después del corte puede desaparecer de esa composición. El estado de cuenta usa movimientos y saldos por período: no confundir ambos reportes ni anunciar una reconstrucción histórica de partidas abiertas. Contrastar además pagos parciales y monedas en una prueba funcional.

## 06 — Demostración sugerida

Tomar facturas de un período y un pago posterior. Comparar el estado de cuenta del período con la composición pendiente actual y mostrar por qué pueden diferir. Repetir con un proveedor y exportar PDF y XLS.

## 07 — Temas del Excel vinculados

Ampliación encontrada en código; no hay una fila específica en el Excel.

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

**Lógica revisada en 17:** `customer_balance_history/wizard/customer_balance_history_wizard.py:180` (filtro de conciliación actual), `:268` (residual actual), `:375` (cuenta corriente), `:446` (composición), `:101` y `:544` (exportación XLS/HTML). El asistente de proveedores replica este enfoque en `supplier_balance_history_wizard.py:256` y `:432`.

**Fuentes en 17:** `customer_balance_history/__manifest__.py`; `wizard/customer_balance_history_wizard.py`; `wizard/supplier_balance_history_wizard.py`; `report/customer_balance_history_reports.xml`; `report/supplier_balance_history_reports.xml`.

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

---
title: "Integraciones con ARCA y ARBA"
seo_title: "Integraciones con ARCA y ARBA | Eynes"
meta_description: "Conectá la facturación y las retenciones con los servicios configurados, y conservá las solicitudes y respuestas asociadas a la operación."
slug: "servicios-arca-y-arba"
url: "/localizacion-argentina/servicios-arca-y-arba"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Facturar y vender"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿CAE y CAEA son lo mismo?", "respuesta": "No. El código acredita el circuito CAE de facturación electrónica. No se encontró implementación local de CAEA."}, {"pregunta": "¿Puedo consultar lo que pasó con una factura?", "respuesta": "Hay solicitudes y respuestas asociadas, consultas de comprobantes y asistentes de sincronización."}, {"pregunta": "¿ARBA Digital solo genera un archivo?", "respuesta": "La implementación A122R incorpora comunicación con el servicio, estados, registros de solicitudes y recuperación de PDF. Su operación necesita configuración y validación."}]
---

## 01 — Texto para el sitio

Conectá la facturación y las retenciones con los servicios configurados, y conservá las solicitudes y respuestas asociadas a la operación.

## 02 — El problema que resuelve

Cuando una autorización falla o un comprobante quedó informado fuera del sistema, administración necesita entender qué ocurrió antes de repetir una operación. La localización conserva datos de solicitudes y dispone de consultas y asistentes de sincronización.

## 03 — Alcance funcional

- WSAA: configuración de certificados y autenticación, con separación de homologación y producción.
- WSFE para autorización y consulta de comprobantes locales; WSFEX para exportación y sus tablas auxiliares.
- Consulta de constancia de inscripción mediante el servicio de padrón de ARCA.
- Carga de tablas de monedas, impuestos, puntos de venta y otros catálogos utilizados por los servicios.
- Consulta y sincronización de comprobantes, incluidos asistentes de sincronización masiva.
- Solicitudes vinculadas al comprobante, detalles de respuesta y errores para revisar el proceso.
- A122R Digital de ARBA: configuración por compañía/actividad, declaraciones por período, envío de retenciones, seguimiento de estados, registros de solicitudes, recuperación de comprobantes, descarga PDF y asistentes de diagnóstico/reproceso.
- WSFECRED: implementación parcial localizada que requiere revisión de registro del modelo.
- WSLP y CAEA: alcance declarado en el Excel, sin implementación localizada en estas ramas.

## 04 — Diferencias por versión

WSAA, WSFE, WSFEX, padrón, sincronización y A122R Digital se encontraron en 15, 17 y 19. `wsfecred.py` existe en las tres sin import directo en `models/__init__.py`. La búsqueda de WSLP y CAEA no encontró implementación local. No se inspeccionó internamente la biblioteca externa pyafipws para atribuir servicios adicionales.

## 05 — Condiciones y límites del mensaje

Los certificados, habilitaciones, conectividad y configuración son requisitos de la integración. Tener endpoints y métodos no prueba aceptación en producción. WSFECRED localizado consulta obligatoriedad de recepción FCE; no se debe ampliar el mensaje a todo el ciclo financiero de FCE. Las opciones de reenvío o borrado remoto de A122R requieren controles para evitar duplicados.

## 06 — Demostración sugerida

Autorizar una factura en homologación, revisar una respuesta y consultar un comprobante. Para ARBA, enviar una retención de prueba, revisar el estado y recuperar el PDF. Demostrar diagnóstico/reproceso con datos de ensayo y sin transacciones reales.

## 07 — Temas del Excel vinculados

- `Webservice-1` · WSFE
- `Webservice-2` · WSFEX
- `Webservice-3` · WSLP
- `Webservice-4` · CAEA
- `Webservice-5` · WS Padrón (constancia de inscripción)
- `Webservice-6` · WSFECRED
- `Webservice-7` · Consulta y sincronización de comprobantes con ARCA
- `Webservice-8` · Carga de tablas ARCA
- `Webservice-9` · A122R Digital de ARBA

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/models/arba_a122r.py:2204`
- `l10n_ar_eynes/models/ws_padron.py:38`
- `l10n_ar_eynes/models/wsfe.py:302`
- `l10n_ar_eynes/models/wsfecred.py:40`
- `l10n_ar_eynes/models/wsfex.py:686`
- `l10n_ar_eynes/wizard/afip_sinchronize_voucher.py:139`
- `l10n_ar_eynes/wizard/wsfe_massive_sinchronize.py:67`

### Rama 17.0

- `l10n_ar_eynes/models/arba_a122r.py:2214`
- `l10n_ar_eynes/models/ws_padron.py:38`
- `l10n_ar_eynes/models/wsfe.py:203`
- `l10n_ar_eynes/models/wsfecred.py:40`
- `l10n_ar_eynes/models/wsfex.py:686`
- `l10n_ar_eynes/wizard/afip_sinchronize_voucher.py:152`
- `l10n_ar_eynes/wizard/wsfe_massive_sinchronize.py:67`

### Rama 19.0

- `l10n_ar_eynes/models/arba_a122r.py:2213`
- `l10n_ar_eynes/models/ws_padron.py:47`
- `l10n_ar_eynes/models/wsfe.py:203`
- `l10n_ar_eynes/models/wsfecred.py:40`
- `l10n_ar_eynes/models/wsfex.py:686`
- `l10n_ar_eynes/wizard/afip_sinchronize_voucher.py:152`
- `l10n_ar_eynes/wizard/wsfe_massive_sinchronize.py:67`

**Entrada técnica adicional:** `l10n_ar_eynes/models/wsaa.py`, `certificate_request.py`, `wsfe_request.py` y `arba_a122r.py`. Para A122R revisar también `wizard/arba_a122r_diagnostic_wizard.py` y `wizard/arba_a122r_reprocess_wizard.py`.

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

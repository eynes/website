---
title: "Datos fiscales y padrones en Odoo"
seo_title: "Datos fiscales y padrones en Odoo | Eynes"
meta_description: "Centralizá los datos fiscales de clientes y proveedores, sus alícuotas y certificados de exclusión. Usá esa información en la facturación y en los pagos."
slug: "datos-fiscales-y-padrones"
url: "/localizacion-argentina/datos-fiscales-y-padrones"
estado: "publicado"
publicar: true
schema_type: "Service"
agrupador: "Facturar y vender"
fuente_principal: "temas localización.xlsx"
fecha_revision: "2026-09-10"
faqs: [{"pregunta": "¿La consulta fiscal y los padrones provinciales son lo mismo?", "respuesta": "No. La constancia de inscripción se consulta mediante ARCA; las alícuotas por jurisdicción se alimentan mediante el consumidor de un servidor de padrones configurado."}, {"pregunta": "¿Puedo guardar una exclusión con fecha de vencimiento?", "respuesta": "Sí. Las líneas de retención y percepción del contacto incluyen porcentaje de exclusión, vigencia y certificado adjunto."}, {"pregunta": "¿Los padrones se actualizan solos al instalar?", "respuesta": "La actualización periódica requiere activar y configurar la tarea. Además existe una llamada al crear contactos, cuyo comportamiento depende de la configuración del servicio."}]
---

## 01 — Texto para el sitio

Centralizá los datos fiscales de clientes y proveedores, sus alícuotas y certificados de exclusión. Usá esa información en la facturación y en los pagos.

## 02 — El problema que resuelve

Cuando la condición fiscal, el número de IIBB o una exclusión quedan en una planilla separada, cada factura y cada orden de pago exigen volver a revisar los mismos datos. La ficha del contacto reúne esa información para alimentar los circuitos impositivos.

## 03 — Alcance funcional

- Tipo y número de documento; validaciones de CUIT y control de duplicados en contactos.
- Número de inscripción en IIBB, situaciones fiscales y registros por jurisdicción.
- Posiciones fiscales argentinas y catálogos de tipos de documento; localidades propias y provincias apoyadas en los datos base de Odoo.
- Alícuotas de retención y percepción por contacto y período. Exclusiones con porcentaje, vigencia y archivo de certificado, utilizables para clientes y proveedores según el circuito.
- Consulta de constancia de inscripción desde el contacto mediante el servicio de padrón de ARCA.
- Módulo `l10n_ar_padron_ws_consumer` para consultar un servidor de padrones y actualizar retenciones, percepciones, coeficientes e información de IVA. No es el mismo servicio que la constancia de inscripción de ARCA.
- Campos por compañía y reglas para aplicar la información fiscal en entornos con varias empresas.

## 04 — Diferencias por versión

El núcleo y el consumidor de padrones aparecen en 15, 17 y 19. La estructura de impuestos y algunos campos cambian entre ramas; no copiar una configuración de una versión a otra sin revisar el módulo instalado.

## 05 — Condiciones y límites del mensaje

La tarea `ir_cron_update_partners_from_padron` viene desactivada en los datos inspeccionados. Además, el `create` del contacto invoca `do_update_from_padron` en las tres ramas: desactivar el cron no elimina las consultas disparadas al crear contactos, sujetas a configuración. Requiere configurar servidor, diarios, jurisdicciones y programación. Los registros provinciales precargados no demuestran disponibilidad operativa de todos los padrones ni actualización inmediata. La vigencia de certificados y alícuotas debe formar parte de la configuración del cliente.

## 06 — Demostración sugerida

Cargar un contacto de prueba, consultar su constancia, revisar alícuotas del período y adjuntar una exclusión con vencimiento. Generar una factura y una orden de pago para mostrar qué dato se utiliza en cada cálculo.

## 07 — Temas del Excel vinculados

- `Comprobantes-1` · Carga de tipo de documento en clientes
- `Comprobantes-2` · Carga de número de IIBB en clientes
- `Comprobantes-3` · Carga de certificados de exclusión de retenciones en clientes
- `Comprobantes-4` · Carga de certificados de exclusión de percepciones en clientes
- `Comprobantes-5` · Carga de certificados de exclusión de retenciones en proveedores
- `Comprobantes-6` · Carga de certificados de exclusión de percepciones en proveedores
- `Comprobantes-24` · Cálculo automatizado de retenciones de IIBB a partir de padrones
- `Comprobantes-29` · Cálculo automátizado de percepciones en facturas de clientes a partir de padrones
- `Comprobantes-44` · Tipos de documento de AFIP precargados
- `Comprobantes-46` · Posiciones fiscales argentinas
- `Comprobantes-47` · Situaciones de Ingresos Brutos
- `Comprobantes-48` · Provincias y localidades argentinas precargadas
- `Comprobantes-50` · Alícuotas de retención y percepción por contacto
- `Comprobantes-51` · Consulta del padrón de AFIP desde el contacto
- `Comprobantes-52` · Actualización automática de padrones por jurisdicción

## 08 — Evidencia técnica para edición

La matriz y el catálogo conservan las referencias de cada tema. Estos archivos son puntos de entrada para revisar el alcance; no sustituyen una prueba funcional.

### Rama 15.0

- `l10n_ar_eynes/data/fiscal_position_data.xml:20`
- `l10n_ar_eynes/data/iibb_situation_data.xml:13`
- `l10n_ar_eynes/data/res_document_type_data.xml:17`
- `l10n_ar_eynes/models/res_country_state.py:15`
- `l10n_ar_eynes/models/res_partner.py:172`
- `l10n_ar_padron_ws_consumer/models/res_partner.py:538`

### Rama 17.0

- `l10n_ar_eynes/data/fiscal_position_data.xml:22`
- `l10n_ar_eynes/data/iibb_situation_data.xml:13`
- `l10n_ar_eynes/data/res_city_data.xml:17`
- `l10n_ar_eynes/data/res_document_type_data.xml:17`
- `l10n_ar_eynes/models/res_country_state.py:15`
- `l10n_ar_eynes/models/res_partner.py:171`
- `l10n_ar_padron_ws_consumer/models/res_partner.py:701`

### Rama 19.0

- `l10n_ar_eynes/data/fiscal_position_data.xml:22`
- `l10n_ar_eynes/data/iibb_situation_data.xml:13`
- `l10n_ar_eynes/data/res_city_data.xml:17`
- `l10n_ar_eynes/data/res_document_type_data.xml:17`
- `l10n_ar_eynes/models/res_country_state.py:15`
- `l10n_ar_eynes/models/res_partner.py:170`
- `l10n_ar_padron_ws_consumer/models/res_partner.py:443`

**Revisión adicional:** `l10n_ar_padron_ws_consumer/data/cron_data.xml` y `models/res_partner.py` en las tres ramas. En 19, `_get_padron_values` consulta el servidor configurado y `do_update_from_padron` coordina la actualización.

[Volver al índice](README.md) · [Matriz completa](matriz-excel.md) · [Diferencias y módulos](versiones-y-modulos.md)

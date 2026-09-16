---
title: "Importación y distribución de productos médicos"
seo_title: "Odoo para Importación y distribución de productos médicos | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Importación y distribución de productos médicos."
slug: "importacion-y-distribucion-de-productos-medicos"
estado: "publicado"
schema_type: "Service"
agrupador: "SALUD, CIENCIA Y CUIDADO ANIMAL"
portfolio: true
casos_relacionados: ["emeclar"]
modulos_relevantes: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
integraciones_destacadas: ["Facturación electrónica y comercio exterior", "Trazabilidad de productos médicos ante ANMAT, con registro por lote y número de serie a lo largo de toda la cadena hasta la institución que lo utiliza", "Multimoneda y cotizaciones: actualización de tipos de cambio y valuación de saldos, con la diferencia de cambio separada del margen operativo de cada operación", "Operadores logísticos y agentes comerciales: portal o conexión que permita que el movimiento y el consumo de producto en la red impacten en el sistema sin carga manual"]
faqs: [{"pregunta": "Tenemos un sistema contable que funciona. ¿Por qué sumar un ERP?", "respuesta": "La pregunta útil no es si el sistema contable funciona, sino cuánto de la operación quedó afuera de él. Cuando el seguimiento de importaciones, el stock distribuido y la asistencia técnica viven en planillas, el sistema pasó a ser el lugar donde se registra lo que ya ocurrió en vez del lugar donde la empresa opera. El objetivo no es reemplazar la contabilidad: es que la operación y la contabilidad sean el mismo dato."}, {"pregunta": "¿Odoo calcula el costo real de una importación?", "respuesta": "Sí, mediante costeo en destino: flete, seguro, derechos, despacho y almacenaje se distribuyen sobre los productos de la operación según el criterio que corresponda, y el costo unitario resultante alimenta la valuación de stock y el cálculo de margen. Los gastos que llegan después del ingreso de la mercadería se incorporan cuando se conocen y ajustan el costo de los productos involucrados."}, {"pregunta": "Tenemos producto en consignación en clínicas y con operadores logísticos. ¿Se puede controlar?", "respuesta": "Sí, modelando esas ubicaciones como depósitos de terceros dentro del sistema. El producto sigue siendo propiedad de la empresa y mantiene su lote, su número de serie y su vencimiento, así que se puede saber qué hay en cada institución, qué está por vencer y qué se consumió pendiente de facturar."}, {"pregunta": "¿Puedo trazar un producto médico por número de serie hasta la institución que lo utilizó?", "respuesta": "Sí. La trazabilidad por lote y número de serie acompaña al producto desde la importación hasta la entrega final, lo que permite responder en minutos ante un requerimiento regulatorio o una acción de campo sobre una partida determinada."}, {"pregunta": "Estamos certificados bajo ISO 9001. ¿Complica la implementación?", "respuesta": "Al contrario: tener los procedimientos definidos y auditados es una ventaja, porque el relevamiento parte de procesos que ya están escritos. Lo que cambia es dónde viven los registros. Al pasar los puntos de control al sistema, la evidencia para la auditoría se genera sola en lugar de reconstruirse, que suele ser el trabajo más pesado de cada recertificación."}]
---

## 01 — Hero

**Subtítulo:** Salud, ciencia y cuidado animal

## 02 — Problemas específicos del rubro

### Un sistema contable que deja la operación en planillas

En una importadora y distribuidora de productos médicos, el sistema contable suele cubrir solo la mitad visible del negocio: factura, registra, cierra el mes. Todo lo demás —seguimiento de importaciones, stock repartido en la red, asistencia técnica, documentación regulatoria— termina en planillas, y esas planillas terminan siendo el verdadero sistema de la empresa. Si además hay un sistema de gestión de calidad certificado, el problema pesa más: los procedimientos están definidos y auditados, pero dependen de que cada persona complete su planilla a tiempo. Mantener la certificación termina consumiendo un esfuerzo que el sistema debería absorber solo.

### Stock distribuido en una red que no reporta en tiempo real

La cobertura nacional de productos médicos casi nunca se arma con depósitos propios en cada provincia. Se arma con agentes comerciales y operadores logísticos, con buena parte del producto en consignación en clínicas, sanatorios y centros de salud. Ese stock tiene dueño y tiene vencimiento, pero no está donde la empresa lo puede ver. Sin control por ubicación, lote y número de serie, el resultado es previsible: producto que vence en poder de un tercero, consumo que se factura tarde (o directamente no se factura) y reposición que se decide con datos de la semana pasada.

### Costo de nacionalización y rentabilidad por línea representada

El precio de factura del proveedor del exterior es apenas una parte del costo real. Flete, seguro, derechos, tasas, despacho y almacenaje se conocen en momentos distintos y en una moneda que no es la de venta. Si esos costos no se reparten sobre los productos de cada operación, el costo unitario queda subestimado y el precio se termina fijando sobre un número que no refleja lo que costó. En un modelo de representación exclusiva esto pega más fuerte: cada marca tiene sus propios compromisos de compra y objetivos, y sin saber la rentabilidad real por línea es imposible negociar con la representada o entender qué producto del portfolio sostiene a los demás.

## 03 — Módulos relevantes

Compras con costeo en destino (desarrollo propio) · Inventario con lotes, números de serie, vencimientos y ubicaciones de terceros para el stock en consignación · Ventas y CRM para la red de agentes comerciales · Servicio de Campo para la asistencia técnica e instalación · Calidad para sostener los procedimientos del sistema de gestión certificado · Contabilidad con Localización Argentina, multimoneda y comercio exterior · Contabilidad Analítica para rentabilidad por línea representada · Documentos para registros ANMAT, certificados y documentación técnica.

## 03a — Integraciones

Facturación electrónica y comercio exterior. ARCA (ex AFIP) para comprobantes locales, junto con el circuito de importación y su impacto en el costo del producto.

Trazabilidad de productos médicos ante ANMAT, con registro por lote y número de serie a lo largo de toda la cadena hasta la institución que lo utiliza.

Multimoneda y cotizaciones: actualización de tipos de cambio y valuación de saldos, con la diferencia de cambio separada del margen operativo de cada operación.

Operadores logísticos y agentes comerciales: portal o conexión que permita que el movimiento y el consumo de producto en la red impacten en el sistema sin carga manual.

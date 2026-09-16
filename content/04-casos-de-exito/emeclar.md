---
title: "Emeclar: Odoo para Importación y distribución de productos médicos"
seo_title: "Emeclar | Casos de Odoo | Eynes"
meta_description: "Nula centralización de la información, trabajaban sobre un sistema administrativo contable, pero las operaciones se gestionaban en planillas de cálculo"
slug: "emeclar"
estado: "publicado"
schema_type: "Article"
cliente: "Emeclar"
rubro: "Importación y distribución de productos médicos"
pais: ""
usuarios: ""
modulos_implementados: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
resultado_clave: ""
agrupador: "SALUD, CIENCIA Y CUIDADO ANIMAL"
portfolio: true
faqs: [{"pregunta": "Tenemos un sistema contable que funciona. ¿Por qué sumar un ERP?", "respuesta": "La pregunta útil no es si el sistema contable funciona, sino cuánto de la operación quedó afuera de él. Cuando el seguimiento de importaciones, el stock distribuido y la asistencia técnica viven en planillas, el sistema pasó a ser el lugar donde se registra lo que ya ocurrió en vez del lugar donde la empresa opera. El objetivo no es reemplazar la contabilidad: es que la operación y la contabilidad sean el mismo dato."}, {"pregunta": "¿Odoo calcula el costo real de una importación?", "respuesta": "Sí, mediante costeo en destino: flete, seguro, derechos, despacho y almacenaje se distribuyen sobre los productos de la operación según el criterio que corresponda, y el costo unitario resultante alimenta la valuación de stock y el cálculo de margen. Los gastos que llegan después del ingreso de la mercadería se incorporan cuando se conocen y ajustan el costo de los productos involucrados."}, {"pregunta": "Tenemos producto en consignación en clínicas y con operadores logísticos. ¿Se puede controlar?", "respuesta": "Sí, modelando esas ubicaciones como depósitos de terceros dentro del sistema. El producto sigue siendo propiedad de la empresa y mantiene su lote, su número de serie y su vencimiento, así que se puede saber qué hay en cada institución, qué está por vencer y qué se consumió pendiente de facturar."}, {"pregunta": "¿Puedo trazar un producto médico por número de serie hasta la institución que lo utilizó?", "respuesta": "Sí. La trazabilidad por lote y número de serie acompaña al producto desde la importación hasta la entrega final, lo que permite responder en minutos ante un requerimiento regulatorio o una acción de campo sobre una partida determinada."}, {"pregunta": "Estamos certificados bajo ISO 9001. ¿Complica la implementación?", "respuesta": "Al contrario: tener los procedimientos definidos y auditados es una ventaja, porque el relevamiento parte de procesos que ya están escritos. Lo que cambia es dónde viven los registros. Al pasar los puntos de control al sistema, la evidencia para la auditoría se genera sola en lugar de reconstruirse, que suele ser el trabajo más pesado de cada recertificación."}]
---

## 03 — El problema

Nula centralización de la información, trabajaban sobre un sistema administrativo contable, pero las operaciones se gestionaban en planillas de cálculo

## 04 — La implementación

Emeclar no tenía la información centralizada en ningún lado. La empresa operaba sobre un sistema administrativo-contable que resolvía la facturación y la registración, pero toda la operación real —seguimiento de importaciones, stock repartido en la red de agentes y operadores logísticos, asistencia técnica, documentación del sistema de gestión de calidad— se llevaba en planillas de cálculo. Eso dejaba el costo real de cada nacionalización sin calcular, el stock distribuido sin control por lote ni vencimiento, y un sistema de calidad certificado bajo ISO 9001 sostenido a pulso con registros manuales.

## 05 — Testimonio

EL DESAFÍO
"Teníamos un sistema contable que hacía bien lo suyo: facturaba, registraba, cerraba el mes. El problema era todo lo demás. La operación real de la empresa pasaba afuera, en planillas. El seguimiento de cada importación, el stock que teníamos repartido en el país, los consumos que nos reportaban los agentes y los operadores logísticos, la asistencia técnica. Cada área tenía su planilla y cada una era la versión correcta según a quién le preguntaras.

Lo que más nos pesaba eran dos cosas. Una era el costo: traemos producto importado, y entre flete, seguro, derechos y despacho el costo real recién se termina de conocer bastante después de que la mercadería entró. Si eso no se distribuye sobre los productos, uno fija precio sobre un número que no es. La otra era el stock que no está en nuestro depósito. Buena parte de nuestro producto está en poder de terceros, y tiene vencimiento y número de serie. Controlarlo desde una planilla es imposible.

Y hay algo que quizás desde afuera no se ve: nosotros estamos certificados bajo ISO 9001 desde 2006. Los procedimientos estaban definidos y auditados, pero sostenerlos con planillas significaba que cada recertificación era un esfuerzo enorme para juntar la evidencia."

## 06 — Módulos relevantes para el rubro

Compras con costeo en destino (desarrollo propio) · Inventario con lotes, números de serie, vencimientos y ubicaciones de terceros para el stock en consignación · Ventas y CRM para la red de agentes comerciales · Servicio de Campo para la asistencia técnica e instalación · Calidad para sostener los procedimientos del sistema de gestión certificado · Contabilidad + Localización Argentina con multimoneda y comercio exterior · Contabilidad Analítica para rentabilidad por línea representada · Documentos para registros ANMAT, certificados y documentación técnica.

## 07 — Integraciones del rubro

Facturación electrónica y comercio exterior. ARCA (ex AFIP) para comprobantes locales, junto con el circuito de importación y su impacto en el costo del producto.

Trazabilidad de productos médicos ante ANMAT, con registro por lote y número de serie a lo largo de toda la cadena hasta la institución que lo utiliza.

Multimoneda y cotizaciones: actualización de tipos de cambio y valuación de saldos, con la diferencia de cambio separada del margen operativo de cada operación.

Operadores logísticos y agentes comerciales: portal o conexión que permita que el movimiento y el consumo de producto en la red impacten en el sistema sin carga manual.

## 08 — Otros casos del rubro

JENCK S.A. (ver su ficha en este mismo portfolio). Mismo agrupador de salud y ciencia, con foco en integrar la venta por licitaciones con el servicio técnico de campo, trazabilidad de consumibles con cadena de frío y costeo de instrumental importado multimoneda.

## 09 — Problemas específicos del rubro

### Un sistema contable que deja la operación en planillas

Una importadora y distribuidora de productos médicos tiene un sistema contable que resuelve la mitad visible del negocio: factura, registra y cierra el mes. La otra mitad —seguimiento de importaciones, stock distribuido, gestión de la red comercial, asistencia técnica, documentación regulatoria— queda afuera y se resuelve en planillas. Esa capa paralela deja de ser un atajo y se vuelve el sistema real de la empresa. El agravante aparece cuando existe un sistema de gestión de calidad certificado: los procedimientos están definidos y auditados, pero se sostienen con planillas que dependen de que cada persona las complete a tiempo, con lo cual mantener la certificación consume esfuerzo que debería resolver el sistema.

### Stock distribuido en una red que no reporta en tiempo real

La cobertura nacional en productos médicos no se hace con depósitos propios en cada provincia: se hace con agentes comerciales y operadores logísticos, y buena parte del producto está en consignación en clínicas, sanatorios y centros de salud. Ese stock existe, tiene dueño y tiene vencimiento, pero no está físicamente donde la empresa lo puede ver. Sin un sistema que lo controle por ubicación, lote y número de serie, aparecen tres problemas juntos: producto que se vence en poder de un tercero, consumo que se factura tarde o no se factura, y una reposición que se decide sobre información de la semana pasada.

### Costo de nacionalización y rentabilidad por línea representada

En una importadora, el precio de factura del proveedor del exterior es una fracción del costo real: flete, seguro, derechos, tasas, gastos de despacho y almacenaje se conocen en momentos distintos y en una moneda que no es la de venta. Si esos costos no se distribuyen sobre los productos de cada operación, el costo unitario queda subestimado y el precio se fija sobre un número equivocado. En un modelo de representación exclusiva el problema escala: cada marca tiene sus compromisos de compra y sus objetivos, y sin rentabilidad real por línea no hay forma de negociar con la representada ni de saber cuál del portfolio sostiene a la otra.

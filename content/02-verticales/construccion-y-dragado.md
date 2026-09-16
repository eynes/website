---
title: "Construcción y dragado"
seo_title: "Odoo para Construcción y dragado | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Construcción y dragado."
slug: "construccion-y-dragado"
estado: "publicado"
schema_type: "Service"
agrupador: "CONSTRUCCIÓN E INFRAESTRUCTURA"
portfolio: true
casos_relacionados: ["hydra-argentina-pentamar-s-a"]
modulos_relevantes: ["compras", "contabilidad-y-finanzas"]
integraciones_destacadas: ["ARCA / ARBA / AGIP", "Equipos y telemetría", "Portales de licitación"]
faqs: [{"pregunta": "¿Puedo ver el margen de cada obra en tiempo real?", "respuesta": "Sí, y es el motivo principal por el que una constructora migra a Odoo. Con contabilidad analítica, cada compra, hora de personal, hora de equipo y certificación se imputa a la obra en el momento en que se registra. El presupuesto cargado al inicio se contrasta contra el real acumulado, y el desvío se ve mientras la obra está en ejecución."}, {"pregunta": "¿Cómo se maneja la facturación por avance y las certificaciones?", "respuesta": "El contrato se estructura por hitos o por porcentaje de avance, y la facturación se genera contra la certificación aprobada. El sistema mantiene la relación entre lo certificado, lo facturado y lo cobrado, que es donde suelen aparecer las diferencias cuando se lleva por planilla."}, {"pregunta": "¿Contempla anticipos, fondos de reparo y redeterminación de precios?", "respuesta": "Anticipos y fondos de reparo se modelan dentro del circuito de facturación y cobranza. La redeterminación de precios, según cómo esté planteada en el contrato, puede requerir configuración específica."}, {"pregunta": "¿Puedo controlar costos y mantenimiento de equipos pesados?", "respuesta": "Sí. Cada equipo se gestiona como activo con su plan de mantenimiento preventivo, su historial de intervenciones y sus horas imputadas por obra, lo que permite conocer el costo real por hora de máquina y no una estimación."}, {"pregunta": "Trabajamos con muchos subcontratistas. ¿Cómo se controla?", "respuesta": "Cada subcontratista se gestiona con su contrato, su avance certificado y su circuito de retenciones, todo imputado a la obra correspondiente. Evita el escenario clásico de certificaciones aprobadas verbalmente en obra que aparecen después como factura sin respaldo."}]
---

## 01 — Hero

**Subtítulo:** Construcción e infraestructura

## 02 — Problemas específicos del rubro

### Presupuesto contra gasto real conocido recién al cierre

En construcción y dragado el margen no se pierde de golpe al final de la obra, se va perdiendo de a poco sin que nadie lo note. El presupuesto se arma en una planilla, la obra avanza durante meses, y el gasto real recién se conoce cuando contabilidad cierra el período — para ese momento el desvío ya pasó y no queda nada por corregir. Si nada imputa cada compra, cada hora de equipo y cada certificado de subcontratista a la obra en el momento en que ocurre, controlar costos deja de ser gestión y pasa a ser arqueología.

### Certificaciones y facturación por avance fuera del sistema

Acá no se factura una entrega puntual, se factura avance certificado: metros cúbicos dragados, porcentaje de obra ejecutado, hitos del contrato. Sumale anticipos, fondos de reparo, redeterminaciones de precios y, si es obra pública, los requisitos formales de siempre. Cuando todo eso se maneja por fuera del sistema, aparecen dos problemas al mismo tiempo: certificados que se emitieron pero nunca se facturaron, y una previsión de cobranza que nadie puede armar con confianza.

### Equipos pesados y subcontratistas sin control de costo

Dragas, embarcaciones y maquinaria son el activo más grande y el gasto más grande. Hay que saber cuánto cuesta cada equipo por hora, cuánto consume, cuándo toca mantenimiento y en qué obra está trabajando — incluidos los traslados entre obras, que casi nunca se facturan pero siempre hay que pagar. El subcontratista tiene su propio ciclo de costo: contrato, avance, certificación, retenciones, garantías. Sin sistema, todo eso termina viviendo en mails sueltos y en la planilla del jefe de obra.

## 03 — Módulos relevantes

Proyecto · Contabilidad Analítica · Mantenimiento · Hojas de Horas · Contabilidad. La contabilidad analítica por obra es el eje del diseño: cada compra, gasto, hora de personal, hora de equipo y certificación se imputa al proyecto que la origina, lo que permite contrastar presupuesto contra real mientras la obra está en ejecución.

## 03a — Integraciones

ARCA / ARBA / AGIP. Facturación electrónica y regímenes provinciales, incluido el régimen de retenciones a subcontratistas y proveedores, que en construcción es intensivo.

Equipos y telemetría. Equipos y telemetría: registro de horas de máquina, consumos de combustible y disponibilidad de equipos, para alimentar el costo real por obra.

Portales de licitación. Portales de licitación: presentación y seguimiento de documentación ante organismos públicos y grandes contratantes, certificaciones y avances.

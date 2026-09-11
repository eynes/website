---
title: "Sector Naval / Marítimo"
seo_title: "Odoo para Sector Naval / Marítimo | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Sector Naval / Marítimo."
slug: "sector-naval-maritimo"
estado: "publicado"
schema_type: "Service"
agrupador: "ENERGÍA Y SECTORES PESADOS"
portfolio: true
casos_relacionados: ["crux-marine-sas"]
faqs: [{"pregunta": "No tenemos ningún sistema hoy. ¿Es más difícil implementar desde cero?", "respuesta": "Suele ser lo contrario. Sin un sistema previo no hay que desarmar configuraciones heredadas ni migrar años de datos con inconsistencias: se diseña el circuito como corresponde desde el inicio. El trabajo se concentra en relevar bien cómo opera la empresa y en la carga de información maestra."}, {"pregunta": "¿Puedo conocer la rentabilidad de cada servicio o cada proyecto?", "respuesta": "Sí. Con el proyecto como unidad analítica, los repuestos consumidos, las horas técnicas y los servicios de terceros se imputan al trabajo correspondiente, y se contrastan contra lo facturado. Permite responder qué tipo de servicio y qué cliente dejan margen real."}, {"pregunta": "Facturamos en dólares y compramos en el exterior. ¿Odoo lo maneja?", "respuesta": "Sí, opera en multimoneda con actualización de cotizaciones y valuación de saldos. La diferencia de cambio queda registrada como tal y separada del resultado operativo, que es la única forma de saber si un servicio fue rentable o si el número lo explica el tipo de cambio."}, {"pregunta": "¿Cómo controlo repuestos críticos e importados con plazos largos?", "respuesta": "Con stock mínimo y punto de pedido por artículo, historial de consumo y trazabilidad por número de serie. El costeo de importación incorpora fletes, seguros e impuestos al valor del repuesto, para que el costo del servicio refleje el costo real y no solo el precio de factura."}, {"pregunta": "¿Cuánto tarda una implementación en una empresa sin sistema previo?", "respuesta": "Aproximadamente entre 3 y 4 meses."}]
---

## 01 — Hero

**Subtítulo:** Energía y sectores pesados

## 02 — Problemas específicos del rubro

### Servicios con alcance variable y ventana operativa acotada

El trabajo naval tiene una restricción que no tienen otros rubros: la ventana. El buque está en puerto o en dique un tiempo determinado y todo debe ejecutarse dentro de ese plazo. Además, el alcance real se conoce recién al abrir: lo presupuestado y lo que efectivamente hay que hacer casi nunca coinciden. Sin un sistema que gestione órdenes de trabajo, adicionales aprobados y horas reales del equipo técnico, el trabajo extra se ejecuta primero y se discute después, cuando el buque ya zarpó y la posición de negociación se perdió.

### Repuestos críticos importados con plazos de reposición largos

Buena parte de los componentes son importados, de bajo movimiento y alto valor, con plazos de reposición largos. Convive lo que no puede faltar bajo ninguna circunstancia con lo que no conviene tener inmovilizado. Sin sistema, no hay historial confiable de consumo ni criterio de reposición: se compra por urgencia, a costo alto y con flete premium, o se descubre la falta de un componente cuando el buque ya está en dique. A eso se suma el costeo de importación, donde el precio de factura es solo una parte del costo real.

### Operación multimoneda sin costeo por proyecto

Es un sector donde se cotiza y se cobra frecuentemente en dólares, se compra en el exterior y se pagan costos en pesos, en un contexto de tipos de cambio y ajustes que distorsionan cualquier análisis de rentabilidad hecho a mano. Combinado con la ausencia de costeo por proyecto, el resultado es una empresa que factura bien pero no sabe qué servicios le dejan margen, qué clientes le rinden y cuánto de la utilidad aparente es diferencia de cambio.

## 03 — Módulos relevantes

Proyecto · Contabilidad Analítica · Hojas de Horas · Mantenimiento · Inventario · Compras · Contabilidad. Al ser una implementación desde cero se pudo diseñar el circuito completo sin arrastrar configuraciones heredadas, incorporando desde el inicio el costeo por proyecto para conocer el resultado real de cada servicio.

## 03a — Integraciones

Multimoneda y cotizaciones. Multimoneda y cotizaciones: actualización de tipos de cambio y valuación de saldos, con la diferencia de cambio separada del margen operativo.

ARCA / ARBA / AGIP. Facturación electrónica y regímenes provinciales, incluida la facturación de exportación de servicios.

Portales de licitación. Portales de licitación y clientes institucionales.

Bancos. Bancos: conciliación, pagos al exterior y seguimiento de cobranzas en moneda extranjera.

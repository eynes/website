---
title: "Refrigeración Industrial"
seo_title: "Odoo para Refrigeración Industrial | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Refrigeración Industrial."
slug: "refrigeracion-industrial"
estado: "publicado"
schema_type: "Service"
agrupador: "SERVICIOS E INSUMOS INDUSTRIALES"
portfolio: true
casos_relacionados: ["tecnitower-s-a"]
modulos_relevantes: ["inventario", "compras", "ventas-y-crm", "contabilidad-y-finanzas"]
integraciones_destacadas: ["ARCA / AFIP", "Compras del exterior y costeo en destino", "Bancos y cuenta corriente"]
faqs: [{"pregunta": "¿La producción descuenta el stock automáticamente?", "respuesta": "Sí. Cada orden de producción consume los materiales de su lista contra el inventario en el momento en que se ejecuta, y el sistema registra la diferencia entre consumo teórico y real."}, {"pregunta": "Fabricamos equipos a medida. ¿Se puede costear cada uno?", "respuesta": "Sí, tratando el equipo o el pedido como unidad analítica: materiales, horas de taller y servicios de terceros se imputan ahí y se comparan contra lo presupuestado."}, {"pregunta": "¿Puedo saber qué equipo tiene instalado cada cliente?", "respuesta": "Sí, con número de serie asociado al cliente y a la venta, más el historial de instalación, puesta en marcha y mantenimientos posteriores."}, {"pregunta": "¿Contempla el servicio post-venta y el mantenimiento?", "respuesta": "Sí, con planes de mantenimiento sobre el equipo instalado y órdenes de servicio en campo que registran repuestos y horas, quedando vinculadas al mismo activo."}]
---

## 01 — Hero

**Subtítulo:** Servicios e insumos industriales

## 02 — Problemas específicos del rubro

### Producción que no descuenta el stock que consume

Fabricar equipos de refrigeración combina componentes de compra, partes de fabricación propia y trabajos de terceros. Cuando la producción no descuenta materiales del stock en el momento en que los consume, el inventario deja de reflejar la realidad: se compra lo que ya está, falta lo que figuraba disponible y el arranque de una orden se frena por un componente que el sistema decía tener.

### Costeo de equipos fabricados a medida

Buena parte de la producción no es de catálogo sino contra pedido, con especificaciones del cliente. Sin imputar materiales, horas de taller y servicios de terceros al equipo concreto, el costo se estima por analogía con trabajos anteriores. El presupuesto se arma sobre esa estimación y el margen real recién se conoce, si se conoce, mucho después de entregado.

### Post-venta sin historial del equipo instalado

El ciclo no termina en la entrega: hay instalación, puesta en marcha, garantía y mantenimiento posterior. Cuando la gestión administrativa está separada de la operación técnica, se pierde el rastro de qué equipo se entregó a qué cliente y con qué configuración, y el servicio post-venta arranca cada intervención sin historial.

## 03 — Módulos relevantes

Fabricación/MRP (órdenes de producción, listas de materiales, consumo real, equipos a medida) · Inventario (componentes y producto terminado, números de serie, stock mínimo) · Compras (proveedores locales e importados, plazos, costeo en destino) · Ventas (presupuestos técnicos configurables, anticipos, condiciones por proyecto) · Proyecto + Analítica (costo y margen real por equipo o obra, incluyendo horas de taller) · Servicio de Campo/Mantenimiento (instalación, puesta en marcha, garantía y mantenimiento de equipos instalados) · Contabilidad + Localización Argentina.

## 03a — Integraciones

Facturación electrónica. ARCA (ex AFIP) con emisión desde el pedido o el proyecto, contemplando anticipos y entregas parciales.

Compras del exterior y costeo en destino. Componentes importados con flete, seguro e impuestos incorporados al costo, base indispensable para presupuestar equipos a medida.

Servicio técnico en campo. Registro de la intervención en planta del cliente, con consumo de repuestos, horas y firma de conformidad, asociado al equipo por número de serie.

Bancos y cuenta corriente. Conciliación bancaria y seguimiento de anticipos y saldos de clientes industriales con plazos largos.

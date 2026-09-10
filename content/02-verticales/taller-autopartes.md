---
title: "Taller / Autopartes"
seo_title: "Odoo para Taller / Autopartes | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Taller / Autopartes."
slug: "taller-autopartes"
estado: "publicado"
schema_type: "Service"
agrupador: "AUTOMOTRIZ Y VEHÍCULOS"
portfolio: true
casos_relacionados: ["diesel-frenos"]
faqs: [{"pregunta": "¿Puedo actualizar precios sin tocar producto por producto cuando se mueve el dólar?", "respuesta": "Sí. El precio se construye desde el precio de reposición del importado y dos tablas de coeficientes agrupables por proveedor. Se cambia el valor en la tabla o el tipo de cambio y el recálculo baja a todos los productos afectados, con los presupuestos vencidos etiquetados automáticamente para que nadie venda a un precio viejo."}, {"pregunta": "¿Cómo controlo lo que ya pedí contra el compromiso anual con el proveedor?", "respuesta": "Con acuerdos de compra: se carga el compromiso una vez y cada orden de compra lo va consumiendo. El informe muestra por producto lo comprometido, lo pedido y lo pendiente, y deja de ser necesaria la orden ficticia a dos años."}, {"pregunta": "¿Soporta ser agente de percepción en varias provincias?", "respuesta": "Sí. La localización argentina calcula percepciones y retenciones según el padrón y la jurisdicción del cliente, genera los archivos de Libro IVA Digital, SICORE, SIFERE, ARBA, ARCIBA y SIRCAR, y permite cargar el padrón del mes dentro del plazo legal."}, {"pregunta": "¿Puedo saber el costo real de un importado y de qué despacho salió cada pieza?", "respuesta": "Sí. Los gastos de la operación completa —flete y seguro incluidos, no sólo los locales— se prorratean sobre el costo del stock, y cada movimiento queda trazado por número de despacho y partida, dato que después se refleja en la factura."}, {"pregunta": "Vengo de una implementación fallida, ¿cómo sé que esta vez sale?", "respuesta": "Con método visible: kickoff con alcance y responsables, reuniones semanales con acta y grabación, entregables por app, pruebas en un entorno de testing con validación del cliente antes de pasar a productivo, y acompañamiento diario en la semana de arranque."}]
---

## 01 — Hero

**Subtítulo:** Automotriz y vehículos

## 02 — Problemas específicos del rubro

### Precios atados al dólar actualizados producto por producto

El precio de venta nace del precio de reposición del importado (FOB en USD o EUR) y pasa por dos coeficientes, uno para llegar al costo y otro al precio de venta. En el sistema anterior, cada cambio de un proveedor obligaba a tocar los productos uno por uno, y un presupuesto aprobado semanas más tarde quedaba por debajo del costo real por el salto del tipo de cambio. Sumado a una política interna que exige que los vendedores no vean costos.

### Importaciones sin visibilidad del compromiso ni del despacho

El compromiso anual con el proveedor se modelaba como una orden de compra ficticia a dos años: nadie sabía cuánto de ese cupo estaba ya pedido y cuánto quedaba pendiente. Las recepciones de contenedor llegan con más de 100 líneas —y hubo casos de más de 150— que se cargaban y ubicaban a mano, sin trazabilidad por partida de despacho ni prorrateo de los gastos de nacionalización sobre el costo del stock.

### Carga fiscal multijurisdicción gestionada en planillas

La cuenta corriente y la composición de saldos se seguían con dos reportes del sistema viejo; el límite de crédito y las facturas vencidas se controlaban a ojo; los cheques de terceros en cartera vivían en planilla, sin fecha de emisión ni de recepción porque el sistema anterior no las pedía. En paralelo, la empresa es agente de percepción y retención en seis jurisdicciones con padrones distintos, donde un padrón nuevo hay que aplicarlo en tres días hábiles para no arriesgar sanciones. Y a nivel logístico, un remito no podía salir de varios depósitos a la vez.

## 03 — Módulos relevantes

Compras con acuerdos marco o blanket orders · Ventas con límite de crédito y validación de descuentos · Inventario con ubicaciones y cuarentena · Importaciones (despachos y landed costs) · Contabilidad + Localización Argentina · Comisiones por facturación y cobranza · Fabricación/MRP para kits · Multicompañía. El eje del diseño son las tablas de coeficientes de precios y el circuito de importación: son los dos lugares donde antes se perdía la rentabilidad.

## 03a — Integraciones

COT de ARBA desde el remito. COT de ARBA emitido directamente desde el remito.

WMS por API REST y JSON-RPC. Conexión con el sistema de depósito (WMS) vía API REST y JSON-RPC.

Consultora logística coordinando ERP + WMS. Consultora logística externa coordinando la operación conjunta de ERP y WMS.

Impresión directa a impresoras de red. Impresión directa a impresoras de red para documentación de depósito y expedición.

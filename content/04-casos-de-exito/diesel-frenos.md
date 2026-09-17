---
title: "Diesel frenos: Odoo para Taller / Autopartes"
seo_title: "Diesel frenos | Casos de Odoo | Eynes"
meta_description: "Gestión de la información descentralizada, problemas con el partner anterior que quiso implementar Odoo, problemas continuos de stock"
slug: "diesel-frenos"
estado: "publicado"
schema_type: "Article"
cliente: "Diesel frenos"
rubro: "Taller / Autopartes"
pais: ""
usuarios: 20
modulos_implementados: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
resultado_clave: "Un cambio de tipo de cambio o de proveedor recalcula automáticamente todos los productos afectados y etiqueta los presupuestos vencidos. Las importaciones son trazables por despacho aduanero con costo real, y las percepciones de las seis provincias, la cartera de cheques y el COT de ARBA dejaron de gestionarse a pulmón."
agrupador: "AUTOMOTRIZ Y VEHÍCULOS"
portfolio: true
faqs: [{"pregunta": "¿Puedo actualizar precios sin tocar producto por producto cuando se mueve el dólar?", "respuesta": "Sí. El precio se construye desde el precio de reposición del importado y dos tablas de coeficientes agrupables por proveedor. Se cambia el valor en la tabla o el tipo de cambio y el recálculo baja a todos los productos afectados, con los presupuestos vencidos etiquetados automáticamente para que nadie venda a un precio viejo."}, {"pregunta": "¿Cómo controlo lo que ya pedí contra el compromiso anual con el proveedor?", "respuesta": "Con acuerdos de compra: se carga el compromiso una vez y cada orden de compra lo va consumiendo. El informe muestra por producto lo comprometido, lo pedido y lo pendiente, y deja de ser necesaria la orden ficticia a dos años."}, {"pregunta": "¿Soporta ser agente de percepción en varias provincias?", "respuesta": "Sí. La localización argentina calcula percepciones y retenciones según el padrón y la jurisdicción del cliente, genera los archivos de Libro IVA Digital, SICORE, SIFERE, ARBA, ARCIBA y SIRCAR, y permite cargar el padrón del mes dentro del plazo legal."}, {"pregunta": "¿Puedo saber el costo real de un importado y de qué despacho salió cada pieza?", "respuesta": "Sí. Los gastos de la operación completa —flete y seguro incluidos, no sólo los locales— se prorratean sobre el costo del stock, y cada movimiento queda trazado por número de despacho y partida, dato que después se refleja en la factura."}, {"pregunta": "Vengo de una implementación fallida, ¿cómo sé que esta vez sale?", "respuesta": "Con método visible: kickoff con alcance y responsables, reuniones semanales con acta y grabación, entregables por app, pruebas en un entorno de testing con validación del cliente antes de pasar a productivo, y acompañamiento diario en la semana de arranque."}]
---

## 03 — El problema

Gestión de la información descentralizada, problemas con el partner anterior que quiso implementar Odoo, problemas continuos de stock

## 04 — La implementación

Diesel Frenos llegaba con información descentralizada y problemas de stock que arrastraba de una implementación de Odoo frustrada con otro partner. Los precios dependían del valor de reposición de los productos importados y había que actualizarlos uno por uno cada vez que se movía el tipo de cambio o cambiaba un proveedor, así que no era raro facturar un presupuesto por debajo del costo real. En comercio exterior los compromisos anuales se controlaban con órdenes ficticias, y los contenedores de más de 150 líneas se cargaban a mano, sin trazar partidas de despacho ni prorratear los gastos de nacionalización. Encima, la empresa es agente de percepción y retención en seis jurisdicciones, con cheques de terceros y límites de crédito llevados en planillas.

La implementación fue integral: Compras con acuerdos marco, Ventas con validación estricta de crédito, Inventario con ubicaciones y cuarentena, precios estructurados por tablas de coeficientes, conexión al WMS vía API REST, un módulo de Importaciones con landed costs y la localización argentina de Eynes. Hoy, cambiar el tipo de cambio o la condición de un proveedor recalcula automáticamente todos los productos afectados y etiqueta los presupuestos vencidos; cada importación se traza por número de despacho con su costo real, fletes y seguros incluidos; y las percepciones de las seis provincias se calculan con padrones al día, con el COT de ARBA saliendo directo del remito.

## 05 — Testimonio

EL DESAFÍO
"Veníamos de una experiencia de implementación muy frustrante con otro partner, lo que nos dejó operando con procesos sumamente manuales y descentralizados. Nuestra política de precios era insostenible: dependíamos del valor de reposición de artículos importados, y cada variación en el tipo de cambio o en el proveedor nos obligaba a actualizar los productos uno por uno. Muchas veces, al facturar un presupuesto aprobado semanas atrás, quedábamos por debajo del costo real. En el área de comercio exterior, carecíamos de visibilidad; controlábamos los compromisos anuales de importación mediante órdenes ficticias y la recepción de contenedores de más de 150 líneas se ingresaba manualmente, sin trazar las partidas de despacho ni prorratear los gastos de nacionalización. Sumado a esto, administrar la carga fiscal de ser agentes de percepción y retención en seis jurisdicciones, llevando los cheques de terceros y los límites de crédito en planillas sueltas, generaba un riesgo constante de sanciones y errores."

LA SOLUCIÓN
"Necesitábamos un cambio con una metodología de trabajo segura, predecible y con acompañamiento real. Implementamos una solución integral que incluyó Compras con acuerdos marco (blanket orders), Ventas con validación estricta de crédito, e Inventario con ubicaciones y cuarentena. Estructuramos la fijación de precios mediante tablas de coeficientes y conectamos el ERP con nuestro sistema de depósito (WMS) vía API REST. A nivel financiero, activamos el módulo de Importaciones para los despachos y 'landed costs', junto con la localización Argentina de Eynes para automatizar nuestra complejidad impositiva."

EL RESULTADO
"Recuperamos la confiabilidad en nuestra tecnología operativa. Hoy, al modificar el tipo de cambio o la condición de un proveedor, el recálculo se aplica automáticamente a todos los productos afectados, etiquetando los presupuestos vencidos para proteger la rentabilidad y manteniendo los costos ocultos para la fuerza de ventas. La gestión de importaciones es completamente transparente: conocemos el estado exacto de nuestros compromisos anuales, trazamos cada pieza por su número de despacho aduanero y sabemos su costo real exacto, incluyendo fletes y seguros. Administrativamente, dejamos de trabajar a pulmón; el sistema gestiona las percepciones de las seis provincias actualizando los padrones a tiempo, controlando la cartera de cheques y emitiendo el COT de ARBA de manera directa desde el remito."

## 06 — Módulos relevantes para el rubro

Compras con acuerdos marco o blanket orders · Ventas con límite de crédito y validación de descuentos · Inventario con ubicaciones y cuarentena · Importaciones (despachos y landed costs) · Contabilidad + Localización Argentina · Comisiones por facturación y cobranza · Fabricación/MRP para kits · Multicompañía. El eje del diseño son las tablas de coeficientes de precios y el circuito de importación: son los dos lugares donde antes se perdía la rentabilidad.

## 07 — Integraciones del rubro

COT de ARBA desde el remito. COT de ARBA emitido directamente desde el remito.

WMS por API REST y JSON-RPC. Conexión con el sistema de depósito (WMS) vía API REST y JSON-RPC.

Consultora logística coordinando ERP + WMS. Consultora logística externa coordinando la operación conjunta de ERP y WMS.

Impresión directa a impresoras de red. Impresión directa a impresoras de red para documentación de depósito y expedición.

## 08 — Otros casos del rubro

SUPPLY PARTS (ver su ficha en este mismo portfolio). Mismo rubro de repuestos y autopartes, con foco en el circuito de cobranza y crédito del canal distribuidor y en la sincronía de stock con el WMS y los marketplaces.

## 09 — Problemas específicos del rubro

### Precios atados al dólar actualizados producto por producto

El precio de venta nace del precio de reposición del importado (FOB en USD o EUR) y pasa por dos coeficientes, uno para llegar al costo y otro al precio de venta. En el sistema anterior, cada cambio de un proveedor obligaba a tocar los productos uno por uno, y un presupuesto aprobado semanas más tarde quedaba por debajo del costo real por el salto del tipo de cambio. Sumado a una política interna que exige que los vendedores no vean costos.

### Importaciones sin visibilidad del compromiso ni del despacho

El compromiso anual con el proveedor se modelaba como una orden de compra ficticia a dos años: nadie sabía cuánto de ese cupo estaba ya pedido y cuánto quedaba pendiente. Las recepciones de contenedor llegan con más de 100 líneas —y hubo casos de más de 150— que se cargaban y ubicaban a mano, sin trazabilidad por partida de despacho ni prorrateo de los gastos de nacionalización sobre el costo del stock.

### Carga fiscal multijurisdicción gestionada en planillas

La cuenta corriente y la composición de saldos se seguían con dos reportes del sistema viejo; el límite de crédito y las facturas vencidas se controlaban a ojo; los cheques de terceros en cartera vivían en planilla, sin fecha de emisión ni de recepción porque el sistema anterior no las pedía. En paralelo, la empresa es agente de percepción y retención en seis jurisdicciones con padrones distintos, donde un padrón nuevo hay que aplicarlo en tres días hábiles para no arriesgar sanciones. Y a nivel logístico, un remito no podía salir de varios depósitos a la vez.

---
title: "Comercio Internacional"
seo_title: "Odoo para Comercio Internacional | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Comercio Internacional."
slug: "comercio-internacional"
estado: "publicado"
schema_type: "Service"
agrupador: "SERVICIOS EMPRESARIALES"
portfolio: true
casos_relacionados: ["cidefama-s-a"]
modulos_relevantes: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
integraciones_destacadas: ["Facturación electrónica y comercio exterior", "Multimoneda y cotizaciones", "Despachantes y seguimiento de embarques", "Bancos y pagos al exterior"]
faqs: [{"pregunta": "¿Odoo calcula el costo real de importación?", "respuesta": "Sí, mediante costeo en destino a partir de un desarrollo propio de Eynes: los gastos de la operación (aduana, flete, seguro, derechos, despacho, almacenaje) se distribuyen sobre los productos según el criterio seleccionado por el usuario, y el costo unitario resultante es el que alimenta la valuación de stock y el cálculo de margen."}, {"pregunta": "¿Qué pasa si los gastos llegan después de que la mercadería ingresó?", "respuesta": "Se incorporan a la operación cuando se conocen y ajustan el costo de los productos involucrados, que es exactamente el escenario que las planillas no resuelven bien."}, {"pregunta": "¿Puedo ver el estado de todas mis operaciones de importación a la vez?", "respuesta": "Sí, tratando cada operación como unidad de seguimiento con sus estados, plazos, documentación y costos, lo que permite detectar la demora mientras todavía se puede actuar."}, {"pregunta": "Ya tuvimos una implementación de Odoo que no funcionó. ¿Por qué confiar de nuevo?", "respuesta": "Porque el problema casi nunca es Odoo: es el relevamiento, la configuración hecha sin entender el negocio y la falta de acompañamiento posterior.."}, {"pregunta": "Operamos en varias monedas. ¿Cómo se refleja el resultado?", "respuesta": "Con multimoneda y valuación de saldos, manteniendo la diferencia de cambio identificada por separado, para no confundir resultado financiero con margen comercial."}]
---

## 01 — Hero

**Subtítulo:** Servicios empresariales

## 02 — Problemas específicos del rubro

### Costo real de importación desconocido al fijar precio

Lo que factura el proveedor es apenas una parte del costo real. Flete internacional, seguro, derechos, tasas, despacho, almacenaje y honorarios van llegando en momentos distintos, a veces mucho después de que la mercadería ya entró. Si esos gastos no se reparten sobre los productos de la operación, el costo unitario queda subestimado, el precio de venta se calcula sobre un número que no es el correcto y el margen que se ve en pantalla no es el que hay en realidad.

### Planillas sueltas funcionando como sistema de gestión

Cada importación termina con su propia planilla: una para seguir el embarque, otra para los costos, otra para la relación con el despachante. Funcionan mientras la persona que las armó siga ahí. No se consolidan entre sí, no dejan un historial comparable, y cada vez que dirección pregunta un número alguien tiene que volver a armarlo a mano.

### Operaciones de comercio exterior sin visibilidad de estado

Proveedor, embarque, arribo, despacho, liberación, entrega: cada etapa de una operación de comercio exterior trae su propia documentación y sus propios plazos. Sin un lugar único donde ver el estado de todas las operaciones juntas, las demoras se notan tarde — y se terminan pagando en almacenaje, en clientes esperando y en costos financieros que nadie tenía presupuestados.

## 03 — Módulos relevantes

Compras + Costeo en destino/Landed Cost (distribución de flete, seguro, derechos y gastos sobre el costo de cada producto) · Inventario (mercadería en tránsito, arribos, depósitos, trazabilidad por operación) · Proyecto + Analítica (cada operación de importación como unidad: costos, tiempos y rentabilidad) · Ventas (cotizaciones sobre costo real, listas de precios y márgenes) · Contabilidad + Localización Argentina (facturación electrónica, multimoneda, comercio exterior) · Documentos (documentación de embarque, despacho y certificaciones por operación) · CRM (seguimiento de clientes y proveedores del exterior).

## 03a — Integraciones

Facturación electrónica y comercio exterior. ARCA (ex AFIP) para comprobantes locales, junto al circuito de importación y su impacto contable.

Multimoneda y cotizaciones. Actualización de tipos de cambio y valuación de saldos, con la diferencia de cambio separada del margen de la operación.

Despachantes y seguimiento de embarques. Estado de cada operación y su documentación asociada, para tener la visibilidad completa en un solo lugar en vez de en la casilla de mail.

Bancos y pagos al exterior. Conciliación bancaria, giros y seguimiento de compromisos en moneda extranjera.

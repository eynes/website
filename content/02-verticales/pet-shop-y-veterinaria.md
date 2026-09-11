---
title: "Pet Shop y Veterinaria"
seo_title: "Odoo para Pet Shop y Veterinaria | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Pet Shop y Veterinaria."
slug: "pet-shop-y-veterinaria"
estado: "publicado"
schema_type: "Service"
agrupador: "COMERCIO MAYORISTA Y MINORISTA"
portfolio: true
casos_relacionados: ["comercializadora-casper-s-a-casper-pet-store"]
modulos_relevantes: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
integraciones_destacadas: ["Facturación electrónica", "Medios de pago", "Logística y couriers", "Marketplaces y canales"]
faqs: [{"pregunta": "¿El stock de la tienda online es realmente el mismo que el del local?", "respuesta": "Sí: no hay sincronización entre sistemas porque no hay dos sistemas. El ecommerce, el POS de cada sucursal y el depósito leen y escriben sobre el mismo sistema de inventario, y una venta en mostrador impacta en la web en el momento."}, {"pregunta": "¿Puedo agendar servicios y cobrarlos en la misma operación?", "respuesta": "Sí. El turno queda asociado al cliente y a su mascota, y al momento de cobrar se suma al ticket junto con los productos, con la venta de servicio y la de mercadería en el mismo comprobante."}, {"pregunta": "¿Cómo se cotiza el envío de una bolsa de 15 kilos?", "respuesta": "Con reglas por peso y volumen en lugar de por monto de compra, integradas con el courier o con las zonas del reparto propio, de manera que el costo cotizado se parezca al costo real."}, {"pregunta": "¿Puedo trazar vencimientos de alimento y medicamentos?", "respuesta": "Sí, por lote y fecha de vencimiento, con salida FEFO y alertas de próximo vencimiento por depósito."}, {"pregunta": "¿Sirve si tengo varias sucursales con precios distintos?", "respuesta": "Sí, con listas de precios y promociones por sucursal o por canal, sobre un catálogo único."}]
---

## 01 — Hero

**Subtítulo:** Comercio mayorista y minorista

## 02 — Problemas específicos del rubro

### Stock desincronizado entre la tienda online y los locales

El comercio de mascotas vende el mismo producto en varias sucursales y en la tienda web, con reposición desde un depósito central. Cuando cada canal lee un stock distinto, aparecen las dos caras del mismo error: se vende online algo que ya no está y se pierde la venta, o se sobre-stockea para cubrirse y queda capital inmovilizado en alimento con vencimiento. El problema no es la falta de datos, es que están en sistemas que no se hablan.

### Agenda de servicios desconectada del punto de venta

Peluquería, baño, consulta veterinaria y aplicación de vacunas se agendan por un lado y se cobran por otro. El turno vive en una agenda que el punto de venta no conoce, así que el ticket se arma a mano, el servicio no queda asociado a la mascota ni al cliente, y no hay forma de saber qué rinde más por metro cuadrado ni de recordarle al cliente la próxima dosis.

### Envíos de productos pesados y voluminosos mal cotizados

Una bolsa de alimento de 15 kilos o un transportador grande rompen la lógica del ecommerce estándar: el costo de envío real depende del peso y del volumen, no del precio del producto. Sin cálculo por peso volumétrico y sin coordinación de reparto propio por zona, el envío se cotiza mal y el margen se lo come el flete.

## 03 — Módulos relevantes

Inventario (stock multi-depósito y multi-sucursal, lotes y vencimientos de alimento y medicamentos, reposición automática) · Punto de Venta (mostrador de cada sucursal integrado en tiempo real con stock y contabilidad) · eCommerce/Sitio Web (tienda online sobre el mismo catálogo y stock que el local) · Citas/Planificación (agenda de peluquería, baño y consultas conectada al POS) · Ventas y CRM (ficha del cliente y de su mascota, historial, campañas de recompra) · Compras (punto de pedido, acuerdos con laboratorios y distribuidores) · Inventario-Envíos (reglas por peso y volumen, zonas de reparto, logística propia).

## 03a — Integraciones

Facturación electrónica. ARCA (ex AFIP) para comprobantes de mostrador y de tienda online, con emisión desde el POS sin doble carga.

Medios de pago. Pasarelas y QR para el canal online y cobro con tarjeta y billeteras en el mostrador, con conciliación automática de liquidaciones.

Logística y couriers. Cotización de envío según peso y volumen, generación de etiquetas y seguimiento, más hojas de ruta para el reparto propio de bultos grandes.

Marketplaces y canales. Publicación y sincronía de stock y precios con marketplaces, para que el mismo inventario alimente todos los canales.

---
title: "Manolo: Odoo para Gastronomía"
seo_title: "Manolo | Casos de Odoo | Eynes"
meta_description: "Ausencia de sistema de producción y control de stock, fallas en el cálculo de retenciones automáticas a proveedores"
slug: "manolo"
estado: "publicado"
schema_type: "Article"
cliente: "Manolo"
rubro: "Gastronomía"
pais: ""
usuarios: ""
modulos_implementados: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
resultado_clave: "Logramos orden de punta a punta. Hoy la cocina central lanza órdenes de producción precisas, el stock de insumos se descuenta automáticamente con cada lote terminado de masa o rellenos, las sucursales se reabastecen desde el almacén central, y pagamos a los proveedores emitiendo el certificado de retención sin intervención manual."
agrupador: "ALIMENTOS Y GASTRONOMÍA"
portfolio: true
faqs: [{"pregunta": "¿El sistema permite gestionar una cocina central y abastecer a varias sucursales?", "respuesta": "Sí, el módulo de fabricación te permite planificar la producción en tu cocina central basada en la demanda o los pedidos internos de tus sucursales, gestionando los envíos mediante documentos de transferencia internos."}, {"pregunta": "¿Calcula automáticamente las retenciones de ARCA e IIBB al pagar a proveedores de mercadería?", "respuesta": "El sistema se integra con los padrones de las diferentes entidades de control (ARCA, ARBA, AGIP, etc.). Al momento de emitir una orden de pago, calcula y contabiliza automáticamente las retenciones de Ganancias, IVA o Ingresos Brutos correspondientes al proveedor."}, {"pregunta": "¿Cómo controlo las mermas y el consumo de materia prima a granel (harina, aceite)?", "respuesta": "Mediante las recetas. Cuando la cocina finaliza una orden de producción (ej. 100 kg de masa), el sistema descuenta instantáneamente las cantidades teóricas de materia prima del almacén. Luego, podrás registrar las mermas reales para mantener el inventario siempre exacto."}, {"pregunta": "¿El sistema cuenta con herramientas para la atención en el salón y el envío de comandas a la cocina?", "respuesta": "Sí, el módulo de Restaurante (Punto de Venta) incluye un plano de mesas interactivo y totalmente personalizable. Los empleados pueden tomar el pedido directamente desde una tablet o dispositivo móvil junto a la mesa del cliente y enviarlo al instante a las impresoras o pantallas de la cocina (Kitchen Display System). Esto agiliza la atención, permite dividir cuentas fácilmente y evita errores en la preparación de los platos."}, {"pregunta": "¿Puedo configurar promociones automáticas como \"Happy Hour\" o programas de fidelidad para mis clientes?", "respuesta": "Absolutamente. El sistema te permite configurar programas de promociones muy avanzados. Podrás establecer listas de precios condicionales o reglas de \"Happy Hour\" (ej. 2x1 en pintas) que se activen solas en días y horarios específicos dentro del Punto de Venta. Además, podrás crear programas de puntos, tarjetas de regalo y cupones de descuento para fidelizar a tus clientes recurrentes sin depender de cálculos manuales en la caja."}]
---

## 03 — El problema

Ausencia de sistema de producción y control de stock, fallas en el cálculo de retenciones automáticas a proveedores

## 04 — La implementación

MANOLO. Situación inicial: ausencia de sistema de producción y control de stock, y fallas en el cálculo de retenciones automáticas a proveedores. La cocina central producía a ciegas, sin MRP, lo que generaba a la vez faltantes en los locales y exceso de desperdicio; el inventario de materias primas pesadas (harina, aceite, carnes) tenía inconsistencias graves porque la producción no descargaba los insumos utilizados; y los pagos a proveedores estaban expuestos a errores impositivos costosos porque el sistema no calculaba las retenciones de IIBB y Ganancias. Qué se hizo: implementación de Fabricación e Inventario completamente integrados con Contabilidad, automatización del cálculo de retenciones y estandarización de recetas y órdenes de producción. Resultado: la cocina central lanza órdenes de producción precisas, el stock de insumos se descuenta automáticamente con cada lote terminado, las sucursales se reabastecen desde el almacén central y los pagos a proveedores emiten el certificado de retención sin intervención manual.

## 05 — Testimonio

EL DESAFÍO
"Teníamos dos grandes focos de pérdida. Por un lado, la cocina central operaba sin sistema: no teníamos un sistema de producción que descontara la materia prima y el control de stock de insumos críticos era inexistente. Por el otro, el área de pagos a proveedores era un caos porque el sistema no nos calculaba las retenciones impositivas, lo que nos generaba estar expuestos a multas y reclamos."

LA SOLUCIÓN
"Implementamos los módulos de fabricación e inventario completamente integrados con la contabilidad. Automatizamos el cálculo de retenciones de ganancias para evitar trabajo manual, y estandarizamos las recetas y órdenes de producción."

EL RESULTADO
"Logramos orden de punta a punta. Hoy la cocina central lanza órdenes de producción precisas, el stock de insumos se descuenta automáticamente con cada lote terminado de masa o rellenos, las sucursales se reabastecen desde el almacén central, y pagamos a los proveedores emitiendo el certificado de retención sin intervención manual."

## 06 — Módulos relevantes para el rubro

Fabricación (Producción) · Compras · Contabilidad · Inventario. El diseño integra la producción de la cocina central con el inventario y la contabilidad, de modo que cada lote terminado descuente su materia prima y cada orden de pago calcule y contabilice sus retenciones sin intervención manual. Se complementa con el módulo de Restaurante o Punto de Venta para salón, comandas y promociones.

## 07 — Integraciones del rubro

ARCA. Facturación electrónica y cálculo automático de retenciones de Ganancias, IVA e Ingresos Brutos contra los padrones de los organismos de control.

PedidosYa. PedidosYa: ingreso directo de pedidos al circuito de venta.

Rappi. Rappi: ingreso directo de pedidos al circuito de venta.

Balanzas industriales de producción.. Balanzas industriales de producción, para el registro de pesos reales en la cocina central.

## 08 — Otros casos del rubro

FRANCO PARMA

## 09 — Problemas específicos del rubro

### Cocina central produciendo sin planificación

Una cocina central sin sistema de planificación produce contra una demanda estimada a mano. El resultado es simultáneo y contradictorio: faltantes en algunos locales y desperdicio en la cocina, porque no hay forma de ajustar la producción a lo que las sucursales realmente van a necesitar.

### Materias primas a granel sin descarga automática de stock

Las materias primas a granel son las que más se prestan a la diferencia silenciosa: si la producción no descarga los insumos consumidos, el inventario teórico de harina, aceite o carne se despega del real un poco cada día, hasta que el recuento físico expone un desvío que ya no se puede atribuir a nada.

### Retenciones a proveedores calculadas manualmente

Cuando el sistema no calcula las retenciones al pagar, cada orden de pago es una oportunidad de error impositivo. En un rubro con muchos proveedores y pagos frecuentes, el riesgo no es puntual sino acumulativo: multas, reclamos y certificados que hay que rehacer.

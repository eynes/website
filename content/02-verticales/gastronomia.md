---
title: "Gastronomía"
seo_title: "Odoo para Gastronomía | Eynes"
meta_description: "Problemas, módulos, integraciones y experiencias de implementación de Odoo para Gastronomía."
slug: "gastronomia"
estado: "publicado"
schema_type: "Service"
agrupador: "ALIMENTOS Y GASTRONOMÍA"
portfolio: true
casos_relacionados: ["franco-parma", "manolo", "la-guitarrita-s-a"]
modulos_relevantes: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
integraciones_destacadas: ["Facturación electrónica ARCA", "Aplicaciones de delivery (PedidosYa, Rappi)", "Medios de pago y billeteras (Mercado Pago)", "Balanzas electrónicas (venta al peso y producción)", "Bancos y proveedores"]
faqs: [{"pregunta": "¿El sistema descuenta los ingredientes automáticamente al vender?", "respuesta": "Sí, mediante la carga de recetas de cada plato o producto. Al concretar una venta en el POS, el sistema descuenta automáticamente las porciones o gramos correspondientes de tu inventario."}, {"pregunta": "¿Puedo ver las ventas y auditar el stock de varias sucursales en tiempo real?", "respuesta": "Sí. Al ser un sistema en la nube y multi-sucursal, la administración central puede monitorear las cajas, las ventas por hora y los movimientos de mercadería entre depósitos desde una única pantalla, evitando diferencias."}, {"pregunta": "¿Se integra con aplicaciones de delivery para no cargar los pedidos a mano?", "respuesta": "Absolutamente. Los pedidos de plataformas externas (como PedidosYa o Rappi) ingresan directamente al sistema, centralizando la facturación y la comanda para la cocina sin tener que tipear el ticket nuevamente en el local."}, {"pregunta": "¿El sistema permite gestionar una cocina central y abastecer a varias sucursales?", "respuesta": "Sí, el módulo de fabricación te permite planificar la producción en tu cocina central basada en la demanda o los pedidos internos de tus sucursales, gestionando los envíos mediante documentos de transferencia internos."}, {"pregunta": "¿Calcula automáticamente las retenciones de ARCA e IIBB al pagar a proveedores de mercadería?", "respuesta": "El sistema se integra con los padrones de las diferentes entidades de control (ARCA, ARBA, AGIP, etc.). Al momento de emitir una orden de pago, calcula y contabiliza automáticamente las retenciones de Ganancias, IVA o Ingresos Brutos correspondientes al proveedor."}, {"pregunta": "¿Cómo controlo las mermas y el consumo de materia prima a granel (harina, aceite)?", "respuesta": "Mediante las recetas. Cuando la cocina finaliza una orden de producción (ej. 100 kg de masa), el sistema descuenta instantáneamente las cantidades teóricas de materia prima del almacén. Luego, podrás registrar las mermas reales para mantener el inventario siempre exacto."}, {"pregunta": "¿El sistema cuenta con herramientas para la atención en el salón y el envío de comandas a la cocina?", "respuesta": "Sí, el módulo de Restaurante (Punto de Venta) incluye un plano de mesas interactivo y totalmente personalizable. Los empleados pueden tomar el pedido directamente desde una tablet o dispositivo móvil junto a la mesa del cliente y enviarlo al instante a las impresoras o pantallas de la cocina (Kitchen Display System). Esto agiliza la atención, permite dividir cuentas fácilmente y evita errores en la preparación de los platos."}, {"pregunta": "¿Puedo configurar promociones automáticas como \"Happy Hour\" o programas de fidelidad para mis clientes?", "respuesta": "Absolutamente. El sistema te permite configurar programas de promociones muy avanzados. Podrás establecer listas de precios condicionales o reglas de \"Happy Hour\" (ej. 2x1 en pintas) que se activen solas en días y horarios específicos dentro del Punto de Venta. Además, podrás crear programas de puntos, tarjetas de regalo y cupones de descuento para fidelizar a tus clientes recurrentes sin depender de cálculos manuales en la caja."}, {"pregunta": "¿Cómo se controla la merma de insumos?", "respuesta": "Cargando las recetas de cada plato: al venderse, el sistema descuenta los insumos teóricos. La diferencia contra el inventario físico es la merma real, y por primera vez se puede atribuir a un producto, un turno o un local en lugar de aparecer como un número global."}, {"pregunta": "¿Sirve para varios locales con administración centralizada?", "respuesta": "Sí. Cada local opera su POS y su stock, y la casa central ve todo consolidado, con comparación de resultado, consumo y merma entre sucursales."}, {"pregunta": "¿Los pedidos de las apps de delivery entran al sistema?", "respuesta": "Sí, integrados al mismo circuito de venta, de modo que descuentan insumos y se registran contablemente igual que una venta de salón, sin carga manual paralela."}, {"pregunta": "Ya intentamos implementar Odoo y no funcionó. ¿Por qué sería distinto?", "respuesta": "Las implementaciones fallidas casi nunca fallan por el software: fallan por relevamiento insuficiente, por configurar sin entender el proceso real o por falta de acompañamiento después del arranque."}, {"pregunta": "¿Puedo llevar los controles de calidad en el sistema?", "respuesta": "Sí, con puntos de control en recepción y en proceso, registrados en el momento y con historial consultable, lo que convierte la auditoría en una consulta y no en una reconstrucción."}]
---

## 01 — Hero

**Subtítulo:** Alimentos y gastronomía

## 02 — Problemas específicos del rubro

### Sucursales que no se pueden auditar en tiempo real

Si cada local cierra su caja con su propio criterio, la casa central no tiene forma de auditar en tiempo real: los cierres que no cuadran se descubren tarde, y ya no hay cómo reconstruir qué pasó en ese turno. El control termina dependiendo de cuánto confiás en cada encargado, no del sistema.

### Ventas sin recetas cargadas: consumo real desconocido

Sin escandallos cargados no hay forma de saber cuánto insumo debería haberse gastado para las ventas del día. La merma no se mide, se la encuentra de casualidad en el inventario, y la rentabilidad por plato queda como una estimación que nunca se compara contra el consumo real.

### Mermas y transferencias entre locales sin trazabilidad

Las transferencias de mercadería entre locales son el punto ciego de siempre en el multi-sucursal: salen de un depósito y no siempre entran al otro con el mismo registro. Sumado a las mermas que tampoco se anotan, generan diferencias de inventario que nadie puede explicar ni atribuir a nada puntual.

### Cocina central produciendo sin planificación

Una cocina central sin planificación produce contra una demanda calculada a ojo. Y el resultado es contradictorio: faltan productos en algunos locales mientras sobra comida en la cocina, porque no hay manera de ajustar lo que se produce a lo que las sucursales realmente van a pedir.

### Materias primas a granel sin descarga automática de stock

Harina, aceite, carne — las materias primas a granel son las que más se prestan a la diferencia silenciosa. Si la producción no descuenta los insumos que consume, el inventario teórico se va despegando del real un poco cada día, hasta que el recuento físico expone un desvío que para entonces ya no tiene explicación.

### Retenciones a proveedores calculadas manualmente

Si el sistema no calcula solo las retenciones al pagar, cada orden de pago es una chance de error impositivo. Y en un rubro con muchos proveedores y pagos frecuentes, ese riesgo no es un hecho aislado: se acumula en multas, reclamos y certificados que hay que rehacer.

### Administración multi-local sin consolidación

Varios locales, turnos, personal que rota mucho, caja diaria, proveedores que entregan directo en cada sucursal. Cuando cada local resuelve su administración por su cuenta, la casa central recibe la información tarde y en formatos distintos — no puede comparar el resultado real entre sucursales, ni negociar con un proveedor con el consumo consolidado en la mano.

### Registros de calidad en papel poco fiables ante auditoría

Recepción de mercadería, control de temperatura, vencimientos, limpieza: todo eso suele anotarse en planillas de papel que se completan al final del turno, cuando ya nadie se acuerda bien. Frente a una auditoría esos registros no sirven de mucho, y tampoco permiten detectar a tiempo a un proveedor que entrega sistemáticamente fuera de especificación.

## 03 — Módulos relevantes

Punto de Venta (POS) · Inventario · Fabricación (Recetas) · Contabilidad. La combinación de recetas cargadas con POS integrado es la que resuelve el problema de fondo: la venta de un producto en una sucursal descuenta automáticamente los insumos del stock de ese local, y la contabilidad y los almacenes de todos los locales quedan unificados en un solo tablero.

Fabricación (Producción) · Compras · Contabilidad · Inventario. El diseño integra la producción de la cocina central con el inventario y la contabilidad, de modo que cada lote terminado descuente su materia prima y cada orden de pago calcule y contabilice sus retenciones sin intervención manual. Se complementa con el módulo de Restaurante o Punto de Venta para salón, comandas y promociones.

Punto de Venta/Restaurante (salón, mesas, mostrador y delivery, con cierre de caja integrado a contabilidad) · Inventario (insumos por local, lotes y vencimientos, transferencias entre sucursales) · Fabricación/MRP (recetas y preparaciones base, descuento automático de insumos por venta) · Compras (proveedores, precios acordados, recepción por sucursal, reposición automática) · Calidad (controles de recepción, temperatura y limpieza registrados en el sistema) · Contabilidad + Localización Argentina (facturación electrónica, resultado por local, consolidación central) · Empleados (turnos, presentismo y costo de personal por sucursal).

## 03a — Integraciones

Facturación electrónica ARCA. Emisión en el momento del cobro, tanto en salón como en delivery, y cálculo automático de retenciones de Ganancias, IVA e Ingresos Brutos contra los padrones de los organismos de control.

Aplicaciones de delivery (PedidosYa, Rappi). Los pedidos entran directo al sistema, sin que nadie tenga que volver a tipear el ticket en el local: se centraliza la facturación y la comanda que va a cocina.

Medios de pago y billeteras (Mercado Pago). Tarjetas, QR y billeteras con conciliación automática de las liquidaciones — en gastronomía es la mayoría del ticket, y la principal fuente de diferencias de caja cuando no está bien resuelto.

Balanzas electrónicas (venta al peso y producción). Las balanzas del mostrador, para fiambres y venta al peso, y las de la cocina central, para pesos reales de producción, cargan el dato directo al sistema.

Bancos y proveedores. Conciliación bancaria, pagos a proveedores y control de precios acordados contra lo que realmente terminó facturado.

---
title: "Supply Parts: Odoo para Repuestos y Autopartes"
seo_title: "Supply Parts | Casos de Odoo | Eynes"
meta_description: "Gestión de la información descentralizada, problemas continuos de stock"
slug: "supply-parts"
estado: "publicado"
schema_type: "Article"
cliente: "Supply Parts"
rubro: "Repuestos y Autopartes"
pais: ""
usuarios: ""
modulos_implementados: ["ventas-y-crm", "inventario"]
resultado_clave: "En Supply Parts el pago que un cliente reporta por el portal impacta su cuenta corriente y libera el cupo de crédito en el acto, sin que administración tenga que tocarlo — lo que antes frenaba ventas por puro trámite ahora escala en volumen sin sumar personal."
agrupador: "AUTOMOTRIZ Y VEHÍCULOS"
portfolio: true
faqs: [{"pregunta": "¿El sistema cumple con la facturación de ARCA para mayoristas de repuestos?", "respuesta": "Sí, la plataforma está 100% actualizada con las normativas de ARCA (ex AFIP). Automatiza la emisión de facturas y recibos, gestiona la validación de CAE y calcula automáticamente las percepciones y retenciones impositivas específicas que aplican al rubro."}, {"pregunta": "¿Puedo integrar mi cuenta de Mercado Libre?", "respuesta": "Totalmente. Contamos con integraciones nativas para el rubro automotor. Podés sincronizar tus precios y disponibilidad de stock en Mercado Libre en tiempo real, e integrar tu inventario. Una vez que Odoo recibe la información desde mercado libre, desencadena el proceso de facturación y generación del recibo de cobro de forma automática."}, {"pregunta": "¿Qué pasa si un cliente compra por el portal pero no hay stock real en el depósito?", "respuesta": "Ese problema desaparece. Al conectarse de forma directa con tu gestión de almacenes (WMS), el portal lee el stock físico en tiempo real. Tu cliente solo podrá agregar al carrito los repuestos que realmente están disponibles en los estantes en ese preciso segundo, eliminando las ventas en falso y los quiebres de stock."}, {"pregunta": "¿Cómo evito que las cuentas corrientes queden desactualizadas y me bloqueen ventas?", "respuesta": "A través de nuestro Portal de Clientes. En lugar de que tu equipo cargue los cobros a mano, tus distribuidores pueden ingresar con su usuario, ver su saldo y subir sus propios recibos o comprobantes de transferencia. El sistema actualiza la cuenta corriente y libera el límite de crédito al instante, evitando que las ventas se frenen por demoras administrativas."}, {"pregunta": "¿Puedo migrar mi base histórica de clientes, sus saldos y límites de crédito actuales?", "respuesta": "Sí, el proceso de implementación incluye la migración de tus datos. Importamos tu maestro de artículos, tu lista de clientes, los saldos pendientes de cada cuenta corriente y los límites de crédito que ya tenés asignados, para que el salto al nuevo sistema sea transparente y no pierdas tu historial comercial."}]
---

## 03 — El problema

Gestión de la información descentralizada, problemas continuos de stock

## 04 — La implementación

En Supply Parts los pedidos de los distribuidores se pasaban a mano al sistema, el stock publicado no reflejaba lo que realmente había en el depósito, y como la carga de recibos de cobro no era online, las cuentas corrientes se actualizaban con días de atraso — el sistema terminaba bloqueando a clientes que ya habían pagado. La implementación sumó Ventas, Stock, Límite de crédito y Portal de clientes, integrados con Mercado Libre, el WMS y ARCA.

## 05 — Testimonio

EL DESAFÍO
"Nuestro mayor cuello de botella en las ventas era la gestión de cobros y cuentas corrientes. La carga de los recibos de pago no se hacía online; dependíamos de que un administrativo procesara manualmente cada comprobante recibo por recibo. Esto generaba un desfasaje enorme: los clientes pagaban, pero sus cuentas corrientes demoraban días en actualizarse. Como consecuencia, el sistema los bloqueaba por 'límite de crédito excedido' y no podían seguir comprando, lo que provocaba enojos constantes, llamados a la oficina y ventas paralizadas injustamente."

LA SOLUCIÓN
"Decidimos automatizar el flujo de cobranzas e implementamos los módulos de Límite de Crédito y Portal de Clientes, integrando el sistema con la facturación de ARCA y nuestra gestión de ventas. Les dimos a los distribuidores acceso a su propio panel donde pueden autogestionarse, subir sus comprobantes de pago de forma online y ver el estado de su cuenta en tiempo real."

EL RESULTADO
"El cambio en la relación con los clientes fue inmediato. Ahora, en cuanto el cliente reporta su pago en el portal, el impacto se refleja en su cuenta corriente y el cupo de crédito se libera en el acto. Eliminamos la fricción de tener clientes queriendo comprar y no poder hacerlo por un trámite administrativo demorado. Además, libero a nuestro equipo de contabilidad de horas de carga manual, permitiéndonos escalar el volumen de clientes sin necesidad de sumar más personal administrativo."

## 06 — Módulos relevantes para el rubro

Ventas · Stock · Límite de crédito · Portal de clientes. El portal es la pieza central: el distribuidor arma su pedido contra stock real, sube sus comprobantes de pago y consulta el estado de su cuenta, lo que libera el cupo de crédito sin intervención administrativa. Ventas y Stock quedan conectados al WMS y a Mercado Libre para que la disponibilidad publicada sea la física.

## 07 — Integraciones del rubro

Mercado libre. Publicación y sincronía de precios y stock en tiempo real. Cuando Odoo recibe la venta desde Mercado Libre, dispara automáticamente la facturación y la generación del recibo de cobro.

WMS. Gestión avanzada de almacenes como fuente de verdad del stock físico: el portal lee la disponibilidad real en estantería, lo que elimina las ventas en falso.

Aleph. Circuito de datos conectado con la plataforma Aleph del rubro automotor.

ARCA. Facturación electrónica: emisión de facturas y recibos, validación de CAE y cálculo automático de percepciones y retenciones del rubro.

## 08 — Otros casos del rubro

MACRO ARGENTINA (ver su ficha en este mismo portfolio). Mismo rubro de repuestos y autopartes, con el foco puesto en profesionalizar las compras: reglas de reabastecimiento automático sobre historial real de ventas y tableros de rotación por SKU, en reemplazo de la compra basada en la intuición del personal más antiguo.

## 09 — Problemas específicos del rubro

### Pedidos del canal distribuidor cargados a mano

El distribuidor arma el pedido en su plataforma y alguien lo vuelve a tipear en el sistema de gestión: el pedido llega tarde, con errores de transcripción y sin validación de crédito ni de disponibilidad real. Cada importación manual es una oportunidad de equivocarse en un código de repuesto que, en autopartes, se parece muchísimo al de al lado.

### Disponibilidad publicada que no refleja el stock real

El distribuidor consulta disponibilidad sobre información desactualizada, así que compra lo que no está o no compra lo que sí está. En repuestos, donde el catálogo tiene miles de referencias y la rotación es despareja, ese desfasaje se traduce directo en venta perdida y en pedidos que hay que rearmar por teléfono.

### Cobranzas offline que frenan ventas por límite de crédito

El cliente paga, pero su cuenta corriente tarda días en reflejarlo porque un administrativo tiene que procesar recibo por recibo. Mientras eso pasa, el sistema lo bloquea por límite de crédito excedido y no puede seguir comprando. La venta se frena por un trámite administrativo, no por riesgo real.

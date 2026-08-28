---
# Fuente de todos los datos de este caso: Excel "portfolio de proyectos
# realizados.xlsx", hojas "Casos" y "Verticales" (fila Supply Parts).
# El testimonio y las FAQ están tomados casi textual del material que la
# empresa ya usa en su propio deck de portfolio — no son contenido inventado.

cliente: "Supply Parts"
logo: ""
rubro: "distribucion-y-mayoristas"
pais: "Argentina"
usuarios: 67
modulos_implementados:
  - "ventas-y-crm"
  - "inventario"
  # GUÍA: el cliente usa además "Límite de crédito" y "Portal de clientes",
  # que hoy no tienen módulo propio en 03-modulos/ — se describen en el
  # cuerpo de la página en vez de linkear a una página inexistente.
resultado_clave: "Liberación instantánea de cuentas corrientes y cupo de crédito al reportar un pago, sin carga manual — antes tardaba días. (Sin cifra porcentual dicha por el cliente; ver voz-y-tono.md regla 3.)"

title: "Cómo Supply Parts eliminó los bloqueos de crédito a sus distribuidores con el Portal de Clientes de Odoo"
seo_title: "Caso de Éxito Supply Parts — Odoo para Repuestos | Eynes"
meta_description: "Supply Parts automatizó cobranzas y cuentas corrientes con Odoo y Eynes: los distribuidores ya no se quedan bloqueados por demoras administrativas."
slug: "supply-parts"
url: "eynes.com.ar/casos/supply-parts"
schema_type: "Article"
estado: "publicado"
og_image: ""
---

## 01 — Hero del caso

Logo del cliente + "Cuentas corrientes y cupo de crédito liberados al instante, sin carga manual de cobros"

## 02 — Ficha rápida

| Rubro | País | Usuarios | Módulos implementados |
|---|---|---|---|
| Repuestos y autopartes (mayorista/minorista) | Argentina | 67 (Odoo Community, 95 empleados) | Ventas, Stock, Límite de crédito, Portal de clientes |

Se dedica a la comercialización mayorista y minorista de repuestos industriales y automotrices, abasteciendo a talleres, fábricas y flotas.

## 03 — El problema

> "Nuestro mayor cuello de botella en las ventas era la gestión de cobros y cuentas corrientes. La carga de los recibos de pago no se hacía online; dependíamos de que un administrativo procesara manualmente cada comprobante recibo por recibo. Esto generaba un desfasaje enorme: los clientes pagaban, pero sus cuentas corrientes demoraban días en actualizarse. Como consecuencia, el sistema los bloqueaba por 'límite de crédito excedido' y no podían seguir comprando, lo que provocaba enojos constantes, llamados a la oficina y ventas paralizadas injustamente."

A esto se sumaban dos problemas de base: los pedidos de los clientes distribuidores se importaban manualmente al sistema, y el stock de productos no estaba actualizado para mostrar disponibilidad real al distribuidor.

## 04 — La solución

> "Decidimos automatizar el flujo de cobranzas e implementamos los módulos de Límite de Crédito y Portal de Clientes, integrando el sistema con la facturación de ARCA y nuestra gestión de ventas. Les dimos a los distribuidores acceso a su propio panel donde pueden autogestionarse, subir sus comprobantes de pago de forma online y ver el estado de su cuenta en tiempo real."

Se integró además con Mercado Libre (sincronización de precios y stock) y con el WMS de gestión de almacenes, para que el portal muestre solo el stock físico realmente disponible. Módulos relacionados: [Ventas y CRM](../03-modulos/ventas-y-crm.md), [Inventario](../03-modulos/inventario.md).

## 05 — El resultado

> "El cambio en la relación con los clientes fue inmediato. Ahora, en cuanto el cliente reporta su pago en el portal, el impacto se refleja en su cuenta corriente y el cupo de crédito se libera en el acto. Eliminamos la fricción de tener clientes queriendo comprar y no poder hacerlo por un trámite administrativo demorado. Además, libero a nuestro equipo de contabilidad de horas de carga manual, permitiéndonos escalar el volumen de clientes sin necesidad de sumar más personal administrativo."
>
> — Supply Parts

## 06 — CTA

"Quiero un resultado similar en mi empresa" → Agendar demo (`/demo`)

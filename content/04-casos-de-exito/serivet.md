---
title: "Serivet: Odoo para Veterinaria"
seo_title: "Serivet | Casos de Odoo | Eynes"
meta_description: "Ausencia de sistema de gestión, solo utilizaban un sistema para facturación"
slug: "serivet"
estado: "publicado"
schema_type: "Article"
cliente: "Serivet"
rubro: "Veterinaria"
pais: ""
usuarios: ""
modulos_implementados: ["ventas-y-crm", "inventario", "compras", "contabilidad-y-finanzas"]
resultado_clave: "Ahora tenemos todo el historial en un solo lugar. Cuando atendemos a un paciente, veo sus vacunas previas, laboratorios, las prestaciones realizadas y los insumos usados, y eso impacta directo en caja. Además, el sistema nos avisa qué medicamentos están por vencer para darles prioridad, eliminando las pérdidas por caducidad."
agrupador: "SALUD, CIENCIA Y CUIDADO ANIMAL"
portfolio: true
faqs: [{"pregunta": "¿El sistema permite unificar la historia clínica del animal con la facturación?", "respuesta": "Sí. Podés crear fichas detalladas por animal asociadas a la cuenta de su dueño. Al registrar una consulta clínica, podés imputar directamente los servicios y medicamentos utilizados, generando la factura sin doble carga manual."}, {"pregunta": "¿Puedo controlar el vencimiento de vacunas y medicamentos veterinarios?", "respuesta": "Totalmente. El módulo de inventario exige la carga de número de lote y fecha de vencimiento al ingresar mercadería (cumpliendo normas de SENASA/ANMAT). El sistema utiliza el método FEFO (Primero en vencer, primero en salir) y te alerta sobre productos próximos a caducar."}, {"pregunta": "¿Se pueden automatizar los recordatorios para los clientes?", "respuesta": "Sí. Al tener la base de datos centralizada, podés configurar envíos automáticos de correos o mensajes (vía integración con WhatsApp) para recordarle a los tutores sobre fechas de vacunación, laboratorios, desparasitación o turnos programados, aumentando la recurrencia."}]
---

## 03 — El problema

Ausencia de sistema de gestión, solo utilizaban un sistema para facturación

## 04 — La implementación

SERIVET. Situación inicial: ausencia de sistema de gestión; se usaba un sistema básico solo para emitir comprobantes fiscales, mientras la gestión real vivía en planillas y cuadernos. Los trabajos a campo se registraban de forma incompleta y se subfacturaban, no había control sobre insumos médicos, vacunas y alimentos, lo que generaba pérdidas por vencimiento, y no existía una base de datos que permitiera enviar recordatorios de desparasitación o vacunación, con la consiguiente pérdida de oportunidades de fidelización. Qué se hizo: implementación de Odoo unificando la ficha del animal con la cuenta de su dueño y pasando a controlar todo el stock de farmacia y alimentos por número de lote y fecha de vencimiento. Resultado: todo el historial en un solo lugar, con vacunas previas, laboratorios, prestaciones realizadas e insumos usados visibles al atender e impactando directo en caja; y alertas de productos próximos a vencer que eliminaron las pérdidas por caducidad.

## 05 — Testimonio

EL DESAFÍO
"Teníamos una veterinaria con áreas que sabíamos podían mejorar. Usábamos un sistema básico solo para emitir comprobantes fiscales, pero la gestión real estaba en planillas o cuadernos. No podíamos vincular lo que compraba un cliente con la historia clínica del animal. Además, perdíamos plata porque se nos vencían vacunas en la heladera al no tener un control de lotes sistematizado."

LA SOLUCIÓN
"Cambiamos el sistema anterior e implementamos Odoo. Unificamos la ficha del animal en relación a la cuenta de su dueño, y pasamos a controlar todo el stock de farmacia y alimentos por número de lote y fecha de vencimiento."

EL RESULTADO
"Ahora tenemos todo el historial en un solo lugar. Cuando atendemos a un paciente, veo sus vacunas previas, laboratorios, las prestaciones realizadas y los insumos usados, y eso impacta directo en caja. Además, el sistema nos avisa qué medicamentos están por vencer para darles prioridad, eliminando las pérdidas por caducidad."

## 06 — Módulos relevantes para el rubro

Ventas · Inventario con lotes y caducidad · Compras · Gestión de laboratorio. La pieza que ordena todo es la ficha del animal asociada a la cuenta de su dueño: al registrar una consulta se imputan servicios, prácticas de laboratorio y medicamentos utilizados, y eso impacta directo en la facturación y en el descuento de stock.

## 07 — Integraciones del rubro

Trazabilidad SENASA/ANMAT (Medicamentos veterinarios). Trazabilidad SENASA y ANMAT para medicamentos veterinarios, con carga obligatoria de lote y vencimiento y salida por método FEFO.

WhatsApp / SMS (Recordatorios automáticos). WhatsApp y SMS para recordatorios automáticos de vacunación, desparasitación, laboratorios y turnos programados.

ARCA. Facturación electrónica.

## 09 — Problemas específicos del rubro

### Trabajos a campo sin registro y subfacturados

El trabajo a campo es el que más fácilmente queda sin registrar: se atiende, se aplica, se usa insumo y el comprobante se arma después, de memoria o desde un cuaderno. Lo que no se registra en el momento se subfactura, y la pérdida no se detecta porque nunca existió como dato.

### Insumos y vacunas sin control de lote y vencimiento

Vacunas, medicamentos y alimentos tienen vencimientos estrictos y valor unitario alto. Sin control por lote y fecha de caducidad, el producto se vence en la heladera y la pérdida se descubre al descartarlo, no cuando todavía había tiempo de darle prioridad de venta.

### Sin base de datos para sostener la recurrencia del cliente

Desparasitación, vacunación y controles son consumo recurrente y predecible. Sin una base de datos que vincule al animal con su dueño y su historial, no hay forma de recordarlo, y la recurrencia depende de que el cliente se acuerde solo.

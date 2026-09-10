# Pendientes y criterios para publicar

Estos puntos se detectaron comparando el Excel con las tres ramas. No impiden documentar el resto del producto. Identifican qué redacción ajustar o qué escenario demostrar antes de usar una afirmación pública.

## Contradicciones y alcances no demostrados

| Tema | Hallazgo | Tratamiento editorial | Qué resuelve la duda |
|---|---|---|---|
| WSLP | Está en `Webservice!A3`; no se localizó implementación ni registro en las ramas | Mantener en matriz como declarado por Excel, fuera de la lista de servicios demostrados | Identificar addon externo, método, configuración y ejemplo de operación |
| CAEA | Está en `Webservice!A4`; no se localizó implementación | No confundir CAEA con CAE ni con bloqueo offline del POS | Identificar autorización anticipada, información posterior y pruebas |
| WSFECRED | Existe `models/wsfecred.py` y llamada desde `account_move.py`; falta import en `models/__init__.py` en las tres ramas | Presentar circuito FCE con pendiente de consulta de obligatoriedad; no afirmar WSFECRED operativo | Verificar registro de `wsfecred.config`, configuración, consulta y alternativa ABC en Odoo |
| Facturas M | El Excel las incluye; `_check_denomination_not_m` las bloquea en diarios y facturas de las tres ramas | No ofrecer emisión M. Separar catálogo histórico de emisión permitida | Definir mensaje para históricos y A con leyenda; no derivar normativa actual del mensaje del código |
| Jurisdicciones PDF | `Reportes!A2` dice PDF; `sales_by_jurisdiction.py` genera XLSX | Corregir formato a XLSX en contenido público | Mostrar un PDF distinto si existe fuera del repo |
| ND/NC por diferencia de cambio | Se encontró multimoneda, asistentes de notas y ajustes de pago; no el flujo específico de la fila `Comprobantes!A32` | Conservar alcance declarado como pendiente | Identificar automatismo, módulo o procedimiento de usuario y demostrarlo |
| Remito sobre plantilla | Hay QWeb de Remito R; la planilla pide revisar descripción | Explicar diseño del comprobante; no prometer editor ni formulario preimpreso universal | Definir modalidad y mostrar salida real |
| Actualización de padrones | Servidor configurable y cron inicialmente desactivado | Explicar requisito de servicio y activación | Identificar jurisdicciones cubiertas efectivamente, frecuencia y manejo de indisponibilidad |
| Cambio masivo de cheques | Hay asistentes con múltiples cheques; el genérico exige uno | Nombrar las operaciones concretas | Probar depósito/débito/acreditación y transiciones permitidas en cada rama |
| Cierre sin RECPAM | Hay opciones de generación; en las tres ramas `action_confirm` exige `recpam_move_id` | No prometer cualquier transición de cierre sin ajuste | Ejecutar cierre con y sin RECPAM y registrar el flujo permitido |
| Impresión de cheques | Addons distintos en 17/19, con dependencia `sign_oca` y bibliotecas PDF | Explicar módulo adicional y plantilla configurada | Instalar dependencias y generar un ejemplo de impresión |
| eCheq bancario | Se acredita registro de formato y estados, no una API bancaria | Hablar de gestión/registro de eCheqs | Identificar conector bancario si se quiere prometer emisión o endoso remoto |
| DDJJ en 19 | `l10n_ar_taxes_report/__manifest__.py` tiene `installable: False` | No ofrecerlo como disponible en 19 | Completar validación técnica y cambiar el manifiesto en el proyecto correspondiente |
| Cobertura provincial | Catálogos, reglas, padrones y exportadores tienen alcances diferentes | Describir cada capa; evitar “todas las provincias automáticamente” | Matriz comercial de jurisdicciones, regímenes, servicio de padrón y formato de salida |

## Diferencias que deben conservarse

- PDF Libro Diario, IVA Compras/Ventas y asistente de IVA prorrateable: localizados en 17/19, no en 15 dentro de este repositorio.
- Motor específico de impuestos internos: localizado en 17/19; validar tratamiento de 15 antes de describirlo como idéntico.
- Cuenta corriente histórica, talonarios CAI y exportadores SIRCAR/SIPOT/SIRETPER/Misiones: localizados en 17; no extrapolar a 19 por ser una versión posterior.
- Complemento de conciliación de cheques: presente en 15/19, no en 17. El núcleo de cheques sí existe en 17.
- POS: modalidad inicial configurable y bloqueo por posición fiscal en 17/19; 15 tiene selección de modalidad y valor inicial fijado por código. Control específico de cuentas al cierre localizado en 19.

## Correcciones sugeridas para la página actual

La página existente en `../01-paginas-unicas/localizacion-argentina.md` y su plantilla Astro contienen afirmaciones más amplias que la evidencia reunida. No se reescribieron en esta tarea, cuyo entregable es la carpeta documental.

| Expresión o idea actual | Redacción respaldable |
|---|---|
| “La más completa del mercado” | “Facturación, impuestos y operación argentina integrados en Odoo” |
| “Todo nativo, sin parches de terceros” | “Localización desarrollada por Eynes, con módulos y dependencias definidos para cada versión” |
| “Moneda dual y ajuste por inflación nativos” | “Cotización por comprobante, campos de segunda moneda y proceso de cierre con RECPAM configurable” |
| “Mantenemos al día cada cambio normativo” | Separar capacidades verificadas del compromiso de mantenimiento, que requiere definición comercial |
| “Todas las jurisdicciones” | Explicar las reglas y jurisdicciones implementadas para el cliente; no equiparar precarga con servicio activo |

## Evidencia y validación

Los manifiestos muestran 5 módulos en 15, 8 en 17 y 7 en 19, pero la cantidad no mide cobertura ni calidad. `installable: True` tampoco acredita pruebas aprobadas ni soporte contratado. Los README de 15/17 todavía describen configuración V15 y los README de varios addons están vacíos; por eso se priorizó el código y el manifiesto de cada rama.

En 19, `l10n_ar_eynes/tests/__init__.py` importa `test_res_partner` y deja comentado `test_account_payment_order`. No se ejecutaron esas pruebas ni un entorno Odoo. No presentar este relevamiento como certificación funcional o fiscal.

Los nombres AFIP se conservan en identificadores técnicos y textos originales del Excel. En la explicación al visitante se usa ARCA cuando se habla del organismo, sin renombrar arbitrariamente los servicios o símbolos del código.

No publicar valores de alícuotas, mínimos, fechas de vigencia o instrucciones tributarias basándose solo en este repositorio. Si luego se necesita contenido normativo, verificarlo contra la documentación oficial aplicable al momento de publicación.

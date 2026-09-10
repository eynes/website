# Propuesta de incorporación al sitio

## La página principal

Mantener `/localizacion-argentina` como entrada del menú. Su objetivo es explicar el alcance, mostrar los circuitos y llevar a una demo. El texto propuesto está en [_hub.md](_hub.md).

El menú principal no necesita trece entradas nuevas. La página puede agrupar las capacidades en:

1. **Facturar y vender:** comprobantes, datos fiscales, POS y servicios de autorización.
2. **Cobrar y pagar:** medios combinados, retenciones, cheques y cuentas corrientes.
3. **Operar y cerrar:** remitos, reportes, exportadores, monedas y cierre contable.

## Páginas de detalle propuestas

Las rutas de esta tabla son propuestas; esta tarea no las implementa. Cada ficha incluye `url`, `estado: revision` y `publicar: false` para evitar confundir insumos con páginas ya disponibles.

| Ruta bajo `/localizacion-argentina/` | Foco | Relación principal |
|---|---|---|
| `facturacion-y-comprobantes` | Emisión y documentación | Ventas y CRM |
| `datos-fiscales-y-padrones` | Información que alimenta impuestos | Contactos, facturación y pagos |
| `cobros-y-pagos` | Cancelación de cuentas y documentos | Contabilidad y finanzas |
| `retenciones-y-percepciones` | Reglas, bases y certificados | Pagos y facturación |
| `multimoneda-y-diferencias` | Cotización y registro | Empresas con operaciones en otras monedas |
| `cheques-y-conciliacion` | Cartera y tesorería | Contabilidad y finanzas |
| `punto-de-venta` | Circuito de caja | Comercios y gastronomía |
| `remitos-y-transporte` | Documentación de entregas | Inventario y distribución |
| `reportes-contables` | Información para administración | Cierre y revisión contable |
| `exportadores-impositivos` | Archivos por régimen | Equipo administrativo y contable |
| `cierre-contable-e-inflacion` | Ejercicio y RECPAM | Contabilidad y finanzas |
| `servicios-arca-y-arba` | Autorización y trazabilidad | Facturación y retenciones |
| `cuentas-corrientes` | Movimientos por período y pendientes actuales | Clientes y proveedores; alcance localizado en 17 |

No crear una página individual por cada una de las 124 filas: hay duplicados, funciones auxiliares y temas que se entienden mejor dentro de un circuito. Las fichas documentales permiten separar contenido sin decidir todavía que todas ameriten una ruta pública independiente.

## Qué contenido va a la web

De cada ficha usar el texto para el visitante, capacidades comprobables, condiciones que afecten su decisión y FAQs. Los detalles de imports, rutas, manifiestos, estados de migración y conflictos se usan para edición y definición del alcance; no deben terminar en el texto comercial por un render automático de todo el Markdown.

La versión de Odoo puede aparecer como dato de consulta o en una tabla de disponibilidad validada. No usar los números de versión del manifiesto como insignias de soporte comercial. Una rama más nueva no contiene necesariamente todos los módulos de una anterior.

## Enlaces a preparar

- Desde Contabilidad y finanzas hacia cobros/pagos, cheques, reportes y cierre.
- Desde Ventas y CRM hacia facturación y datos fiscales.
- Desde Inventario hacia remitos.
- Desde rubros con caja hacia POS, usando la relación temática y sin atribuir módulos concretos a un cliente si el portfolio no lo dice.
- Desde casos de éxito hacia el circuito que efectivamente describe su ficha.
- Desde todas las páginas de localización hacia la demo y de regreso al índice de capacidades.

Los destinos de módulos y casos deben resolverse contra contenido publicado para evitar enlaces rotos. Para los detalles nuevos, construir enlaces solo cuando exista una ruta.

## Material para demostraciones

| Escenario | Qué mostrar | Requisito de producción del material |
|---|---|---|
| Facturación | Venta, factura, autorización, CAE, QR | Compañía de ensayo y homologación |
| Pago combinado | Dos facturas, transferencia, cheque, retenciones y certificados | Reglas y cuentas configuradas |
| Cartera de cheques | Recepción, vencimiento, depósito o entrega, rechazo | Elegir circuito según versión |
| IVA y exportadores | Comprobantes, subdiario, agrupación y archivos | Período con datos de prueba y formato identificado |
| Remitos | Entrega, bultos, transportista, R/X | Datos de prueba; CAI solo donde corresponda |
| Cierre | Controles, índices, asientos y trazabilidad | Ejercicio de ensayo y criterio contable definido |
| ARBA Digital | Retención, envío, estado y PDF | Servicio de ensayo o evidencia previamente autorizada |

## Implementación futura

Crear una colección específica para esta carpeta o un adaptador que lea solo las fichas habilitadas. Excluir `README`, matriz, versiones, arquitectura, pendientes y `_fuentes`. El esquema debe separar las secciones técnicas de las públicas; no basta con renderizar todo el cuerpo.

La documentación existente en `01-paginas-unicas/localizacion-argentina.md` puede reemplazarse por el hub o quedar como entrada que remita a esta nueva fuente. Mantener una sola fuente editorial para la página principal al hacer esa integración.

# Localización argentina de Eynes — base documental

Esta carpeta reúne el alcance funcional de la localización para convertirlo en contenido del sitio. Se construyó a partir de **los 124 temas de las seis hojas de `temas localización.xlsx`** y de la inspección estática de las referencias locales `origin/15.0`, `origin/17.0` y `origin/19.0` del repositorio `l10n_ar_eynes`, el 10 de septiembre de 2026.

El Excel define el alcance declarado. El código permite precisar qué se encontró en cada rama, qué requiere un módulo adicional y qué contradice o no alcanza a demostrar lo escrito en la planilla. Las diferencias se conservan; no se convierten en promesas de disponibilidad universal.

## Por dónde empezar

- [Página principal propuesta](_hub.md): relato y estructura para ampliar `/localizacion-argentina`.
- [Matriz del Excel](matriz-excel.md): las 124 entradas, sin eliminar duplicados, con ficha de destino y referencias por versión.
- [Versiones y módulos](versiones-y-modulos.md): composición del proyecto y diferencias entre 15, 17 y 19.
- [Pendientes y correcciones](pendientes-y-criterios-editoriales.md): contradicciones, restricciones y comprobaciones necesarias.
- [Arquitectura del contenido](arquitectura-web.md): propuesta de páginas, enlaces y demostraciones.

## Fichas funcionales

| Ficha | Qué permite explicar |
|---|---|
| [Datos fiscales y padrones](datos-fiscales-y-padrones.md) | Identificación, posiciones fiscales, IIBB, exclusiones y consulta de padrones |
| [Facturación y comprobantes](facturacion-y-comprobantes.md) | Puntos de venta, numeración, CAE, QR, notas y exportación |
| [Cobros y pagos](cobros-y-pagos.md) | Recibos, órdenes de pago, medios combinados, anticipos y certificados |
| [Retenciones y percepciones](retenciones-y-percepciones.md) | Reglas de cálculo, escalas, mínimos, acumulados e impuestos internos |
| [Multimoneda](multimoneda-y-diferencias.md) | Cotización por comprobante, segunda moneda y ajustes |
| [Cheques y conciliación](cheques-y-conciliacion.md) | Cartera, cheques propios, endosos, rechazos, vencimientos e impresión |
| [Punto de venta](punto-de-venta.md) | Facturación desde caja, impuestos, modalidad y controles |
| [Remitos y transporte](remitos-y-transporte.md) | R, X, autoimpresores, CAI, transportistas y COT |
| [Reportes contables](reportes-contables.md) | IVA, Libro Diario, prorrateo, jurisdicciones y DDJJ |
| [Exportadores impositivos](exportadores-impositivos.md) | Libro IVA Digital, IVA Simple, SICORE, SIFERE y formatos provinciales |
| [Cierre e inflación](cierre-contable-e-inflacion.md) | Ejercicios, controles, cierre, apertura e índices para RECPAM |
| [Servicios ARCA y ARBA](servicios-arca-y-arba.md) | Autenticación, autorización, sincronización y A122R Digital |
| [Cuentas corrientes](cuentas-corrientes.md) | Cuenta por período y composición de saldos pendientes actuales; módulo localizado en 17 |

## Cómo interpretar la evidencia

Las fichas separan texto para el visitante, alcance, diferencias por versión y notas técnicas. `estado: revision` significa que son insumos documentales. **No están conectadas todavía a una colección de Astro y no generan rutas públicas.** La página actual de localización sigue tomando el archivo de `01-paginas-unicas`.

La presencia de una clase, una vista o un manifiesto no prueba una instalación exitosa ni una operación aprobada por el organismo. Se revisaron modelos, métodos, datos, reportes, vistas, imports y manifiestos, pero no se ejecutó Odoo ni se hicieron transacciones contra ARCA, ARBA o el servidor de padrones. No se verificó normativa vigente: las referencias normativas del código se tratan como comportamiento del software, no como asesoramiento fiscal.

Las ramas se leyeron mediante `git show` y `git ls-tree`, sin cambiar el checkout ni modificar el proyecto de localización. Se usaron los commits disponibles localmente, sin `fetch`. Los SHA y fechas están en [_fuentes/ramas.json](_fuentes/ramas.json).

## Fuentes reproducibles

- [_fuentes/excel.json](_fuentes/excel.json): transcripción íntegra de celdas no vacías, incluida la nota sobre impresión de cheques, y huella SHA-256 del archivo.
- [_fuentes/catalogo-temas.json](_fuentes/catalogo-temas.json): cada tema, ficha, observaciones y evidencia por rama con archivo y línea.
- [_fuentes/ramas.json](_fuentes/ramas.json): commits, listado de archivos, versiones de módulos, dependencias y archivos declarados en los manifiestos.
- `_fuentes/inventario-{15.0,17.0,19.0}.json`: índice de clases, métodos y campos; excluye scripts de migración del índice de símbolos.
- [_fuentes/extraer.py](_fuentes/extraer.py): vuelve a generar esas fuentes y la matriz con Python 3, sin paquetes adicionales. No importa ni ejecuta el código de Odoo.

Desde la raíz de `website`:

```bash
python3 content/08-localizacion-argentina/_fuentes/extraer.py --repo /Users/santiago/workspace/eynes/l10n_ar_eynes
```

Las fichas y las conclusiones editoriales se mantienen a mano. Si cambian el Excel o los commits, volver a revisar esas conclusiones después de regenerar los índices. Los selectores de evidencia son explícitos en el script: una coincidencia es una referencia para revisión, no una certificación automática de la funcionalidad.

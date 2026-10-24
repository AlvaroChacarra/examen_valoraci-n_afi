# Simulación, integración y lectura de los Excel

Fuentes prácticas: XLS-001/002, XLS-005, XLS-013/014/016/017, XLS-027, XLS-039 y XLS-042. [Catálogo](../CATALOGO.md).

## Monte Carlo

1. Identificar la medida, numerario y dinámica del observable.
2. Generar normales independientes y transformarlas a la correlación objetivo.
3. Simular los factores hasta cada fecha necesaria, incluyendo fijaciones futuras que entren en denominadores.
4. Calcular el payoff de cada trayectoria y expresarlo en el numerario.
5. Promediar y volver a unidades monetarias. Registrar número de sendas, semilla y error estándar cuando se produzca una valoración nueva.

Dos factores: `Z2=rho Z1+sqrt(1-rho²)epsilon`. Para más factores, usar una factorización válida de la matriz de correlaciones y comprobar su semidefinición positiva. La matriz equicorrelada de tres factores con rho=0,4 es válida. Variar sólo una entrada o variar todo rho son escenarios económicos distintos.

## Cuadratura

Las hojas aproximan esperanzas con una rejilla normal y `phi(z) delta_z`; la doble integral usa densidad bivariante o dos normales independientes según la representación. Verificar masa cubierta por el dominio y convergencia al variar paso y límites. Ponderar sólo una vez por las probabilidades y descontar sólo una vez.

## Tablas What-If y resultados guardados

Las tablas de datos vuelven a ejecutar un cálculo cambiando una entrada o para generar nuevas simulaciones. Sus celdas especiales aparecen como `DataTableFormula` en la extracción. No son macros VBA ni una simple fórmula copiada. RAND y las tablas guardan el último estado del libro: esas cifras no prueban una nueva ejecución.

## Cómo leer la normalización

- Cada hoja conserva todas las etiquetas y enunciados de celdas, notas y nombres definidos.
- Las fórmulas se agrupan por equivalencia de traslación, con primera/última posición, número de celdas y ejemplos literales. Esos extremos no afirman un rectángulo completo.
- Se conservan constantes hasta fila 100 en Markdown; series numéricas posteriores se compactan por columna. El JSON de trabajo local conserva detalle para la generación, pero el agente usa las fichas y las familias.
- Las imágenes matemáticas están extraídas en PNG y enlazadas con su procedencia. Su OCR no fija exponentes ni signos dudosos.
- Las macros de interpolación se han descomprimido y leído estáticamente; no se han ejecutado.
- Las referencias externas, errores guardados y nombres rotos se declaran. No repararlos altera la evidencia original.

Los datos de los ejemplos son pedagógicos y pueden tener fechas antiguas. No sustituirlos por cotizaciones actuales para explicar el procedimiento del curso.

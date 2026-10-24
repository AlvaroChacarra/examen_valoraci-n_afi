# Limitaciones y discrepancias de las fuentes

La normalización conserva la evidencia original. Estas observaciones no reparan ni recalculan los libros. Las fórmulas nuevas que se produzcan al resolver el trabajo deberán verificarse por separado.

## Errores guardados en Excel

| Fuente | Hoja | Errores | Ejemplos |
|---|---|---:|---|
| XLS-009 | Hoja1 | 28 | L15=#NUM!, S20=#NUM!, S21=#NUM!, S22=#NUM!, S23=#NUM! |
| XLS-011 | Hoja1 | 51 | P50=#NUM!, R50=#NUM!, P51=#NUM!, R51=#NUM!, P52=#NUM! |
| XLS-012 | Sheet1 | 1 | AD51=#DIV/0! |

Los errores se concentran en hojas parciales. No atribuirlos automáticamente a la hoja más desarrollada del mismo libro. Un caché sin error tampoco es prueba de recalculación correcta.

## Nombres definidos rotos

| Fuente | Nombres |
|---|---|
| XLS-013 | div |
| XLS-021 | flujos, paso, probs |
| XLS-027 | Nom, spread, vola |
| XLS-035 | Nom, spread, vola |

Los nombres pueden estar sin uso en la fórmula activa. Una referencia rota no demuestra por sí sola que todas las primas del archivo estén mal; requiere trazar sus dependencias.

## Dependencias externas

XLS-040 y XLS-043 contienen un vínculo externo y fórmulas `[1]!interpol(...)`. Se recuperó VBA local de interpolación, pero eso no garantiza que el enlace externo esté resuelto. No se ha obtenido ni ejecutado el libro externo.

## Diferencias concretas observadas

- **XLS-013:** el enunciado incrustado pide rebalanceo mensual y un criterio del 95%; G28 guarda `1/50`. Mantener ambos hechos al explicar el ejercicio.
- **XLS-014:** el input de dividendos existe, pero las fórmulas de simulación/calls muestreadas no usan q. El ejemplo no permite asumir automáticamente comportamiento correcto para q distinto de cero.
- **XLS-016:** la regla ex-dividendo depende del nivel del spot. Explicitar la política usada antes de comparar con un modelo de dividendo fijo garantizado.
- **XLS-017:** I48 implementa el máximo sin strike. El enunciado incrustado también plantea una call sobre el máximo; no etiquetar la prima de la primera como si resolviera ambas.
- **XLS-039:** la fórmula K31 guarda `volash*T`; la acumulación general es `volash*sqrt(T)`. Con T=1 no se distingue. Es una observación de la implementación original, no una corrección aplicada.
- **XLS-040/043:** aparece una etiqueta EUR006M con una curva EUR3M y frecuencias trimestrales. No inferir el tenor sólo de esa etiqueta.
- **XLS-011 frente al encargo:** el ejemplo de curva usa malla uniforme de varianza y volatilidades spot; el encargo fija paso mensual y volatilidades por año. No son intercambiables sin adaptación.
- **XLS-042 frente al PPT:** el anexo trata quanto del propio FX, mientras el encargo usa una acción en dólares. Falta desarrollar la covariación acción-FX.

## Extracción de PDF, fórmulas e imágenes

Los PDF se extrajeron sin reordenar por coordenadas porque las notas de teoría están giradas 90 grados y ese reordenamiento mezclaba las palabras. PDF-006 tiene muchas capturas: se añadió OCR a 60 páginas con poco texto. Las fracciones, raíces, subíndices y signos OCR pueden ser incorrectos.

Se extrajeron 60 imágenes únicas de los Excel, incluidas fórmulas y enunciados. Se conservan como PNG enlazados desde Markdown y se revisaron visualmente. El OCR sirve para búsqueda; las fórmulas centrales están reescritas en conceptos. Una fotografía decorativa repetida no aporta reglas de cálculo.

Algunos números del nombre de un Excel reflejan la paginación de otra edición del temario. Las fichas remiten a páginas físicas verificadas de los PDF recibidos. Varios PDF con nombre 2026 conservan fechas internas 2021–2022.

## Lo que no se ha hecho

No se han ejecutado Solver, What-If ni VBA, ni recalculado los Excel. Se interpretaron estructura y fórmulas estáticamente. No se han generado soluciones nuevas del trabajo ni se ha validado económicamente cada resultado docente. El encargo deja convenciones abiertas para el extra de cesta, enumeradas en [ENCARGO](ejercicios/ENCARGO.md).

## Compresión de series

Las series numéricas posteriores a la fila 100 se compactan por columna; las fórmulas repetidas se agrupan por traslación. Se preservan todas las etiquetas de celdas, familias de cálculo, comentarios y nombres, además de los originales con hash. Esta capa está diseñada para explicar métodos, no para reproducir cada realización aleatoria pegada como número.

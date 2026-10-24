# XLS-022: Opciones sobre el máximo de dos activos

Archivo: **1.5.opcion sobre dos activos_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity/1-5-opcion-sobre-dos-activos-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-022-1-5-opcion-sobre-dos-activos-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar max(X_T,Y_T) y max(max(X_T,Y_T)-K,0), y estudiar la influencia de la correlación.

Primas por distintos métodos y tabla de sensibilidad a correlación. La fórmula I48 de la solución corresponde al máximo sin strike, no a la segunda variante.

## Método observado

Generar normales independientes; correlacionarlas con Z2=rho Z1+sqrt(1-rho²) epsilon; transformar en dos spots lognormales; calcular el payoff; comparar Monte Carlo con integral doble; usar cambio de numerario/Margrabe cuando corresponda; variar rho.

## Teoría relacionada

PDF-007 pp. 34–35 y 40–45. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

No transferir automáticamente el efecto de correlación de un máximo a una cesta promedio. El signo depende del payoff.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `B1:BN2056` | 200 | 2 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `correla` | `Hoja1!$D$27` |
| `K` | `Hoja1!$H$34` |
| `paso` | `Hoja1!$P$41` |
| `T` | `Hoja1!$F$32` |
| `tipo` | `Hoja1!$D$21` |
| `volagorro` | `Hoja1!$AJ$22` |
| `volaX` | `Hoja1!$D$24` |
| `volaY` | `Hoja1!$F$24` |
| `X0` | `Hoja1!$D$23` |
| `Y0` | `Hoja1!$F$23` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `Q43` | `=P43+paso` | -4.8 |
| `O45` | `=O44+paso` | -4.8 |

## Plantilla / solución relacionada

- [XLS-017: pag 1.39 opcion sobre dos activos.xlsx](../fuentes/xls-017-pag-1-39-opcion-sobre-dos-activos.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

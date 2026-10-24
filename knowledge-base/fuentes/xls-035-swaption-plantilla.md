# XLS-035: Swaption payer bajo numerario anualidad

Archivo: **swaption_Plantilla.xlsm**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos/swaption-plantilla.xlsm) · [Extracción detallada](../extracciones/xls-035-swaption-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar el derecho a entrar en un swap payer comparando Black con integración normal.

Prima de swaption N24 y contraste numérico T12 en la solución.

## Método observado

Construir la curva interpolada; obtener anualidad y forward swap; usar la anualidad como numerario; modelizar el swap rate lognormal; aplicar la fórmula call y compararla con la integral del payoff.

## Teoría relacionada

PDF-008 pp. 21–28. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La anualidad corresponde a las fechas del swap subyacente; el tiempo de volatilidad corresponde al vencimiento de la opción.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `C6:T114` | 147 | 10 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Hoja1!$D$9` |
| `fechavalor` | `Hoja1!$D$8` |
| `Nom` | `Hoja1!#REF!` |
| `spread` | `Hoja1!#REF!` |
| `vola` | `Hoja1!#REF!` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `I8` | `=SUM(I17:I55)*deltat` | 8.819777225110117 |
| `D9` | `=3/12` | 0.25 |
| `I10` | `=(I16-I55)/I8` | 0.024422960062495776 |
| `D15` | `=(fechavalor)` | 2021-09-29T00:00:00 |
| `E15` | `=YEARFRAC(fechavalor,D15)` | 0 |
| `I15` | `=interpola(H15,$E$15:$F$36)` | 1 |
| `N15` | `=H16` | 0.25 |
| `H16` | `=H15+deltat` | 0.25 |
| `I16` | `=interpola(H16,$E$15:$F$36,1)` | 0.9994572144870387 |
| `J16` | `=(I16/I17-1)/deltat` | 0.010831746886775129 |

## Plantilla / solución relacionada

- [XLS-027: pag 2.28 swaption.xlsm](../fuentes/xls-027-pag-2-28-swaption.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **True**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Procedimientos recuperados: `InterPola`.
La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.

Nombres con referencia rota: `Nom`, `spread`, `vola`. Ver [limitaciones](../LIMITACIONES.md).

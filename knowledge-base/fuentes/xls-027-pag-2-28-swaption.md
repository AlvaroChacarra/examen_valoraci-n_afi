# XLS-027: Swaption payer bajo numerario anualidad

Archivo: **pag 2.28 swaption.xlsm**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-28-swaption.xlsm) · [Extracción detallada](../extracciones/xls-027-pag-2-28-swaption.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Hoja1 | visible | `C6:T114` | 558 | 21 | 0 |

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
| `T12` | `=SUMPRODUCT(R14:R114,T14:T114)*I8` | 4224.6334208374155 |
| `R14` | `=_xlfn.NORM.DIST(Q14,0,1,FALSE)*0.1` | 1.4867195147342977e-07 |
| `S14` | `=$I$10*EXP(-0.5*$N$6^2*$N$15)*EXP($N$6*SQRT($N$15)*Q14)` | 0.008806795822585145 |
| `T14` | `=$N$14*MAX(S14-$N$16,0)` | 0 |
| `D15` | `=(fechavalor)` | 2021-09-29T00:00:00 |
| `E15` | `=YEARFRAC(fechavalor,D15)` | 0 |
| `I15` | `=interpola(H15,$E$15:$F$36)` | 1 |
| `N15` | `=H16` | 0.25 |
| `Q15` | `=Q14+0.1` | -4.9 |
| `I16` | `=interpola(H16,$E$15:$F$36,1)` | 0.9994572144870387 |

## Plantilla / solución relacionada

- [XLS-035: swaption_Plantilla.xlsm](../fuentes/xls-035-swaption-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **True**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Procedimientos recuperados: `InterPola`.
La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.

Nombres con referencia rota: `Nom`, `spread`, `vola`. Ver [limitaciones](../LIMITACIONES.md).

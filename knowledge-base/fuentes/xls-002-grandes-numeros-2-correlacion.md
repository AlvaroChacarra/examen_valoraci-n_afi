# XLS-002: Correlación y límites de la diversificación

Archivo: **Grandes números-2-correlación.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/fundamentos/ejercicios-valoracion-fundamentos-1/grandes-numeros-2-correlacion.xlsx) · [Extracción detallada](../extracciones/xls-002-grandes-numeros-2-correlacion.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Comparar la concentración de sumas de Bernoulli cuando comparten un factor normal y dejan de ser independientes.

Media, desviación y proporción dentro de un intervalo. La correlación del factor normal no coincide automáticamente con la correlación de las Bernoulli.

## Método observado

Generar una normal común y normales idiosincráticas; construir Y_i=sqrt(rho) Z_común+sqrt(1-rho) Z_i; transformar por umbral normal a Bernoulli(p); sumar; repetir y contrastar con el intervalo y la aproximación TLC.

## Teoría relacionada

PDF-004 pp. 16–21; PDF-005 pp. 30–39. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La construcción de raíz cuadrada exige 0≤rho≤1. No extrapolar esta fórmula a correlaciones negativas.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `B2:U1011` | 4086 | 23 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `epsilon` | `Hoja1!$N$9` |
| `N` | `Hoja1!$I$11` |
| `numsims` | `Hoja1!$T$14` |
| `p` | `Hoja1!$D$2` |
| `rho` | `Hoja1!$D$3` |
| `sigma` | `Hoja1!$I$15` |
| `sims` | `Hoja1!$L$12:$L$1011` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `L6` | `=AVERAGE(L12:L1011)` | 148.595 |
| `L7` | `=STDEV(L12:L1011)` | 8.596678304896487 |
| `C11` | `=NORMSINV(RAND())` | 0.7235853072715372 |
| `I11` | `=COUNT(F12:F307)` | 296 |
| `L11` | `=I12` | 150 |
| `M11` | `=$I$14-epsilon` | 138 |
| `N11` | `=$I$14+epsilon` | 158 |
| `Q11` | `=AVERAGE(O12:O1011)` | 0.782 |
| `D12` | `=SQRT(rho)*$C$11+SQRT(1-rho)*C12` | -0.2108736471218546 |
| `F12` | `=IF(D12<NORMSINV(p),1,0)` | 1 |
| `I12` | `=SUM(OFFSET(F12,0,0,I11,1))` | 150 |
| `L12` | `<DataTableFormula: {'ref': 'L12:L1011', 'ca': '1', 'dt2D': '0', 'dtr': '0', 'r1': 'K11', 'r2': None, 'del1': False, 'del2': False}>` | 145 |
| `T16` | `=MAX(sims)` | 175 |

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

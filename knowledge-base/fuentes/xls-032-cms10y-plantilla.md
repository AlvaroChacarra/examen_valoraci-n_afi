# XLS-032: CMS 10 años y ajuste de convexidad

Archivo: **CMS10Y_Plantilla.xlsm**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos/cms10y-plantilla.xlsm) · [Extracción detallada](../extracciones/xls-032-cms10y-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar un bono de cupones trimestrales referidos al CMS 10Y y comparar con descuento por forward swap sin ajuste.

Valor total corregido R6 frente al valor naive; tabla del impacto de volatilidad.

## Método observado

Interpolar descuentos; calcular para cada fixing la anualidad de diez años y su forward swap; aproximar la inversa de anualidad por alpha+beta S; calcular la corrección de convexidad; sumar cupones descontados y principal; variar volatilidad.

## Teoría relacionada

PDF-008 pp. 29–32. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

El ajuste usa una aproximación de anualidad, no una fórmula exacta de CMS para cualquier curva.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `A2:U117` | 238 | 6 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Hoja1!$G$6` |
| `vola` | `Hoja1!$I$11` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `C10` | `=YEARFRAC($B$10,B10)` | 0 |
| `F10` | `=G10*deltat` | 0 |
| `H10` | `=interpola(F10,$C$10:$D$42,1)` | 1 |
| `I12` | `=vola` | 0.3 |
| `N56` | `=R6` | 0 |
| `O56` | `=T6` | 0 |

## Plantilla / solución relacionada

- [XLS-029: pag 2.35-CMS10Y.xlsm](../fuentes/xls-029-pag-2-35-cms10y.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **True**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Procedimientos recuperados: `InterPola`.
La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.

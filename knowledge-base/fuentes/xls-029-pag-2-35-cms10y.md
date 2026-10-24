# XLS-029: CMS 10 años y ajuste de convexidad

Archivo: **pag 2.35-CMS10Y.xlsm**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-35-cms10y.xlsm) · [Extracción detallada](../extracciones/xls-029-pag-2-35-cms10y.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Hoja1 | visible | `A2:U117` | 516 | 17 | 0 |

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
| `R6` | `=SUM(R11:R50)` | 1.1185342263848255 |
| `C10` | `=YEARFRAC($B$10,B10)` | 0 |
| `F10` | `=G10*deltat` | 0 |
| `H10` | `=interpola(F10,$C$10:$D$42,1)` | 1 |
| `L11` | `=SUM(H12:H51)*deltat` | 8.636255375 |
| `M11` | `=(H11-H51)/L11` | 0.03418072847342129 |
| `O11` | `=1/N11` | 0.1 |
| `P11` | `=1/M11*(H11/L11-1/N11)` | 0.4576471450082744 |
| `Q11` | `=(P11*M11/(O11+P11*M11))*(EXP(I11^2*F11)-1)` | 0.003078018973901568 |
| `R11` | `=M11*H11*(1+Q11)*deltat` | 0.00856051285108172 |
| `T11` | `=H11*M11*deltat` | 0.008534244285243828 |
| `I12` | `=vola` | 0.3 |

## Plantilla / solución relacionada

- [XLS-032: CMS10Y_Plantilla.xlsm](../fuentes/xls-032-cms10y-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **True**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Procedimientos recuperados: `InterPola`.
La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.

# XLS-015: Distribución implícita en calls y puts

Archivo: **pag 1.33 probs implicitas con calls-puts.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-33-probs-implicitas-con-calls-puts.xlsx) · [Extracción detallada](../extracciones/xls-015-pag-1-33-probs-implicitas-con-calls-puts.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Extraer una aproximación a probabilidades riesgo-neutras desde precios o volatilidades por strike y compararla con volatilidad ATM constante.

Probabilidades aproximadas por nivel, suma de masas representadas y comparación gráfica.

## Método observado

Calcular precios de calls y puts para la parrilla de strikes; formar spreads de primas entre strikes vecinos; dividir por el paso para aproximar digitales; deshacer el descuento; comparar probabilidades obtenidas con smile y con vola plana.

## Teoría relacionada

PDF-007 pp. 29–30; PDF-004 pp. 125–130. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Son probabilidades de valoración, no frecuencias históricas. La parrilla finita y la convención del spread afectan la aproximación y las colas.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `A3:U115` | 1318 | 23 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `spot` | `Hoja1!$C$6` |
| `T` | `Hoja1!$C$5` |
| `tipo` | `Hoja1!$C$4` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `C5` | `=(C8-C7)/365` | 0.06027397260273973 |
| `C10` | `=spot*EXP(tipo*T)` | 10502.025400799497 |
| `Q16` | `=SUM(Q17:Q63)` | 1.0000000000000064 |
| `F17` | `=LN(spot/(C17*EXP(-tipo*T)))` | 0.2474339796055991 |
| `G17` | `=D17*SQRT(T)` | 0.12295019684453372 |
| `H17` | `=NORMSDIST(F17/G17+0.5*G17)` | 0.9809579449479666 |
| `I17` | `=NORMSDIST(F17/G17-0.5*G17)` | 0.9744713658952059 |
| `J17` | `=spot*H17-C17*EXP(-tipo*T)*I17` | 2310.934286223609 |
| `K17` | `=spot-C17*EXP(-tipo*T)` | 2301.5814365250553 |
| `L17` | `=J17-K17` | 9.352849698553655 |
| `N17` | `=L18-L17` | 2.1246604455272973 |
| `O17` | `=N17/100` | 0.021246604455272974 |

## Plantilla / solución relacionada

- [XLS-020: 1.3.probs implicitas con calls-puts_Plantilla.xlsx](../fuentes/xls-020-1-3-probs-implicitas-con-calls-puts-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

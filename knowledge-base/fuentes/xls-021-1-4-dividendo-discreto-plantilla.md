# XLS-021: Call con dividendo discreto por condicionamiento

Archivo: **1.4.dividendo discreto_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity/1-4-dividendo-discreto-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-021-1-4-dividendo-discreto-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar una call cuyo dividendo se paga antes del vencimiento, comparando condicionamiento e integración doble.

Precio con dividendo y comparación de procedimientos. La solución añade la hoja integral doble que no está en la plantilla.

## Método observado

Generar escenarios del spot en la fecha del dividendo; aplicar la regla ex-dividendo del archivo; valorar condicionalmente la call durante el periodo restante; integrar y descontar; contrastar con la cuadratura bivariante y con la call sin dividendos.

## Teoría relacionada

PDF-007 pp. 31–33. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La regla de dividendo cuando S es menor que D tiene ramas particulares en la fuente; no sustituirlas silenciosamente por un dividendo garantizado.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| condicionando | visible | `C2:T267` | 5 | 5 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `divid` | `condicionando!$G$12` |
| `flujos` | `#REF!` |
| `K` | `condicionando!$G$11` |
| `paso` | `#REF!` |
| `plazo1` | `condicionando!$E$7` |
| `plazo2` | `condicionando!$F$7` |
| `probs` | `#REF!` |
| `q` | `condicionando!$J$6` |
| `sigma` | `condicionando!$G$14` |
| `spot` | `condicionando!$G$13` |
| `tipo` | `condicionando!$D$3` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### condicionando

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `E8` | `=EXP(-plazo1*tipo)` | 0.9900498337491681 |
| `F8` | `=EXP(-plazo2*tipo)` | 0.9801986733067553 |
| `F9` | `=F8/E8` | 0.990049833749168 |
| `C24` | `=0.1` | 0.1 |
| `O24` | `=SUMPRODUCT(F26:F126,M26:M126)*$E$8` | 0 |

## Plantilla / solución relacionada

- [XLS-016: pag 1.36 dividendo discreto.xlsx](../fuentes/xls-016-pag-1-36-dividendo-discreto.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Nombres con referencia rota: `flujos`, `paso`, `probs`. Ver [limitaciones](../LIMITACIONES.md).

# XLS-044: Tipo swap par en marco multicurva

Archivo: **Anexo1.-calculo-tipo-swap_Plantilla.xlsm**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/anexos-valoracion/anexo1-calculo-tipo-swap-plantilla.xlsm) · [Extracción detallada](../extracciones/xls-044-anexo1-calculo-tipo-swap-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Comparar el tipo swap calculado con proyección y descuento separados frente a usar una sola curva.

Tipo swap mixto Y19 y comparaciones AB19 y AE19 en la solución.

## Método observado

Interpolar las curvas EUR3M y Eonia; obtener forwards de cada una; calcular la anualidad descontada; sumar forwards EUR3M por descuentos Eonia; dividir por anualidad; comparar con todo Eonia y todo EUR3M.

## Teoría relacionada

PDF-009 pp. 15–16. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La fórmula telescópica de una sola curva no debe trasladarse sin cambios al caso multicurva.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| EUR3M | visible | `C3:AF80` | 82 | 2 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `EUR3M!$P$3` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### EUR3M

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `P8` | `=interpola(O8,$D$8:$E$37,1)` | 1 |
| `Q8` | `=interpola(O8,$J$8:$K$52,1)` | 1 |

## Plantilla / solución relacionada

- [XLS-041: Anexo1.p16-calculo-tipo-swap.xlsm](../fuentes/xls-041-anexo1-p16-calculo-tipo-swap.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **True**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Procedimientos recuperados: `InterPola`.
La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.

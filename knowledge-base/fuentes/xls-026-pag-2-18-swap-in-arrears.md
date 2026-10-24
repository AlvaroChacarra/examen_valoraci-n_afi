# XLS-026: Swap usual frente a swap in arrears

Archivo: **pag 2.18 swap in arrears.xlsm**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-18-swap-in-arrears.xlsm) · [Extracción detallada](../extracciones/xls-026-pag-2-18-swap-in-arrears.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Construir flujos de un swap y comparar valoración ingenua y corregida de la rama in arrears.

Valores de ramas, valor total y spread de equilibrio. La solución compara O14 (naive), P14 y Q14.

## Método observado

Interpolar factores de descuento; construir forwards por periodo; calcular anualidad y tipo swap par; valorar ambas ramas del swap usual; corregir los forwards de cada pago temprano; calcular el spread que equilibra el swap modificado con Solver.

## Teoría relacionada

PDF-008 pp. 14–19 y 21–22. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

VBA recuperada: interpolación. El modo 0 interpola logaritmos y el 1 niveles. Conservar la convención elegida en cada llamada.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `C6:S55` | 346 | 17 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Hoja1!$D$9` |
| `fechavalor` | `Hoja1!$D$8` |
| `Nom` | `Hoja1!$M$9` |
| `spread` | `Hoja1!$Q$9` |
| `vola` | `Hoja1!$Q$8` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `I8` | `=SUM(I17:I55)*deltat` | 8.819777225110117 |
| `D9` | `=3/12` | 0.25 |
| `I10` | `=(I16-I55)/I8` | 0.024422960062495776 |
| `L14` | `=SUM(L17:L55)` | 21540.506692897456 |
| `O14` | `=SUM(O16:O54)` | 21693.676837631512 |
| `S14` | `=(Q14-P14)*100000000000` | 14090427907.649427 |
| `D15` | `=(fechavalor)` | 2021-09-29T00:00:00 |
| `I15` | `=interpola(H15,$E$15:$F$36)` | 1 |
| `E16` | `=YEARFRAC(fechavalor,D16)` | 0.08055555555555556 |
| `H16` | `=H15+deltat` | 0.25 |
| `I16` | `=interpola(H16,$E$15:$F$36,1)` | 0.9994572144870387 |
| `J16` | `=(I16/I17-1)/deltat` | 0.010831746886775129 |

## Plantilla / solución relacionada

- [XLS-034: swap in arrears_Plantilla.xlsm](../fuentes/xls-034-swap-in-arrears-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **True**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Procedimientos recuperados: `InterPola`.
La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.

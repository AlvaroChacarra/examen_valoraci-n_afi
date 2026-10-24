# XLS-025: FRA y caplet in arrears lognormales

Archivo: **pag 2.17 fra-caplet-floorlet+in arrears.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-17-fra-caplet-floorlet-in-arrears.xlsx) · [Extracción detallada](../extracciones/xls-025-pag-2-17-fra-caplet-floorlet-in-arrears.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Cuantificar el ajuste de timing al pagar en T un flujo ligado al forward del periodo que termina en T+delta.

FRA usual, forward corregido D25, prima in arrears D26 y caplet corregido D34 en la solución.

## Método observado

Valorar las versiones usuales; expresar el pago temprano bajo la medida T+delta usando 1/P(T,T+delta)=1+delta F_T; calcular momentos lognormales; obtener el forward corregido y su aproximación; valorar la corrección del caplet y comparar.

## Teoría relacionada

PDF-008 pp. 14–19. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

El Excel desarrolla el caso lognormal. El ejercicio 2 del encargo exige normal: sirve de estructura de derivación, no de respuesta final.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `C2:N36` | 26 | 23 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Hoja1!$D$8` |
| `descuento1` | `Hoja1!$G$3` |
| `descuento2` | `Hoja1!$G$4` |
| `fwd0` | `Hoja1!$G$6` |
| `K` | `Hoja1!$D$4` |
| `nom` | `Hoja1!$D$3` |
| `plazo1` | `Hoja1!$D$6` |
| `plazo2` | `Hoja1!$D$7` |
| `vola` | `Hoja1!$D$5` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `G6` | `=(descuento1/descuento2-1)/deltat` | 0.00280673616680005 |
| `D8` | `=D7-D6` | 0.25 |
| `D11` | `=LN(fwd0/K)` | -0.35427205932251843 |
| `F11` | `=D11/D12+0.5*D12` | -1.2336899815404616 |
| `H11` | `=NORMSDIST(F11)` | 0.10865922425738267 |
| `D12` | `=vola*SQRT(plazo1)` | 0.25980762113533157 |
| `F12` | `=D11/D12-0.5*D12` | -1.4934976026757931 |
| `E17` | `=deltat*descuento2*(fwd0*H11-K*H12)*nom` | 0.8570334697247602 |
| `F17` | `=deltat*descuento2*(-fwd0*(1-H11)+K*(1-H12))*nom` | 30.617033469731524 |
| `G17` | `=descuento2*deltat*(fwd0-K)*nom` | -29.76000000000675 |
| `F18` | `=E17-G17` | 30.617033469731513 |
| `G18` | `=E17-F17` | -29.760000000006762 |

## Plantilla / solución relacionada

- [XLS-033: fra-caplet-floorlet+in arrears_Plantilla.xlsx](../fuentes/xls-033-fra-caplet-floorlet-in-arrears-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

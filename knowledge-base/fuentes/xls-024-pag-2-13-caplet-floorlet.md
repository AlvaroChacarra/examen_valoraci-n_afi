# XLS-024: Caplet, floorlet y FRA usuales

Archivo: **pag 2.13 caplet- floorlet.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-13-caplet-floorlet.xlsx) · [Extracción detallada](../extracciones/xls-024-pag-2-13-caplet-floorlet.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar instrumentos que comparten fixing y pago y comprobar la paridad caplet-floorlet.

Primas y comprobación de paridad. La solución usa E19:G19 y F20.

## Método observado

Obtener F0=(P(0,T)/P(0,T+delta)-1)/delta; calcular moneyness y sigma sqrt(T); obtener d+ y d-; valorar call y put sobre forward descontando al pago; comprobar que caplet-floorlet=FRA.

## Teoría relacionada

PDF-008 pp. 5–13. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La volatilidad Black es relativa y requiere el dominio positivo de forward y strike en la fórmula logarítmica.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Ejercicio | visible | `C4:I20` | 12 | 11 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Ejercicio!$D$10` |
| `descuento1` | `Ejercicio!$G$5` |
| `descuento2` | `Ejercicio!$G$6` |
| `fwd0` | `Ejercicio!$G$8` |
| `K` | `Ejercicio!$D$6` |
| `nom` | `Ejercicio!$D$5` |
| `plazo1` | `Ejercicio!$D$8` |
| `plazo2` | `Ejercicio!$D$9` |
| `vola` | `Ejercicio!$D$7` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Ejercicio

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `G8` | `=(descuento1/descuento2-1)/deltat` | 0.004012036108324679 |
| `D10` | `=D9-D8` | 0.25 |
| `D13` | `=LN(fwd0/K)` | 0.5563897472050116 |
| `F13` | `=D13/D14+0.5*D14` | 2.2714489460554077 |
| `H13` | `=NORMSDIST(F13)` | 0.9884400928703331 |
| `D14` | `=vola*SQRT(plazo1)` | 0.25980762113533157 |
| `F14` | `=D13/D14-0.5*D14` | 2.0116413249200757 |
| `E19` | `=deltat*descuento2*(fwd0*H13-K*H14)*nom` | 42.78510265167909 |
| `F19` | `=deltat*descuento2*(-fwd0*(1-H13)+K*(1-H14))*nom` | 0.11260265168644856 |
| `G19` | `=descuento2*deltat*(fwd0-K)*nom` | 42.67249999999263 |
| `F20` | `=E19-G19` | 0.11260265168645844 |

## Plantilla / solución relacionada

- [XLS-031: caplet- floorlet_Plantilla.xlsx](../fuentes/xls-031-caplet-floorlet-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

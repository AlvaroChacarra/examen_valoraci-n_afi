# XLS-031: Caplet, floorlet y FRA usuales

Archivo: **caplet- floorlet_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos/caplet-floorlet-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-031-caplet-floorlet-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Ejercicio | visible | `C4:I20` | 1 | 1 | 0 |

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
| `D10` | `=D9-D8` | 0.25 |

## Plantilla / solución relacionada

- [XLS-024: pag 2.13 caplet- floorlet.xlsx](../fuentes/xls-024-pag-2-13-caplet-floorlet.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

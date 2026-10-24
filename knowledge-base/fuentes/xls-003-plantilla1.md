# XLS-003: Mercado matricial: réplica, arbitraje y numerarios

Archivo: **Plantilla1.xlsx**. Papel: **plantilla**.

[Original](../../raw/fundamentos/ejercicios-valoracion-fundamentos-1/plantilla1.xlsx) · [Extracción detallada](../extracciones/xls-003-plantilla1.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Usar precios actuales y flujos en cuatro escenarios para buscar arbitraje, replicar activos y calcular probabilidades de valoración.

Pesos, coste de la réplica, errores por escenario y probabilidades por numerario. Las soluciones usan MMULT, MINVERSE y MDETERM.

## Método observado

Formar la matriz de pagos; proponer pesos de cartera; comparar flujos con el activo objetivo; resolver por Solver o inversión matricial; valorar la réplica con los precios actuales; imponer ecuaciones de martingala tras elegir numerario.

## Teoría relacionada

PDF-004 pp. 37–76; PDF-005 pp. 59–92. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Una probabilidad válida debe sumar uno y ser positiva bajo los supuestos de equivalencia usados en clase. Un sistema algebraico con solución no basta.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `B1:XFD79` | 0 | 0 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `matrizS` | `Hoja1!$D$8:$G$11` |
| `preciosHoy` | `Hoja1!$B$8:$B$11` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| — | No hay fórmulas de celda en esta hoja | — |

## Plantilla / solución relacionada

- [XLS-007: Plantilla1_Solucion.xlsx](../fuentes/xls-007-plantilla1-solucion.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

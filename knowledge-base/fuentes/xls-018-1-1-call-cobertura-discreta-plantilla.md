# XLS-018: Call Black–Scholes y error de cobertura discreta

Archivo: **1.1.call-cobertura discreta_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity/1-1-call-cobertura-discreta-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-018-1-1-call-cobertura-discreta-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Medir por simulación el descasamiento entre una call y una cartera que se rebalancea con frecuencia finita, y calcular una prima con un criterio de cobertura del 95%.

Distribución del descasamiento y prima necesaria para que el saldo sea positivo con probabilidad 95%, según el enunciado incrustado.

## Método observado

Valorar call, put y forward; simular S lognormal; calcular delta con plazo restante; actualizar acciones y cash autofinanciados; comparar valor final con payoff; repetir, construir histograma y estudiar el percentil del error.

## Teoría relacionada

PDF-007 pp. 18–28. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

El texto incrustado menciona rebalanceo mensual, pero el control guardado G28=1/50. Distinguir contrato didáctico de parametrización guardada.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Ejercicio | visible | `A10:AF4961` | 27 | 2 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Ejercicio!$G$28` |
| `K` | `Ejercicio!$D$12` |
| `numsims` | `Ejercicio!$O$60` |
| `pasohist` | `Ejercicio!$O$65` |
| `S0` | `Ejercicio!$D$14` |
| `sigma` | `Ejercicio!$D$15` |
| `T` | `Ejercicio!$D$11` |
| `tipo` | `Ejercicio!$D$13` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Ejercicio

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `G28` | `=1/50` | 0.02 |
| `D44` | `=D32*deltat` | 0 |

## Plantilla / solución relacionada

- [XLS-013: pag 1.27 call-cobertura discreta.xlsx](../fuentes/xls-013-pag-1-27-call-cobertura-discreta.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

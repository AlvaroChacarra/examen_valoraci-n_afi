# XLS-007: Mercado matricial: réplica, arbitraje y numerarios

Archivo: **Plantilla1_Solucion.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/fundamentos/sesion-ii/plantilla1-solucion.xlsx) · [Extracción detallada](../extracciones/xls-007-plantilla1-solucion.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Hoja1 | visible | `B1:XFD91` | 135 | 29 | 0 |

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
| `S6` | `=MMULT($N$6:$Q$6,D8:D11)` | 0.3074688215416401 |
| `S8` | `=SUMPRODUCT(S6:V6,S6:V6)` | 1.9642047648917962 |
| `N9` | `=MMULT(N6:Q6,preciosHoy)` | 0.6943301213665183 |
| `I18` | `=MMULT(J18:M18,preciosHoy)` | 0.5562492889329631 |
| `N18` | `=MMULT($J18:$M18,D$8:D$11)` | 0.9999993650317265 |
| `R18` | `=(N18-D18)^2` | 4.0318470837224374e-13 |
| `V18` | `=SQRT(SUM(R18:U18))*1000000` | 3.4290569357075134 |
| `J26` | `=MMULT(D26:G26,$S$27:$V$30)` | -1.9374999999999962 |
| `V26` | `=MDETERM(matrizS)` | -4.000000000000009 |
| `S27` | `=MINVERSE(matrizS)` | 1.9999999999999958 |
| `B39` | `=B8` | 1.5 |
| `D39` | `=D8:G8` | 2 |
| `E56` | `=(SUMPRODUCT($D$54:$G$54,D45:G45)-B45)^2` | 1.1484442647221026e-13 |
| `N56` | `=(SUMPRODUCT($M$54:$P$54,M45:P45)-K45)^2` | 6.122438898224819e-17 |
| `D68` | `=TRANSPOSE(MMULT(D62:G65,B45:B48))` | 0.13333333333333286 |
| `D78` | `=SUMPRODUCT(D76:G76,D68:G68)*B39` | 0.09999999999999964 |

## Plantilla / solución relacionada

- [XLS-003: Plantilla1.xlsx](../fuentes/xls-003-plantilla1.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

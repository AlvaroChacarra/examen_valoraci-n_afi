# XLS-005: Jarrow–Rudd: árbol, simulación, valoración y réplica

Archivo: **Plantilla_3 - Solucion1.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/fundamentos/plantilla-3-solucion1.xlsx) · [Extracción detallada](../extracciones/xls-005-plantilla-3-solucion1.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Construir un árbol binomial calibrado a tipo y volatilidad y comparar distintos métodos de valoración de una opción europea.

Prima, comparación con Black–Scholes, árboles de cash/delta y simulación de cobertura. La solución contiene el JR con ajuste exacto de martingala mediante cosh.

## Método observado

Calcular u,d,p=1/2 y descuentos; construir el árbol de S; comprobar la distribución y varianza de log-retornos; simular sendas; valorar por fórmula binomial, backward induction y simulación; obtener las posiciones de réplica.

## Teoría relacionada

PDF-003 pp. 6–60; PDF-006 pp. 4–46. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Plantilla de seis pasos, no solución del encargo de 36 pasos. No sustituir la especificación exacta por su aproximación exponencial sin decirlo.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `A3:R3061` | 198 | 48 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `call_put` | `Hoja1!$D$48` |
| `d` | `Hoja1!$H$12` |
| `deltat` | `Hoja1!$D$11` |
| `desc_per` | `Hoja1!$D$13` |
| `desc_T` | `Hoja1!$D$14` |
| `factorVola` | `Hoja1!$K$11` |
| `p` | `Hoja1!$H$13` |
| `S0` | `Hoja1!$D$7` |
| `strike` | `Hoja1!$D$49` |
| `T` | `Hoja1!$D$12` |
| `tipo` | `Hoja1!$D$5` |
| `u` | `Hoja1!$H$11` |
| `vola` | `Hoja1!$D$6` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `D11` | `=1/12` | 0.08333333333333333 |
| `H11` | `=EXP(tipo*deltat)*EXP(vola*SQRT(deltat))*(2/(EXP(vola*SQRT(deltat))+EXP(-vola*SQRT(deltat))))` | 1.0869300107425321 |
| `D12` | `=6*deltat` | 0.5 |
| `H12` | `=EXP(tipo*deltat)*EXP(-vola*SQRT(deltat))*(2/(EXP(vola*SQRT(deltat))+EXP(-vola*SQRT(deltat))))` | 0.9140702392991397 |
| `D20` | `=S0` | 80 |
| `E20` | `=D20*u` | 86.95440085940257 |
| `M20` | `=BINOMDIST(L20,$L$20,p,FALSE)` | 0.015625000000000007 |
| `N20` | `=SUMPRODUCT(M20:M26,J20:J26)/J32` | 80.00000000000004 |
| `P20` | `=LN(J20/$D$20)` | 0.5001433111484215 |
| `R20` | `=SUMPRODUCT(P20:P26,M20:M26)^2` | 0.00037915610162931847 |
| `E21` | `=D20*d` | 73.12561914393117 |
| `R22` | `=SUMPRODUCT(P20:P26^2,M20:M26)` | 0.04537915610162931 |
| `P55` | `=MAX(call_put*(J41-strike),0)` | 9.294371983025599 |
| `H56` | `=SUMPRODUCT(F57:F63,E57:E63)*EXP(-tipo*T)` | 5.43610123490592 |
| `F57` | `=MAX(call_put*(D57-strike),0)` | 47.91660542163655 |
| `R62` | `=AVERAGE(P62:P3061)` | 5.274036021989797 |
| `J68` | `=MAX(call_put*(J20-strike),0)` | 47.91660542163655 |

## Plantilla / solución relacionada

- [XLS-006: Plantilla_3.xlsx](../fuentes/xls-006-plantilla-3.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

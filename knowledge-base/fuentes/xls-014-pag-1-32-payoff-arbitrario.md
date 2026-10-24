# XLS-014: Payoff arbitrario: integral, Monte Carlo y descomposición

Archivo: **pag 1.32 payoff arbitrario.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-32-payoff-arbitrario.xlsx) · [Extracción detallada](../extracciones/xls-014-pag-1-32-payoff-arbitrario.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar un payoff triangular y contrastar tres procedimientos que deben representar el mismo flujo.

Precio por cuadratura, por simulación y por cartera de calls. La equivalencia de la mariposa exige la relación apropiada entre los cortes.

## Método observado

Leer los tres cortes; implementar f(S_T); integrar contra una normal transformada a S_T; simular S_T y promediar pagos; descomponer el payoff en una call comprada, dos vendidas y otra comprada; descontar y comparar.

## Teoría relacionada

PDF-007 pp. 29–30. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La hoja contiene una tasa de dividendos pero las fórmulas muestreadas de simulación y calls usan tipo, sin restar div. Comprobar el caso con q≠0 antes de reutilizarlo.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Ejercicio | visible | `C3:S2207` | 7054 | 19 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `corte1` | `Ejercicio!$D$12` |
| `corte2` | `Ejercicio!$D$13` |
| `corte3` | `Ejercicio!$D$14` |
| `div` | `Ejercicio!$D$6` |
| `paso` | `Ejercicio!$D$21` |
| `S0` | `Ejercicio!$D$7` |
| `sigma` | `Ejercicio!$D$8` |
| `T` | `Ejercicio!$D$4` |
| `tipo` | `Ejercicio!$D$5` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Ejercicio

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `R16` | `=COUNT(S24:S2207)` | 2184 |
| `F21` | `=SUMPRODUCT(F25:F145,D25:D145)*EXP(-tipo*T)` | 5.388956549248451 |
| `R21` | `=AVERAGE(S24:S2207)*EXP(-tipo*T)` | 5.284175642880174 |
| `Q24` | `=NORMSINV(RAND())` | 1.8273148784289743 |
| `R24` | `=S0*EXP((tipo-0.5*sigma^2)*T)*EXP(sigma*SQRT(T)*Q24)` | 54.11389362560549 |
| `S24` | `=IF(R24<=corte1,0,IF(R24<=corte2,R24-corte1,IF(R24<=corte3,corte3-R24,0)))` | 0 |
| `D25` | `=NORMDIST(C25,0,1,FALSE)*paso` | 6.075882849823286e-10 |
| `E25` | `=S0*EXP((tipo-0.5*sigma^2)*T)*EXP(sigma*SQRT(T)*C25)` | 17.888203636126562 |
| `C26` | `=C25+paso` | -5.9 |
| `J28` | `=LN(S0*EXP(tipo*T)/corte1)` | 0.3414722366212129 |
| `K28` | `=sigma*SQRT(T)` | 0.14142135623730953 |
| `L28` | `=J28/K28+0.5*K28` | 2.485284019136624 |

## Plantilla / solución relacionada

- [XLS-019: 1.2.payoff arbitrario_Plantilla.xlsx](../fuentes/xls-019-1-2-payoff-arbitrario-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

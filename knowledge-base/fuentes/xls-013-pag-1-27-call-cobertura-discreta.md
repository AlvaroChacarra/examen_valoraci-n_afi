# XLS-013: Call Black–Scholes y error de cobertura discreta

Archivo: **pag 1.27 call-cobertura discreta.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-27-call-cobertura-discreta.xlsx) · [Extracción detallada](../extracciones/xls-013-pag-1-27-call-cobertura-discreta.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Ejercicio | visible | `A1:AF4961` | 402 | 39 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Ejercicio!$G$28` |
| `div` | `Ejercicio!#REF!` |
| `K` | `Ejercicio!$D$12` |
| `numsims` | `Ejercicio!$O$60` |
| `pasohist` | `Ejercicio!$O$65` |
| `S0` | `Ejercicio!$D$14` |
| `sigma` | `Ejercicio!$D$15` |
| `sims` | `Ejercicio!$D$59:$D$4961` |
| `T` | `Ejercicio!$D$11` |
| `tipo` | `Ejercicio!$D$13` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Ejercicio

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `G11` | `=LN(S0*EXP(tipo*T)/K)` | 0.05379016416943189 |
| `G12` | `=sigma*SQRT(T)` | 0.14142135623730953 |
| `G13` | `=G11/G12+0.5*G12` | 0.45106457657208415 |
| `G14` | `=G11/G12-0.5*G12` | 0.3096432203347746 |
| `G15` | `=NORMSDIST(G13)` | 0.6740284962785699 |
| `D20` | `=S0*G15-K*EXP(-tipo*T)*G16` | 3.569849048924663 |
| `E20` | `=D20/S0` | 0.0849964059267777 |
| `D21` | `=K*EXP(-tipo*T)*(1-G16)-S0*(1-G15)` | 1.3703482166319567 |
| `D22` | `=D20-D21` | 2.1995008322927063 |
| `G28` | `=1/50` | 0.02 |
| `D33` | `=D32*deltat` | 0 |
| `E34` | `=NORMSINV(RAND())` | -0.7024249743872925 |
| `D50` | `=MAX(AC35-K,0)` | 0 |
| `O62` | `=AVERAGE(sims)` | 0.004340624953456996 |
| `O63` | `=MAX(sims)` | 1.5387639571579825 |

## Plantilla / solución relacionada

- [XLS-018: 1.1.call-cobertura discreta_Plantilla.xlsx](../fuentes/xls-018-1-1-call-cobertura-discreta-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Nombres con referencia rota: `div`. Ver [limitaciones](../LIMITACIONES.md).

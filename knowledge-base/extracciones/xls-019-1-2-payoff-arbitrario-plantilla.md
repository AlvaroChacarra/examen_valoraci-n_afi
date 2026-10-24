# XLS-019: 1.2.payoff arbitrario_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity/1-2-payoff-arbitrario-plantilla.xlsx). SHA-256: `7fc364a3702dc630fb50180b8b3545a7cf35cd45f3286bebfaf6c308f49563d6`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
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

## Hoja: Ejercicio

Estado: `visible`. Rango usado: `C3:S2207`. Celdas con contenido: 2224. Fórmulas: 1. Familias: 1.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C3` | Datos |
| `C4` | T |
| `C5` | tipo |
| `C6` | tasa divid |
| `C7` | S0 |
| `C8` | sigma |
| `F10` | La función f es |
| `C12` | corte1 |
| `C13` | corte2 |
| `C14` | corte3 |
| `Q16` | numsims |
| `C18` | cálculo numérico de la integral |
| `I18` | Cálculo por desestructuración  |
| `P18` | cálculo por simulación |
| `F20` | valor numérico |
| `R20` | valor por simulación |
| `C21` | paso |
| `C23` | valores normal |
| `D23` | probs |
| `E23` | S_T |
| `F23` | payoff |
| `Q23` | normal |
| `R23` | S_T |
| `S23` | payoff |
| `J27` | moneyness |
| `K27` | vola acum |
| `L27` | d+ |
| `M27` | d- |
| `N27` | precios |
| `K32` | valor por desestructuración |
| `P24 … P2207` | sim1 … sim2184 (2184 etiquetas consecutivas, compactadas) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D4` | 0.5 | `General` |
| `D5` | 0.01 | `0%` |
| `D6` | 0 | `0%` |
| `D7` | 42 | `General` |
| `D8` | 0.2 | `0%` |
| `D12` | 30 | `General` |
| `D13` | 40 | `General` |
| `D14` | 50 | `General` |
| `D21` | 0.1 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `R16` | `R16` | 1 | `=COUNTA(P24:P2207)` | 2184 |

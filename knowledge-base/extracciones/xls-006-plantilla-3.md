# XLS-006: Plantilla_3.xlsx

Original: [archivo raw](../../raw/fundamentos/sesion-ii/plantilla-3.xlsx). SHA-256: `9a65ce1bea71c4207d82fdf9d79a6bb0964bc826410d06526a1a5810fc780e21`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `call_put` | `Hoja1!$D$48` |
| `d` | `Hoja1!$H$12` |
| `deltat` | `Hoja1!$D$11` |
| `desc_per` | `Hoja1!$D$13` |
| `desc_T` | `Hoja1!$D$14` |
| `factorVola` | `Hoja1!$K$11` |
| `S0` | `Hoja1!$D$7` |
| `strike` | `Hoja1!$D$49` |
| `T` | `Hoja1!$D$12` |
| `tipo` | `Hoja1!$D$5` |
| `u` | `Hoja1!$H$11` |
| `vola` | `Hoja1!$D$6` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `C3:R3061`. Celdas con contenido: 3096. Fórmulas: 5. Familias: 5.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C3` | Datos de mercado |
| `C5` | tipo |
| `C6` | volatilidad |
| `C7` | S0 |
| `G8` | Cálculo de los parámetros del modelo |
| `C9` | Datos del modelo |
| `C11` | Deltat |
| `G11` | u |
| `C12` | Vencimiento |
| `G12` | d |
| `G13` | p |
| `C17` | Árbol de evolución de los valores del subyacente |
| `C19` | tiempo |
| `M19` | probs |
| `P19` | rendimientos |
| `R19` | (media rendimientos) ^2 |
| `R21` | media (rends^2) |
| `R23` | varianza rendimientos |
| `R25` | desviación típica rends |
| `R27` | y esperábamos acumular |
| `C30` | CuentaBancaria |
| `C31` | tiempo |
| `C35` | Simulación en el árbol |
| `C38` | senda de +1/-1 |
| `C39` | bajada? |
| `C40` | acumuladas |
| `C41` | senda de valores |
| `C45` | Valoración de opciones europeas |
| `C47` | Instrumento |
| `H47` | 0. Con la fórmula de Black-Scholes |
| `C48` | Call/put |
| `H48` | d+ |
| `C49` | strike |
| `H49` | d- |
| `H50` | prima |
| `C52` | 1. Con probabilidades |
| `O52` | 2. Por simulación |
| `D54` | valores subyacente  vencimiento |
| `E55` | probabilidades |
| `F55` | flujos instrumento |
| `H55` | valor instrumento |
| `O55` | flujo en simulación |
| `O56` | flujo descontado |
| `O59` | tabla de simulaciones |
| `R59` | número de sims |
| `R61` | valor por simulación |
| `C65` | 3. Valoración en el árbol |
| `C67` | tiempo |
| `O62 … O3061` | sim1 … sim3000 (3000 etiquetas consecutivas, compactadas) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D5` | 0.006 | `0.0%` |
| `D6` | 0.3 | `0%` |
| `D7` | 80 | `General` |
| `D19` | 0 | `General` |
| `E19` | 1 | `General` |
| `F19` | 2 | `General` |
| `G19` | 3 | `General` |
| `H19` | 4 | `General` |
| `I19` | 5 | `General` |
| `J19` | 6 | `General` |
| `L20` | 6 | `General` |
| `L21` | 5 | `General` |
| `L22` | 4 | `General` |
| `L23` | 3 | `General` |
| `L24` | 2 | `General` |
| `L25` | 1 | `General` |
| `L26` | 0 | `General` |
| `D31` | 0 | `General` |
| `E31` | 1 | `General` |
| `F31` | 2 | `General` |
| `G31` | 3 | `General` |
| `H31` | 4 | `General` |
| `I31` | 5 | `General` |
| `J31` | 6 | `General` |
| `D37` | 0 | `General` |
| `E37` | 1 | `General` |
| `F37` | 2 | `General` |
| `G37` | 3 | `General` |
| `H37` | 4 | `General` |
| `I37` | 5 | `General` |
| `J37` | 6 | `General` |
| `D48` | 1 | `General` |
| `D49` | 84 | `General` |
| `D67` | 0 | `General` |
| `E67` | 1 | `General` |
| `F67` | 2 | `General` |
| `G67` | 3 | `General` |
| `H67` | 4 | `General` |
| `I67` | 5 | `General` |
| `J67` | 6 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `D11` | `D11` | 1 | `=1/12` | 0.08333333333333333 |
| `D12` | `D12` | 1 | `=6*deltat` | 0.5 |
| `I48` | `I48` | 1 | `=(LN(S0/strike)+(tipo+0.5*vola^2)*T)/(vola*SQRT(T))` | -0.10979088679435575 |
| `I49` | `I49` | 1 | `=(LN(S0/strike)+(tipo-0.5*vola^2)*T)/(vola*SQRT(T))` | -0.32192292115032 |
| `I50` | `I50` | 1 | `=S0*NORMSDIST(I48)-strike*EXP(-T*tipo)*NORMSDIST(I49)` | 5.201588299180152 |

### Notas de celdas

- `I50`: se trata de otro modelo (en realidad el límite de éste cuando Deltat->0), pero sirve de referencia

- `P61`: Genera una tabla de simulaciones con el procedimiento habitual  (está borrada para que no afecte al cállculo de la hoja)
- `I68`: el resto del árbol se rellena con la condición de martingala

- `J68`: a vencimiento registramos el payoff de la opción

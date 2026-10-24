# XLS-042: Anexo2.FX.xlsx

Original: [archivo raw](../../raw/marco-black/anexos-valoracion-marco-black-soluciones/anexo2-fx.xlsx). SHA-256: `15990deb6f3d8875714b3bdce35db81990532658eaf948473aa5399d89fd21ef`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `descd` | `Hoja1!$E$14` |
| `desce` | `Hoja1!$E$13` |
| `FX0` | `Hoja1!$D$12` |
| `FXf0` | `Hoja1!$D$15` |
| `FXfwd0` | `Hoja1!$D$15` |
| `K` | `Hoja1!$D$9` |
| `nom` | `Hoja1!$D$10` |
| `probabs` | `Hoja1!$O$12:$O$952` |
| `T` | `Hoja1!$D$8` |
| `tipod` | `Hoja1!$D$14` |
| `tipoe` | `Hoja1!$D$13` |
| `vola` | `Hoja1!$D$11` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `A5:Y952`. Celdas con contenido: 9494. Fórmulas: 9442. Familias: 36.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `I5` | Con fórmulas |
| `N5` | Con cálculo numérico |
| `Q6` | primas |
| `P7` | con fórmula |
| `C8` | T |
| `P8` | con cálculo numérico |
| `C9` | K |
| `I9` | fwd quanto |
| `J9` | paga FX(T)*Nom |
| `K9` | en dólares |
| `C10` | nom |
| `C11` | vola |
| `I11` | prima |
| `N11` | valores norm |
| `O11` | probs |
| `P11` | FXf(T) |
| `Q11` | flujo call |
| `R11` | flujo put |
| `S11` | flujo fwd |
| `U11` | flujo fwd quanto |
| `V11` | flujo call quanto |
| `W11` | call binaria dól |
| `X11` | call binaria eur |
| `C12` | FX0 |
| `C13` | tipoe |
| `C14` | tipod |
| `I14` | call quanto |
| `C15` | FXfwd0 |
| `I16` | d* |
| `C17` | moneyness |
| `I17` | phi(d*) |
| `C18` | vola acum |
| `C20` | d+ |
| `I20` | prima |
| `C21` | d- |
| `C23` | phi(d+) |
| `I23` | call binaria que paga en dólares |
| `C24` | phi(d-) |
| `I25` | prima |
| `C26` | prima call |
| `C27` | prima put |
| `C29` | fwd |
| `I29` | call binaria que paga en euros |
| `I31` | prima |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D8` | 1 | `General` |
| `D9` | 0.9 | `General` |
| `D10` | 1000000 | `#,##0.00\ [$USD]` |
| `D11` | 0.15 | `0%` |
| `D12` | 0.8 | `General` |
| `N12` | -5 | `General` |
| `D13` | 0.005 | `0.0%` |
| `D14` | 0.015 | `0.00%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `Q7` | `Q7` | 1 | `=D26` | 13804.761178764755 |
| `R7` | `R7` | 1 | `=D27` | 121149.8093369884 |
| `S7` | `S7` | 1 | `=D29` | -107345.04815822365 |
| `U7` | `U7` | 1 | `=J11` | -70823.32696782584 |
| `V7` | `V7` | 1 | `=J20` | 14371.20955209884 |
| `W7` | `W7` | 1 | `=J25` | 172459.01234405185 |
| `X7` | `X7` | 1 | `=J31` | 176282.50129476347 |
| `Q8` | `X8` | 7 | `=SUMPRODUCT(Q12:Q952,probabs)*desce` | 13801.379041672248 |
| `J11` | `J11` | 1 | `=E13*FXfwd0*(FXfwd0*EXP(vola^2*T)-K)*nom` | -70823.32696782584 |
| `O12` | `O952` | 941 | `=NORMDIST(N12,0,1,FALSE)*0.01` | 1.4867195147342977e-08 |
| `P12` | `P952` | 941 | `=FXf0*EXP(-0.5*T*vola^2)*EXP(vola*SQRT(T)*N12)` | 0.3699843312191504 |
| `Q12` | `Q952` | 941 | `=MAX(P12-K,0)*nom` | 0 |
| `R12` | `R952` | 941 | `=MAX(K-P12,0)*nom` | 530015.6687808495 |
| `S12` | `S952` | 941 | `=(P12-K)*nom` | -530015.6687808495 |
| `U12` | `U952` | 941 | `=(P12-K)*P12*nom` | -196097.49274955338 |
| `V12` | `V952` | 941 | `=MAX(P12-K,0)*P12*nom` | 0 |
| `W12` | `W952` | 941 | `=IF(P12>K,nom*P12,0)` | 0 |
| `X12` | `X952` | 941 | `=IF(P12>K,nom,0)` | 0 |
| `E13` | `E13` | 1 | `=1/(1+tipoe*T)` | 0.9950248756218907 |
| `N13` | `N952` | 940 | `=N12+0.01` | -4.99 |
| `E14` | `E14` | 1 | `=1/(1+tipod*T)` | 0.9852216748768474 |
| `D15` | `D15` | 1 | `=FX0*(1+tipoe)/(1+tipod)` | 0.7921182266009852 |
| `E15` | `E15` | 1 | `=FX0*E14/E13` | 0.7921182266009853 |
| `J16` | `J16` | 1 | `=D17/D18+1.5*D18` | -0.6262273775939676 |
| `D17` | `D17` | 1 | `=LN(FXfwd0/K)` | -0.12768410663909513 |
| `J17` | `J17` | 1 | `=NORMSDIST(J16)` | 0.2655829061777551 |
| `D18` | `D18` | 1 | `=vola*SQRT(T)` | 0.15 |
| `D20` | `D20` | 1 | `=D17/D18+0.5*D18` | -0.7762273775939676 |
| `J20` | `J20` | 1 | `=nom*E13*(FXfwd0^2*EXP(vola^2*T)*J17-K*FXfwd0*D23)` | 14371.20955209884 |
| `D21` | `D21` | 1 | `=D17/D18-0.5*D18` | -0.9262273775939676 |
| `D23` | `D24` | 2 | `=NORMSDIST(D20)` | 0.2188073719115158 |
| `J25` | `J25` | 1 | `=desce*FXf0*D23*nom` | 172459.01234405185 |
| `D26` | `D26` | 1 | `=E13*(FXfwd0*D23-K*D24)*nom` | 13804.761178764755 |
| `D27` | `D27` | 1 | `=D26-D29` | 121149.8093369884 |
| `D29` | `D29` | 1 | `=(E14*FX0-K*E13)*nom` | -107345.04815822365 |
| `J31` | `J31` | 1 | `=desce*nom*D24` | 176282.50129476347 |

### Notas de celdas

- `N12`: Observa que ponemos paso 0.01 para aumentar precisión del cálculo

# XLS-005: Plantilla_3 - Solucion1.xlsx

Original: [archivo raw](../../raw/fundamentos/plantilla-3-solucion1.xlsx). SHA-256: `25e6734128a6694eb781e447c4bd46460834d6ddf5f5cad6358f554b67aa8de2`.

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
| `p` | `Hoja1!$H$13` |
| `S0` | `Hoja1!$D$7` |
| `strike` | `Hoja1!$D$49` |
| `T` | `Hoja1!$D$12` |
| `tipo` | `Hoja1!$D$5` |
| `u` | `Hoja1!$H$11` |
| `vola` | `Hoja1!$D$6` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `A3:R3061`. Celdas con contenido: 6380. Fórmulas: 198. Familias: 48.

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
| `C78` | 4. Árbol de deltas |
| `C80` | tiempo |
| `L91` | Flujo Derivado |
| `C92` | senda de valores |
| `C95` | Uds de subyacente |
| `C96` | Uds de dinero |
| `C98` | Valor de cartera antes de recomponer |
| `C99` | Valor de cartera después de recomponer |
| `C102` | Valoración de opciones americanas |
| `C103` | Instrumento |
| `C104` | Call/put |
| `C105` | strike |
| `C107` | 5. Valoración en el árbol |
| `C109` | tiempo |
| `C118` | 6. Árbol de deltas |
| `C120` | tiempo |
| `C129` | 7. Árbol de Ejercicio |
| `C131` | tiempo |
| `C140` | 8. Árbol de Decisión |
| `C142` | tiempo |
| `C152` | 9. Cálculo de la cartera replicante |
| `L154` | Flujo Derivado |
| `C155` | Senda Sim Posición |
| `C156` | Senda Ejercicio |
| `C157` | senda de valores |
| `C160` | Uds de subyacente |
| `C161` | Uds de dinero |
| `C163` | Valor de cartera antes de recomponer |
| `C164` | Valor de cartera después de recomponer |
| `O62 … O3061` | sim1 … sim3000 (3000 etiquetas consecutivas, compactadas) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D5` | 0.006 | `0.0%` |
| `D6` | 0.3 | `0%` |
| `D7` | 80 | `General` |
| `H13` | 0.5 | `0%` |
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
| `D32` | 1 | `General` |
| `D37` | 0 | `General` |
| `E37` | 1 | `General` |
| `F37` | 2 | `General` |
| `G37` | 3 | `General` |
| `H37` | 4 | `General` |
| `I37` | 5 | `General` |
| `J37` | 6 | `General` |
| `D48` | 1 | `General` |
| `D49` | 84 | `General` |
| `P63` | 9.266530649957122 | `General` |
| `P64` | 0 | `General` |
| `P65` | 0 | `General` |
| `P66` | 0 | `General` |
| `D67` | 0 | `General` |
| `E67` | 1 | `General` |
| `F67` | 2 | `General` |
| `G67` | 3 | `General` |
| `H67` | 4 | `General` |
| `I67` | 5 | `General` |
| `J67` | 6 | `General` |
| `P67` | 0 | `General` |
| `P68` | 0 | `General` |
| `P69` | 9.266530649957122 | `General` |
| `P70` | 9.266530649957122 | `General` |
| `P71` | 0 | `General` |
| `P72` | 0 | `General` |
| `P73` | 9.266530649957122 | `General` |
| `P74` | 0 | `General` |
| `P75` | 26.856574711664848 | `General` |
| `P76` | 0 | `General` |
| `P77` | 0 | `General` |
| `P78` | 0 | `General` |
| `P79` | 0 | `General` |
| `D80` | 0 | `General` |
| `E80` | 1 | `General` |
| `F80` | 2 | `General` |
| `G80` | 3 | `General` |
| `H80` | 4 | `General` |
| `I80` | 5 | `General` |
| `J80` | 6 | `General` |
| `P80` | 0 | `General` |
| `P81` | 9.266530649957122 | `General` |
| `P82` | 0 | `General` |
| `P83` | 47.77307101463293 | `General` |
| `P84` | 0 | `General` |
| `P85` | 0 | `General` |
| `P86` | 0 | `General` |
| `P87` | 0 | `General` |
| `P88` | 0 | `General` |
| `P89` | 0 | `General` |
| `P90` | 0 | `General` |
| `D91` | 0 | `General` |
| `E91` | 1 | `General` |
| `F91` | 2 | `General` |
| `G91` | 3 | `General` |
| `H91` | 4 | `General` |
| `I91` | 5 | `General` |
| `J91` | 6 | `General` |
| `P91` | 0 | `General` |
| `P92` | 26.856574711664848 | `General` |
| `P93` | 0 | `General` |
| `D94` | 0 | `General` |
| `E94` | 1 | `General` |
| `F94` | 2 | `General` |
| `G94` | 3 | `General` |
| `H94` | 4 | `General` |
| `I94` | 5 | `General` |
| `J94` | 6 | `General` |
| `P94` | 26.856574711664848 | `General` |
| `P95` | 0 | `General` |
| `P96` | 0 | `General` |
| `P97` | 0 | `General` |
| `P98` | 9.266530649957122 | `General` |
| `P99` | 9.266530649957122 | `General` |
| `P100` | 9.266530649957122 | `General` |

Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):

| Columna | Primera / última celda | N | Primer / último valor |
|---|---|---:|---|
| P | `P101` / `P3061` | 2961 | 9.266530649957122 / 9.266530649957122 |
| D | `D109` / `D159` | 6 | 0 / 0 |
| E | `E109` / `E159` | 6 | 1 / 1 |
| F | `F109` / `F159` | 6 | 2 / 2 |
| G | `G109` / `G159` | 6 | 3 / 3 |
| H | `H109` / `H159` | 6 | 4 / 4 |
| I | `I109` / `I159` | 6 | 5 / 5 |
| J | `J109` / `J159` | 6 | 6 / 6 |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `D11` | `D11` | 1 | `=1/12` | 0.08333333333333333 |
| `H11` | `H11` | 1 | `=EXP(tipo*deltat)*EXP(vola*SQRT(deltat))*(2/(EXP(vola*SQRT(deltat))+EXP(-vola*SQRT(deltat))))` | 1.0869300107425321 |
| `D12` | `D12` | 1 | `=6*deltat` | 0.5 |
| `H12` | `H12` | 1 | `=EXP(tipo*deltat)*EXP(-vola*SQRT(deltat))*(2/(EXP(vola*SQRT(deltat))+EXP(-vola*SQRT(deltat))))` | 0.9140702392991397 |
| `D20` | `D20` | 1 | `=S0` | 80 |
| `E20` | `J20` | 6 | `=D20*u` | 86.95440085940257 |
| `M20` | `M26` | 7 | `=BINOMDIST(L20,$L$20,p,FALSE)` | 0.015625000000000007 |
| `N20` | `N20` | 1 | `=SUMPRODUCT(M20:M26,J20:J26)/J32` | 80.00000000000004 |
| `P20` | `P26` | 7 | `=LN(J20/$D$20)` | 0.5001433111484215 |
| `R20` | `R20` | 1 | `=SUMPRODUCT(P20:P26,M20:M26)^2` | 0.00037915610162931847 |
| `E21` | `J26` | 21 | `=D20*d` | 73.12561914393117 |
| `R22` | `R22` | 1 | `=SUMPRODUCT(P20:P26^2,M20:M26)` | 0.04537915610162931 |
| `R24` | `R24` | 1 | `=R22-R20` | 0.04499999999999999 |
| `R26` | `R26` | 1 | `=SQRT(R24)/SQRT(T)` | 0.29999999999999993 |
| `R28` | `R28` | 1 | `=vola` | 0.3 |
| `E32` | `J32` | 6 | `=D32*EXP(tipo*deltat)` | 1.0005001250208359 |
| `E38` | `J38` | 6 | `=IF(RAND()<=p,1,-1)` | 1 |
| `E39` | `J39` | 6 | `=-(E38-1)/2` | 0 |
| `E40` | `J40` | 6 | `=SUM($E$39:E39)` | 0 |
| `D41` | `D41` | 1 | `=D20` | 80 |
| `E41` | `J41` | 6 | `=OFFSET(E20,E40,0)` | 86.95440085940257 |
| `I48` | `I48` | 1 | `=(LN(S0/strike)+(tipo+0.5*vola^2)*T)/(vola*SQRT(T))` | -0.10979088679435575 |
| `I49` | `I49` | 1 | `=(LN(S0/strike)+(tipo-0.5*vola^2)*T)/(vola*SQRT(T))` | -0.32192292115032 |
| `I50` | `I50` | 1 | `=S0*NORMSDIST(I48)-strike*EXP(-T*tipo)*NORMSDIST(I49)` | 5.201588299180152 |
| `P55` | `P55` | 1 | `=MAX(call_put*(J41-strike),0)` | 9.294371983025599 |
| `H56` | `H56` | 1 | `=SUMPRODUCT(F57:F63,E57:E63)*EXP(-tipo*T)` | 5.43610123490592 |
| `P56` | `P56` | 1 | `=P55*EXP(-tipo*T)` | 9.266530649957122 |
| `D57` | `D63` | 7 | `=J20` | 131.91660542163655 |
| `E57` | `E63` | 7 | `=M20` | 0.015625000000000007 |
| `F57` | `L92` | 8 | `=MAX(call_put*(D57-strike),0)` | 47.91660542163655 |
| `R60` | `R60` | 1 | `=COUNTA(O62:O3061)` | 3000 |
| `P61` | `P61` | 1 | `=P56` | 9.266530649957122 |
| `P62` | `P62` | 1 | `<DataTableFormula: {'ref': 'P62:P3061', 'ca': '1', 'dt2D': '0', 'dtr': '0', 'r1': 'N61', 'r2': None, 'del1': False, 'del2': False}>` | 9.266530649957122 |
| `R62` | `R62` | 1 | `=AVERAGE(P62:P3061)` | 5.274036021989797 |
| `D68` | `I73` | 21 | `=(E68*p+E69*(1-p))*EXP(-tipo*deltat)` | 5.4361012349059195 |
| `J68` | `J74` | 7 | `=MAX(call_put*(J20-strike),0)` | 47.91660542163655 |
| `D81` | `I86` | 21 | `=(E68-E69)/(E20-E21)` | 0.4556457377874805 |
| `D92` | `J92` | 7 | `=D41` | 80 |
| `D95` | `D95` | 1 | `=D81` | 0.4556457377874805 |
| `E95` | `I95` | 5 | `=OFFSET(E81,E40,0)` | 0.6113349462086431 |
| `D96` | `D96` | 1 | `=D98-D95*D92` | -31.015557788092522 |
| `E96` | `I96` | 5 | `=D96*EXP(tipo*deltat)-(E95-D95)*E92` | -44.56893128311438 |
| `D98` | `D98` | 1 | `=D68` | 5.4361012349059195 |
| `E98` | `I98` | 5 | `=E95*E92+E96` | 8.589332688873284 |
| `J98` | `J98` | 1 | `=I95*J92+I96*EXP(tipo*deltat)` | 9.294371983025599 |
| `E99` | `J99` | 6 | `=D95*E92+D96*EXP(deltat*tipo)` | 8.589332688873288 |
| `D104` | `D104` | 1 | `=call_put` | 1 |
| `D105` | `D105` | 1 | `=strike` | 84 |

### Notas de celdas

- `I50`: se trata de otro modelo (en realidad el límite de éste cuando Deltat->0), pero sirve de referencia

- `P61`: Genera una tabla de simulaciones con el procedimiento habitual  (está borrada para que no afecte al cállculo de la hoja)
- `I68`: el resto del árbol se rellena con la condición de martingala

- `J68`: a vencimiento registramos el payoff de la opción

- `J110`: a vencimiento registramos el payoff de la opción

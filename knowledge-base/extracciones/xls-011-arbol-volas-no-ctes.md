# XLS-011: Arbol volas no ctes.xlsm

Original: [archivo raw](../../raw/fundamentos/sesioniii/arbol-volas-no-ctes.xlsm). SHA-256: `c67f2ae7a57e11a2cdfacaa39b0badb70d25779c5ec397a6444b4737f32fc7c8`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **True**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `callput` | `Hoja1!$H$63` |
| `deltat` | `Hoja1!$E$4` |
| `factorVola` | `Hoja1!$H$19` |
| `nuevostiempos` | `Hoja1!$E$22:$K$22` |
| `pasovola` | `Hoja1!$E$19` |
| `S0` | `Hoja1!$E$13` |
| `strike` | `Hoja1!$F$63` |
| `T` | `Hoja1!$E$3` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B1:XFD99`. Celdas con contenido: 305. Fórmulas: 128. Familias: 28.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `XFD1` | . |
| `D2` | Número de pasos |
| `D3` | T |
| `D4` | Deltat |
| `O5` | Interpolación de tiempos |
| `D6` | Datos de mercado |
| `O7` | paso |
| `P7` | vars acums |
| `Q7` | plazos |
| `R7` | nuevas vars |
| `S7` | nuevos plazos |
| `D9` | instante j |
| `D10` | tiempo (años) |
| `D11` | tipos spot R(0,j) |
| `D12` | volatilidades spot sj |
| `D13` | cotización hoy S0 |
| `D16` | varianzas acumuladas |
| `O16` | Interpolación de tipos spot |
| `D17` | Varianza acumulada |
| `O17` | paso |
| `P17` | plazos |
| `Q17` | tipos spot |
| `R17` | nuevos plazos |
| `S17` | nuevos tipos |
| `D18` | paso de varianza A^2 |
| `D19` | paso de vola A |
| `G19` | factor(vola) |
| `D22` | tiempo (años) |
| `D23` | tipos spot R(0,j) |
| `D24` | descuentos |
| `D25` | descuentos forward |
| `D28` | Árbol de ruidos |
| `D41` | deriva por tipos |
| `D44` | ajustes de convexidad |
| `P45` | comprobación de volatilidad |
| `R46` | debería salir |
| `D47` | Árbol de valores del subyacente |
| `N47` | comprobación de martingala |
| `Q50` | media |
| `Q51` | media cudrados |
| `Q52` | varianza |
| `Q53` | desv típica |
| `B62` | Valoración de call/put europea |
| `F62` | strike |
| `G62` | vencimiento |
| `H62` | call=+1 put=-1 |
| `D65` | Árbol de valoración de la opción |
| `D76` | Árbol de deltas |
| `D86` | Simulación en el árbol |
| `D92` | senda valores subyacente |
| `M92` | flujo opción |
| `D93` | senda deltas |
| `D96` | Cartera de réplica |
| `D97` | subyacente (unidades) |
| `D98` | cash |
| `D99` | valor liquidativo cartera |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `E2` | 6 | `General` |
| `E3` | 0.5 | `General` |
| `O8` | 0 | `General` |
| `E9` | 0 | `General` |
| `F9` | 1 | `General` |
| `G9` | 2 | `General` |
| `H9` | 3 | `General` |
| `I9` | 4 | `General` |
| `J9` | 5 | `General` |
| `K9` | 6 | `General` |
| `O9` | 1 | `General` |
| `O10` | 2 | `General` |
| `F11` | 0.0064 | `0.000%` |
| `G11` | 0.0092 | `0.000%` |
| `H11` | 0.0121 | `0.000%` |
| `I11` | 0.0124 | `0.000%` |
| `J11` | 0.0129 | `0.000%` |
| `K11` | 0.0178 | `0.000%` |
| `O11` | 3 | `General` |
| `F12` | 0.27 | `0.00%` |
| `G12` | 0.29 | `0.00%` |
| `H12` | 0.34 | `0.00%` |
| `I12` | 0.35 | `0.00%` |
| `J12` | 0.36 | `0.00%` |
| `K12` | 0.365 | `0.00%` |
| `O12` | 4 | `General` |
| `E13` | 80 | `0` |
| `O13` | 5 | `General` |
| `O14` | 6 | `General` |
| `O18` | 0 | `General` |
| `O19` | 1 | `General` |
| `O20` | 2 | `General` |
| `E21` | 0 | `General` |
| `F21` | 1 | `General` |
| `G21` | 2 | `General` |
| `H21` | 3 | `General` |
| `I21` | 4 | `General` |
| `J21` | 5 | `General` |
| `K21` | 6 | `General` |
| `O21` | 3 | `General` |
| `O22` | 4 | `General` |
| `O23` | 5 | `General` |
| `O24` | 6 | `General` |
| `E29` | 0 | `General` |
| `F29` | 1 | `General` |
| `G29` | 2 | `General` |
| `H29` | 3 | `General` |
| `I29` | 4 | `General` |
| `J29` | 5 | `General` |
| `K29` | 6 | `General` |
| `E39` | 0 | `General` |
| `F39` | 1 | `General` |
| `G39` | 2 | `General` |
| `H39` | 3 | `General` |
| `I39` | 4 | `General` |
| `J39` | 5 | `General` |
| `K39` | 6 | `General` |
| `E48` | 0 | `General` |
| `F48` | 1 | `General` |
| `G48` | 2 | `General` |
| `H48` | 3 | `General` |
| `I48` | 4 | `General` |
| `J48` | 5 | `General` |
| `K48` | 6 | `General` |
| `F49` | 0 | `General` |
| `G49` | 0 | `General` |
| `H49` | 0 | `General` |
| `I49` | 0 | `General` |
| `J49` | 0 | `General` |
| `K49` | 0 | `General` |
| `L50` | 6 | `General` |
| `L51` | 5 | `General` |
| `L52` | 4 | `General` |
| `L53` | 3 | `General` |
| `L54` | 2 | `General` |
| `L55` | 1 | `General` |
| `L56` | 0 | `General` |
| `F63` | 84 | `General` |
| `H63` | 1 | `General` |
| `E66` | 0 | `General` |
| `F66` | 1 | `General` |
| `G66` | 2 | `General` |
| `H66` | 3 | `General` |
| `I66` | 4 | `General` |
| `J66` | 5 | `General` |
| `K66` | 6 | `General` |
| `F67` | 0 | `General` |
| `G67` | 0 | `General` |
| `H67` | 0 | `General` |
| `I67` | 0 | `General` |
| `J67` | 0 | `General` |
| `K67` | 0 | `General` |
| `E77` | 0 | `General` |
| `F77` | 1 | `General` |
| `G77` | 2 | `General` |
| `H77` | 3 | `General` |
| `I77` | 4 | `General` |
| `J77` | 5 | `General` |
| `K77` | 6 | `General` |
| `F78` | 0 | `General` |
| `G78` | 0 | `General` |
| `H78` | 0 | `General` |
| `I78` | 0 | `General` |
| `J78` | 0 | `General` |
| `K78` | 0 | `General` |
| `E87` | 0 | `General` |
| `F87` | 1 | `General` |
| `G87` | 2 | `General` |
| `H87` | 3 | `General` |
| `I87` | 4 | `General` |
| `J87` | 5 | `General` |
| `K87` | 6 | `General` |
| `F88` | 0 | `General` |
| `G88` | 0 | `General` |
| `H88` | 0 | `General` |
| `I88` | 0 | `General` |
| `J88` | 0 | `General` |
| `K88` | 0 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `E4` | `E4` | 1 | `=1/12` | 0.08333333333333333 |
| `E10` | `K10` | 7 | `=E9*deltat` | 0 |
| `R47` | `R47` | 1 | `=K12*SQRT(T)` | 0.25809397513308985 |
| `N48` | `N48` | 1 | `=SUMPRODUCT(K50:K56,M50:M56)*K24` | 0 |
| `E49` | `E88` | 4 | `=nuevostiempos` | 0 |
| `M50` | `M56` | 7 | `=BINOMDIST(L50,6,50%,FALSE)` | 0.015625000000000007 |
| `P50` | `P56` | 7 | `=LN(K50/S0)` | #NUM! |
| `R50` | `R50` | 1 | `=SUMPRODUCT(P50:P56,M50:M56)` | #NUM! |
| `R51` | `R51` | 1 | `=SUMPRODUCT(P50:P56^2,M50:M56)` | #NUM! |
| `R52` | `R52` | 1 | `=R51-R50^2` | #NUM! |
| `R53` | `R53` | 1 | `=SQRT(R52)` | #NUM! |
| `G63` | `G63` | 1 | `=T` | 0.5 |
| `E68` | `J73` | 21 | `=AVERAGE(F68:F69)*E$25` | 0 |
| `K68` | `K74` | 7 | `=MAX(callput*(K50-strike),0)` | 0 |
| `E79` | `J84` | 21 | `=(F68-F69)/(F50-F51)` | #DIV/0! |
| `F89` | `K89` | 6 | `=IF(RAND()<50%,1,-1)` | 1 |
| `F90` | `K90` | 6 | `=IF(F89=1,0,1)` | 0 |
| `F91` | `K91` | 6 | `=SUM($F$90:F90)` | 0 |
| `E92` | `E92` | 1 | `=S0` | 80 |
| `F92` | `K92` | 6 | `=OFFSET(F50,F91,0)` | 0 |
| `E93` | `E93` | 1 | `=E79` | #DIV/0! |
| `F93` | `J93` | 5 | `=OFFSET(F79,F91,0)` | #DIV/0! |
| `M93` | `M93` | 1 | `=MAX(callput*(K92-strike),0)` | 0 |
| `E97` | `J97` | 6 | `=E93` | #DIV/0! |
| `E98` | `E98` | 1 | `=E99-E97*E92` | #DIV/0! |
| `F98` | `J98` | 5 | `=E98/E25-(F97-E97)*F92` | #DIV/0! |
| `E99` | `E99` | 1 | `=E68` | 0 |
| `K99` | `K99` | 1 | `=J97*K92+J98/J25` | #DIV/0! |

### Notas de celdas

- `S9`: jcontreras: este código hace interpolación lineal

- `K10`: la escala original de tiempos

- `K22`: jcontreras: los nuevos instantes del árbol (acomodados a la estructura temporal de las volatilidades)

- `K41`: jcontreras: varias maneras de calcular la deriva (acumulada) por tipos 

- `E99`: jcontreras: valor inicial= prima de la opción

- `K99`: jcontreras: valor a mercado de la cartera cuando vence la opción


### Errores guardados

Se detectan 51 celdas de error. No se han corregido.

```json
[
  {
    "cell": "P50",
    "value": "#NUM!"
  },
  {
    "cell": "R50",
    "value": "#NUM!"
  },
  {
    "cell": "P51",
    "value": "#NUM!"
  },
  {
    "cell": "R51",
    "value": "#NUM!"
  },
  {
    "cell": "P52",
    "value": "#NUM!"
  },
  {
    "cell": "R52",
    "value": "#NUM!"
  },
  {
    "cell": "P53",
    "value": "#NUM!"
  },
  {
    "cell": "R53",
    "value": "#NUM!"
  },
  {
    "cell": "P54",
    "value": "#NUM!"
  },
  {
    "cell": "P55",
    "value": "#NUM!"
  },
  {
    "cell": "P56",
    "value": "#NUM!"
  },
  {
    "cell": "E79",
    "value": "#DIV/0!"
  },
  {
    "cell": "F79",
    "value": "#DIV/0!"
  },
  {
    "cell": "G79",
    "value": "#DIV/0!"
  },
  {
    "cell": "H79",
    "value": "#DIV/0!"
  },
  {
    "cell": "I79",
    "value": "#DIV/0!"
  },
  {
    "cell": "J79",
    "value": "#DIV/0!"
  },
  {
    "cell": "F80",
    "value": "#DIV/0!"
  },
  {
    "cell": "G80",
    "value": "#DIV/0!"
  },
  {
    "cell": "H80",
    "value": "#DIV/0!"
  },
  {
    "cell": "I80",
    "value": "#DIV/0!"
  },
  {
    "cell": "J80",
    "value": "#DIV/0!"
  },
  {
    "cell": "G81",
    "value": "#DIV/0!"
  },
  {
    "cell": "H81",
    "value": "#DIV/0!"
  },
  {
    "cell": "I81",
    "value": "#DIV/0!"
  },
  {
    "cell": "J81",
    "value": "#DIV/0!"
  },
  {
    "cell": "H82",
    "value": "#DIV/0!"
  },
  {
    "cell": "I82",
    "value": "#DIV/0!"
  },
  {
    "cell": "J82",
    "value": "#DIV/0!"
  },
  {
    "cell": "I83",
    "value": "#DIV/0!"
  },
  {
    "cell": "J83",
    "value": "#DIV/0!"
  },
  {
    "cell": "J84",
    "value": "#DIV/0!"
  },
  {
    "cell": "E93",
    "value": "#DIV/0!"
  },
  {
    "cell": "F93",
    "value": "#DIV/0!"
  },
  {
    "cell": "G93",
    "value": "#DIV/0!"
  },
  {
    "cell": "H93",
    "value": "#DIV/0!"
  },
  {
    "cell": "I93",
    "value": "#DIV/0!"
  },
  {
    "cell": "J93",
    "value": "#DIV/0!"
  },
  {
    "cell": "E97",
    "value": "#DIV/0!"
  },
  {
    "cell": "F97",
    "value": "#DIV/0!"
  },
  {
    "cell": "G97",
    "value": "#DIV/0!"
  },
  {
    "cell": "H97",
    "value": "#DIV/0!"
  },
  {
    "cell": "I97",
    "value": "#DIV/0!"
  },
  {
    "cell": "J97",
    "value": "#DIV/0!"
  },
  {
    "cell": "E98",
    "value": "#DIV/0!"
  },
  {
    "cell": "F98",
    "value": "#DIV/0!"
  },
  {
    "cell": "G98",
    "value": "#DIV/0!"
  },
  {
    "cell": "H98",
    "value": "#DIV/0!"
  },
  {
    "cell": "I98",
    "value": "#DIV/0!"
  },
  {
    "cell": "J98",
    "value": "#DIV/0!"
  },
  {
    "cell": "K99",
    "value": "#DIV/0!"
  }
]
```

## Hoja: Hoja2

Estado: `hidden`. Rango usado: `B2:S99`. Celdas con contenido: 499. Fórmulas: 266. Familias: 53.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `D2` | Número de pasos |
| `D3` | T |
| `D4` | Deltat |
| `O5` | Interpolación de tiempos |
| `D6` | Datos de mercado |
| `O7` | paso |
| `P7` | vars acums |
| `Q7` | plazos |
| `R7` | nuevas vars |
| `S7` | nuevos plazos |
| `D9` | instante j |
| `D10` | tiempo (años) |
| `D11` | tipos spot R(0,j) |
| `D12` | volatilidades spot sj |
| `D13` | cotización hoy S0 |
| `D16` | varianzas acumuladas |
| `O16` | Interpolación de tipos spot |
| `D17` | Varianza acumulada |
| `O17` | paso |
| `P17` | plazos |
| `Q17` | tipos spot |
| `R17` | nuevos plazos |
| `S17` | nuevos tipos |
| `D18` | paso de varianza A^2 |
| `D19` | paso de vola A |
| `G19` | factor(vola) |
| `D22` | tiempo (años) |
| `D23` | tipos spot R(0,j) |
| `D24` | descuentos |
| `D25` | descuentos forward |
| `D28` | Árbol de ruidos |
| `D41` | deriva por tipos |
| `D44` | ajustes de convexidad |
| `P45` | comprobación de volatilidad |
| `R46` | debería salir |
| `D47` | Árbol de valores del subyacente |
| `N47` | comprobación de martingala |
| `Q50` | media |
| `Q51` | media cudrados |
| `Q52` | varianza |
| `Q53` | desv típica |
| `B62` | Valoración de call/put europea |
| `F62` | strike |
| `G62` | vencimiento |
| `H62` | call=+1 put=-1 |
| `D65` | Árbol de valoración de la opción |
| `D76` | Árbol de deltas |
| `D86` | Simulación en el árbol |
| `D92` | senda valores subyacente |
| `M92` | flujo opción |
| `D93` | senda deltas |
| `D96` | Cartera de réplica |
| `D97` | subyacente (unidades) |
| `D98` | cash |
| `D99` | valor liquidativo cartera |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `E2` | 6 | `General` |
| `E3` | 0.5 | `General` |
| `O8` | 0 | `General` |
| `S8` | 0 | `0.0000` |
| `E9` | 0 | `General` |
| `F9` | 1 | `General` |
| `G9` | 2 | `General` |
| `H9` | 3 | `General` |
| `I9` | 4 | `General` |
| `J9` | 5 | `General` |
| `K9` | 6 | `General` |
| `O9` | 1 | `General` |
| `P9` | 0.0060750000000000005 | `0.000%` |
| `Q9` | 0.08333333333333333 | `0.0000` |
| `O10` | 2 | `General` |
| `P10` | 0.014016666666666665 | `0.000%` |
| `Q10` | 0.16666666666666666 | `0.0000` |
| `F11` | 0.0064 | `0.000%` |
| `G11` | 0.0092 | `0.000%` |
| `H11` | 0.0121 | `0.000%` |
| `I11` | 0.0124 | `0.000%` |
| `J11` | 0.0129 | `0.000%` |
| `K11` | 0.0178 | `0.000%` |
| `O11` | 3 | `General` |
| `P11` | 0.028900000000000006 | `0.000%` |
| `Q11` | 0.25 | `0.0000` |
| `F12` | 0.27 | `0.00%` |
| `G12` | 0.29 | `0.00%` |
| `H12` | 0.34 | `0.00%` |
| `I12` | 0.35 | `0.00%` |
| `J12` | 0.36 | `0.00%` |
| `K12` | 0.365 | `0.00%` |
| `O12` | 4 | `General` |
| `P12` | 0.040833333333333326 | `0.000%` |
| `Q12` | 0.3333333333333333 | `0.0000` |
| `E13` | 80 | `0` |
| `O13` | 5 | `General` |
| `P13` | 0.05399999999999999 | `0.000%` |
| `Q13` | 0.41666666666666663 | `0.0000` |
| `O14` | 6 | `General` |
| `P14` | 0.06661249999999999 | `0.000%` |
| `Q14` | 0.5 | `0.0000` |
| `E16` | 0 | `0%` |
| `O18` | 0 | `General` |
| `Q18` | 0 | `0.000%` |
| `S18` | 0 | `0.000%` |
| `O19` | 1 | `General` |
| `P19` | 0.08333333333333333 | `0.0000` |
| `R19` | 0.13608342077649527 | `0.0000` |
| `O20` | 2 | `General` |
| `P20` | 0.16666666666666666 | `0.0000` |
| `Q20` | 0.0092 | `0.000%` |
| `R20` | 0.21250933184023887 | `0.0000` |
| `E21` | 0 | `General` |
| `F21` | 1 | `General` |
| `G21` | 2 | `General` |
| `H21` | 3 | `General` |
| `I21` | 4 | `General` |
| `J21` | 5 | `General` |
| `K21` | 6 | `General` |
| `O21` | 3 | `General` |
| `P21` | 0.25 | `0.0000` |
| `Q21` | 0.0121 | `0.000%` |
| `R21` | 0.2807699022346369 | `0.0000` |
| `F22` | 0.13608342077649527 | `0.00000` |
| `G22` | 0.21250933184023887 | `0.00000` |
| `H22` | 0.2807699022346369 | `0.00000` |
| `I22` | 0.3559599156118144 | `0.00000` |
| `J22` | 0.42664629446096247 | `0.00000` |
| `K22` | 0.5000000000000001 | `0.00000` |
| `O22` | 4 | `General` |
| `P22` | 0.3333333333333333 | `0.0000` |
| `Q22` | 0.0124 | `0.000%` |
| `R22` | 0.3559599156118144 | `0.0000` |
| `F23` | 0.008172402938090241 | `0.000%` |
| `G23` | 0.010795324748040312 | `0.000%` |
| `H23` | 0.012210771648044693 | `0.000%` |
| `I23` | 0.012535759493670886 | `0.000%` |
| `J23` | 0.013486802114304596 | `0.000%` |
| `K23` | 0.017800000000000007 | `0.000%` |
| `O23` | 5 | `General` |
| `P23` | 0.41666666666666663 | `0.0000` |
| `Q23` | 0.0129 | `0.000%` |
| `R23` | 0.42664629446096247 | `0.0000` |
| `O24` | 6 | `General` |
| `P24` | 0.5 | `0.0000` |
| `Q24` | 0.0178 | `0.000%` |
| `R24` | 0.5000000000000001 | `0.0000` |
| `E29` | 0 | `General` |
| `F29` | 1 | `General` |
| `G29` | 2 | `General` |
| `H29` | 3 | `General` |
| `I29` | 4 | `General` |
| `J29` | 5 | `General` |
| `K29` | 6 | `General` |
| `F30` | 0.13608342077649527 | `General` |
| `G30` | 0.21250933184023887 | `General` |
| `H30` | 0.2807699022346369 | `General` |
| `I30` | 0.3559599156118144 | `General` |
| `J30` | 0.42664629446096247 | `General` |
| `K30` | 0.5000000000000001 | `General` |
| `E31` | 0 | `General` |
| `E39` | 0 | `General` |
| `F39` | 1 | `General` |
| `G39` | 2 | `General` |
| `H39` | 3 | `General` |
| `I39` | 4 | `General` |
| `J39` | 5 | `General` |
| `K39` | 6 | `General` |
| `F40` | 0.13608342077649527 | `General` |
| `G40` | 0.21250933184023887 | `General` |
| `H40` | 0.2807699022346369 | `General` |
| `I40` | 0.3559599156118144 | `General` |
| `J40` | 0.42664629446096247 | `General` |
| `K40` | 0.5000000000000001 | `General` |
| `E41` | 1 | `0%` |
| `E45` | 1 | `0%` |
| `E48` | 0 | `General` |
| `F48` | 1 | `General` |
| `G48` | 2 | `General` |
| `H48` | 3 | `General` |
| `I48` | 4 | `General` |
| `J48` | 5 | `General` |
| `K48` | 6 | `General` |
| `F49` | 0.13608342077649527 | `General` |
| `G49` | 0.21250933184023887 | `General` |
| `H49` | 0.2807699022346369 | `General` |
| `I49` | 0.3559599156118144 | `General` |
| `J49` | 0.42664629446096247 | `General` |
| `K49` | 0.5000000000000001 | `General` |
| `L50` | 6 | `General` |
| `L51` | 5 | `General` |
| `L52` | 4 | `General` |
| `L53` | 3 | `General` |
| `L54` | 2 | `General` |
| `L55` | 1 | `General` |
| `L56` | 0 | `General` |
| `F63` | 84 | `General` |
| `H63` | 1 | `General` |
| `E66` | 0 | `General` |
| `F66` | 1 | `General` |
| `G66` | 2 | `General` |
| `H66` | 3 | `General` |
| `I66` | 4 | `General` |
| `J66` | 5 | `General` |
| `K66` | 6 | `General` |
| `F67` | 0.13608342077649527 | `General` |
| `G67` | 0.21250933184023887 | `General` |
| `H67` | 0.2807699022346369 | `General` |
| `I67` | 0.3559599156118144 | `General` |
| `J67` | 0.42664629446096247 | `General` |
| `K67` | 0.5000000000000001 | `General` |
| `E77` | 0 | `General` |
| `F77` | 1 | `General` |
| `G77` | 2 | `General` |
| `H77` | 3 | `General` |
| `I77` | 4 | `General` |
| `J77` | 5 | `General` |
| `K77` | 6 | `General` |
| `F78` | 0.13608342077649527 | `General` |
| `G78` | 0.21250933184023887 | `General` |
| `H78` | 0.2807699022346369 | `General` |
| `I78` | 0.3559599156118144 | `General` |
| `J78` | 0.42664629446096247 | `General` |
| `K78` | 0.5000000000000001 | `General` |
| `E87` | 0 | `General` |
| `F87` | 1 | `General` |
| `G87` | 2 | `General` |
| `H87` | 3 | `General` |
| `I87` | 4 | `General` |
| `J87` | 5 | `General` |
| `K87` | 6 | `General` |
| `F88` | 0.13608342077649527 | `General` |
| `G88` | 0.21250933184023887 | `General` |
| `H88` | 0.2807699022346369 | `General` |
| `I88` | 0.3559599156118144 | `General` |
| `J88` | 0.42664629446096247 | `General` |
| `K88` | 0.5000000000000001 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `E4` | `E4` | 1 | `=1/12` | 0.08333333333333333 |
| `P8` | `P8` | 1 | `=TRANSPOSE(E16:K16)` | 0 |
| `Q8` | `Q8` | 1 | `=TRANSPOSE(E10:K10)` | 0 |
| `R8` | `R14` | 7 | `=O8*pasovola^2` | 0 |
| `S9` | `S14` | 6 | `=InterPola(R9,$P$8:$Q$14,1)` | 0.13608342077649527 |
| `E10` | `K10` | 7 | `=E9*deltat` | 0 |
| `F16` | `K16` | 6 | `=F10*F12^2` | 0.0060750000000000005 |
| `E17` | `E17` | 1 | `=K16` | 0.06661249999999999 |
| `E18` | `E18` | 1 | `=E17/E2` | 0.011102083333333332 |
| `P18` | `P18` | 1 | `=TRANSPOSE(E10:K10)` | 0 |
| `R18` | `R18` | 1 | `=S8:S14` | 0 |
| `E19` | `R53` | 2 | `=SQRT(E18)` | 0.1053664241271067 |
| `H19` | `H19` | 1 | `=2/(EXP(pasovola)+EXP(-pasovola))` | 0.9944745213051771 |
| `I19` | `I19` | 1 | `=1/COSH(pasovola)` | 0.9944745213051771 |
| `Q19` | `Q19` | 1 | `=TRANSPOSE(F11:K11)` | 0.0064 |
| `S19` | `S24` | 6 | `=InterPola(R19,$P$18:$Q$24,1)` | 0.008172402938090241 |
| `E22` | `E22` | 1 | `=TRANSPOSE(S8:S14)` | 0 |
| `E23` | `E23` | 1 | `=TRANSPOSE(S18:S24)` | 0 |
| `E24` | `K24` | 7 | `=EXP(-E23*E22)` | 1 |
| `E25` | `J25` | 6 | `=F24/E24` | 0.9988884896379856 |
| `E30` | `E88` | 6 | `=nuevostiempos` | 0 |
| `F31` | `K31` | 6 | `=E31+pasovola` | 0.1053664241271067 |
| `F32` | `K37` | 21 | `=E31-pasovola` | -0.1053664241271067 |
| `F41` | `K41` | 6 | `=EXP(F23*F22)` | 1.0011127471920487 |
| `F42` | `K42` | 6 | `=1/PRODUCT($E$25:E25)` | 1.0011127471920487 |
| `F43` | `K43` | 6 | `=1/F24` | 1.0011127471920487 |
| `E44` | `K44` | 7 | `=factorVola^E39` | 1 |
| `F45` | `K45` | 6 | `=E45*factorVola` | 0.9944745213051771 |
| `R47` | `R47` | 1 | `=K12*SQRT(T)` | 0.25809397513308985 |
| `N48` | `N48` | 1 | `=SUMPRODUCT(K50:K56,M50:M56)*K24` | 79.99999999999996 |
| `E50` | `K56` | 28 | `=S0*E$41*E$44*EXP(E31)` | 80 |
| `M50` | `M56` | 7 | `=BINOMDIST(L50,6,50%,FALSE)` | 0.015625000000000007 |
| `P50` | `P56` | 7 | `=LN(K50/S0)` | 0.6078537410490292 |
| `R50` | `R50` | 1 | `=SUMPRODUCT(P50:P56,M50:M56)` | -0.02434480371361106 |
| `R51` | `R51` | 1 | `=SUMPRODUCT(P50:P56^2,M50:M56)` | 0.06720516946785428 |
| `R52` | `R52` | 1 | `=R51-R50^2` | 0.06661250000000003 |
| `G63` | `G63` | 1 | `=T` | 0.5 |
| `E68` | `J73` | 21 | `=AVERAGE(F68:F69)*E$25` | 7.10528808168346 |
| `K68` | `K74` | 7 | `=MAX(callput*(K50-strike),0)` | 62.91884738354187 |
| `E79` | `J84` | 21 | `=(F68-F69)/(F50-F51)` | 0.48845539562559775 |
| `F89` | `K89` | 6 | `=IF(RAND()<50%,1,-1)` | 1 |
| `F90` | `K90` | 6 | `=IF(F89=1,0,1)` | 0 |
| `F91` | `K91` | 6 | `=SUM($F$90:F90)` | 0 |
| `E92` | `E92` | 1 | `=S0` | 80 |
| `F92` | `K92` | 6 | `=OFFSET(F50,F91,0)` | 88.49662243681469 |
| `E93` | `E93` | 1 | `=E79` | 0.48845539562559775 |
| `F93` | `J93` | 5 | `=OFFSET(F79,F91,0)` | 0.6431994407222366 |
| `M93` | `M93` | 1 | `=MAX(callput*(K92-strike),0)` | 35.00286012287346 |
| `E97` | `J97` | 6 | `=E93` | 0.48845539562559775 |
| `E98` | `E98` | 1 | `=E99-E97*E92` | -31.97114356836436 |
| `F98` | `J98` | 5 | `=E98/E25-(F97-E97)*F92` | -45.70104470185931 |
| `E99` | `E99` | 1 | `=E68` | 7.10528808168346 |
| `K99` | `K99` | 1 | `=J97*K92+J98/J25` | 35.002860122873415 |

### Notas de celdas

- `S9`: jcontreras: este código hace interpolación lineal

- `K10`: la escala original de tiempos

- `K22`: jcontreras: los nuevos instantes del árbol (acomodados a la estructura temporal de las volatilidades)

- `K41`: jcontreras: varias maneras de calcular la deriva (acumulada) por tipos 

- `E99`: jcontreras: valor inicial= prima de la opción

- `K99`: jcontreras: valor a mercado de la cartera cuando vence la opción

## Código VBA recuperado

Código fuente leído estáticamente del contenedor VBA. No se ha ejecutado. Los módulos de interfaz sin procedimientos no añaden lógica de cálculo.

### Módulo ThisWorkbook

```vb
Attribute VB_Name = "ThisWorkbook"
Attribute VB_Base = "0{00020819-0000-0000-C000-000000000046}"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Attribute VB_TemplateDerived = False
Attribute VB_Customizable = True

```

### Módulo Hoja1

```vb
Attribute VB_Name = "Hoja1"
Attribute VB_Base = "0{00020820-0000-0000-C000-000000000046}"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Attribute VB_TemplateDerived = False
Attribute VB_Customizable = True

```

### Módulo Módulo1

```vb
Attribute VB_Name = "Módulo1"

Option Explicit

Function InterPola(ByVal Fecha As Variant, _
ByRef Curva As Variant, Optional ByVal modo As Integer) As Variant
    Dim a As Integer, b As Integer, N As Integer, m As Integer
    
    If IsMissing(modo) Then
        m = 0
    Else
        m = modo
    End If
      
    a = 1
    b = Curva.Rows.Count
    N = Int((a + b) / 2)
      
    While b - a > 1
        If Curva(N, 1) >= Fecha Then b = N
        If Curva(N, 1) < Fecha Then a = N
        N = Int((a + b) / 2)
    Wend
    
    Select Case modo
        Case 0
            InterPola = Exp(Log(Curva(a, 2)) + (Log(Curva(b, 2)) _
            - Log(Curva(a, 2))) * ((Fecha - Curva(a, 1)) _
            / (Curva(b, 1) - Curva(a, 1))))
        Case 1
            InterPola = Curva(a, 2) + (Curva(b, 2) - Curva(a, 2)) * (Fecha - Curva(a, 1)) / (Curva(b, 1) - Curva(a, 1))
    End Select
    
End Function




```

### Módulo Hoja2

```vb
Attribute VB_Name = "Hoja2"
Attribute VB_Base = "0{00020820-0000-0000-C000-000000000046}"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Attribute VB_TemplateDerived = False
Attribute VB_Customizable = True

```

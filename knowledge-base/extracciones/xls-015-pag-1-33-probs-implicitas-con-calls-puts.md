# XLS-015: pag 1.33 probs implicitas con calls-puts.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-33-probs-implicitas-con-calls-puts.xlsx). SHA-256: `686eb1dfadeee79240602605587a899c6727cbc6e570e46cc41fdb3777dd7341`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `spot` | `Hoja1!$C$6` |
| `T` | `Hoja1!$C$5` |
| `tipo` | `Hoja1!$C$4` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `A3:U115`. Celdas con contenido: 1500. Fórmulas: 1318. Familias: 23.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `B3` | Datos |
| `B4` | tipo  |
| `B5` | vencimiento |
| `B6` | spot |
| `B7` | Fecha valoracion |
| `B8` | Fecha vencimiento |
| `B10` | strikeATM |
| `T13` | comparación de probs implícitas |
| `C15` | K |
| `D15` | vola |
| `J15` | precios |
| `Q15` | probs |
| `T15` | con volas de mercado |
| `U15` | con vola ATM |
| `F16` | moneyness |
| `G16` | vola acum |
| `H16` | phi(d+) |
| `I16` | phi(d-) |
| `J16` | call |
| `K16` | fwd |
| `L16` | put |
| `B17` | PUT |
| `B18` | PUT |
| `B19` | PUT |
| `B20` | PUT |
| `B21` | PUT |
| `B22` | PUT |
| `B23` | PUT |
| `B24` | PUT |
| `B25` | PUT |
| `B26` | PUT |
| `B27` | PUT |
| `B28` | PUT |
| `B29` | PUT |
| `B30` | PUT |
| `B31` | PUT |
| `B32` | PUT |
| `B33` | PUT |
| `B34` | PUT |
| `B35` | PUT |
| `B36` | PUT |
| `B37` | PUT |
| `B38` | PUT |
| `B39` | PUT |
| `A40` | ATM |
| `B40` | PUT |
| `B41` | PUT |
| `B42` | PUT |
| `B43` | PUT |
| `B44` | CALL |
| `B45` | CALL |
| `B46` | CALL |
| `B47` | CALL |
| `B48` | CALL |
| `B49` | CALL |
| `B50` | CALL |
| `B51` | CALL |
| `B52` | CALL |
| `B53` | CALL |
| `B54` | CALL |
| `B55` | CALL |
| `B56` | CALL |
| `B57` | CALL |
| `B58` | CALL |
| `B59` | CALL |
| `B60` | CALL |
| `B61` | CALL |
| `B62` | CALL |
| `B63` | CALL |
| `C67` | K |
| `D67` | vola |
| `J67` | precios |
| `Q67` | probs |
| `F68` | moneyness |
| `G68` | vola acum |
| `H68` | phi(d+) |
| `I68` | phi(d-) |
| `J68` | call |
| `K68` | fwd |
| `L68` | put |
| `B69` | PUT |
| `B70` | PUT |
| `B71` | PUT |
| `B72` | PUT |
| `B73` | PUT |
| `B74` | PUT |
| `B75` | PUT |
| `B76` | PUT |
| `B77` | PUT |
| `B78` | PUT |
| `B79` | PUT |
| `B80` | PUT |
| `B81` | PUT |
| `B82` | PUT |
| `B83` | PUT |
| `B84` | PUT |
| `B85` | PUT |
| `B86` | PUT |
| `B87` | PUT |
| `B88` | PUT |
| `B89` | PUT |
| `B90` | PUT |
| `B91` | PUT |
| `B92` | PUT |
| `B93` | PUT |
| `B94` | PUT |
| `B95` | PUT |
| `B96` | CALL |
| `B97` | CALL |
| `B98` | CALL |
| `B99` | CALL |
| `B100` | CALL |
| `B101` | CALL |
| `B102` | CALL |
| `B103` | CALL |
| `B104` | CALL |
| `B105` | CALL |
| `B106` | CALL |
| `B107` | CALL |
| `B108` | CALL |
| `B109` | CALL |
| `B110` | CALL |
| `B111` | CALL |
| `B112` | CALL |
| `B113` | CALL |
| `B114` | CALL |
| `B115` | CALL |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `C4` | 0.0032 | `0.00%` |
| `C6` | 10500 | `General` |
| `C7` | 2020-01-24T00:00:00 | `mm-dd-yy` |
| `C8` | 2020-02-15T00:00:00 | `mm-dd-yy` |
| `C16` | 0 | `General` |
| `C17` | 8200 | `#,##0` |
| `D17` | 0.5008 | `0.00%` |
| `D18` | 0.49563333333333337 | `0.00%` |
| `D19` | 0.4904666666666667 | `0.00%` |
| `D20` | 0.4853 | `0.00%` |
| `D21` | 0.48013333333333336 | `0.00%` |
| `D22` | 0.4749666666666667 | `0.00%` |
| `D23` | 0.46980000000000005 | `0.00%` |
| `D24` | 0.4646333333333334 | `0.00%` |
| `D25` | 0.45946666666666675 | `0.00%` |
| `D26` | 0.4543000000000001 | `0.00%` |
| `D27` | 0.44913333333333344 | `0.00%` |
| `D28` | 0.4439666666666668 | `0.00%` |
| `D29` | 0.43880000000000013 | `0.00%` |
| `D30` | 0.4336333333333335 | `0.00%` |
| `D31` | 0.42846666666666683 | `0.00%` |
| `D32` | 0.4233 | `0.00%` |
| `D33` | 0.4181 | `0.00%` |
| `D34` | 0.41295000000000004 | `0.00%` |
| `D35` | 0.4078 | `0.00%` |
| `D36` | 0.40259999999999996 | `0.00%` |
| `D37` | 0.3974 | `0.00%` |
| `D38` | 0.3923 | `0.00%` |
| `D39` | 0.3871 | `0.00%` |
| `C40` | 10500 | `#,##0` |
| `D40` | 0.3818 | `0.00%` |
| `D41` | 0.3764 | `0.00%` |
| `D42` | 0.371 | `0.00%` |
| `D43` | 0.3655 | `0.00%` |
| `D44` | 0.3601 | `0.00%` |
| `D45` | 0.3547 | `0.00%` |
| `D46` | 0.3492 | `0.00%` |
| `D47` | 0.3438 | `0.00%` |
| `D48` | 0.3383 | `0.00%` |
| `D49` | 0.3329 | `0.00%` |
| `D50` | 0.3275 | `0.00%` |
| `D51` | 0.322 | `0.00%` |
| `D52` | 0.3166 | `0.00%` |
| `D53` | 0.3112 | `0.00%` |
| `D54` | 0.3057 | `0.00%` |
| `D55` | 0.3 | `0.00%` |
| `D56` | 0.2948 | `0.00%` |
| `D57` | 0.2894 | `0.00%` |
| `D58` | 0.284 | `0.00%` |
| `D59` | 0.2785 | `0.00%` |
| `D60` | 0.2731 | `0.00%` |
| `D61` | 0.2677 | `0.00%` |
| `D62` | 0.26225 | `0.00%` |
| `D63` | 0.2568 | `0.00%` |
| `C68` | 0 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `C5` | `C5` | 1 | `=(C8-C7)/365` | 0.06027397260273973 |
| `C10` | `C10` | 1 | `=spot*EXP(tipo*T)` | 10502.025400799497 |
| `Q16` | `Q68` | 2 | `=SUM(Q17:Q63)` | 1.0000000000000064 |
| `F17` | `F115` | 94 | `=LN(spot/(C17*EXP(-tipo*T)))` | 0.2474339796055991 |
| `G17` | `G115` | 94 | `=D17*SQRT(T)` | 0.12295019684453372 |
| `H17` | `H115` | 94 | `=NORMSDIST(F17/G17+0.5*G17)` | 0.9809579449479666 |
| `I17` | `I115` | 94 | `=NORMSDIST(F17/G17-0.5*G17)` | 0.9744713658952059 |
| `J17` | `J115` | 94 | `=spot*H17-C17*EXP(-tipo*T)*I17` | 2310.934286223609 |
| `K17` | `K115` | 94 | `=spot-C17*EXP(-tipo*T)` | 2301.5814365250553 |
| `L17` | `L115` | 94 | `=J17-K17` | 9.352849698553655 |
| `N17` | `N69` | 2 | `=L18-L17` | 2.1246604455272973 |
| `O17` | `O115` | 94 | `=N17/100` | 0.021246604455272974 |
| `P17` | `P115` | 4 | `=O17` | 0.021246604455272974 |
| `Q17` | `Q115` | 94 | `=P17*EXP(tipo*T)` | 0.02125070282571586 |
| `S17` | `S63` | 47 | `=C17` | 8200 |
| `T17` | `T63` | 47 | `=Q17` | 0.02125070282571586 |
| `U17` | `U63` | 47 | `=Q69` | 0.005763393367043012 |
| `C18` | `C39` | 22 | `=C19-100` | 8300 |
| `N18` | `N115` | 92 | `=J17-J18` | 97.8560537431922 |
| `P18` | `P114` | 90 | `=O18-O19` | 0.004254821481390558 |
| `C41` | `C63` | 23 | `=C40+100` | 10600 |
| `C69` | `C115` | 47 | `=C17` | 8200 |
| `D69` | `D115` | 47 | `=$D$40` | 0.3818 |

### Notas de celdas

- `N17`: El primero es especial. La diferencia de las dos primeras puts nos da la probabilidad de la cola de la izquierda

- `O17`: esta división por 100 es porque la diferencia entre strikes consecutivos es justamente 100

- `D18`: los datos en negro "parecen" haber sido rellenados linealmente

- `N18`: para el resto, usamos calls (se puede hacer con todo puts)

- `P18`: observa que son "segundas" diferencias de precios de calls, para obtener butterflies. En clase escribimos este código como cartera con pesos 1, -2 y 1, de las 3 calls involucradas

- `C40`: el strike más cercano al ATM

- `D40`: vola ATM


### Gráficos y rangos de origen

```json
[
  {
    "type": "LineChart",
    "title": "",
    "series": [
      {
        "val": "Hoja1!$T$17:$T$63",
        "cat": "Hoja1!$S$17:$S$63"
      },
      {
        "val": "Hoja1!$U$17:$U$63",
        "cat": "Hoja1!$S$17:$S$63"
      }
    ]
  }
]
```

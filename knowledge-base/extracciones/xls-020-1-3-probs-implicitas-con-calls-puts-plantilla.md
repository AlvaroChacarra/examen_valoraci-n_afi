# XLS-020: 1.3.probs implicitas con calls-puts_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity/1-3-probs-implicitas-con-calls-puts-plantilla.xlsx). SHA-256: `5dc045a9ec10fe400e7d09af28e99668015c9ff1a6ba714a6b4f66cfb57f599c`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `spot` | `Hoja1!$C$13` |
| `T` | `Hoja1!$C$12` |
| `tipo` | `Hoja1!$C$11` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `A10:U122`. Celdas con contenido: 329. Fórmulas: 143. Familias: 7.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `B10` | Datos |
| `B11` | tipo  |
| `B12` | vencimiento |
| `B13` | spot |
| `B14` | Fecha valoracion |
| `B15` | Fecha vencimiento |
| `B17` | strikeATM |
| `T20` | comparación de probs implícitas |
| `C22` | K |
| `D22` | vola |
| `J22` | precios |
| `Q22` | probs |
| `T22` | con volas de mercado |
| `U22` | con vola ATM |
| `F23` | moneyness |
| `G23` | vola acum |
| `H23` | phi(d+) |
| `I23` | phi(d-) |
| `J23` | call |
| `K23` | fwd |
| `L23` | put |
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
| `B40` | PUT |
| `B41` | PUT |
| `B42` | PUT |
| `B43` | PUT |
| `B44` | PUT |
| `B45` | PUT |
| `B46` | PUT |
| `A47` | ATM |
| `B47` | PUT |
| `B48` | PUT |
| `B49` | PUT |
| `B50` | PUT |
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
| `B64` | CALL |
| `B65` | CALL |
| `B66` | CALL |
| `B67` | CALL |
| `B68` | CALL |
| `B69` | CALL |
| `B70` | CALL |
| `C74` | K |
| `D74` | vola |
| `J74` | precios |
| `Q74` | probs |
| `F75` | moneyness |
| `G75` | vola acum |
| `H75` | phi(d+) |
| `I75` | phi(d-) |
| `J75` | call |
| `K75` | fwd |
| `L75` | put |
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
| `B96` | PUT |
| `B97` | PUT |
| `B98` | PUT |
| `B99` | PUT |
| `B100` | PUT |
| `B101` | PUT |
| `B102` | PUT |
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
| `B116` | CALL |
| `B117` | CALL |
| `B118` | CALL |
| `B119` | CALL |
| `B120` | CALL |
| `B121` | CALL |
| `B122` | CALL |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `C11` | 0.0032 | `0.00%` |
| `C13` | 10500 | `General` |
| `C14` | 2020-01-24T00:00:00 | `mm-dd-yy` |
| `C15` | 2020-02-15T00:00:00 | `mm-dd-yy` |
| `C23` | 0 | `General` |
| `C24` | 8200 | `#,##0` |
| `D24` | 0.5008 | `0.00%` |
| `D25` | 0.49563333333333337 | `0.00%` |
| `D26` | 0.4904666666666667 | `0.00%` |
| `D27` | 0.4853 | `0.00%` |
| `D28` | 0.48013333333333336 | `0.00%` |
| `D29` | 0.4749666666666667 | `0.00%` |
| `D30` | 0.46980000000000005 | `0.00%` |
| `D31` | 0.4646333333333334 | `0.00%` |
| `D32` | 0.45946666666666675 | `0.00%` |
| `D33` | 0.4543000000000001 | `0.00%` |
| `D34` | 0.44913333333333344 | `0.00%` |
| `D35` | 0.4439666666666668 | `0.00%` |
| `D36` | 0.43880000000000013 | `0.00%` |
| `D37` | 0.4336333333333335 | `0.00%` |
| `D38` | 0.42846666666666683 | `0.00%` |
| `D39` | 0.4233 | `0.00%` |
| `D40` | 0.4181 | `0.00%` |
| `D41` | 0.41295000000000004 | `0.00%` |
| `D42` | 0.4078 | `0.00%` |
| `D43` | 0.40259999999999996 | `0.00%` |
| `D44` | 0.3974 | `0.00%` |
| `D45` | 0.3923 | `0.00%` |
| `D46` | 0.3871 | `0.00%` |
| `C47` | 10500 | `#,##0` |
| `D47` | 0.3818 | `0.00%` |
| `D48` | 0.3764 | `0.00%` |
| `D49` | 0.371 | `0.00%` |
| `D50` | 0.3655 | `0.00%` |
| `D51` | 0.3601 | `0.00%` |
| `D52` | 0.3547 | `0.00%` |
| `D53` | 0.3492 | `0.00%` |
| `D54` | 0.3438 | `0.00%` |
| `D55` | 0.3383 | `0.00%` |
| `D56` | 0.3329 | `0.00%` |
| `D57` | 0.3275 | `0.00%` |
| `D58` | 0.322 | `0.00%` |
| `D59` | 0.3166 | `0.00%` |
| `D60` | 0.3112 | `0.00%` |
| `D61` | 0.3057 | `0.00%` |
| `D62` | 0.3 | `0.00%` |
| `D63` | 0.2948 | `0.00%` |
| `D64` | 0.2894 | `0.00%` |
| `D65` | 0.284 | `0.00%` |
| `D66` | 0.2785 | `0.00%` |
| `D67` | 0.2731 | `0.00%` |
| `D68` | 0.2677 | `0.00%` |
| `D69` | 0.26225 | `0.00%` |
| `D70` | 0.2568 | `0.00%` |
| `C75` | 0 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `C12` | `C12` | 1 | `=(C15-C14)/365` | 0.06027397260273973 |
| `C17` | `C17` | 1 | `=spot*EXP(tipo*T)` | 10502.025400799497 |
| `Q23` | `Q75` | 2 | `=SUM(Q24:Q70)` | 0 |
| `C25` | `C46` | 22 | `=C26-100` | 8300 |
| `C48` | `C70` | 23 | `=C47+100` | 10600 |
| `C76` | `C122` | 47 | `=C24` | 8200 |
| `D76` | `D122` | 47 | `=$D$47` | 0.3818 |

### Notas de celdas

- `N24`: El primero es especial. La diferencia de las dos primeras puts nos da la probabilidad de la cola de la izquierda

- `O24`: esta división por 100 es porque la diferencia entre strikes consecutivos es justamente 100

- `D25`: los datos en negro "parecen" haber sido rellenados linealmente

- `N25`: para el resto, usamos calls (se puede hacer con todo puts)

- `P25`: observa que son "segundas" diferencias de precios de calls, para obtener butterflies. En clase escribimos este código como cartera con pesos 1, -2 y 1, de las 3 calls involucradas

- `C47`: el strike más cercano al ATM

- `D47`: vola ATM

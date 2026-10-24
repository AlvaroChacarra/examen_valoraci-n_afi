# XLS-030: cap_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos/cap-plantilla.xlsx). SHA-256: `a1ef8a26d68ff79d43e8042e0ca27874191d612091fd35e8e9d5779574f80068`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `deltat` | `Hoja1!$E$3` |
| `K` | `Hoja1!$M$4` |
| `nom` | `Hoja1!$M$3` |
| `vola` | `Hoja1!$E$23` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `D3:Q23`. Celdas con contenido: 71. Fórmulas: 23. Familias: 2.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `D3` | deltat |
| `J3` | cap semestral a 5 años |
| `L3` | nom |
| `L4` | K |
| `D6` | plazo |
| `E6` | FD |
| `G6` | tipos fwd |
| `K7` | moneyness |
| `L7` | vola acum |
| `M7` | dmas |
| `N7` | dmenos |
| `O7` | phi(dmas) |
| `P7` | phi(dmenos) |
| `Q7` | primas |
| `I8` | pago de tiempo |
| `I9` | pago (caplet) de tiempo |
| `I10` | pago (caplet) de tiempo |
| `I11` | pago (caplet) de tiempo |
| `I12` | pago (caplet) de tiempo |
| `I13` | pago (caplet) de tiempo |
| `I14` | pago (caplet) de tiempo |
| `I15` | pago (caplet) de tiempo |
| `I16` | pago (caplet) de tiempo |
| `I17` | pago (caplet) de tiempo |
| `P20` | prima cap |
| `D23` | vola  |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `E3` | 0.5 | `General` |
| `M3` | 1000 | `_-* #,##0.00\ "€"_-;\-* #,##0.00\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `M4` | 0.008 | `0.0%` |
| `D7` | 0 | `General` |
| `E7` | 1 | `0.000%` |
| `E8` | 0.9956 | `0.000%` |
| `J8` | 0.5 | `General` |
| `E9` | 0.99283 | `0.000%` |
| `E10` | 0.98786 | `0.000%` |
| `E11` | 0.98145 | `0.000%` |
| `E12` | 0.97456 | `0.000%` |
| `E13` | 0.96845 | `0.000%` |
| `E14` | 0.95951 | `0.000%` |
| `E15` | 0.95231 | `0.000%` |
| `E16` | 0.94393 | `0.000%` |
| `E17` | 0.93543 | `0.000%` |
| `E18` | 0.9292 | `0.000%` |
| `E19` | 0.91952 | `0.000%` |
| `E20` | 0.90984 | `0.000%` |
| `E21` | 0.89834 | `0.000%` |
| `E23` | 0.35 | `0%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `D8` | `D21` | 14 | `=D7+deltat` | 0.5 |
| `J9` | `J17` | 9 | `=D9` | 1 |

### Notas de celdas

- `Q8`: habitualmente este primer pago (fijo y conocido) no se considera dentro del cap, que solo constaría de los 9 caplets siguientes. Puedes quitarlo.

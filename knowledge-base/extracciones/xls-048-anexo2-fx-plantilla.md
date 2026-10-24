# XLS-048: Anexo2.FX_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/anexos-valoracion/anexo2-fx-plantilla.xlsx). SHA-256: `da08a5bd39f6e3586fdcba40a6113a23e5cc83cb39ee8dccac01e073871b8564`.

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

Estado: `visible`. Rango usado: `A5:Y952`. Celdas con contenido: 55. Fórmulas: 4. Familias: 4.

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
| `D13` | 0.005 | `0.0%` |
| `D14` | 0.015 | `0.00%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `E13` | `E13` | 1 | `=1/(1+tipoe*T)` | 0.9950248756218907 |
| `E14` | `E14` | 1 | `=1/(1+tipod*T)` | 0.9852216748768474 |
| `D15` | `D15` | 1 | `=FX0*(1+tipoe)/(1+tipod)` | 0.7921182266009852 |
| `E15` | `E15` | 1 | `=FX0*E14/E13` | 0.7921182266009853 |

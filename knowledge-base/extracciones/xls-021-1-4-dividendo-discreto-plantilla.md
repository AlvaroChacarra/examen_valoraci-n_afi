# XLS-021: 1.4.dividendo discreto_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity/1-4-dividendo-discreto-plantilla.xlsx). SHA-256: `d4e1ecfabb94a52f8c846c09c25af428df1207d9c940e5e5515e36b638dcbd39`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `divid` | `condicionando!$G$12` |
| `flujos` | `#REF!` |
| `K` | `condicionando!$G$11` |
| `paso` | `#REF!` |
| `plazo1` | `condicionando!$E$7` |
| `plazo2` | `condicionando!$F$7` |
| `probs` | `#REF!` |
| `q` | `condicionando!$J$6` |
| `sigma` | `condicionando!$G$14` |
| `spot` | `condicionando!$G$13` |
| `tipo` | `condicionando!$D$3` |

## Hoja: condicionando

Estado: `visible`. Rango usado: `C2:T267`. Celdas con contenido: 44. Fórmulas: 5. Familias: 5.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C3` | tipo |
| `E6` | T |
| `F6` | T' |
| `C7` | tiempo |
| `C8` | Descuentos |
| `C9` | desc fwd |
| `C11` | Strike |
| `C12` | Dividendo (se paga en tiempo 1) |
| `C13` | Spot |
| `C14` | Sigma |
| `C19` | Cálculo numérico de la integral doble |
| `K20` | para cada escenario (condicionando a él), calculamos la prima de la call |
| `E21` | estos son escenarios del subyacente en tiempo 1 |
| `C23` | paso |
| `O23` | precio call |
| `S23` | precio call sin dividendos |
| `E24` | valores normal |
| `F24` | probs |
| `G24` | S_plazo1 |
| `I24` | S ex-dividendo |
| `K24` | moneyness |
| `L24` | vola acumulada |
| `M24` | valor (en T) de la call (que paga en T') |
| `S25` | moneyness |
| `S26` | vola acum |
| `S27` | d+ |
| `S28` | d- |
| `S29` | Phi(d+) |
| `S30` | Phi(d-) |
| `S31` | precio |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D3` | 0.01 | `0%` |
| `D7` | 0 | `General` |
| `E7` | 1 | `General` |
| `F7` | 2 | `General` |
| `D8` | 1 | `0.000%` |
| `G11` | 120 | `_-* #,##0.00\ "€"_-;\-* #,##0.00\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `G12` | 5 | `General` |
| `G13` | 100 | `_-* #,##0.00\ "€"_-;\-* #,##0.00\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `G14` | 0.3 | `0%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `E8` | `E8` | 1 | `=EXP(-plazo1*tipo)` | 0.9900498337491681 |
| `F8` | `F8` | 1 | `=EXP(-plazo2*tipo)` | 0.9801986733067553 |
| `F9` | `F9` | 1 | `=F8/E8` | 0.990049833749168 |
| `C24` | `C24` | 1 | `=0.1` | 0.1 |
| `O24` | `O24` | 1 | `=SUMPRODUCT(F26:F126,M26:M126)*$E$8` | 0 |

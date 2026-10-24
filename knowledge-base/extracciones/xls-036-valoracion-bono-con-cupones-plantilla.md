# XLS-036: valoración bono con cupones_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos/valoracion-bono-con-cupones-plantilla.xlsx). SHA-256: `f9f42b88a61386ba611d79dbfc6f5d71e786cf9fd11cb4c79f4bc435508b92af`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `A0` | `Hoja1!$D$11` |
| `corte1` | `Hoja1!$G$12` |
| `corte2` | `Hoja1!$G$13` |
| `deltat` | `Hoja1!$D$4` |
| `Fswap0` | `Hoja1!$D$12` |
| `pago1` | `Hoja1!$H$12` |
| `pago3` | `Hoja1!$H$14` |
| `vola` | `Hoja1!$D$14` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B4:AJ126`. Celdas con contenido: 86. Fórmulas: 3. Familias: 3.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C4` | deltat |
| `Y5` | volas |
| `B7` | descuentos |
| `T7` | Versión con smile |
| `W7` | fwd-swap0 |
| `C9` | tipo swap a 5 años que se fijará dentro de 5 años |
| `AB9` | con fórmulas |
| `C11` | anualidad |
| `G11` | cortes |
| `H11` | pagos |
| `W11` | valor |
| `AB11` | pago fijo |
| `C12` | tipo fwd-swap0 |
| `AD12` | moneyness |
| `AE12` | vola acum |
| `AF12` | dmas |
| `AG12` | dmenos |
| `AH12` | phi(dmas) |
| `AI12` | phi(dmenos) |
| `AJ12` | prima |
| `W13` | promedio |
| `Y13` | promedio |
| `C14` | vola |
| `G14` | más de 8% |
| `W14` | prima |
| `Y14` | prima |
| `T16` | valores normal |
| `U16` | probs |
| `W16` | valores de SwapT (6%) |
| `X16` | flujo |
| `Y16` | valores de SwapT (8%) |
| `Z16` | flujo |
| `AD16` | valor |
| `C21` | Valoración por integración |
| `H21` | valor por integración |
| `L21` | Valoración por desestructuración (con fórmulas BS) |
| `L23` | El instrumento equivale a  |
| `C24` | valores normal |
| `D24` | probs |
| `E24` | valores de SwapT |
| `F24` | flujo |
| `H24` | flujo promedio |
| `L24` | instrumento 1 |
| `L25` | instrumento 2 |
| `L26` | instrumento 3 |
| `J29` | moneyness |
| `K29` | vola acum |
| `L29` | dmas |
| `M29` | dmenos |
| `N29` | phi(dmas) |
| `O29` | phi(dmenos) |
| `N34` | valor por desestructuración |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D4` | 1 | `General` |
| `C6` | 1 | `General` |
| `D6` | 2 | `General` |
| `E6` | 3 | `General` |
| `F6` | 4 | `General` |
| `G6` | 5 | `General` |
| `H6` | 6 | `General` |
| `I6` | 7 | `General` |
| `J6` | 8 | `General` |
| `K6` | 9 | `General` |
| `L6` | 10 | `General` |
| `X6` | 0.06 | `0%` |
| `Y6` | 0.26 | `0%` |
| `C7` | 0.99456 | `0.000%` |
| `D7` | 0.9912 | `0.000%` |
| `E7` | 0.98434 | `0.000%` |
| `F7` | 0.9625 | `0.000%` |
| `G7` | 0.94312 | `0.000%` |
| `H7` | 0.92245 | `0.000%` |
| `I7` | 0.90455 | `0.000%` |
| `J7` | 0.85674 | `0.000%` |
| `K7` | 0.79987 | `0.000%` |
| `L7` | 0.73491 | `0.000%` |
| `Y7` | 0.25 | `0%` |
| `X8` | 0.08 | `0%` |
| `Y8` | 0.24 | `0%` |
| `G12` | 0.06 | `0%` |
| `H12` | 0.03 | `0%` |
| `G13` | 0.08 | `0%` |
| `D14` | 0.25 | `0%` |
| `H14` | 0.09 | `0%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `X7` | `X7` | 1 | `=Fswap0` | 0.049356172306875404 |
| `D11` | `D11` | 1 | `=SUM(H7:L7)*deltat` | 4.21852 |
| `D12` | `D12` | 1 | `=(G7-L7)/D11` | 0.049356172306875404 |

# XLS-046: Anexo1.-cotizador-volas-mueve-strikes_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/anexos-valoracion/anexo1-cotizador-volas-mueve-strikes-plantilla.xlsx). SHA-256: `85f7c3ee144c98fccdcf452e9393ea10a76de9f836d3abbddb6b0232f4c1452e`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `desc` | `Hoja1!$D$8` |
| `DT` | `Hoja1!$D$7` |
| `F0` | `Hoja1!$D$5` |
| `Nom` | `Hoja1!$D$3` |
| `T` | `Hoja1!$D$6` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `C3:AJ29`. Celdas con contenido: 75. Fórmulas: 14. Familias: 1.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C3` | Nom |
| `C5` | F0 |
| `C6` | T |
| `C7` | deltat |
| `C8` | desc T+DT |
| `C11` | precios de mercado |
| `F11` | shift=3% |
| `P11` | shift=0% |
| `AF12` | factor de escala entre volas |
| `C13` | precios |
| `D13` | strike |
| `F13` | moneyness |
| `G13` | vola acum |
| `H13` | d+ |
| `I13` | d- |
| `J13` | Phi(d+) |
| `K13` | Phi(d-) |
| `L13` | precio |
| `M13` | error |
| `N13` | volas |
| `P13` | moneyness |
| `Q13` | vola acum |
| `R13` | d+ |
| `S13` | d- |
| `T13` | Phi(d+) |
| `U13` | Phi(d-) |
| `V13` | precio |
| `W13` | error |
| `X13` | volas |
| `Z13` | d |
| `AA13` | Phi(d) |
| `AB13` | phi(d) |
| `AC13` | precio |
| `AD13` | error |
| `AE13` | volas normales |
| `AH13` | deltas shifted |
| `AI13` | deltas normales |
| `AJ13` | variación relativa |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D3` | 10000 | `_-* #,##0.00\ "€"_-;\-* #,##0.00\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `D5` | 0.004 | `0.00%` |
| `D6` | 1 | `General` |
| `D7` | 0.5 | `General` |
| `D8` | 0.997 | `0.00%` |
| `N10` | 0.03 | `0%` |
| `X10` | 0 | `0%` |
| `C14` | 49.923 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `D14` | -0.006 | `0.00%` |
| `C15` | 39.958 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C16` | 30.062 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C17` | 20.261 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C18` | 11.672 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C19` | 3.38 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C20` | 1.424 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C21` | 0.537 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C22` | 0.233 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C23` | 0.535 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C24` | 0.696 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C25` | 1.385 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C26` | 1.106 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C27` | 0.723 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C28` | 1.161 | `_-* #,##0.000\ "€"_-;\-* #,##0.000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `D15` | `D28` | 14 | `=D14+0.2%` | -0.004 |

# XLS-033: fra-caplet-floorlet+in arrears_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos/fra-caplet-floorlet-in-arrears-plantilla.xlsx). SHA-256: `020c1ad696ae1f90f2f52db14643c883ad23935dde36e40df7d29a254d3b8b40`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `deltat` | `Hoja1!$D$8` |
| `descuento1` | `Hoja1!$G$3` |
| `descuento2` | `Hoja1!$G$4` |
| `fwd0` | `Hoja1!$G$6` |
| `K` | `Hoja1!$D$4` |
| `nom` | `Hoja1!$D$3` |
| `plazo1` | `Hoja1!$D$6` |
| `plazo2` | `Hoja1!$D$7` |
| `vola` | `Hoja1!$D$5` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `C2:N36`. Celdas con contenido: 47. Fórmulas: 1. Familias: 1.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C2` | Datos |
| `F2` | descuentos |
| `C3` | nominal |
| `F3` | P(0,T) |
| `C4` | strike |
| `F4` | P(0,T') |
| `C5` | volatilidad |
| `C6` | T |
| `F6` | tipo fwd(0) |
| `C7` | T' |
| `C8` | deltat |
| `C11` | moneyness |
| `E11` | dmas |
| `G11` | phi(dmas) |
| `C12` | vola acum |
| `E12` | dmenos |
| `G12` | phi(dmenos) |
| `C15` | Cálculo de primas |
| `E15` | caplet |
| `F15` | floorlet |
| `G15` | fra |
| `C22` | Versiones in arrears |
| `I23` | fwd corregido |
| `L23` | aproximación del fwd corregido |
| `C24` | FRA in arrears |
| `F24` | usando aproximación |
| `C25` | fwd corregido |
| `C26` | prima FRA in arrears |
| `C27` | diferencia con FRA usual |
| `C28` | diferencia porcentual |
| `C30` | Caplet in arrears |
| `C31` | d* |
| `E31` | phi(d*) |
| `C32` | caplet |
| `C33` | corrección in arrears |
| `C34` | caplet in arrears |
| `C35` | diferencia con caplet usual |
| `C36` | diferencia porcentual |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D3` | 100000 | `_-* #,##0.00\ "€"_-;\-* #,##0.00\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `G3` | 0.9983 | `0.000%` |
| `D4` | 0.004 | `0.00%` |
| `G4` | 0.9976 | `0.000%` |
| `D5` | 0.3 | `0%` |
| `D6` | 0.75 | `General` |
| `D7` | 1 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `D8` | `D8` | 1 | `=D7-D6` | 0.25 |

### Notas de celdas

- `F18`: usando paridad call-put

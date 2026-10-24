# XLS-031: caplet- floorlet_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos/caplet-floorlet-plantilla.xlsx). SHA-256: `599d8f020184eb60307550e02853703e07b6011c162a1f9a0b94935b2b0fa01d`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `deltat` | `Ejercicio!$D$10` |
| `descuento1` | `Ejercicio!$G$5` |
| `descuento2` | `Ejercicio!$G$6` |
| `fwd0` | `Ejercicio!$G$8` |
| `K` | `Ejercicio!$D$6` |
| `nom` | `Ejercicio!$D$5` |
| `plazo1` | `Ejercicio!$D$8` |
| `plazo2` | `Ejercicio!$D$9` |
| `vola` | `Ejercicio!$D$7` |

## Hoja: Ejercicio

Estado: `visible`. Rango usado: `C4:I20`. Celdas con contenido: 29. Fórmulas: 1. Familias: 1.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C4` | Datos |
| `F4` | Descuentos |
| `C5` | nominal |
| `F5` | P(0,T) |
| `C6` | strike |
| `F6` | P(0,T') |
| `C7` | volatilidad |
| `C8` | T |
| `F8` | tipo fwd(0) |
| `C9` | T' |
| `C10` | deltat |
| `C13` | moneyness |
| `E13` | dmas |
| `G13` | phi(dmas) |
| `C14` | vola acum |
| `E14` | dmenos |
| `G14` | phi(dmenos) |
| `C17` | Cálculo de primas |
| `E17` | caplet |
| `F17` | floorlet |
| `G17` | fra |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D5` | 100000 | `_-* #,##0.00\ "€"_-;\-* #,##0.00\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `G5` | 0.998 | `0.000%` |
| `D6` | 0.0023 | `0.00000%` |
| `G6` | 0.997 | `0.000%` |
| `D7` | 0.3 | `0%` |
| `D8` | 0.75 | `General` |
| `D9` | 1 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `D10` | `D10` | 1 | `=D9-D8` | 0.25 |

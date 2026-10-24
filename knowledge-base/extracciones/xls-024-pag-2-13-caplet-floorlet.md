# XLS-024: pag 2.13 caplet- floorlet.xlsx

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-13-caplet-floorlet.xlsx). SHA-256: `44329975d04bee365353f5678074b112d6a6bb75e550f6d67d9f6c4ab125ce87`.

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

Estado: `visible`. Rango usado: `C4:I20`. Celdas con contenido: 40. Fórmulas: 12. Familias: 11.

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
| `G8` | `G8` | 1 | `=(descuento1/descuento2-1)/deltat` | 0.004012036108324679 |
| `D10` | `D10` | 1 | `=D9-D8` | 0.25 |
| `D13` | `D13` | 1 | `=LN(fwd0/K)` | 0.5563897472050116 |
| `F13` | `F13` | 1 | `=D13/D14+0.5*D14` | 2.2714489460554077 |
| `H13` | `H14` | 2 | `=NORMSDIST(F13)` | 0.9884400928703331 |
| `D14` | `D14` | 1 | `=vola*SQRT(plazo1)` | 0.25980762113533157 |
| `F14` | `F14` | 1 | `=D13/D14-0.5*D14` | 2.0116413249200757 |
| `E19` | `E19` | 1 | `=deltat*descuento2*(fwd0*H13-K*H14)*nom` | 42.78510265167909 |
| `F19` | `F19` | 1 | `=deltat*descuento2*(-fwd0*(1-H13)+K*(1-H14))*nom` | 0.11260265168644856 |
| `G19` | `G19` | 1 | `=descuento2*deltat*(fwd0-K)*nom` | 42.67249999999263 |
| `F20` | `F20` | 1 | `=E19-G19` | 0.11260265168645844 |

# XLS-022: 1.5.opcion sobre dos activos_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity/1-5-opcion-sobre-dos-activos-plantilla.xlsx). SHA-256: `902566e3d6aa5147908223310d7be36a443b20c01e3bf8350d2b278dc64706c2`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `correla` | `Hoja1!$D$27` |
| `K` | `Hoja1!$H$34` |
| `paso` | `Hoja1!$P$41` |
| `T` | `Hoja1!$F$32` |
| `tipo` | `Hoja1!$D$21` |
| `volagorro` | `Hoja1!$AJ$22` |
| `volaX` | `Hoja1!$D$24` |
| `volaY` | `Hoja1!$F$24` |
| `X0` | `Hoja1!$D$23` |
| `Y0` | `Hoja1!$F$23` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B1:BN2056`. Celdas con contenido: 2254. Fórmulas: 200. Familias: 2.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `AA12` | 4. Tabla de primas en función de correlación |
| `AB14` | correlación |
| `AC14` | prima |
| `C20` | Datos |
| `C21` | tipo |
| `C24` | volaX |
| `E24` | volaY |
| `C27` | correla |
| `C29` | Datos del contrato a) |
| `F30` | vencimiento T |
| `C31` | paga  |
| `B39` | 1a) Cálculo de la prima por simulación (numerario = cuenta bancaria) |
| `O39` | 2. Cálculo de la prima por integración numérica doble (numerario = cuenta bancaria)) |
| `Y39` | valor por integración |
| `I41` | valor por simulación |
| `O41` | paso |
| `P42` | valores de NX |
| `B43` | media |
| `O43` | probs |
| `B44` | desv típica |
| `N44` | valores de NY |
| `C46` | normales indeps |
| `E46` | normales correladas |
| `G46` | valores subyacentes |
| `C47` | normal1 |
| `D47` | normal2 |
| `E47` | N1 |
| `F47` | N2 |
| `G47` | XT |
| `H47` | YT |
| `I47` | payoff derivado |
| `Y98` | los valores y probs de |
| `O99` | El payoff es |
| `Q99` | donde X e Y  |
| `Y99` | las normales N_X y N_Y |
| `Q100` | son variables aleatorias |
| `Y100` | están registradas en la  |
| `Q101` | dadas por |
| `Y101` | tabla de arriba |
| `O106` | valores integrando |
| `C23` | X0 |
| `E23` | Y0 |
| `B48 … B2047` | sim1 … sim2000 (2000 etiquetas consecutivas, compactadas) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D21` | 0.01 | `0%` |
| `D23` | 25 | `General` |
| `F23` | 20 | `General` |
| `D24` | 0.15 | `0%` |
| `F24` | 0.3 | `0%` |
| `D27` | -0.2 | `0%` |
| `F32` | 1 | `General` |
| `P41` | 0.2 | `General` |
| `P43` | -5 | `General` |
| `O44` | -5 | `General` |

Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):

| Columna | Primera / última celda | N | Primer / último valor |
|---|---|---:|---|
| P | `P106` / `P106` | 1 | -5 / -5 |
| O | `O107` / `O107` | 1 | -5 / -5 |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `Q43` | `BN106` | 100 | `=P43+paso` | -4.8 |
| `O45` | `O157` | 100 | `=O44+paso` | -4.8 |

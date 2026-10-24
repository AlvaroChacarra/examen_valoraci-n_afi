# XLS-025: pag 2.17 fra-caplet-floorlet+in arrears.xlsx

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-17-fra-caplet-floorlet-in-arrears.xlsx). SHA-256: `18d1cedf06b69564040888aba3e8c315c4bd2c139fd2b85316e620e9140996e4`.

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

Estado: `visible`. Rango usado: `C2:N36`. Celdas con contenido: 71. Fórmulas: 26. Familias: 23.

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
| `G6` | `G6` | 1 | `=(descuento1/descuento2-1)/deltat` | 0.00280673616680005 |
| `D8` | `D8` | 1 | `=D7-D6` | 0.25 |
| `D11` | `D11` | 1 | `=LN(fwd0/K)` | -0.35427205932251843 |
| `F11` | `F11` | 1 | `=D11/D12+0.5*D12` | -1.2336899815404616 |
| `H11` | `F31` | 3 | `=NORMSDIST(F11)` | 0.10865922425738267 |
| `D12` | `D12` | 1 | `=vola*SQRT(plazo1)` | 0.25980762113533157 |
| `F12` | `F12` | 1 | `=D11/D12-0.5*D12` | -1.4934976026757931 |
| `E17` | `E17` | 1 | `=deltat*descuento2*(fwd0*H11-K*H12)*nom` | 0.8570334697247602 |
| `F17` | `F17` | 1 | `=deltat*descuento2*(-fwd0*(1-H11)+K*(1-H12))*nom` | 30.617033469731524 |
| `G17` | `G17` | 1 | `=descuento2*deltat*(fwd0-K)*nom` | -29.76000000000675 |
| `F18` | `F18` | 1 | `=E17-G17` | 30.617033469731513 |
| `G18` | `G18` | 1 | `=E17-F17` | -29.760000000006762 |
| `D25` | `D25` | 1 | `=fwd0*(1+deltat*fwd0*EXP(vola^2*plazo1))/(1+deltat*fwd0)` | 0.002806873597012016 |
| `F25` | `F25` | 1 | `=fwd0*(1+(deltat*fwd0*vola^2*plazo1)/(1+deltat*fwd0))` | 0.0028068690109189333 |
| `D26` | `F26` | 2 | `=deltat*descuento1*(D25-K)*nom` | -29.777452202572615 |
| `D27` | `D27` | 1 | `=D26-G17` | -0.017452202565863217 |
| `D28` | `D28` | 1 | `=D27/G17` | 0.0005864315378312923 |
| `D31` | `D31` | 1 | `=D11/D12+1.5*D12` | -0.97388236040513 |
| `D32` | `D32` | 1 | `=E17` | 0.8570334697247602 |
| `D33` | `D33` | 1 | `=descuento2*deltat^2*(fwd0^2*EXP(vola^2*plazo1)*F31-K*fwd0*H11)*nom` | 0.001067261144938515 |
| `D34` | `D34` | 1 | `=D32+D33` | 0.8581007308696987 |
| `D35` | `D35` | 1 | `=D34-E17` | 0.0010672611449384917 |
| `D36` | `D36` | 1 | `=D35/E17` | 0.0012452969255462647 |

### Notas de celdas

- `F18`: usando paridad call-put

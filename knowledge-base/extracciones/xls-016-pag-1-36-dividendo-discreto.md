# XLS-016: pag 1.36 dividendo discreto.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-36-dividendo-discreto.xlsx). SHA-256: `a27abc2d42472406fd2c63abd4176990011e3c6126db0b271ea511ec6e40be4a`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `divid` | `condicionando!$G$12` |
| `flujos` | `'integral doble'!$D$68:$BB$118` |
| `K` | `condicionando!$G$11` |
| `paso` | `'integral doble'!$D$10` |
| `plazo1` | `condicionando!$E$7` |
| `plazo2` | `condicionando!$F$7` |
| `probs` | `'integral doble'!$D$14:$BB$64` |
| `q` | `condicionando!$J$6` |
| `sigma` | `condicionando!$G$14` |
| `spot` | `condicionando!$G$13` |
| `tipo` | `condicionando!$D$3` |

## Hoja: condicionando

Estado: `visible`. Rango usado: `C2:T267`. Celdas con contenido: 758. Fórmulas: 718. Familias: 18.

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
| `E26` | 5 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `E8` | `E8` | 1 | `=EXP(-plazo1*tipo)` | 0.9900498337491681 |
| `F8` | `F8` | 1 | `=EXP(-plazo2*tipo)` | 0.9801986733067553 |
| `F9` | `F9` | 1 | `=F8/E8` | 0.990049833749168 |
| `C24` | `C24` | 1 | `=0.1` | 0.1 |
| `O24` | `O24` | 1 | `=SUMPRODUCT(F26:F126,M26:M126)*$E$8` | 9.132827318334984 |
| `T25` | `T25` | 1 | `=LN(spot/(EXP(-tipo*plazo2)*K))` | -0.16232155679395452 |
| `F26` | `F126` | 101 | `=NORMDIST(E26,0,1,FALSE)*0.1` | 1.4867195147342977e-07 |
| `G26` | `G126` | 101 | `=spot*EXP(sigma*SQRT(plazo1)*E26)*EXP(tipo*plazo1-(sigma^2/2)*plazo1)` | 432.7543240300773 |
| `I26` | `I126` | 101 | `=IF(G26>divid,G26-divid,G26)` | 427.7543240300773 |
| `K26` | `K126` | 101 | `=LN(I26/(K*$F$9))` | 1.2810572787178365 |
| `L26` | `L126` | 101 | `=sigma*SQRT(plazo2-plazo1)` | 0.3 |
| `M26` | `M126` | 101 | `=(NORMSDIST(K26/L26+L26/2)-EXP(-K26)*NORMSDIST(K26/L26-L26/2))*I26` | 308.94848360869975 |
| `T26` | `T26` | 1 | `=sigma*SQRT(plazo2)` | 0.4242640687119285 |
| `E27` | `E126` | 100 | `=E26-$C$24` | 4.9 |
| `T27` | `T27` | 1 | `=T25/T26+0.5*T26` | -0.17046354411657758 |
| `T28` | `T28` | 1 | `=T25/T26-0.5*T26` | -0.5947276128285061 |
| `T29` | `T30` | 2 | `=NORMSDIST(T27)` | 0.4323228011523794 |
| `T31` | `T31` | 1 | `=spot*T29-K*EXP(-tipo*plazo2)*T30` | 10.766596758515703 |

## Hoja: integral doble

Estado: `visible`. Rango usado: `C3:BB118`. Celdas con contenido: 5412. Fórmulas: 5407. Familias: 10.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `D4` | valor call |
| `C10` | paso |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D10` | 0.2 | `General` |
| `D13` | -5 | `General` |
| `D67` | -5 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `E3` | `E3` | 1 | `=SUMPRODUCT(probs,flujos)` | 9.307376473621225 |
| `E4` | `E4` | 1 | `=E3*condicionando!F8` | 9.123078071410031 |
| `E13` | `BB13` | 50 | `=D13+paso` | -4.8 |
| `C14` | `C68` | 2 | `=-5` | -5 |
| `D14` | `BB64` | 2601 | `=EXP(-0.5*(D$13^2+$C14^2))/(2*PI())*paso^2` | 8.841339661967145e-14 |
| `C15` | `C64` | 50 | `=C14+paso` | -4.8 |
| `C66` | `C66` | 1 | `=MAX((spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)-IF(spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)>=divid,divid,spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)))*EXP(sigma*SQRT(plazo2-plazo1)*D$67+(tipo-0.5*sigma^2)*(plazo2-plazo1))-K,0)` | 0 |
| `E67` | `BB67` | 50 | `=D67+0.2` | -4.8 |
| `D68` | `BB118` | 2601 | `=MAX((spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)-IF(spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)>=divid,divid,0.000001))*EXP(sigma*SQRT(plazo2-plazo1)*D$67+(tipo-0.5*sigma^2)*(plazo2-plazo1))-K,0)` | 0 |
| `C69` | `C118` | 50 | `=C68+0.2` | -4.8 |

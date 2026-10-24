# XLS-013: pag 1.27 call-cobertura discreta.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-27-call-cobertura-discreta.xlsx). SHA-256: `8143b57842ac1ee831d672a06a56ec3f6f196ab953375943bfb6475af48ed253`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `deltat` | `Ejercicio!$G$28` |
| `div` | `Ejercicio!#REF!` |
| `K` | `Ejercicio!$D$12` |
| `numsims` | `Ejercicio!$O$60` |
| `pasohist` | `Ejercicio!$O$65` |
| `S0` | `Ejercicio!$D$14` |
| `sigma` | `Ejercicio!$D$15` |
| `sims` | `Ejercicio!$D$59:$D$4961` |
| `T` | `Ejercicio!$D$11` |
| `tipo` | `Ejercicio!$D$13` |

## Hoja: Ejercicio

Estado: `visible`. Rango usado: `A1:AF4961`. Celdas con contenido: 10372. Fórmulas: 402. Familias: 39.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C10` | Datos |
| `F10` | Cálculos intermedios |
| `C11` | T |
| `F11` | moneyness |
| `C12` | K |
| `F12` | vola acumulada |
| `C13` | tipo |
| `F13` | d+ |
| `C14` | S0 |
| `F14` | d- |
| `C15` | sigma |
| `F15` | Phi(d+) |
| `F16` | Phi(d-) |
| `C19` | Primas |
| `D19` | prima |
| `E19` | prima/S0 |
| `C20` | call |
| `C21` | put |
| `C22` | fwd |
| `C28` | cobertura discreta de la call |
| `F28` | deltat |
| `B31` | Subyacente |
| `C32` | instante |
| `C33` | tiempo |
| `C34` | sorteos normal |
| `C35` | evolución subyacente |
| `B37` | Deltas |
| `C38` | S |
| `C39` | tiempo a venc |
| `C40` | d+ |
| `C41` | senda de deltas |
| `B43` | Cartera replicante |
| `C44` | instante |
| `C45` | unidades de suby |
| `C46` | cash |
| `C47` | valor cartera |
| `B49` | Resumen del resultado de la simulación |
| `C50` | pago call |
| `C51` | valor cartera replicante |
| `C52` | descasamiento |
| `C57` | tabla de simulaciones |
| `N58` | histograma |
| `N60` | numsims |
| `N62` | media |
| `Q62` | percentil 5% |
| `N63` | max |
| `N64` | min |
| `N65` | pasohist |
| `O67` | clases |
| `Q67` | frecs relativas |
| `C59 … C4961` | sim1 … sim4903 (4903 etiquetas consecutivas, compactadas) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D11` | 0.5 | `General` |
| `D12` | 40 | `General` |
| `D13` | 0.01 | `0.00%` |
| `D14` | 42 | `General` |
| `D15` | 0.2 | `0.00%` |
| `D32` | 0 | `General` |
| `E32` | 1 | `General` |
| `F32` | 2 | `General` |
| `G32` | 3 | `General` |
| `H32` | 4 | `General` |
| `I32` | 5 | `General` |
| `J32` | 6 | `General` |
| `K32` | 7 | `General` |
| `L32` | 8 | `General` |
| `M32` | 9 | `General` |
| `N32` | 10 | `General` |
| `O32` | 11 | `General` |
| `P32` | 12 | `General` |
| `Q32` | 13 | `General` |
| `R32` | 14 | `General` |
| `S32` | 15 | `General` |
| `T32` | 16 | `General` |
| `U32` | 17 | `General` |
| `V32` | 18 | `General` |
| `W32` | 19 | `General` |
| `X32` | 20 | `General` |
| `Y32` | 21 | `General` |
| `Z32` | 22 | `General` |
| `AA32` | 23 | `General` |
| `AB32` | 24 | `General` |
| `AC32` | 25 | `General` |
| `D60` | -0.08038956010153697 | `General` |
| `D61` | -0.22175214702449533 | `General` |
| `D62` | 0.14464161138079135 | `General` |
| `D63` | 0.8053188497641415 | `General` |
| `D64` | 0.28700602936618935 | `General` |
| `D65` | 0.17353960284960013 | `General` |
| `O65` | 0.1 | `General` |
| `D66` | 0.3369719342843389 | `General` |
| `D67` | 0.6687724043030308 | `General` |
| `D68` | 0.3597010726458194 | `General` |
| `N68` | 0 | `General` |
| `O68` | -2 | `0.0` |
| `R68` | 0 | `0%` |
| `D69` | 0.5237914703355528 | `General` |
| `N69` | 1 | `General` |
| `R69` | 0 | `0%` |
| `D70` | 0.29691748085842234 | `General` |
| `N70` | 2 | `General` |
| `R70` | 0 | `0%` |
| `D71` | 0.17023598328163025 | `General` |
| `N71` | 3 | `General` |
| `R71` | 0 | `0%` |
| `D72` | -0.15294014195518457 | `General` |
| `N72` | 4 | `General` |
| `R72` | 0 | `0%` |
| `D73` | -0.26772524745340576 | `General` |
| `N73` | 5 | `General` |
| `R73` | 0 | `0%` |
| `D74` | 0.2171538022003645 | `General` |
| `N74` | 6 | `General` |
| `R74` | 0 | `0%` |
| `D75` | -0.03937977070079768 | `General` |
| `N75` | 7 | `General` |
| `R75` | 0 | `0%` |
| `D76` | 0.12396383271384037 | `General` |
| `N76` | 8 | `General` |
| `R76` | 0 | `0%` |
| `D77` | -0.40618534679398977 | `General` |
| `N77` | 9 | `General` |
| `R77` | 0 | `0%` |
| `D78` | -0.1375569836400743 | `General` |
| `N78` | 10 | `General` |
| `R78` | 0 | `0%` |
| `D79` | 0.16021741600536643 | `General` |
| `N79` | 11 | `General` |
| `R79` | 0 | `0%` |
| `D80` | -0.1203464671992941 | `General` |
| `N80` | 12 | `General` |
| `R80` | 0 | `0%` |
| `D81` | -0.11512482906794475 | `General` |
| `N81` | 13 | `General` |
| `R81` | 0 | `0%` |
| `D82` | -0.03515716781523537 | `General` |
| `N82` | 14 | `General` |
| `R82` | 0 | `0%` |
| `D83` | -0.3174963663360941 | `General` |
| `N83` | 15 | `General` |
| `R83` | 0 | `0%` |
| `D84` | 0.4799462000591106 | `General` |
| `N84` | 16 | `General` |
| `R84` | 0 | `0%` |
| `D85` | 0.1338558955056115 | `General` |
| `N85` | 17 | `General` |
| `R85` | 0 | `0%` |
| `D86` | 0.24029663425984182 | `General` |
| `N86` | 18 | `General` |
| `R86` | 0 | `0%` |
| `D87` | -0.21984752873486713 | `General` |
| `N87` | 19 | `General` |
| `R87` | 0 | `0%` |
| `D88` | 0.2828356529119702 | `General` |
| `N88` | 20 | `General` |
| `R88` | 0.3 | `0%` |
| `D89` | 0.27999716396710994 | `General` |
| `N89` | 21 | `General` |
| `R89` | 0 | `0%` |
| `D90` | 0.18197032989439066 | `General` |
| `N90` | 22 | `General` |
| `R90` | 0 | `0%` |
| `D91` | -0.04224664129081141 | `General` |
| `N91` | 23 | `General` |
| `R91` | 0 | `0%` |
| `D92` | 0.10398136208608832 | `General` |
| `N92` | 24 | `General` |
| `R92` | 0 | `0%` |
| `D93` | 0.21636579072847884 | `General` |
| `N93` | 25 | `General` |
| `R93` | 0 | `0%` |
| `D94` | 0.4265894579611871 | `General` |
| `N94` | 26 | `General` |
| `R94` | 0 | `0%` |
| `D95` | -0.4716456668375386 | `General` |
| `N95` | 27 | `General` |
| `R95` | 0 | `0%` |
| `D96` | 0.7598462037312856 | `General` |
| `N96` | 28 | `General` |
| `R96` | 0 | `0%` |
| `D97` | -0.05242514298755907 | `General` |
| `N97` | 29 | `General` |
| `R97` | 0 | `0%` |
| `D98` | -0.2780783215610825 | `General` |
| `N98` | 30 | `General` |
| `R98` | 0 | `0%` |
| `D99` | 0.6822360754514492 | `General` |
| `N99` | 31 | `General` |
| `R99` | 0 | `0%` |
| `D100` | 0.13261124043213357 | `General` |
| `N100` | 32 | `General` |
| `R100` | 0 | `0%` |

Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):

| Columna | Primera / última celda | N | Primer / último valor |
|---|---|---:|---|
| D | `D101` / `D4961` | 4861 | 0.1070732764799871 / 0.1577410743092571 |
| N | `N101` / `N108` | 8 | 33 / 40 |
| R | `R101` / `R108` | 8 | 0 / 0 |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `G11` | `G11` | 1 | `=LN(S0*EXP(tipo*T)/K)` | 0.05379016416943189 |
| `G12` | `G12` | 1 | `=sigma*SQRT(T)` | 0.14142135623730953 |
| `G13` | `G13` | 1 | `=G11/G12+0.5*G12` | 0.45106457657208415 |
| `G14` | `G14` | 1 | `=G11/G12-0.5*G12` | 0.3096432203347746 |
| `G15` | `G16` | 2 | `=NORMSDIST(G13)` | 0.6740284962785699 |
| `D20` | `D20` | 1 | `=S0*G15-K*EXP(-tipo*T)*G16` | 3.569849048924663 |
| `E20` | `E22` | 3 | `=D20/S0` | 0.0849964059267777 |
| `D21` | `D21` | 1 | `=K*EXP(-tipo*T)*(1-G16)-S0*(1-G15)` | 1.3703482166319567 |
| `D22` | `D22` | 1 | `=D20-D21` | 2.1995008322927063 |
| `G28` | `G28` | 1 | `=1/50` | 0.02 |
| `D33` | `AC33` | 26 | `=D32*deltat` | 0 |
| `E34` | `AC34` | 25 | `=NORMSINV(RAND())` | -0.7024249743872925 |
| `D35` | `D35` | 1 | `=S0` | 42 |
| `E35` | `AC35` | 25 | `=D35*EXP((tipo-0.5*sigma^2)*deltat)*EXP(sigma*SQRT(deltat)*E34)` | 41.165562277662545 |
| `D38` | `AC38` | 26 | `=D35` | 42 |
| `D39` | `AC39` | 26 | `=T-D33` | 0.5 |
| `D40` | `AB40` | 25 | `=LN(D38*EXP(tipo*D39)/K)/(sigma*SQRT(D39))+0.5*sigma*SQRT(D39)` | 0.45106457657208415 |
| `D41` | `AB41` | 25 | `=NORMSDIST(D40)` | 0.6740284962785699 |
| `D44` | `AC44` | 26 | `=D32*deltat` | 0 |
| `D45` | `AB45` | 25 | `=D41` | 0.6740284962785699 |
| `D46` | `D46` | 1 | `=D47-D45*D35` | -24.73934779477527 |
| `E46` | `AB46` | 24 | `=D46*EXP(tipo*deltat)-(E45-D45)*E35` | -22.609910584630953 |
| `D47` | `D47` | 1 | `=D20` | 3.569849048924663 |
| `AC47` | `AC47` | 1 | `=AB45*AC35+AB46*EXP(tipo*deltat)` | -0.49810018283296686 |
| `D50` | `D50` | 1 | `=MAX(AC35-K,0)` | 0 |
| `D51` | `D51` | 1 | `=AC47` | -0.49810018283296686 |
| `D52` | `D52` | 1 | `=D51-D50` | -0.49810018283296686 |
| `D58` | `D58` | 1 | `=D52` | -0.49810018283296686 |
| `D59` | `D59` | 1 | `<DataTableFormula: {'ref': 'D59:D4961', 'ca': '1', 'dt2D': '0', 'dtr': '0', 'r1': 'C58', 'r2': None, 'del1': False, 'del2': False}>` | 0.11043519519227374 |
| `O60` | `O60` | 1 | `=COUNT(sims)` | 4903 |
| `O62` | `O62` | 1 | `=AVERAGE(sims)` | 0.004340624953456996 |
| `R62` | `R62` | 1 | `=PERCENTILE(sims,5%)` | -0.5880565245837422 |
| `O63` | `O63` | 1 | `=MAX(sims)` | 1.5387639571579825 |
| `O64` | `O64` | 1 | `=MIN(sims)` | -1.8192700299001316 |
| `P68` | `P108` | 41 | `=COUNTIF(sims,"<="&O68)/numsims` | 0 |
| `Q68` | `Q68` | 1 | `=P68` | 0 |
| `O69` | `O108` | 37 | `=O68+pasohist` | -1.9 |
| `Q69` | `Q108` | 40 | `=P69-P68` | 0 |
| `O88` | `O96` | 3 | `=O87+pasohist+0.02` | 0.02000000000000064 |

### Notas de celdas

- `G28`: recalculamos la cartera de cobertura cada 0.02 años

- `D47`: Ponemos la prima de la call como valor inicial de la cartera de cobertura
- `R62`: el ejercicio concluye variando la prima que se ha de cobrar (celda D51) para que aquí aparezca un 0. Es decir, para que en el 95% de los escenarios el descasamiento sea positivo. Ese valor será la prima original más, claro, este percentil.

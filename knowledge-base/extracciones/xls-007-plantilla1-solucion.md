# XLS-007: Plantilla1_Solucion.xlsx

Original: [archivo raw](../../raw/fundamentos/sesion-ii/plantilla1-solucion.xlsx). SHA-256: `16e99a21100402bc5b19d2901725fdc76b167bb81f4962ae2c397e560238cde4`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

Un nombre local prevalece sobre el nombre de libro al evaluar fórmulas de su hoja. Se incluyen los parámetros Solver, sin ejecutarlo.

| Nombre | Ámbito | Referencia | Oculto |
|---|---|---|---|
| `matrizS` | `libro` | `Hoja1!$D$8:$G$11` | 0 |
| `preciosHoy` | `libro` | `Hoja1!$B$8:$B$11` | 0 |
| `solver_adj` | `Hoja1` | `Hoja1!$N$6:$Q$6` | 1 |
| `solver_cvg` | `Hoja1` | `0.0001` | 1 |
| `solver_drv` | `Hoja1` | `1` | 1 |
| `solver_eng` | `Hoja1` | `1` | 1 |
| `solver_est` | `Hoja1` | `1` | 1 |
| `solver_itr` | `Hoja1` | `100` | 1 |
| `solver_lhs1` | `Hoja1` | `Hoja1!$S$6:$V$6` | 1 |
| `solver_lhs2` | `Hoja1` | `Hoja1!$S$8` | 1 |
| `solver_lhs3` | `Hoja1` | `Hoja1!$F$54` | 1 |
| `solver_lhs4` | `Hoja1` | `Hoja1!$G$54` | 1 |
| `solver_lin` | `Hoja1` | `2` | 1 |
| `solver_mip` | `Hoja1` | `2147483647` | 1 |
| `solver_mni` | `Hoja1` | `30` | 1 |
| `solver_mrt` | `Hoja1` | `0.075` | 1 |
| `solver_msl` | `Hoja1` | `2` | 1 |
| `solver_neg` | `Hoja1` | `2` | 1 |
| `solver_nod` | `Hoja1` | `2147483647` | 1 |
| `solver_num` | `Hoja1` | `1` | 1 |
| `solver_nwt` | `Hoja1` | `1` | 1 |
| `solver_opt` | `Hoja1` | `Hoja1!$N$9` | 1 |
| `solver_pre` | `Hoja1` | `0.000001` | 1 |
| `solver_rbv` | `Hoja1` | `1` | 1 |
| `solver_rel1` | `Hoja1` | `3` | 1 |
| `solver_rel2` | `Hoja1` | `3` | 1 |
| `solver_rel3` | `Hoja1` | `3` | 1 |
| `solver_rel4` | `Hoja1` | `3` | 1 |
| `solver_rhs1` | `Hoja1` | `0` | 1 |
| `solver_rhs2` | `Hoja1` | `1` | 1 |
| `solver_rhs3` | `Hoja1` | `0` | 1 |
| `solver_rhs4` | `Hoja1` | `0` | 1 |
| `solver_rlx` | `Hoja1` | `1` | 1 |
| `solver_rsd` | `Hoja1` | `0` | 1 |
| `solver_scl` | `Hoja1` | `2` | 1 |
| `solver_sho` | `Hoja1` | `2` | 1 |
| `solver_ssz` | `Hoja1` | `100` | 1 |
| `solver_tim` | `Hoja1` | `100` | 1 |
| `solver_tol` | `Hoja1` | `0.05` | 1 |
| `solver_typ` | `Hoja1` | `3` | 1 |
| `solver_val` | `Hoja1` | `0` | 1 |
| `solver_ver` | `Hoja1` | `3` | 1 |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B1:XFD91`. Celdas con contenido: 513. Fórmulas: 135. Familias: 29.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `N2` | Buscando oportunidades de arbitraje |
| `N4` | composición de la cartera de arbitraje |
| `S4` | flujo de la cartera en cada escenario |
| `B5` | Mercado  |
| `N5` | lambda1 |
| `O5` | lambda2 |
| `P5` | lambda3 |
| `Q5` | lambda4 |
| `S5` | en omega1 |
| `T5` | en omega2 |
| `U5` | en omega3 |
| `V5` | en omega4 |
| `B7` | tiempo 0 |
| `D7` | omega1 |
| `E7` | omega2 |
| `F7` | omega3 |
| `G7` | omega4 |
| `H8` | S1 |
| `N8` | coste cartera |
| `H9` | S2 |
| `H10` | S3 |
| `H11` | S4 |
| `B15` | Cálculo de carteras replicantes |
| `J16` | composición de las carteras replicantes |
| `N16` | flujos |
| `B17` | con solver |
| `I17` | coste |
| `J17` | lambda1 |
| `K17` | lambda2 |
| `L17` | lambda3 |
| `M17` | lambda4 |
| `N17` | en omega1 |
| `O17` | en omega2 |
| `P17` | en omega3 |
| `Q17` | en omega4 |
| `R17` | error Esc1 |
| `S17` | error Esc2 |
| `T17` | error Esc3 |
| `U17` | error Esc4 |
| `V17` | error total |
| `C18` | Activo X |
| `C19` | AD1 |
| `C20` | AD2 |
| `C21` | AD3 |
| `C22` | AD4 |
| `C23` | bono |
| `B25` | con álgebra lineal |
| `I25` | coste |
| `J25` | lambda1 |
| `K25` | lambda2 |
| `L25` | lambda3 |
| `M25` | lambda4 |
| `V25` | determinante |
| `C26` | Activo X |
| `S26` | Matriz inversa |
| `C27` | AD1 |
| `C28` | AD2 |
| `C29` | AD3 |
| `C30` | AD4 |
| `C31` | bono |
| `B35` | Cálculo de probabilidades de valoración |
| `K35` | Cálculo de probabilidades de valoración |
| `B37` | numerario N=S1 |
| `K37` | numerario M=3*S1+S2 |
| `B38` | tiempo 0 |
| `D38` | tiempo 1 |
| `K38` | tiempo 0 |
| `M38` | tiempo 1 |
| `B42` | Mercado, en términos del numerario |
| `K42` | Mercado, en términos del numerario |
| `B44` | tiempo 0 |
| `D44` | omega1 |
| `E44` | omega2 |
| `F44` | omega3 |
| `G44` | omega4 |
| `K44` | tiempo 0 |
| `M44` | omega1 |
| `N44` | omega2 |
| `O44` | omega3 |
| `P44` | omega4 |
| `H45` | S1/N |
| `Q45` | S1/M |
| `H46` | S2/N |
| `Q46` | S2/M |
| `H47` | S3/N |
| `Q47` | S3/M |
| `H48` | S4/N |
| `Q48` | S4/M |
| `B51` | Probabilidad de valoración |
| `K51` | Probabilidad de valoración |
| `B53` | con solver |
| `D53` | q1 |
| `E53` | q2 |
| `F53` | q3 |
| `G53` | q4 |
| `K53` | con solver |
| `M53` | p1 |
| `N53` | p2 |
| `O53` | p3 |
| `P53` | p4 |
| `D56` | error en activo 1 |
| `M56` | error en activo 1 |
| `D57` | error en activo 2 |
| `M57` | error en activo 2 |
| `D58` | error en activo 3 |
| `M58` | error en activo 3 |
| `D59` | error en activo 4 |
| `M59` | error en activo 4 |
| `D60` | error total |
| `M60` | error total |
| `B62` | con álgebra lineal |
| `K62` | con álgebra lineal |
| `D67` | q1 |
| `E67` | q2 |
| `F67` | q3 |
| `G67` | q4 |
| `M67` | p1 |
| `N67` | p2 |
| `O67` | p3 |
| `P67` | p4 |
| `B71` | Valoración con probabilidades |
| `K71` | Valoración con probabilidades |
| `D73` | activo X |
| `M73` | activo X |
| `D75` | activo X/N |
| `M75` | activo X/M |
| `C78` | valor hoy de X   |
| `L78` | valor hoy de X    |
| `J83` | Cambio de probabilidad (de las q's a las p's) |
| `H86` | Variable M/N |
| `H87` | tiempo 0 |
| `I87` | tiempo 1 |
| `D90` | q1 |
| `E90` | q2 |
| `F90` | q3 |
| `G90` | q4 |
| `M90` | p1 |
| `N90` | p2 |
| `O90` | p3 |
| `P90` | p4 |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `N6` | -0.4628874142443454 | `General` |
| `O6` | 0.5425180820189874 | `General` |
| `P6` | -0.05939573692998873 | `General` |
| `Q6` | 1.0572270465017783 | `General` |
| `B8` | 1.5 | `General` |
| `D8` | 2 | `General` |
| `E8` | 1 | `General` |
| `F8` | 1.5 | `General` |
| `G8` | 2 | `General` |
| `B9` | 0.3 | `General` |
| `D9` | -4 | `General` |
| `E9` | 2 | `General` |
| `F9` | -1 | `General` |
| `G9` | 1 | `General` |
| `B10` | 2.5 | `General` |
| `D10` | 5 | `General` |
| `E10` | 1 | `General` |
| `F10` | 1.5 | `General` |
| `G10` | 4 | `General` |
| `B11` | 1.3 | `General` |
| `D11` | 3.5 | `General` |
| `E11` | 0 | `General` |
| `F11` | 2 | `General` |
| `G11` | 1.5 | `General` |
| `D18` | 1 | `General` |
| `E18` | 0 | `General` |
| `F18` | 0.5 | `General` |
| `G18` | 1 | `General` |
| `J18` | -1.9374961186281512 | `0.0000` |
| `K18` | 0.8124987651464676 | `0.0000` |
| `L18` | 0.31249811952146817 | `0.0000` |
| `M18` | 1.8749988757904454 | `0.0000` |
| `D19` | 1 | `General` |
| `E19` | 0 | `General` |
| `F19` | 0 | `General` |
| `G19` | 0 | `General` |
| `J19` | 1.9999666504144944 | `0.0000` |
| `K19` | -0.9999881871740578 | `0.0000` |
| `L19` | 4.563508345723573e-06 | `0.0000` |
| `M19` | -1.999974329009888 | `0.0000` |
| `D20` | 0 | `General` |
| `E20` | 1 | `General` |
| `F20` | 0 | `General` |
| `G20` | 0 | `General` |
| `J20` | 5.312500698865436 | `0.0000` |
| `K20` | -1.9375001831846266 | `0.0000` |
| `L20` | -0.43750024570150026 | `0.0000` |
| `M20` | -4.625000359716165 | `0.0000` |
| `D21` | 0 | `General` |
| `E21` | 0 | `General` |
| `F21` | 1 | `General` |
| `G21` | 0 | `General` |
| `J21` | -0.8749915156042278 | `0.0000` |
| `K21` | 0.6249980500045748 | `0.0000` |
| `L21` | -0.3750043907182418 | `0.0000` |
| `M21` | 1.7499982876241702 | `0.0000` |
| `D22` | 0 | `General` |
| `E22` | 0 | `General` |
| `F22` | 0 | `General` |
| `G22` | 1 | `General` |
| `J22` | -3.4999940443322437 | `0.0000` |
| `K22` | 1.499996224730821 | `0.0000` |
| `L22` | 0.4999980853677392 | `0.0000` |
| `M22` | 2.999995976008642 | `0.0000` |
| `D23` | 1 | `General` |
| `E23` | 1 | `General` |
| `F23` | 1 | `General` |
| `G23` | 1 | `General` |
| `J23` | 2.9375309224179804 | `0.0000` |
| `K23` | -0.8125138819770303 | `0.0000` |
| `L23` | -0.31250246070082743 | `0.0000` |
| `M23` | -1.8750296418000483 | `0.0000` |
| `D26` | 1 | `General` |
| `E26` | 0 | `General` |
| `F26` | 0.5 | `General` |
| `G26` | 1 | `General` |
| `K26` | 0.8124999999999982 | `0.0000` |
| `L26` | 0.3125000000000001 | `0.0000` |
| `M26` | 1.874999999999996 | `0.0000` |
| `D27` | 1 | `General` |
| `E27` | 0 | `General` |
| `F27` | 0 | `General` |
| `G27` | 0 | `General` |
| `K27` | -0.999999999999998 | `0.0000` |
| `L27` | -1.7763568394002506e-16 | `0.0000` |
| `M27` | -1.9999999999999953 | `0.0000` |
| `T27` | -0.999999999999998 | `0.0000` |
| `U27` | -1.7763568394002506e-16 | `0.0000` |
| `V27` | -1.9999999999999953 | `0.0000` |
| `D28` | 0 | `General` |
| `E28` | 1 | `General` |
| `F28` | 0 | `General` |
| `G28` | 0 | `General` |
| `K28` | -1.9374999999999956 | `0.0000` |
| `L28` | -0.4375000000000004 | `0.0000` |
| `M28` | -4.62499999999999 | `0.0000` |
| `S28` | 5.31249999999999 | `0.0000` |
| `T28` | -1.9374999999999956 | `0.0000` |
| `U28` | -0.4375000000000004 | `0.0000` |
| `V28` | -4.62499999999999 | `0.0000` |
| `D29` | 0 | `General` |
| `E29` | 0 | `General` |
| `F29` | 1 | `General` |
| `G29` | 0 | `General` |
| `K29` | 0.6249999999999988 | `0.0000` |
| `L29` | -0.3749999999999999 | `0.0000` |
| `M29` | 1.7499999999999971 | `0.0000` |
| `S29` | -0.8749999999999973 | `0.0000` |
| `T29` | 0.6249999999999988 | `0.0000` |
| `U29` | -0.3749999999999999 | `0.0000` |
| `V29` | 1.7499999999999971 | `0.0000` |
| `D30` | 0 | `General` |
| `E30` | 0 | `General` |
| `F30` | 0 | `General` |
| `G30` | 1 | `General` |
| `K30` | 1.499999999999997 | `0.0000` |
| `L30` | 0.5000000000000002 | `0.0000` |
| `M30` | 2.999999999999993 | `0.0000` |
| `S30` | -3.4999999999999933 | `0.0000` |
| `T30` | 1.499999999999997 | `0.0000` |
| `U30` | 0.5000000000000002 | `0.0000` |
| `V30` | 2.999999999999993 | `0.0000` |
| `D31` | 1 | `General` |
| `E31` | 1 | `General` |
| `F31` | 1 | `General` |
| `G31` | 1 | `General` |
| `K31` | -0.8124999999999982 | `0.0000` |
| `L31` | -0.3125000000000002 | `0.0000` |
| `M31` | -1.8749999999999956 | `0.0000` |
| `E39` | 1 | `General` |
| `F39` | 1.5 | `General` |
| `G39` | 2 | `General` |
| `N39` | 5 | `General` |
| `O39` | 3.5 | `General` |
| `P39` | 7 | `General` |
| `E45` | 1 | `0.000` |
| `F45` | 1 | `0.000` |
| `G45` | 1 | `0.000` |
| `N45` | 0.2 | `0.000` |
| `O45` | 0.42857142857142855 | `0.000` |
| `P45` | 0.2857142857142857 | `0.000` |
| `B46` | 0.19999999999999998 | `General` |
| `D46` | -2 | `0.000` |
| `E46` | 2 | `0.000` |
| `F46` | -0.6666666666666666 | `0.000` |
| `G46` | 0.5 | `0.000` |
| `K46` | 0.0625 | `General` |
| `M46` | -2 | `0.000` |
| `N46` | 0.4 | `0.000` |
| `O46` | -0.2857142857142857 | `0.000` |
| `P46` | 0.14285714285714285 | `0.000` |
| `B47` | 1.6666666666666667 | `General` |
| `D47` | 2.5 | `0.000` |
| `E47` | 1 | `0.000` |
| `F47` | 1 | `0.000` |
| `G47` | 2 | `0.000` |
| `K47` | 0.5208333333333334 | `General` |
| `M47` | 2.5 | `0.000` |
| `N47` | 0.2 | `0.000` |
| `O47` | 0.42857142857142855 | `0.000` |
| `P47` | 0.5714285714285714 | `0.000` |
| `B48` | 0.8666666666666667 | `General` |
| `D48` | 1.75 | `0.000` |
| `E48` | 0 | `0.000` |
| `F48` | 1.3333333333333333 | `0.000` |
| `G48` | 0.75 | `0.000` |
| `K48` | 0.27083333333333337 | `General` |
| `M48` | 1.75 | `0.000` |
| `N48` | 0 | `0.000` |
| `O48` | 0.5714285714285714 | `0.000` |
| `P48` | 0.21428571428571427 | `0.000` |
| `D54` | 0.1333362379857227 | `0.000%` |
| `E54` | 0.18750354829364077 | `0.000%` |
| `F54` | 0.21249860901150544 | `0.000%` |
| `G54` | 0.466661943596172 | `0.000%` |
| `M54` | 0.041666637919105104 | `0.000%` |
| `N54` | 0.2929687292299655 | `0.000%` |
| `O54` | 0.1549480347711815 | `0.000%` |
| `P54` | 0.5104166320514893 | `0.000%` |
| `E62` | -1.9999999999999971 | `0.000` |
| `F62` | 3.552713678800501e-16 | `0.000` |
| `G62` | -3.9999999999999942 | `0.000` |
| `N62` | -2.000000000000001 | `0.000` |
| `O62` | -5.329070518200751e-16 | `0.000` |
| `P62` | -4.000000000000003 | `0.000` |
| `D63` | 5.312499999999992 | `0.000` |
| `E63` | -1.937499999999997 | `0.000` |
| `F63` | -0.4374999999999997 | `0.000` |
| `G63` | -4.624999999999994 | `0.000` |
| `M63` | 26.56250000000002 | `0.000` |
| `N63` | -9.687500000000007 | `0.000` |
| `O63` | -2.187500000000003 | `0.000` |
| `P63` | -23.125000000000014 | `0.000` |
| `D64` | -1.312499999999997 | `0.000` |
| `E64` | 0.9374999999999987 | `0.000` |
| `F64` | -0.5625000000000002 | `0.000` |
| `G64` | 2.6249999999999973 | `0.000` |
| `M64` | -3.0625000000000036 | `0.000` |
| `N64` | 2.1875000000000013 | `0.000` |
| `O64` | -1.3124999999999996 | `0.000` |
| `P64` | 6.1250000000000036 | `0.000` |
| `D65` | -6.999999999999989 | `0.000` |
| `E65` | 2.9999999999999956 | `0.000` |
| `F65` | 0.9999999999999996 | `0.000` |
| `G65` | 5.999999999999991 | `0.000` |
| `M65` | -24.50000000000002 | `0.000` |
| `N65` | 10.500000000000007 | `0.000` |
| `O65` | 3.500000000000003 | `0.000` |
| `P65` | 21.000000000000018 | `0.000` |
| `E68` | 0.18749999999999822 | `0.000%` |
| `F68` | 0.21250000000000036 | `0.000%` |
| `G68` | 0.4666666666666677 | `0.000%` |
| `N68` | 0.2929687500000009 | `0.000%` |
| `O68` | 0.15494791666666696 | `0.000%` |
| `P68` | 0.510416666666667 | `0.000%` |
| `D74` | 1 | `General` |
| `E74` | 0 | `General` |
| `F74` | 0 | `General` |
| `G74` | 0 | `General` |
| `N74` | 0 | `General` |
| `O74` | 0 | `General` |
| `P74` | 0 | `General` |
| `E76` | 0 | `General` |
| `F76` | 0 | `General` |
| `G76` | 0 | `General` |
| `N76` | 0 | `General` |
| `O76` | 0 | `General` |
| `P76` | 0 | `General` |
| `J88` | 5 | `General` |
| `K88` | 2.3333333333333335 | `General` |
| `L88` | 3.5 | `General` |
| `E91` | 0.18749999999999822 | `0.000%` |
| `F91` | 0.21250000000000036 | `0.000%` |
| `G91` | 0.4666666666666677 | `0.000%` |
| `N91` | 0.2929687499999972 | `0.000%` |
| `O91` | 0.15494791666666693 | `0.000%` |
| `P91` | 0.5104166666666679 | `0.000%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `S6` | `V6` | 4 | `=MMULT($N$6:$Q$6,D8:D11)` | 0.3074688215416401 |
| `S8` | `S8` | 1 | `=SUMPRODUCT(S6:V6,S6:V6)` | 1.9642047648917962 |
| `N9` | `N9` | 1 | `=MMULT(N6:Q6,preciosHoy)` | 0.6943301213665183 |
| `I18` | `I31` | 12 | `=MMULT(J18:M18,preciosHoy)` | 0.5562492889329631 |
| `N18` | `Q31` | 48 | `=MMULT($J18:$M18,D$8:D$11)` | 0.9999993650317265 |
| `R18` | `U23` | 24 | `=(N18-D18)^2` | 4.0318470837224374e-13 |
| `V18` | `V23` | 6 | `=SQRT(SUM(R18:U18))*1000000` | 3.4290569357075134 |
| `J26` | `J31` | 6 | `=MMULT(D26:G26,$S$27:$V$30)` | -1.9374999999999962 |
| `V26` | `V26` | 1 | `=MDETERM(matrizS)` | -4.000000000000009 |
| `S27` | `S27` | 1 | `=MINVERSE(matrizS)` | 1.9999999999999958 |
| `B39` | `B39` | 1 | `=B8` | 1.5 |
| `D39` | `D39` | 1 | `=D8:G8` | 2 |
| `K39` | `K39` | 1 | `=3*B8+B9` | 4.8 |
| `M39` | `M39` | 1 | `=3*D8:G8+D9:G9` | 2 |
| `B45` | `K45` | 2 | `=preciosHoy/B39` | 1 |
| `D45` | `M45` | 2 | `=matrizS/D39:G39` | 1 |
| `E56` | `E59` | 4 | `=(SUMPRODUCT($D$54:$G$54,D45:G45)-B45)^2` | 1.1484442647221026e-13 |
| `N56` | `N59` | 4 | `=(SUMPRODUCT($M$54:$P$54,M45:P45)-K45)^2` | 6.122438898224819e-17 |
| `E60` | `E60` | 1 | `=SUM(E56:E59)*1000000` | 2.356503937111781e-07 |
| `N60` | `N60` | 1 | `=SUM(N56:N59)*10000` | 2.3085840613996947e-11 |
| `D62` | `M62` | 2 | `=MINVERSE(D45:G48)` | 3.999999999999994 |
| `D68` | `M68` | 2 | `=TRANSPOSE(MMULT(D62:G65,B45:B48))` | 0.13333333333333286 |
| `M74` | `M74` | 1 | `=D74:G74` | 1 |
| `D76` | `M76` | 2 | `=D74:G74/D39:G39` | 0.5 |
| `D78` | `M78` | 2 | `=SUMPRODUCT(D76:G76,D68:G68)*B39` | 0.09999999999999964 |
| `H88` | `H88` | 1 | `=K39/B39` | 3.1999999999999997 |
| `I88` | `I88` | 1 | `=M39:P39/D39:G39` | 1 |
| `D91` | `D91` | 1 | `=D68:G68` | 0.13333333333333286 |
| `M91` | `M91` | 1 | `=D91:G91*I88:L88/H88` | 0.04166666666666652 |

### Notas de celdas

- `P2`: Para que solver encuentre una solución, cambia, por ejemplo, el precio  B8 a 3

- `V6`: jcontreras: deben ser todos >=0

- `S8`: jcontreras: esta casilla es para comprobar si hay al menos un flujo positivo

- `N9`: jcontreras: queremos un 0 aqui

# XLS-008: Plantilla2_Solucion.xlsx

Original: [archivo raw](../../raw/fundamentos/sesion-ii/plantilla2-solucion.xlsx). SHA-256: `75d0ca4dc327ebfd98ee39f1be7b42f1daa8011e205e18174529ef2859cefacd`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

Un nombre local prevalece sobre el nombre de libro al evaluar fórmulas de su hoja. Se incluyen los parámetros Solver, sin ejecutarlo.

| Nombre | Ámbito | Referencia | Oculto |
|---|---|---|---|
| `Num0` | `libro` | `Hoja1!$R$9` | 0 |
| `solver_adj` | `Hoja1` | `Hoja1!$AH$25:$AH$27` | 1 |
| `solver_cvg` | `Hoja1` | `0.0001` | 1 |
| `solver_drv` | `Hoja1` | `1` | 1 |
| `solver_eng` | `Hoja1` | `1` | 1 |
| `solver_est` | `Hoja1` | `1` | 1 |
| `solver_itr` | `Hoja1` | `10000` | 1 |
| `solver_lhs1` | `Hoja1` | `Hoja1!$U$21` | 1 |
| `solver_lhs2` | `Hoja1` | `Hoja1!$U$20` | 1 |
| `solver_lhs3` | `Hoja1` | `Hoja1!$U$21` | 1 |
| `solver_lin` | `Hoja1` | `2` | 1 |
| `solver_mip` | `Hoja1` | `2147483647` | 1 |
| `solver_mni` | `Hoja1` | `30` | 1 |
| `solver_mrt` | `Hoja1` | `0.075` | 1 |
| `solver_msl` | `Hoja1` | `2` | 1 |
| `solver_neg` | `Hoja1` | `2` | 1 |
| `solver_nod` | `Hoja1` | `2147483647` | 1 |
| `solver_num` | `Hoja1` | `0` | 1 |
| `solver_nwt` | `Hoja1` | `1` | 1 |
| `solver_opt` | `Hoja1` | `Hoja1!$AL$35` | 1 |
| `solver_pre` | `Hoja1` | `0.0000000001` | 1 |
| `solver_rbv` | `Hoja1` | `1` | 1 |
| `solver_rel1` | `Hoja1` | `3` | 1 |
| `solver_rel2` | `Hoja1` | `3` | 1 |
| `solver_rel3` | `Hoja1` | `3` | 1 |
| `solver_rhs1` | `Hoja1` | `0` | 1 |
| `solver_rhs2` | `Hoja1` | `0` | 1 |
| `solver_rhs3` | `Hoja1` | `0` | 1 |
| `solver_rlx` | `Hoja1` | `1` | 1 |
| `solver_rsd` | `Hoja1` | `0` | 1 |
| `solver_scl` | `Hoja1` | `2` | 1 |
| `solver_sho` | `Hoja1` | `2` | 1 |
| `solver_ssz` | `Hoja1` | `100` | 1 |
| `solver_tim` | `Hoja1` | `10000` | 1 |
| `solver_tol` | `Hoja1` | `0.05` | 1 |
| `solver_typ` | `Hoja1` | `3` | 1 |
| `solver_val` | `Hoja1` | `0` | 1 |
| `solver_ver` | `Hoja1` | `3` | 1 |
| `tipo` | `libro` | `Hoja1!$E$16` | 0 |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B3:BC76`. Celdas con contenido: 583. Fórmulas: 217. Familias: 69.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `R3` | 2. Elegimos como numerario el activo S1 |
| `AE3` | 3. Elegimos como numerario el activo S2 |
| `AR3` | 4. Cambio de numerario/probabilidad |
| `Q5` | numerario N |
| `AD5` | numerario M |
| `AQ5` | numerario N |
| `AX5` | numerario M |
| `J8` | En esta hoja de cálculo hay 4 ejercicios: |
| `J10` | 1. Valorar un activo cualquiera X por replicación |
| `J11` | 2. Calcular la prob de valoración para N=S1 y valorar X |
| `B12` | Modelo: tres activos, con los siguientes valores en cada uno de los escenarios: |
| `J12` | 3. Calcular la prob de valoración para M=S2 y valorar X |
| `J13` | 4. Usar la fórmula del cambio de numerario |
| `D16` | r |
| `X16` | cálculos para nodos finales |
| `Z16` | cálculos para nodo inicial |
| `AK16` | cálculos para nodos finales |
| `AM16` | cálculos para nodo inicial |
| `AR16` | Para el numerario N, las probabilidades en cada nodo son |
| `AY16` | Para el numerario M, las probabilidades en cada nodo son |
| `U18` | probabilidades |
| `AH18` | probabilidades |
| `B19` | activo S1 |
| `Q19` | activo S1/N |
| `AD19` | activo S1/M |
| `Y26` | error en a |
| `Y28` | error en b |
| `B29` | activo S2 |
| `Q29` | activo S2/N |
| `AD29` | activo S2/M |
| `Y30` | error en c |
| `AL30` | error en a |
| `AS30` | Queremos hallar la probabilidad de valoración con respecto a M sin necesidad de resolver los sistemas de ecuaciones correspondientes |
| `AA31` | error inicial |
| `AN31` | error inicial |
| `AS31` | (solo usando los valores de los dos numerarios y la prob de valoración con respecto a N) |
| `AL32` | error en b |
| `AL34` | error en c |
| `B39` | activo S3 |
| `Q39` | activo S3/N |
| `AD39` | activo S3/M |
| `AQ39` | proceso M/N |
| `R49` | Una vez calculadas las probabilidades de valoración, |
| `AE49` | Una vez calculadas las probabilidades de valoración, |
| `AR49` | N(0)/M(0) |
| `B50` | 1. Valoración por replicación |
| `J50` | Cálculo de carteras replicantes |
| `R50` | las usamos para valorar un activo X cualquiera |
| `AE50` | las usamos para valorar un activo X cualquiera |
| `K51` | composición |
| `L51` | flujo |
| `M51` | error |
| `N51` | total |
| `B52` | activo X |
| `J52` | lambda1 |
| `Q52` | activo X/N |
| `AD52` | activo X/M |
| `AR52` | El primer juego de probs (para el nodo inicial) se obtiene aplicando la fórmula: |
| `I53` | nodo a |
| `J53` | lambda2 |
| `J54` | lambda3 |
| `AT54` | a |
| `J55` | lambda1 |
| `I56` | nodo b |
| `J56` | lambda2 |
| `J57` | lambda3 |
| `AT57` | b |
| `J58` | lambda1 |
| `I59` | nodo c |
| `J59` | lambda2 |
| `J60` | lambda3 |
| `AT60` | c |
| `AR62` | Para los 9 escenarios finales: |
| `F63` | compos |
| `G63` | flujo |
| `H63` | error |
| `I63` | total |
| `Q63` | activo X |
| `AD63` | activo X |
| `E64` | lambda1 |
| `AS64` | Observa que las probs que asigna Q_N a los 9 escenarios finales son |
| `AV64` | Hacemos el cambio de probabilidad, con la fórmula general |
| `AY64` | Finalmente, recuperamos las probs en cada nodo |
| `D65` | nodo inicial |
| `E65` | lambda2 |
| `E66` | lambda3 |
| `AT68` | (a,1) |
| `AW68` | (a,1) |
| `AZ68` | (a,1) |
| `AT69` | (a,2) |
| `AW69` | (a,2) |
| `AZ69` | (a,2) |
| `AT70` | (a,3) |
| `AW70` | (a,3) |
| `AZ70` | (a,3) |
| `AT71` | (b,1) |
| `AW71` | (b,1) |
| `AZ71` | (b,1) |
| `AT72` | (b,2) |
| `AW72` | (b,2) |
| `AZ72` | (b,2) |
| `AT73` | (b,3) |
| `AW73` | (b,3) |
| `AZ73` | (b,3) |
| `AT74` | (c,1) |
| `AW74` | (c,1) |
| `AZ74` | (c,1) |
| `AT75` | (c,2) |
| `AW75` | (c,2) |
| `AZ75` | (c,2) |
| `AT76` | (c,3) |
| `AW76` | (c,3) |
| `AZ76` | (c,3) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `V6` | 1.0404 | `General` |
| `AV6` | 1.0404 | `General` |
| `BC6` | 12 | `General` |
| `V7` | 1.0404 | `General` |
| `AV7` | 1.0404 | `General` |
| `BC7` | 5 | `General` |
| `V8` | 1.0404 | `General` |
| `AV8` | 1.0404 | `General` |
| `BC8` | 11 | `General` |
| `V9` | 1.0404 | `General` |
| `AV9` | 1.0404 | `General` |
| `BC9` | 10 | `General` |
| `V10` | 1.0404 | `General` |
| `AV10` | 1.0404 | `General` |
| `BC10` | 9 | `General` |
| `V11` | 1.0404 | `General` |
| `AV11` | 1.0404 | `General` |
| `BC11` | 11 | `General` |
| `V12` | 1.0404 | `General` |
| `AV12` | 1.0404 | `General` |
| `BC12` | 8 | `General` |
| `V13` | 1.0404 | `General` |
| `AV13` | 1.0404 | `General` |
| `BC13` | 7 | `General` |
| `E16` | 0.02 | `0%` |
| `U19` | 0.6799999942661007 | `0.00%` |
| `AH19` | 0.77777782859387 | `0.00%` |
| `S20` | 0.5350001357348568 | `0.00%` |
| `U20` | 0.1600000438290322 | `0.00%` |
| `V20` | 1 | `General` |
| `AF20` | 0.6294122125191391 | `0.00%` |
| `AH20` | 0.1568628016157034 | `0.00%` |
| `AI20` | 0.0867 | `General` |
| `AU20` | 0.1600000438290322 | `0.00%` |
| `BB20` | 0.1568628016157034 | `0.00%` |
| `U21` | 0.1599999643970968 | `0.00%` |
| `V21` | 1 | `General` |
| `AH21` | 0.065359300414164 | `0.00%` |
| `AI21` | 0.20808 | `General` |
| `AU21` | 0.1599999643970968 | `0.00%` |
| `BB21` | 0.065359300414164 | `0.00%` |
| `U22` | 0.33666658569294566 | `0.00%` |
| `V22` | 1 | `General` |
| `AH22` | 0.36307350776982084 | `0.00%` |
| `AI22` | 0.09458181818181818 | `General` |
| `AU22` | 0.33666658569294566 | `0.00%` |
| `BB22` | 0.36307350776982084 | `0.00%` |
| `D23` | 1 | `General` |
| `S23` | 0.030000027638011684 | `0.00%` |
| `U23` | 0.5266665725991069 | `0.00%` |
| `V23` | 1 | `General` |
| `AF23` | 0.02941252922637688 | `0.00%` |
| `AH23` | 0.51633822601906 | `0.00%` |
| `AI23` | 0.10404 | `General` |
| `AU23` | 0.5266665725991069 | `0.00%` |
| `BB23` | 0.51633822601906 | `0.00%` |
| `U24` | 0.13666676419332555 | `0.00%` |
| `V24` | 1 | `General` |
| `AH24` | 0.1205882854861896 | `0.00%` |
| `AI24` | 0.1156 | `General` |
| `AU24` | 0.13666676419332555 | `0.00%` |
| `BB24` | 0.1205882854861896 | `0.00%` |
| `U25` | 0.1363633867033645 | `0.00%` |
| `V25` | 1 | `General` |
| `AH25` | 0.18381578812823185 | `0.00%` |
| `AI25` | 0.09458181818181818 | `General` |
| `AU25` | 0.1363633867033645 | `0.00%` |
| `BB25` | 0.18381578812823185 | `0.00%` |
| `S26` | 0.43499981411694777 | `0.00%` |
| `U26` | 0.6145450632940045 | `0.00%` |
| `V26` | 1 | `General` |
| `AF26` | 0.34117556542103333 | `0.00%` |
| `AH26` | 0.602507948708021 | `0.00%` |
| `AI26` | 0.13005 | `General` |
| `AU26` | 0.6145450632940045 | `0.00%` |
| `BB26` | 0.602507948708021 | `0.00%` |
| `U27` | 0.2490912965221882 | `0.00%` |
| `V27` | 1 | `General` |
| `AH27` | 0.2136757279752852 | `0.00%` |
| `AI27` | 0.14862857142857142 | `General` |
| `AU27` | 0.2490912965221882 | `0.00%` |
| `BB27` | 0.2136757279752852 | `0.00%` |
| `H29` | 14 | `General` |
| `F30` | 12 | `General` |
| `H30` | 12 | `General` |
| `U30` | 0.1600000438290322 | `0.00%` |
| `V30` | 11.534025374855824 | `General` |
| `AH30` | 0.1568628016157034 | `0.00%` |
| `AI30` | 1 | `General` |
| `H31` | 5 | `General` |
| `U31` | 0.1599999643970968 | `0.00%` |
| `V31` | 4.805843906189927 | `General` |
| `AH31` | 0.065359300414164 | `0.00%` |
| `AI31` | 1 | `General` |
| `H32` | 11 | `General` |
| `U32` | 0.33666658569294566 | `0.00%` |
| `V32` | 10.57285659361784 | `General` |
| `AH32` | 0.36307350776982084 | `0.00%` |
| `AI32` | 1 | `General` |
| `D33` | 10 | `General` |
| `F33` | 10 | `General` |
| `H33` | 10 | `General` |
| `U33` | 0.5266665725991069 | `0.00%` |
| `V33` | 9.611687812379854 | `General` |
| `AH33` | 0.51633822601906 | `0.00%` |
| `AI33` | 1 | `General` |
| `H34` | 9 | `General` |
| `U34` | 0.13666676419332555 | `0.00%` |
| `V34` | 8.650519031141869 | `General` |
| `AH34` | 0.1205882854861896 | `0.00%` |
| `AI34` | 1 | `General` |
| `H35` | 11 | `General` |
| `U35` | 0.1363633867033645 | `0.00%` |
| `V35` | 10.57285659361784 | `General` |
| `AH35` | 0.18381578812823185 | `0.00%` |
| `AI35` | 1 | `General` |
| `F36` | 8 | `General` |
| `H36` | 8 | `General` |
| `U36` | 0.6145450632940045 | `0.00%` |
| `V36` | 7.6893502499038835 | `General` |
| `AH36` | 0.602507948708021 | `0.00%` |
| `AI36` | 1 | `General` |
| `H37` | 7 | `General` |
| `U37` | 0.2490912965221882 | `0.00%` |
| `V37` | 6.728181468665897 | `General` |
| `AH37` | 0.2136757279752852 | `0.00%` |
| `AI37` | 1 | `General` |
| `H39` | 5 | `General` |
| `F40` | 6 | `General` |
| `H40` | 7 | `General` |
| `U40` | 0.1600000438290322 | `0.00%` |
| `V40` | 6.728181468665897 | `General` |
| `AH40` | 0.1568628016157034 | `0.00%` |
| `AI40` | 0.5833333333333334 | `General` |
| `H41` | 10 | `General` |
| `U41` | 0.1599999643970968 | `0.00%` |
| `V41` | 9.611687812379854 | `General` |
| `AH41` | 0.065359300414164 | `0.00%` |
| `AI41` | 2 | `General` |
| `H42` | 4 | `General` |
| `U42` | 0.33666658569294566 | `0.00%` |
| `V42` | 3.8446751249519417 | `General` |
| `AH42` | 0.36307350776982084 | `0.00%` |
| `AI42` | 0.36363636363636365 | `General` |
| `D43` | 12 | `General` |
| `F43` | 11 | `General` |
| `H43` | 12 | `General` |
| `U43` | 0.5266665725991069 | `0.00%` |
| `V43` | 11.534025374855824 | `General` |
| `AH43` | 0.51633822601906 | `0.00%` |
| `AI43` | 1.2 | `General` |
| `H44` | 26 | `General` |
| `U44` | 0.13666676419332555 | `0.00%` |
| `V44` | 24.99038831218762 | `General` |
| `AH44` | 0.1205882854861896 | `0.00%` |
| `AI44` | 2.888888888888889 | `General` |
| `H45` | 11 | `General` |
| `U45` | 0.1363633867033645 | `0.00%` |
| `V45` | 10.57285659361784 | `General` |
| `AH45` | 0.18381578812823185 | `0.00%` |
| `AI45` | 1 | `General` |
| `F46` | 20 | `General` |
| `H46` | 19 | `General` |
| `U46` | 0.6145450632940045 | `0.00%` |
| `V46` | 18.26220684352172 | `General` |
| `AH46` | 0.602507948708021 | `0.00%` |
| `AI46` | 2.375 | `General` |
| `H47` | 29 | `General` |
| `U47` | 0.2490912965221882 | `0.00%` |
| `V47` | 27.873894655901577 | `General` |
| `AH47` | 0.2136757279752852 | `0.00%` |
| `AI47` | 4.142857142857143 | `General` |
| `H52` | 1 | `General` |
| `K52` | 10.212433059321762 | `General` |
| `H53` | 0 | `General` |
| `K53` | -0.3750010805093849 | `General` |
| `U53` | 0.1600000438290322 | `0.0000%` |
| `V53` | 0 | `General` |
| `AH53` | 0.1568628016157034 | `0.0000%` |
| `AI53` | 0 | `General` |
| `H54` | 0 | `General` |
| `K54` | -0.8750002954737958 | `General` |
| `U54` | 0.1599999643970968 | `0.0000%` |
| `V54` | 0 | `General` |
| `AH54` | 0.065359300414164 | `0.0000%` |
| `AI54` | 0 | `General` |
| `H55` | 1 | `General` |
| `K55` | -24.349571775946924 | `General` |
| `U55` | 0.33666658569294566 | `0.0000%` |
| `V55` | 0.9611687812379854 | `General` |
| `AH55` | 0.36307350776982084 | `0.0000%` |
| `AI55` | 0.09090909090909091 | `General` |
| `H56` | 0 | `General` |
| `K56` | 2.3333264743805007 | `General` |
| `U56` | 0.5266665725991069 | `0.0000%` |
| `V56` | 0 | `General` |
| `AH56` | 0.51633822601906 | `0.0000%` |
| `AI56` | 0 | `General` |
| `H57` | 0 | `General` |
| `K57` | 0.16666790866088546 | `General` |
| `U57` | 0.13666676419332555 | `0.0000%` |
| `V57` | 0 | `General` |
| `AH57` | 0.1205882854861896 | `0.0000%` |
| `AI57` | 0 | `General` |
| `H58` | 1 | `General` |
| `K58` | -4.32525158542714 | `General` |
| `U58` | 0.1363633867033645 | `0.0000%` |
| `V58` | 0.9611687812379854 | `General` |
| `AH58` | 0.18381578812823185 | `0.0000%` |
| `AI58` | 0.09090909090909091 | `General` |
| `H59` | 0 | `General` |
| `K59` | 0.45454367845719246 | `General` |
| `U59` | 0.6145450632940045 | `0.0000%` |
| `V59` | 0 | `General` |
| `AH59` | 0.602507948708021 | `0.0000%` |
| `AI59` | 0 | `General` |
| `H60` | 0 | `General` |
| `K60` | 0.04545475611224917 | `General` |
| `U60` | 0.2490912965221882 | `0.0000%` |
| `V60` | 0 | `General` |
| `AH60` | 0.2136757279752852 | `0.0000%` |
| `AI60` | 0 | `General` |
| `F64` | -2.5640783115591033 | `General` |
| `V64` | 0 | `General` |
| `AI64` | 0 | `General` |
| `F65` | 0.2559705626611672 | `General` |
| `V65` | 0 | `General` |
| `AI65` | 0 | `General` |
| `F66` | 0.03506415213745179 | `General` |
| `V66` | 1 | `General` |
| `AI66` | 1 | `General` |
| `V67` | 0 | `General` |
| `AI67` | 0 | `General` |
| `V68` | 0 | `General` |
| `AI68` | 0 | `General` |
| `V69` | 1 | `General` |
| `AI69` | 1 | `General` |
| `AS69` | 0.08560004516611527 | `0.00%` |
| `AY69` | 0.15686278806767864 | `0.00%` |
| `V70` | 0 | `General` |
| `AI70` | 0 | `General` |
| `AS70` | 0.08560000267001905 | `0.00%` |
| `AY70` | 0.06535946258051341 | `0.00%` |
| `V71` | 0 | `General` |
| `AI71` | 0 | `General` |
| `AS72` | 0.015800011733990094 | `0.00%` |
| `AY72` | 0.5163397770579479 | `0.00%` |
| `AS73` | 0.004100006702997392 | `0.00%` |
| `AY73` | 0.12058832134705194 | `0.00%` |
| `AS75` | 0.26732698829937984 | `0.00%` |
| `AY75` | 0.6024951600921614 | `0.00%` |
| `AS76` | 0.10835466768530139 | `0.00%` |
| `AY76` | 0.21368125927148499 | `0.00%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `V5` | `V5` | 1 | `=H19:H27` | 1.0404 |
| `AI5` | `AI13` | 13 | `=H29` | 14 |
| `AV5` | `AU19` | 2 | `=V5:V13` | 1.0404 |
| `BC5` | `BB19` | 2 | `=AI5:AI13` | 14 |
| `T6` | `T12` | 4 | `=F20` | 1.02 |
| `AT6` | `AS26` | 6 | `=T6` | 1.02 |
| `BA6` | `AZ26` | 7 | `=AG6` | 12 |
| `AR9` | `AR9` | 1 | `=Num0` | 1 |
| `H19` | `H27` | 9 | `=(1+tipo)^2` | 1.0404 |
| `V19` | `V39` | 3 | `=H19:H27/$V$5:$V$13` | 1 |
| `AI19` | `AI19` | 1 | `=H19:H27/AI5:AI13` | 0.07431428571428571 |
| `F20` | `F26` | 3 | `=(1+tipo)` | 1.02 |
| `T20` | `T40` | 3 | `=F20/$T$6` | 1 |
| `X20` | `X36` | 6 | `=(SUMPRODUCT(V19:V21,U19:U21)-T20)^2*10000` | 6.21120915620123e-14 |
| `AG20` | `AG26` | 3 | `=F20/$AG6` | 0.085 |
| `AK20` | `AK46` | 9 | `=(SUMPRODUCT(AI19:AI21,AH19:AH21)-AG20)^2` | 7.89237870235567e-16 |
| `R23` | `R23` | 1 | `=D23/Num0` | 1 |
| `T23` | `T43` | 3 | `=F23/$T$9` | 1 |
| `Z23` | `AM33` | 4 | `=(SUMPRODUCT(T20:T26,S20:S26)-R23)^2` | 5.067083709738656e-16 |
| `AE23` | `AE43` | 3 | `=D23/$AE$9` | 0.1 |
| `T26` | `T46` | 3 | `=F26/$T$12` | 1 |
| `Y27` | `Y27` | 1 | `=X20+X30+X39` | 7.179747143649025e-10 |
| `U29` | `AH29` | 2 | `=U19:U27` | 0.6799999942661007 |
| `Y29` | `Y29` | 1 | `=X23+X33+X42` | 1.9297353845202675e-08 |
| `AI29` | `AI39` | 2 | `=H29:H37/$AI$5:$AI$13` | 1 |
| `S30` | `AF36` | 6 | `=S20` | 0.5350001357348568 |
| `AG30` | `AG36` | 3 | `=F30/AG6` | 1 |
| `Y31` | `Y31` | 1 | `=X26+X36+X45` | 1.0343440063084721e-07 |
| `AL31` | `AL31` | 1 | `=(AK20+AK30+AK40)*100000` | 9.698928428503658e-09 |
| `AA32` | `AA32` | 1 | `=SUM(Z23:Z42)` | 6.662225511990449e-12 |
| `AN32` | `AN32` | 1 | `=SUM(AM23:AM42)*100000` | 1.5296487378637534e-07 |
| `R33` | `R43` | 2 | `=D33/$R$9` | 10 |
| `AL33` | `AL33` | 1 | `=(AK23+AK33+AK43)*100000` | 1.5396396174748075e-07 |
| `AL35` | `AL35` | 1 | `=(AK26+AK36+AK46)*100000` | 3.313722520090328e-08 |
| `U39` | `AH39` | 2 | `=U19:U27` | 0.6799999942661007 |
| `X39` | `X45` | 3 | `=(SUMPRODUCT(V39:V41,U39:U41)-T40)^2*10000` | 5.6055968274169296e-11 |
| `AV39` | `AV47` | 12 | `=BC5/AV5` | 13.456362937331795 |
| `S40` | `AF46` | 6 | `=S20` | 0.5350001357348568 |
| `AG40` | `AG46` | 3 | `=F40/AG6` | 0.5 |
| `Z42` | `AM42` | 2 | `=(SUMPRODUCT(T40:T46,S40:S46)-R43)^2` | 6.493671873882093e-12 |
| `AS49` | `AS49` | 1 | `=AR9/AY9` | 0.1 |
| `L52` | `L54` | 3 | `=($K$52*H19+$K$53*H29+$K$54*H39)` | 0.9999987504179932 |
| `M52` | `M60` | 9 | `=(L52-H52)^2` | 1.5614551916110167e-12 |
| `U52` | `AH52` | 2 | `=U19:U27` | 0.6799999942661007 |
| `V52` | `V52` | 1 | `=V63:V71/$V$5:$V$13` | 0.9611687812379854 |
| `AI52` | `AI52` | 1 | `=AI63:AI71/$AI$5:$AI$13` | 0.07142857142857142 |
| `F53` | `F59` | 3 | `=K52*F20+K53*F30+K54*F40` | 0.6666669815528037 |
| `N53` | `I65` | 4 | `=SUM(M52:M54)*100000` | 5.0631042780476705e-06 |
| `S53` | `AF59` | 6 | `=S20` | 0.5350001357348568 |
| `T53` | `AG59` | 6 | `=SUMPRODUCT(V52:V54,U52:U54)` | 0.6535947657305851 |
| `AS54` | `AS60` | 3 | `=AS20*AT40*$AS$49` | 0.6294119243939492 |
| `L55` | `L57` | 3 | `=($K$55*H22+$K$56*H32+$K$57*H42)` | 0.9999683771338713 |
| `D56` | `D56` | 1 | `=F64*D23+F65*D33+F66*D43` | 0.4163971407019902 |
| `R56` | `R56` | 1 | `=SUMPRODUCT(T53:T59,S53:S59)` | 0.4163957554555653 |
| `AE56` | `AE56` | 1 | `=SUMPRODUCT(AG53:AG59,AF20:AF26)` | 0.04163938066150331 |
| `L58` | `L60` | 3 | `=($K$58*H25+$K$59*H35+$K$60*H45)` | 0.9999910307854617 |
| `V63` | `V63` | 1 | `=H52:H60` | 1 |
| `AI63` | `AI63` | 1 | `=H52:H60` | 1 |
| `G64` | `G64` | 1 | `=($F$64*F20+$F$65*F30+$F$66*F40)` | 0.6666717869684312 |
| `H64` | `H64` | 1 | `=(G64-F53)^2` | 2.3092019353300013e-11 |
| `T64` | `AG70` | 7 | `=T53*T6` | 0.6666666610451968 |
| `G65` | `G65` | 1 | `=($F$64*F23+$F$65*F33+$F$66*F43)` | 0.3300514223333561 |
| `H65` | `H65` | 1 | `=(G65-F56)^2` | 8.379429762767308e-12 |
| `G66` | `G66` | 1 | `=($F$64*F26+$F$65*F36+$F$66*F46)` | 0.1336876662480877 |
| `H66` | `H66` | 1 | `=(G66-F59)^2` | 7.103224508544377e-14 |
| `R67` | `R67` | 1 | `=R56*Num0` | 0.4163957554555653 |
| `AS68` | `AS74` | 3 | `=AU19:AU21*AS20` | 0.36380008923206575 |
| `AV68` | `AV76` | 9 | `=AS68*AV39*$AS$49` | 0.48954260373403696 |
| `AY68` | `AY74` | 3 | `=AV68:AV70/AS54` | 0.7777777712193963 |

### Notas de celdas

- `L52`: jcontreras: observa que solver no ha conseguido resolver "exactamente" el sistema de ecuaciones

- `Q52`: todo este árbol está escrito en las unidades del numerario
- `V52`: 2. Escribimos los payoffs finales en términos del numerario

- `T53`: 3. El resto del árbol se calcula (hacia atrás) promediando con las probabilidades

- `Q63`: y éste, en las unidades originales. Compárese con el obtenido por replicación

- `V63`: 1. El dato es el payoff a vencimiento

- `R67`: 4. Los valores de este árbol se obtienen a partir del anterior multiplicando por los valores del numerario. Observa que coinciden (salvo detalle de precisión de solver) con los de los obtenidos por replicación

- `AE67`: jcontreras: observa que, aunque en el cálculo hemos usado unas probs distintas (pues el numerario era diferente), los precios obtenidos son los mismos

- `AS68`: El escenario (a,1) tiene la probabilidad producto de "llegar a a" por "llegar luego a 1"

## Textos en objetos de dibujo

```json
[
  {
    "part": "xl/drawings/drawing1.xml",
    "text": [
      "compárese con las probabiidades obtenidas antes"
    ]
  }
]
```

# XLS-012: BDT.xlsx

Original: [archivo raw](../../raw/fundamentos/sesioniii/bdt.xlsx). SHA-256: `c77c7ea47283b28716f27cca5367532309de44c744cf73cb18573eb16cf07cc2`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

Un nombre local prevalece sobre el nombre de libro al evaluar fórmulas de su hoja. Se incluyen los parámetros Solver, sin ejecutarlo.

| Nombre | Ámbito | Referencia | Oculto |
|---|---|---|---|
| `deltat` | `Sheet2` | `Sheet2!$B$7` | 0 |
| `deltat` | `libro` | `Sheet1!$B$7` | 0 |
| `Nom` | `Sheet2` | `Sheet2!$AA$27` | 0 |
| `Nom` | `libro` | `Sheet1!$AA$27` | 0 |
| `solver_adj` | `Sheet1` | `Sheet1!$C$10:$G$10` | 1 |
| `solver_adj` | `Sheet2` | `Sheet2!$AG$65:$AG$66` | 1 |
| `solver_cvg` | `Sheet1` | `0.0001` | 1 |
| `solver_cvg` | `Sheet2` | `0.0001` | 1 |
| `solver_drv` | `Sheet1` | `1` | 1 |
| `solver_drv` | `Sheet2` | `1` | 1 |
| `solver_eng` | `Sheet1` | `1` | 1 |
| `solver_eng` | `Sheet2` | `1` | 1 |
| `solver_est` | `Sheet1` | `1` | 1 |
| `solver_est` | `Sheet2` | `1` | 1 |
| `solver_itr` | `Sheet1` | `1000` | 1 |
| `solver_itr` | `Sheet2` | `1000` | 1 |
| `solver_lin` | `Sheet1` | `2` | 1 |
| `solver_lin` | `Sheet2` | `2` | 1 |
| `solver_mip` | `Sheet1` | `2147483647` | 1 |
| `solver_mip` | `Sheet2` | `2147483647` | 1 |
| `solver_mni` | `Sheet1` | `30` | 1 |
| `solver_mni` | `Sheet2` | `30` | 1 |
| `solver_mrt` | `Sheet1` | `0.075` | 1 |
| `solver_mrt` | `Sheet2` | `0.075` | 1 |
| `solver_msl` | `Sheet1` | `2` | 1 |
| `solver_msl` | `Sheet2` | `2` | 1 |
| `solver_neg` | `Sheet1` | `2` | 1 |
| `solver_neg` | `Sheet2` | `2` | 1 |
| `solver_nod` | `Sheet1` | `2147483647` | 1 |
| `solver_nod` | `Sheet2` | `2147483647` | 1 |
| `solver_num` | `Sheet1` | `0` | 1 |
| `solver_num` | `Sheet2` | `0` | 1 |
| `solver_nwt` | `Sheet1` | `1` | 1 |
| `solver_nwt` | `Sheet2` | `1` | 1 |
| `solver_opt` | `Sheet1` | `Sheet1!$T$16` | 1 |
| `solver_opt` | `Sheet2` | `Sheet2!$AK$69` | 1 |
| `solver_pre` | `Sheet1` | `0.000001` | 1 |
| `solver_pre` | `Sheet2` | `0.000001` | 1 |
| `solver_rbv` | `Sheet1` | `1` | 1 |
| `solver_rbv` | `Sheet2` | `1` | 1 |
| `solver_rlx` | `Sheet1` | `1` | 1 |
| `solver_rlx` | `Sheet2` | `1` | 1 |
| `solver_rsd` | `Sheet1` | `0` | 1 |
| `solver_rsd` | `Sheet2` | `0` | 1 |
| `solver_scl` | `Sheet1` | `2` | 1 |
| `solver_scl` | `Sheet2` | `2` | 1 |
| `solver_sho` | `Sheet1` | `2` | 1 |
| `solver_sho` | `Sheet2` | `2` | 1 |
| `solver_ssz` | `Sheet1` | `100` | 1 |
| `solver_ssz` | `Sheet2` | `100` | 1 |
| `solver_tim` | `Sheet1` | `1000` | 1 |
| `solver_tim` | `Sheet2` | `1000` | 1 |
| `solver_tol` | `Sheet1` | `5` | 1 |
| `solver_tol` | `Sheet2` | `0.05` | 1 |
| `solver_typ` | `Sheet1` | `3` | 1 |
| `solver_typ` | `Sheet2` | `3` | 1 |
| `solver_val` | `Sheet1` | `0` | 1 |
| `solver_val` | `Sheet2` | `0` | 1 |
| `solver_ver` | `Sheet1` | `3` | 1 |
| `solver_ver` | `Sheet2` | `3` | 1 |
| `strike` | `Sheet2` | `Sheet2!$Y$27` | 0 |
| `strike` | `libro` | `Sheet1!$Y$27` | 0 |
| `vola` | `Sheet2` | `Sheet2!$C$7` | 0 |
| `vola` | `libro` | `Sheet1!$C$7` | 0 |

## Hoja: Sheet1

Estado: `visible`. Rango usado: `A1:XFD88`. Celdas con contenido: 222. Fórmulas: 67. Familias: 20.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `XFD1` | . |
| `B4` | Para el ajuste Black-Derman-Toy con vola constante |
| `L5` | Calibración del modelo a la CCC |
| `B6` | delta |
| `C6` | volatilidad |
| `P6` | CCC del modelo |
| `L7` | instante |
| `M7` | tiempo |
| `N7` | descuentos de mercado |
| `Q8` | desc |
| `R8` | tipos |
| `T9` | errores |
| `B10` |  función U |
| `B12` | árbol de ruidos |
| `L22` | Instrumentos de mercado (bonos cupón cero de nominal 1) |
| `X22` | Uso del modelo para valoración de instrumentos |
| `C24` | tipos (continuos, plazo deltat) |
| `L24` | Bono de vencimiento 5*deltat |
| `X24` | Vamos a valorar un FRA (in advance/in arrears) y un caplet (in advance/in arrears) |
| `X25` | Todos pagan en función del tipo simple que se fije en tiempo 4*deltat |
| `X26` | El strike común es |
| `Z26` | El nominal común es |
| `X27` | K |
| `Z27` | Nom |
| `X29` | Exhibimos los flujos de los cuatro instrumentos (escritos como flujos de tiempo 4*deltat) |
| `X31` | tipos simples |
| `Y31` | FRA in arrears |
| `Z31` | FRA |
| `AA31` | caplet in arrears |
| `AB31` | caplet |
| `C33` | tipos (simples, plazo deltat) |
| `L34` | Bono de vencimiento 4*deltat |
| `X39` | Árbol de valoración del FRA in arrears |
| `L43` | Bono de vencimiento 3*deltat |
| `X47` | Árbol de valoración del FRA |
| `AD48` | un solver para calcular el strike de equilibrio del FRA |
| `AD50` | ese tipo de equlibrio debería ser (el tipo fwd) |
| `L51` | Bono de vencimiento 2*deltat |
| `X55` | Árbol de valoración del caplet in arrears |
| `AD55` | Cálculo de la cartera de réplica para el FRA |
| `AD57` | Lo hacemos solo en el nodo superior de tiempo 4 |
| `AD58` | En la cartera de réplica solo intervendrán el bono 4 y el bono 5 (los instrumentos "vivos" en tiempo 4) |
| `L59` | Bono de vencimiento 1*deltat |
| `AD60` | valores del FRA |
| `AG60` | valores del bono 4 |
| `AJ60` | valores del bono 5 |
| `X63` | Árbol de valoración del caplet |
| `AD65` | unidades del bono 4 |
| `AF65` | alpha |
| `AD66` | unidades del bono 5 |
| `AF66` | beta |
| `AJ67` | errores |
| `AF68` | flujos cartera de réplica |
| `AD72` | Coste de la cartera de réplica |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `C9` | 0 | `General` |
| `D9` | 1 | `General` |
| `E9` | 2 | `General` |
| `F9` | 3 | `General` |
| `G9` | 4 | `General` |
| `L10` | 0 | `General` |
| `N10` | 1 | `0.000%` |
| `P10` | 0 | `General` |
| `L11` | 1 | `General` |
| `N11` | 0.995 | `0.000%` |
| `P11` | 1 | `General` |
| `C12` | 0 | `General` |
| `D12` | 1 | `General` |
| `E12` | 2 | `General` |
| `F12` | 3 | `General` |
| `G12` | 4 | `General` |
| `L12` | 2 | `General` |
| `N12` | 0.991 | `0.000%` |
| `P12` | 2 | `General` |
| `L13` | 3 | `General` |
| `N13` | 0.989 | `0.000%` |
| `P13` | 3 | `General` |
| `L14` | 4 | `General` |
| `N14` | 0.98 | `0.000%` |
| `P14` | 4 | `General` |
| `L15` | 5 | `General` |
| `N15` | 0.9745 | `0.000%` |
| `P15` | 5 | `General` |
| `C25` | 0 | `General` |
| `D25` | 1 | `General` |
| `E25` | 2 | `General` |
| `F25` | 3 | `General` |
| `G25` | 4 | `General` |
| `L25` | 0 | `General` |
| `M25` | 1 | `General` |
| `N25` | 2 | `General` |
| `O25` | 3 | `General` |
| `P25` | 4 | `General` |
| `Q25` | 5 | `General` |
| `C34` | 0 | `General` |
| `D34` | 1 | `General` |
| `E34` | 2 | `General` |
| `F34` | 3 | `General` |
| `G34` | 4 | `General` |
| `L35` | 0 | `General` |
| `M35` | 1 | `General` |
| `N35` | 2 | `General` |
| `O35` | 3 | `General` |
| `P35` | 4 | `General` |
| `X40` | 0 | `General` |
| `Y40` | 1 | `General` |
| `Z40` | 2 | `General` |
| `AA40` | 3 | `General` |
| `AB40` | 4 | `General` |
| `AB42` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB43` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `L44` | 0 | `General` |
| `M44` | 1 | `General` |
| `N44` | 2 | `General` |
| `O44` | 3 | `General` |
| `AB44` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB45` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X48` | 0 | `General` |
| `Y48` | 1 | `General` |
| `Z48` | 2 | `General` |
| `AA48` | 3 | `General` |
| `AB48` | 4 | `General` |
| `AB50` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB51` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `L52` | 0 | `General` |
| `M52` | 1 | `General` |
| `N52` | 2 | `General` |
| `AB52` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB53` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X56` | 0 | `General` |
| `Y56` | 1 | `General` |
| `Z56` | 2 | `General` |
| `AA56` | 3 | `General` |
| `AB56` | 4 | `General` |
| `AB58` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB59` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `L60` | 0 | `General` |
| `M60` | 1 | `General` |
| `AB60` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB61` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X64` | 0 | `General` |
| `Y64` | 1 | `General` |
| `Z64` | 2 | `General` |
| `AA64` | 3 | `General` |
| `AB64` | 4 | `General` |
| `AG65` | 9999.825817380464 | `General` |
| `AB66` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AG66` | -10056.263631392192 | `General` |
| `AB67` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB68` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB69` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `B7` | `B7` | 1 | `=1/4` | 0.25 |
| `M10` | `M15` | 6 | `=L10*deltat` | 0 |
| `X41` | `AA44` | 10 | `=AVERAGE(Y41:Y42)*EXP(-C26*deltat)` | 0 |
| `AB41` | `AB41` | 1 | `=Y33:Y37` | 0 |
| `X49` | `AA52` | 10 | `=AVERAGE(Y49:Y50)*EXP(-C26*deltat)` | 0 |
| `AB49` | `AB49` | 1 | `=Z33:Z37` | 0 |
| `AD49` | `AD49` | 1 | `=X49*100000000000` | 0 |
| `AD51` | `AD51` | 1 | `=(Q14/Q15-1)/deltat` | #DIV/0! |
| `X57` | `AA60` | 10 | `=AVERAGE(Y57:Y58)*EXP(-C26*deltat)` | 0 |
| `AB57` | `AB57` | 1 | `=AA33:AA37` | 0 |
| `AE61` | `AE62` | 2 | `=AB49` | 0 |
| `AG61` | `AH62` | 3 | `=O36` | 0 |
| `AJ61` | `AK62` | 3 | `=O26` | 0 |
| `X65` | `AA68` | 10 | `=AVERAGE(Y65:Y66)*EXP(-C26*deltat)` | 0 |
| `AB65` | `AB65` | 1 | `=AB33:AB37` | 0 |
| `AG68` | `AG68` | 1 | `=AG65*AH61+AG66*AK61` | 0 |
| `AJ68` | `AJ69` | 2 | `=(AG68-AE61)^2` | 0 |
| `AG69` | `AG69` | 1 | `=AG65*AH62+AG66*AK62` | 0 |
| `AK69` | `AK69` | 1 | `=SUM(AJ68:AJ69)*10000000000` | 0 |
| `AG72` | `AG72` | 1 | `=AG65*AG61+AG66*AJ61` | 0 |

### Notas de celdas

- `C7`: jcontreras: dato básico del modelo
- `G10`: solver fijará estos valores (que son ajustes de convexidad)

- `T16`: jcontreras: solver fija los valores de la función U (para cada dato de volatilidad) de manera que los descuentos del modelo coincidan con los de mercado

- `Y27`: jcontreras: el strike elegido es el que hace que el FRA valga hoy 0

- `Z33`: es un pago de tiempo 5*deltat, que descontamos para hacerlo de tiempo 4*deltat

- `X41`: jcontreras: este precio depende del valor de la volatilidad (!!)

- `X49`: jcontreras: este precio no depende del dato de volatilidad

- `X65`: jcontreras: el precio del caplet (y el de la versión in arrears) depende de la volatilidad 

- `AG65`: calculados con solver

- `AG72`: compara con el valor de AA47


### Errores guardados

Se detectan 1 celdas de error. No se han corregido.

```json
[
  {
    "cell": "AD51",
    "value": "#DIV/0!"
  }
]
```

## Hoja: Sheet2

Estado: `hidden`. Rango usado: `A1:AK88`. Celdas con contenido: 366. Fórmulas: 183. Familias: 42.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `B4` | Para el ajuste Black-Derman-Toy con vola constante |
| `L5` | Calibración del modelo a la CCC |
| `B6` | delta |
| `C6` | volatilidad |
| `P6` | CCC del modelo |
| `L7` | instante |
| `M7` | tiempo |
| `N7` | descuentos de mercado |
| `Q8` | desc |
| `R8` | tipos |
| `T9` | errores |
| `B10` |  función U |
| `B12` | árbol de ruidos |
| `L22` | Instrumentos de mercado (bonos cupón cero de nominal 1) |
| `X22` | Uso del modelo para valoración de instrumentos |
| `C24` | tipos (continuos, plazo deltat) |
| `L24` | Bono de vencimiento 5*deltat |
| `X24` | Vamos a valorar un FRA (in advance/in arrears) y un caplet (in advance/in arrears) |
| `X25` | Todos pagan en función del tipo simple que se fije en tiempo 4*deltat |
| `X26` | El strike común es |
| `Z26` | El nominal común es |
| `X27` | K |
| `Z27` | Nom |
| `X29` | Exhibimos los flujos de los cuatro instrumentos (escritos como flujos de tiempo 4*deltat) |
| `X31` | tipos simples |
| `Y31` | FRA in arrears |
| `Z31` | FRA |
| `AA31` | caplet in arrears |
| `AB31` | caplet |
| `C33` | tipos (simples, plazo deltat) |
| `L34` | Bono de vencimiento 4*deltat |
| `X39` | Árbol de valoración del FRA in arrears |
| `L43` | Bono de vencimiento 3*deltat |
| `X47` | Árbol de valoración del FRA |
| `AD48` | un solver para calcular el strike de equilibrio del FRA |
| `AD50` | ese tipo de equlibrio debería ser (el tipo fwd) |
| `L51` | Bono de vencimiento 2*deltat |
| `X55` | Árbol de valoración del caplet in arrears |
| `AD55` | Cálculo de la cartera de réplica para el FRA |
| `AD57` | Lo hacemos solo en el nodo superior de tiempo 4 |
| `AD58` | En la cartera de réplica solo intervendrán el bono 4 y el bono 5 (los instrumentos "vivos" en tiempo 4) |
| `L59` | Bono de vencimiento 1*deltat |
| `AD60` | valores del FRA |
| `AG60` | valores del bono 4 |
| `AJ60` | valores del bono 5 |
| `X63` | Árbol de valoración del caplet |
| `AD65` | unidades del bono 4 |
| `AF65` | alpha |
| `AD66` | unidades del bono 5 |
| `AF66` | beta |
| `AJ67` | errores |
| `AF68` | flujos cartera de réplica |
| `AD72` | Coste de la cartera de réplica |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `C7` | 0.45 | `0%` |
| `C9` | 0 | `General` |
| `D9` | 1 | `General` |
| `E9` | 2 | `General` |
| `F9` | 3 | `General` |
| `G9` | 4 | `General` |
| `C10` | 0.020049708073236812 | `0.000%` |
| `D10` | 0.01571488104376531 | `0.000%` |
| `E10` | 0.007687305613161145 | `0.000%` |
| `F10` | 0.03395233237178417 | `0.000%` |
| `G10` | 0.020410740854450656 | `0.000%` |
| `L10` | 0 | `General` |
| `N10` | 1 | `0.000%` |
| `P10` | 0 | `General` |
| `Q10` | 1 | `0.000%` |
| `L11` | 1 | `General` |
| `N11` | 0.995 | `0.000%` |
| `P11` | 1 | `General` |
| `C12` | 0 | `General` |
| `D12` | 1 | `General` |
| `E12` | 2 | `General` |
| `F12` | 3 | `General` |
| `G12` | 4 | `General` |
| `L12` | 2 | `General` |
| `N12` | 0.991 | `0.000%` |
| `P12` | 2 | `General` |
| `C13` | 0 | `0%` |
| `L13` | 3 | `General` |
| `N13` | 0.989 | `0.000%` |
| `P13` | 3 | `General` |
| `L14` | 4 | `General` |
| `N14` | 0.98 | `0.000%` |
| `P14` | 4 | `General` |
| `L15` | 5 | `General` |
| `N15` | 0.9745 | `0.000%` |
| `P15` | 5 | `General` |
| `C25` | 0 | `General` |
| `D25` | 1 | `General` |
| `E25` | 2 | `General` |
| `F25` | 3 | `General` |
| `G25` | 4 | `General` |
| `L25` | 0 | `General` |
| `M25` | 1 | `General` |
| `N25` | 2 | `General` |
| `O25` | 3 | `General` |
| `P25` | 4 | `General` |
| `Q25` | 5 | `General` |
| `Q26` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `Q27` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `Y27` | 0.022575844936059148 | `0.0000000%` |
| `AA27` | 10000 | `#,##0.00\ "€"` |
| `Q28` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `Q29` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `Q30` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `Q31` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `C34` | 0 | `General` |
| `D34` | 1 | `General` |
| `E34` | 2 | `General` |
| `F34` | 3 | `General` |
| `G34` | 4 | `General` |
| `X34` | 0.03213883927057548 | `0.0000%` |
| `L35` | 0 | `General` |
| `M35` | 1 | `General` |
| `N35` | 2 | `General` |
| `O35` | 3 | `General` |
| `P35` | 4 | `General` |
| `X35` | 0.020462904334094034 | `0.0000%` |
| `P36` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X36` | 0.01303565797560946 | `0.0000%` |
| `P37` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X37` | 0.008307001825331284 | `0.0000%` |
| `P38` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `P39` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `P40` | 1 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X40` | 0 | `General` |
| `Y40` | 1 | `General` |
| `Z40` | 2 | `General` |
| `AA40` | 3 | `General` |
| `AB40` | 4 | `General` |
| `AB42` | 23.90748583629083 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB43` | -5.282351504912785 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `L44` | 0 | `General` |
| `M44` | 1 | `General` |
| `N44` | 2 | `General` |
| `O44` | 3 | `General` |
| `AB44` | -23.85046740112422 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `O45` | 1 | `_-* #,##0.00000\ "€"_-;\-* #,##0.00000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB45` | -35.67210777681966 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `O46` | 1 | `_-* #,##0.00000\ "€"_-;\-* #,##0.00000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `O47` | 1 | `_-* #,##0.00000\ "€"_-;\-* #,##0.00000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `O48` | 1 | `_-* #,##0.00000\ "€"_-;\-* #,##0.00000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X48` | 0 | `General` |
| `Y48` | 1 | `General` |
| `Z48` | 2 | `General` |
| `AA48` | 3 | `General` |
| `AB48` | 4 | `General` |
| `AB50` | 23.71692720840511 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB51` | -5.255465980515193 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `L52` | 0 | `General` |
| `M52` | 1 | `General` |
| `N52` | 2 | `General` |
| `AB52` | -23.772993248862065 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `N53` | 1 | `_-* #,##0.00000\ "€"_-;\-* #,##0.00000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB53` | -35.59817924183456 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `N54` | 1 | `_-* #,##0.00000\ "€"_-;\-* #,##0.00000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `N55` | 1 | `_-* #,##0.00000\ "€"_-;\-* #,##0.00000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X56` | 0 | `General` |
| `Y56` | 1 | `General` |
| `Z56` | 2 | `General` |
| `AA56` | 3 | `General` |
| `AB56` | 4 | `General` |
| `AB58` | 23.90748583629083 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB59` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `L60` | 0 | `General` |
| `M60` | 1 | `General` |
| `AB60` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `M61` | 1 | `_-* #,##0.000000\ "€"_-;\-* #,##0.000000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB61` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `M62` | 1 | `_-* #,##0.000000\ "€"_-;\-* #,##0.000000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `X64` | 0 | `General` |
| `Y64` | 1 | `General` |
| `Z64` | 2 | `General` |
| `AA64` | 3 | `General` |
| `AB64` | 4 | `General` |
| `AG65` | 9999.825817380464 | `General` |
| `AB66` | 23.71692720840511 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AG66` | -10056.263631392192 | `General` |
| `AB67` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB68` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `AB69` | 0 | `_-* #,##0.0000\ "€"_-;\-* #,##0.0000\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `B7` | `B7` | 1 | `=1/4` | 0.25 |
| `M10` | `M15` | 6 | `=L10*deltat` | 0 |
| `Q11` | `Q11` | 1 | `=L61` | 0.9950001142312155 |
| `R11` | `R15` | 5 | `=(1/(P11*deltat))*LN(1/Q11)` | 0.02004970807323649 |
| `T11` | `T15` | 5 | `=(N11-Q11)^2` | 1.3048770591569856e-14 |
| `Q12` | `Q12` | 1 | `=L53` | 0.9910001275695014 |
| `D13` | `G13` | 4 | `=C13+vola*SQRT(deltat)` | 0.225 |
| `Q13` | `Q13` | 1 | `=L45` | 0.9890001612361484 |
| `D14` | `G17` | 10 | `=C13-vola*SQRT(deltat)` | -0.225 |
| `Q14` | `Q14` | 1 | `=L36` | 0.9800000660788983 |
| `Q15` | `Q15` | 1 | `=L26` | 0.9745000257112376 |
| `T16` | `T16` | 1 | `=SUM(T11:T15)*10000000` | 6.034733238780664e-07 |
| `C26` | `G30` | 15 | `=C$10*EXP(C13)` | 0.020049708073236812 |
| `L26` | `P30` | 15 | `=AVERAGE(M26:M27)*EXP(-C26*deltat)` | 0.9745000257112376 |
| `X33` | `X33` | 1 | `=G35:G39` | 0.05051867794415266 |
| `Y33` | `Y37` | 5 | `=(X33-strike)*deltat*Nom` | 69.85708252023377 |
| `Z33` | `Z37` | 5 | `=Y33*EXP(-G26*deltat)` | 68.98581448407477 |
| `AA33` | `AA37` | 5 | `=MAX(X33-strike,0)*deltat*Nom` | 69.85708252023377 |
| `AB33` | `AB37` | 5 | `=AA33*EXP(-G26*deltat)` | 68.98581448407477 |
| `C35` | `G39` | 15 | `=(EXP(C26*deltat)-1)/deltat` | 0.02010004098400575 |
| `L36` | `O39` | 10 | `=AVERAGE(M36:M37)*EXP(-C26*deltat)` | 0.9800000660788983 |
| `X41` | `AA44` | 10 | `=AVERAGE(Y41:Y42)*EXP(-C26*deltat)` | 0.0658732940049933 |
| `AB41` | `AB41` | 1 | `=Y33:Y37` | 69.85708252023377 |
| `L45` | `N47` | 6 | `=AVERAGE(M45:M46)*EXP(-C26*deltat)` | 0.9890001612361484 |
| `X49` | `AA52` | 10 | `=AVERAGE(Y49:Y50)*EXP(-C26*deltat)` | 0 |
| `AB49` | `AB49` | 1 | `=Z33:Z37` | 68.98581448407477 |
| `AD49` | `AD49` | 1 | `=X49*100000000000` | 0 |
| `AD51` | `AD51` | 1 | `=(Q14/Q15-1)/deltat` | 0.022575844936059575 |
| `L53` | `M54` | 3 | `=AVERAGE(M53:M54)*EXP(-C26*deltat)` | 0.9910001275695014 |
| `X57` | `AA60` | 10 | `=AVERAGE(Y57:Y58)*EXP(-C26*deltat)` | 10.07326655416573 |
| `AB57` | `AB57` | 1 | `=AA33:AA37` | 69.85708252023377 |
| `L61` | `L61` | 1 | `=AVERAGE(M61:M62)*EXP(-C26*deltat)` | 0.9950001142312155 |
| `AE61` | `AE62` | 2 | `=AB49` | 68.98581448407477 |
| `AG61` | `AH62` | 3 | `=O36` | 0.9834673149589154 |
| `AJ61` | `AK62` | 3 | `=O26` | 0.9734148932139217 |
| `X65` | `AA68` | 10 | `=AVERAGE(Y65:Y66)*EXP(-C26*deltat)` | 9.973895672629494 |
| `AB65` | `AB65` | 1 | `=AB33:AB37` | 68.98581448407477 |
| `AG68` | `AG68` | 1 | `=AG65*AH61+AG66*AK61` | 68.98541795165329 |
| `AJ68` | `AJ69` | 2 | `=(AG68-AE61)^2` | 1.5723796128168455e-07 |
| `AG69` | `AG69` | 1 | `=AG65*AH62+AG66*AK62` | 23.7173228511474 |
| `AK69` | `AK69` | 1 | `=SUM(AJ68:AJ69)*10000000000` | 3137.71140808948 |
| `AG72` | `AG72` | 1 | `=AG65*AG61+AG66*AJ61` | 45.585057793330634 |

### Notas de celdas

- `C7`: jcontreras: dato básico del modelo
- `G10`: solver fijará estos valores (que son ajustes de convexidad)

- `T16`: jcontreras: solver fija los valores de la función U (para cada dato de volatilidad) de manera que los descuentos del modelo coincidan con los de mercado

- `Y27`: jcontreras: el strike elegido es el que hace que el FRA valga hoy 0

- `Z33`: es un pago de tiempo 5*deltat, que descontamos para hacerlo de tiempo 4*deltat

- `X41`: jcontreras: este precio depende del valor de la volatilidad (!!)

- `X49`: jcontreras: este precio no depende del dato de volatilidad

- `X65`: jcontreras: el precio del caplet (y el de la versión in arrears) depende de la volatilidad 

- `AG65`: calculados con solver

- `AG72`: compara con el valor de AA47

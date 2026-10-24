# XLS-009: Americana con dividendos.xlsx

Original: [archivo raw](../../raw/fundamentos/sesioniii/americana-con-dividendos.xlsx). SHA-256: `9e8c745e20fb66a5e798a746c0c20c19d21a9ac448bb1811f35bd108de351539`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

Un nombre local prevalece sobre el nombre de libro al evaluar fórmulas de su hoja. Se incluyen los parámetros Solver, sin ejecutarlo.

| Nombre | Ámbito | Referencia | Oculto |
|---|---|---|---|
| `d` | `Hoja2` | `Hoja2!$C$15` | 0 |
| `d` | `libro` | `Hoja1!$C$15` | 0 |
| `Deltat` | `Hoja2` | `Hoja2!$C$9` | 0 |
| `Deltat` | `libro` | `Hoja1!$C$9` | 0 |
| `Descuento` | `Hoja2` | `Hoja2!$C$10` | 0 |
| `Descuento` | `libro` | `Hoja1!$C$10` | 0 |
| `dividendo1` | `Hoja2` | `Hoja2!$F$6` | 0 |
| `dividendo1` | `libro` | `Hoja1!$F$6` | 0 |
| `dividendo2` | `Hoja2` | `Hoja2!$H$6` | 0 |
| `dividendo2` | `libro` | `Hoja1!$H$6` | 0 |
| `p` | `Hoja2` | `Hoja2!$C$13` | 0 |
| `p` | `libro` | `Hoja1!$C$13` | 0 |
| `probs` | `Hoja2` | `Hoja2!$P$20:$P$32` | 0 |
| `probs` | `libro` | `Hoja1!$P$20:$P$32` | 0 |
| `S0` | `Hoja2` | `Hoja2!$C$6` | 0 |
| `S0` | `libro` | `Hoja1!$C$6` | 0 |
| `solver_adj` | `Hoja1` | `Hoja1!#REF!` | 1 |
| `solver_adj` | `Hoja2` | `Hoja2!#REF!` | 1 |
| `solver_cvg` | `Hoja1` | `0.0001` | 1 |
| `solver_cvg` | `Hoja2` | `0.0001` | 1 |
| `solver_drv` | `Hoja1` | `1` | 1 |
| `solver_drv` | `Hoja2` | `1` | 1 |
| `solver_est` | `Hoja1` | `1` | 1 |
| `solver_est` | `Hoja2` | `1` | 1 |
| `solver_itr` | `Hoja1` | `100` | 1 |
| `solver_itr` | `Hoja2` | `100` | 1 |
| `solver_lin` | `Hoja1` | `2` | 1 |
| `solver_lin` | `Hoja2` | `2` | 1 |
| `solver_neg` | `Hoja1` | `2` | 1 |
| `solver_neg` | `Hoja2` | `2` | 1 |
| `solver_num` | `Hoja1` | `0` | 1 |
| `solver_num` | `Hoja2` | `0` | 1 |
| `solver_nwt` | `Hoja1` | `1` | 1 |
| `solver_nwt` | `Hoja2` | `1` | 1 |
| `solver_opt` | `Hoja1` | `Hoja1!$F$10` | 1 |
| `solver_opt` | `Hoja2` | `Hoja2!$F$10` | 1 |
| `solver_pre` | `Hoja1` | `0.000001` | 1 |
| `solver_pre` | `Hoja2` | `0.000001` | 1 |
| `solver_scl` | `Hoja1` | `2` | 1 |
| `solver_scl` | `Hoja2` | `2` | 1 |
| `solver_sho` | `Hoja1` | `2` | 1 |
| `solver_sho` | `Hoja2` | `2` | 1 |
| `solver_tim` | `Hoja1` | `100` | 1 |
| `solver_tim` | `Hoja2` | `100` | 1 |
| `solver_tol` | `Hoja1` | `0.05` | 1 |
| `solver_tol` | `Hoja2` | `0.05` | 1 |
| `solver_typ` | `Hoja1` | `3` | 1 |
| `solver_typ` | `Hoja2` | `3` | 1 |
| `solver_val` | `Hoja1` | `0` | 1 |
| `solver_val` | `Hoja2` | `0` | 1 |
| `strike` | `Hoja2` | `Hoja2!$C$93` | 0 |
| `strike` | `libro` | `Hoja1!$C$93` | 0 |
| `Tiempo1` | `Hoja2` | `Hoja2!$F$5` | 0 |
| `Tiempo1` | `libro` | `Hoja1!$F$5` | 0 |
| `Tiempo2` | `Hoja2` | `Hoja2!$H$5` | 0 |
| `Tiempo2` | `libro` | `Hoja1!$H$5` | 0 |
| `tipo` | `Hoja2` | `Hoja2!$C$4` | 0 |
| `tipo` | `libro` | `Hoja1!$C$4` | 0 |
| `u` | `Hoja2` | `Hoja2!$C$14` | 0 |
| `u` | `libro` | `Hoja1!$C$14` | 0 |
| `vola` | `Hoja2` | `Hoja2!$C$5` | 0 |
| `vola` | `libro` | `Hoja1!$C$5` | 0 |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `A1:XFD150`. Celdas con contenido: 643. Fórmulas: 463. Familias: 29.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `XFD1` | . |
| `B3` | Datos de mercado |
| `B4` | Tipo de interés (continuo) |
| `E4` | dividendos |
| `B5` | Volatilidad |
| `E5` | Tiempo1 |
| `G5` | Tiempo2 |
| `B6` | Cotización hoy |
| `E6` | Div1 |
| `G6` | Div2 |
| `F7` | meses |
| `H7` | meses |
| `B8` | Datos del modelo |
| `B9` | Deltat |
| `B10` | Descuento periodo |
| `B12` | Parámetros del modelo |
| `B13` | p |
| `J13` | ¿martingala? |
| `L13` | volatilidad anual |
| `B14` | u |
| `J14` | una mínima comprobación |
| `B15` | d |
| `B17` | Árbol de evolución de S* |
| `P18` | probabilidades |
| `S18` | rendimientos anuales |
| `B37` | Proceso de dividendos |
| `B44` | Árbol de evolución de la cotización S |
| `S45` | rendimientos anuales |
| `B53` | ¿martingala? |
| `D53` | volatilidad anual |
| `B54` | una mínima comprobación |
| `B62` | Árbol de evolución del valor de la inversión en el activo |
| `B70` | pequeña comprobación de martingala |
| `A84` | senda S* |
| `A85` | senda S |
| `A86` | senda inversión |
| `A87` | dividendos |
| `B91` | Valoración de una put americana |
| `B92` | vencimiento |
| `B93` | strike |
| `B95` | Árbol de evolución de la opción |
| `B111` | Valoración de una call europea |
| `B112` | vencimiento |
| `B113` | strike |
| `B115` | Árbol de evolución de la opción |
| `B132` | Valoración de una call americana |
| `B133` | vencimiento |
| `B134` | strike |
| `B136` | Árbol de evolución de la opción |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `C4` | 0.006 | `0.0%` |
| `C5` | 0.4 | `0%` |
| `F5` | 2.5 | `General` |
| `H5` | 9.5 | `General` |
| `C6` | 80 | `General` |
| `F6` | 1.5 | `General` |
| `H6` | 2 | `General` |
| `C13` | 0.5 | `0.00%` |
| `B18` | 0 | `General` |
| `C18` | 1 | `General` |
| `D18` | 2 | `General` |
| `E18` | 3 | `General` |
| `F18` | 4 | `General` |
| `G18` | 5 | `General` |
| `H18` | 6 | `General` |
| `I18` | 7 | `General` |
| `J18` | 8 | `General` |
| `K18` | 9 | `General` |
| `L18` | 10 | `General` |
| `M18` | 11 | `General` |
| `N18` | 12 | `General` |
| `Q20` | 12 | `General` |
| `Q21` | 11 | `General` |
| `Q22` | 10 | `General` |
| `Q23` | 9 | `General` |
| `Q24` | 8 | `General` |
| `Q25` | 7 | `General` |
| `Q26` | 6 | `General` |
| `Q27` | 5 | `General` |
| `Q28` | 4 | `General` |
| `Q29` | 3 | `General` |
| `Q30` | 2 | `General` |
| `Q31` | 1 | `General` |
| `Q32` | 0 | `General` |
| `B38` | 0 | `General` |
| `C38` | 1 | `General` |
| `D38` | 2 | `General` |
| `E38` | 3 | `General` |
| `F38` | 4 | `General` |
| `G38` | 5 | `General` |
| `H38` | 6 | `General` |
| `I38` | 7 | `General` |
| `J38` | 8 | `General` |
| `K38` | 9 | `General` |
| `L38` | 10 | `General` |
| `M38` | 11 | `General` |
| `N38` | 12 | `General` |
| `B45` | 0 | `General` |
| `C45` | 1 | `General` |
| `D45` | 2 | `General` |
| `E45` | 3 | `General` |
| `F45` | 4 | `General` |
| `G45` | 5 | `General` |
| `H45` | 6 | `General` |
| `I45` | 7 | `General` |
| `J45` | 8 | `General` |
| `K45` | 9 | `General` |
| `L45` | 10 | `General` |
| `M45` | 11 | `General` |
| `N45` | 12 | `General` |
| `B63` | 0 | `General` |
| `C63` | 1 | `General` |
| `D63` | 2 | `General` |
| `E63` | 3 | `General` |
| `F63` | 4 | `General` |
| `G63` | 5 | `General` |
| `H63` | 6 | `General` |
| `I63` | 7 | `General` |
| `J63` | 8 | `General` |
| `K63` | 9 | `General` |
| `L63` | 10 | `General` |
| `M63` | 11 | `General` |
| `N63` | 12 | `General` |
| `B80` | 0 | `General` |
| `C80` | 1 | `General` |
| `D80` | 2 | `General` |
| `E80` | 3 | `General` |
| `F80` | 4 | `General` |
| `G80` | 5 | `General` |
| `H80` | 6 | `General` |
| `I80` | 7 | `General` |
| `J80` | 8 | `General` |
| `K80` | 9 | `General` |
| `L80` | 10 | `General` |
| `M80` | 11 | `General` |
| `N80` | 12 | `General` |
| `C92` | 1 | `General` |
| `C93` | 84 | `General` |
| `B96` | 0 | `General` |
| `C96` | 1 | `General` |
| `D96` | 2 | `General` |
| `E96` | 3 | `General` |
| `F96` | 4 | `General` |
| `G96` | 5 | `General` |
| `H96` | 6 | `General` |
| `I96` | 7 | `General` |
| `J96` | 8 | `General` |
| `K96` | 9 | `General` |
| `L96` | 10 | `General` |
| `M96` | 11 | `General` |
| `N96` | 12 | `General` |

Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):

| Columna | Primera / última celda | N | Primer / último valor |
|---|---|---:|---|
| C | `C112` / `C137` | 4 | 1 / 1 |
| B | `B116` / `B137` | 2 | 0 / 0 |
| D | `D116` / `D137` | 2 | 2 / 2 |
| E | `E116` / `E137` | 2 | 3 / 3 |
| F | `F116` / `F137` | 2 | 4 / 4 |
| G | `G116` / `G137` | 2 | 5 / 5 |
| H | `H116` / `H137` | 2 | 6 / 6 |
| I | `I116` / `I137` | 2 | 7 / 7 |
| J | `J116` / `J137` | 2 | 8 / 8 |
| K | `K116` / `K137` | 2 | 9 / 9 |
| L | `L116` / `L137` | 2 | 10 / 10 |
| M | `M116` / `M137` | 2 | 11 / 11 |
| N | `N116` / `N137` | 2 | 12 / 12 |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `C9` | `C9` | 1 | `=1/12` | 0.08333333333333333 |
| `C10` | `C10` | 1 | `=+EXP(-tipo*Deltat)` | 0.9995001249791693 |
| `C14` | `C14` | 1 | `=EXP(tipo*Deltat)*EXP(vola*SQRT(Deltat))*2/(EXP(vola*SQRT(Deltat))+EXP(-vola*SQRT(Deltat)))` | 1.115517195155658 |
| `C15` | `C15` | 1 | `=EXP(tipo*Deltat)*EXP(-vola*SQRT(Deltat))*2/(EXP(vola*SQRT(Deltat))+EXP(-vola*SQRT(Deltat)))` | 0.8854830548860136 |
| `J15` | `J15` | 1 | `=SUMPRODUCT(N20:N32,probs)*Descuento^12` | 0 |
| `L15` | `L15` | 1 | `=SQRT(SUMPRODUCT(S20:S32^2,probs)-SUMPRODUCT(S20:S32,probs)^2)` | #NUM! |
| `B19` | `N64` | 52 | `=B18*Deltat` | 0 |
| `P20` | `P32` | 13 | `=BINOMDIST(Q20,12,p,FALSE)` | 0.00024414062500000016 |
| `S20` | `S59` | 26 | `=LN(N20/S0)` | #NUM! |
| `B55` | `B55` | 1 | `=SUMPRODUCT(N47:N59,P20:P32)*Descuento^12` | 0 |
| `D55` | `D55` | 1 | `=SQRT(SUMPRODUCT(S47:S59^2,probs)-SUMPRODUCT(S47:S59,probs)^2)` | #NUM! |
| `B71` | `B71` | 1 | `=SUMPRODUCT(N65:N77,P20:P32)*Descuento^12` | 0 |
| `C81` | `N81` | 12 | `=IF(RAND()<p,0,1)` | 1 |
| `C82` | `N82` | 12 | `=IF(C81=0,"sube","baja")` | baja |
| `C83` | `N83` | 12 | `=SUM($C$81:C81)` | 1 |
| `B84` | `B84` | 1 | `=B20` | 0 |
| `C84` | `N84` | 12 | `=OFFSET(C20,C83,0)` | 0 |
| `B85` | `B85` | 1 | `=B47` | 0 |
| `C85` | `N85` | 12 | `=OFFSET(C47,C83,0)` | 0 |
| `B86` | `B86` | 1 | `=B65` | 0 |
| `C86` | `N86` | 12 | `=OFFSET(C65,C83,0)` | 0 |
| `B87` | `N87` | 13 | `=B40` | 0 |
| `B97` | `M108` | 78 | `=MAX(MAX(strike-B47,0),Descuento*(p*C97+(1-p)*C98))` | 84 |
| `N97` | `N109` | 13 | `=MAX(strike-N47,0)` | 84 |
| `C113` | `C134` | 2 | `=strike` | 84 |
| `B117` | `M128` | 78 | `=Descuento*(p*C117+(1-p)*C118)` | 0 |
| `N117` | `N129` | 13 | `=MAX(N47-strike,0)` | 0 |
| `B138` | `M149` | 78 | `=MAX(Descuento*(p*C138+(1-p)*C139),MAX(B47-strike,0))` | 0 |
| `N138` | `N150` | 13 | `=MAX(N47-strike,0)` | 0 |

### Notas de celdas

- `B20`: la evolución parte de la cotización de hoy, a la que le restamos el valor actual de los dividendos futuros

- `B55`: la evolución de S no es martingala

- `D55`: pero acumula la volatilidad correcta

- `E65`: coincide con la cotización hasta el primer pago de dividendo

- `B138`: observa que la call americana ya es más valiosa que la correspondiente europea (por la presencia de los dividendos)


### Gráficos y rangos de origen

```json
[
  {
    "type": "LineChart",
    "title": "",
    "series": [
      {
        "val": "Hoja1!$B$40:$N$40",
        "cat": "Hoja1!$B$39:$N$39"
      }
    ]
  }
]
```

### Errores guardados

Se detectan 28 celdas de error. No se han corregido.

```json
[
  {
    "cell": "L15",
    "value": "#NUM!"
  },
  {
    "cell": "S20",
    "value": "#NUM!"
  },
  {
    "cell": "S21",
    "value": "#NUM!"
  },
  {
    "cell": "S22",
    "value": "#NUM!"
  },
  {
    "cell": "S23",
    "value": "#NUM!"
  },
  {
    "cell": "S24",
    "value": "#NUM!"
  },
  {
    "cell": "S25",
    "value": "#NUM!"
  },
  {
    "cell": "S26",
    "value": "#NUM!"
  },
  {
    "cell": "S27",
    "value": "#NUM!"
  },
  {
    "cell": "S28",
    "value": "#NUM!"
  },
  {
    "cell": "S29",
    "value": "#NUM!"
  },
  {
    "cell": "S30",
    "value": "#NUM!"
  },
  {
    "cell": "S31",
    "value": "#NUM!"
  },
  {
    "cell": "S32",
    "value": "#NUM!"
  },
  {
    "cell": "S47",
    "value": "#NUM!"
  },
  {
    "cell": "S48",
    "value": "#NUM!"
  },
  {
    "cell": "S49",
    "value": "#NUM!"
  },
  {
    "cell": "S50",
    "value": "#NUM!"
  },
  {
    "cell": "S51",
    "value": "#NUM!"
  },
  {
    "cell": "S52",
    "value": "#NUM!"
  },
  {
    "cell": "S53",
    "value": "#NUM!"
  },
  {
    "cell": "S54",
    "value": "#NUM!"
  },
  {
    "cell": "D55",
    "value": "#NUM!"
  },
  {
    "cell": "S55",
    "value": "#NUM!"
  },
  {
    "cell": "S56",
    "value": "#NUM!"
  },
  {
    "cell": "S57",
    "value": "#NUM!"
  },
  {
    "cell": "S58",
    "value": "#NUM!"
  },
  {
    "cell": "S59",
    "value": "#NUM!"
  }
]
```

## Hoja: Hoja2

Estado: `hidden`. Rango usado: `A3:S150`. Celdas con contenido: 926. Fórmulas: 749. Familias: 35.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `B3` | Datos de mercado |
| `B4` | Tipo de interés (continuo) |
| `E4` | dividendos |
| `B5` | Volatilidad |
| `E5` | Tiempo1 |
| `G5` | Tiempo2 |
| `B6` | Cotización hoy |
| `E6` | Div1 |
| `G6` | Div2 |
| `F7` | meses |
| `H7` | meses |
| `B8` | Datos del modelo |
| `B9` | Deltat |
| `B10` | Descuento periodo |
| `B12` | Parámetros del modelo |
| `B13` | p |
| `J13` | ¿martingala? |
| `L13` | volatilidad anual |
| `B14` | u |
| `J14` | una mínima comprobación |
| `B15` | d |
| `B17` | Árbol de evolución de S* |
| `P18` | probabilidades |
| `S18` | rendimientos anuales |
| `B37` | Proceso de dividendos |
| `B44` | Árbol de evolución de la cotización S |
| `S45` | rendimientos anuales |
| `B53` | ¿martingala? |
| `D53` | volatilidad anual |
| `B54` | una mínima comprobación |
| `B62` | Árbol de evolución del valor de la inversión en el activo |
| `B70` | pequeña comprobación de martingala |
| `A84` | senda S* |
| `A85` | senda S |
| `A86` | senda inversión |
| `A87` | dividendos |
| `B91` | Valoración de una put americana |
| `B92` | vencimiento |
| `B93` | strike |
| `B95` | Árbol de evolución de la opción |
| `B111` | Valoración de una call europea |
| `B112` | vencimiento |
| `B113` | strike |
| `B115` | Árbol de evolución de la opción |
| `B132` | Valoración de una call americana |
| `B133` | vencimiento |
| `B134` | strike |
| `B136` | Árbol de evolución de la opción |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `C4` | 0.006 | `0.0%` |
| `C5` | 0.4 | `0%` |
| `F5` | 2.5 | `General` |
| `H5` | 9.5 | `General` |
| `C6` | 80 | `General` |
| `F6` | 1.5 | `General` |
| `H6` | 2 | `General` |
| `C13` | 0.5 | `0.00%` |
| `B18` | 0 | `General` |
| `C18` | 1 | `General` |
| `D18` | 2 | `General` |
| `E18` | 3 | `General` |
| `F18` | 4 | `General` |
| `G18` | 5 | `General` |
| `H18` | 6 | `General` |
| `I18` | 7 | `General` |
| `J18` | 8 | `General` |
| `K18` | 9 | `General` |
| `L18` | 10 | `General` |
| `M18` | 11 | `General` |
| `N18` | 12 | `General` |
| `Q20` | 12 | `General` |
| `Q21` | 11 | `General` |
| `Q22` | 10 | `General` |
| `Q23` | 9 | `General` |
| `Q24` | 8 | `General` |
| `Q25` | 7 | `General` |
| `Q26` | 6 | `General` |
| `Q27` | 5 | `General` |
| `Q28` | 4 | `General` |
| `Q29` | 3 | `General` |
| `Q30` | 2 | `General` |
| `Q31` | 1 | `General` |
| `Q32` | 0 | `General` |
| `B38` | 0 | `General` |
| `C38` | 1 | `General` |
| `D38` | 2 | `General` |
| `E38` | 3 | `General` |
| `F38` | 4 | `General` |
| `G38` | 5 | `General` |
| `H38` | 6 | `General` |
| `I38` | 7 | `General` |
| `J38` | 8 | `General` |
| `K38` | 9 | `General` |
| `L38` | 10 | `General` |
| `M38` | 11 | `General` |
| `N38` | 12 | `General` |
| `B45` | 0 | `General` |
| `C45` | 1 | `General` |
| `D45` | 2 | `General` |
| `E45` | 3 | `General` |
| `F45` | 4 | `General` |
| `G45` | 5 | `General` |
| `H45` | 6 | `General` |
| `I45` | 7 | `General` |
| `J45` | 8 | `General` |
| `K45` | 9 | `General` |
| `L45` | 10 | `General` |
| `M45` | 11 | `General` |
| `N45` | 12 | `General` |
| `B63` | 0 | `General` |
| `C63` | 1 | `General` |
| `D63` | 2 | `General` |
| `E63` | 3 | `General` |
| `F63` | 4 | `General` |
| `G63` | 5 | `General` |
| `H63` | 6 | `General` |
| `I63` | 7 | `General` |
| `J63` | 8 | `General` |
| `K63` | 9 | `General` |
| `L63` | 10 | `General` |
| `M63` | 11 | `General` |
| `N63` | 12 | `General` |
| `B80` | 0 | `General` |
| `C80` | 1 | `General` |
| `D80` | 2 | `General` |
| `E80` | 3 | `General` |
| `F80` | 4 | `General` |
| `G80` | 5 | `General` |
| `H80` | 6 | `General` |
| `I80` | 7 | `General` |
| `J80` | 8 | `General` |
| `K80` | 9 | `General` |
| `L80` | 10 | `General` |
| `M80` | 11 | `General` |
| `N80` | 12 | `General` |
| `C92` | 1 | `General` |
| `C93` | 84 | `General` |
| `B96` | 0 | `General` |
| `C96` | 1 | `General` |
| `D96` | 2 | `General` |
| `E96` | 3 | `General` |
| `F96` | 4 | `General` |
| `G96` | 5 | `General` |
| `H96` | 6 | `General` |
| `I96` | 7 | `General` |
| `J96` | 8 | `General` |
| `K96` | 9 | `General` |
| `L96` | 10 | `General` |
| `M96` | 11 | `General` |
| `N96` | 12 | `General` |

Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):

| Columna | Primera / última celda | N | Primer / último valor |
|---|---|---:|---|
| C | `C112` / `C137` | 4 | 1 / 1 |
| B | `B116` / `B137` | 2 | 0 / 0 |
| D | `D116` / `D137` | 2 | 2 / 2 |
| E | `E116` / `E137` | 2 | 3 / 3 |
| F | `F116` / `F137` | 2 | 4 / 4 |
| G | `G116` / `G137` | 2 | 5 / 5 |
| H | `H116` / `H137` | 2 | 6 / 6 |
| I | `I116` / `I137` | 2 | 7 / 7 |
| J | `J116` / `J137` | 2 | 8 / 8 |
| K | `K116` / `K137` | 2 | 9 / 9 |
| L | `L116` / `L137` | 2 | 10 / 10 |
| M | `M116` / `M137` | 2 | 11 / 11 |
| N | `N116` / `N137` | 2 | 12 / 12 |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `C9` | `C9` | 1 | `=1/12` | 0.08333333333333333 |
| `C10` | `C10` | 1 | `=+EXP(-tipo*Deltat)` | 0.9995001249791693 |
| `C14` | `C14` | 1 | `=EXP(tipo*Deltat)*EXP(vola*SQRT(Deltat))*2/(EXP(vola*SQRT(Deltat))+EXP(-vola*SQRT(Deltat)))` | 1.115517195155658 |
| `C15` | `C15` | 1 | `=EXP(tipo*Deltat)*EXP(-vola*SQRT(Deltat))*2/(EXP(vola*SQRT(Deltat))+EXP(-vola*SQRT(Deltat)))` | 0.8854830548860136 |
| `J15` | `J15` | 1 | `=SUMPRODUCT(N20:N32,probs)*Descuento^12` | 76.51135130179459 |
| `L15` | `L15` | 1 | `=SQRT(SUMPRODUCT(S20:S32^2,probs)-SUMPRODUCT(S20:S32,probs)^2)` | 0.40000000000000013 |
| `B19` | `N64` | 52 | `=B18*Deltat` | 0 |
| `B20` | `B20` | 1 | `=S0-B40` | 76.5113513017947 |
| `C20` | `N20` | 12 | `=B20*u` | 85.34972800174722 |
| `P20` | `P32` | 13 | `=BINOMDIST(Q20,12,p,FALSE)` | 0.00024414062500000016 |
| `S20` | `S59` | 26 | `=LN(N20/S0)` | 1.2672302724625304 |
| `C21` | `N32` | 78 | `=B20*d` | 67.74950508417015 |
| `B40` | `N40` | 13 | `=IF(B38<=Tiempo1,dividendo1*EXP(-tipo*(Tiempo1-B38)*Deltat),0)+IF(B38<=Tiempo2,dividendo2*EXP(-tipo*(Tiempo2-B38)*Deltat),0)` | 3.488648698205295 |
| `B47` | `N59` | 91 | `=B20+B$40` | 80 |
| `B55` | `B55` | 1 | `=SUMPRODUCT(N47:N59,P20:P32)*Descuento^12` | 76.51135130179459 |
| `D55` | `D55` | 1 | `=SQRT(SUMPRODUCT(S47:S59^2,probs)-SUMPRODUCT(S47:S59,probs)^2)` | 0.40000000000000013 |
| `B65` | `N77` | 91 | `=B20+dividendo1*EXP(tipo*Deltat*(-Tiempo1+B$63))+dividendo2*EXP(tipo*Deltat*(-Tiempo2+B$63))` | 80 |
| `B71` | `B71` | 1 | `=SUMPRODUCT(N65:N77,P20:P32)*Descuento^12` | 79.99999999999989 |
| `C81` | `N81` | 12 | `=IF(RAND()<p,0,1)` | 0 |
| `C82` | `N82` | 12 | `=IF(C81=0,"sube","baja")` | sube |
| `C83` | `N83` | 12 | `=SUM($C$81:C81)` | 0 |
| `B84` | `B84` | 1 | `=B20` | 76.5113513017947 |
| `C84` | `N84` | 12 | `=OFFSET(C20,C83,0)` | 85.34972800174722 |
| `B85` | `B85` | 1 | `=B47` | 80 |
| `C85` | `N85` | 12 | `=OFFSET(C47,C83,0)` | 88.84012146045539 |
| `B86` | `B86` | 1 | `=B65` | 80 |
| `C86` | `N86` | 12 | `=OFFSET(C65,C83,0)` | 88.8401214604554 |
| `B87` | `N87` | 13 | `=B40` | 3.488648698205295 |
| `B97` | `M108` | 78 | `=MAX(MAX(strike-B47,0),Descuento*(p*C97+(1-p)*C98))` | 16.62681644800156 |
| `N97` | `N109` | 13 | `=MAX(strike-N47,0)` | 0 |
| `C113` | `C134` | 2 | `=strike` | 84 |
| `B117` | `M128` | 78 | `=Descuento*(p*C117+(1-p)*C118)` | 9.604030041502403 |
| `N117` | `N129` | 13 | `=MAX(N47-strike,0)` | 200.08028933607602 |
| `B138` | `M149` | 78 | `=MAX(Descuento*(p*C138+(1-p)*C139),MAX(B47-strike,0))` | 9.813960642866608 |
| `N138` | `N150` | 13 | `=MAX(N47-strike,0)` | 200.08028933607602 |

### Notas de celdas

- `B20`: la evolución parte de la cotización de hoy, a la que le restamos el valor actual de los dividendos futuros

- `B55`: la evolución de S no es martingala

- `D55`: pero acumula la volatilidad correcta

- `E65`: coincide con la cotización hasta el primer pago de dividendo

- `B138`: observa que la call americana ya es más valiosa que la correspondiente europea (por la presencia de los dividendos)


### Gráficos y rangos de origen

```json
[
  {
    "type": "LineChart",
    "title": "",
    "series": [
      {
        "val": "Hoja2!$B$40:$N$40",
        "cat": "Hoja2!$B$39:$N$39"
      }
    ]
  }
]
```

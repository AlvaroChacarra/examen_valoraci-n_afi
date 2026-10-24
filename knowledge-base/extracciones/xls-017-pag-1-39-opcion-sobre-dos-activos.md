# XLS-017: pag 1.39 opcion sobre dos activos.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-39-opcion-sobre-dos-activos.xlsx). SHA-256: `75e9e5eedc3599bcf8acb2873d94d78dbc32502f0f3d893039526f74fbeddfdc`.

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

Estado: `visible`. Rango usado: `B1:BN2056`. Celdas con contenido: 21507. Fórmulas: 19414. Familias: 16.

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
| `AB16` | -0.9 | `0%` |
| `AB17` | -0.8 | `0%` |
| `AC17` | 26.821469965923153 | `General` |
| `AB18` | -0.7 | `0%` |
| `AC18` | 26.74091812427674 | `General` |
| `AB19` | -0.6 | `0%` |
| `AC19` | 26.658781591947072 | `General` |
| `AB20` | -0.5 | `0%` |
| `AC20` | 26.57498025190152 | `General` |
| `D21` | 0.01 | `0%` |
| `AB21` | -0.4 | `0%` |
| `AC21` | 26.489429411804796 | `General` |
| `AB22` | -0.3 | `0%` |
| `AC22` | 26.402039859886763 | `General` |
| `D23` | 25 | `General` |
| `F23` | 20 | `General` |
| `AB23` | -0.2 | `0%` |
| `AC23` | 26.312718486029077 | `General` |
| `D24` | 0.15 | `0%` |
| `F24` | 0.3 | `0%` |
| `AB24` | -0.1 | `0%` |
| `AC24` | 26.22136968069886 | `General` |
| `AB25` | 0 | `0%` |
| `AC25` | 26.12789797593609 | `General` |
| `AB26` | 0.1 | `0%` |
| `AC26` | 26.032212758032077 | `General` |
| `D27` | -0.2 | `0%` |
| `AB27` | 0.2 | `0%` |
| `AC27` | 25.934236518875124 | `General` |
| `AB28` | 0.3 | `0%` |
| `AC28` | 25.833919292029346 | `General` |
| `AB29` | 0.4 | `0%` |
| `AC29` | 25.73126419947788 | `General` |
| `AB30` | 0.5 | `0%` |
| `AC30` | 25.62637365094386 | `General` |
| `AB31` | 0.6 | `0%` |
| `AC31` | 25.51953558205343 | `General` |
| `F32` | 1 | `General` |
| `AB32` | 0.7 | `0%` |
| `AC32` | 25.411391405634106 | `General` |
| `AB33` | 0.8 | `0%` |
| `AC33` | 25.303281348262335 | `General` |
| `AB34` | 0.9 | `0%` |
| `AC34` | 25.198003269028515 | `General` |
| `AB35` | 0.99 | `0%` |
| `AC35` | 25.11312408738784 | `General` |
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
| `AC15` | `AC15` | 1 | `=Y40` | 26.312718486029077 |
| `AC16` | `AC16` | 1 | `<DataTableFormula: {'ref': 'AC16:AC35', 'ca': '1', 'dt2D': '0', 'dtr': '0', 'r1': 'D27', 'r2': None, 'del1': False, 'del2': False}>` | 26.900513268556182 |
| `Y40` | `Y40` | 1 | `=SUMPRODUCT(P44:BN94,P107:BN157)*EXP(-tipo*T)` | 26.312718486029077 |
| `I42` | `I42` | 1 | `=EXP(-tipo*T)*AVERAGE(I48:I2047)` | 26.46066805884229 |
| `C43` | `F43` | 4 | `=AVERAGE(C48:C2047)` | 0.01960984726849898 |
| `Q43` | `BN106` | 100 | `=P43+paso` | -4.8 |
| `C44` | `F44` | 4 | `=STDEV(C48:C2047)` | 1.015640158203008 |
| `P44` | `BN94` | 2601 | `=1/(2*PI()*SQRT(1-correla^2))*EXP(-1/(2*(1-correla^2))*(P$43^2+$O44^2-2*correla*P$43*$O44))*paso^2` | 1.7419751165038155e-16 |
| `O45` | `O157` | 100 | `=O44+paso` | -4.8 |
| `C48` | `D2047` | 4000 | `=NORMSINV(RAND())` | -0.6674251258922519 |
| `E48` | `E2047` | 2000 | `=C48` | -0.6674251258922519 |
| `F48` | `F2047` | 2000 | `=correla*C48+SQRT(1-correla^2)*D48` | -1.1356472088594518 |
| `G48` | `G2047` | 2000 | `=X0*EXP(volaX*SQRT(T)*E48+(tipo-0.5*volaX^2)*T)` | 22.59010674939777 |
| `H48` | `H2047` | 2000 | `=Y0*EXP(volaY*SQRT(T)*F48+(tipo-0.5*volaY^2)*T)` | 13.736247075788384 |
| `I48` | `I2047` | 2000 | `=(MAX(G48,H48))` | 22.59010674939777 |
| `P107` | `BN157` | 2601 | `=MAX(X0*EXP(volaX*SQRT(T)*P$106+(tipo-0.5*volaX^2)*T),Y0*EXP(volaY*SQRT(T)*$O107+(tipo-0.5*volaY^2)*T))` | 11.794411585818516 |

### Notas de celdas

- `P44`: son las probabilidades conjuntas de las dos normales estándar con la correlación dada. Usamos la fórmula de la densidad conjunta, por eso multiplicamos por el "área de la base"


### Gráficos y rangos de origen

```json
[
  {
    "type": "LineChart",
    "title": "",
    "series": [
      {
        "val": "Hoja1!$AC$16:$AC$35",
        "cat": "Hoja1!$AB$16:$AB$35"
      }
    ]
  }
]
```

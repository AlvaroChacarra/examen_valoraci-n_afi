# XLS-029: pag 2.35-CMS10Y.xlsm

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-35-cms10y.xlsm). SHA-256: `17529489811bbbed15ebe43582a2602cae16bdf3f8b09671a7295504382925b9`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **True**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `deltat` | `Hoja1!$G$6` |
| `vola` | `Hoja1!$I$11` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `A2:U117`. Celdas con contenido: 911. Fórmulas: 516. Familias: 17.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `L2` | Valoración del bono con cupones trimestrales en función del CMS 10Y |
| `T2` | Valoración "naive" |
| `R5` | valor total |
| `T5` | valor total |
| `B6` | fecha hoy |
| `F6` | deltat |
| `L6` | Liquidador |
| `B9` | FECHA |
| `C9` | PLAZO |
| `D9` | FD |
| `F9` | PLAZO |
| `G9` | trimestres |
| `H9` | descuentos |
| `I9` | volas |
| `L9` | anualidad10 |
| `M9` | fswap10 (hoy) |
| `N9` | plazo |
| `O9` | alpha |
| `P9` | beta |
| `Q9` | corrección |
| `R9` | valor |
| `T9` | desc*fwdswap*periodo |
| `M54` | Impacto de la volatilidad sobre el valor total del instrumento |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `C6` | 2019-03-12T00:00:00 | `d-mmm-yy` |
| `G6` | 0.25 | `General` |
| `B10` | 2019-03-12T00:00:00 | `d-mmm-yy` |
| `D10` | 1 | `0.00%` |
| `G10` | 0 | `General` |
| `B11` | 2019-03-19T00:00:00 | `d-mmm-yy` |
| `D11` | 0.99994 | `0.00%` |
| `G11` | 1 | `General` |
| `I11` | 0.3 | `0.00%` |
| `N11` | 10 | `General` |
| `B12` | 2019-03-26T00:00:00 | `d-mmm-yy` |
| `D12` | 0.99988 | `0.00%` |
| `G12` | 2 | `General` |
| `N12` | 10 | `General` |
| `B13` | 2019-04-02T00:00:00 | `d-mmm-yy` |
| `D13` | 0.9998 | `0.00%` |
| `G13` | 3 | `General` |
| `N13` | 10 | `General` |
| `B14` | 2019-04-12T00:00:00 | `d-mmm-yy` |
| `D14` | 0.9997 | `0.00%` |
| `G14` | 4 | `General` |
| `N14` | 10 | `General` |
| `B15` | 2019-05-12T00:00:00 | `d-mmm-yy` |
| `D15` | 0.99915 | `0.00%` |
| `G15` | 5 | `General` |
| `N15` | 10 | `General` |
| `B16` | 2019-06-12T00:00:00 | `d-mmm-yy` |
| `D16` | 0.99872 | `0.00%` |
| `G16` | 6 | `General` |
| `N16` | 10 | `General` |
| `B17` | 2019-07-12T00:00:00 | `d-mmm-yy` |
| `D17` | 0.99797 | `0.00%` |
| `G17` | 7 | `General` |
| `N17` | 10 | `General` |
| `B18` | 2019-08-12T00:00:00 | `d-mmm-yy` |
| `D18` | 0.99703 | `0.00%` |
| `G18` | 8 | `General` |
| `N18` | 10 | `General` |
| `B19` | 2019-09-12T00:00:00 | `d-mmm-yy` |
| `D19` | 0.99593 | `0.00%` |
| `G19` | 9 | `General` |
| `N19` | 10 | `General` |
| `B20` | 2019-10-12T00:00:00 | `d-mmm-yy` |
| `D20` | 0.99468 | `0.00%` |
| `G20` | 10 | `General` |
| `N20` | 10 | `General` |
| `B21` | 2019-11-12T00:00:00 | `d-mmm-yy` |
| `D21` | 0.99358 | `0.00%` |
| `G21` | 11 | `General` |
| `N21` | 10 | `General` |
| `B22` | 2019-12-12T00:00:00 | `d-mmm-yy` |
| `D22` | 0.99186 | `0.00%` |
| `G22` | 12 | `General` |
| `N22` | 10 | `General` |
| `B23` | 2020-01-12T00:00:00 | `d-mmm-yy` |
| `D23` | 0.99115 | `0.00%` |
| `G23` | 13 | `General` |
| `N23` | 10 | `General` |
| `B24` | 2020-02-12T00:00:00 | `d-mmm-yy` |
| `D24` | 0.98981 | `0.00%` |
| `G24` | 14 | `General` |
| `N24` | 10 | `General` |
| `B25` | 2020-03-12T00:00:00 | `d-mmm-yy` |
| `D25` | 0.98803 | `0.00%` |
| `G25` | 15 | `General` |
| `N25` | 10 | `General` |
| `B26` | 2021-03-12T00:00:00 | `d-mmm-yy` |
| `D26` | 0.97018 | `0.00%` |
| `G26` | 16 | `General` |
| `N26` | 10 | `General` |
| `B27` | 2022-03-12T00:00:00 | `d-mmm-yy` |
| `D27` | 0.94535 | `0.00%` |
| `G27` | 17 | `General` |
| `N27` | 10 | `General` |
| `B28` | 2023-03-12T00:00:00 | `d-mmm-yy` |
| `D28` | 0.91608 | `0.00%` |
| `G28` | 18 | `General` |
| `N28` | 10 | `General` |
| `B29` | 2024-03-12T00:00:00 | `d-mmm-yy` |
| `D29` | 0.88367 | `0.00%` |
| `G29` | 19 | `General` |
| `N29` | 10 | `General` |
| `B30` | 2025-03-12T00:00:00 | `d-mmm-yy` |
| `D30` | 0.84908 | `0.00%` |
| `G30` | 20 | `General` |
| `N30` | 10 | `General` |
| `B31` | 2026-03-12T00:00:00 | `d-mmm-yy` |
| `D31` | 0.81385 | `0.00%` |
| `G31` | 21 | `General` |
| `N31` | 10 | `General` |
| `B32` | 2027-03-12T00:00:00 | `d-mmm-yy` |
| `D32` | 0.77878 | `0.00%` |
| `G32` | 22 | `General` |
| `N32` | 10 | `General` |
| `B33` | 2028-03-12T00:00:00 | `d-mmm-yy` |
| `D33` | 0.74453 | `0.00%` |
| `G33` | 23 | `General` |
| `N33` | 10 | `General` |
| `B34` | 2029-03-12T00:00:00 | `d-mmm-yy` |
| `D34` | 0.71102 | `0.00%` |
| `G34` | 24 | `General` |
| `N34` | 10 | `General` |
| `B35` | 2034-03-12T00:00:00 | `d-mmm-yy` |
| `D35` | 0.56115 | `0.00%` |
| `G35` | 25 | `General` |
| `N35` | 10 | `General` |
| `B36` | 2039-03-12T00:00:00 | `d-mmm-yy` |
| `D36` | 0.44996 | `0.00%` |
| `G36` | 26 | `General` |
| `N36` | 10 | `General` |
| `B37` | 2044-03-12T00:00:00 | `d-mmm-yy` |
| `D37` | 0.37497 | `0.00%` |
| `G37` | 27 | `General` |
| `N37` | 10 | `General` |
| `B38` | 2049-03-12T00:00:00 | `d-mmm-yy` |
| `D38` | 0.32143 | `0.00%` |
| `G38` | 28 | `General` |
| `N38` | 10 | `General` |
| `B39` | 2054-03-12T00:00:00 | `d-mmm-yy` |
| `D39` | 0.27863 | `0.00%` |
| `G39` | 29 | `General` |
| `N39` | 10 | `General` |
| `B40` | 2059-03-12T00:00:00 | `d-mmm-yy` |
| `D40` | 0.24243 | `0.00%` |
| `G40` | 30 | `General` |
| `N40` | 10 | `General` |
| `B41` | 2064-03-12T00:00:00 | `d-mmm-yy` |
| `D41` | 0.20755 | `0.00%` |
| `G41` | 31 | `General` |
| `N41` | 10 | `General` |
| `B42` | 2069-03-12T00:00:00 | `d-mmm-yy` |
| `D42` | 0.17825 | `0.00%` |
| `G42` | 32 | `General` |
| `N42` | 10 | `General` |
| `G43` | 33 | `General` |
| `N43` | 10 | `General` |
| `G44` | 34 | `General` |
| `N44` | 10 | `General` |
| `G45` | 35 | `General` |
| `N45` | 10 | `General` |
| `G46` | 36 | `General` |
| `N46` | 10 | `General` |
| `G47` | 37 | `General` |
| `N47` | 10 | `General` |
| `G48` | 38 | `General` |
| `N48` | 10 | `General` |
| `G49` | 39 | `General` |
| `N49` | 10 | `General` |
| `G50` | 40 | `General` |
| `G51` | 41 | `General` |
| `G52` | 42 | `General` |
| `G53` | 43 | `General` |
| `G54` | 44 | `General` |
| `G55` | 45 | `General` |
| `G56` | 46 | `General` |
| `G57` | 47 | `General` |
| `M57` | 0 | `0%` |
| `O57` | 1.07521451297762 | `0.00%` |
| `G58` | 48 | `General` |
| `M58` | 0.01 | `0%` |
| `N58` | 1.0752495225539924 | `0.00%` |
| `O58` | 1.07521451297762 | `0.00%` |
| `G59` | 49 | `General` |
| `M59` | 0.02 | `0%` |
| `N59` | 1.075354689784002 | `0.00%` |
| `O59` | 1.07521451297762 | `0.00%` |
| `G60` | 50 | `General` |
| `M60` | 0.03 | `0%` |
| `N60` | 1.0755304311903413 | `0.00%` |
| `O60` | 1.07521451297762 | `0.00%` |
| `G61` | 51 | `General` |
| `M61` | 0.04 | `0%` |
| `N61` | 1.0757774443887596 | `0.00%` |
| `O61` | 1.07521451297762 | `0.00%` |
| `G62` | 52 | `General` |
| `M62` | 0.05 | `0%` |
| `N62` | 1.076096713244381 | `0.00%` |
| `O62` | 1.07521451297762 | `0.00%` |
| `G63` | 53 | `General` |
| `M63` | 0.06 | `0%` |
| `N63` | 1.076489515169995 | `0.00%` |
| `O63` | 1.07521451297762 | `0.00%` |
| `G64` | 54 | `General` |
| `M64` | 0.07 | `0%` |
| `N64` | 1.0769574306471728 | `0.00%` |
| `O64` | 1.07521451297762 | `0.00%` |
| `G65` | 55 | `General` |
| `M65` | 0.08 | `0%` |
| `N65` | 1.0775023550762115 | `0.00%` |
| `O65` | 1.07521451297762 | `0.00%` |
| `G66` | 56 | `General` |
| `M66` | 0.09 | `0%` |
| `N66` | 1.07812651308762 | `0.00%` |
| `O66` | 1.07521451297762 | `0.00%` |
| `G67` | 57 | `General` |
| `M67` | 0.1 | `0%` |
| `N67` | 1.0788324754765926 | `0.00%` |
| `O67` | 1.07521451297762 | `0.00%` |
| `G68` | 58 | `General` |
| `M68` | 0.11 | `0%` |
| `N68` | 1.0796231789530726 | `0.00%` |
| `O68` | 1.07521451297762 | `0.00%` |
| `G69` | 59 | `General` |
| `M69` | 0.12 | `0%` |
| `N69` | 1.080501948934107 | `0.00%` |
| `O69` | 1.07521451297762 | `0.00%` |
| `G70` | 60 | `General` |
| `M70` | 0.13 | `0%` |
| `N70` | 1.0814725256427893 | `0.00%` |
| `O70` | 1.07521451297762 | `0.00%` |
| `G71` | 61 | `General` |
| `M71` | 0.14 | `0%` |
| `N71` | 1.0825390938197852 | `0.00%` |
| `O71` | 1.07521451297762 | `0.00%` |
| `G72` | 62 | `General` |
| `M72` | 0.15 | `0%` |
| `N72` | 1.083706316399945 | `0.00%` |
| `O72` | 1.07521451297762 | `0.00%` |
| `G73` | 63 | `General` |
| `M73` | 0.16 | `0%` |
| `N73` | 1.0849793725586294 | `0.00%` |
| `O73` | 1.07521451297762 | `0.00%` |
| `G74` | 64 | `General` |
| `M74` | 0.17 | `0%` |
| `N74` | 1.0863640005909896 | `0.00%` |
| `O74` | 1.07521451297762 | `0.00%` |
| `G75` | 65 | `General` |
| `M75` | 0.18 | `0%` |
| `N75` | 1.0878665461536419 | `0.00%` |
| `O75` | 1.07521451297762 | `0.00%` |
| `G76` | 66 | `General` |
| `M76` | 0.19 | `0%` |
| `N76` | 1.089494016473079 | `0.00%` |
| `O76` | 1.07521451297762 | `0.00%` |
| `G77` | 67 | `General` |
| `M77` | 0.2 | `0%` |
| `N77` | 1.0912541412102224 | `0.00%` |
| `O77` | 1.07521451297762 | `0.00%` |
| `G78` | 68 | `General` |
| `M78` | 0.21 | `0%` |
| `N78` | 1.0931554407672561 | `0.00%` |
| `O78` | 1.07521451297762 | `0.00%` |
| `G79` | 69 | `General` |
| `M79` | 0.22 | `0%` |
| `N79` | 1.0952073029331943 | `0.00%` |
| `O79` | 1.07521451297762 | `0.00%` |
| `G80` | 70 | `General` |
| `M80` | 0.23 | `0%` |
| `N80` | 1.097420068890583 | `0.00%` |
| `O80` | 1.07521451297762 | `0.00%` |
| `G81` | 71 | `General` |
| `M81` | 0.24 | `0%` |
| `N81` | 1.0998051297498672 | `0.00%` |
| `O81` | 1.07521451297762 | `0.00%` |
| `G82` | 72 | `General` |
| `M82` | 0.25 | `0%` |
| `N82` | 1.1023750349430734 | `0.00%` |
| `O82` | 1.07521451297762 | `0.00%` |
| `G83` | 73 | `General` |
| `M83` | 0.26 | `0%` |
| `N83` | 1.1051436139979587 | `0.00%` |
| `O83` | 1.07521451297762 | `0.00%` |
| `G84` | 74 | `General` |
| `M84` | 0.27 | `0%` |
| `N84` | 1.108126113431536 | `0.00%` |
| `O84` | 1.07521451297762 | `0.00%` |
| `G85` | 75 | `General` |
| `M85` | 0.28 | `0%` |
| `N85` | 1.111339350752476 | `0.00%` |
| `O85` | 1.07521451297762 | `0.00%` |
| `G86` | 76 | `General` |
| `M86` | 0.29 | `0%` |
| `N86` | 1.1148018878506016 | `0.00%` |
| `O86` | 1.07521451297762 | `0.00%` |
| `G87` | 77 | `General` |
| `M87` | 0.3 | `0%` |
| `N87` | 1.1185342263848255 | `0.00%` |
| `O87` | 1.07521451297762 | `0.00%` |
| `G88` | 78 | `General` |
| `M88` | 0.31 | `0%` |
| `N88` | 1.122559028165652 | `0.00%` |
| `O88` | 1.07521451297762 | `0.00%` |
| `G89` | 79 | `General` |
| `M89` | 0.32 | `0%` |
| `N89` | 1.1269013639734318 | `0.00%` |
| `O89` | 1.07521451297762 | `0.00%` |
| `G90` | 80 | `General` |
| `M90` | 0.33 | `0%` |
| `N90` | 1.1315889947689173 | `0.00%` |
| `O90` | 1.07521451297762 | `0.00%` |
| `G91` | 81 | `General` |
| `M91` | 0.34 | `0%` |
| `N91` | 1.136652689850194 | `0.00%` |
| `O91` | 1.07521451297762 | `0.00%` |
| `M92` | 0.35 | `0%` |
| `N92` | 1.1421265872036888 | `0.00%` |
| `O92` | 1.07521451297762 | `0.00%` |
| `M93` | 0.36 | `0%` |
| `N93` | 1.1480486021031027 | `0.00%` |
| `O93` | 1.07521451297762 | `0.00%` |
| `M94` | 0.37 | `0%` |
| `N94` | 1.1544608909481897 | `0.00%` |
| `O94` | 1.07521451297762 | `0.00%` |
| `M95` | 0.38 | `0%` |
| `N95` | 1.1614103784282 | `0.00%` |
| `O95` | 1.07521451297762 | `0.00%` |
| `M96` | 0.39 | `0%` |
| `N96` | 1.1689493573696572 | `0.00%` |
| `O96` | 1.07521451297762 | `0.00%` |
| `M97` | 0.4 | `0%` |
| `N97` | 1.1771361721170268 | `0.00%` |
| `O97` | 1.07521451297762 | `0.00%` |
| `M98` | 0.41 | `0%` |
| `N98` | 1.1860359980358517 | `0.00%` |
| `O98` | 1.07521451297762 | `0.00%` |
| `M99` | 0.42 | `0%` |
| `N99` | 1.1957217317662718 | `0.00%` |
| `O99` | 1.07521451297762 | `0.00%` |
| `M100` | 0.43 | `0%` |
| `N100` | 1.2062750092442514 | `0.00%` |
| `O100` | 1.07521451297762 | `0.00%` |

Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):

| Columna | Primera / última celda | N | Primer / último valor |
|---|---|---:|---|
| M | `M101` / `M117` | 17 | 0.44 / 0.6 |
| N | `N101` / `N117` | 17 | 1.2177873713122636 / 1.6772221832050385 |
| O | `O101` / `O117` | 17 | 1.07521451297762 / 1.07521451297762 |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `R6` | `T6` | 2 | `=SUM(R11:R50)` | 1.1185342263848255 |
| `C10` | `C42` | 33 | `=YEARFRAC($B$10,B10)` | 0 |
| `F10` | `F91` | 82 | `=G10*deltat` | 0 |
| `H10` | `H91` | 82 | `=interpola(F10,$C$10:$D$42,1)` | 1 |
| `L11` | `L49` | 39 | `=SUM(H12:H51)*deltat` | 8.636255375 |
| `M11` | `M49` | 39 | `=(H11-H51)/L11` | 0.03418072847342129 |
| `O11` | `O49` | 39 | `=1/N11` | 0.1 |
| `P11` | `P49` | 39 | `=1/M11*(H11/L11-1/N11)` | 0.4576471450082744 |
| `Q11` | `Q49` | 39 | `=(P11*M11/(O11+P11*M11))*(EXP(I11^2*F11)-1)` | 0.003078018973901568 |
| `R11` | `R49` | 39 | `=M11*H11*(1+Q11)*deltat` | 0.00856051285108172 |
| `T11` | `T49` | 39 | `=H11*M11*deltat` | 0.008534244285243828 |
| `I12` | `I50` | 39 | `=vola` | 0.3 |
| `R50` | `R50` | 1 | `=1*H50` | 0.71102 |
| `T50` | `T50` | 1 | `=1*H50` | 0.71102 |
| `N56` | `N56` | 1 | `=R6` | 1.1185342263848255 |
| `O56` | `O56` | 1 | `=T6` | 1.07521451297762 |
| `N57` | `N57` | 1 | `<DataTableFormula: {'ref': 'N57:O117', 'ca': False, 'dt2D': '0', 'dtr': '0', 'r1': 'I11', 'r2': None, 'del1': False, 'del2': False}>` | 1.07521451297762 |

### Gráficos y rangos de origen

```json
[
  {
    "type": "LineChart",
    "title": "",
    "series": [
      {
        "val": "Hoja1!$N$57:$N$117",
        "cat": "Hoja1!$M$57:$M$117"
      },
      {
        "val": "Hoja1!$O$57:$O$117",
        "cat": "Hoja1!$M$57:$M$117"
      }
    ]
  },
  {
    "type": "LineChart",
    "title": "",
    "series": [
      {
        "val": "Hoja1!$R$11:$R$49",
        "cat": "Hoja1!$F$11:$F$49"
      },
      {
        "val": "Hoja1!$T$11:$T$49",
        "cat": "Hoja1!$F$11:$F$49"
      }
    ]
  }
]
```

## Código VBA recuperado

Código fuente leído estáticamente del contenedor VBA. No se ha ejecutado. Los módulos de interfaz sin procedimientos no añaden lógica de cálculo.

### Módulo ThisWorkbook

```vb
Attribute VB_Name = "ThisWorkbook"
Attribute VB_Base = "0{00020819-0000-0000-C000-000000000046}"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Attribute VB_TemplateDerived = False
Attribute VB_Customizable = True

```

### Módulo Hoja1

```vb
Attribute VB_Name = "Hoja1"
Attribute VB_Base = "0{00020820-0000-0000-C000-000000000046}"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Attribute VB_TemplateDerived = False
Attribute VB_Customizable = True

```

### Módulo Módulo1

```vb
Attribute VB_Name = "Módulo1"
Option Explicit

Function InterPola(ByVal Fecha As Variant, _
ByRef Curva As Variant, Optional ByVal modo As Integer) As Variant
    Dim a As Integer, b As Integer, N As Integer, m As Integer
    
    If IsMissing(modo) Then
        m = 0
    Else
        m = modo
    End If
      
    a = 1
    b = Curva.Rows.Count
    N = Int((a + b) / 2)
      
    While b - a > 1
        If Curva(N, 1) >= Fecha Then b = N
        If Curva(N, 1) < Fecha Then a = N
        N = Int((a + b) / 2)
    Wend
    
    Select Case modo
        Case 0
            InterPola = Exp(Log(Curva(a, 2)) + (Log(Curva(b, 2)) _
            - Log(Curva(a, 2))) * ((Fecha - Curva(a, 1)) _
            / (Curva(b, 1) - Curva(a, 1))))
        Case 1
            InterPola = Curva(a, 2) + (Curva(b, 2) - Curva(a, 2)) * (Fecha - Curva(a, 1)) / (Curva(b, 1) - Curva(a, 1))
    End Select
    
End Function


```

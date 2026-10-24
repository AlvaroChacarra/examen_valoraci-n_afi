# XLS-032: CMS10Y_Plantilla.xlsm

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos/cms10y-plantilla.xlsm). SHA-256: `c085ced28c27c8e75fe25bf6554b8fd890073c09d5eed72dbbdc0010230fb4c1`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **True**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `deltat` | `Hoja1!$G$6` |
| `vola` | `Hoja1!$I$11` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `A2:U117`. Celdas con contenido: 473. Fórmulas: 238. Familias: 6.

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
| `B12` | 2019-03-26T00:00:00 | `d-mmm-yy` |
| `D12` | 0.99988 | `0.00%` |
| `G12` | 2 | `General` |
| `B13` | 2019-04-02T00:00:00 | `d-mmm-yy` |
| `D13` | 0.9998 | `0.00%` |
| `G13` | 3 | `General` |
| `B14` | 2019-04-12T00:00:00 | `d-mmm-yy` |
| `D14` | 0.9997 | `0.00%` |
| `G14` | 4 | `General` |
| `B15` | 2019-05-12T00:00:00 | `d-mmm-yy` |
| `D15` | 0.99915 | `0.00%` |
| `G15` | 5 | `General` |
| `B16` | 2019-06-12T00:00:00 | `d-mmm-yy` |
| `D16` | 0.99872 | `0.00%` |
| `G16` | 6 | `General` |
| `B17` | 2019-07-12T00:00:00 | `d-mmm-yy` |
| `D17` | 0.99797 | `0.00%` |
| `G17` | 7 | `General` |
| `B18` | 2019-08-12T00:00:00 | `d-mmm-yy` |
| `D18` | 0.99703 | `0.00%` |
| `G18` | 8 | `General` |
| `B19` | 2019-09-12T00:00:00 | `d-mmm-yy` |
| `D19` | 0.99593 | `0.00%` |
| `G19` | 9 | `General` |
| `B20` | 2019-10-12T00:00:00 | `d-mmm-yy` |
| `D20` | 0.99468 | `0.00%` |
| `G20` | 10 | `General` |
| `B21` | 2019-11-12T00:00:00 | `d-mmm-yy` |
| `D21` | 0.99358 | `0.00%` |
| `G21` | 11 | `General` |
| `B22` | 2019-12-12T00:00:00 | `d-mmm-yy` |
| `D22` | 0.99186 | `0.00%` |
| `G22` | 12 | `General` |
| `B23` | 2020-01-12T00:00:00 | `d-mmm-yy` |
| `D23` | 0.99115 | `0.00%` |
| `G23` | 13 | `General` |
| `B24` | 2020-02-12T00:00:00 | `d-mmm-yy` |
| `D24` | 0.98981 | `0.00%` |
| `G24` | 14 | `General` |
| `B25` | 2020-03-12T00:00:00 | `d-mmm-yy` |
| `D25` | 0.98803 | `0.00%` |
| `G25` | 15 | `General` |
| `B26` | 2021-03-12T00:00:00 | `d-mmm-yy` |
| `D26` | 0.97018 | `0.00%` |
| `G26` | 16 | `General` |
| `B27` | 2022-03-12T00:00:00 | `d-mmm-yy` |
| `D27` | 0.94535 | `0.00%` |
| `G27` | 17 | `General` |
| `B28` | 2023-03-12T00:00:00 | `d-mmm-yy` |
| `D28` | 0.91608 | `0.00%` |
| `G28` | 18 | `General` |
| `B29` | 2024-03-12T00:00:00 | `d-mmm-yy` |
| `D29` | 0.88367 | `0.00%` |
| `G29` | 19 | `General` |
| `B30` | 2025-03-12T00:00:00 | `d-mmm-yy` |
| `D30` | 0.84908 | `0.00%` |
| `G30` | 20 | `General` |
| `B31` | 2026-03-12T00:00:00 | `d-mmm-yy` |
| `D31` | 0.81385 | `0.00%` |
| `G31` | 21 | `General` |
| `B32` | 2027-03-12T00:00:00 | `d-mmm-yy` |
| `D32` | 0.77878 | `0.00%` |
| `G32` | 22 | `General` |
| `B33` | 2028-03-12T00:00:00 | `d-mmm-yy` |
| `D33` | 0.74453 | `0.00%` |
| `G33` | 23 | `General` |
| `B34` | 2029-03-12T00:00:00 | `d-mmm-yy` |
| `D34` | 0.71102 | `0.00%` |
| `G34` | 24 | `General` |
| `B35` | 2034-03-12T00:00:00 | `d-mmm-yy` |
| `D35` | 0.56115 | `0.00%` |
| `G35` | 25 | `General` |
| `B36` | 2039-03-12T00:00:00 | `d-mmm-yy` |
| `D36` | 0.44996 | `0.00%` |
| `G36` | 26 | `General` |
| `B37` | 2044-03-12T00:00:00 | `d-mmm-yy` |
| `D37` | 0.37497 | `0.00%` |
| `G37` | 27 | `General` |
| `B38` | 2049-03-12T00:00:00 | `d-mmm-yy` |
| `D38` | 0.32143 | `0.00%` |
| `G38` | 28 | `General` |
| `B39` | 2054-03-12T00:00:00 | `d-mmm-yy` |
| `D39` | 0.27863 | `0.00%` |
| `G39` | 29 | `General` |
| `B40` | 2059-03-12T00:00:00 | `d-mmm-yy` |
| `D40` | 0.24243 | `0.00%` |
| `G40` | 30 | `General` |
| `B41` | 2064-03-12T00:00:00 | `d-mmm-yy` |
| `D41` | 0.20755 | `0.00%` |
| `G41` | 31 | `General` |
| `B42` | 2069-03-12T00:00:00 | `d-mmm-yy` |
| `D42` | 0.17825 | `0.00%` |
| `G42` | 32 | `General` |
| `G43` | 33 | `General` |
| `G44` | 34 | `General` |
| `G45` | 35 | `General` |
| `G46` | 36 | `General` |
| `G47` | 37 | `General` |
| `G48` | 38 | `General` |
| `G49` | 39 | `General` |
| `G50` | 40 | `General` |
| `G51` | 41 | `General` |
| `G52` | 42 | `General` |
| `G53` | 43 | `General` |
| `G54` | 44 | `General` |
| `G55` | 45 | `General` |
| `G56` | 46 | `General` |
| `G57` | 47 | `General` |
| `M57` | 0 | `0%` |
| `G58` | 48 | `General` |
| `M58` | 0.01 | `0%` |
| `G59` | 49 | `General` |
| `M59` | 0.02 | `0%` |
| `G60` | 50 | `General` |
| `M60` | 0.03 | `0%` |
| `G61` | 51 | `General` |
| `M61` | 0.04 | `0%` |
| `G62` | 52 | `General` |
| `M62` | 0.05 | `0%` |
| `G63` | 53 | `General` |
| `M63` | 0.06 | `0%` |
| `G64` | 54 | `General` |
| `M64` | 0.07 | `0%` |
| `G65` | 55 | `General` |
| `M65` | 0.08 | `0%` |
| `G66` | 56 | `General` |
| `M66` | 0.09 | `0%` |
| `G67` | 57 | `General` |
| `M67` | 0.1 | `0%` |
| `G68` | 58 | `General` |
| `M68` | 0.11 | `0%` |
| `G69` | 59 | `General` |
| `M69` | 0.12 | `0%` |
| `G70` | 60 | `General` |
| `M70` | 0.13 | `0%` |
| `G71` | 61 | `General` |
| `M71` | 0.14 | `0%` |
| `G72` | 62 | `General` |
| `M72` | 0.15 | `0%` |
| `G73` | 63 | `General` |
| `M73` | 0.16 | `0%` |
| `G74` | 64 | `General` |
| `M74` | 0.17 | `0%` |
| `G75` | 65 | `General` |
| `M75` | 0.18 | `0%` |
| `G76` | 66 | `General` |
| `M76` | 0.19 | `0%` |
| `G77` | 67 | `General` |
| `M77` | 0.2 | `0%` |
| `G78` | 68 | `General` |
| `M78` | 0.21 | `0%` |
| `G79` | 69 | `General` |
| `M79` | 0.22 | `0%` |
| `G80` | 70 | `General` |
| `M80` | 0.23 | `0%` |
| `G81` | 71 | `General` |
| `M81` | 0.24 | `0%` |
| `G82` | 72 | `General` |
| `M82` | 0.25 | `0%` |
| `G83` | 73 | `General` |
| `M83` | 0.26 | `0%` |
| `G84` | 74 | `General` |
| `M84` | 0.27 | `0%` |
| `G85` | 75 | `General` |
| `M85` | 0.28 | `0%` |
| `G86` | 76 | `General` |
| `M86` | 0.29 | `0%` |
| `G87` | 77 | `General` |
| `M87` | 0.3 | `0%` |
| `G88` | 78 | `General` |
| `M88` | 0.31 | `0%` |
| `G89` | 79 | `General` |
| `M89` | 0.32 | `0%` |
| `G90` | 80 | `General` |
| `M90` | 0.33 | `0%` |
| `G91` | 81 | `General` |
| `M91` | 0.34 | `0%` |
| `M92` | 0.35 | `0%` |
| `M93` | 0.36 | `0%` |
| `M94` | 0.37 | `0%` |
| `M95` | 0.38 | `0%` |
| `M96` | 0.39 | `0%` |
| `M97` | 0.4 | `0%` |
| `M98` | 0.41 | `0%` |
| `M99` | 0.42 | `0%` |
| `M100` | 0.43 | `0%` |

Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):

| Columna | Primera / última celda | N | Primer / último valor |
|---|---|---:|---|
| M | `M101` / `M117` | 17 | 0.44 / 0.6 |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `C10` | `C42` | 33 | `=YEARFRAC($B$10,B10)` | 0 |
| `F10` | `F91` | 82 | `=G10*deltat` | 0 |
| `H10` | `H91` | 82 | `=interpola(F10,$C$10:$D$42,1)` | 1 |
| `I12` | `I50` | 39 | `=vola` | 0.3 |
| `N56` | `N56` | 1 | `=R6` | 0 |
| `O56` | `O56` | 1 | `=T6` | 0 |

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

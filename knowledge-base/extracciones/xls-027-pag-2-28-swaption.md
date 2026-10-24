# XLS-027: pag 2.28 swaption.xlsm

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-28-swaption.xlsm). SHA-256: `09780e5f51c9c4f4eef8b2d83649f070438d5d3cdb0135c584b882097ff50ffc`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **True**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `deltat` | `Hoja1!$D$9` |
| `fechavalor` | `Hoja1!$D$8` |
| `Nom` | `Hoja1!#REF!` |
| `spread` | `Hoja1!#REF!` |
| `vola` | `Hoja1!#REF!` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `C6:T114`. Celdas con contenido: 653. Fórmulas: 558. Familias: 21.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `M6` | vola |
| `I7` | anualidad |
| `C8` | fecha valor |
| `C9` | deltat |
| `I9` | tipo fwd -swap hoy |
| `M10` | Valoración de swaption payer (call) |
| `R10` | por integración numérica |
| `D12` | datos ccc |
| `H12` | interpolación de descuentos |
| `D14` | fecha |
| `E14` | plazo |
| `F14` | FD |
| `H14` | plazos |
| `I14` | FD |
| `J14` | fwd |
| `M14` | Nominal |
| `M15` | t0 |
| `C16` | 1M |
| `M16` | strike |
| `C17` | 2M |
| `C18` | 3M |
| `M18` | moneyness |
| `C19` | 4M |
| `M19` | vola acum |
| `C20` | 5M |
| `M20` | d+ |
| `C21` | 6M |
| `M21` | d- |
| `C22` | 7M |
| `M22` | Phi(d+) |
| `C23` | 8M |
| `M23` | Phi(d-) |
| `C24` | 9M |
| `M24` | precio |
| `C25` | 10M |
| `C26` | 11M |
| `C27` | 12M |
| `C28` | 2A |
| `C29` | 3A |
| `C30` | 4A |
| `C31` | 5A |
| `C32` | 6A |
| `C33` | 7A |
| `C34` | 8A |
| `C35` | 9A |
| `C36` | 10A |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `N6` | 0.4 | `0%` |
| `D8` | 2021-09-29T00:00:00 | `mm-dd-yy` |
| `N14` | 100000 | `_-* #,##0.00\ "€"_-;\-* #,##0.00\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `Q14` | -5 | `General` |
| `F15` | 1 | `0%` |
| `H15` | 0 | `General` |
| `D16` | 2021-10-28T00:00:00 | `mm-dd-yy` |
| `F16` | 0.999882963564388 | `0.000%` |
| `N16` | 0.02 | `0%` |
| `D17` | 2021-11-28T00:00:00 | `mm-dd-yy` |
| `F17` | 0.999672730078568 | `0.000%` |
| `D18` | 2021-12-28T00:00:00 | `mm-dd-yy` |
| `F18` | 0.99950235222721 | `0.000%` |
| `D19` | 2022-01-28T00:00:00 | `mm-dd-yy` |
| `F19` | 0.998148220022072 | `0.000%` |
| `D20` | 2022-02-27T00:00:00 | `mm-dd-yy` |
| `F20` | 0.99723759959148 | `0.000%` |
| `D21` | 2022-03-30T00:00:00 | `mm-dd-yy` |
| `F21` | 0.996743071028512 | `0.000%` |
| `D22` | 2022-04-30T00:00:00 | `mm-dd-yy` |
| `F22` | 0.994879245263098 | `0.000%` |
| `D23` | 2022-05-30T00:00:00 | `mm-dd-yy` |
| `F23` | 0.994064389815622 | `0.000%` |
| `D24` | 2022-06-30T00:00:00 | `mm-dd-yy` |
| `F24` | 0.993065656345667 | `0.000%` |
| `D25` | 2022-07-30T00:00:00 | `mm-dd-yy` |
| `F25` | 0.992119505512734 | `0.000%` |
| `D26` | 2022-08-30T00:00:00 | `mm-dd-yy` |
| `F26` | 0.991089646786538 | `0.000%` |
| `D27` | 2022-09-30T00:00:00 | `mm-dd-yy` |
| `F27` | 0.990095274882298 | `0.000%` |
| `D28` | 2023-09-30T00:00:00 | `mm-dd-yy` |
| `F28` | 0.978456082991356 | `0.000%` |
| `D29` | 2024-09-29T00:00:00 | `mm-dd-yy` |
| `F29` | 0.965823606183929 | `0.000%` |
| `D30` | 2025-09-29T00:00:00 | `mm-dd-yy` |
| `F30` | 0.941879476032273 | `0.000%` |
| `D31` | 2026-09-30T00:00:00 | `mm-dd-yy` |
| `F31` | 0.927492028234604 | `0.000%` |
| `D32` | 2027-09-30T00:00:00 | `mm-dd-yy` |
| `F32` | 0.893965290556549 | `0.000%` |
| `D33` | 2028-09-29T00:00:00 | `mm-dd-yy` |
| `F33` | 0.863007498467545 | `0.000%` |
| `D34` | 2029-09-29T00:00:00 | `mm-dd-yy` |
| `F34` | 0.834467032944631 | `0.000%` |
| `D35` | 2030-09-30T00:00:00 | `mm-dd-yy` |
| `F35` | 0.80810486467052 | `0.000%` |
| `D36` | 2031-09-30T00:00:00 | `mm-dd-yy` |
| `F36` | 0.783985148346052 | `0.000%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `I8` | `I8` | 1 | `=SUM(I17:I55)*deltat` | 8.819777225110117 |
| `D9` | `D9` | 1 | `=3/12` | 0.25 |
| `I10` | `I10` | 1 | `=(I16-I55)/I8` | 0.024422960062495776 |
| `T12` | `T12` | 1 | `=SUMPRODUCT(R14:R114,T14:T114)*I8` | 4224.6334208374155 |
| `R14` | `R114` | 101 | `=_xlfn.NORM.DIST(Q14,0,1,FALSE)*0.1` | 1.4867195147342977e-07 |
| `S14` | `S114` | 101 | `=$I$10*EXP(-0.5*$N$6^2*$N$15)*EXP($N$6*SQRT($N$15)*Q14)` | 0.008806795822585145 |
| `T14` | `T114` | 101 | `=$N$14*MAX(S14-$N$16,0)` | 0 |
| `D15` | `D15` | 1 | `=(fechavalor)` | 2021-09-29T00:00:00 |
| `E15` | `E36` | 22 | `=YEARFRAC(fechavalor,D15)` | 0 |
| `I15` | `I15` | 1 | `=interpola(H15,$E$15:$F$36)` | 1 |
| `N15` | `N15` | 1 | `=H16` | 0.25 |
| `Q15` | `Q114` | 100 | `=Q14+0.1` | -4.9 |
| `H16` | `H55` | 40 | `=H15+deltat` | 0.25 |
| `I16` | `I55` | 40 | `=interpola(H16,$E$15:$F$36,1)` | 0.9994572144870387 |
| `J16` | `J54` | 39 | `=(I16/I17-1)/deltat` | 0.010831746886775129 |
| `N18` | `N18` | 1 | `=LN(I10/N16)` | 0.19979140246307855 |
| `N19` | `N19` | 1 | `=N6*SQRT(N15)` | 0.2 |
| `N20` | `N20` | 1 | `=N18/N19+0.5*N19` | 1.0989570123153927 |
| `N21` | `N21` | 1 | `=N18/N19-0.5*N19` | 0.8989570123153927 |
| `N22` | `N23` | 2 | `=NORMSDIST(N20)` | 0.8641065915657057 |
| `N24` | `N24` | 1 | `=N14*(I10*N22-N16*N23)*I8` | 4225.375662738867 |

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

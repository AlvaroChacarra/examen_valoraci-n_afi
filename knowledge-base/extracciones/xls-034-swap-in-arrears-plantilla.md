# XLS-034: swap in arrears_Plantilla.xlsm

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos/swap-in-arrears-plantilla.xlsm). SHA-256: `8cf9e078b2b8082ffb32ada3c828b8282e7acae0c77a9fa5b2841cf847ab3ec3`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **True**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

Un nombre local prevalece sobre el nombre de libro al evaluar fórmulas de su hoja. Se incluyen los parámetros Solver, sin ejecutarlo.

| Nombre | Ámbito | Referencia | Oculto |
|---|---|---|---|
| `deltat` | `libro` | `Hoja1!$D$9` | 0 |
| `fechavalor` | `libro` | `Hoja1!$D$8` | 0 |
| `Nom` | `libro` | `Hoja1!$M$9` | 0 |
| `solver_adj` | `Hoja1` | `Hoja1!$Q$9` | 1 |
| `solver_cvg` | `Hoja1` | `0.0001` | 1 |
| `solver_drv` | `Hoja1` | `1` | 1 |
| `solver_eng` | `Hoja1` | `1` | 1 |
| `solver_est` | `Hoja1` | `1` | 1 |
| `solver_itr` | `Hoja1` | `100` | 1 |
| `solver_lin` | `Hoja1` | `2` | 1 |
| `solver_mip` | `Hoja1` | `2147483647` | 1 |
| `solver_mni` | `Hoja1` | `30` | 1 |
| `solver_mrt` | `Hoja1` | `0.075` | 1 |
| `solver_msl` | `Hoja1` | `2` | 1 |
| `solver_neg` | `Hoja1` | `2` | 1 |
| `solver_nod` | `Hoja1` | `2147483647` | 1 |
| `solver_num` | `Hoja1` | `0` | 1 |
| `solver_nwt` | `Hoja1` | `1` | 1 |
| `solver_opt` | `Hoja1` | `Hoja1!$S$14` | 1 |
| `solver_pre` | `Hoja1` | `0.000001` | 1 |
| `solver_rbv` | `Hoja1` | `1` | 1 |
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
| `spread` | `libro` | `Hoja1!$Q$9` | 0 |
| `vola` | `libro` | `Hoja1!$Q$8` | 0 |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `C6:S55`. Celdas con contenido: 205. Fórmulas: 110. Familias: 9.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `I7` | anualidad |
| `C8` | fecha valor |
| `P8` | vola |
| `C9` | deltat |
| `I9` | tipo fwd -swap hoy |
| `L9` | Nominal |
| `P9` | spread |
| `D12` | datos ccc |
| `H12` | interpolación de descuentos |
| `L12` | swap normal |
| `P12` | swap in arrears |
| `L13` | rama variable |
| `M13` | rama fija |
| `P13` | rama variable |
| `Q13` | rama fija |
| `S13` | discrepancia para solver |
| `D14` | fecha |
| `E14` | plazo |
| `F14` | FD |
| `H14` | plazos |
| `I14` | FD |
| `J14` | fwd |
| `L15` | valoración de flujos |
| `O15` | valoración naive |
| `P15` | valoración de flujos |
| `C16` | 1M |
| `C17` | 2M |
| `C18` | 3M |
| `C19` | 4M |
| `C20` | 5M |
| `C21` | 6M |
| `C22` | 7M |
| `C23` | 8M |
| `C24` | 9M |
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
| `D8` | 2021-09-29T00:00:00 | `mm-dd-yy` |
| `Q8` | 0.4 | `0.00%` |
| `M9` | 100000 | `_-* #,##0.00\ "€"_-;\-* #,##0.00\ "€"_-;_-* "-"??\ "€"_-;_-@_-` |
| `E15` | 0 | `0.000` |
| `F15` | 1 | `0%` |
| `H15` | 0 | `General` |
| `D16` | 2021-10-28T00:00:00 | `mm-dd-yy` |
| `F16` | 0.999882963564388 | `0.000%` |
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
| `D9` | `D9` | 1 | `=3/12` | 0.25 |
| `L14` | `M14` | 2 | `=SUM(L17:L55)` | 0 |
| `O14` | `Q14` | 3 | `=SUM(O16:O54)` | 0 |
| `S14` | `S14` | 1 | `=(Q14-P14)*100000000000` | 0 |
| `D15` | `D15` | 1 | `=(fechavalor)` | 2021-09-29T00:00:00 |
| `I15` | `I15` | 1 | `=interpola(H15,$E$15:$F$36)` | 1 |
| `E16` | `E36` | 21 | `=YEARFRAC(fechavalor,D16)` | 0.08055555555555556 |
| `H16` | `H55` | 40 | `=H15+deltat` | 0.25 |
| `I16` | `I55` | 40 | `=interpola(H16,$E$15:$F$36,1)` | 0.9994572144870387 |

### Notas de celdas

- `Q9`: usar solver para determinar spread que hace que el swap in arrears esté equilibrado

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

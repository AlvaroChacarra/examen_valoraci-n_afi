# XLS-028: pag 2.29 valoración bono con cupones.xlsx

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-29-valoracion-bono-con-cupones.xlsx). SHA-256: `fb32c336b043adc4f2757181573931852c9764ce44de7c32643edfec614ea9e1`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `A0` | `Hoja1!$D$11` |
| `corte1` | `Hoja1!$G$12` |
| `corte2` | `Hoja1!$G$13` |
| `deltat` | `Hoja1!$D$4` |
| `Fswap0` | `Hoja1!$D$12` |
| `pago1` | `Hoja1!$H$12` |
| `pago3` | `Hoja1!$H$14` |
| `vola` | `Hoja1!$D$14` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B4:AJ126`. Celdas con contenido: 1146. Fórmulas: 1052. Familias: 34.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C4` | deltat |
| `Y5` | volas |
| `B7` | descuentos |
| `T7` | Versión con smile |
| `W7` | fwd-swap0 |
| `C9` | tipo swap a 5 años que se fijará dentro de 5 años |
| `AB9` | con fórmulas |
| `C11` | anualidad |
| `G11` | cortes |
| `H11` | pagos |
| `W11` | valor |
| `AB11` | pago fijo |
| `C12` | tipo fwd-swap0 |
| `AD12` | moneyness |
| `AE12` | vola acum |
| `AF12` | dmas |
| `AG12` | dmenos |
| `AH12` | phi(dmas) |
| `AI12` | phi(dmenos) |
| `AJ12` | prima |
| `W13` | promedio |
| `Y13` | promedio |
| `C14` | vola |
| `G14` | más de 8% |
| `W14` | prima |
| `Y14` | prima |
| `T16` | valores normal |
| `U16` | probs |
| `W16` | valores de SwapT (6%) |
| `X16` | flujo |
| `Y16` | valores de SwapT (8%) |
| `Z16` | flujo |
| `AD16` | valor |
| `C21` | Valoración por integración |
| `H21` | valor por integración |
| `L21` | Valoración por desestructuración (con fórmulas BS) |
| `L23` | El instrumento equivale a  |
| `C24` | valores normal |
| `D24` | probs |
| `E24` | valores de SwapT |
| `F24` | flujo |
| `H24` | flujo promedio |
| `L24` | instrumento 1 |
| `O24` | pago de |
| `L25` | instrumento 2 |
| `O25` | más 3* swaption de strike |
| `L26` | instrumento 3 |
| `O26` | menos 3* swaption de strike  |
| `J29` | moneyness |
| `K29` | vola acum |
| `L29` | dmas |
| `M29` | dmenos |
| `N29` | phi(dmas) |
| `O29` | phi(dmenos) |
| `Q30` | prima 2 |
| `Q31` | prima 3 |
| `Q32` | prima 1 |
| `N34` | valor por desestructuración |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D4` | 1 | `General` |
| `C6` | 1 | `General` |
| `D6` | 2 | `General` |
| `E6` | 3 | `General` |
| `F6` | 4 | `General` |
| `G6` | 5 | `General` |
| `H6` | 6 | `General` |
| `I6` | 7 | `General` |
| `J6` | 8 | `General` |
| `K6` | 9 | `General` |
| `L6` | 10 | `General` |
| `X6` | 0.06 | `0%` |
| `Y6` | 0.26 | `0%` |
| `C7` | 0.99456 | `0.000%` |
| `D7` | 0.9912 | `0.000%` |
| `E7` | 0.98434 | `0.000%` |
| `F7` | 0.9625 | `0.000%` |
| `G7` | 0.94312 | `0.000%` |
| `H7` | 0.92245 | `0.000%` |
| `I7` | 0.90455 | `0.000%` |
| `J7` | 0.85674 | `0.000%` |
| `K7` | 0.79987 | `0.000%` |
| `L7` | 0.73491 | `0.000%` |
| `Y7` | 0.25 | `0%` |
| `X8` | 0.08 | `0%` |
| `Y8` | 0.24 | `0%` |
| `G12` | 0.06 | `0%` |
| `H12` | 0.03 | `0%` |
| `G13` | 0.08 | `0%` |
| `AC13` | 1 | `General` |
| `D14` | 0.25 | `0%` |
| `H14` | 0.09 | `0%` |
| `AC14` | 2 | `General` |
| `P24` | 0.03 | `0%` |
| `P25` | 0.06 | `0%` |
| `P26` | 0.08 | `0%` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `X7` | `X7` | 1 | `=Fswap0` | 0.049356172306875404 |
| `D11` | `D11` | 1 | `=SUM(H7:L7)*deltat` | 4.21852 |
| `X11` | `X11` | 1 | `=3%*A0+X14-Z14` | 0.18409231391528105 |
| `AC11` | `AC11` | 1 | `=3%*A0` | 0.1265556 |
| `D12` | `D12` | 1 | `=(G7-L7)/D11` | 0.049356172306875404 |
| `X13` | `X13` | 1 | `=SUMPRODUCT(X18:X118,U18:U118)` | 0.02358509434462207 |
| `Z13` | `Z13` | 1 | `=SUMPRODUCT(Z18:Z118,U18:U118)` | 0.00994601857509127 |
| `AD13` | `AD13` | 1 | `=LN(Fswap0/X6)` | -0.19528173208899355 |
| `AE13` | `AE13` | 1 | `=Y6*SQRT($G$6)` | 0.5813776741499453 |
| `AF13` | `L31` | 4 | `=AD13/AE13+0.5*AE13` | -0.04520595347494394 |
| `AG13` | `M31` | 4 | `=AD13/AE13-0.5*AE13` | -0.6265836276248893 |
| `AH13` | `O31` | 8 | `=NORMSDIST(AF13)` | 0.48197157445833827 |
| `AJ13` | `AJ13` | 1 | `=A0*(Fswap0*AH13-X6*AI13)*3` | 0.09947657395621137 |
| `X14` | `Z14` | 2 | `=X13*A0` | 0.09949419219467509 |
| `AD14` | `AD14` | 1 | `=LN(Fswap0/X8)` | -0.48296380454077464 |
| `AE14` | `AE14` | 1 | `=Y8*SQRT($G$6)` | 0.5366563145999496 |
| `AJ14` | `AJ14` | 1 | `=A0*(Fswap0*AH14-X8*AI14)*3` | 0.041930581574201105 |
| `AE16` | `AE16` | 1 | `=AC11+AJ13-AJ14` | 0.18410159238201027 |
| `T18` | `C26` | 2 | `=-5` | -5 |
| `U18` | `D126` | 202 | `=NORMDIST(T18,0,1,FALSE)*0.1` | 1.4867195147342977e-07 |
| `W18` | `W118` | 101 | `=Fswap0*EXP(-0.5*$Y$6^2*$G$6)*EXP($Y$6*SQRT($G$6)*T18)` | 0.002277718899293475 |
| `X18` | `X118` | 101 | `=3*MAX(W18-$X$6,0)` | 0 |
| `Y18` | `Y118` | 101 | `=Fswap0*EXP(-0.5*$Y$8^2*$G$6)*EXP($Y$8*SQRT($G$6)*T18)` | 0.002920577168325395 |
| `Z18` | `Z118` | 101 | `=3*MAX(Y18-$X$8,0)` | 0 |
| `T19` | `C126` | 200 | `=T18+0.1` | -4.9 |
| `H22` | `H22` | 1 | `=H25*A0` | 0.17388683793700607 |
| `H25` | `H25` | 1 | `=SUMPRODUCT(F26:F126,D26:D126)` | 0.04121986809046919 |
| `E26` | `E126` | 101 | `=Fswap0*EXP(-0.5*vola^2*$G$6)*EXP(vola*SQRT($G$6)*C26)` | 0.0025798412299435553 |
| `F26` | `F126` | 101 | `=IF(E26<corte1,pago1,IF(E26<corte2,pago1+3*(E26-corte1),pago3))` | 0.03 |
| `J30` | `J31` | 2 | `=LN(Fswap0/P25)` | -0.19528173208899355 |
| `K30` | `K31` | 2 | `=vola*SQRT($G$6)` | 0.5590169943749475 |
| `P30` | `P31` | 2 | `=A0*(Fswap0*N30-P25*O30)*3` | 0.09391380684428069 |
| `P32` | `P32` | 1 | `=P24*A0` | 0.1265556 |
| `N35` | `N35` | 1 | `=P32+P30-P31` | 0.17390673457200465 |

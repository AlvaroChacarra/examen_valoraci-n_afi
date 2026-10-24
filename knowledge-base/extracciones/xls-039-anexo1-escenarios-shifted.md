# XLS-039: Anexo1.-escenarios-shifted.xlsx

Original: [archivo raw](../../raw/marco-black/anexos-valoracion-marco-black-soluciones/anexo1-escenarios-shifted.xlsx). SHA-256: `6745dfd770fe25ce891e4623f9b80881f335e44237b987be2371d73bae522460`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `DT` | `Hoja1!$D$7` |
| `F0` | `Hoja1!$D$6` |
| `shift` | `Hoja1!$D$11` |
| `strike` | `Hoja1!$M$26` |
| `T` | `Hoja1!$D$8` |
| `volash` | `Hoja1!$D$9` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `C6:P98`. Celdas con contenido: 456. Fórmulas: 423. Familias: 13.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C6` | F0 |
| `C7` | DT |
| `E7` | año |
| `C8` | T |
| `E8` | año |
| `C9` | vola sh |
| `C10` | descuento T+DT |
| `C11` | sh |
| `D15` | normal |
| `E15` | probs |
| `F15` | escenarios de F_T |
| `G15` | probs |
| `H15` | Payoff |
| `J26` | Valoración del caplet |
| `L26` | K |
| `L27` | Nominal |
| `J28` | con fórmula |
| `J30` | moneyness |
| `K30` | vola acum |
| `L30` | d+ |
| `M30` | d- |
| `N30` | Phi(d+) |
| `O30` | Phi(d-) |
| `P30` | precio |
| `J33` | con numérico |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D6` | -0.003 | `0.00%` |
| `D8` | 1 | `General` |
| `D9` | 0.3 | `0%` |
| `D10` | 0.995 | `0.00%` |
| `D11` | 0.03 | `0%` |
| `D16` | -4 | `General` |
| `M26` | -0.004 | `0.00%` |
| `M27` | 1000000 | `#,##0.00` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `D7` | `D7` | 1 | `=1/4` | 0.25 |
| `E16` | `E98` | 83 | `=NORMDIST(D16,0,1,FALSE)*0.1` | 1.3383022576488537e-05 |
| `F16` | `F98` | 83 | `=(F0+shift)*EXP(-0.5*volash^2*T)*EXP(volash*SQRT(T)*D16)-shift` | -0.0222255954804692 |
| `G16` | `G98` | 83 | `=E16` | 1.3383022576488537e-05 |
| `H16` | `H98` | 83 | `=MAX(F16-strike,0)` | 0 |
| `D17` | `D98` | 82 | `=D16+0.1` | -3.9 |
| `J31` | `J31` | 1 | `=LN((F0+shift)/(strike+shift))` | 0.03774032798284711 |
| `K31` | `K31` | 1 | `=volash*T` | 0.3 |
| `L31` | `L31` | 1 | `=J31/K31+0.5*K31` | 0.27580109327615704 |
| `M31` | `M31` | 1 | `=J31/K31-0.5*K31` | -0.02419890672384295 |
| `N31` | `O31` | 2 | `=NORMSDIST(L31)` | 0.6086495780214555 |
| `P31` | `P31` | 1 | `=DT*D10*((F0+shift)*N31-(strike+shift)*O31)*M27` | 916.5236669789778 |
| `M34` | `M34` | 1 | `=DT*D10*SUMPRODUCT(H16:H98,G16:G98)*M27` | 916.3980089358088 |

### Gráficos y rangos de origen

```json
[
  {
    "type": "ScatterChart",
    "title": "",
    "series": [
      {
        "xVal": "Hoja1!$F$16:$F$98",
        "yVal": "Hoja1!$G$16:$G$98"
      }
    ]
  }
]
```

## Hoja: Hoja2

Estado: `visible`. Rango usado: `A1:A1`. Celdas con contenido: 0. Fórmulas: 0. Familias: 0.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| — | No hay etiquetas de texto |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|

## Hoja: Hoja3

Estado: `visible`. Rango usado: `A1:A1`. Celdas con contenido: 0. Fórmulas: 0. Familias: 0.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| — | No hay etiquetas de texto |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|

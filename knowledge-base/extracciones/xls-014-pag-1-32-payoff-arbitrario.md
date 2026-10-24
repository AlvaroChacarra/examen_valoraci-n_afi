# XLS-014: pag 1.32 payoff arbitrario.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-32-payoff-arbitrario.xlsx). SHA-256: `3c28f48c6a2825a495aa0506634f70b68958244cc3d05006010d26229c6323c3`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `corte1` | `Ejercicio!$D$12` |
| `corte2` | `Ejercicio!$D$13` |
| `corte3` | `Ejercicio!$D$14` |
| `div` | `Ejercicio!$D$6` |
| `paso` | `Ejercicio!$D$21` |
| `S0` | `Ejercicio!$D$7` |
| `sigma` | `Ejercicio!$D$8` |
| `T` | `Ejercicio!$D$4` |
| `tipo` | `Ejercicio!$D$5` |

## Hoja: Ejercicio

Estado: `visible`. Rango usado: `C3:S2207`. Celdas con contenido: 9285. Fórmulas: 7054. Familias: 19.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C3` | Datos |
| `C4` | T |
| `C5` | tipo |
| `C6` | tasa divid |
| `C7` | S0 |
| `C8` | sigma |
| `F10` | La función f es |
| `C12` | corte1 |
| `C13` | corte2 |
| `C14` | corte3 |
| `Q16` | numsims |
| `C18` | cálculo numérico de la integral |
| `I18` | Cálculo por desestructuración  |
| `P18` | cálculo por simulación |
| `F20` | valor numérico |
| `R20` | valor por simulación |
| `C21` | paso |
| `J21` |  1 call comprada con K=corte1 |
| `J22` |  2 calls vendidas de K=corte2  |
| `C23` | valores normal |
| `D23` | probs |
| `E23` | S_T |
| `F23` | payoff |
| `J23` |  1 call comprada de K=corte3 |
| `Q23` | normal |
| `R23` | S_T |
| `S23` | payoff |
| `I25` | Calculamos los precios con las fórmulas de B-S |
| `J27` | moneyness |
| `K27` | vola acum |
| `L27` | d+ |
| `M27` | d- |
| `N27` | precios |
| `I28` | strike corte1 |
| `I29` | strike corte2 |
| `I30` | strike corte3 |
| `K32` | valor por desestructuración |
| `P24 … P2207` | sim1 … sim2184 (2184 etiquetas consecutivas, compactadas) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D4` | 0.5 | `General` |
| `D5` | 0.01 | `0%` |
| `D6` | 0 | `0%` |
| `D7` | 42 | `General` |
| `D8` | 0.2 | `0%` |
| `D12` | 30 | `General` |
| `D13` | 40 | `General` |
| `D14` | 50 | `General` |
| `D21` | 0.1 | `General` |
| `C25` | -6 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `R16` | `R16` | 1 | `=COUNT(S24:S2207)` | 2184 |
| `F21` | `F21` | 1 | `=SUMPRODUCT(F25:F145,D25:D145)*EXP(-tipo*T)` | 5.388956549248451 |
| `R21` | `R21` | 1 | `=AVERAGE(S24:S2207)*EXP(-tipo*T)` | 5.284175642880174 |
| `Q24` | `Q2207` | 2184 | `=NORMSINV(RAND())` | 1.8273148784289743 |
| `R24` | `R2207` | 2184 | `=S0*EXP((tipo-0.5*sigma^2)*T)*EXP(sigma*SQRT(T)*Q24)` | 54.11389362560549 |
| `S24` | `S2207` | 2305 | `=IF(R24<=corte1,0,IF(R24<=corte2,R24-corte1,IF(R24<=corte3,corte3-R24,0)))` | 0 |
| `D25` | `D145` | 121 | `=NORMDIST(C25,0,1,FALSE)*paso` | 6.075882849823286e-10 |
| `E25` | `E145` | 121 | `=S0*EXP((tipo-0.5*sigma^2)*T)*EXP(sigma*SQRT(T)*C25)` | 17.888203636126562 |
| `C26` | `C145` | 120 | `=C25+paso` | -5.9 |
| `J28` | `J28` | 1 | `=LN(S0*EXP(tipo*T)/corte1)` | 0.3414722366212129 |
| `K28` | `K30` | 3 | `=sigma*SQRT(T)` | 0.14142135623730953 |
| `L28` | `L30` | 3 | `=J28/K28+0.5*K28` | 2.485284019136624 |
| `M28` | `M30` | 3 | `=J28/K28-0.5*K28` | 2.3438626628993147 |
| `N28` | `N28` | 1 | `=S0*NORMSDIST(L28)-corte1*EXP(-tipo*T)*NORMSDIST(M28)` | 12.162634737987865 |
| `J29` | `J29` | 1 | `=LN(S0*EXP(tipo*T)/corte2)` | 0.05379016416943189 |
| `N29` | `N29` | 1 | `=S0*NORMSDIST(L29)-corte2*EXP(-tipo*T)*NORMSDIST(M29)` | 3.569849048924663 |
| `J30` | `J30` | 1 | `=LN(S0*EXP(tipo*T)/corte3)` | -0.16935338714477788 |
| `N30` | `N30` | 1 | `=S0*NORMSDIST(L30)-corte3*EXP(-tipo*T)*NORMSDIST(M30)` | 0.36392124466886777 |
| `K33` | `K33` | 1 | `=N28-2*N29+N30` | 5.386857884807407 |

### Gráficos y rangos de origen

```json
[
  {
    "type": "LineChart",
    "title": "",
    "series": [
      {
        "val": "Ejercicio!$F$25:$F$145",
        "cat": "Ejercicio!$E$25:$E$145"
      }
    ]
  }
]
```

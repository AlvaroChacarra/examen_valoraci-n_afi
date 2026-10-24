# XLS-018: 1.1.call-cobertura discreta_Plantilla.xlsx

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity/1-1-call-cobertura-discreta-plantilla.xlsx). SHA-256: `6bc583ae5097450097770f586dfa9bb10f92afcc2e5f1b79c707461622edb28b`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `deltat` | `Ejercicio!$G$28` |
| `K` | `Ejercicio!$D$12` |
| `numsims` | `Ejercicio!$O$60` |
| `pasohist` | `Ejercicio!$O$65` |
| `S0` | `Ejercicio!$D$14` |
| `sigma` | `Ejercicio!$D$15` |
| `T` | `Ejercicio!$D$11` |
| `tipo` | `Ejercicio!$D$13` |

## Hoja: Ejercicio

Estado: `visible`. Rango usado: `A10:AF4961`. Celdas con contenido: 5013. Fórmulas: 27. Familias: 2.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C10` | Datos |
| `F10` | Cálculos intermedios |
| `C11` | T |
| `F11` | moneyness |
| `C12` | K |
| `F12` | vola acumulada |
| `C13` | tipo |
| `F13` | d+ |
| `C14` | S0 |
| `F14` | d- |
| `C15` | sigma |
| `F15` | Phi(d+) |
| `F16` | Phi(d-) |
| `C19` | Primas |
| `D19` | prima |
| `E19` | prima/S0 |
| `C20` | call |
| `C21` | put |
| `C22` | fwd |
| `C28` | cobertura discreta de la call |
| `F28` | deltat |
| `B31` | Subyacente |
| `C32` | instante |
| `C33` | tiempo |
| `C34` | sorteos normal |
| `C35` | evolución subyacente |
| `B37` | Deltas |
| `C38` | S |
| `C39` | tiempo a venc |
| `C40` | d+ |
| `C41` | senda de deltas |
| `B43` | Cartera replicante |
| `C44` | instante |
| `C45` | unidades de suby |
| `C46` | cash |
| `C47` | valor cartera |
| `B49` | Resumen del resultado de la simulación |
| `C50` | pago call |
| `C51` | valor cartera replicante |
| `C52` | descasamiento |
| `C57` | tabla de simulaciones |
| `N58` | histograma |
| `N60` | numsims |
| `N62` | media |
| `Q62` | percentil 5% |
| `N63` | max |
| `N64` | min |
| `N65` | pasohist |
| `O67` | clases |
| `Q67` | frecs relativas |
| `C59 … C4961` | sim1 … sim4903 (4903 etiquetas consecutivas, compactadas) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D11` | 0.5 | `General` |
| `D12` | 40 | `General` |
| `D13` | 0.01 | `0.00%` |
| `D14` | 42 | `General` |
| `D15` | 0.2 | `0.00%` |
| `D32` | 0 | `General` |
| `E32` | 1 | `General` |
| `F32` | 2 | `General` |
| `G32` | 3 | `General` |
| `H32` | 4 | `General` |
| `I32` | 5 | `General` |
| `J32` | 6 | `General` |
| `K32` | 7 | `General` |
| `L32` | 8 | `General` |
| `M32` | 9 | `General` |
| `N32` | 10 | `General` |
| `O32` | 11 | `General` |
| `P32` | 12 | `General` |
| `Q32` | 13 | `General` |
| `R32` | 14 | `General` |
| `S32` | 15 | `General` |
| `T32` | 16 | `General` |
| `U32` | 17 | `General` |
| `V32` | 18 | `General` |
| `W32` | 19 | `General` |
| `X32` | 20 | `General` |
| `Y32` | 21 | `General` |
| `Z32` | 22 | `General` |
| `AA32` | 23 | `General` |
| `AB32` | 24 | `General` |
| `AC32` | 25 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `G28` | `G28` | 1 | `=1/50` | 0.02 |
| `D44` | `AC44` | 26 | `=D32*deltat` | 0 |

### Notas de celdas

- `G28`: recalculamos la cartera de cobertura cada 0.02 años

- `D47`: Ponemos la prima de la call como valor inicial de la cartera de cobertura
- `R62`: el ejercicio concluye variando la prima que se ha de cobrar (celda D51) para que aquí aparezca un 0. Es decir, para que en el 95% de los escenarios el descasamiento sea positivo. Ese valor será la prima original más, claro, este percentil.

## Textos en objetos de dibujo

```json
[
  {
    "part": "xl/drawings/drawing1.xml",
    "text": [
      "Pretendemos cubrir una call rebalanceando la cartera de cobertura mensualmente: cada mes recomponemos nuestra cartera con la delta que vayamos calculando. Hallar por simulación el histograma de los posibles descasamientos. Calcular la prima que habrá que cobrar para que, con un 95 % de probabilidad, el descasamiento sea positivo"
    ]
  }
]
```

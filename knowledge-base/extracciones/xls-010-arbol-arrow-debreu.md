# XLS-010: Arbol arrow-debreu.xlsx

Original: [archivo raw](../../raw/fundamentos/sesioniii/arbol-arrow-debreu.xlsx). SHA-256: `73502d3186c05471eed13965cf0652e94924ca1a443ee8b85a4e2e0d760fda84`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `d` | `Hoja1!$H$12` |
| `deltat` | `Hoja1!$D$11` |
| `factorVola` | `Hoja1!$J$11` |
| `S0` | `Hoja1!$D$7` |
| `T` | `Hoja1!$D$12` |
| `tipo` | `Hoja1!$D$5` |
| `u` | `Hoja1!$H$11` |
| `vola` | `Hoja1!$D$6` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `C1:XFD66`. Celdas con contenido: 129. Fórmulas: 56. Familias: 13.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `XFD1` | . |
| `C3` | Datos de mercado |
| `C5` | tipo |
| `C6` | volatilidad |
| `C7` | S0 |
| `G8` | Cálculo de los parámetros JR |
| `C9` | Datos del modelo |
| `I10` | deriva tipos |
| `J10` | factor(vola) |
| `K10` | ruido |
| `C11` | Deltat |
| `G11` | u |
| `C12` | Vencimiento |
| `G12` | d |
| `G13` | p |
| `C15` | Árbol de evolución de los valores del subyacente |
| `C17` | tiempo |
| `C29` | Valoración de opciones europeas con el árbol de Arrow-Debreu |
| `C32` | Construcción del árbol de Arrow-Debreu |
| `C34` | tiempo |
| `C44` | sumas |
| `C45` | descuentos |
| `C48` | Valoración de una cartera de opciones europeas |
| `C50` | Call1 |
| `D50` | strike1 |
| `F50` | T1 |
| `C51` | Call2 |
| `D51` | strike2 |
| `F51` | T2 |
| `C52` | Put3 |
| `D52` | strike3 |
| `F52` | T3 |
| `C54` | Árbol de payoffs de la cartera |
| `C56` | tiempo |
| `C65` | Valoración usando el árbol de Arrow-Debreu |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D5` | 0.006 | `0.0%` |
| `D6` | 0.3 | `0%` |
| `D7` | 80 | `General` |
| `H13` | 0.5 | `0%` |
| `D17` | 0 | `General` |
| `E17` | 1 | `General` |
| `F17` | 2 | `General` |
| `G17` | 3 | `General` |
| `H17` | 4 | `General` |
| `I17` | 5 | `General` |
| `J17` | 6 | `General` |
| `E34` | 1 | `General` |
| `F34` | 2 | `General` |
| `G34` | 3 | `General` |
| `H34` | 4 | `General` |
| `I34` | 5 | `General` |
| `J34` | 6 | `General` |
| `D35` | 0 | `General` |
| `E35` | 0 | `General` |
| `F35` | 0 | `General` |
| `G35` | 0 | `General` |
| `H35` | 0 | `General` |
| `I35` | 0 | `General` |
| `J35` | 0 | `General` |
| `E50` | 86 | `General` |
| `G50` | 6 | `General` |
| `E51` | 75 | `General` |
| `G51` | 5 | `General` |
| `E52` | 68 | `General` |
| `G52` | 4 | `General` |
| `E56` | 1 | `General` |
| `F56` | 2 | `General` |
| `G56` | 3 | `General` |
| `H56` | 4 | `General` |
| `I56` | 5 | `General` |
| `J56` | 6 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `D11` | `D11` | 1 | `=1/12` | 0.08333333333333333 |
| `H11` | `H12` | 2 | `=I11*J11*K11` | 1.0869300107425321 |
| `I11` | `I12` | 2 | `=EXP(tipo*deltat)` | 1.0005001250208359 |
| `J11` | `J12` | 2 | `=2/(EXP(vola*SQRT(deltat))+EXP(-vola*SQRT(deltat)))` | 0.9962616831161694 |
| `K11` | `K11` | 1 | `=EXP(vola*SQRT(deltat))` | 1.0904631784921235 |
| `D12` | `D12` | 1 | `=6*deltat` | 0.5 |
| `K12` | `K12` | 1 | `=EXP(-vola*SQRT(deltat))` | 0.9170415101799084 |
| `D18` | `D18` | 1 | `=S0` | 80 |
| `E18` | `J18` | 6 | `=D18*u` | 86.95440085940257 |
| `E19` | `J24` | 21 | `=D18*d` | 73.12561914393117 |
| `H57` | `H61` | 5 | `=MAX($E$52-H18,0)` | 0 |
| `I57` | `I62` | 6 | `=MAX(I18-$E$51,0)` | 46.36623712461321 |
| `J57` | `J63` | 7 | `=MAX(J18-$E$50,0)` | 45.91660542163655 |

### Notas de celdas

- `D35`: estos ceros son auxiliares, para dar cuenta de la situación en los "bordes"

- `G44`: observa cómo la suma de los precios de los AD de un cierto tiempo coincide con el descuento de esa fecha

- `C66`: valoramos la cartera completa con una simple multiplicación por los precios de los AD


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

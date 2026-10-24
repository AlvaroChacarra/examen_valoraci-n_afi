# XLS-002: Grandes números-2-correlación.xlsx

Original: [archivo raw](../../raw/fundamentos/ejercicios-valoracion-fundamentos-1/grandes-numeros-2-correlacion.xlsx). SHA-256: `5cb77c881df07cab89cb715db89222873f62ee3c6fa972885aed620fd6156372`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

| Nombre | Referencia |
|---|---|
| `epsilon` | `Hoja1!$N$9` |
| `N` | `Hoja1!$I$11` |
| `numsims` | `Hoja1!$T$14` |
| `p` | `Hoja1!$D$2` |
| `rho` | `Hoja1!$D$3` |
| `sigma` | `Hoja1!$I$15` |
| `sims` | `Hoja1!$L$12:$L$1011` |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B2:U1011`. Celdas con contenido: 6707. Fórmulas: 4086. Familias: 23.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `C2` | p |
| `C3` | rho |
| `B6` | una simulación |
| `K6` | promedio |
| `K7` | desv típica |
| `C9` | normales indeps |
| `D9` | normales correladas |
| `F9` | bernoullis correladas |
| `K9` | Tabla de simulaciones |
| `M9` | epsilon |
| `O9` | ¿dentro del intervalo? |
| `M10` | intevalo |
| `Q10` | proporción |
| `B11` | Y |
| `H11` | N |
| `H12` | suma |
| `Q12` | "con TLC" |
| `H14` | N*E(X) |
| `S14` | numsims |
| `H15` | sigma |
| `S15` | mínimo |
| `T15` | máximo |
| `S17` | clases |
| `S18` | longitud |
| `B12 … B307` | Z1 … Z296 (296 etiquetas consecutivas, compactadas) |
| `E12 … E307` | X1 … X296 (296 etiquetas consecutivas, compactadas) |
| `K12 … K1011` | sim1 … sim1000 (1000 etiquetas consecutivas, compactadas) |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `D2` | 0.5 | `General` |
| `D3` | 0 | `0%` |
| `N9` | 10 | `General` |
| `L13` | 155 | `General` |
| `L14` | 137 | `General` |
| `L15` | 152 | `General` |
| `L16` | 145 | `General` |
| `L17` | 142 | `General` |
| `T17` | 40 | `General` |
| `L18` | 142 | `General` |
| `T18` | 5 | `General` |
| `L19` | 149 | `General` |
| `L20` | 141 | `General` |
| `S20` | 0 | `General` |
| `L21` | 146 | `General` |
| `L22` | 144 | `General` |
| `L23` | 138 | `General` |
| `L24` | 159 | `General` |
| `L25` | 140 | `General` |
| `L26` | 137 | `General` |
| `L27` | 141 | `General` |
| `L28` | 138 | `General` |
| `L29` | 144 | `General` |
| `L30` | 145 | `General` |
| `L31` | 159 | `General` |
| `L32` | 145 | `General` |
| `L33` | 149 | `General` |
| `L34` | 151 | `General` |
| `L35` | 164 | `General` |
| `L36` | 145 | `General` |
| `L37` | 141 | `General` |
| `L38` | 145 | `General` |
| `L39` | 160 | `General` |
| `L40` | 157 | `General` |
| `L41` | 153 | `General` |
| `L42` | 145 | `General` |
| `L43` | 145 | `General` |
| `L44` | 147 | `General` |
| `L45` | 151 | `General` |
| `L46` | 164 | `General` |
| `L47` | 154 | `General` |
| `L48` | 152 | `General` |
| `L49` | 171 | `General` |
| `L50` | 165 | `General` |
| `L51` | 157 | `General` |
| `L52` | 151 | `General` |
| `L53` | 165 | `General` |
| `L54` | 141 | `General` |
| `L55` | 144 | `General` |
| `L56` | 168 | `General` |
| `L57` | 155 | `General` |
| `L58` | 155 | `General` |
| `L59` | 151 | `General` |
| `L60` | 153 | `General` |
| `L61` | 140 | `General` |
| `L62` | 131 | `General` |
| `L63` | 144 | `General` |
| `L64` | 147 | `General` |
| `L65` | 158 | `General` |
| `L66` | 142 | `General` |
| `L67` | 145 | `General` |
| `L68` | 143 | `General` |
| `L69` | 151 | `General` |
| `L70` | 148 | `General` |
| `L71` | 156 | `General` |
| `L72` | 135 | `General` |
| `L73` | 152 | `General` |
| `L74` | 163 | `General` |
| `L75` | 157 | `General` |
| `L76` | 148 | `General` |
| `L77` | 142 | `General` |
| `L78` | 143 | `General` |
| `L79` | 163 | `General` |
| `L80` | 168 | `General` |
| `L81` | 154 | `General` |
| `L82` | 151 | `General` |
| `L83` | 149 | `General` |
| `L84` | 151 | `General` |
| `L85` | 144 | `General` |
| `L86` | 133 | `General` |
| `L87` | 140 | `General` |
| `L88` | 163 | `General` |
| `L89` | 136 | `General` |
| `L90` | 143 | `General` |
| `L91` | 144 | `General` |
| `L92` | 164 | `General` |
| `L93` | 151 | `General` |
| `L94` | 160 | `General` |
| `L95` | 141 | `General` |
| `L96` | 159 | `General` |
| `L97` | 150 | `General` |
| `L98` | 144 | `General` |
| `L99` | 161 | `General` |
| `L100` | 146 | `General` |

Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):

| Columna | Primera / última celda | N | Primer / último valor |
|---|---|---:|---|
| L | `L101` / `L1011` | 911 | 160 / 130 |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `L6` | `L6` | 1 | `=AVERAGE(L12:L1011)` | 148.595 |
| `L7` | `L7` | 1 | `=STDEV(L12:L1011)` | 8.596678304896487 |
| `C11` | `C307` | 297 | `=NORMSINV(RAND())` | 0.7235853072715372 |
| `I11` | `I11` | 1 | `=COUNT(F12:F307)` | 296 |
| `L11` | `L11` | 1 | `=I12` | 150 |
| `M11` | `M1011` | 1001 | `=$I$14-epsilon` | 138 |
| `N11` | `N1011` | 1001 | `=$I$14+epsilon` | 158 |
| `Q11` | `Q11` | 1 | `=AVERAGE(O12:O1011)` | 0.782 |
| `D12` | `D307` | 296 | `=SQRT(rho)*$C$11+SQRT(1-rho)*C12` | -0.2108736471218546 |
| `F12` | `F307` | 296 | `=IF(D12<NORMSINV(p),1,0)` | 1 |
| `I12` | `I12` | 1 | `=SUM(OFFSET(F12,0,0,I11,1))` | 150 |
| `L12` | `L12` | 1 | `<DataTableFormula: {'ref': 'L12:L1011', 'ca': '1', 'dt2D': '0', 'dtr': '0', 'r1': 'K11', 'r2': None, 'del1': False, 'del2': False}>` | 145 |
| `O12` | `O1011` | 1000 | `=IF(AND(L12>=M12,L12<=N12),1,0)` | 1 |
| `Q13` | `Q13` | 1 | `=1-2*NORMSDIST(-epsilon/(sigma*SQRT(N)))` | 0.7549579893676138 |
| `I14` | `I14` | 1 | `=I11*p` | 148 |
| `T14` | `T14` | 1 | `=COUNT(sims)` | 1000 |
| `I15` | `I15` | 1 | `=SQRT(p*(1-p))` | 0.5 |
| `S16` | `S16` | 1 | `=MIN(sims)` | 116 |
| `T16` | `T16` | 1 | `=MAX(sims)` | 175 |
| `T20` | `T80` | 61 | `=COUNTIF(sims,"<="&S20)/numsims` | 0 |
| `U20` | `U20` | 1 | `=T20` | 0 |
| `S21` | `S80` | 60 | `=S20+$T$18` | 5 |
| `U21` | `U80` | 60 | `=T21-T20` | 0 |

### Notas de celdas

- `D3`: jcontreras: cambia la correlación (entre 0 y 1)  y comprueba el efecto en el histograma


### Gráficos y rangos de origen

```json
[
  {
    "type": "BarChart",
    "title": "",
    "series": [
      {
        "val": "Hoja1!$U$20:$U$80",
        "cat": "Hoja1!$S$20:$S$80"
      }
    ]
  }
]
```

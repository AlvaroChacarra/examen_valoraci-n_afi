# XLS-004: plantilla2.xlsx

Original: [archivo raw](../../raw/fundamentos/ejercicios-valoracion-fundamentos-1/plantilla2.xlsx). SHA-256: `781b724ecc8a97872e549a79b4c1257db82be9d8f7d04721cd0b1ee1e95eadb7`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

Un nombre local prevalece sobre el nombre de libro al evaluar fórmulas de su hoja. Se incluyen los parámetros Solver, sin ejecutarlo.

| Nombre | Ámbito | Referencia | Oculto |
|---|---|---|---|
| `Num0` | `libro` | `Hoja1!$R$9` | 0 |
| `solver_adj` | `Hoja1` | `Hoja1!$F$64:$F$66` | 1 |
| `solver_cvg` | `Hoja1` | `0.0001` | 1 |
| `solver_drv` | `Hoja1` | `1` | 1 |
| `solver_eng` | `Hoja1` | `1` | 1 |
| `solver_est` | `Hoja1` | `1` | 1 |
| `solver_itr` | `Hoja1` | `10000` | 1 |
| `solver_lhs1` | `Hoja1` | `Hoja1!$U$21` | 1 |
| `solver_lhs2` | `Hoja1` | `Hoja1!$U$20` | 1 |
| `solver_lhs3` | `Hoja1` | `Hoja1!$U$21` | 1 |
| `solver_lin` | `Hoja1` | `2` | 1 |
| `solver_mip` | `Hoja1` | `2147483647` | 1 |
| `solver_mni` | `Hoja1` | `30` | 1 |
| `solver_mrt` | `Hoja1` | `0.075` | 1 |
| `solver_msl` | `Hoja1` | `2` | 1 |
| `solver_neg` | `Hoja1` | `2` | 1 |
| `solver_nod` | `Hoja1` | `2147483647` | 1 |
| `solver_num` | `Hoja1` | `0` | 1 |
| `solver_nwt` | `Hoja1` | `1` | 1 |
| `solver_opt` | `Hoja1` | `Hoja1!$I$65` | 1 |
| `solver_pre` | `Hoja1` | `0.0000000001` | 1 |
| `solver_rbv` | `Hoja1` | `1` | 1 |
| `solver_rel1` | `Hoja1` | `3` | 1 |
| `solver_rel2` | `Hoja1` | `3` | 1 |
| `solver_rel3` | `Hoja1` | `3` | 1 |
| `solver_rhs1` | `Hoja1` | `0` | 1 |
| `solver_rhs2` | `Hoja1` | `0` | 1 |
| `solver_rhs3` | `Hoja1` | `0` | 1 |
| `solver_rlx` | `Hoja1` | `1` | 1 |
| `solver_rsd` | `Hoja1` | `0` | 1 |
| `solver_scl` | `Hoja1` | `2` | 1 |
| `solver_sho` | `Hoja1` | `2` | 1 |
| `solver_ssz` | `Hoja1` | `100` | 1 |
| `solver_tim` | `Hoja1` | `10000` | 1 |
| `solver_tol` | `Hoja1` | `0.05` | 1 |
| `solver_typ` | `Hoja1` | `3` | 1 |
| `solver_val` | `Hoja1` | `0` | 1 |
| `solver_ver` | `Hoja1` | `3` | 1 |
| `tipo` | `libro` | `Hoja1!$E$16` | 0 |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B3:AA71`. Celdas con contenido: 111. Fórmulas: 17. Familias: 4.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `R3` | Elegimos como numerario el activo S1 |
| `Q5` | numerario N |
| `J7` |   |
| `B12` | Modelo: tres activos, con los siguientes valores en cada uno de los escenarios: |
| `D16` | r |
| `X16` | cálculos para nodos finales |
| `Z16` | cálculos para nodo inicial |
| `U18` | probabilidades |
| `B19` | activo S1 |
| `Q19` | activo S1/N |
| `Y26` | error en a |
| `Y28` | error en b |
| `B29` | activo S2 |
| `Q29` | activo S2/N |
| `Y30` | error en c |
| `AA31` | error inicial |
| `B39` | activo S3 |
| `Q39` | activo S3/N |
| `R49` | Una vez calculadas las probabilidades de valoración, |
| `B50` | Valoración por replicación |
| `J50` | Cálculo de carteras replicantes |
| `R50` | las usamos para valorar un activo X cualquiera |
| `K51` | composición |
| `L51` | flujo |
| `M51` | error |
| `N51` | total |
| `B52` | activo X |
| `J52` | lambda1 |
| `Q52` | activo X/N |
| `I53` | nodo a |
| `J53` | lambda2 |
| `J54` | lambda3 |
| `J55` | lambda1 |
| `I56` | nodo b |
| `J56` | lambda2 |
| `J57` | lambda3 |
| `J58` | lambda1 |
| `I59` | nodo c |
| `J59` | lambda2 |
| `J60` | lambda3 |
| `F63` | compos |
| `G63` | flujo |
| `H63` | error |
| `I63` | total |
| `Q63` | activo X |
| `E64` | lambda1 |
| `D65` | nodo inicial |
| `E65` | lambda2 |
| `E66` | lambda3 |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `V6` | 1.0404 | `General` |
| `V7` | 1.0404 | `General` |
| `V8` | 1.0404 | `General` |
| `V9` | 1.0404 | `General` |
| `V10` | 1.0404 | `General` |
| `V11` | 1.0404 | `General` |
| `V12` | 1.0404 | `General` |
| `V13` | 1.0404 | `General` |
| `E16` | 0.02 | `0%` |
| `D23` | 1 | `General` |
| `H29` | 14 | `General` |
| `F30` | 12 | `General` |
| `H30` | 12 | `General` |
| `H31` | 5 | `General` |
| `H32` | 11 | `General` |
| `D33` | 10 | `General` |
| `F33` | 10 | `General` |
| `H33` | 10 | `General` |
| `H34` | 9 | `General` |
| `H35` | 11 | `General` |
| `F36` | 8 | `General` |
| `H36` | 8 | `General` |
| `H37` | 7 | `General` |
| `H39` | 5 | `General` |
| `F40` | 6 | `General` |
| `H40` | 7 | `General` |
| `H41` | 10 | `General` |
| `H42` | 4 | `General` |
| `D43` | 12 | `General` |
| `F43` | 11 | `General` |
| `H43` | 12 | `General` |
| `H44` | 26 | `General` |
| `H45` | 11 | `General` |
| `F46` | 20 | `General` |
| `H46` | 19 | `General` |
| `H47` | 29 | `General` |
| `H52` | 1 | `General` |
| `H53` | 0 | `General` |
| `H54` | 0 | `General` |
| `H55` | 1 | `General` |
| `H56` | 0 | `General` |
| `H57` | 0 | `General` |
| `H58` | 1 | `General` |
| `H59` | 0 | `General` |
| `H60` | 0 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|
| `V5` | `V5` | 1 | `=H19:H27` | 1.0404 |
| `T6` | `T12` | 4 | `=F20` | 1.02 |
| `H19` | `H27` | 9 | `=(1+tipo)^2` | 1.0404 |
| `F20` | `F26` | 3 | `=(1+tipo)` | 1.02 |

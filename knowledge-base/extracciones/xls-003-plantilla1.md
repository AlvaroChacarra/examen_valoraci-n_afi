# XLS-003: Plantilla1.xlsx

Original: [archivo raw](../../raw/fundamentos/ejercicios-valoracion-fundamentos-1/plantilla1.xlsx). SHA-256: `fa60b086524f134c836f1f69c09ad2e03e63856ca1e5fe218f36817290dc07ac`.

Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.

Macros VBA: **False**. Vínculos externos: **0**. Objetos incrustados: **0**.

## Nombres definidos

Un nombre local prevalece sobre el nombre de libro al evaluar fórmulas de su hoja. Se incluyen los parámetros Solver, sin ejecutarlo.

| Nombre | Ámbito | Referencia | Oculto |
|---|---|---|---|
| `matrizS` | `libro` | `Hoja1!$D$8:$G$11` | 0 |
| `preciosHoy` | `libro` | `Hoja1!$B$8:$B$11` | 0 |
| `solver_adj` | `Hoja1` | `Hoja1!$J$18:$M$18` | 1 |
| `solver_cvg` | `Hoja1` | `0.0001` | 1 |
| `solver_drv` | `Hoja1` | `1` | 1 |
| `solver_eng` | `Hoja1` | `1` | 1 |
| `solver_est` | `Hoja1` | `1` | 1 |
| `solver_itr` | `Hoja1` | `100` | 1 |
| `solver_lhs1` | `Hoja1` | `Hoja1!$U$6:$X$6` | 1 |
| `solver_lhs2` | `Hoja1` | `Hoja1!$U$8` | 1 |
| `solver_lhs3` | `Hoja1` | `Hoja1!$F$54` | 1 |
| `solver_lhs4` | `Hoja1` | `Hoja1!$G$54` | 1 |
| `solver_lin` | `Hoja1` | `2` | 1 |
| `solver_mip` | `Hoja1` | `2147483647` | 1 |
| `solver_mni` | `Hoja1` | `30` | 1 |
| `solver_mrt` | `Hoja1` | `0.075` | 1 |
| `solver_msl` | `Hoja1` | `2` | 1 |
| `solver_neg` | `Hoja1` | `2` | 1 |
| `solver_nod` | `Hoja1` | `2147483647` | 1 |
| `solver_num` | `Hoja1` | `0` | 1 |
| `solver_nwt` | `Hoja1` | `1` | 1 |
| `solver_opt` | `Hoja1` | `Hoja1!$V$18` | 1 |
| `solver_pre` | `Hoja1` | `0.000001` | 1 |
| `solver_rbv` | `Hoja1` | `1` | 1 |
| `solver_rel1` | `Hoja1` | `3` | 1 |
| `solver_rel2` | `Hoja1` | `3` | 1 |
| `solver_rel3` | `Hoja1` | `3` | 1 |
| `solver_rel4` | `Hoja1` | `3` | 1 |
| `solver_rhs1` | `Hoja1` | `0` | 1 |
| `solver_rhs2` | `Hoja1` | `1` | 1 |
| `solver_rhs3` | `Hoja1` | `0` | 1 |
| `solver_rhs4` | `Hoja1` | `0` | 1 |
| `solver_rlx` | `Hoja1` | `1` | 1 |
| `solver_rsd` | `Hoja1` | `0` | 1 |
| `solver_scl` | `Hoja1` | `2` | 1 |
| `solver_sho` | `Hoja1` | `2` | 1 |
| `solver_ssz` | `Hoja1` | `100` | 1 |
| `solver_tim` | `Hoja1` | `100` | 1 |
| `solver_tol` | `Hoja1` | `5` | 1 |
| `solver_typ` | `Hoja1` | `3` | 1 |
| `solver_val` | `Hoja1` | `0` | 1 |
| `solver_ver` | `Hoja1` | `3` | 1 |

## Hoja: Hoja1

Estado: `visible`. Rango usado: `B1:XFD79`. Celdas con contenido: 107. Fórmulas: 0. Familias: 0.

### Etiquetas y enunciados completos

| Celda | Texto |
|---|---|
| `P2` | Buscando oportunidades de arbitraje |
| `P4` | composición de la cartera de arbitraje |
| `U4` | flujo de la cartera en cada escenario |
| `B5` | Mercado  |
| `P5` | lambda1 |
| `Q5` | lambda2 |
| `R5` | lambda3 |
| `S5` | lambda4 |
| `U5` | en omega1 |
| `V5` | en omega2 |
| `W5` | en omega3 |
| `X5` | en omega4 |
| `B7` | tiempo 0 |
| `D7` | omega1 |
| `E7` | omega2 |
| `F7` | omega3 |
| `G7` | omega4 |
| `H8` | S1 |
| `P8` | coste cartera |
| `H9` | S2 |
| `H10` | S3 |
| `H11` | S4 |
| `B15` | Cálculo de carteras replicantes |
| `J16` | composición de las carteras replicantes |
| `N16` | flujos |
| `B17` | con solver |
| `I17` | coste |
| `J17` | lambda1 |
| `K17` | lambda2 |
| `L17` | lambda3 |
| `M17` | lambda4 |
| `N17` | en omega1 |
| `O17` | en omega2 |
| `P17` | en omega3 |
| `Q17` | en omega4 |
| `R17` | error Esc1 |
| `S17` | error Esc2 |
| `T17` | error Esc3 |
| `U17` | error Esc4 |
| `V17` | error total |
| `C18` | Activo X |
| `C19` | AD1 |
| `C20` | AD2 |
| `C21` | AD3 |
| `C22` | AD4 |
| `C23` | bono |
| `B25` | con álgebra lineal |
| `I25` | coste |
| `J25` | lambda1 |
| `K25` | lambda2 |
| `L25` | lambda3 |
| `M25` | lambda4 |
| `C26` | Activo X |
| `C27` | AD1 |
| `C28` | AD2 |
| `C29` | AD3 |
| `C30` | AD4 |
| `C31` | bono |
| `B35` | Cálculo de probabilidades de valoración |
| `B37` | numerario N |
| `B38` | tiempo 0 |
| `D38` | tiempo 1 |
| `B42` | Mercado, en términos del numerario |
| `B44` | tiempo 0 |
| `D44` | omega1 |
| `E44` | omega2 |
| `F44` | omega3 |
| `G44` | omega4 |
| `H45` | S1/N |
| `H46` | S2/N |
| `H47` | S3/N |
| `H48` | S4/N |
| `B51` | Probabilidad de valoración |
| `B53` | con solver |
| `D53` | q1 |
| `E53` | q2 |
| `F53` | q3 |
| `G53` | q4 |
| `B62` | con álgebra lineal |
| `D67` | q1 |
| `E67` | q2 |
| `F67` | q3 |
| `G67` | q4 |
| `B71` | Valoración con probabilidades |
| `D73` | activo X |
| `D75` | activo X/N |
| `C78` | valor hoy de X   |

### Constantes e inputs guardados

Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.

| Celda | Valor | Formato |
|---|---|---|
| `B8` | 1.5 | `General` |
| `D8` | 2 | `General` |
| `E8` | 1 | `General` |
| `F8` | 1.5 | `General` |
| `G8` | 2 | `General` |
| `B9` | 0.3 | `General` |
| `D9` | -4 | `General` |
| `E9` | 2 | `General` |
| `F9` | -1 | `General` |
| `G9` | 1 | `General` |
| `B10` | 2.5 | `General` |
| `D10` | 5 | `General` |
| `E10` | 1 | `General` |
| `F10` | 1.5 | `General` |
| `G10` | 4 | `General` |
| `B11` | 1.3 | `General` |
| `D11` | 3.5 | `General` |
| `E11` | 0 | `General` |
| `F11` | 2 | `General` |
| `G11` | 1.5 | `General` |

### Familias de fórmulas

Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.

| Primera | Última | N | Fórmula literal de la primera | Valor guardado |
|---|---|---:|---|---|

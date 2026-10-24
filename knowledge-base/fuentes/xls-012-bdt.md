# XLS-012: Calibración Black–Derman–Toy y derivados de tipos

Archivo: **BDT.xlsx**. Papel: **ejemplo con hojas de distinto grado de desarrollo**.

[Original](../../raw/fundamentos/sesioniii/bdt.xlsx) · [Extracción detallada](../extracciones/xls-012-bdt.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Calibrar un árbol de tipos a la curva cupón cero y usarlo para comparar flujos usuales e in arrears.

Errores de calibración, curva implícita, valores de FRA/caplet usuales e in arrears y réplica local.

## Método observado

Construir ruido lognormal y la función U por nivel; producir tipos cortos; valorar bonos por backward induction con descuento local; ajustar U a los descuentos de mercado mediante Solver; construir flujos de FRA y caplet; comparar fechas de pago y carteras replicantes.

## Teoría relacionada

PDF-003 pp. 84–101; PDF-006 pp. 59–72. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

El descuento depende del nodo y de la trayectoria. Sheet1 es parcial; Sheet2 desarrolla más cálculos. Hay un error guardado en la fuente.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Sheet1 | visible | `A1:XFD88` | 67 | 20 | 1 |
| Sheet2 | hidden | `A1:AK88` | 183 | 42 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Sheet1!$B$7` |
| `Nom` | `Sheet1!$AA$27` |
| `strike` | `Sheet1!$Y$27` |
| `vola` | `Sheet1!$C$7` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Sheet1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `B7` | `=1/4` | 0.25 |
| `M10` | `=L10*deltat` | 0 |
| `X41` | `=AVERAGE(Y41:Y42)*EXP(-C26*deltat)` | 0 |
| `AB41` | `=Y33:Y37` | 0 |
| `X49` | `=AVERAGE(Y49:Y50)*EXP(-C26*deltat)` | 0 |
| `AB49` | `=Z33:Z37` | 0 |
| `AD49` | `=X49*100000000000` | 0 |
| `AD51` | `=(Q14/Q15-1)/deltat` | #DIV/0! |
| `X57` | `=AVERAGE(Y57:Y58)*EXP(-C26*deltat)` | 0 |
| `AB57` | `=AA33:AA37` | 0 |
| `AE61` | `=AB49` | 0 |
| `AG61` | `=O36` | 0 |
| `X65` | `=AVERAGE(Y65:Y66)*EXP(-C26*deltat)` | 0 |
### Sheet2

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `B7` | `=1/4` | 0.25 |
| `M10` | `=L10*deltat` | 0 |
| `Q11` | `=L61` | 0.9950001142312155 |
| `R11` | `=(1/(P11*deltat))*LN(1/Q11)` | 0.02004970807323649 |
| `T11` | `=(N11-Q11)^2` | 1.3048770591569856e-14 |
| `Q12` | `=L53` | 0.9910001275695014 |
| `D13` | `=C13+vola*SQRT(deltat)` | 0.225 |
| `Q13` | `=L45` | 0.9890001612361484 |
| `D14` | `=C13-vola*SQRT(deltat)` | -0.225 |
| `Q14` | `=L36` | 0.9800000660788983 |
| `Q15` | `=L26` | 0.9745000257112376 |
| `T16` | `=SUM(T11:T15)*10000000` | 6.034733238780664e-07 |
| `L26` | `=AVERAGE(M26:M27)*EXP(-C26*deltat)` | 0.9745000257112376 |
| `AA33` | `=MAX(X33-strike,0)*deltat*Nom` | 69.85708252023377 |
| `L36` | `=AVERAGE(M36:M37)*EXP(-C26*deltat)` | 0.9800000660788983 |
| `X41` | `=AVERAGE(Y41:Y42)*EXP(-C26*deltat)` | 0.0658732940049933 |
| `L45` | `=AVERAGE(M45:M46)*EXP(-C26*deltat)` | 0.9890001612361484 |
| `X49` | `=AVERAGE(Y49:Y50)*EXP(-C26*deltat)` | 0 |
| `L53` | `=AVERAGE(M53:M54)*EXP(-C26*deltat)` | 0.9910001275695014 |
| `X57` | `=AVERAGE(Y57:Y58)*EXP(-C26*deltat)` | 10.07326655416573 |

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.


## Ámbito de nombres verificado en segunda revisión

El cuadro anterior recoge referencias de libro. La extracción incluye además los nombres locales de cada hoja. En una hoja oculta, el nombre local prevalece sobre el global: no sustituirlo por una referencia a la hoja visible. Las diferencias de alcance se comprobaron directamente en `xl/workbook.xml`.

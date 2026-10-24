# XLS-017: Opciones sobre el máximo de dos activos

Archivo: **pag 1.39 opcion sobre dos activos.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-39-opcion-sobre-dos-activos.xlsx) · [Extracción detallada](../extracciones/xls-017-pag-1-39-opcion-sobre-dos-activos.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar max(X_T,Y_T) y max(max(X_T,Y_T)-K,0), y estudiar la influencia de la correlación.

Primas por distintos métodos y tabla de sensibilidad a correlación. La fórmula I48 de la solución corresponde al máximo sin strike, no a la segunda variante.

## Método observado

Generar normales independientes; correlacionarlas con Z2=rho Z1+sqrt(1-rho²) epsilon; transformar en dos spots lognormales; calcular el payoff; comparar Monte Carlo con integral doble; usar cambio de numerario/Margrabe cuando corresponda; variar rho.

## Teoría relacionada

PDF-007 pp. 34–35 y 40–45. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

No transferir automáticamente el efecto de correlación de un máximo a una cesta promedio. El signo depende del payoff.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `B1:BN2056` | 19414 | 16 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `correla` | `Hoja1!$D$27` |
| `K` | `Hoja1!$H$34` |
| `paso` | `Hoja1!$P$41` |
| `T` | `Hoja1!$F$32` |
| `tipo` | `Hoja1!$D$21` |
| `volagorro` | `Hoja1!$AJ$22` |
| `volaX` | `Hoja1!$D$24` |
| `volaY` | `Hoja1!$F$24` |
| `X0` | `Hoja1!$D$23` |
| `Y0` | `Hoja1!$F$23` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `AC15` | `=Y40` | 26.312718486029077 |
| `AC16` | `<DataTableFormula: {'ref': 'AC16:AC35', 'ca': '1', 'dt2D': '0', 'dtr': '0', 'r1': 'D27', 'r2': None, 'del1': False, 'del2': False}>` | 26.900513268556182 |
| `Y40` | `=SUMPRODUCT(P44:BN94,P107:BN157)*EXP(-tipo*T)` | 26.312718486029077 |
| `I42` | `=EXP(-tipo*T)*AVERAGE(I48:I2047)` | 26.46066805884229 |
| `C43` | `=AVERAGE(C48:C2047)` | 0.01960984726849898 |
| `Q43` | `=P43+paso` | -4.8 |
| `C44` | `=STDEV(C48:C2047)` | 1.015640158203008 |
| `P44` | `=1/(2*PI()*SQRT(1-correla^2))*EXP(-1/(2*(1-correla^2))*(P$43^2+$O44^2-2*correla*P$43*$O44))*paso^2` | 1.7419751165038155e-16 |
| `O45` | `=O44+paso` | -4.8 |
| `C48` | `=NORMSINV(RAND())` | -0.6674251258922519 |
| `E48` | `=C48` | -0.6674251258922519 |
| `F48` | `=correla*C48+SQRT(1-correla^2)*D48` | -1.1356472088594518 |
| `I48` | `=(MAX(G48,H48))` | 22.59010674939777 |
| `P107` | `=MAX(X0*EXP(volaX*SQRT(T)*P$106+(tipo-0.5*volaX^2)*T),Y0*EXP(volaY*SQRT(T)*$O107+(tipo-0.5*volaY^2)*T))` | 11.794411585818516 |

## Plantilla / solución relacionada

- [XLS-022: 1.5.opcion sobre dos activos_Plantilla.xlsx](../fuentes/xls-022-1-5-opcion-sobre-dos-activos-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

# XLS-016: Call con dividendo discreto por condicionamiento

Archivo: **pag 1.36 dividendo discreto.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity-soluciones/pag-1-36-dividendo-discreto.xlsx) · [Extracción detallada](../extracciones/xls-016-pag-1-36-dividendo-discreto.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar una call cuyo dividendo se paga antes del vencimiento, comparando condicionamiento e integración doble.

Precio con dividendo y comparación de procedimientos. La solución añade la hoja integral doble que no está en la plantilla.

## Método observado

Generar escenarios del spot en la fecha del dividendo; aplicar la regla ex-dividendo del archivo; valorar condicionalmente la call durante el periodo restante; integrar y descontar; contrastar con la cuadratura bivariante y con la call sin dividendos.

## Teoría relacionada

PDF-007 pp. 31–33. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La regla de dividendo cuando S es menor que D tiene ramas particulares en la fuente; no sustituirlas silenciosamente por un dividendo garantizado.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| condicionando | visible | `C2:T267` | 718 | 18 | 0 |
| integral doble | visible | `C3:BB118` | 5407 | 10 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `divid` | `condicionando!$G$12` |
| `flujos` | `'integral doble'!$D$68:$BB$118` |
| `K` | `condicionando!$G$11` |
| `paso` | `'integral doble'!$D$10` |
| `plazo1` | `condicionando!$E$7` |
| `plazo2` | `condicionando!$F$7` |
| `probs` | `'integral doble'!$D$14:$BB$64` |
| `q` | `condicionando!$J$6` |
| `sigma` | `condicionando!$G$14` |
| `spot` | `condicionando!$G$13` |
| `tipo` | `condicionando!$D$3` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### condicionando

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `E8` | `=EXP(-plazo1*tipo)` | 0.9900498337491681 |
| `F8` | `=EXP(-plazo2*tipo)` | 0.9801986733067553 |
| `F9` | `=F8/E8` | 0.990049833749168 |
| `C24` | `=0.1` | 0.1 |
| `O24` | `=SUMPRODUCT(F26:F126,M26:M126)*$E$8` | 9.132827318334984 |
| `T25` | `=LN(spot/(EXP(-tipo*plazo2)*K))` | -0.16232155679395452 |
| `F26` | `=NORMDIST(E26,0,1,FALSE)*0.1` | 1.4867195147342977e-07 |
| `G26` | `=spot*EXP(sigma*SQRT(plazo1)*E26)*EXP(tipo*plazo1-(sigma^2/2)*plazo1)` | 432.7543240300773 |
| `I26` | `=IF(G26>divid,G26-divid,G26)` | 427.7543240300773 |
| `K26` | `=LN(I26/(K*$F$9))` | 1.2810572787178365 |
| `L26` | `=sigma*SQRT(plazo2-plazo1)` | 0.3 |
| `M26` | `=(NORMSDIST(K26/L26+L26/2)-EXP(-K26)*NORMSDIST(K26/L26-L26/2))*I26` | 308.94848360869975 |
### integral doble

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `E3` | `=SUMPRODUCT(probs,flujos)` | 9.307376473621225 |
| `E4` | `=E3*condicionando!F8` | 9.123078071410031 |
| `E13` | `=D13+paso` | -4.8 |
| `C14` | `=-5` | -5 |
| `D14` | `=EXP(-0.5*(D$13^2+$C14^2))/(2*PI())*paso^2` | 8.841339661967145e-14 |
| `C15` | `=C14+paso` | -4.8 |
| `C66` | `=MAX((spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)-IF(spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)>=divid,divid,spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)))*EXP(sigma*SQRT(plazo2-plazo1)*D$67+(tipo-0.5*sigma^2)*(plazo2-plazo1))-K,0)` | 0 |
| `E67` | `=D67+0.2` | -4.8 |
| `D68` | `=MAX((spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)-IF(spot*EXP(sigma*SQRT(plazo1)*$C68+(tipo-0.5*sigma^2)*plazo1)>=divid,divid,0.000001))*EXP(sigma*SQRT(plazo2-plazo1)*D$67+(tipo-0.5*sigma^2)*(plazo2-plazo1))-K,0)` | 0 |
| `C69` | `=C68+0.2` | -4.8 |

## Plantilla / solución relacionada

- [XLS-021: 1.4.dividendo discreto_Plantilla.xlsx](../fuentes/xls-021-1-4-dividendo-discreto-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

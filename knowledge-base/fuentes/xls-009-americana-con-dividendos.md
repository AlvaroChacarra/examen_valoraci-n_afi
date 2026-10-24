# XLS-009: Dividendos discretos y ejercicio americano

Archivo: **Americana con dividendos.xlsx**. Papel: **ejemplo con hojas de distinto grado de desarrollo**.

[Original](../../raw/fundamentos/sesioniii/americana-con-dividendos.xlsx) · [Extracción detallada](../extracciones/xls-009-americana-con-dividendos.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Separar cotización ex-dividendo, valor de dividendos y ganancia total para valorar y cubrir una opción americana.

Árboles de subyacente, dividendos, valor de inversión, opción y cartera. Hoja1 y Hoja2 tienen distinto grado de desarrollo.

## Método observado

Descontar los dividendos futuros y definir S*; construir su árbol; recomponer la cotización S y la inversión total incluyendo dividendos; simular las tres series; comparar continuación y ejercicio; formar la cartera de cobertura.

## Teoría relacionada

PDF-003 pp. 49–71; PDF-006 pp. 40–50. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Hay errores guardados en la fuente. No interpretarlos como resultados válidos. No usar la cotización ex-dividendo como si fuera el proceso de ganancia.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `A1:XFD150` | 463 | 29 | 28 |
| Hoja2 | hidden | `A3:S150` | 749 | 35 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `d` | `Hoja1!$C$15` |
| `Deltat` | `Hoja1!$C$9` |
| `Descuento` | `Hoja1!$C$10` |
| `dividendo1` | `Hoja1!$F$6` |
| `dividendo2` | `Hoja1!$H$6` |
| `p` | `Hoja1!$C$13` |
| `probs` | `Hoja1!$P$20:$P$32` |
| `S0` | `Hoja1!$C$6` |
| `strike` | `Hoja1!$C$93` |
| `Tiempo1` | `Hoja1!$F$5` |
| `Tiempo2` | `Hoja1!$H$5` |
| `tipo` | `Hoja1!$C$4` |
| `u` | `Hoja1!$C$14` |
| `vola` | `Hoja1!$C$5` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `C9` | `=1/12` | 0.08333333333333333 |
| `C10` | `=+EXP(-tipo*Deltat)` | 0.9995001249791693 |
| `C14` | `=EXP(tipo*Deltat)*EXP(vola*SQRT(Deltat))*2/(EXP(vola*SQRT(Deltat))+EXP(-vola*SQRT(Deltat)))` | 1.115517195155658 |
| `C15` | `=EXP(tipo*Deltat)*EXP(-vola*SQRT(Deltat))*2/(EXP(vola*SQRT(Deltat))+EXP(-vola*SQRT(Deltat)))` | 0.8854830548860136 |
| `J15` | `=SUMPRODUCT(N20:N32,probs)*Descuento^12` | 0 |
| `L15` | `=SQRT(SUMPRODUCT(S20:S32^2,probs)-SUMPRODUCT(S20:S32,probs)^2)` | #NUM! |
| `B19` | `=B18*Deltat` | 0 |
| `P20` | `=BINOMDIST(Q20,12,p,FALSE)` | 0.00024414062500000016 |
| `S20` | `=LN(N20/S0)` | #NUM! |
| `B55` | `=SUMPRODUCT(N47:N59,P20:P32)*Descuento^12` | 0 |
| `D55` | `=SQRT(SUMPRODUCT(S47:S59^2,probs)-SUMPRODUCT(S47:S59,probs)^2)` | #NUM! |
| `B71` | `=SUMPRODUCT(N65:N77,P20:P32)*Descuento^12` | 0 |
| `B97` | `=MAX(MAX(strike-B47,0),Descuento*(p*C97+(1-p)*C98))` | 84 |
| `N97` | `=MAX(strike-N47,0)` | 84 |
| `N117` | `=MAX(N47-strike,0)` | 0 |
| `B138` | `=MAX(Descuento*(p*C138+(1-p)*C139),MAX(B47-strike,0))` | 0 |
| `N138` | `=MAX(N47-strike,0)` | 0 |
### Hoja2

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `C9` | `=1/12` | 0.08333333333333333 |
| `C10` | `=+EXP(-tipo*Deltat)` | 0.9995001249791693 |
| `C14` | `=EXP(tipo*Deltat)*EXP(vola*SQRT(Deltat))*2/(EXP(vola*SQRT(Deltat))+EXP(-vola*SQRT(Deltat)))` | 1.115517195155658 |
| `C15` | `=EXP(tipo*Deltat)*EXP(-vola*SQRT(Deltat))*2/(EXP(vola*SQRT(Deltat))+EXP(-vola*SQRT(Deltat)))` | 0.8854830548860136 |
| `J15` | `=SUMPRODUCT(N20:N32,probs)*Descuento^12` | 76.51135130179459 |
| `L15` | `=SQRT(SUMPRODUCT(S20:S32^2,probs)-SUMPRODUCT(S20:S32,probs)^2)` | 0.40000000000000013 |
| `B19` | `=B18*Deltat` | 0 |
| `B20` | `=S0-B40` | 76.5113513017947 |
| `C20` | `=B20*u` | 85.34972800174722 |
| `P20` | `=BINOMDIST(Q20,12,p,FALSE)` | 0.00024414062500000016 |
| `S20` | `=LN(N20/S0)` | 1.2672302724625304 |
| `C21` | `=B20*d` | 67.74950508417015 |
| `B55` | `=SUMPRODUCT(N47:N59,P20:P32)*Descuento^12` | 76.51135130179459 |
| `D55` | `=SQRT(SUMPRODUCT(S47:S59^2,probs)-SUMPRODUCT(S47:S59,probs)^2)` | 0.40000000000000013 |
| `B71` | `=SUMPRODUCT(N65:N77,P20:P32)*Descuento^12` | 79.99999999999989 |
| `B97` | `=MAX(MAX(strike-B47,0),Descuento*(p*C97+(1-p)*C98))` | 16.62681644800156 |
| `N97` | `=MAX(strike-N47,0)` | 0 |
| `N117` | `=MAX(N47-strike,0)` | 200.08028933607602 |
| `B138` | `=MAX(Descuento*(p*C138+(1-p)*C139),MAX(B47-strike,0))` | 9.813960642866608 |
| `N138` | `=MAX(N47-strike,0)` | 200.08028933607602 |

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

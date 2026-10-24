# XLS-011: Árbol recombinante con curva de volatilidad

Archivo: **Arbol volas no ctes.xlsm**. Papel: **ejemplo con hojas de distinto grado de desarrollo**.

[Original](../../raw/fundamentos/sesioniii/arbol-volas-no-ctes.xlsm) · [Extracción detallada](../extracciones/xls-011-arbol-volas-no-ctes.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Ajustar el árbol a una estructura temporal de tipos y volatilidades manteniendo un tamaño recombinante.

Nueva malla temporal, árbol ajustado, comprobación de volatilidad y valoración. La VBA InterPola distingue interpolación lineal y logarítmica.

## Método observado

Transformar volatilidad spot en varianza acumulada t sigma(t)^2; fijar un paso uniforme de varianza; invertir por interpolación la relación tiempo-varianza; interpolar los tipos en los nuevos plazos; combinar ruido, deriva de tipos y corrección cosh; valorar y cubrir.

## Teoría relacionada

PDF-003 pp. 74–83; PDF-006 pp. 54–58. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Este método cambia la malla de tiempo. El encargo pide paso mensual y volatilidades de cada año: no son automáticamente los mismos inputs ni las mismas fechas de ejercicio.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `B1:XFD99` | 128 | 28 | 51 |
| Hoja2 | hidden | `B2:S99` | 266 | 53 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `callput` | `Hoja1!$H$63` |
| `deltat` | `Hoja1!$E$4` |
| `factorVola` | `Hoja1!$H$19` |
| `nuevostiempos` | `Hoja1!$E$22:$K$22` |
| `pasovola` | `Hoja1!$E$19` |
| `S0` | `Hoja1!$E$13` |
| `strike` | `Hoja1!$F$63` |
| `T` | `Hoja1!$E$3` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `E4` | `=1/12` | 0.08333333333333333 |
| `E10` | `=E9*deltat` | 0 |
| `R47` | `=K12*SQRT(T)` | 0.25809397513308985 |
| `N48` | `=SUMPRODUCT(K50:K56,M50:M56)*K24` | 0 |
| `E49` | `=nuevostiempos` | 0 |
| `M50` | `=BINOMDIST(L50,6,50%,FALSE)` | 0.015625000000000007 |
| `P50` | `=LN(K50/S0)` | #NUM! |
| `R50` | `=SUMPRODUCT(P50:P56,M50:M56)` | #NUM! |
| `R51` | `=SUMPRODUCT(P50:P56^2,M50:M56)` | #NUM! |
| `R52` | `=R51-R50^2` | #NUM! |
| `R53` | `=SQRT(R52)` | #NUM! |
| `G63` | `=T` | 0.5 |
| `E68` | `=AVERAGE(F68:F69)*E$25` | 0 |
| `K68` | `=MAX(callput*(K50-strike),0)` | 0 |
| `M93` | `=MAX(callput*(K92-strike),0)` | 0 |
### Hoja2

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `E4` | `=1/12` | 0.08333333333333333 |
| `P8` | `=TRANSPOSE(E16:K16)` | 0 |
| `Q8` | `=TRANSPOSE(E10:K10)` | 0 |
| `R8` | `=O8*pasovola^2` | 0 |
| `S9` | `=InterPola(R9,$P$8:$Q$14,1)` | 0.13608342077649527 |
| `E10` | `=E9*deltat` | 0 |
| `F16` | `=F10*F12^2` | 0.0060750000000000005 |
| `E17` | `=K16` | 0.06661249999999999 |
| `E18` | `=E17/E2` | 0.011102083333333332 |
| `P18` | `=TRANSPOSE(E10:K10)` | 0 |
| `R18` | `=S8:S14` | 0 |
| `E19` | `=SQRT(E18)` | 0.1053664241271067 |
| `S19` | `=InterPola(R19,$P$18:$Q$24,1)` | 0.008172402938090241 |
| `N48` | `=SUMPRODUCT(K50:K56,M50:M56)*K24` | 79.99999999999996 |
| `R50` | `=SUMPRODUCT(P50:P56,M50:M56)` | -0.02434480371361106 |
| `R51` | `=SUMPRODUCT(P50:P56^2,M50:M56)` | 0.06720516946785428 |
| `E68` | `=AVERAGE(F68:F69)*E$25` | 7.10528808168346 |
| `K68` | `=MAX(callput*(K50-strike),0)` | 62.91884738354187 |
| `M93` | `=MAX(callput*(K92-strike),0)` | 35.00286012287346 |

## Macros, imágenes y dependencias

Proyecto VBA presente: **True**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Procedimientos recuperados: `InterPola`.
La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.

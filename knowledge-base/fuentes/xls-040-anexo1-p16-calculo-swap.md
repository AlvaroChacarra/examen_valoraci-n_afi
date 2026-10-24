# XLS-040: Valoración de swap con curvas distintas

Archivo: **Anexo1.p16-cálculo-swap.xlsm**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/anexos-valoracion-marco-black-soluciones/anexo1-p16-calculo-swap.xlsm) · [Extracción detallada](../extracciones/xls-040-anexo1-p16-calculo-swap.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Separar curva de proyección del Euribor y curva de descuento al valorar un swap.

Valor de rama variable, fija, neto y cupón de equilibrio en Valoracion!H2:H6 en la solución.

## Método observado

Leer las dos curvas de Inputs; generar calendarios de fixing, inicio y fin; ajustar fechas y devengos; interpolar descuentos de proyección para calcular forwards; descontar los flujos con Eonia; sumar ambas ramas y obtener el cupón par.

## Teoría relacionada

PDF-009 pp. 7–16. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Existen llamadas externas [1]!interpol y una etiqueta EUR006M junto a una curva EUR3M. La disponibilidad de una función VBA de nombre parecido no resuelve automáticamente el vínculo externo.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Inputs | visible | `B2:F42` | 0 | 0 | 0 |
| Valoracion | visible | `B2:T72` | 215 | 16 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `CCC_Eonia` | `Inputs!$B$7:$C$42` |
| `CCC_EUR3M` | `Inputs!$E$7:$F$33` |
| `FV` | `Inputs!$C$2` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Inputs

| Celda | Fórmula | Valor guardado |
|---|---|---|
| — | No hay fórmulas de celda en esta hoja | — |
### Valoracion

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `H2` | `=+SUMPRODUCT(H12:H31,K12:K31,L12:L31)*C6` | 230731.85156188614 |
| `H3` | `=+SUMPRODUCT(S12:S16,T12:T16)*C7*C6` | 299061.5228923861 |
| `H4` | `=H2-H3` | -68329.67133049999 |
| `H6` | `=H2/SUMPRODUCT(S12:S16,T12:T16)/C6` | 0.004629118102463064 |
| `B12` | `=+WORKDAY(D12,-2)` | 2018-04-12T00:00:00 |
| `D12` | `=+$C$2` | 2018-04-15T00:00:00 |
| `E12` | `=+EDATE(D12,3)` | 2018-07-15T00:00:00 |
| `F12` | `=IF(WEEKDAY(D12)=7,D12+2,IF(WEEKDAY(D12)=1,D12+1,D12))` | 2018-04-16T00:00:00 |
| `H12` | `=+YEARFRAC(F12,G12,$D$4)` | 0.25277777777777777 |
| `I12` | `=[1]!interpol(F12,CCC_EUR3M)` | 1.0006779237374164 |
| `K12` | `=+(I12/J12-1)/H12` | -0.002439592925494114 |
| `L12` | `=[1]!interpol(G12,CCC_Eonia)` | 1.0015513119666861 |
| `T12` | `=[1]!interpol(R12,CCC_Eonia)` | 1.003846275303818 |

## Plantilla / solución relacionada

- [XLS-043: Anexo1.-cálculo-swap.xlsm](../fuentes/xls-043-anexo1-calculo-swap.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **True**. Vínculos externos declarados: **1**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

Procedimientos recuperados: `InterPol`, `Interpol2`, `Interpol3`, `InterPol_filas`.
La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.

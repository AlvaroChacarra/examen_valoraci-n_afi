# XLS-001: Ley de los grandes números con pagos independientes

Archivo: **Grandes números-1-iid.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/fundamentos/ejercicios-valoracion-fundamentos-1/grandes-numeros-1-iid.xlsx) · [Extracción detallada](../extracciones/xls-001-grandes-numeros-1-iid.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Simular sumas de pagos iid y estimar la proporción que queda dentro de una tolerancia relativa respecto a su esperanza.

Proporción dentro del margen y distribución de pagos agregados. Se busca entender cuándo la diversificación justifica un promedio actuarial, antes de introducir valoración por réplica.

## Método observado

Definir valores y probabilidades de X; calcular E(X) y su desviación; generar X mediante una uniforme y la tabla acumulada; sumar N pagos; repetir y comparar la desviación relativa con la tolerancia.

## Teoría relacionada

PDF-004 pp. 16–21; PDF-005 pp. 30–39. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

N y tolerancia son controles. Las tablas What-If y RAND guardan realizaciones, no una muestra nueva verificada.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `B5:X2042` | 4946 | 28 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `N` | `Hoja1!$E$16` |
| `numsims` | `Hoja1!$S$19` |
| `sims` | `Hoja1!$I$19:$I$585` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `E7` | `=B8` | 0 |
| `D8` | `=C8+D7` | 0.53 |
| `H8` | `=SUMPRODUCT(B8:B11,C8:C11)` | 0.56 |
| `H9` | `=SQRT(SUMPRODUCT(B8:B11^2,C8:C11)-H8^2)` | 0.7391887445030533 |
| `C11` | `=1-SUM(C8:C10)` | 0.010000000000000009 |
| `G12` | `=H8*E16` | 0.56 |
| `R16` | `=MIN(I19:I585)` | 0 |
| `S16` | `=MAX(I19:I585)` | 5 |
| `C17` | `=VLOOKUP(RAND(),$D$7:$E$10,2,TRUE)` | 1 |
| `E18` | `=SUM(OFFSET(C17,0,0,E16,1))` | 1 |
| `I18` | `=E18` | 1 |
| `R18` | `=(S16-R16)/S17` | 0.25 |
| `M19` | `=AVERAGE(K19:K585)` | 0 |

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

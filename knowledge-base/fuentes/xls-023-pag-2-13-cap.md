# XLS-023: Cap como cartera de caplets

Archivo: **pag 2.13 cap.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos-soluciones/pag-2-13-cap.xlsx) · [Extracción detallada](../extracciones/xls-023-pag-2-13-cap.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar un cap semestral a cinco años y analizar su sensibilidad a strike y volatilidad.

Prima total Q20 en la solución, primas parciales y sensibilidades.

## Método observado

Derivar forwards de la curva de descuentos; distinguir el primer flujo ya fijado; calcular Black por caplet usando tiempo de fixing y descuento de pago; sumar; variar strike y volatilidad con tablas de datos.

## Teoría relacionada

PDF-008 pp. 5–13. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

No confundir fixing con pago ni volatilidad de un cap con una estructura de volatilidades caplet calibrada.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `D3:Q96` | 106 | 15 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Hoja1!$E$3` |
| `K` | `Hoja1!$M$4` |
| `nom` | `Hoja1!$M$3` |
| `vola` | `Hoja1!$E$23` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `D8` | `=D7+deltat` | 0.5 |
| `G8` | `=(E7/E8-1)/deltat` | 0.008838891120932058 |
| `Q8` | `=E8*deltat*MAX(G8-K,0)*nom` | 0.41759999999997816 |
| `J9` | `=D9` | 1 |
| `K9` | `=LN(G9/K)` | -0.3602512129387861 |
| `L9` | `=vola*SQRT(D8)` | 0.24748737341529164 |
| `M9` | `=K9/L9+0.5*L9` | -1.3318910310048944 |
| `N9` | `=K9/L9-0.5*L9` | -1.579378404420186 |
| `O9` | `=NORMSDIST(M9)` | 0.09144799935530948 |
| `Q9` | `=deltat*E9*(G9*O9-K*P9)*nom` | 0.026450717504982207 |
| `Q20` | `=SUM(Q8:Q17)` | 28.790124285402747 |
| `H26` | `=Q20` | 28.790124285402747 |

## Plantilla / solución relacionada

- [XLS-030: cap_Plantilla.xlsx](../fuentes/xls-030-cap-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

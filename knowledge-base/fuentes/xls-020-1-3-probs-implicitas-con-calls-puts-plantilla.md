# XLS-020: Distribución implícita en calls y puts

Archivo: **1.3.probs implicitas con calls-puts_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/1-valoracion-marco-black-equity/1-3-probs-implicitas-con-calls-puts-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-020-1-3-probs-implicitas-con-calls-puts-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Extraer una aproximación a probabilidades riesgo-neutras desde precios o volatilidades por strike y compararla con volatilidad ATM constante.

Probabilidades aproximadas por nivel, suma de masas representadas y comparación gráfica.

## Método observado

Calcular precios de calls y puts para la parrilla de strikes; formar spreads de primas entre strikes vecinos; dividir por el paso para aproximar digitales; deshacer el descuento; comparar probabilidades obtenidas con smile y con vola plana.

## Teoría relacionada

PDF-007 pp. 29–30; PDF-004 pp. 125–130. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Son probabilidades de valoración, no frecuencias históricas. La parrilla finita y la convención del spread afectan la aproximación y las colas.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `A10:U122` | 143 | 7 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `spot` | `Hoja1!$C$13` |
| `T` | `Hoja1!$C$12` |
| `tipo` | `Hoja1!$C$11` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `C12` | `=(C15-C14)/365` | 0.06027397260273973 |
| `C17` | `=spot*EXP(tipo*T)` | 10502.025400799497 |
| `Q23` | `=SUM(Q24:Q70)` | 0 |
| `C25` | `=C26-100` | 8300 |
| `C48` | `=C47+100` | 10600 |
| `C76` | `=C24` | 8200 |
| `D76` | `=$D$47` | 0.3818 |

## Plantilla / solución relacionada

- [XLS-015: pag 1.33 probs implicitas con calls-puts.xlsx](../fuentes/xls-015-pag-1-33-probs-implicitas-con-calls-puts.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

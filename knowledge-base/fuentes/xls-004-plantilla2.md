# XLS-004: Réplica dinámica y cambio de numerario

Archivo: **plantilla2.xlsx**. Papel: **plantilla**.

[Original](../../raw/fundamentos/ejercicios-valoracion-fundamentos-1/plantilla2.xlsx) · [Extracción detallada](../extracciones/xls-004-plantilla2.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar un flujo terminal en un árbol de varios periodos y demostrar que el precio coincide usando distintos numerarios.

Carteras locales, probabilidades por nodo, precio inicial y errores de réplica. La solución explicita cuatro tareas en J10:J13.

## Método observado

Leer los activos en cada nodo; construir carteras replicantes desde los nodos finales; calcular probabilidades condicionadas bajo S1; repetir usando S2; aplicar el cambio de numerario y comparar los precios.

## Teoría relacionada

PDF-004 pp. 77–101; PDF-005 pp. 93–118. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Distinguir probabilidades condicionadas por nodo de probabilidades de trayectorias. Una estrategia debe ser adaptada y autofinanciada.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `B3:AA71` | 17 | 4 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `Num0` | `Hoja1!$R$9` |
| `tipo` | `Hoja1!$E$16` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `V5` | `=H19:H27` | 1.0404 |
| `T6` | `=F20` | 1.02 |
| `H19` | `=(1+tipo)^2` | 1.0404 |
| `F20` | `=(1+tipo)` | 1.02 |

## Plantilla / solución relacionada

- [XLS-008: Plantilla2_Solucion.xlsx](../fuentes/xls-008-plantilla2-solucion.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

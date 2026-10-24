# XLS-008: Réplica dinámica y cambio de numerario

Archivo: **Plantilla2_Solucion.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/fundamentos/sesion-ii/plantilla2-solucion.xlsx) · [Extracción detallada](../extracciones/xls-008-plantilla2-solucion.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Hoja1 | visible | `B3:BC76` | 217 | 69 | 0 |

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
| `AI5` | `=H29` | 14 |
| `AV5` | `=V5:V13` | 1.0404 |
| `BC5` | `=AI5:AI13` | 14 |
| `T6` | `=F20` | 1.02 |
| `AT6` | `=T6` | 1.02 |
| `BA6` | `=AG6` | 12 |
| `AR9` | `=Num0` | 1 |
| `H19` | `=(1+tipo)^2` | 1.0404 |
| `V19` | `=H19:H27/$V$5:$V$13` | 1 |
| `AI19` | `=H19:H27/AI5:AI13` | 0.07431428571428571 |
| `F20` | `=(1+tipo)` | 1.02 |
| `X20` | `=(SUMPRODUCT(V19:V21,U19:U21)-T20)^2*10000` | 6.21120915620123e-14 |
| `AK20` | `=(SUMPRODUCT(AI19:AI21,AH19:AH21)-AG20)^2` | 7.89237870235567e-16 |
| `Z23` | `=(SUMPRODUCT(T20:T26,S20:S26)-R23)^2` | 5.067083709738656e-16 |
| `X39` | `=(SUMPRODUCT(V39:V41,U39:U41)-T40)^2*10000` | 5.6055968274169296e-11 |
| `Z42` | `=(SUMPRODUCT(T40:T46,S40:S46)-R43)^2` | 6.493671873882093e-12 |
| `T53` | `=SUMPRODUCT(V52:V54,U52:U54)` | 0.6535947657305851 |
| `R56` | `=SUMPRODUCT(T53:T59,S53:S59)` | 0.4163957554555653 |
| `AE56` | `=SUMPRODUCT(AG53:AG59,AF20:AF26)` | 0.04163938066150331 |

## Plantilla / solución relacionada

- [XLS-004: plantilla2.xlsx](../fuentes/xls-004-plantilla2.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

# XLS-047: Escenarios shifted lognormal y valoración de caplet

Archivo: **Anexo1.-escenarios-shifted_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/anexos-valoracion/anexo1-escenarios-shifted-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-047-anexo1-escenarios-shifted-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Visualizar tipos negativos permitidos por un desplazamiento y contrastar precio analítico con cuadratura.

Distribución de forward, payoff y prima por fórmula frente a cuadratura.

## Método observado

Construir una rejilla normal y sus pesos; transformar F_T=(F0+shift)exp(-sigma² T/2+sigma sqrt(T) Z)-shift; aplicar el payoff de caplet; integrar y descontar; comparar con shifted Black.

## Teoría relacionada

PDF-009 pp. 30–34. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La fórmula guardada K31 usa volash*T donde la volatilidad acumulada general exige volash*sqrt(T). Como T=1, el caso guardado puede ocultar la diferencia. No se ha corregido el original.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `C6:P98` | 166 | 3 | 0 |
| Hoja2 | visible | `A1:A1` | 0 | 0 | 0 |
| Hoja3 | visible | `A1:A1` | 0 | 0 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `DT` | `Hoja1!$D$7` |
| `F0` | `Hoja1!$D$6` |
| `shift` | `Hoja1!$D$11` |
| `strike` | `Hoja1!$M$26` |
| `T` | `Hoja1!$D$8` |
| `volash` | `Hoja1!$D$9` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `D7` | `=1/4` | 0.25 |
| `E16` | `=NORMDIST(D16,0,1,FALSE)*0.1` | 1.3383022576488537e-05 |
| `D17` | `=D16+0.1` | -3.9 |
### Hoja2

| Celda | Fórmula | Valor guardado |
|---|---|---|
| — | No hay fórmulas de celda en esta hoja | — |
### Hoja3

| Celda | Fórmula | Valor guardado |
|---|---|---|
| — | No hay fórmulas de celda en esta hoja | — |

## Plantilla / solución relacionada

- [XLS-039: Anexo1.-escenarios-shifted.xlsx](../fuentes/xls-039-anexo1-escenarios-shifted.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

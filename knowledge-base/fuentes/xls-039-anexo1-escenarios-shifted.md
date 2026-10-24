# XLS-039: Escenarios shifted lognormal y valoración de caplet

Archivo: **Anexo1.-escenarios-shifted.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/anexos-valoracion-marco-black-soluciones/anexo1-escenarios-shifted.xlsx) · [Extracción detallada](../extracciones/xls-039-anexo1-escenarios-shifted.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Hoja1 | visible | `C6:P98` | 423 | 13 | 0 |
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
| `F16` | `=(F0+shift)*EXP(-0.5*volash^2*T)*EXP(volash*SQRT(T)*D16)-shift` | -0.0222255954804692 |
| `G16` | `=E16` | 1.3383022576488537e-05 |
| `H16` | `=MAX(F16-strike,0)` | 0 |
| `D17` | `=D16+0.1` | -3.9 |
| `J31` | `=LN((F0+shift)/(strike+shift))` | 0.03774032798284711 |
| `K31` | `=volash*T` | 0.3 |
| `L31` | `=J31/K31+0.5*K31` | 0.27580109327615704 |
| `M31` | `=J31/K31-0.5*K31` | -0.02419890672384295 |
| `N31` | `=NORMSDIST(L31)` | 0.6086495780214555 |
| `P31` | `=DT*D10*((F0+shift)*N31-(strike+shift)*O31)*M27` | 916.5236669789778 |
| `M34` | `=DT*D10*SUMPRODUCT(H16:H98,G16:G98)*M27` | 916.3980089358088 |
### Hoja2

| Celda | Fórmula | Valor guardado |
|---|---|---|
| — | No hay fórmulas de celda en esta hoja | — |
### Hoja3

| Celda | Fórmula | Valor guardado |
|---|---|---|
| — | No hay fórmulas de celda en esta hoja | — |

## Plantilla / solución relacionada

- [XLS-047: Anexo1.-escenarios-shifted_Plantilla.xlsx](../fuentes/xls-047-anexo1-escenarios-shifted-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

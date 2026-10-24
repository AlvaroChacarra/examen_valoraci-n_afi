# XLS-037: Cotizador de volatilidades por vencimiento

Archivo: **Anexo1.-cotizador-volas-mueve-plazos.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/anexos-valoracion-marco-black-soluciones/anexo1-cotizador-volas-mueve-plazos.xlsx) · [Extracción detallada](../extracciones/xls-037-anexo1-cotizador-volas-mueve-plazos.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Recuperar volatilidades shifted y normales que reproducen precios de caplets para una estructura de plazos.

Curvas de volatilidad, errores de precio y deltas en dos convenciones.

## Método observado

Obtener forwards y devengos desde descuentos; leer primas de mercado; valorar con shifted Black y con Bachelier; ajustar cada volatilidad a su precio; calcular deltas y comparar escalas por vencimiento.

## Teoría relacionada

PDF-009 pp. 30–40. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

La conversión entre volatilidades se hace igualando precios. La aproximación sigma_n≈(F+shift)sigma_sh es local, no una identidad global.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Sheet1 | visible | `B3:AD36` | 249 | 21 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `deltat` | `Sheet1!$B$7` |
| `K` | `Sheet1!$J$6` |
| `Nom` | `Sheet1!$J$5` |
| `shift` | `Sheet1!$M$4` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Sheet1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `AC3` | `=SUM(AC8:AC18)*10000` | 37.658344123186296 |
| `E7` | `=YEARFRAC($D$6,D7)` | 0.25 |
| `G7` | `=(F6/F7-1)/deltat` | -0.0037944366354505377 |
| `I8` | `=E8` | 0.5 |
| `M8` | `=LN((G8+shift)/(K+shift))` | -0.027332359429342833 |
| `N8` | `=L8*SQRT(E7)` | 0.05035952281942554 |
| `O8` | `=M8/N8+0.5*N8` | -0.5175648457492678 |
| `P8` | `=M8/N8-0.5*N8` | -0.5679243685686933 |
| `Q8` | `=NORMSDIST(O8)` | 0.30238095726170044 |
| `S8` | `=deltat*F8*((G8+shift)*Q8-(K+shift)*R8)*Nom` | 0.6439995523920291 |
| `T8` | `=(S8-J8)*1000000` | -0.44760797091036864 |
| `U8` | `=deltat*F8*Q8` | 0.075719168218659 |

## Plantilla / solución relacionada

- [XLS-045: Anexo1.-cotizador-volas-mueve-plazos_Plantilla.xlsx](../fuentes/xls-045-anexo1-cotizador-volas-mueve-plazos-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

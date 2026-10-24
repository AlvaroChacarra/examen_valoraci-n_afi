# XLS-045: Cotizador de volatilidades por vencimiento

Archivo: **Anexo1.-cotizador-volas-mueve-plazos_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/anexos-valoracion/anexo1-cotizador-volas-mueve-plazos-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-045-anexo1-cotizador-volas-mueve-plazos-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Sheet1 | visible | `B4:AD36` | 41 | 2 | 0 |

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
| `E7` | `=YEARFRAC($D$6,D7)` | 0.25 |
| `I8` | `=E8` | 0.5 |

## Plantilla / solución relacionada

- [XLS-037: Anexo1.-cotizador-volas-mueve-plazos.xlsx](../fuentes/xls-037-anexo1-cotizador-volas-mueve-plazos.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

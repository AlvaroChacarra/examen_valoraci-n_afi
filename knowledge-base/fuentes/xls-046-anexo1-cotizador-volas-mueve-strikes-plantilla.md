# XLS-046: Cotizador de volatilidades por strike

Archivo: **Anexo1.-cotizador-volas-mueve-strikes_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/anexos-valoracion/anexo1-cotizador-volas-mueve-strikes-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-046-anexo1-cotizador-volas-mueve-strikes-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Comparar smiles de volatilidad asociados a los mismos precios bajo lognormal, shifted lognormal y normal.

Sonrisas por convención y controles de reproducción de precios.

## Método observado

Leer precios y strikes; calcular precio shifted con distintos shifts; ajustar volatilidades por strike; calcular precios Bachelier y ajustar sigma normal; comparar errores y factores de escala.

## Teoría relacionada

PDF-009 pp. 30–40. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

El shift cambia la parametrización, no autoriza cambiar las primas de mercado objetivo.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `C3:AJ29` | 14 | 1 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `desc` | `Hoja1!$D$8` |
| `DT` | `Hoja1!$D$7` |
| `F0` | `Hoja1!$D$5` |
| `Nom` | `Hoja1!$D$3` |
| `T` | `Hoja1!$D$6` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `D15` | `=D14+0.2%` | -0.004 |

## Plantilla / solución relacionada

- [XLS-038: Anexo1.-cotizador-volas-mueve-strikes.xlsx](../fuentes/xls-038-anexo1-cotizador-volas-mueve-strikes.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

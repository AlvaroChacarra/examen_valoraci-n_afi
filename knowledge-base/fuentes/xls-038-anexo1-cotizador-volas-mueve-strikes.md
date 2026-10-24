# XLS-038: Cotizador de volatilidades por strike

Archivo: **Anexo1.-cotizador-volas-mueve-strikes.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/anexos-valoracion-marco-black-soluciones/anexo1-cotizador-volas-mueve-strikes.xlsx) · [Extracción detallada](../extracciones/xls-038-anexo1-cotizador-volas-mueve-strikes.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Hoja1 | visible | `C3:AJ29` | 358 | 21 | 0 |

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
| `W12` | `=SUM(W18:W28)` | 0.0005821821119133264 |
| `F14` | `=LN((F0+$N$10)/(D14+$N$10))` | 0.3483066942682158 |
| `G14` | `=N14*SQRT(T)` | 0.14995312500000277 |
| `H14` | `=F14/G14+0.5*G14` | 2.3977470567341785 |
| `I14` | `=F14/G14-0.5*G14` | 2.247793931734176 |
| `J14` | `=NORMSDIST(H14)` | 0.991751873862926 |
| `L14` | `=DT*Nom*desc*((F0+$N$10)*J14-(D14+$N$10)*K14)` | 49.922959001292355 |
| `M14` | `=ABS(L14-C14)` | 4.099870764662228e-05 |
| `Z14` | `=(F0-D14)/(AE14*SQRT(T))` | 2.3241867518880546 |
| `AA14` | `=NORMSDIST(Z14)` | 0.9899422564781724 |
| `AB14` | `=NORMDIST(Z14,0,1,FALSE)` | 0.02678641127504138 |
| `AC14` | `=DT*desc*((F0-D14)*AA14+AE14*SQRT(T)*AB14)*Nom` | 49.92314614485855 |

## Plantilla / solución relacionada

- [XLS-046: Anexo1.-cotizador-volas-mueve-strikes_Plantilla.xlsx](../fuentes/xls-046-anexo1-cotizador-volas-mueve-strikes-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

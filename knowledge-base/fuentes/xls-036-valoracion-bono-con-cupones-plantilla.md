# XLS-036: Cupones estructurados ligados al tipo swap

Archivo: **valoración bono con cupones_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/2-valoracion-marco-black-tipos/valoracion-bono-con-cupones-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-036-valoracion-bono-con-cupones-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Valorar una estructura de cupones por integración y por descomposición en instrumentos sencillos, incluyendo una versión con smile.

Valor de cupones y comparación entre integración y descomposición; fórmula de contraste AE16 en la solución.

## Método observado

Calcular anualidad y forward swap; identificar los tramos del cupón; integrar los pagos bajo la medida anualidad; separar pago fijo y opciones de strike distinto; aplicar Black por tramo; comparar el precio con volatilidades por strike.

## Teoría relacionada

PDF-008 pp. 21–32. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Las volatilidades distintas se asignan por strike a cada instrumento; no crean por sí solas una única distribución lognormal común.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `B4:AJ126` | 3 | 3 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `A0` | `Hoja1!$D$11` |
| `corte1` | `Hoja1!$G$12` |
| `corte2` | `Hoja1!$G$13` |
| `deltat` | `Hoja1!$D$4` |
| `Fswap0` | `Hoja1!$D$12` |
| `pago1` | `Hoja1!$H$12` |
| `pago3` | `Hoja1!$H$14` |
| `vola` | `Hoja1!$D$14` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `X7` | `=Fswap0` | 0.049356172306875404 |
| `D11` | `=SUM(H7:L7)*deltat` | 4.21852 |
| `D12` | `=(G7-L7)/D11` | 0.049356172306875404 |

## Plantilla / solución relacionada

- [XLS-028: pag 2.29 valoración bono con cupones.xlsx](../fuentes/xls-028-pag-2-29-valoracion-bono-con-cupones.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

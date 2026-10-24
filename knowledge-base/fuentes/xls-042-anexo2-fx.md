# XLS-042: Forwards, opciones y pagos quanto sobre FX

Archivo: **Anexo2.FX.xlsx**. Papel: **solución o ejemplo desarrollado**.

[Original](../../raw/marco-black/anexos-valoracion-marco-black-soluciones/anexo2-fx.xlsx) · [Extracción detallada](../extracciones/xls-042-anexo2-fx.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Comparar contratos sobre FX que pagan en euros o dólares y comprobar fórmulas con integración numérica.

Primas usuales, quanto y binarias, comparadas en la cabecera Q7:X8 en la solución.

## Método observado

Definir FX como euros por dólar; obtener el forward desde spot y descuentos; calcular call, put y forward usuales; convertir cada payoff a euros; obtener momentos y opciones quanto; contrastar con una rejilla normal y su descuento.

## Teoría relacionada

PDF-010 pp. 4–21. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Este anexo trata quanto sobre el propio FX. El ejercicio 3 añade una acción en dólares y requiere también correlación acción-FX. No confundir ambos contratos.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `A5:Y952` | 9442 | 36 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `descd` | `Hoja1!$E$14` |
| `desce` | `Hoja1!$E$13` |
| `FX0` | `Hoja1!$D$12` |
| `FXf0` | `Hoja1!$D$15` |
| `FXfwd0` | `Hoja1!$D$15` |
| `K` | `Hoja1!$D$9` |
| `nom` | `Hoja1!$D$10` |
| `probabs` | `Hoja1!$O$12:$O$952` |
| `T` | `Hoja1!$D$8` |
| `tipod` | `Hoja1!$D$14` |
| `tipoe` | `Hoja1!$D$13` |
| `vola` | `Hoja1!$D$11` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `Q7` | `=D26` | 13804.761178764755 |
| `R7` | `=D27` | 121149.8093369884 |
| `S7` | `=D29` | -107345.04815822365 |
| `U7` | `=J11` | -70823.32696782584 |
| `V7` | `=J20` | 14371.20955209884 |
| `W7` | `=J25` | 172459.01234405185 |
| `X7` | `=J31` | 176282.50129476347 |
| `Q8` | `=SUMPRODUCT(Q12:Q952,probabs)*desce` | 13801.379041672248 |
| `J11` | `=E13*FXfwd0*(FXfwd0*EXP(vola^2*T)-K)*nom` | -70823.32696782584 |
| `O12` | `=NORMDIST(N12,0,1,FALSE)*0.01` | 1.4867195147342977e-08 |
| `P12` | `=FXf0*EXP(-0.5*T*vola^2)*EXP(vola*SQRT(T)*N12)` | 0.3699843312191504 |
| `Q12` | `=MAX(P12-K,0)*nom` | 0 |
| `R12` | `=MAX(K-P12,0)*nom` | 530015.6687808495 |
| `V12` | `=MAX(P12-K,0)*P12*nom` | 0 |

## Plantilla / solución relacionada

- [XLS-048: Anexo2.FX_Plantilla.xlsx](../fuentes/xls-048-anexo2-fx-plantilla.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

# XLS-048: Forwards, opciones y pagos quanto sobre FX

Archivo: **Anexo2.FX_Plantilla.xlsx**. Papel: **plantilla de ejercicios**.

[Original](../../raw/marco-black/anexos-valoracion/anexo2-fx-plantilla.xlsx) · [Extracción detallada](../extracciones/xls-048-anexo2-fx-plantilla.md) · [Mapa del curso](../MAPA_RELACIONES.md)

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
| Hoja1 | visible | `A5:Y952` | 4 | 4 | 0 |

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
| `E13` | `=1/(1+tipoe*T)` | 0.9950248756218907 |
| `E14` | `=1/(1+tipod*T)` | 0.9852216748768474 |
| `D15` | `=FX0*(1+tipoe)/(1+tipod)` | 0.7921182266009852 |
| `E15` | `=FX0*E14/E13` | 0.7921182266009853 |

## Plantilla / solución relacionada

- [XLS-042: Anexo2.FX.xlsx](../fuentes/xls-042-anexo2-fx.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

# XLS-006: Jarrow–Rudd: árbol, simulación, valoración y réplica

Archivo: **Plantilla_3.xlsx**. Papel: **plantilla**.

[Original](../../raw/fundamentos/sesion-ii/plantilla-3.xlsx) · [Extracción detallada](../extracciones/xls-006-plantilla-3.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Construir un árbol binomial calibrado a tipo y volatilidad y comparar distintos métodos de valoración de una opción europea.

Prima, comparación con Black–Scholes, árboles de cash/delta y simulación de cobertura. La solución contiene el JR con ajuste exacto de martingala mediante cosh.

## Método observado

Calcular u,d,p=1/2 y descuentos; construir el árbol de S; comprobar la distribución y varianza de log-retornos; simular sendas; valorar por fórmula binomial, backward induction y simulación; obtener las posiciones de réplica.

## Teoría relacionada

PDF-003 pp. 6–60; PDF-006 pp. 4–46. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

Plantilla de seis pasos, no solución del encargo de 36 pasos. No sustituir la especificación exacta por su aproximación exponencial sin decirlo.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `C3:R3061` | 5 | 5 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `call_put` | `Hoja1!$D$48` |
| `d` | `Hoja1!$H$12` |
| `deltat` | `Hoja1!$D$11` |
| `desc_per` | `Hoja1!$D$13` |
| `desc_T` | `Hoja1!$D$14` |
| `factorVola` | `Hoja1!$K$11` |
| `S0` | `Hoja1!$D$7` |
| `strike` | `Hoja1!$D$49` |
| `T` | `Hoja1!$D$12` |
| `tipo` | `Hoja1!$D$5` |
| `u` | `Hoja1!$H$11` |
| `vola` | `Hoja1!$D$6` |

## Cálculos representativos de este archivo

Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.

### Hoja1

| Celda | Fórmula | Valor guardado |
|---|---|---|
| `D11` | `=1/12` | 0.08333333333333333 |
| `D12` | `=6*deltat` | 0.5 |
| `I48` | `=(LN(S0/strike)+(tipo+0.5*vola^2)*T)/(vola*SQRT(T))` | -0.10979088679435575 |
| `I49` | `=(LN(S0/strike)+(tipo-0.5*vola^2)*T)/(vola*SQRT(T))` | -0.32192292115032 |
| `I50` | `=S0*NORMSDIST(I48)-strike*EXP(-T*tipo)*NORMSDIST(I49)` | 5.201588299180152 |

## Plantilla / solución relacionada

- [XLS-005: Plantilla_3 - Solucion1.xlsx](../fuentes/xls-005-plantilla-3-solucion1.md)

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

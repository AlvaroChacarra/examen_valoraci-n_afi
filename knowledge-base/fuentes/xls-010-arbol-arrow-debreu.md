# XLS-010: Árbol de precios de Arrow–Debreu

Archivo: **Arbol arrow-debreu.xlsx**. Papel: **ejemplo con hojas de distinto grado de desarrollo**.

[Original](../../raw/fundamentos/sesioniii/arbol-arrow-debreu.xlsx) · [Extracción detallada](../extracciones/xls-010-arbol-arrow-debreu.md) · [Mapa del curso](../MAPA_RELACIONES.md)

## Qué ejercicio plantea y qué busca

Reutilizar precios de estado descontados para valorar una cartera con varios pagos y vencimientos.

Valor de la cartera y comprobación de que la suma de precios de estado a un plazo coincide con su descuento.

## Método observado

Construir el JR; inicializar el precio de estado raíz; propagar precios descontados por las dos ramas y sumar contribuciones que recombinan; formar el árbol de payoffs de dos calls y una put; sumar precio de estado por flujo.

## Teoría relacionada

PDF-003 pp. 52–53; PDF-006 p. 46. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.

## Precaución concreta

El archivo conserva zonas de plantilla y hojas vacías. Los precios de estado no son probabilidades sin descontar.

## Hojas e información recuperada

| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |
|---|---|---|---:|---:|---:|
| Hoja1 | visible | `C1:XFD66` | 56 | 13 | 0 |
| Hoja2 | visible | `A1:A1` | 0 | 0 | 0 |
| Hoja3 | visible | `A1:A1` | 0 | 0 | 0 |

## Entradas y resultados localizables

Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.

| Nombre | Celda o rango |
|---|---|
| `d` | `Hoja1!$H$12` |
| `deltat` | `Hoja1!$D$11` |
| `factorVola` | `Hoja1!$J$11` |
| `S0` | `Hoja1!$D$7` |
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
| `H11` | `=I11*J11*K11` | 1.0869300107425321 |
| `I11` | `=EXP(tipo*deltat)` | 1.0005001250208359 |
| `J11` | `=2/(EXP(vola*SQRT(deltat))+EXP(-vola*SQRT(deltat)))` | 0.9962616831161694 |
| `K11` | `=EXP(vola*SQRT(deltat))` | 1.0904631784921235 |
| `D12` | `=6*deltat` | 0.5 |
| `K12` | `=EXP(-vola*SQRT(deltat))` | 0.9170415101799084 |
| `D18` | `=S0` | 80 |
| `E18` | `=D18*u` | 86.95440085940257 |
| `E19` | `=D18*d` | 73.12561914393117 |
| `H57` | `=MAX($E$52-H18,0)` | 0 |
| `I57` | `=MAX(I18-$E$51,0)` | 46.36623712461321 |
| `J57` | `=MAX(J18-$E$50,0)` | 45.91660542163655 |
### Hoja2

| Celda | Fórmula | Valor guardado |
|---|---|---|
| — | No hay fórmulas de celda en esta hoja | — |
### Hoja3

| Celda | Fórmula | Valor guardado |
|---|---|---|
| — | No hay fórmulas de celda en esta hoja | — |

## Macros, imágenes y dependencias

Proyecto VBA presente: **False**. Vínculos externos declarados: **0**. Los módulos recuperados y los textos de objetos están en la extracción.

Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.

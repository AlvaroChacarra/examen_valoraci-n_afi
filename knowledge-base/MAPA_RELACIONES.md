# Mapa de contenidos y relaciones

Las relaciones son una guía de lectura revisada, no enlaces inferidos únicamente por nombres de archivo.

## Ruta conceptual

1. Fundamentos: escenarios, flujos y numerario; réplica, arbitraje y probabilidad de valoración.
2. Modelo matricial y multiperiodo: pasar de resolver una cartera estática a estrategias adaptadas y autofinanciadas.
3. Árboles: materializar esas condiciones en Jarrow–Rudd, americanas, dividendos y precios de estado.
4. Black equity: expresar dinámicas martingala y valorar por fórmulas, integración o simulación.
5. Tipos: elegir el bono de pago o la anualidad como numerario; explicar por qué cambia la valoración al cambiar la fecha del flujo.
6. Multicurva y Bachelier: separar proyección/descuento y distinguir volatilidad relativa de absoluta.
7. FX y quanto: mantener moneda, unidades, correlaciones y medida de valoración consistentes.

## Teoría, práctica y uso en el encargo

| Bloque práctico | Teoría | Archivos normalizados | Uso |
|---|---|---|
| Ley de los grandes números con pagos independientes | PDF-004 pp. 16–21; PDF-005 pp. 30–39 | [XLS-001](fuentes/xls-001-grandes-numeros-1-iid.md) | Base común de los tres ejercicios |
| Correlación y límites de la diversificación | PDF-004 pp. 16–21; PDF-005 pp. 30–39 | [XLS-002](fuentes/xls-002-grandes-numeros-2-correlacion.md) | Base común de los tres ejercicios |
| Mercado matricial: réplica, arbitraje y numerarios | PDF-004 pp. 37–76; PDF-005 pp. 59–92 | [XLS-003](fuentes/xls-003-plantilla1.md), [XLS-007](fuentes/xls-007-plantilla1-solucion.md) | Base común de los tres ejercicios |
| Réplica dinámica y cambio de numerario | PDF-004 pp. 77–101; PDF-005 pp. 93–118 | [XLS-004](fuentes/xls-004-plantilla2.md), [XLS-008](fuentes/xls-008-plantilla2-solucion.md) | Base común de los tres ejercicios |
| Jarrow–Rudd: árbol, simulación, valoración y réplica | PDF-003 pp. 6–60; PDF-006 pp. 4–46 | [XLS-005](fuentes/xls-005-plantilla-3-solucion1.md), [XLS-006](fuentes/xls-006-plantilla-3.md) | Ejercicio 1 |
| Dividendos discretos y ejercicio americano | PDF-003 pp. 49–71; PDF-006 pp. 40–50 | [XLS-009](fuentes/xls-009-americana-con-dividendos.md) | Ejercicio 1 |
| Árbol de precios de Arrow–Debreu | PDF-003 pp. 52–53; PDF-006 p. 46 | [XLS-010](fuentes/xls-010-arbol-arrow-debreu.md) | Ejercicio 1 |
| Árbol recombinante con curva de volatilidad | PDF-003 pp. 74–83; PDF-006 pp. 54–58 | [XLS-011](fuentes/xls-011-arbol-volas-no-ctes.md) | Ejercicio 1 |
| Calibración Black–Derman–Toy y derivados de tipos | PDF-003 pp. 84–101; PDF-006 pp. 59–72 | [XLS-012](fuentes/xls-012-bdt.md) | Ejercicio 2; CMS/swaption amplían contexto |
| Call Black–Scholes y error de cobertura discreta | PDF-007 pp. 18–28 | [XLS-013](fuentes/xls-013-pag-1-27-call-cobertura-discreta.md), [XLS-018](fuentes/xls-018-1-1-call-cobertura-discreta-plantilla.md) | Ejercicio 3 y simulación del extra |
| Payoff arbitrario: integral, Monte Carlo y descomposición | PDF-007 pp. 29–30 | [XLS-014](fuentes/xls-014-pag-1-32-payoff-arbitrario.md), [XLS-019](fuentes/xls-019-1-2-payoff-arbitrario-plantilla.md) | Ejercicio 3 y simulación del extra |
| Distribución implícita en calls y puts | PDF-007 pp. 29–30; PDF-004 pp. 125–130 | [XLS-015](fuentes/xls-015-pag-1-33-probs-implicitas-con-calls-puts.md), [XLS-020](fuentes/xls-020-1-3-probs-implicitas-con-calls-puts-plantilla.md) | Ejercicio 3 y simulación del extra |
| Call con dividendo discreto por condicionamiento | PDF-007 pp. 31–33 | [XLS-016](fuentes/xls-016-pag-1-36-dividendo-discreto.md), [XLS-021](fuentes/xls-021-1-4-dividendo-discreto-plantilla.md) | Ejercicio 3 y simulación del extra |
| Opciones sobre el máximo de dos activos | PDF-007 pp. 34–35 y 40–45 | [XLS-017](fuentes/xls-017-pag-1-39-opcion-sobre-dos-activos.md), [XLS-022](fuentes/xls-022-1-5-opcion-sobre-dos-activos-plantilla.md) | Ejercicio 3 y simulación del extra |
| Cap como cartera de caplets | PDF-008 pp. 5–13 | [XLS-023](fuentes/xls-023-pag-2-13-cap.md), [XLS-030](fuentes/xls-030-cap-plantilla.md) | Ejercicio 2; CMS/swaption amplían contexto |
| Caplet, floorlet y FRA usuales | PDF-008 pp. 5–13 | [XLS-024](fuentes/xls-024-pag-2-13-caplet-floorlet.md), [XLS-031](fuentes/xls-031-caplet-floorlet-plantilla.md) | Ejercicio 2; CMS/swaption amplían contexto |
| FRA y caplet in arrears lognormales | PDF-008 pp. 14–19 | [XLS-025](fuentes/xls-025-pag-2-17-fra-caplet-floorlet-in-arrears.md), [XLS-033](fuentes/xls-033-fra-caplet-floorlet-in-arrears-plantilla.md) | Ejercicio 2; CMS/swaption amplían contexto |
| Swap usual frente a swap in arrears | PDF-008 pp. 14–19 y 21–22 | [XLS-026](fuentes/xls-026-pag-2-18-swap-in-arrears.md), [XLS-034](fuentes/xls-034-swap-in-arrears-plantilla.md) | Ejercicio 2; CMS/swaption amplían contexto |
| Swaption payer bajo numerario anualidad | PDF-008 pp. 21–28 | [XLS-027](fuentes/xls-027-pag-2-28-swaption.md), [XLS-035](fuentes/xls-035-swaption-plantilla.md) | Ejercicio 2; CMS/swaption amplían contexto |
| Cupones estructurados ligados al tipo swap | PDF-008 pp. 21–32 | [XLS-028](fuentes/xls-028-pag-2-29-valoracion-bono-con-cupones.md), [XLS-036](fuentes/xls-036-valoracion-bono-con-cupones-plantilla.md) | Ejercicio 2; CMS/swaption amplían contexto |
| CMS 10 años y ajuste de convexidad | PDF-008 pp. 29–32 | [XLS-029](fuentes/xls-029-pag-2-35-cms10y.md), [XLS-032](fuentes/xls-032-cms10y-plantilla.md) | Ejercicio 2; CMS/swaption amplían contexto |
| Cotizador de volatilidades por vencimiento | PDF-009 pp. 30–40 | [XLS-037](fuentes/xls-037-anexo1-cotizador-volas-mueve-plazos.md), [XLS-045](fuentes/xls-045-anexo1-cotizador-volas-mueve-plazos-plantilla.md) | Normal para ejercicio 2; multicurva como contraste |
| Cotizador de volatilidades por strike | PDF-009 pp. 30–40 | [XLS-038](fuentes/xls-038-anexo1-cotizador-volas-mueve-strikes.md), [XLS-046](fuentes/xls-046-anexo1-cotizador-volas-mueve-strikes-plantilla.md) | Normal para ejercicio 2; multicurva como contraste |
| Escenarios shifted lognormal y valoración de caplet | PDF-009 pp. 30–34 | [XLS-039](fuentes/xls-039-anexo1-escenarios-shifted.md), [XLS-047](fuentes/xls-047-anexo1-escenarios-shifted-plantilla.md) | Normal para ejercicio 2; multicurva como contraste |
| Valoración de swap con curvas distintas | PDF-009 pp. 7–16 | [XLS-040](fuentes/xls-040-anexo1-p16-calculo-swap.md), [XLS-043](fuentes/xls-043-anexo1-calculo-swap.md) | Normal para ejercicio 2; multicurva como contraste |
| Tipo swap par en marco multicurva | PDF-009 pp. 15–16 | [XLS-041](fuentes/xls-041-anexo1-p16-calculo-tipo-swap.md), [XLS-044](fuentes/xls-044-anexo1-calculo-tipo-swap-plantilla.md) | Normal para ejercicio 2; multicurva como contraste |
| Forwards, opciones y pagos quanto sobre FX | PDF-010 pp. 4–21 | [XLS-042](fuentes/xls-042-anexo2-fx.md), [XLS-048](fuentes/xls-048-anexo2-fx-plantilla.md) | Ejercicio 3 y componente extranjero del extra |

## Relaciones que evitan errores

- **JR exacto y JR aproximado:** PDF-003 pp. 24–25 los distingue. Los Excel de fundamentos usan la versión exacta.
- **Volatilidad por año y spot por vencimiento:** el encargo da volatilidades de periodos; el Excel de curva trabaja con t sigma_spot(t)^2. Convertir antes de comparar.
- **Réplica exacta en árbol y hedge discreto Black:** un mercado binomial de dos sucesores admite réplica local exacta; discretizar el hedge de un modelo continuo genera descasamiento.
- **Pago usual e in arrears:** el activo subyacente puede ser el mismo y el numerario conveniente cambiar con la fecha de pago.
- **In arrears lognormal y normal:** reutilizar el cambio de numeraire y sustituir la distribución/momentos, no copiar los resultados lognormales.
- **Quanto FX y quanto equity:** el primero puede involucrar FX² al convertir un pago en dólares. El segundo exige el término de covariación entre acción y FX.
- **Máximo y cesta promedio:** comparten simulación correlacionada; no necesariamente comparten el signo de sensibilidad a correlación.
- **Plantilla y solución:** son versiones pedagógicas distintas; una solución del curso puede conservar errores o parámetros no alineados con el enunciado.

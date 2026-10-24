# Segunda revisión — aptitud para preparar los tres ejercicios

**Veredicto: APTA para comenzar los tres ejercicios obligatorios.** Certificación documental acotada a las fuentes incorporadas el 24/10/2026: integridad, extracción, dependencias y rutas metodológicas. No certifica todavía precios, cobertura de una implementación, fórmulas nuevas ni una entrega final del alumno.

Base revisada: commit `82e829924135448be4850998ebe7813f85c0c682`. Modo RECONCILE: se conserva la estructura canónica y se corrigen sus huecos, sin crear otra base paralela.

## Hallazgos y cierre

| Hallazgo | Impacto | Cierre |
|---|---|---|
| PDF-005 tenía 98 páginas con menos de 80 caracteres de texto nativo y no tenía OCR | El índice existía, pero buena parte de la sesión no se podía consultar como texto | OCR auxiliar de sus 138 páginas, conservando texto nativo separado |
| PDF-006 sólo tenía OCR selectivo en 60 páginas | Podían quedar figuras sin recuperar por superar un umbral de texto nativo | OCR auxiliar de sus 74 páginas; se mantienen las pp.51–53 sobre suavizado |
| La extracción de nombres sólo recogía el ámbito de libro | Faltaban nombres locales de hojas ocultas y configuración Solver | Incorporados 490 nombres locales en 15 libros; quedan 797 nombres globales/locales documentados |
| El validador inicial comprobaba número de hojas, sin cotejar familias con el original | Un total de hojas correcto no certificaba recuperación del cálculo | Segundo comprobador coteja estados, 60.701 fórmulas, 880 familias y sus literales con los libros |
| Las referencias de nombres de la ficha de XLS-011 podían leerse como universales | El lector podía usar nombres de Hoja1 al interpretar Hoja2 | Explicado el sombreado local: por ejemplo, pasovola de Hoja2 apunta a su propio E19 |
| Había advertencias metodológicas dispersas | Un agente podía comenzar sin cerrar una decisión esencial | La matriz siguiente reúne las decisiones y controles por apartado |

Los originales permanecen intactos. Se revisaron los contratos, el texto y ecuaciones del PPT, las rutas de teoría, las tres hojas ocultas y los mecanismos de pago y numeraire. Los errores guardados y vínculos externos siguen visibles en [LIMITACIONES](LIMITACIONES.md); no se reparó evidencia docente.

## Ejercicio1 — contrato, método y prueba necesaria

| Apartado | Evidencia suficiente | Qué se decide o demuestra al resolver |
|---|---|---|
| Árbol de arranque | PDF-002 p.2; PDF-003 pp.24–25,74–83; XLS-005/006/011 | 36 pasos mensuales y volatilidades de intervalos anuales; documentar la representación de estados y verificar martingala sin imponer recombinación incorrecta |
| a: precios | PDF-003 pp.34–39,49–51; conceptos de árboles | Mismo modelo para los tres contratos; europea≤bermuda≤americana de la malla; no tratar esa americana discreta como ejercicio continuo exacto |
| b: 15 días | PDF-002 p.2 y calendario contractual | Mantener vencimiento y fechas de ejercicio; declarar base temporal y si se compara cambio de valor o P&L financiado; usar el mismo criterio para las tres |
| c: réplica | PDF-003 pp.54–60; XLS-005 y Hoja2 de XLS-011 | Actualizar acción y cash autofinanciados sobre la misma dinámica simulada; liquidar y detener al ejercer; informar error de réplica y su tolerancia |
| c: ejercicio | Regla de máximo en fechas bermuda | Estimar bajo la medida declarada la primera parada al año1 y a vencimiento; no confundir ejercicio, estar ITM y supervivencia; declarar tratamiento de empates y payoff cero |
| d: mejora | PDF-006 pp.51–53, recuperadas y contrastadas visualmente | Sustituir último retroceso por continuación Black–Scholes sin añadir pasos, manteniendo la comparación con intrínseco donde pueda ejercerse; cuantificar mejora frente a una referencia justificada |

La malla uniforme en varianza de XLS-011 es una referencia, no una licencia para mover las catorce fechas del contrato. Una cobertura discreta de una difusión Black–Scholes (XLS-013) tampoco es la misma prueba que la réplica dentro del árbol. Estas son decisiones de implementación futuras; no falta un archivo para abordarlas.

## Ejercicio2 — unión de los dos desarrollos de clase

| Pieza | Evidencia suficiente | Control al resolver |
|---|---|---|
| Contrato | PDF-002 p.3 | FRA y caplet pagan en T, según el tipo de [T,T+delta]; no añadir otro denominador de liquidación |
| Medida y pago temprano | PDF-008 pp.5–19; XLS-025/033 | F es martingala bajo la medida del bono de T+delta; el factor 1+delta F_T queda dentro de la esperanza |
| Distribución normal | PDF-009 pp.38–40 | sigma_n es absoluta; rehacer momentos completos y truncados normales, sin importar exp(sigma²T) del caso lognormal |
| Coherencia | Conceptos de tipos y normal | Unidades, límite sigma_n→0 y paridad caplet-floorlet=FRA para el mismo calendario y contrato; comparar la fórmula propia con integración independiente |

**Matiz teórico para la memoria:** una normal no degenerada tiene soporte en toda la recta. La identidad single-curve con bono estrictamente positivo exige 1+delta F_T>0; por tanto una normal exacta sin cota y esa identidad no constituyen globalmente un modelo exacto de bonos positivos. Es una inferencia matemática de los supuestos, no un dato adicional del enunciado. Se recomienda desarrollar la aproximación normal docente que pide el trabajo y declarar su alcance, sin truncar o cambiar la distribución silenciosamente. No es un hueco documental ni se ha resuelto aún la derivación solicitada.

## Ejercicio3 — obligaciones de la plantilla

| Bloque de la presentación | Evidencia y comprobación al desarrollar |
|---|---|
| (1)–(2), diap.11 | Dinámicas y soluciones de las martingalas M,N; brownianos U,V y su correlación |
| (3), diap.12 | Diccionario FX,S ↔ M,N; relacionar los parámetros auxiliares con los observables |
| (4)–(5), diap.14–16 | Itô de FX y de S·FX, incluido el término de covariación; comprobar deriva cero de M,N |
| (6), diap.17 | Distribuciones terminales conjuntas con horizonte y correlación correctos |
| (7), diap.18–20 | Forward usual: misma valoración por esperanza en EUR y por réplica estática |
| (8), diap.21–22 | Forward quanto: flujo ya expresado en EUR; no multiplicar otra vez por FX |
| (9), diap.23–24 | Call quanto: desarrollo de la esperanza positiva y descuento en EUR |
| (10), diap.25 | Bonus +0,5: call usual USD convertida a EUR dentro del mismo marco |

La presentación y sus 25 diapositivas están disponibles. El inversor es EUR; FX son euros por dólar; el factor exp(qt) corresponde a retorno total con dividendos. No identificar rho_M,N con rho_F,S sin transformar procesos. Donde la plantilla mezcla t/T en un flujo terminal, el contrato de diap.8 y el vencimiento T son la referencia: explicitar la corrección notacional.

## Extra y decisiones no cerradas por el enunciado

El extra de cesta no bloquea comenzar los tres obligatorios. Antes de su precio final habrá que declarar moneda y nominal, fecha de liquidación, dividendos y tratamiento del SPX en EUR, además de qué correlaciones se varían. El nivel inicial de diciembre2026 es futuro a la fecha de valoración; el promedio usa doce niveles relativos, no retornos mensuales consecutivos. Cada matriz de correlaciones ensayada debe ser semidefinida positiva.

## Evidencia de comprobación y límites de la certificación

Se verificaron 56 documentos finales contra los ZIP anidados y los tres adjuntos de evaluación contra sus hashes: 59 fuentes, 10 PDF/620 páginas, 60 hojas con sus tres ocultas y 25 diapositivas. La segunda comprobación recorrió las 60.701 fórmulas y contrastó los literales de 880 familias, los 797 nombres y los estados de hoja. Todas las páginas de las sesiones I/II tienen OCR auxiliar: 212.

Comandos reproducibles:

```bash
python scripts/validate_knowledge_base.py
python scripts/review_readiness.py
# Si también se conservan los ZIP de entrada:
python scripts/review_readiness.py --archives-dir /ruta/a/los/adjuntos
```

Ambas comprobaciones deben pasar. La comprobación de enlaces y alcanzabilidad no certifica comprensión humana ni exactitud de cada signo OCR. Los conceptos matemáticos centrales y las páginas críticas del encargo se contrastaron con las fuentes. Una ecuación nueva, una modificación del contrato o un símbolo no restaurado que afecte al resultado requieren su verificación específica al resolver.

**Conclusión operativa:** no se identifican carencias documentales críticas restantes para iniciar E1, E2 y E3. Persisten las decisiones metodológicas de la matriz, que deben quedar explícitas en las soluciones. El siguiente paso es fijar la especificación de E1 antes de programar su árbol.

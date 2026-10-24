# Revisión independiente del núcleo matemático

**Veredicto: PASS en el alcance revisado.** Modo standard. Conformidad sustancial: FULL para las matemáticas, código y memoria de los tres ejercicios en el commit indicado. Confianza HIGH. No se detectan hallazgos materiales ni se requieren correcciones antes de construir la entrega sobre este núcleo.

## Contrato y versión

- Repositorio `examen_valoraci-n_afi`, rama `solucion/mefc-2026`.
- Baseline del encargo: `25b879067144d380edd08b0ecf19dd861410d628`.
- **Commit auditado: `5c0e1df515917a57dad2a718ef30765f97c85998`.** Auditoría realizada el 24/10/2026, aproximadamente 17:33–17:39 UTC.
- Uso autorizado por este dictamen: confiar en los resultados matemáticos de E1/E2/E3 y continuar la preparación del paquete. La publicación o entrega integrada exige revisar sus artefactos finales.
- Fuentes congeladas antes de abrir implementación: PDF-002 pp.1–4, PPT-001 diapositivas 1–25, PDF-001 pp.1–2, decisiones de `MATRIZ_CUMPLIMIENTO.md` y requisitos comunicados por el responsable. Se leyeron AGENTS.md y la documentación de entrada obligatoria. Se verificó además el OfficeMath del original PPT-001 diap.25 para contrastar el signo de la errata.

Requisitos materiales: E1 conserva 36 intervalos mensuales, volatilidades anuales por bloques y 14 fechas de ejercicio; revalora a 15/365 sin reiniciar calendario; compara P&L; replica y simula el mismo árbol; estima primera parada y mejora sin más pasos. E2 deriva pagos en T bajo medida U, normal absoluta y una curva. E3 completa los diez bloques de la presentación, incluida call usual, con EUR/USD y covariación coherentes. Memoria explicativa y evidencias reproducibles. El extra de cesta se mantiene fuera del alcance aprobado.

## Hallazgos materiales

Ninguno. No se han identificado BLOCKER, HIGH ni MEDIUM en este alcance. No se proponen cambios de implementación por preferencia de estilo o complejidad.

## Evidencia decisiva

**E1.** `src/ejercicio1.py` y `MEMORIA.md`, apartados a–d, son coherentes con el contrato y entre sí. Una recursión escalar independiente, escrita sin importar el pricer de la solución, reproduce las seis primas inicial/15 días con diferencias del orden de 1e-14. La propagación de masa independiente reproduce primera parada en mes 12 = 0,019287109375 y mes 36 = 0,0606478278641589. La representación por conteos de bloque conserva el árbol no falsamente recombinante; el acortamiento del primer intervalo respeta los cambios de volatilidad en años contractuales 1 y 2.

La referencia independiente por diferencias finitas Crank–Nicolson en log-precio, con pasos implícitos tras cada kink y máximo únicamente en las fechas bermuda, da:

|Paso log-precio|Precio de difusión|
|---:|---:|
|0,004|9,113648980384008|
|0,002|9,113661534207784|
|0,001|9,113664723856598|
|0,0005|9,113665366382763|

Esto contrasta el semigrupo FFT de la implementación (9,11366796 en su última malla), con una diferencia final de aproximadamente 2,6e-6. Es evidencia suficiente para la reducción de error declarada al pasar de JR 9,16290759 a JR suavizado 9,13920110. La prueba no constituye una cota matemática certificada de la referencia de difusión.

**E2.** Se revisaron independientemente numerario, identidad de bonos, momento cuadrático y momentos truncados. El factor por pagar en T es multiplicativo `(1+δF_T)`. Las fórmulas FRA/caplet y paridad floorlet se corresponden con ese contrato. Una integración directa en la coordenada del tipo, en 50 escenarios aleatorios de tipos/strikes negativos y positivos, volatilidad y devengo, contrasta los tres pagos; error máximo aproximadamente 1,77e-8 unidades monetarias con nominal 1e6. Véase el JSON de contraste para la cifra exacta.

**E3.** Se comprobaron el diccionario M,N ↔ FX,S, parámetros y casos degenerados, Itô del producto, signo de la deriva quanto, distribuciones y los cuatro contratos. La call usual recupera Black USD multiplicada por FX spot después de integrar FX terminal dentro del marco EUR. Una integral bidimensional anidada que integra directamente el payoff usual en 12 escenarios aleatorios da error máximo aproximadamente 3,56e-14 EUR. La corrección del signo de rUSD en el d impreso en diap.25 es matemáticamente necesaria y está declarada en la memoria.

Se ejecutaron los **11 tests del commit** con resultado OK (1,495 s observado). Se ejecutaron los dos validadores documentales: 59 fuentes, 620 páginas PDF, 25 diapositivas, 60 hojas, 60.701 fórmulas y 797 nombres; ambos pasan. El primer validador comprueba hashes de originales sin errores. Estas comprobaciones documentales acreditan integridad, no son el oráculo de precios utilizado en la auditoría.

## Reproducción exacta de los contrastes independientes

Desde la raíz del repositorio, con Python, NumPy y SciPy disponibles:

```bash
python soluciones/auditoria/contraste_independiente_e1.py --output /tmp/contraste_independiente_e1.json
python soluciones/auditoria/contraste_independiente_e2_e3.py --commit 5c0e1df515917a57dad2a718ef30765f97c85998 --output /tmp/contraste_independiente_e2_e3.json
python -m unittest discover -s soluciones/tests -v
python scripts/validate_knowledge_base.py
python scripts/review_readiness.py
```

E1 no importa implementación: sus resultados reproducen la versión auditada y pueden cotejarse con el JSON archivado. E2/E3 cargan mediante `git show` las funciones `prices` del commit explícito; sus integrales se calculan aparte y no utilizan el integrador ni los momentos de la solución. Los resultados originales están en los JSON vecinos. Los comandos de tests y validadores usan el checkout desde el que se ejecutan; para repetir exactamente aquella suite debe emplearse un checkout de `5c0e1df`, sin incluir cambios posteriores.

## Cobertura y riesgos residuales

La memoria satisface el desarrollo teórico solicitado y las limitaciones están explicadas con precisión: americana sólo en la malla mensual, probabilidades bajo Q, P&L por una opción de cada contrato, normal formal incompatible en sus colas con bonos globalmente positivos. No se reclama cobertura perfecta de una difusión al rebalancear mensualmente. Estos límites son apropiados al encargo y no defectos ocultos.

La validación es para los datos del enunciado y las escalas ilustrativas. No certifica una API de producción con inputs arbitrarios ni la integración de E3 en colas de volatilidad extrema. Los IC Monte Carlo son marginales y no garantías simultáneas. E2 conserva la aproximación normal sin truncarla: fuera de las escalas en que la cola imposible es despreciable sus precios formales no deben interpretarse como un modelo global de arbitraje.

## No auditado todavía / revisión posterior

**No se inspeccionaron ni aprobaron las hojas XLSX, su recálculo, el PDF final, README, comandos de generación, guía de defensa, estado final de la matriz ni el empaquetado integrado.** En esta fase eran artefactos en preparación en el worktree. Tampoco se revisaron modificaciones de código o memoria posteriores a `5c0e1df`, aunque fueran visibles después de terminar los contrastes. Una revisión posterior debe identificar su propio commit y distinguir cualquier delta frente a este informe.

La auditoría original fue de sólo lectura. La autorización posterior permite conservar exclusivamente estos scripts, JSON e informe bajo `soluciones/auditoria/`; el auditor no modificó implementación, datos originales ni documentación de la solución.

## Mejoras no bloqueantes

Ninguna mejora adicional es necesaria para el núcleo auditado. Lo pendiente es acreditar la entrega integrada y completar los nombres de integrantes antes de su presentación académica.

# Evidencia de validación

Ámbito: soluciones nuevas en `soluciones/`, separadas de las 59 fuentes docentes originales. El resultado de cada comando está en `resultados/`; una prueba de integridad documental no acredita precios. La revisión independiente está en [auditoria](auditoria/REVISION_5c0e1df.md).

## Pruebas específicas ejecutadas

`python -m unittest discover -s soluciones/tests -v`: **12 pruebas pasan** (5 E1, 3 E2, 3 E3 y una regresión del motor de hojas). Semillas fijas y contrastes deterministas permiten detectar regresiones numéricas; no se compara sólo con cifras pegadas.

|Prueba|Qué puede detectar|Resultado / criterio|
|---|---|---|
|E1 contrato, calendario y martingala|Volatilidades desplazadas, calendario incorrecto, JR aproximado mezclado|36 pasos,14 fechas; esperanza de u,d=exp(rh); varianza residual correcta|
|E1 europea por producto de binomiales|Error en retroceso, índices o distribución terminal|Coincide con retroceso a 11 decimales|
|E1 masa absorbida y pagos|Doble ejercicio, pérdida de masa, política inconsistente|Masa 1 con expiración; PV pagos=prima a 11 decimales|
|E1 réplica local y acumulada|Delta/cash incorrectos, inyección de capital, falta de parada|Máximos ~1e−13; tolerancia 1e−10 u.m.|
|E1 MC vs exacta|Simulación distinta del árbol o primer ejercicio erróneo|200.000 sendas,14 fechas, diferencias<5 errores estándar+1/N; IC95 Wilson reportados|
|E1 referencia y suavizado|Afirmar mejora sin referencia, americana continua confundida|Difusión con mismas14 fechas; refinamiento .0005→.00025 cambia2,52e−6; error suavizado menor|
|E1 referencia europea y dominio|Integración/FFT o límites de dominio defectuosos|Europea vs BS error<2e−6; dominio6→8 cambia<1e−8 a dx=.001|
|E2 cuadratura original|Ajuste de distribución/pago o momentos erróneos|18 escenarios,54 valores; discrepancia<1e−7 con Nom 1e6|
|E2 paridad y límites|Contratos no equivalentes, σ absoluta confundida, división por cero|Caplet−floorlet=FRA; límites v→0 y T→0, nominal y strike par|
|E3 cuadratura y MC|FX extra o ausente, ajuste quanto incorrecto, rho auxiliar confundido|Cinco correlaciones en cuadratura;1e6 pares MC; medias dentro de5SE y en IC95 en ejemplo|
|Motor de hojas: cachés erróneas y normal|Conversión sin recálculo y función normal incompatible|Fixture de cachés −999; recálculo forzado entrega 4 y Φ(0)=0,5|
|E3 martingalas, paridades, límites|Signo de deriva o moneda incorrecta|E[M]=M0,E[N]=N0; σ=0, T=0, ρ=±1 y caso N constante; usual invariante a rd,ρ,σFX|

La prueba estocástica usa 5SE como umbral de regresión para evitar que un IC95 marginal se convierta en criterio de aceptación múltiple. Los IC95 se reportan como incertidumbre estadística del estimador, no de la dinámica ni de los supuestos.

## Hojas de cálculo

La auditoría integrada del commit `7bc599d` detectó que la conversión inicial con el perfil por defecto conservaba cachés auxiliares a cero: aquella evidencia de recálculo era insuficiente. Al provocar cálculo efectivo también apareció una incompatibilidad de `NORM.S.DIST` sin prefijo de función futura. Se retiró esa versión como entrega aceptada; el informe y la reproducción del fallo se conservan en `auditoria/REVISION_INTEGRADA_7bc599d.md`.

La corrección usa la función compatible `NORMDIST(x,0,1,acumulada)` y un perfil aislado con `OOXMLRecalcMode=0`, que fuerza recálculo completo al abrir antes de exportar los tres libros. Un fixture comienza con cachés deliberadamente erróneas de −999 y verifica que se transforman en 4 para `A1^2` y 0,5 para Φ(0). El verificador ampliado rechaza correctamente la entrega anterior en Arbol0!P3 (0 frente a 0,5 esperado); esa regresión está registrada en `resultados/cache_obsoleta_rechazada.log`.

Se generaron tres libros .xlsx sin macros ni enlaces externos y se **recalcularon realmente** mediante LibreOffice con ese perfil forzado, usando otro directorio para no sobrescribir la entrada antes del cotejo. El generador contiene fórmulas visibles; las cifras Python auxiliares no constituyen su único cálculo.

`python -m soluciones.src.verifica_hojas` vuelve a leer los valores guardados por el motor ofimático y coteja los **46.868 estados** de Arbol0 y Arbol15: spots, europea, bermuda, americana, mejorada, política, masa viva y absorbida, delta/cash y continuación BS; comprueba además las 14 fechas agregadas de probabilidades y todos los auxiliares numéricos de E2/E3. Máxima diferencia entre valores de nodo y Python: **6,14e−12**; tolerancia 1e−9. Los residuos locales/de presupuesto de la hoja son<1e−10. Hay más de 900.000 celdas no vacías en E1. Se escanean todos los libros para detectar errores de fórmula: ninguno. Precios E2 y E3 coinciden con Python a menos de 1e−7, con errores observados menores de 5e−12. Evidencia exacta en `resultados/hojas_verificadas.json`.

El recálculo ejecuta fórmulas equivalentes en otro motor; es control de implementación, no una validación financiera independiente. La independencia financiera procede de convolución/distribución, cuadratura, réplica, límites y revisión externa al implementador.

## Documentación y PDF

`python scripts/validate_knowledge_base.py` verifica hashes de raw, catálogo y enlaces. `python scripts/review_readiness.py` coteja fórmulas/familias originales, nombres, hojas, OCR y alcance documental. Se guardan sus salidas completas. No se ejecuta `--archives-dir`: los ZIP adjuntos originales no están en este checkout; sí están los 59 documentos finales y sus hashes.

El PDF se compila con Pandoc y XeLaTeX desde MEMORIA.md. Se inspeccionan todas las páginas renderizadas y sus ecuaciones/tablas; se corrigen desbordamientos y el símbolo «ñ» dentro de una unidad matemática. Se comprueban también límites de bloques de texto para detectar recortes laterales. Las gráficas se generan con Matplotlib y sus datos son los JSON reproducibles.

## Revisión independiente

Otro agente, con contexto inicial limpio y lectura de fuentes, revisó matemáticas y código del commit `5c0e1df`. Registró PASS sin hallazgos materiales en ese alcance. Sus scripts y resultados se conservan en `auditoria/`: recursión escalar y propagación E1; PDE Crank–Nicolson distinta de la referencia FFT; integración directa de E2 en50 escenarios aleatorios; integral bidimensional de E3 en12 escenarios. La PDE independiente a dx=.0005 dio 9,113665366, compatible con la referencia de la memoria9,113667959. El dictamen integrado posterior identifica su revisión exacta en el mismo directorio.

## Límites reales

- La base365 con mesesm/12 es una convención explícita por falta de fecha civil inicial; no se presenta como calendario docente dado.
- JR finito y difusión de referencia son modelos distintos. La americana es mensual; la réplica perfecta corresponde al árbol puro. El suavizado no satisface por construcción la misma réplica terminal binaria.
- La normal ilimitada de E2 se resuelve formalmente; no define globalmente bonos positivos. No se ha truncado la distribución.
- E2/E3 numéricos son ejemplos ilustrativos. La cuadratura E3 limitada a±12 normales está validada en esos casos, no en todo parámetro concebible.
- Convergencia numérica de referencia y MC son evidencia, no garantías matemáticas de error global ni estimaciones históricas.
- Los nuevos XLSX sí se han recalculado; los libros de clase raw siguen intactos y sin recalcular ni ejecutar VBA.
- Los nombres del grupo y la entrega/defensa personal siguen a cargo del alumno. El extra independiente de cesta sigue opcional pendiente.

Versiones del sistema usadas: Python 3.12.14; Pandoc 3.1.11.1; LibreOfficeDev 26.8.0.0.alpha0 (recalculo documentado, sin errores en los casos cotejados); XeTeX de TeX Live 2025/dev. Las versiones Python se fijan en requirements.txt.

## Dictamen final de integración

**PASS sobre `92be7d90c6d1961e90e6a308eb9980accbd17156`**, sin hallazgos materiales abiertos: [informe independiente](auditoria/REVISION_INTEGRADA.md). La reproducción completa aislada pasa con 12 pruebas y la [perturbación de los tres libros](auditoria/perturbacion_92be7d9.json) demuestra cálculo efectivo tras editar spot E1, volatilidad E2 y correlación/FX E3. No se ha ejecutado Microsoft Excel; el motor efectivamente probado es LibreOffice con recálculo forzado. El PDF regenerado coincide visualmente en sus 18 páginas.

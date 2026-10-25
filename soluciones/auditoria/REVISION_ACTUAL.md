# Revisión de C-01 y navegación para estudio

**PASS en el alcance revisado.** Modo standard; sin errores materiales ni caminos de entrada rotos. Se puede continuar el cierre de la actualización y preparar el estudio desde las nuevas entradas. Este dictamen no sustituye la verificación de los entregables que el responsable está regenerando.

## Versión y alcance

Worktree de `/workspace/examen_valoraci-n_afi`, rama `solucion/mefc-2026`, sobre baseline `fb7270313c85bad6cf15f15a3ac4e3c669cdaac2`. Inspección del 25/10/2026, alrededor de 12:15–12:17 UTC. Se revisaron el cambio en `src/ejercicio2.py`, sus tests nuevos, precisiones de MEMORIA y las entradas AGENTS, README, GUIA_PARA_EL_AGENTE, DECISIONES, ESTADO, VALIDACION y AUDITORIA. El worktree estaba en actualización; no se atribuye este resultado a un commit final todavía inexistente.

No se modificaron archivos de entrega ni fuentes; no se ejecutó generación ni recálculo en el worktree compartido. Sólo se escribe este informe temporal.

## C-01: reproducción y cierre

Se cargó por `git show fb72703:soluciones/src/ejercicio2.py` la implementación anterior para reproducir el defecto:

|Caso|Antes|Worktree corregido|
|---|---|---|
|f=.03, K=.032, v=1e-10, δ=.5, Pu=.95, Nom=1e6|FRA=caplet=floorlet=0, sin advertencia|FRA=−964.2499762500007; caplet=0; floorlet=+964.2499762500007|
|f=K=.03, v=0, mismos δ/Pu/Nom|Tres NaN, con RuntimeWarning/IntegrationWarning|Tres ceros, sin advertencias|

La corrección preserva el contrato: trata explícitamente la distribución degenerada y divide los demás casos por el centro y las zonas ±8, además del strike. La unión de los paneles sigue siendo `(-∞,+∞)`; no se elimina ni renormaliza probabilidad. Las fórmulas cerradas no cambian.

Se ejecutó `python -m unittest soluciones.tests.test_ejercicio2 -v`: **5 tests pasan**. Incluyen 18 combinaciones ATM/ITM/OTM con varianzas 0, 1e-20, 1e-16, 1e-12, 1e-10 y 1e-8, finitud y advertencias como errores, además del rechazo de varianza negativa.

Como contraste independiente de las llamadas a `prices`, se usaron los momentos de media normal en ATM: `E[Z 1(Z>0)]=1/sqrt(2π)` y `E[Z² 1(Z>0)]=1/2`. FRA/caplet/floorlet coinciden a menos de 1e-9 u.m. para las cinco varianzas positivas anteriores. El valor del contraejemplo también coincide con la expansión directa del primer y segundo momento del FRA.

SHA-256 del código efectivamente probado: `11251380ab695dc87c8d15e37215c55687a012e131d13409623f4898dc8c2b1a`. Tests: `df4d89b2fef40da3baf33a851cfbd1cb91037f0c96bde4b516004c2442a03aaf`. Memoria inspeccionada al cierre: `79d2f641a818cd7b9add251aa2aef89d41390ce2e94b3ce0ac348d1efb549aae`; el último cambio durante la revisión sólo condensaba el párrafo de entrega personal.

## Recorrido de entrada para explicar sin recurrir al historial

Se siguió la ruta estructural desde AGENTS y la guía, tratando los informes anteriores como evidencia histórica y no como resolución o estado vigente:

|Duda de estudio|Resolución localizada|Decisión, fuente y límite localizados|
|---|---|---|
|E1b: por qué europea tras 15 días|MEMORIA, «Apartado b. Quince días y resultado económico»; Tree y hojas Calendario/Arbol/Resumen|DECISIONES E1-3/4/5; PDF-002 p.2 y teoría dirigida de árboles. Convención 15/365, reconstrucción fuera de malla y P&L por unidad explícitos.|
|E2: caplet y ajuste por pago anticipado|MEMORIA, contrato/numerario y «Momentos truncados y caplet»; prices/integrate y hoja Calculo|DECISIONES E2-1/2/3/4; PDF-008 pp.5–19 y PDF-009 pp.38–40. Factor multiplicativo, volatilidad absoluta, normal formal y C-01 quedan separados.|
|E3: quanto|MEMORIA, bloques (8) y (9), y desarrollo Itô previo; ejercicio3.py y hoja Calculo|DECISIONES E3-1/2/3; PPT-001 y teoría FX dirigida. Q EUR, FX EUR/USD, covariación y conversión fija frente a FX terminal explícitos.|

La guía identifica una sola memoria canónica, proporciona rutas hacia contrato, teoría, código y hojas, y evita que un PASS de otra versión sustituya al estado actual. La carpeta histórica queda fuera del recorrido inicial de aprendizaje. La nota sobre la rama vigente evita conectar por error `main`, que conserva la base anterior.

Se comprobaron **75 enlaces locales** de las entradas anteriores, sin roturas. Los dos validadores del repositorio pasan: 59 fuentes, 620 páginas PDF, 25 diapositivas, 60 hojas originales, 60.701 fórmulas, 797 nombres y 811 enlaces; sin errores ni huérfanos. Son controles documentales, no prueba de comprensión del alumno.

También se rehicieron las sensibilidades JR de MEMORIA E1b para 15/365 y 1/24, y el precio suavizado tras 15 días: coinciden con las cifras añadidas. La precisión de `L_T/L_t` en E2 es correcta para la valoración condicional. No se identifican errores materiales en estas precisiones.

## Límites y siguiente paso

Este es un recorrido simulado de navegación, no un test con un alumno ni con otro chat sin contexto. No se reaudita todo E1/E3 ni se reconstruyen en esta fase las sensibilidades de difusión de la revisión crítica. No se han inspeccionado los PDF/XLSX nuevos que seguían generándose, ni se ha repetido la ruta completa de entregables; ese cierre corresponde a la ejecución del responsable. Tampoco se afirma validación universal del integrador para cualquier parámetro concebible.

**Acciones necesarias dentro del alcance revisado: ninguna.** Tras terminar la generación en curso, fijar el commit final y actualizar ESTADO/evidencia para que la entrada describa la versión cerrada. Se preservan los límites metodológicos, históricos y de entrega personal ya documentados. No hay mejoras cosméticas que condicionen el resultado.

## Fijación posterior del cierre

El código y los tests revisados se guardaron en `23aa1b3aba425fd265b97135d82d8bb53c14f5d7`. Después sólo se retiró del final de la memoria un párrafo administrativo redundante (presente en README/DEFENSA/ESTADO) para evitar una página final casi vacía; no cambió la resolución matemática. El responsable regeneró y revisó PDF y XLSX. Esta precisión no amplía el alcance de la revisión independiente a esos binarios.

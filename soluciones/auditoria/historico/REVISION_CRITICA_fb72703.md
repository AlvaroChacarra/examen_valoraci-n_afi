---
title: "Revisión crítica de Valoración MEFC 2026"
subtitle: "Contraste del contrato, decisiones metodológicas y resultados"
date: "25 de octubre de 2026"
lang: es
geometry: margin=23mm
fontsize: 11pt
colorlinks: true
---

# Dictamen

**PASS WITH CONDITIONS — utilizable con una corrección acotada en la verificación auxiliar.** Modo: `standard`, con sensibilidad focalizada. Conformidad: `SUBSTANTIAL` por el defecto descrito a continuación; el núcleo de valoración y los resultados entregados satisfacen el contrato revisado. Confianza: **HIGH** para esos resultados y para la reproducción del hallazgo.

No he encontrado errores en las fórmulas teóricas ni en las primas entregadas para los datos del encargo y las convenciones declaradas. Sí he encontrado **un fallo numérico silencioso en el integrador auxiliar del ejercicio 2**: cerca de volatilidad cero puede devolver valores falsos aun cuando las fórmulas cerradas y las hojas calculan correctamente. Por ello no considero justificado afirmar que toda la implementación y su verificación están perfectamente cerradas.

Se puede confiar en los resultados actuales del trabajo dentro de su alcance documentado. Antes de declarar completa la herramienta de verificación para los límites solicitados, debe cerrarse el hallazgo C-01. No hay BLOCKER ni HIGH relativos a las primas o derivaciones presentadas.

Versión auditada: **`fb7270313c85bad6cf15f15a3ac4e3c669cdaac2`**, rama `solucion/mefc-2026`; sus artefactos técnicos corresponden a `92be7d9`. El repositorio se mantuvo intacto durante esta auditoría. La reproducción completa se ejecutó en una copia aislada de la revisión exacta. Los scripts y evidencias de esta pasada se conservan junto a este informe, fuera de la entrega.

Esta es una revisión crítica nueva del trabajo elaborado por el mismo agente; **no constituye una segunda auditoría externa independiente**. Para reducir el sesgo de confirmación se congelaron primero los requisitos desde los originales y la petición del usuario, se emplearon cálculos nuevos y se volvieron a ejecutar los controles. Los dictámenes previos no se utilizaron como prueba suficiente de corrección.

# Hallazgo material C-01

**Severidad: MEDIUM. Estado: abierto; no corregido en esta auditoría.**

**Problema.** `soluciones/src/ejercicio2.py:23–33`, en particular la partición de integración de la línea 32. La función `integrate` integra respecto de una normal estándar separando únicamente en $a=(K-f)/s$. Cuando $s$ es pequeño y $f\ne K$, ese punto puede quedar a cientos o miles de desviaciones de cero. La cuadratura adaptativa sobre un intervalo semiinfinito desplazado puede no muestrear la zona que contiene la masa gaussiana y aceptar el resultado cero sin advertencias. Tampoco existe una rama explícita para varianza nula: con $f=K$ se produce $0/0$ y resultados `NaN`.

**Reproducción ejecutada.** Este es un caso de prueba de baja volatilidad, no un dato del enunciado:

```python
from soluciones.src.ejercicio2 import integrate, prices
args = dict(f=0.03, k=0.032, variance=1e-10,
            delta=0.5, p_u=0.95, nominal=1_000_000)
integrate(**args)  # fra=0.0, caplet=0.0, floorlet=0.0
prices(**args)
# fra=-964.2499762500007, caplet≈0, floorlet=964.2499762500007
```

Una cuadratura adicional, dividida alrededor del centro de la normal, reproduce $-964{,}2499762500009$ y $+964{,}2499762500009$. La hoja E2 editada con los mismos inputs y recalculada efectivamente también produce esos valores correctos. No es un desacuerdo entre modelos ni el efecto de la cola incompatible con bonos positivos: es pérdida numérica de la masa de integración.

Con `f=k=0.03` y `variance=0`, `integrate` devuelve `NaN` para los tres contratos; el valor correcto es cero. Evidencia resumida en `hallazgo_integrador_e2.json` y `hoja_e2_baja_volatilidad.json`.

**Impacto.** El fallo no altera los resultados numéricos de la entrega ni las fórmulas cerradas. Sí vuelve inadecuado ese integrador como comprobación general de los límites y puede generar falsos desacuerdos o una falsa verificación si se comparan entre sí varios ceros incorrectos. La suite actual pasa porque `test_ejercicio2.py:5–11` contrasta cuadratura sólo a volatilidades 0,003 y 0,02; `:13–18` comprueba el límite únicamente con `prices`, sin aplicar `integrate` cerca de él.

**Corrección mínima recomendada.** Añadir tratamiento explícito de varianza cero, comprobar finitud y estabilizar la cuadratura conservando paneles alrededor de la masa normal —además del punto de strike— y un tratamiento justificado de las colas. No modificar el payoff ni truncar silenciosamente la distribución económica. Es una reparación local del cálculo numérico; no requiere rehacer el modelo ni cambiar las primas del trabajo.

**Prueba de cierre.** Reproducir el caso anterior con error menor de $10^{-7}$ u.m.; probar varianza cero ATM/ITM/OTM sin warnings ni `NaN`; contrastar varianzas pequeñas positivas y continuidad del límite mediante una integración independiente estable. Mantener aprobados los controles existentes y las hojas. La auditoría no implementa esta corrección. Se crearon dos regresiones nuevas fuera del repositorio; ambas fallan sobre la versión auditada, tal como documenta `regresiones_nuevas_fallan.log`. Este fallo esperado es evidencia del defecto, no un cambio de la suite entregada.

# Challenge de las decisiones del ejercicio 1

## Estados, modelo y réplica

Se construyó un segundo valorador sin importar el pricer principal: usa una retícula de ruido entero, aprovechando las amplitudes proporcionales a 75, 85 y 78, y fusiona coincidencias que la representación original conserva como tuplas distintas. La distribución de estados y el modo de localizar hijos son distintos; ambos preservan las fechas contractuales. El intervalo residual de los 15 días se mantiene como componente separada.

Reproduce las seis primas iniciales y posteriores a 15 días con error máximo $8{,}9\cdot10^{-15}$ u.m. La representación original es redundante en algunos precios, pero es válida y computacionalmente viable; no es necesario imponer un árbol triangular global.

Una simulación nueva de réplica, con actualización escalar del spot, cuenta y posiciones, detiene cada camino al primer ejercicio o expiración. Para 5.000 caminos y semilla 60131025, el error máximo es $1{,}07\cdot10^{-13}$ y el residuo autofinanciado $7{,}11\cdot10^{-15}$, frente a tolerancia $10^{-10}$. La propagación por diccionarios reproduce primera parada en mes 12 de 1,9287109375% y en mes 36 de 6,0647827864%, además de la supervivencia al vencimiento de 49,2730027647%.

Estos resultados certifican la réplica en el árbol puro; no la extrapolan a una difusión ni al último intervalo sustituido por Black–Scholes.

## Quince días: base temporal y elección económica

Se interrogó si la preferencia por la europea era un efecto de la base elegida. Se repitió con 15/365, 15/366 y medio mes de 1/24 años, manteniendo los tiempos contractuales originales.

|Convención|P&L financiado europea|Bermuda|Americana de malla|
|---|---:|---:|---:|
|15/365|−0,754216|−0,780076|−0,785670|
|1/24|−0,754601|−0,780606|−0,786203|
|15/366|−0,754141|−0,779972|−0,785565|

En todos los casos conviene la europea por unidad de contrato, también al comparar resultado sobre prima inicial. La elección de base no cambia esta conclusión.

Se contrastó además con la difusión de volatilidad por tramos, conservando las mismas fechas de ejercicio. A paso espacial 0,00025, los P&L son −0,725582, −0,751421 y −0,757313. La preferencia por la europea tampoco depende de mantener el ruido binomial del paso mensual.

## Matiz para la defensa: revalorar fuera de la malla

La memoria declara que reconstruye el árbol en el día 15, conservando las fechas y usando JR en el intervalo residual (`MEMORIA.md:77`). Es una convención de revaloración defendible. Conviene explicar que un árbol definido sólo en las fechas mensuales no determina por sí mismo un precio único entre ellas: dividir un paso JR en dos pasos JR no conserva su distribución terminal, aunque ambos esquemas satisfagan la martingala.

Como contraste conceptual, mantener los dos extremos originales del primer mes y valorar en el día 15 su cartera delta/cash produce precios 8,246070, 8,462383 y 8,491403. No es el mismo supuesto que imponer una nueva transición JR con volatilidad residual constante; no debe presentarse como una segunda solución idéntica en datos dinámicos. La comparación sirve para identificar qué elección añade la reconstrucción, no para sustituirla sin justificación. También en ese puente la europea registra la menor pérdida.

**Conclusión:** la decisión económica es robusta en los contrastes realizados, pero las primas posteriores a 15 días son condicionales a la convención de reconstrucción declarada. No corresponde defenderlas como un condicionamiento exacto y único del árbol original entre fechas.

## La mejora Black–Scholes es local al escenario estudiado

Se revisó el criterio de precisión sin aceptar que un precio más bajo fuese automáticamente mejor. La referencia por convolución mantiene las 14 fechas de parada. Se volvió a ejecutar la PDE Crank–Nicolson del contraste independiente existente, inspeccionando antes su código: a paso 0,0005 obtiene 9,113665366, frente a 9,113667959 por convolución. Esa diferencia de unos $2{,}6\cdot10^{-6}$ es muy inferior al margen entre los errores comparados.

|Escenario|JR puro|JR con BS final|Referencia difusión|Error puro|Error con BS|
|---|---:|---:|---:|---:|---:|
|Inicial|9,16290759|9,13920110|9,11366796|0,04923963|0,02553314|
|15 días, spot 52,5|8,39074302|8,39647757|8,37011514|0,02062788|0,02636243|

La mejora de aproximadamente 48,15% se sostiene en el escenario inicial solicitado para el apartado d. En el escenario posterior el error aumenta aproximadamente 27,8%. No es un fallo del apartado d ni contradice la memoria, que limita expresamente la afirmación al contrato y escenario estudiados. Es una advertencia relevante para defender que la técnica no garantiza mejorar en toda revaloración.

# Challenge del ejercicio 2

Se rehicieron las relaciones de numerario y pago, los momentos normales y la paridad, y se contrastaron 36 escenarios nuevos de tipos, strikes, devengos y volatilidad. Se integró directamente el payoff ponderado, sin usar los momentos de la fórmula cerrada. En esos escenarios, alejados del problema de partición descrito en C-01, el error máximo observado fue $5{,}82\cdot10^{-11}$ u.m. con nominal de un millón.

El factor $(1+\delta F_T)$ es multiplicativo por el pago en $T$, no un denominador de liquidación. Los momentos del FRA y del caplet de la memoria son correctos. También se contrastó si bastaría introducir el forward ajustado en Bachelier: en el ejemplo de la memoria eso da 2.232,711530 frente a 2.232,647690 de la fórmula correcta, una diferencia de 0,063840. Ajustar la media no transforma la distribución ponderada en otra normal exacta; la solución actual evita ese error.

La normal ilimitada y la identidad de bonos positivos siguen siendo globalmente incompatibles. Un stress artificial, expresamente ajeno a los datos docentes, con $f=0{,}03$, $s=0{,}8$, $\delta=0{,}5$ y strike −2,5 produce un floorlet formal negativo. Esto confirma la limitación de modelo ya declarada, no un defecto nuevo que deba «repararse» truncando la normal en secreto.

**Precisión notacional aconsejable.** En `MEMORIA.md:181–184`, para un tiempo de valoración general $t>0$, el cociente escrito debe entenderse como incremento condicional $L_T/L_t$ de la densidad; la densidad absoluta con origen cero se normaliza por $1+\delta F_0$. La valoración condicional usada es correcta. Sería más preciso escribir esa distinción; no cambia ninguna fórmula de precio ni resultado numérico. Su carácter es editorial y no bloqueante, además de estar bajo la cautela de aproximación formal.

# Challenge del ejercicio 3

Se reconstruyó la distribución desde las martingalas $M,N$ y su correlación auxiliar, en vez de simular directamente $S,FX$ como hace el pricer. Condicionando en el browniano de $M$, se integró la innovación residual de $N/M$ y luego el flujo en EUR. Esta vía cambia tanto la variable condicionante como el modo de incorporar la conversión FX.

En 24 escenarios nuevos, incluidos correlaciones −1 y +1, tipos domésticos/foráneos positivos y negativos, dividendos y distintos vencimientos, los seis flujos de control —los cuatro contratos pedidos y las puts de paridad— coinciden con error máximo $9{,}24\cdot10^{-14}$ EUR. La transformación auxiliar reproduce la varianza de $S$ y su covarianza observable.

Las condiciones de martingala confirman $\mu_{FX}=r_d-r_f$ y $\mu_S=r_f-q-\rho\sigma_S\sigma_{FX}$. El signo negativo quanto es correcto para EUR por USD. La correlación de $M,N$ no se confunde con la de los observables. Los pagos quanto usan conversión fija y los usuales FX terminal.

Se tomó literalmente el signo impreso en el $d$ de diapositiva 25: en el ejemplo ilustrativo produciría una call de 11,002696 frente a 11,311997 de la expresión correcta. La corrección notacional de la memoria es necesaria y está bien justificada por la derivación y valoración en USD; no es una alteración arbitraria de la plantilla.

# Reproducción y cobertura

Se ejecutó nuevamente `python -m soluciones.src.reproduce --deliverables` desde una copia aislada del commit exacto: terminó correctamente. Pasan las 12 pruebas existentes, el fixture que comienza con cachés deliberadamente falsas y el recálculo completo de los tres libros. Se cotejan 46.868 estados, 14 probabilidades y 33 auxiliares numéricos de E2/E3. Pasan también los dos validadores documentales, con 59 fuentes intactas y sin enlaces rotos ni huérfanos.

Esto acredita la ruta entregada; **no invalida el nuevo hallazgo sólo porque todas las pruebas existentes pasen**. El caso que lo reproduce no estaba en la suite. El PDF regenerado tiene 18 páginas, sin bloques detectados fuera de los márgenes; sus renders se contrastan con los del PDF entregado.

|Requisito|Resultado de esta pasada|
|---|---|
|E1 modelo, calendario y tres precios|Implementado y reproducido con representación alternativa|
|E1 revaloración y P&L|Implementado; conclusión robusta, con convención fuera de malla explícita|
|E1 réplica y primeras paradas|Implementado; comprobación nueva por camino y masa|
|E1 suavizado y referencia|Implementado; mejora demostrada en el escenario inicial|
|E2 fórmulas y pagos|Correctos; integrador auxiliar incompleto en baja volatilidad y varianza cero|
|E3 bloques (1)–(10), incluida call usual|Implementados y contrastados desde las martingalas|
|Hojas y reproducción|Recálculo real y controles aprobados en la copia aislada|
|Defensa/entrega|Guía conforme; nombres y proceso individual siguen a cargo del alumno|
|Cesta +1|Diferida explícitamente; fuera de esta auditoría|

# Límites de esta revisión y siguiente paso mínimo

No se ha ejecutado Microsoft Excel: el motor probado es LibreOffice. No se verifican operaciones en campus, Zoom ni correo, ni el extra de cesta excluido. No se garantiza comportamiento de todas las funciones auxiliares para parámetros arbitrarios; C-01 demuestra una limitación concreta que debe cerrarse. La inspección mecánica de márgenes no sustituye la lectura visual de ecuaciones y tablas. Tampoco se afirma independencia externa de esta nueva revisión.

El requisito técnico antes de dar por cerrada toda la verificación es **corregir C-01 y añadir sus regresiones**. No es necesario recalcular o cambiar los resultados principales del trabajo por ese hallazgo. Las precisiones sobre reconstrucción fuera de malla y densidad condicional ayudarían a defender las decisiones con más rigor; no requieren rediseñar los ejercicios.

La entrega original no ha sido modificada. Este informe expresa un juicio condicionado y falsable, con una reproducción concreta del defecto; no una garantía de perfección absoluta.

# Evidencia y comandos

Con el repositorio en el commit auditado y las dependencias de `soluciones/requirements.txt`:

```bash
python -m unittest discover -s soluciones/tests -v
# En copia o worktree aislado para preservar los binarios entregados:
python -m soluciones.src.reproduce --deliverables
python scripts/validate_knowledge_base.py
python scripts/review_readiness.py
```

Scripts nuevos junto a este informe:

- `contraste_arbol_y_replica.py`
- `challenge_calendario.py`
- `challenge_formulas.py`
- `test_hallazgo_e2.py`

Los tres primeros guardan sus resultados en JSON. Se pueden ejecutar con Python y la variable opcional `MEFC_REPO` apuntando al checkout que se quiera comprobar; por defecto usan el workspace de esta revisión. El cuarto contiene las dos regresiones que deben pasar tras corregir C-01 y que fallan en la versión auditada.

`hallazgo_integrador_e2.json` contiene el contraejemplo y la cuadratura estable adicional. `hoja_e2_baja_volatilidad.json` registra el control del mismo caso en hoja. El script PDE ya versionado se volvió a ejecutar con:

```bash
python soluciones/auditoria/contraste_independiente_e1.py \
  --output /ruta/a/pde_y_arbol_previo_repetidos.json
```

Su etiqueta interna de commit conserva el origen histórico del script; en esta pasada se ejecutó el archivo presente en `fb72703`, tras leer su lógica. La revisión no se apoya en su dictamen anterior.

# Decisiones metodológicas vigentes

La resolución y sus demostraciones se mantienen sólo en [MEMORIA](MEMORIA.md). Este registro conserva por qué elegimos cada alternativa y qué se puede afirmar. Para saber dónde estudiar cada pieza, usar [GUIA_PARA_EL_AGENTE](GUIA_PARA_EL_AGENTE.md).

|ID|Decisión y razón|Alternativa considerada / consecuencia|Evidencia y límite|
|---|---|---|---|
|E1-1|JR exacto del curso: p=.5 y normalización cosh|El JR con deriva r−σ²/2 sólo satisface aproximadamente la martingala a paso finito|PDF-003pp24–25; test de martingala|
|E1-2|Conteos de subidas por amplitud anual|Un único conteo de subidas no conserva precios entre volatilidades distintas; una malla uniforme de varianza movería fechas|36meses y14fechas; estados redundantes por coincidencias son válidos|
|E1-3|15/365 y fechas j/12 originales|No hay fecha civil inicial para construir meses reales; medio mes1/24 es sensibilidad, no el dato adoptado|La preferencia por europea se mantiene con ambas bases|
|E1-4|Reconstruir JR en el intervalo residual|El árbol mensual no fija un precio único entre fechas; no es un semigrupo exacto al partir pasos|Memoria E1b; no llamarlo condicionamiento único del árbol original|
|E1-5|Comparar una opción de cada tipo con coste financiado|Comparar nuevas primas ignora el precio pagado; otras exposiciones podrían requerir otra comparación|También se calcula resultado sobre prima inicial; conclusión local al escenario|
|E1-6|Simular las mismas ramas valoradas y absorber primera parada positiva|Un hedge mensual de una difusión diferente tendría error; ITM no basta para ejercicio temprano|Réplica y MC/exacta en src/ejercicio1.py; empates continúan|
|E1-7|BS final con max(intrínseco,continuación),36intervalos|Refinar una referencia no sustituye la valoración mensual solicitada; BS cambia la última transición|Mejora inicial≈48,15%; en escenario15d empeora≈27,8%; no promesa universal|
|E2-1|Bono U y factor multiplicativo1+δF_T por pagoT|Descontar en T bajo Q^U sin cambiar distribución es incorrecto; no introducir otro contrato de liquidación|PDF-002p3,PDF-008pp14–19; densidad condicional L_T/L_t|
|E2-2|Momentos normales con varianza integrada determinista|Momentos lognormales no son intercambiables; ajustar sólo la media no da la call exacta|Derivación de momentos completos/truncados y cuadratura|
|E2-3|Normal formal sin cota; declarar inconsistencia global|Truncar o desplazar silenciosamente cambiaría el encargo|1+δF debe ser positivo para bonos, pero la normal ilimitada no lo garantiza|
|E2-4|Cuadratura centrada y rama de varianza cero|Partir sólo por el strike puede perder masa gaussiana y devolver cero falso|C-01 reproducido y corregido; colas infinitas y regresiones de baja varianza|
|E3-1|Q EUR, FX EUR/USD y retorno total con q|Invertir FX exige transformar derivas y correlaciones; no cambiar sólo el nombre|PPTdiap3–17; Itô de SX y N/M|
|E3-2|Transformar parámetros auxiliares M,N a observables|N incorpora acción y FX: no identificar las dos correlaciones|Covarianzas y condiciones de martingala fijan signo quanto negativo|
|E3-3|Quanto con λ=1 fijo, usual con FX_T|Multiplicar el quanto de nuevo por FX es otro contrato|Unidades de los cuatro pagos; réplica/paridades/integración|
|E3-4|Corregir signo rUSD en d de diap25 y t/T terminal|Copiar literalmente el signo impreso contradice la call USD y el desarrollo|Corrección explicitada, contrastada visualmente; callusual adicional incluida|
|ENT-1|Hojas con fórmulas y recálculo forzado|Convertir XLSX puede conservar cachés; coincidencia de precios precargados no prueba cálculo|OOXMLRecalcMode=0, fixture de cachés falsas y cotejo de auxiliares/masas|
|ENT-2|E2/E3 numéricos sólo ilustrativos|No existen juegos de datos numéricos completos en esos enunciados|No presentar ejemplos propios como inputs docentes|
|ENT-3|Archivar auditorías viejas; conservar fuentes|Borrar evidencia de defectos impediría trazar correcciones; usarla como estado actual confundiría|VALIDACION es actual; auditoria/historico tiene versiones y fallos anteriores|

No se ha hecho merge a main, entrega en campus ni envío de correos. Extra de cesta+1 explícitamente diferido; callusual+0,5 incluida. Las decisiones se cambian sólo con una justificación y actualización proporcional de memoria, código, hojas y controles.

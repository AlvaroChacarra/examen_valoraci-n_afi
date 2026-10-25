# Explicar esta resolución a Álvaro

La resolución vigente está integrada en la rama `main` del repositorio. Usar main al conectar el repositorio al siguiente chat.

Este repositorio contiene la resolución y la teoría de apoyo. La sesión de aprendizaje se hará después: este documento permite que otro chat la prepare sin conocer el historial. No es necesario rehacer el trabajo para empezar a explicar una duda.

## Qué abrir primero

|Necesidad del alumno|Ruta canónica|
|---|---|
|Dónde está la resolución completa|[MEMORIA.md](MEMORIA.md) y [PDF](MEMORIA.pdf)|
|Ver números y fórmulas editables|[E1.xlsx](hojas/Ejercicio1.xlsx), [E2.xlsx](hojas/Ejercicio2.xlsx), [E3.xlsx](hojas/Ejercicio3.xlsx); empezar por LEEME|
|Por qué se eligió cada método|[DECISIONES.md](DECISIONES.md)|
|Qué se comprobó y qué limitaciones quedan|[VALIDACION.md](VALIDACION.md)|
|Ejecutar o cambiar el código|[README.md](README.md), luego src/ejercicio1.py, ejercicio2.py o ejercicio3.py|
|Qué exigía literalmente la entrega|[MATRIZ_CUMPLIMIENTO.md](MATRIZ_CUMPLIMIENTO.md); contrastar originales PDF-002/PPT-001|
|Preparar preguntas de defensa|[DEFENSA.md](DEFENSA.md)|
|Situación vigente|[ESTADO.md](ESTADO.md)|

La memoria es la **única solución canónica**. Esta guía es un mapa pedagógico, DECISIONES conserva motivos y alternativas, y knowledge-base conserva fuentes docentes. `auditoria/historico/` acredita revisiones anteriores: no empezar por allí ni convertir un PASS histórico en el estado actual.

## Cómo responder a una duda

1. Identificar ejercicio y apartado. Si la pregunta es concreta, responder directamente con su referencia; no imponer un curso entero.
2. Separar lo que dice el enunciado, la convención que adoptamos y lo que hemos derivado.
3. Explicar primero el significado económico; después definir símbolos y unidades y reconstruir la ecuación necesaria. No saltar desde el nombre de un modelo a la fórmula final.
4. Conectar esa ecuación con una función o celdas concretas. Para E1 mostrar un nodo con sus dos sucesores; para E2 un flujo y numerario; para E3 el pago con su moneda.
5. Cerrar con un control: martingala, paridad, límite o réplica. Preguntar algo corto que revele comprensión si el alumno quiere estudiar paso a paso.

No usar como prueba de comprensión el hecho de que el código pase tests. No exigir que Álvaro sepa programar para entender las matemáticas. Los ejemplos propios deben rotularse como ilustrativos, sin atribuirlos al enunciado. No confundir precisión de redondeo del árbol con exactitud económica universal.

## Ejercicio 1: recorrido para entenderlo

**Resolución:** MEMORIA, sección «Ejercicio 1», desde contrato hasta apartado d. **Implementación:** `src/ejercicio1.py`: `Tree` construye estados y retrocede, `exact_exercise` absorbe probabilidad y `simulate` mantiene riqueza. **Hoja:** Entradas → Calendario0/15 → Arbol0/15 → Resumen; Probabilidades y Simulacion permiten seguir el ejercicio y la réplica.

Orden sugerido:

1. Qué compra una put; diferencia entre ejercicio europeo, bermuda y americano de malla. Escribir las 14 fechas antes de calcular.
2. Numerario bancario, probabilidad Q y condición de martingala. Derivar u,d desde p=1/2 y desviación logarítmica σ√h. Explicar el cosh del JR exacto.
3. Recombinar dentro de bloques sin confundir número total de subidas con estado suficiente. Reconstruir un precio con los conteos por año.
4. Valor de continuar frente a ejercicio inmediato: retroceder un nodo y justificar el orden de primas.
5. Revaloración a 15 días: conservar fechas, acortar el primer intervalo y comparar P&L, no primas finales. Distinguir reconstrucción de un condicionamiento único fuera de malla.
6. Resolver dos ecuaciones para delta/cash. Rebalancear sin aportación de capital y liquidar al primer ejercicio.
7. Primera parada frente a estar ITM; probabilidad bajo Q frente a histórica; incondicional frente a dada supervivencia. Entender qué mide un IC Monte Carlo.
8. Suavizar sólo la continuación final con BS. Comparar con difusión de mismas fechas, sin convertir la referencia en la solución pedida ni extender la réplica binaria al esquema híbrido.

**Teoría docente dirigida:** [árboles](../knowledge-base/conceptos/arboles.md); PDF-003 pp.24–25 (calibración), 34–39 (retroceso), 45–51 (ejercicio), 54–60 (réplica), 74–83 (volatilidad). PDF-006 pp.51–53 (BS final). IDs y originales en [catálogo](../knowledge-base/CATALOGO.md).

**Puntos que deben poder defenderse:** por qué no usamos una malla uniforme en varianza; por qué una opción más cara puede dar peor P&L; por qué payoff cero no se cuenta como ejercicio; por qué la americana es discreta; por qué el suavizado mejora inicialmente pero puede empeorar tras el movimiento de spot.

## Ejercicio 2: recorrido para entenderlo

**Resolución:** MEMORIA, sección «Ejercicio 2». **Implementación:** `src/ejercicio2.py`, `prices` y `integrate`. **Hoja:** Calculo, desde f/K/devengo hasta momentos y paridad. Los números son ilustrativos: el enunciado pide fórmulas generales.

1. Dibujar t, fixing T y U=T+δ. Los dos contratos pagan en T; no añadir el denominador de otro FRA de liquidación.
2. Identidad de una curva: 1+δF_t=P(t,T)/P(t,U). Elegir el bono U como numerario y demostrar por qué el pago anticipado incorpora un factor **multiplicativo** dentro de la esperanza.
3. Normal absoluta: F_T=f+sZ, v=s²=integral σ_n². Diferenciar 100 puntos básicos de volatilidad absoluta de una volatilidad relativa del 1%.
4. Expandir el payoff del FRA usando E[F] y E[F²]. Interpretar el ajuste positivo del strike par.
5. Integrar φ, zφ y z²φ sobre el umbral de ejercicio; obtener el caplet. No copiar momentos lognormales ni sustituir sólo el forward ajustado dentro de Bachelier.
6. Reconstruir floorlet y paridad para idéntica fecha de pago. Entender los límites v→0 y T→t.
7. Explicar la incompatibilidad global entre normal ilimitada y bonos positivos; resolver la aproximación docente sin modificar su distribución.

**Teoría dirigida:** [tipos](../knowledge-base/conceptos/tipos.md) y [normal/multicurva](../knowledge-base/conceptos/normal-multicurva.md). PDF-008 pp.5–19 para numerario y pago; PDF-009 pp.38–40 para normal. El desarrollo lognormal del curso es una referencia metodológica, no la respuesta normal.

**Punto numérico importante:** la cuadratura divide también alrededor del centro normal y conserva colas infinitas. Un strike remoto no permite al algoritmo omitir la masa de probabilidad. La varianza cero tiene rama explícita; véase la regresión C-01 en VALIDACION.

## Ejercicio 3: recorrido para entenderlo

**Resolución:** MEMORIA, sección «Ejercicio 3», bloques (1)–(10), incluida call usual +0,5. **Implementación:** `src/ejercicio3.py`. **Hoja:** Calculo; Contrastes contiene evidencia Python ilustrativa.

1. Unidades: S en USD/acción, X=FX en EUR/USD. Escribir los cuatro pagos y separar conversión terminal de conversión fija quanto λ=1.
2. Retorno total con dividendos reinvertidos. Definir M y N como inversiones descontadas por cuenta EUR; por qué ambas deben ser martingalas bajo Q EUR.
3. Resolver sus exponenciales y despejar X y S=N/M por factores deterministas.
4. Derivar volatilidades/correlaciones: N contiene ruido tanto de S como de X; ρ_MN no es ρ_SX.
5. Aplicar Itô a X, SX y N/M, conservando covariaciones. El signo quanto se deduce de deriva cero, no se memoriza.
6. Distribución conjunta terminal; diferenciar correlación de brownianos/logaritmos de correlación de niveles lognormales.
7. Forward usual por esperanza y réplica USD convertida al spot; forward quanto por su pago ya en EUR.
8. Integrar la call quanto y después la call usual: el peso X_T inclina la normal conjunta y cancela el ajuste quanto en el contrato usual.
9. Revisar paridades, volatilidades nulas y vencimiento cero. Justificar la corrección del signo de rUSD en d de diap.25.

**Teoría dirigida:** [FX/quanto](../knowledge-base/conceptos/fx-quanto.md); PDF-007 pp.12–23 (numerario/Itô/réplica) y PDF-010 pp.4–11 (unidades/FX). PPT-001 completo es vinculante. El quanto del propio FX de una hoja de clase no sustituye la covariación acción-FX del trabajo.

## Notación mínima a vigilar

|Símbolo|Significado y cuidado|
|---|---|
|Q|Medida de valoración según numerario; no probabilidad histórica|
|h,δ,T|h es paso E1; δ devengo E2; T vencimiento/fixing según contrato|
|B,Δ|Saldo monetario y unidades de acción en la réplica E1|
|f,F_t,v|Forward observado hoy, proceso forward y varianza normal integrada E2|
|M,N|Martingalas auxiliares E3; N no es nominal ni normal estándar|
|X,λ|FX terminal aleatorio frente a conversión quanto fija|
|r_d,r_f,q|Tipo EUR, tipo USD y dividendos continuos E3|

## Un inicio útil para el siguiente chat

«Usa la rama main de AlvaroChacarra/examen_valoraci-n_afi. Lee AGENTS.md y soluciones/GUIA_PARA_EL_AGENTE.md. Quiero entender el ejercicio [n], apartado [x]. Usa la memoria canónica, distingue enunciado, supuestos y derivación; explícame el mecanismo y reconstruye las cuentas conmigo, consultando sólo la teoría necesaria.»

Si falta una fuente real, indicarlo. No inventar datos, resultados ni una aprobación de entrega; completar nombres y realizar la defensa sigue correspondiendo al alumno.

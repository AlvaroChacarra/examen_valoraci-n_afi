---
title: "Valoración MEFC 2026"
subtitle: "Resolución reproducible de los ejercicios 1, 2 y 3"
author: "Entrega de trabajo — nombres de integrantes por completar"
date: "24 de octubre de 2026"
lang: es
geometry: margin=23mm
fontsize: 11pt
colorlinks: true
---

# Alcance, fuentes y lectura

Esta memoria contiene **derivaciones y cálculos nuevos**, no soluciones docentes transcritas. La autoridad contractual es PDF-002, *Valoración MEFC 2026*, pp.1–4; el desarrollo de E3 corresponde a las 25 diapositivas de PPT-001; PDF-001 fija entrega y defensa. Los originales están intactos en `raw/encargo/`. Las referencias a páginas son físicas del PDF. Las fichas de `knowledge-base/` son interpretación documental, no una fuente sustitutiva ni resultados recalculados.

Se han leído completos los tres documentos vinculantes y sus extracciones. Se han inspeccionado los originales renderizados, especialmente las ecuaciones de PPT-001 y PDF-003 pp.24–25 y la mejora de PDF-006 pp.51–53. El extra de cesta de +1 punto (PDF-002 p.4) queda opcional pendiente; sí se incluye la call usual de +0,5 de PPT-001 diap.25. E2 y E3 son encargos teóricos sin un juego de parámetros numéricos; sus ejemplos de control están rotulados como ilustrativos.

La matriz de cumplimiento está en `MATRIZ_CUMPLIMIENTO.md`. El código de referencia está en `src/`, las evidencias en `resultados/` y las hojas identificadas por ejercicio en `hojas/`. La memoria es el documento canónico; los JSON conservan más decimales que las tablas. Para defender la solución conviene reconstruir primero cada contrato, elegir su numerario y, sólo después, aplicar su fórmula.

# Ejercicio 1. Put bermuda mensual

## Contrato, significado y convenciones

PDF-002 p.2 pide valorar el derecho a vender por $K=45$ un activo inicialmente a $S_0=50$, sin dividendos. El tipo es $r=0{,}021$ continuo anual; $T=3$ años y los 36 tiempos son $t_j=j/12$. Las volatilidades **de los intervalos anuales** son $0{,}375$, $0{,}425$, $0{,}39$. No son volatilidades spot acumuladas a cada vencimiento. La moneda no está especificada: todos los precios se expresan en unidades monetarias (u.m.) por opción sobre una unidad del activo.

Las fechas bermuda son $\mathcal E=\{12,24,25,\ldots,36\}$ en meses: exactamente 14. La europea sólo paga en 36; la americana de esta comparación permite ejercicio en **todas las fechas de la malla**, incluido el origen. No se afirma que sea la americana de tiempo continuo.

Para los 15 días se adopta $t_*=15/365$ años (base fija de 365 días). Al no existir fecha civil de origen en el enunciado, los meses contractuales siguen siendo fracciones $m/12$ del año; no se inventan meses de 30 días ni un calendario real. Así se fija de manera transparente cómo relacionar días naturales y tiempos del modelo.

## Construcción. JR exacto y estados

PDF-003 pp.24–25 distingue JR exacto y aproximado. Elegimos el exacto del curso. Para cada intervalo $h_j=t_{j+1}-t_j$, $a_j=\sigma_j\sqrt{h_j}$:

$$p_u=p_d=\tfrac12,\quad
u_j=\frac{e^{rh_j+a_j}}{\cosh a_j},\qquad
d_j=\frac{e^{rh_j-a_j}}{\cosh a_j}.$$

Aquí $u_j$ es el multiplicador alcista. Se cumple exactamente

$$\frac{u_j+d_j}{2}=e^{rh_j},\quad
\operatorname{Var}(\log S_{j+1}/S_j)=a_j^2,\quad
E^Q[e^{-rh_j}S_{j+1}\mid\mathcal F_j]=S_j.$$

La condición $d_j<e^{rh_j}<u_j$ asegura ausencia de arbitraje. El numerario es la cuenta bancaria $e^{rt}$ y $Q$ es su medida de valoración, no una medida histórica. La variante $e^{(r-\sigma^2/2)h\pm\sigma\sqrt h}$ sólo impone aproximadamente la primera igualdad; no se mezcla con probabilidades CRR.

Dentro de un año sí recombinan las ramas con el mismo $a$; entre años diferentes, no se puede reunir todo por el número total de subidas. Con $n_g$ pasos consumidos y $k_g$ subidas en cada grupo $g$ de amplitud común:

$$S_j=S_0\exp\left(\sum_{i<j}[rh_i-\log\cosh a_i]+
\sum_g(2k_g-n_g)a_g\right).$$

El estado es el vector $(k_1,k_2,k_3)$, con dimensiones que crecen sólo al consumir pasos del grupo. Son 2.197 estados terminales y 16.471 estados sumando todos los niveles, frente a $2^{36}$ historias posibles. No se fusionan estados de bloques distintos por parecido de spot; una eventual coincidencia de precio tampoco sería problemática, pues el futuro es el mismo en un tiempo dado. La representación conserva exactamente el contrato mensual. La malla de varianza uniforme de XLS-011/PDF-003 pp.74–83 sirve como contraste metodológico, pero movería las fechas del encargo y no se utiliza.

`Tree` construye cada matriz `spot` con la ecuación anterior. Los índices `groups` indican la dimensión que cambia en cada transición; los dos sucesores son cortes contiguos de la matriz del nivel siguiente. El primer intervalo residual de E1b constituye un grupo independiente.

## Apartado a. Retroceso y precios

Desde $V_{36}=(K-S_{36})^+$, se calcula

$$C_j=e^{-rh_j}(V_{j+1,u}+V_{j+1,d})/2.$$

Fuera de las fechas permitidas, $V_j=C_j$. Donde hay derecho de ejercicio, $V_j=\max((K-S_j)^+,C_j)$. Es la regla de parada de PDF-003 pp.45–51. Los tres contratos comparten exactamente los factores, probabilidades y descuento.

|Contrato|Prima inicial (u.m.)|Exceso sobre europea|
|---|---:|---:|
|Europea|8,921639|0|
|Bermuda|9,162908|0,241269|
|Americana mensual|9,197452|0,275813|

La americana excede la bermuda en 0,034545. La inclusión de conjuntos de fechas demuestra el orden europea $\leq$ bermuda $\leq$ americana: más derechos no pueden disminuir el valor. Económicamente, la put puede beneficiarse de recibir antes el strike y evitar la pérdida de intereses; debe compararse este beneficio con la opcionalidad sacrificada. Los meses adicionales de la americana aportan poco frente a la bermuda, que ya permite ejercicio mensual el último año.

Una suma directa del payoff europeo bajo la distribución producto de tres binomiales da 8,921639042393926, frente a 8,921639042393917 por retroceso. Este control cambia el modo de calcular la esperanza. No se usaron cachés de los Excel docentes.

## Apartado b. Quince días y resultado económico

Se reconstruye el árbol desde $S_{t_*}=52{,}5$ hasta las mismas fechas $j/12$. El primer paso dura $1/12-15/365=0{,}042237443$ años; el resto sigue mensual. La volatilidad sigue cambiando en **los años contractuales 1 y 2**, sin reiniciar un año de volatilidad desde la revaloración. La varianza restante es

$$0{,}375^2(1-15/365)+0{,}425^2+0{,}39^2.$$

La suma de intervalos es $3-15/365$ y se mantienen las 14 fechas bermuda. La americana desde el nuevo origen puede ejercerse en ese instante y las restantes fechas originales; sigue siendo una aproximación discreta.

|Contrato|Prima después de 15 días|Cambio $V_*-V_0$|Resultado financiado $V_*-e^{rt_*}V_0$|
|---|---:|---:|---:|
|Europea|8,175126|−0,746513|−0,754216|
|Bermuda|8,390743|−0,772165|−0,780076|
|Americana mensual|8,419723|−0,777729|−0,785670|

**Habría convenido mantener una europea**, bajo el criterio de una opción de cada tipo comprada en el origen y liquidada en este escenario: pierde 0,025860 u.m. menos que la bermuda y 0,031454 menos que la americana, contando financiación. Es una comparación de P&L, no de prima actual. En rentabilidad financiada sobre prima inicial también tiene la menor pérdida (aproximadamente 8,45%, 8,51% y 8,54%, respectivamente). No es una recomendación universal: depende del movimiento observado y de la exposición elegida. No hubo fechas bermuda de ejercicio durante esos 15 días.

## Apartado c. Réplica autofinanciada y primera parada

En cada nodo vivo que continúa (PDF-003 pp.54–60):

$$\Delta_j=\frac{V_u-V_d}{S_j(u_j-d_j)},\qquad
B_j=e^{-rh_j}(V_d-\Delta_jS_jd_j).$$

$\Delta$ son unidades de activo y $B$ es el saldo **en dinero de ese instante**, no unidades de bono. Se verifican las dos identidades locales

$$\Delta_jS_ju_j+B_je^{rh_j}=V_u,\quad
\Delta_jS_jd_j+B_je^{rh_j}=V_d.$$

Su promedio descontado da $\Delta_jS_j+B_j=C_j=V_j$ en continuación. Tras observar el siguiente precio, el patrimonio es $W_{j+1}=\Delta_jS_{j+1}+B_je^{rh_j}$. El rebalanceo establece

$$B_{j+1}=W_{j+1}-\Delta_{j+1}S_{j+1},$$

por lo que no se aporta ni retira capital. Se preserva este saldo calculado desde la riqueza, en lugar de reiniciar cada paso con el saldo teórico: así se mide el error acumulado. Al primer ejercicio óptimo se vende la acción, se liquida la cuenta y se paga $(K-S)^+$. Cada senda acaba ahí. A vencimiento con payoff cero el contrato expira sin ejercicio.

La política elige ejercicio sólo si el intrínseco es positivo y excede la continuación en más de $10^{-12}$ u.m.; los empates continúan. Este umbral numérico no tiene significado económico. Se simulan 200.000 sendas iid con generador NumPy PCG64 y semilla 20261024; en cada paso se sortea una rama equiprobable. Se usa exactamente la dinámica valorada, bajo $Q$.

Los máximos observados son: error local $1{,}51\cdot10^{-14}$, error de presupuesto teórico $1{,}42\cdot10^{-14}$, error acumulado de réplica $1{,}15\cdot10^{-13}$ y de rebalanceo $1{,}18\cdot10^{-13}$ u.m. La tolerancia de aceptación es $10^{-10}$. La cobertura es exacta matemáticamente en el árbol y alcanza precisión de redondeo en cómputo. No prueba cobertura perfecta al simular una difusión continua con rebalanceo mensual: ésa sería otra dinámica y otra prueba.

Para contraste exacto se propaga una masa inicial 1. En cada nivel se absorbe la masa que ejerce; sólo la viva se reparte por mitades a los sucesores. Al recombinar se suman contribuciones. Esta propagación permite obtener probabilidades sin error de Monte Carlo y reconstruir el precio como suma de pagos descontados.

|Primera parada|Estimación MC incondicional|IC Wilson 95%|Probabilidad exacta|Exacta condicionada a supervivencia|
|---|---:|---|---:|---:|
|Mes 12|1,9010%|[1,8421%; 1,9618%]|1,928711%|1,928711%|
|Mes 36|6,0420%|[5,9384%; 6,1473%]|6,064783%|12,308531%|

La probabilidad exacta de llegar vivo al mes 36 es 49,273003%; la de expirar sin ejercicio es 43,208220%. Las probabilidades de todos los primeros ejercicios más esa expiración suman 1. Los IC anteriores son marginales, no bandas simultáneas de toda la política. Para cada proporción se usa Wilson con $z=1{,}959964$, centro $(\hat p+z^2/(2N))/(1+z^2/N)$ y semiancho $z\sqrt{\hat p(1-\hat p)/N+z^2/(4N^2)}/(1+z^2/N)$.

Estar dentro del dinero en el mes 12 **no** basta para ejercer: puede ser óptimo esperar. Estar ITM al vencimiento sí implica ejercicio para las sendas aún vivas; no cuenta a quienes ya ejercieron. Los JSON y la hoja incluyen las 14 fechas, supervivencia, probabilidad incondicional y condicionada, además de una senda con posiciones y saldos.

## Apartado d. Continuación Black–Scholes sin añadir pasos

PDF-006 pp.51–53 propone suavizar la discontinuidad de la delta del payoff final. En el nivel 35 se sustituye la media de los dos pagos terminales por la put europea Black–Scholes de un mes, con volatilidad 39% y el mismo tipo:

$$C_{35}^{BS}=Ke^{-rh}\Phi(-d_2)-S_{35}\Phi(-d_1),\quad
 d_1=\frac{\log(S_{35}/K)+(r+\sigma^2/2)h}{\sigma\sqrt h},\quad d_2=d_1-\sigma\sqrt h.$$

Se mantiene $V_{35}=\max(K-S_{35},C_{35}^{BS})$ pues el mes 35 es ejercitable. Antes de él se usa el retroceso mensual original. La malla sigue teniendo 36 intervalos; el último se integra analíticamente. Esto **modifica la aproximación de continuación**, no es otro precio exacto del árbol binario original ni se somete a su prueba de réplica de dos ramas.

Para evaluar precisión se usa como referencia la difusión límite de JR con volatilidad anual por tramos, conservando las mismas 14 fechas de parada (no una americana continua). Entre fechas la transición de $x=\log(S/50)$ es normal de media $rh-v/2$ y varianza $v=\int\sigma^2dt$. Se aplica su semigrupo por convolución gaussiana en una malla uniforme de log-precio, seguido del máximo sólo en las fechas contractuales.

|Paso espacial $\Delta x$|Bermuda de difusión (u.m.)|
|---|---:|
|0,004|9,11389412|
|0,002|9,11375310|
|0,001|9,11369124|
|0,0005|9,11367048|
|0,00025|9,11366796|

Se utiliza dominio $x\in[-8,8]$, kernel truncado a nueve desviaciones, convolución FFT y desplazamiento por interpolación lineal. Ampliar el dominio de [-6,6] a [-8,8] cambia menos de $10^{-8}$ a paso 0,001. Con paso 0,00025 la europea de la misma integración reproduce Black–Scholes con varianza total a menos de $2\cdot10^{-6}$. La última diferencia de refinamiento de la bermuda es $2{,}52\cdot10^{-6}$; es evidencia empírica de convergencia, no una cota matemática certificada. La referencia se justifica por la transición lognormal exacta de la difusión y por estos controles independientes de la recurrencia binomial.

|Aproximación mensual|Precio|Error absoluto frente a 9,11366796|
|---|---:|---:|
|JR puro|9,16290759|0,04923963|
|JR con BS en mes 35|9,13920110|0,02553314|

El suavizado reduce el error aproximadamente un 48,15% en **este** contrato. El error restante procede de los otros intervalos binarios y de las fronteras de ejercicio. No se sostiene que siempre mejore: se demuestra aquí frente a la referencia de difusión; la solución solicitada sigue siendo la de 36 pasos.

# Ejercicio 2. FRA y caplet in arrears normales

## Contrato, numerario y cambio de fecha de pago

PDF-002 p.3 define $U=T+\delta$, fixing en $T$ para el periodo $[T,U]$, con **pago en $T$** de $Nom\,\delta(F_T-K)$ o $Nom\,\delta(F_T-K)^+$. Aquí $F_T=R(T,U)$, $Nom$ es nominal en la moneda del contrato y $K,F$ son tipos simples anuales. El enunciado no aporta cifras. La derivación siguiente es general para $0\le t\le T$; $\tau=T-t$.

En una sola curva (PDF-008 pp.5–8),

$$F_t=\frac{P(t,T)/P(t,U)-1}{\delta},\quad
1+\delta F_t=\frac{P(t,T)}{P(t,U)},\quad
1+\delta F_T=\frac1{P(T,U)}.$$

Se toma el bono $P(t,U)$ como numerario; su medida es $Q^U$. El cociente de bonos y, por linealidad, $F_t$, son martingalas. Un flujo $H_T$ que paga antes de vencer el numerario se valora como

$$V_t=P(t,U)E_t^{Q^U}\left[\frac{H_T}{P(T,U)}\right].$$

Por tanto, para $g(x)=x-K$ o $(x-K)^+$,

$$V_t=Nom\,\delta P(t,U)E_t^{Q^U}[g(F_T)(1+\delta F_T)].\tag{E2.1}$$

El factor adicional **multiplica**, no divide el payoff. No se añade el denominador de un FRA comercial liquidado por descuento de su liquidación: sería otro contrato. Este paso retoma el argumento de PDF-008 pp.14–19 pero **no** sus momentos lognormales.

Formalmente, la densidad del cambio de $Q^U$ a la medida $Q^T$, hasta $T$, sería

$$\left.\frac{dQ^T}{dQ^U}\right|_T
=\frac{1+\delta F_T}{1+\delta F_t}.$$

Entonces $V_t=P(t,T)E_t^{Q^T}[H_T]$. Esta igualdad explica por qué descontar en $T$ manteniendo sin cambios la distribución $Q^U$ pierde el ajuste. La positividad de esa densidad se matiza al final: en el normal ilimitado es una identidad formal de la aproximación, no un cambio global de probabilidad exacto.

## Dinámica y momentos completos

Se postula bajo $Q^U$ (PDF-009 pp.38–40)

$$dF_s=\sigma_n(s)dW_s^U,\qquad
F_T=f+sZ,\quad f=F_t,\quad s=\sqrt v,\quad
v=\int_t^T\sigma_n(u)^2du,\quad Z\sim N(0,1).$$

La forma normal es válida para volatilidad determinista integrable; si la volatilidad es constante, $v=\sigma_n^2\tau$. No se afirma normalidad con una volatilidad estocástica arbitraria. $\sigma_n$ tiene unidades de tipo anual por raíz de año: 0,01 significa 100 puntos básicos por raíz de año, no un 1% relativo a $f$.

Sean $\phi(z)=e^{-z^2/2}/\sqrt{2\pi}$ y $\Phi$ su integral acumulada. Por simetría, $E[Z]=0$; usando $\phi'=-z\phi$ e integración por partes, $E[Z^2]=1$. Así,

$$E[F_T]=f,\qquad E[F_T^2]=f^2+v.$$

Luego

$$E[(F_T-K)(1+\delta F_T)]
=(f-K)+\delta(f^2+v-Kf)
=(1+\delta f)(f-K)+\delta v.$$

La fórmula solicitada del FRA es

$$\boxed{V_t^{FRA}=Nom\,\delta P(t,U)
\big[(1+\delta f)(f-K)+\delta v\big].}\tag{E2.2}$$

Usando $P(t,T)=P(t,U)(1+\delta f)$ también puede escribirse

$$V_t^{FRA}=Nom\,\delta P(t,T)
\left[f+\frac{\delta v}{1+\delta f}-K\right].$$

El strike que anula el FRA es $K_{IA}=f+\delta v/(1+\delta f)$. El denominador aparece **al factorizar para expresar el strike**, no como un descuento extra del payoff. Para $1+\delta f>0$ el ajuste de timing es positivo: el peso $1+\delta F_T$ aumenta los escenarios de tipos altos. A diferencia del caso lognormal, la corrección de segundo momento es $v$, no $f^2(e^{\sigma^2\tau}-1)$.

## Momentos truncados y caplet

Para $s>0$, sea $a=(K-f)/s$ y $d=-a=(f-K)/s$. El evento de ejercicio es $Z>a$. Calculamos explícitamente:

$$I_0=\int_a^\infty\phi(z)dz=\Phi(-a)=\Phi(d),$$

$$I_1=\int_a^\infty z\phi(z)dz=[-\phi(z)]_a^\infty=\phi(a),$$

$$I_2=\int_a^\infty z^2\phi(z)dz
=[-z\phi(z)]_a^\infty+\int_a^\infty\phi(z)dz
=a\phi(a)+\Phi(-a).$$

Los términos de frontera en infinito son cero porque la gaussiana domina cualquier polinomio. Por expansión de $f+sZ$:

$$E[1_{F_T>K}]=\Phi(d),$$

$$E[F_T1_{F_T>K}]=f\Phi(d)+s\phi(d),$$

$$E[F_T^2 1_{F_T>K}]=(f^2+v)\Phi(d)+(f+K)s\phi(d).$$

La última expresión usa $2fs+s^2a=(f+K)s$. Definimos el momento Bachelier sin descuento

$$A=E[(F_T-K)^+]=(f-K)\Phi(d)+s\phi(d).$$

Restando $K$ veces el momento de primer grado al de segundo grado:

$$E[F_T(F_T-K)^+]
=[f(f-K)+v]\Phi(d)+fs\phi(d)
=fA+v\Phi(d).$$

Al sustituir en (E2.1), obtenemos

$$\boxed{V_t^C=Nom\,\delta P(t,U)
\left[(1+\delta f)\big((f-K)\Phi(d)+s\phi(d)\big)
+\delta v\Phi(d)\right].}\tag{E2.3}$$

Para volatilidad constante basta usar $s=\sigma_n\sqrt{T-t}$. La fórmula equivalente con descuento al fixing es

$$V_t^C=Nom\,\delta P(t,T)
\left[A+\frac{\delta v}{1+\delta f}\Phi(d)\right].$$

El primer término es Bachelier con descuento en $T$; el segundo mide el cambio de distribución por pago temprano, no un ajuste lognormal copiado. En `ejercicio2.py`, `variance` representa $v$, `a` representa $A$ y `p_u` representa $P(t,U)$; se separa explícitamente la rama $v=0$ para evitar dividir por cero.

## Floorlet, paridad, límites y unidades

Como control adicional, $B=E[(K-F_T)^+]=(K-f)\Phi(-d)+s\phi(d)$ y

$$E[F_T(K-F_T)^+]=fB-v\Phi(-d).$$

Por tanto, el floorlet equivalente, que también paga en $T$, vale

$$V_t^P=Nom\,\delta P(t,U)[(1+\delta f)B-\delta v\Phi(-d)].$$

Usando $A-B=f-K$ y $\Phi(d)+\Phi(-d)=1$ se verifica exactamente $V^C-V^P=V^{FRA}$. Una paridad con floorlet de pago en $U$ no correspondería a los mismos contratos.

Al hacer $\sigma_n\to0$ o $T\to t$, $v\to0$; las fórmulas convergen a $Nom\,\delta P(t,T)g(f)$. Para ATM, $A=s/\sqrt{2\pi}$ y el término de convexidad del caplet es $\delta v/2$ dentro del corchete con $P(t,U)$. Al escalar el nominal todos los valores escalan linealmente. En unidades, $\delta F$ es adimensional, $v$ tiene unidades de tipo al cuadrado, $\delta v$ tiene unidades de tipo, y $Nom\,\delta$ veces cada corchete devuelve moneda. Los tipos y devengos usan la misma unidad anual.

**Ejemplo meramente ilustrativo:** $f=3\%$, $K=3{,}2\%$, $T=2$, $\delta=0{,}5$, $\sigma_n=1\%/\sqrt{año}$, $P(0,U)=e^{-0{,}03\cdot2{,}5}$ y $Nom=10^6$. La curva se completa con $P(0,T)=P(0,U)(1+\delta f)$: no se supone simultáneamente un descuento exponencial plano para ambos bonos. Se obtiene:

|Magnitud|Resultado ilustrativo|
|---|---:|
|FRA in arrears|−895,272464|
|Caplet in arrears|2.232,647690|
|Floorlet in arrears|3.127,920154|
|Strike de equilibrio|3,00985222%|

La integración adaptativa independiente evalúa directamente $g(f+s z)(1+\delta(f+s z))\phi(z)$, separando en el strike; no llama a las fórmulas de momentos. Coincide a menos de $10^{-7}$ u.m. en 54 escenarios con tipos y strikes positivos, negativos y cero, y en dos escalas de volatilidad. Se comprueban además paridad, escala nominal, límites de varianza nula y strike de equilibrio. La hoja E2 presenta inputs ilustrativos editables, todos los momentos y las fórmulas de precio.

## Alcance de la aproximación normal

Una normal no degenerada asigna probabilidad positiva a $F_T<-1/\delta$. Pero un bono estrictamente positivo exige $1+\delta F_T=1/P(T,U)>0$. Los dos supuestos no definen globalmente un modelo exacto coherente de bonos positivos. Incluso la densidad formal de cambio de medida puede resultar negativa en esa cola. La inconsistencia afecta al modelo global, no al cálculo de los momentos solicitados.

Resolvemos la **aproximación normal docente sin truncar su distribución**, como pide el encargo. En el ejemplo la frontera está a más de 140 desviaciones típicas; esto explica su insignificancia numérica allí, pero no elimina la incompatibilidad matemática. Para otras escalas la cola podría ser material e incluso originar precios formales negativos de flujos no negativos; no habría que interpretarlos como precios de arbitraje de un modelo global válido. No se introduce silenciosamente una distribución truncada o desplazada, pues alteraría el ejercicio.

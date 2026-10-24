# Guía de defensa individual

No memorizar sólo precios: reconstruir contrato, numerario, ecuación y control. Practicar cada respuesta en 1–2 minutos y ser capaz de escribir sus ecuaciones sin mirar. Las preguntas siguientes son preparación, no predicción del cuestionario.

## Ejercicio 1

**¿Qué se ha calibrado en JR?** Probabilidad 1/2, esperanza de capitalización igual a exp(rh) y desviación del logretorno σ√h. La división por cosh(σ√h) asegura martingala exactamente. El JR exponencial con deriva r−σ²/2 sólo la aproxima a paso finito.

**¿Por qué no sirve el árbol triangular mensual habitual?** Con σ distinta por año, el tamaño de ruido de una subida cambia. Una subida en año1 y bajada en año2 no equivale a sus signos intercambiados. Se guardan conteos por cada bloque de igual amplitud, no un total único. Hay 2197 estados terminales, no 37 ni 2^36.

**¿Se ha cambiado el calendario para recombinar?** No. Sigue j/12, con ejercicio sólo en 12,24,25–36. Una malla uniforme en varianza sería otra aproximación temporal. Se reutiliza recombinación dentro de bloques, sin imponerla entre ellos.

**¿Por qué ese orden de primas?** Toda política europea está disponible a la bermuda y toda política bermuda a la americana mensual. El máximo sobre un conjunto mayor no puede valer menos. Las primas son 8,921639≤9,162908≤9,197452. La americana sigue siendo de fechas discretas.

**¿Por qué la put podría ejercerse antes?** Recibir K antes genera intereses y elimina la exposición futura; se sacrifica valor temporal. Estar ITM no decide: se compara K−S con el valor de continuar, no con cero solamente.

**¿Cómo se tratan los 15 días?** Se fija t*=15/365, se acorta sólo el primer intervalo hasta 1/12, y se mantienen vencimiento, ejercicios y fronteras de volatilidad en los tiempos originales. No se reinicia un contrato de tres años ni el primer año de volatilidad. El nuevo spot es 52,5.

**¿Qué opción habría convenido tener?** Una europea por unidad: P&L financiado −0,754216 frente a −0,780076 y −0,785670. Comparar primas después del movimiento no mide la ganancia de mantenerla desde el principio. Hay que restar el coste inicial y, si procede, financiarlo. Tampoco es una dominancia en todos los escenarios.

**¿Cómo se obtiene delta sin Black–Scholes?** Se resuelve el sistema de dos ecuaciones de pago en los dos sucesores. Δ=(Vu−Vd)/(Su−Sd), B=e^(−rh)(Vd−ΔSd). Dos activos y dos ramas distintas permiten réplica local exacta.

**¿Por qué es autofinanciada?** Al cambiar posiciones, la nueva cuenta es riqueza observada menos nueva Δ por spot. No se reinicia con dinero externo. Las identidades locales se encadenan y se liquida todo al primer ejercicio. El máximo error acumulado observado es del orden de 10^−13 con tolerancia 10^−10.

**¿Es cobertura perfecta de cualquier movimiento real?** La prueba sólo corresponde al mercado binomial simulado con las mismas ramas de valoración. Una difusión continua con rebalanceos mensuales admite movimientos distintos y genera error discreto. No es el mismo experimento.

**¿Qué probabilidad se estima?** Bajo Q del numerario bancario, no frecuencia histórica. Primera parada positiva óptima: 1,928711% exacto en mes12 y 6,064783% en mes36. En mes36, condicionado a haber llegado vivo, es 12,308531%; sólo llega vivo el 49,273003%. El resto puede haber ejercido antes o expirar sin payoff.

**¿Por qué no contar toda senda ITM en vencimiento?** Si ejerció antes ya no tiene opción; contarla de nuevo duplica eventos. En año1 además puede ser óptimo esperar aun estando ITM. Los empates continúan y payoff cero no se etiqueta como ejercicio.

**¿Cómo se conoce la incertidumbre?** N=200.000, semilla 20261024, IC Wilson95% para proporciones. Además hay propagación exacta de masa viva, que suma a1 con las primeras paradas y la expiración sin ejercicio. Wilson no mide incertidumbre del modelo ni es una banda simultánea.

**¿Qué mejora E1d y qué no?** En mes35 se integra el último mes con BS y se conserva max(intrínseco,continuación). Se mantienen36 intervalos. Frente a una difusión con las mismas fechas, el error pasa de 0,04924 a0,02553. El suavizado ya no es la recurrencia pura del árbol de dos ramas; no hereda su prueba de réplica terminal.

**¿Por qué confiar en la referencia?** Integra transiciones lognormales de la difusión por convolución, conserva las 14 fechas y converge al refinar log-precio. También reproduce la europea analítica y no cambia materialmente al ampliar dominio. La revisión independiente usa una PDE distinta. Es evidencia numérica, no prueba de una cota exacta.

## Ejercicio 2

**¿Qué es in arrears en este encargo?** Un flujo observado en T sobre [T,T+δ] y pagado en T. El contrato docente es la autoridad, aunque otra mesa use ese nombre para otra liquidación. No añadir un denominador al payoff.

**¿Por qué el bono U es numerario si se paga en T?** Hace martingala al forward en una curva. Un pago en T se divide por P(T,U) dentro de la esperanza. La identidad 1/P(T,U)=1+δF_T origina el factor multiplicativo.

**¿Cuál es el error de usar P(0,T) con esperanza Q^U sin ajuste?** Cambia el descuento sin cambiar la medida. El peso para pasar a Q^T es proporcional a 1+δF_T; favorece tipos altos. El ajuste del FRA viene de su covarianza con ese peso.

**¿Qué diferencia la normal de la lognormal?** F_T=f+σ_n√τ Z admite negativos y σ_n es absoluta. E[F²]=f²+v, no f² exp(σ²τ). Una σ_n de 0,01 son100pb/√año, no1% relativo al nivel del tipo.

**Reconstruye el FRA.** Expandir (F−K)(1+δF), tomar E[F]=f y E[F²]=f²+v. Sale Nom δ P_U[(1+δf)(f−K)+δv]. Su strike par es f+δv/(1+δf).

**Reconstruye el caplet sin aprender la fórmula.** Integrar sobre Z>a=(K−f)/s. Las integrales de φ,zφ,z²φ dan Φ(−a),φ(a),aφ(a)+Φ(−a). Así A=(f−K)Φ(d)+sφ(d), y E[F(F−K)+]=fA+vΦ(d). Introducirlos en la valoración da Nom δ P_U[(1+δf)A+δvΦ(d)].

**¿Qué paridad comprueba el calendario?** Caplet−floorlet=FRA si todos tienen mismo fixing, pagoT, strike, nominal y devengo. Mezclar pagoU y pagoT rompe la equivalencia contractual.

**¿Es un modelo exacto de bonos positivos?** No globalmente: una normal permite F<−1/δ pero la identidad de bonos positivos no. Se resuelve la aproximación docente sin truncar en secreto. La cola es insignificante en el ejemplo ilustrativo, no necesariamente con otros parámetros.

## Ejercicio 3

**¿Qué significa FX?** EUR porUSD. Multiplicarlo por un pagoUSD produceEUR. Invertir la cotización altera las derivas y correlaciones: no se cambia sólo el nombre del símbolo.

**¿Qué representan M y N?** La cuentaUSD convertida aEUR y descontada por cuentaEUR, y la acción con dividendos reinvertidos convertida y descontada. Las dos deben ser martingalas bajo Q EUR; el spot exdividendo descontado por sí solo no lo sería.

**¿Por qué ρMN no es ρS,FX?** La innovación de N es σS dZ+σX dW, no sólo la del spotS. Por covariación, σN²=σS²+σX²+2ρσSσX y ρMN=(σX+ρσS)/σN. En el ejemplo pasan de 0,4 a0,69259.

**¿Cómo decides el signo del quanto?** Calcular d(SX)=X dS+S dX+d[S,X]. El término cruzado es +ρσSσX SX dt. M fija μX=rd−rf y N obliga a μS=rf−q−ρσSσX. Para FX EUR/USD y ρ >0, el ajuste es negativo.

**¿Cuáles son los pagos usual y quanto?** Usual:X_T(S_T−K) o X_T(S_T−K)+ EUR. Quanto:λ(S_T−K) o λ(S_T−K)+ EUR, con λ fijo1EUR/USD. Multiplicar el quanto por FX otra vez sería valorar otro contrato.

**¿Cómo replicas el forward usual?** Comprar e^(−qT) acciones con reinversión para recibir una acción enT, y endeudarse Ke^(−rfT)USD. El coste totalUSD es S0e^(−qT)−Ke^(−rfT); todo se convierte aEUR con X0.

**¿Por qué no hay quanto en el precio usual?** Al ponderar el payoff por X_T, la inclinación exponencial de la normal conjunta cancela el ajuste de derivaS bajo Q EUR. Sale Black–Scholes USD por X0. La call quanto no recibe ese peso y conserva μS corregida.

**¿Qué corregiste en diap25 y cómo lo defenderías?** El cociente dentro del logaritmo de d lleva K exp(−rfT), no K exp(+rfT). La expresión con signo negativo produce ln(S0/K)+(rf−q)T. Lo comprueban la derivación EUR, el precioUSD, la réplica y las paridades. No se atribuyen a la plantilla pérdidas de paréntesis propias de la extracción.

**¿Qué casos límite conviene explicar?** T=0 devuelve payoff; σS=0 devuelve flujo determinista descontado; ρσXσS=0 elimina ajuste de deriva quanto. La call usual no cambia con rd,ρ,σX a datosUSD y X0 fijos. Si una martingala es constante no se inventa una correlación para ella.

## Ensayo y proceso individual (PDF-001 pp.1–2)

1. Completar los nombres del grupo, verificar que cada archivo abre y ensayar una pregunta de cada ejercicio con pantalla compartida.
2. Preparar Zoom de escritorio, grabación local, micrófono, compartir pantalla completa y SMOWL actualizado con prueba previa. Zoom con cámara apagada: la cámara la usa SMOWL.
3. Entre 1 y 8 de noviembre de 2026, antes de 23:59, iniciar grabación **antes** de subir la entrega. El máximo global es60 minutos; incluye todos los pasos posteriores.
4. Subir personalmente memoria y hojas; entrar al único intento del cuestionario, leer la pregunta y exponer la respuesta. Enviar todo y terminar antes de finalizar el tiempo; detener grabación (máximo30 minutos).
5. GuardarMP4, subirlo aOneDrive/GoogleDrive, permitir acceso a cualquiera con enlace y comprobarlo. Enviar enlace a jcontreras@afi.es y jcalderon@afi.es, con copia a jmedina@afi.es; asunto `MEFC_Defensa Trabajo de Valoración_Nombre Apellidos`.
6. Todo debe quedar terminado antes del plazo. Para defensa en la escuela, solicitar cita con al menos3 días de antelación. En incidencias, contactar con jmedina@afi.es.

Estos pasos se documentan para el alumno. No se han realizado acciones en campus, Zoom, almacenamiento de vídeo ni correo.

# PDF-004: MFC_26_ValoracionFundamentos_Teoría.pdf

Original: [archivo raw](../../raw/fundamentos/mfc-26-valoracionfundamentos-teoria.pdf). SHA-256: `928b526073ad39e25327e6a30120f3efdbe1c60709e0bdca04fc6eda6d541c89`.

Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.

## Página 1

Máster Executive Finanzas Cuantitativas
Valoración: 
Fundamentos
José María Contreras
jcontreras@afi.es

## Página 2

MFC 21-22
Valoraci´on. Fundamentos
Plan y resumen
Se pretende dar un marco general de modelos estoc´asticos que permiten valorar a
mercado (por replicaci´on) instrumentos derivados.
Los ingredientes de estos modelos ser´an
unos “activos b´asicos” Sj, en los que podemos invertir (comprar y vender) y que
constituyen el mercado subyacente;
uno de ellos se elegir´a como “numerario” N (la unidad de referencia);
y se postular´an “escenarios de evoluci´on” de los valores Sj(t) de los activos en el
tiempo;
(Los requisitos ﬁnancieros) Para que podamos usar el modelo para valorar a mercado
(lo que llamaremos un modelo “certiﬁcado”), deber´a
ser “(internamente) libre de oportunidades de arbitraje”: comprando y vendiendo
activos b´asicos dentro del modelo no podemos generar oportunidades de arbitraje.
ser “consistente con el mercado”: los precios que el modelo asigna en tiempo t = 0
a los activos b´asicos coinciden con los de mercado.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
2

## Página 3

MFC 21-22
Valoraci´on. Fundamentos
(La modelaci´on matem´atica) En la pr´actica,
→si el modelo incorpora una probabilidad P (que diremos de valoraci´on) en el espacio
de escenarios de evoluci´on de manera que, para cada uno de los activos Sj,
Sj(t)
N(t)
sea martingala,
entonces
→tendremos garantizado que el modelo es (internamente) libre de arbitraje y que
adem´as permite valorar (de manera consistente con el mercado) los instrumentos
derivados (que se puedan replicar con carteras de los activos b´asicos).
Si estos instrumentos vencen en tiempo T y llamamos X a sus ﬂujos, entonces la
valoraci´on vendr´a dada, simplemente, por
X0 = N(0) E
X(T)
N(T)

c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
3

## Página 4

MFC 21-22
Valoraci´on. Fundamentos
As´ı que si en un modelo tenemos
un numerario;
una probabilidad de valoraci´on;
y los activos b´asicos arrancan en tiempo t = 0 con su valor de mercado,
el modelo permitir´a “valorar” de manera eﬁciente y consistente con el mercado los
instrumentos derivados replicables con activos b´asicos.
Hay aqu´ı muchos t´erminos, muchos entrecomillados, todav´ıa por deﬁnir y formalizar. Lo
haremos gradualmente.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
4

## Página 5

MFC 21-22
Valoraci´on. Fundamentos
Discutiremos primero los distintos paradigmas de valoraci´on, centr´andonos en (e ilus-
trando con ejemplos sencillos) el de valoraci´on por replicaci´on (no arbitraje).
A continuaci´on, presentaremos la metodolog´ıa de valoraci´on por replicaci´on, con todos
sus ingredientes:
activos b´asicos, carteras, numerarios, oportunidades de arbitraje, replicaci´on,
probabilidad de valoraci´on, teorema fundamental de valoraci´on, mercados
completos, activos no replicables, etc.;
en tres contextos, con creciente grado de complejidad:
1. modelos discretos con un s´olo periodo de tiempo (modelos matriciales);
2. modelos discretos con varios periodos de tiempo (procesos discretos);
3. modelos continuos (procesos continuos).
Desarrollaremos el primer caso con todo detalle, y nos serviremos de ´el para ilustrar y
entender las distintas nociones que ir´an apareciendo. Pasaremos algo m´as ligeramente,
pero deteni´endonos en algunos detalles espec´ıﬁcos, sobre el segundo. Finalmente, tras
toda esta preparaci´on, ´unicamente exhibiremos los resultados en el tercer caso.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
5

## Página 6

MFC 21-22
Valoraci´on. Fundamentos
´Indice
1 Paradigmas de valoraci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2 Valoraci´on por replicaci´on. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .22
3 Modelo matricial de un solo periodo de tiempo: planteamiento
Escenarios, activos, carteras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Replicaci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
Oportunidades de arbitraje. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .56
4 Modelo matricial de un solo periodo de tiempo: valoraci´on
Probabilidad de valoraci´on. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .60
Mercados completos/mercados incompletos. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .71
5 Modelo de varios periodos de tiempo: planteamiento . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
6 Modelo de varios periodos de tiempo: valoraci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
7 Modelos continuos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
8 Ap´endice: complementos. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .118
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
6

## Página 7

MFC 21-22
Valoraci´on. Fundamentos
1. Paradigmas de valoraci´on
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
7

## Página 8

MFC 21-22
Valoraci´on. Fundamentos
¿Qu´e es valorar?
Por instrumento ﬁnanciero entendemos un contrato entre dos partes por el que se
estipulan unos ﬂujos en ciertas fechas futuras, y por el que en la fecha de hoy se
paga un cierto montante entre las partes.
Valorar un instrumento ﬁnanciero I consiste en determinar ese montante que se
paga hoy. Queremos que el precio que asignamos hoy al instrumento sea razonable,
consistente, equivalente, representativo de los ﬂujos del futuro.
En nuestro an´alisis, deberemos tener en cuenta dos ingredientes:
Los ﬂujos se reciben en el futuro, y, por supuesto, para valorarlos hay que tener en
cuenta el valor temporal del dinero. Supondremos que disponemos de la curva de
factores de descuento (sin riesgo o incertidumbre): FD(t) es el factor de descuento
desde la fecha t a hoy.
Adem´as, los ﬂujos est´an, en general, sujetos a incertidumbre: no sabemos cu´al va a
ser su montante exacto. El momento del pago de ﬂujos puede ser incierto tambi´en.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
8

## Página 9

MFC 21-22
Valoraci´on. Fundamentos
Valoraci´on de lo cierto
Digamos que el instrumento paga cantidades seguras
f1, . . . , fN
(montantes ﬁjos, que no dependen de niveles de otras variables ﬁnancieras; y sin riesgo
de contrapartida) en correspondientes fechas futuras
t1, . . . , tN
Obtenemos el valor del instrumento descontando los ﬂujos:
Valor =
N

j=1
fj FD(tj) ,
donde FD(tj) es el factor de descuento desde la fecha tj a hoy.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
9

## Página 10

MFC 21-22
Valoraci´on. Fundamentos
La expresi´on anterior es bien natural. Pero, ¡atenci´on!, vista desde otro punto de vista,
la cantidad
f1 FD(t1) + f2 FD(t2) + · · · + fN FD(tN)
es tambi´en el dinero necesario (hoy) para replicar los ﬂujos (futuros) del instrumento.
Porque permite comprar
f1 unidades del bono cup´on cero de fecha t1 (que cuesta hoy FD(t1) y paga 1 en
tiempo t1);
f2 del bono cup´on cero que vence en t2 (que cuesta hoy FD(t2) y paga 1 en
tiempo t2); etc.
Si el precio del instrumento no fuera el valor determinado m´as arriba, entonces (en
principio) se podr´ıa arbitrar.
Observaci´on
El argumento anterior requiere que los factores de descuento sean realmente precios de instrumentos (bonos cup´on
cero, en este caso), que no haya comisiones, que se puedan asumir posiciones cortas sobre los bonos, etc.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
10

## Página 11

MFC 21-22
Valoraci´on. Fundamentos
Valoraci´on de lo incierto: ingredientes
Los ﬂujos de los instrumentos ﬁnancieros generales son inciertos y no seguros. El enfoque
general de valoraci´on de instrumentos ﬁnancieros – en el que se enmarcan los distintos
paradigmas de valoraci´on – requiere especiﬁcar:
escenarios;
ﬂujos y descuentos;
probabilidades.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
11

## Página 12

MFC 21-22
Valoraci´on. Fundamentos
1. Escenarios
Se trata de determinar qu´e puede ocurrir en el futuro. Decidir qu´e eventos futuros
(relevantes para el instrumento, o mejor, para una cierta colecci´on de instrumentos) hay
que tener en cuenta.
En cualquier paradigma de valoraci´on, la determinaci´on de los escenarios del an´alisis
permite cierta discrecionalidad. Muchas veces no podremos abarcar y analizar todas las
posibilidades y nos centraremos en cierto resumen razonable.
Cada escenario es, en realidad, un futuro potencial completo en el que se recoge una
posible evoluci´on de las variables de las que dependen los ﬂujos del instrumento.
Cuando se analiza un escenario, entendemos que ese futuro que recoge es lo que va a
ocurrir, que es seguro: analizar un escenario es condicionar sobre un posible futuro.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
12

## Página 13

MFC 21-22
Valoraci´on. Fundamentos
2. Flujos y descuentos
Para cada escenario habr´a que precisar a continuaci´on
Flujo, el montante que se recibir´a o pagar´a en cada escenario concreto.
Descuento que se ha de aplicar a ese ﬂujo. Se trata del descuento por efecto del valor
temporal del dinero. El descuento depende del escenario. En algunas situaciones, el
descuento depender´a de la evoluci´on (incierta) de los tipos de inter´es.
Tanto el montante del ﬂujo como el descuento aplicable dependen de manera precisa del
escenario. Pero, una vez ﬁjado el escenario, ﬂujos y descuentos quedan completamente
determinados.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
13

## Página 14

MFC 21-22
Valoraci´on. Fundamentos
3. Probabilidad
El ´ultimo ingrediente es el m´as delicado. Si entendemos que estamos en un contexto
de incertidumbre, debemos asignarle a cada escenario de futuro una probabilidad de
que ocurra. Como los escenarios han de cubrir todas las posibilidades, la suma de estas
probabilidades sobre todos los escenarios posibles ha de ser 100 %.
La probabilidad de un escenario es la frecuencia (relativa) con la que puede ocurrir.
¿De d´onde se obtiene esa asignaci´on de probabilidad? Depende. Hay distintos paradigmas
de valoraci´on, y la diferencia esencial entre ellos radica en la fuente de informaci´on. La
asignaci´on puede
depender de nuestras propias intuiciones;
sostenerse exclusivamente en datos estad´ısticos que nos dan la frecuencia de esos
eventos;
basarse en cotizaciones de instrumentos similares;
o ser una combinaci´on de las anteriores.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
14

## Página 15

MFC 21-22
Valoraci´on. Fundamentos
En suma, tendremos una asignaci´on
escenario e −→
⎧
⎨
⎩
ﬂujo (instrumento, fecha, escenario)
descuento (fecha, escenario)
probabilidad (escenario)
El esquema de valoraci´on usual asigna, como valor del instrumento, el valor medio
(valor esperado, esperanza) de los ﬂujos descontados ponderados con las probabilidades
asignadas:
preciohoy(instrumento) =

escenarios e

ﬂujoe × descuentoe × probabilidade
	
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
15

## Página 16

MFC 21-22
Valoraci´on. Fundamentos
Valoraci´on de lo incierto: paradigmas
Paradigma de valoraci´on actuarial
Si tenemos buena informaci´on estad´ıstica de la frecuencia con la que cada escenario ha
ocurrido en el pasado, y el entorno se mantiene, podemos entender que esa frecuencia
del pasado (adecuadamente analizada) es v´alida para el futuro. Es el caso, por ejemplo,
de los juegos de azar, los an´alisis actuariales o el riesgo de cr´edito minorista.
Entendemos, en este caso, que se trata de una probabilidad objetiva. La asignaci´on
de probabilidad es una realidad f´ısica, independiente de opiniones. El paradigma de
valoraci´on nos dice que
precio =

escenarios e
ﬂujoe × descuentoe × probabilidade
Este esquema de valoraci´on se fundamenta en las leyes de los grandes n´umeros, es decir,
en la repetici´on del experimento aleatorio en cuesti´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
16

## Página 17

MFC 21-22
Valoraci´on. Fundamentos
Digamos que las variables aleatorias X1, . . . , XN codiﬁcan
los premios obtenidos en sucesivas partidas de un juego de azar,
o los pagos a N mutualistas por los siniestros sufridos durante el pr´oximo a˜no,
o los impagos de los pr´estamos de una cartera hipotecaria, etc.
Interesa la variable aleatoria que registra el premio tras N partidas (o el pago total a
los mutualistas, o el n´umero de defaults en la cartera, etc.):
YN =
N

i=1
Xi ,
Hip´otesis:
→Si las variables Xi son id´enticas (tienen la misma distribuci´on que una X de
referencia), entonces E(YN) = NE(X) .
(Partidas se juegan en igualdad de condiciones, mutualistas/hipotecados que son clientes
“homog´eneos”, etc.)
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
17

## Página 18

MFC 21-22
Valoraci´on. Fundamentos
→Pero si, adem´as, las variables con independientes (basta con que sean incorreladas),
entonces las leyes de los grandes n´umeros nos dicen que, si N es grande,
N

i=1
Xi

  
aleatorio
≃
N · E(X)



seguro
Es decir, los pagos individuales son aleatorios, pero al agregarse son “casi ciertos”.
Lo que, traducido en valoraci´on, nos dice que recibir los ﬂujos aleatorios YN de un n´umero
grande de partidas es equivalente (con probabilidad elevada y aproximadamente) a
recibir por partida la cantidad ﬁja E(X), el valor medio de los ﬂujos.
Observaci´on
En este paradigma de valoraci´on entendemos que es equivalente tener el activo con riesgo, con incertidumbre en sus
ﬂujos, que tener en dinero su precio hoy.
Las leyes de los grandes n´umeros son las que eliminan el riesgo.
El n´umero E(X) ser´ıa la prima (pura) por partida (o la prima para los mutualistas, o el
coste de cobertura de los posibles defaults, etc.).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
18

## Página 19

MFC 21-22
Valoraci´on. Fundamentos
A´un m´as, el teorema del l´ımite central permite cuantiﬁcar c´omo de probable es que YN
se aparte de la cantidad NE(X). Por ejemplo, permite calcular (aproximadamente)
cantidades como P(|YN −NE(X)| > a) sin necesidad de conocer la distribuci´on
concreta de YN (bastan la media y la desviaci´on t´ıpica de las Xj): si N es grande (con
variables independientes e id´enticas),
P(|YN −NE(X)| > a) ≈1 −Φ

a

NV(X)

.
Ejercicio
Calcula la prima para que N · prima ≥YN con cierto margen de conﬁanza (por ejemplo, 95 %):
• cuando X = ±1 con probabilidad p y 1 −p (premio en partidas a cara/cruz).
• Si X toma valores 0, 1 y 10 con probabilidades 30 %, 60 % y 10 % (pago total a los mutualistas).
• Cuando X = 1 con probabilidad p y X = 0 con 1 −p (n´umero de defaults).
• ¿Qu´e ocurre cuando las Xi tienen alta correlaci´on? Por ejemplo, correlaci´on 1.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
19

## Página 20

MFC 21-22
Valoraci´on. Fundamentos
As´ı que
si se sabe de manera objetiva que los ﬂujos de un instrumento (juego) son aleatorios;
si se conoce con precisi´on la distribuci´on de probabilidad de los resultados;
y si vamos a invertir en ´el un n´umero grande de veces en condiciones id´enticas (jugar
muchas partidas),
entonces (y solo entonces) la esperanza es un equivalente (casi cierto) de los ﬂujos
futuros.
Son muchas hip´otesis sobre la estructura aleatoria, que se cumplen (casi) en los juegos de
azar, en los contratos de seguros, y en el cr´edito minorista. Se cumplen pero (bastante)
menos en inversi´on repetida en periodos (relativamente) cortos en Bolsa. Y poco o nada
en contratos a plazo, derivados o no.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
20

## Página 21

MFC 21-22
Valoraci´on. Fundamentos
Pero digamos ahora que tenemos un ´unico contrato. Por simpliﬁcar, supongamos que
hay una ´unica fecha de pago y que el ﬂujo del instrumento es f.
Disponemos de largas series de datos hist´oricos anteriores valores de f, en las que
observamos que f paga 10 en el 50 % de los casos, 3 en el 30 % de las ocasiones y −1
en el restante 20 %. La tentaci´on (y el pecado) consiste en calcular
valor hoy = 10 × 50 % + 3 × 30 % + (−1) × 20 % = 5.7 .
¿Qu´e sentido tiene esto? Esta “esperanza” no es se justiﬁca por las leyes de los grandes
n´umeros (que no son de aplicaci´on en esta situaci´on). No hay un “equivalente cierto”.
Podr´ıamos, alternativamente, emplear una asignaci´on personal (subjetiva) de probabili-
dades. Desde luego, esta valoraci´on subjetiva (y la basada en datos hist´oricos) permite
tomar decisiones. Pero. . .
En lo que sigue, analizaremos el paradigma de que deberemos utilizar, por ejemplo, en
la valoraci´on de derivados ﬁnancieros: el de valoraci´on por replicaci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
21

## Página 22

MFC 21-22
Valoraci´on. Fundamentos
2. Valoraci´on por replicaci´on
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
22

## Página 23

MFC 21-22
Valoraci´on. Fundamentos
Par´abola de la porra
Supongamos que s´olo hay dos resultados (por ejemplo, una ﬁnal de Copa): victoria de X
o victoria de Y. Cada apuesta es de 1 euro.
Disponemos de los datos hist´oricos, que nos dicen que:
victoria de X en un 40 %; victoria de Y en un 60 %.
Por otro lado, nuestra opini´on experta asigna
probabilidad 20 % a la victoria de X, y 80 % a la victoria de Y.
Por ´ultimo, observamos el mercado. Hay, hasta el momento, 1 mill´on de apuestas:
el 30 % son apuestas por X; el 70 %, apuestas por Y.
Nuestra decisi´on de apostar por uno u otro equipo ya recoge toda nuestra informaci´on,
an´alisis t´ecnico o fundamental.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
23

## Página 24

MFC 21-22
Valoraci´on. Fundamentos
En el mecanismo de la porra, una apuesta por X supone que
su precio es 1;
no hay descuento;
los pagos son
⎧
⎨
⎩
si gana X ,
pago de
1000000
300000 = 10
3 ;
si gana Y ,
pago de 0.
An´alogamente, cada apuesta por Y paga 10/7 en caso de victoria de Y, y 0 en caso
contrario.
Derivados. Alguien nos ofrece
si gana X −→
5;
si gana Y −→
3.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
24

## Página 25

MFC 21-22
Valoraci´on. Fundamentos
¿C´omo valorar esta oferta OTC? ¿C´omo obtener su precio? (hacemos caso omiso de
comisiones).
Queremos aplicar el paradigma de valoraci´on habitual. Esto es, promediar los posibles
pagos (recordemos que no hay descuento).
Pero, ¿c´omo los promediamos?
Usando la probabilidad hist´orica,
precio = 5 × Prob(X)



=0.4
+3 × Prob(Y )



=0.6
= 3.8 .
Usando la probabilidad “personal”,
precio = 5 × Prob(X)



=0.2
+3 × Prob(Y )



=0.8
= 3.4 .
Usando la de “mercado”,
precio = 5 × Prob(X)



=0.3
+3 × Prob(Y )



=0.7
= 3.6 .
Cada par de probabilidades nos dar´ıa un precio distinto. De hecho, se podr´ıa obtener
cualquier precio entre 3 y 5 eligiendo adecuadamente las probabilidades.
Pero en realidad solo el precio (3.6) calculado con las que hemos dado en llamar
probabilidades “de mercado” es el correcto (pues no crea oportunidades de arbitraje).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
25

## Página 26

MFC 21-22
Valoraci´on. Fundamentos
Justiﬁcaci´on: formamos una cartera con 1.5 boletos de X y 2.1 boletos de Y.
Formar esta cartera cuesta precisamente 3.6 euros. Pero la cartera equivale al contrato
que ofrece el revendedor, puesto que
si gana X, paga
−→
(1.5) × 10
3 = 5;
y si gana Y, paga
−→
(2.1) × 10
7 = 3.
Observaci´on
Por supuesto, el 1.5 y el 2.1 han sido calculados resolviendo un sistema de ecuaciones: si la cartera tiene α apuestas
por X y β apuestas por Y, queremos que α y β sean soluci´on de
 si gana X,
α 10/3 = 5
si gana Y,
β 10/7 = 3
As´ı que la “probabilidad” que llam´abamos de “mercado” es la ´unica que permite valorar
“bien” el nuevo contrato con el paradigma de promediar los pagos futuros (descontados).
Por cierto, se trata de una “probabilidad” din´amica, que ir´a cambiando seg´un vayan
llegando nuevas apuestas.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
26

## Página 27

MFC 21-22
Valoraci´on. Fundamentos
Valoraci´on a mercado
Los “mercados” dan ya precio a una gran variedad de instrumentos.
Observaci´on
Pero “mercado”, ¿qu´e es? Depende: (provisionalmente) aquellos instrumentos que tienen precios ﬁrmes, ﬁables,
p´ublicos. . . en los que se puede invertir, comprar/vender, casi sin restricciones de volumen.
Lo que pretenderemos ser´a valorar instrumentos OTC “como si estuvieran en el mercado”
(mark-to-market, mark-to-model, fair value/valor razonable).
Por supuesto, lo que ya est´a en mercado no hace falta valorarlo a mercado.
Al construir un modelo matem´atico formal, estos principios tan toscos se convierten en
ideas mucho m´as exactas de maximizaci´on (de algo) y de equilibrio (de alguna forma).
Sin embargo es aconsejable no olvidar su versi´on m´as imprecisa, por dos razones
opuestas: para acordarnos de no tomar ninguna formalizaci´on matem´atica demasiado
en serio, y para acordarnos de que los principios b´asicos de la econom´ıa no son del todo
est´upidos o poco razonables.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
27

## Página 28

MFC 21-22
Valoraci´on. Fundamentos
Replicaci´on/arbitraje/valoraci´on (relativa)
1. Mercado
Disponemos de una serie de activos, A, B, C, . . . cuyos precios hoy son conocidos, y
con los que se pueden formar carteras.
(Suponemos que no hay l´ımites de compra/venta, ni hay costes de transacci´on, que se
pueden asumir posiciones largas y cortas, etc.)
Asumimos que existe una cartera que es un numerario: tanto su precio como sus posibles
ﬂujos son positivos.
2. Arbitraje
Entendemos por arbitraje una inversi´on en una cartera de coste inicial 0, que tiene ﬂujos
no negativos en todos los escenarios (y en alg´un escenario el ﬂujo es positivo).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
28

## Página 29

MFC 21-22
Valoraci´on. Fundamentos
3. Replicaci´on
Replicar (de manera exacta y est´atica) el activo X con los activos A, B, C, . . . signiﬁca
hallar una cartera de estos ´ultimos de manera que, pase lo que pase (sea cual sea el
escenario que suceda en el futuro), los ﬂujos de la cartera y los ﬂujos de X coincidan.
4. Paradigma de valoraci´on relativa (o por no arbitraje)
La ´unica consideraci´on econ´omica en toda esta modelizaci´on es la asunci´on de que
debemos tener modelos para los que se cumpla la siguiente:
Hip´otesis:
ausencia de oportunidades de arbitraje.
Esta hip´otesis (o exigencia en el modelado) se sustenta en la suposici´on de que los
mercados son eﬁcientes en la gesti´on de informaci´on y no permiten que se generen y
aprovechen oportunidades de arbitraje; o bien que si estas oportunidades aparecieran,
se aprovechar´ıan casi inmediatamente.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
29

## Página 30

MFC 21-22
Valoraci´on. Fundamentos
Consecuencia 1.
Dos carteras que tienen los mismos ﬂujos han de tener el mismo precio hoy.
Observaci´on
Si no fuera as´ı, tomando la diferencia (de las carteras) en el orden adecuado tendr´ıamos una cartera de valor hoy
negativo digamos −A, con A positivo. Y si invirti´eramos A en el numerario tendr´ıamos una cartera de valor hoy cero
que da como ﬂujos los del numerario, que son positivos.
Consecuencia 2. Ley del precio ´unico:
Todo activo replicable tiene un ´unico precio.
Observaci´on
El coste (´unico) de replicar un activo dado (replicable) es el ´unico precio que le podemos asignar (y as´ı lo hacemos)
que no crea oportunidades de arbitraje.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
30

## Página 31

MFC 21-22
Valoraci´on. Fundamentos
Comentarios
Si X se replica con una cartera con α unidades de A, β de B, γ de C, etc., y si no
hay arbitraje, entonces
precio(X)
ha de ser
=
coste de cartera = α·precio(A)+β ·precio(B)+γ ·precio(C)+· · ·
O al rev´es: si el precio de X y el coste de formaci´on de la cartera no coincidieran,
entonces habr´ıa una oportunidad de arbitraje.
Para valorar un activo replicable basta simplemente con obtener la (una) cartera
replicante y calcular su coste de formaci´on hoy.
La valoraci´on de X es relativa (a los precios de A, B,. . . ).
Si el instrumento X cotiza (de alguna manera sensible) entonces, o bien el precio
as´ı calculado coincide con el cotizado, o bien hay (en teor´ıa) una oportunidad de
arbitraje.
Si el instrumento X no cotiza, el precio as´ı obtenido puede considerarse como el
precio que tendr´ıa el instrumento si estuviera en mercado.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
31

## Página 32

MFC 21-22
Valoraci´on. Fundamentos
Ilustraciones de valoraci´on por replicaci´on
Veamos algunos ejemplos de valoraci´on por replicaci´on (exacta) est´atica, en los que
se constituye una cartera al inicio que, sin alteraci´on alguna, es capaz de replicar
exactamente los ﬂujos del activo de inter´es. V´eanse m´as ejemplos en la p´agina 119.
1. Paridad call/put. Una cartera que tiene larga una call y corta una put del mismo
vencimiento y del mismo strike sobre un cierto subyacente replica exactamente un
contrato forward sobre ese subyacente, ese vencimiento y ese mismo strike.
La call larga y la put corta pagar´an en conjunto un ﬂujo incierto y desconocido:
m´ax {S −K; 0} −m´ax {0; K −S}
donde S es el nivel incierto y desconocido del subyacente a vencimiento. Pero, pase
lo que pase, este montante es
S −K ,
que es el ﬂujo del contrato forward. As´ı que
preciocall −precioput = precioforward .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
32

## Página 33

MFC 21-22
Valoraci´on. Fundamentos
2. Contrato forward. El forward con strike K paga ST −K sobre S, que no paga
dividendos. La replicaci´on se obtiene con una acci´on comprada y un bono (de
principal K, cup´on cero y vencimiento T) vendido. Si P(0, T) designa el factor de
descuento a plazo T, el coste hoy de esta replicaci´on exacta es:
S0 −K · P(0, T) .
La replicaci´on tambi´en puede ser din´amica. Es decir, constituimos una cartera al inicio
y dise˜namos un protocolo o estrategia de gesti´on o de inversi´on autoﬁnanciada de esa
cartera que, pase lo que pase, genera exactamente los ﬂujos del activo a replicar.
3. FRA (forward rate agreement) En un contrato FRA (de nominal 100) se acuer-
da
esperar a la ﬁjaci´on, en la fecha T, de un tipo simple R pongamos por caso, a 3
meses: ΔT = 0.25 a˜nos;
y en fecha T + ΔT pagar 100 · (R −K) · ΔT , donde K es el strike.
Los ﬂujos de este contrato son inciertos, pues hoy desconocemos el tipo R a tres
meses que tendremos en tiempo T.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
33

## Página 34

Valoraci´on. Fundamentos
a) Instrumentos de mercado: dos bonos cup´on cero
El primer bono (cup´on cero) es BT, que vence en tiempo T. Si su nominal es Nom,
su precio hoy es Nom · P(0, T).
El segundo bono (cup´on cero), BT +ΔT, vence en tiempo T + ΔT. Si su nominal es
Nom, su precio hoy es Nom · P(0, T + ΔT).
b) Cartera y gesti´on
Formamos la siguiente cartera:
Compramos bono BT de nominal 100;
Vendemos bono BT +ΔT con nominal 100 · (1 + KΔT).
Y especiﬁcamos el siguiente protocolo de gesti´on:
En tiempo T, el nominal 100 del bono BT que se recibe entonces se prestar´a a tipo R
durante un trimestre.
El coste (hoy) de formaci´on de esta cartera:
costecartera = 100 · P(0, T) −100 · (1 + ΔT K) · P(0, T + ΔT).
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
34

## Página 35

Valoraci´on. Fundamentos
c) Flujos de la cartera (en tiempo T + ΔT)
Tras tiempo T, tenemos 100 de contado, procedentes del primer bono (y prestamos esa
cantidad al tipo simple que se ﬁje entonces), y seguimos teniendo el segundo bono.
En tiempo T + ΔT, el ﬂujo es
100 · (1 + ΔT R) −100 · (1 + ΔT K) = 100 · ΔT · (R −K),
que coincide (en cualquier escenario) con el ﬂujo del FRA.
d) Valoraci´on del FRA
Si admitimos que no hay oportunidades de arbitraje, el precio (hoy) del FRA ha de
coincidir con el coste de formaci´on de la cartera de bonos.
Si por ejemplo queremos que el precio del FRA sea 0, entonces K ha de ser
K =
1
ΔT

P(0, T)
P(0, T + ΔT) −1

,
tipo (simple) que llamar´ıamos el tipo impl´ıcito (visto hoy) para el periodo T →T +ΔT.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
35

## Página 36

Valoraci´on. Fundamentos
4. Activo no replicable (est´aticamente)
-4
-2
0
2
4
6
8
10
12
90
95
100
105
110
115
subyacente
cartera; alpha=0,47 beta=-43
call; strike=103
El ejemplo b´asico de instrumento no replicable
es una call (digamos a 1 a˜no ATM forward, es
decir, con strike S0(1+r)) usando como activos
b´asicos dinero y subyacente. Si invertimos α
en el subyacente y β en dinero, a vencimiento
tendremos
αS0 + β −→αS + β(1 + r)
donde S0 es la cotizaci´on hoy, r es el tipo a 1
a˜no, y S es la cotizaci´on desconocida de tiempo 1. Mientras que para ese valor de S, la
call paga
m´ax

S −S0(1 + r); 0

En t´erminos de S, la cartera es una recta, mientras que la call es una l´ınea quebrada.
En este caso, necesitaremos imponer un modelo para la evoluci´on del subyacente (y
tanto la replicaci´on como la valoraci´on depender´an del modelo elegido).
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
36

## Página 37

Valoraci´on. Fundamentos
3. Modelo matricial de un s´olo periodo de tiempo:
planteamiento
c Aﬁ Escuela de Finanzas. Todos los derechos reservados
37

## Página 38

Valoraci´on. Fundamentos
Vamos a exhibir a continuaci´on los ingredientes de nuestro primer modelo (un solo
periodo de tiempo, modelo matricial):
escenarios;
activos;
carteras.
Adem´as, explicaremos qu´e son y c´omo se calculan, en este marco,
las carteras replicantes;
las oportunidades de arbitraje.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
38

## Página 39

Valoraci´on. Fundamentos
Escenarios. Tiempos e incertidumbre
En este modelo matricial de mercado ﬁnanciero, el tiempo desempe˜na un papel menor:
s´olo hay dos instantes de tiempo, que convencionalmente denotaremos por t = 0 y
por t = 1.
S´olo hay transacciones en esos dos instantes de tiempo.
En tiempo t = 0 no hay incertidumbre, todo es conocido.
Pero los valores/ﬂujos de los activos en tiempo t = 1 son inciertos.
En tiempo t = 1 se liquida la cartera, de manera que identiﬁcaremos los ﬂujos en
tiempo t = 1 con sus valores.
La incertidumbre se codiﬁca con un conjunto Ω de N escenarios/estados posibles:
Ω = {ω1, ω2, . . . , ωN}
Ω es el espacio muestral de escenarios/estados.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
39

## Página 40

Valoraci´on. Fundamentos
Activos
1.- Activos b´asicos
Tenemos M activos, que se pueden comprar y vender en tiempo t = 0 y comprar y
vender en tiempo t = 1. Estos activos b´asicos se representan como:
S1, S2, . . . , SM
Los valores de estos activos son n´umeros reales, positivos o negativos (posiciones
largas/cortas, posiciones a favor/en contra)
Estos activos b´asicos ser´an, junto con las carteras que podamos formar con ellos, nuestro
mercado de referencia.
Los activos b´asicos del modelo dependen de los instrumentos que nos pueda interesar
analizar. Como ilustraci´on, los activos b´asicos podr´ıan ser acciones, incorporando adem´as
el dinero o el bono cup´on cero de nominal (sin riesgo de cr´edito) que vence en
tiempo t = 1.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
40

## Página 41

Valoraci´on. Fundamentos
Tiempo t = 0. Los activos en tiempo 0 valen
S0
1, S0
2, . . . , S0
M .
Son datos conocidos. No hay diferencial bid/ask. Exigimos desde el principio que el
modelo arranque con los valores de mercado (cotizados) de los activos b´asicos.
Tiempo t = 1. Los activos en tiempo t = 1 tienen valores inciertos. Denotamos los
valores de estos activos en esos estados por:
S1
i (ωj) = valor (en tiempo t = 1) del activo i en el estado ωj.
Observaci´on
Identiﬁcamos los activos con la lista de ﬂujos/valores que alcanzan en los distintos escenarios.
Observaci´on
Mantendremos en lo que sigue la notaci´on de que hay N escenarios y M activos.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
41

## Página 42

Valoraci´on. Fundamentos
Conviene considerar a cada S1
i como un vector de RN que recoge sus valores en los N
escenarios:
S1
i ↭

S1
i (ω1), S1
i (ω2), . . . , S1
i (ωN)

En total tenemos M vectores en RN, uno por cada activo b´asico.
Podemos registrar la informaci´on sobre valores de los activos en tiempo t = 1 en una
matriz de M ﬁlas (tantas como activos) y N columnas (tantas como estados):
S =

S1
i (ωj)
i = 1, 2, . . . , M
j = 1, 2, . . . , N

S =
⎛
⎜
⎜
⎝
S1
1(ω1)
S1
1(ω2)
· · ·
S1
1(ωN)
S1
2(ω1)
S1
2(ω2)
· · ·
S1
2(ωN)
...
...
...
...
S1
M(ω1)
S1
M(ω2)
· · ·
S1
M(ωN)
⎞
⎟
⎟
⎠
S1
S2...
SM
ω1
ω2
· · ·
ωN
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
42

## Página 43

Valoraci´on. Fundamentos
ejemplo base
En lo que sigue, argumentaremos e ilustraremos las sucesivas nociones que ir´an apareciendo
con este modelo, en el que tenemos
cuatro escenarios ω1, . . . , ω4 y cuatro activos, S1, . . . , S4.
La informaci´on sobre los valores de estos activos en cada uno de los escenarios se codiﬁca con la
siguiente matriz:
S =
⎛
⎜
⎜
⎝
2
1
1.5
2
−4
2
−1
1
5
1
1.5
4
3.5
0
2
1.5
⎞
⎟
⎟
⎠
S1
S2
S3
S4
ω1
ω2
ω3
ω4
Por ejemplo, el activo S3 toma el valor 1 en el escenario ω2.
Adem´as, en tiempo t = 0 tenemos el siguiente vector de precios:
S1
S2
S3
S4
⎛
⎜
⎜
⎝
1.5
0.3
2.5
1.3
⎞
⎟
⎟
⎠
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
43

## Página 44

Valoraci´on. Fundamentos
2.- Activos generales
Un activo (general) es un instrumento X que en tiempo t = 1 tiene ﬂujos/valores dados
en cada escenario: X(ωj), j = 1, . . . , N. Un activo es, pues, un vector arbitrario en RN:
X ↭

X(ω1), X(ω2), . . . , X(ωN)

De nuevo, identiﬁcamos un activo con el vector ﬁla de longitud N que contiene sus
valores en tiempo t = 1 en los N escenarios (se identiﬁca X con X). El conjunto de
activos se identiﬁca con el conjunto de vectores de RN.
ejemplo base
Una call X con vencimiento t = 1 (el ´unico posible) sobre S1 y strike 1 y el activo Y que paga el
m´aximo entre S1 y S4 viene representados por los vectores
X ↭

1
0
0.5
1

ω1
ω2
ω3
ω4
Y ↭

3.5
1
2
2

ω1
ω2
ω3
ω4
Observaci´on
El objetivo es usar el modelo para dar precio a activos generales, como X e Y en el ejemplo anterior.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
44

## Página 45

Valoraci´on. Fundamentos
ejemplo. Activos Arrow–Debreu y bonos.
Un par de activos especiales (no necesariamente b´asicos) son:
Los activos Arrow–Debreu. Hay un activo Arrow–Debreu por cada escenario. El
activo ADj (Arrow–Debreu del escenario j) es aquel que, en tiempo t = 1, paga 1
en el escenario ωj y 0 en cualquier otro caso.
ADj(ωk) =

1,
si k = j,
0,
si k ̸= j.
Otro activo especial es el bono D: el activo que paga 1 en tiempo t = 1 pase lo que
pase, en cualquier estado:
D(ωj) = 1,
j = 1, 2, . . . , N
El bono es activo sin riesgo, pues en todos los escenarios da el mismo ﬂujo. Es decir,
pase lo que pase paga lo mismo; no hay incertidumbre.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
45

## Página 46

Valoraci´on. Fundamentos
3.- Carteras de activos b´asicos y de activos generales
Una cartera de inversi´on en los activos b´asicos es un vector que registra las unidades
invertidas en cada activo, es decir, un vector λ = (λ1, λ2, . . . , λM)T en RM.
Convencionalmente lo denotamos por un vector columna de longitud M (por eso
aparece el s´ımbolo de traspuesta en la ﬁla denotando λ).
Para una cartera de inversi´on λ = (λ1, . . . , λM)T, deﬁnimos su proceso de valor Vλ
como
Vλ =
M

i=1
λi Si .
En tiempo t = 0
Y en tiempo t = 1
el valor (coste) de la cartera es
es la variable (depende del escenario)
V 0
λ =
M

i=1
λi S0
i .
V 1
λ(ωj) =
M

i=1
λi S1
i (ωj),
j = 1, 2, . . . , N .
Dos carteras de inversi´on que tienen los mismos ﬂujos en tiempo t = 1 son, a todos los
efectos, indistinguibles y equivalentes.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
46

## Página 47

Valoraci´on. Fundamentos
Carteras de activos generales
Asimismo se pueden formar carteras de activos generales.
N´otese, por ejemplo, que el bono es una cartera de Arrow–Debreu:
D =
N

j=1
ADj ,
en la que los coeﬁcientes son todos 1. De hecho, cualquier activo X es una cartera de
activos AD:
X ≡
N

j=1
X · ADj .
Esto es ´util para valoraci´on (en el esquema matricial y, en general, en cualquier modelo
de valoraci´on), pues, como veremos, reduce la valoraci´on de activos a la valoraci´on de
los activos AD.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
47

## Página 48

Valoraci´on. Fundamentos
4.- Numerarios
Los valores son siempre relativos. Necesitaremos comparar valores de tiempos distintos,
y para ello expresar los valores en unidades homog´eneas. Lo m´as habitual es utilizar el
dinero como comparaci´on temporal, pero no tiene por qu´e ser as´ı. Podemos usar otros
activos para esa comparaci´on. Un numerario N es
un activo b´asico o una cartera de inversi´on en ellos. Es decir, un activo de mercado,
del que se dispone de su precio (en mercado) en tiempo 0 y del que se conoce el
ﬂujo concreto en cada escenario de tiempo t = 1.
Tanto en tiempo t = 0, como en cada escenario de tiempo t = 1, el numerario N
tiene valor positivo (no nulo).
Supondremos que el modelo tiene un numerario.
ejemplo base
Podemos tomar como numerario N, por ejemplo, a la cartera 3S1 + S2:
N0 = 4.8
N1 = (2, 5, 3.5, 7)
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
48

## Página 49

Valoraci´on. Fundamentos
Elecciones habituales:
El numerario m´as habitual es el bono, el activo D, que suele aparecer como uno de
los activos b´asicos.
Tambi´en es habitual tomar como numerario la cuenta bancaria, que vale 1 en el
instante inicial t = 0 y vale 1 + r en cualquier estado de tiempo t = 1.
Pero puede usarse uno cualquiera de los propios activos b´asicos (siempre que se
cumpla la condici´on de positividad).
M´as adelante comprobaremos cu´an ´util ser´a usar distintos numerarios e incluso cambiar
de un numerario de referencia a otro dentro de un modelo.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
49

## Página 50

Valoraci´on. Fundamentos
Replicaci´on con activos b´asicos
Un activo X es replicable con los activos b´asicos si hay una cartera de inversi´on
λ = (λ1, . . . , λM)T en ellos que genera exactamente el mismo ﬂujo en cada uno de los
escenarios de tiempo t = 1.
La cartera de replicaci´on o replicante λ tiene los mismos ﬂujos que X en todos y cada
uno de los escenarios (pagan lo mismo, pase lo que pase).
C´alculo de una cartera replicante
El activo X tiene ﬂujos (X(ω1), . . . , X(ωN)). Cada escenario supone una condi-
ci´on/ecuaci´on, y por tanto, la replicaci´on se expresa como un sistema de ecuaciones:
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎩
λ1 S1
1(ω1) + λ2 S1
2(ω1) + · · · + λM S1
M(ω1) = X(ω1)
(condici´on en escenario ω1)
λ1 S1
1(ω2) + λ2 S1
2(ω2) + · · · + λM S1
M(ω2) = X(ω2)
(condici´on en escenario ω2)
...
...
λ1 S1
1(ωN) + λ2 S1
2(ωN) + · · · + λM S1
M(ωN) = X(ωN)
(condici´on en escenario ωN)
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
50

## Página 51

MFC 21-22
Valoraci´on. Fundamentos
Que, en notaci´on matricial, se expresa:
(λ1, . . . , λM) ·
⎛
⎜
⎜
⎝
S1
1(ω1)
S1
1(ω2)
· · ·
S1
1(ωN)
S1
2(ω1)
S1
2(ω2)
· · ·
S1
2(ωN)
...
...
...
...
S1
M(ω1)
S1
M(ω2)
· · ·
S1
M(ωN)
⎞
⎟
⎟
⎠= (X(ω1), X(ω2), . . . , X(ωN))
es decir,
X = λT · S
As´ı que
averiguar si un activo es replicable es averiguar si el sistema anterior tiene soluci´on;
y calcular la cartera de replicaci´on consiste en obtener una soluci´on del sistema.
Obs´ervese que en estas dos cuestiones de replicaci´on no intervienen los valores de los
activos b´asicos en tiempo t = 0.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
51

## Página 52

MFC 21-22
Valoraci´on. Fundamentos
Replicabilidad de activos. Mercados completos
Dado un modelo, un activo puede
no ser replicable con los activos b´asicos;
ser replicable con m´as de una cartera;
o ser replicable con una ´unica cartera.
Si todos los activos del modelo son replicables, se dice que el modelo es completo.
ejemplo base
En modelo base S =
⎛
⎜
⎜
⎝
2
1
1.5
2
−4
2
−1
1
5
1
1.5
4
3.5
0
2
1.5
⎞
⎟
⎟
⎠, todos los activos son replicables y adem´as de una ´unica
manera, porque, como det S ̸= 0, esa ´unica cartera replicante de un X dado viene dada por
λT = X · S−1 .
Compru´ebese, por ejemplo (con la resoluci´on matricial expl´ıcita o usando solver), que la cartera
de replicaci´on del activo AD1 es λ = (2, −1, 0, −2)T.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
52

## Página 53

MFC 21-22
Valoraci´on. Fundamentos
Ilustraci´on
Consid´erese el modelo S =
⎛
⎝
2
1
1.5
2
−4
2
−1
1
5
1
1.5
4
⎞
⎠. Hay 3 activos b´asicos, que no pueden generar el espacio total de
activos, que tiene 4 dimensiones.
• Comprobar (solver) que el activo X = (−2, 3, 0.5, 3) es replicable. De hecho, es equivalente. . . ¿a?
• Comprobar (solver?) que el activo X = (3.5, 0, 2, 1.5) no es replicable.
Ilustraci´on
Consid´erese el modelo S =
⎛
⎜
⎜
⎝
2
1
1.5
−4
2
−1
5
1
1.5
3
4
−1
⎞
⎟
⎟
⎠. Hay 4 activos b´asicos, y s´olo 3 escenarios.
• Comprobar (solver) que los tres activos AD son replicables. Por tanto, todo activo es replicable.
• Comprobar (solver) que para replicar el activo X = (6, 8, 1), por ejemplo, podemos ﬁjar λ1, y escoger los
restantes λ2, λ3, λ4. Comprobar que, por ejemplo (1, 1, 1, 1)T y (−4, 4.5, 7, −1)T son carteras que replican X.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
53

## Página 54

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
Notas matriciales. En el modelo matricial, todo lo relacionado con replicabilidad (o no) son cuestiones sobre resoluci´on
de sistemas de ecuaciones:
1.- El activo X es replicable si y s´olo si
rango
S
X

= rango

S

,
donde

 S
X

es la matriz que se forman adjuntando a S la ﬁla X al ﬁnal.
2.- El mercado es completo si y s´olo si
rango(S) = N.
3.- Los activos replicables tiene replicaci´on ´unica si y s´olo si
rango(S) = M.
4.- En el caso especial en que hay tantos activos como escenarios: M = N, la condici´on de completitud equivale a que
det(S) ̸= 0.
En este caso adem´as para cada activo X hay una sola cartera replicante λ dada por
λT = X · S−1 .
Y la matriz S−1 contiene las carteras replicantes de los activos de Arrow–Debreu.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
54

## Página 55

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
N´umero de activos b´asicos y n´umero de escenarios.
• Para que el modelo sea completo hace falta que haya al menos tantos activos b´asicos como escenarios. Pero puede
que el modelo no sea completo a´un cuando haya m´as activos b´asicos que escenarios, porque los activos b´asicos pueden
ser redundantes.
• Para que la replicaci´on (de lo replicable) sea ´unica hace falta que haya al menos tantos escenarios como activos. Pero
que haya m´as escenarios que activos b´asicos no garantiza la replicaci´on ´unica.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
55

## Página 56

MFC 21-22
Valoraci´on. Fundamentos
Oportunidades de arbitraje
Una oportunidad de arbitraje con los activos b´asicos es una cartera que tiene
un valor de 0 en t = 0;
y que en tiempo t = 1 tiene, en todos y cada uno de los escenarios, un valor no
negativo, y en al menos un escenario un valor positivo.
Es decir, hay oportunidad (o cartera) de arbitraje si existen (λ1, . . . , λM) tales que
M

i=1
λiS0
i = 0
y
⎧
⎪
⎨
⎪
⎩
M
i=1 λiS1
i (ωj) ≥0,
para cada j = 1, 2, . . . , N
M
i=1 λiS1
i [ωj] > 0
para alg´un escenario ωj.
ejemplo base
En el ejemplo base, modiﬁcamos los precios hoy: S0
1 = 1, S0
2 = 0, S0
3 = 2 y S0
4 = 1. La cartera
(2, −1, 0, −2)T tiene coste 0 en tiempo t = 0, pero en tiempo t = 1 es justo el activo AD1. As´ı
que tendr´ıamos una oportunidad de arbitraje.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
56

## Página 57

MFC 21-22
Valoraci´on. Fundamentos
Obs´ervese que, en contra de lo que ocurr´ıa con la noci´on de la replicaci´on, en el concepto
de oportunidad de arbitraje s´ı intervienen los valores de los activos b´asicos en t = 0.
N´otese tambi´en que si una cartera da una oportunidad de arbitraje, al multiplicar toda
la cartera por el mismo n´umero positivo, volvemos a tener una cartera de arbitraje.
Ilustraci´on
Para buscar oportunidades de arbitraje en un modelo matricial con solver podemos buscar un vector λ tal que la
cartera asociada cumpla
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎩
V 0
λ = 0
N

i=1
V 1
λ(ωi)2 = 1
con las restricciones de que
V 1
λ(ωi) ≥0,
para cada
i = 1, 2, . . . N
Con la matriz del ejemplo base:
y con precios hoy S0
1 = 1, S0
2 = 0, S0
3 = 2 y S0
4 = 1, hallar con este procedimiento oportunidades de arbitraje.
y con los precios originales: S0
1 = 1.5, S0
2 = 0.3, S0
3 = 2.5 y S0
4 = 1.3, cerciorarse de que no hay oportunidades
de arbitraje.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
57

## Página 58

Valoraci´on. Fundamentos
4. Modelo matricial de un s´olo periodo de tiempo:
valoraci´on
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
58

## Página 59

MFC 21-22
Valoraci´on. Fundamentos
La replicaci´on interesa para valoraci´on:
si un activo (del que tan s´olo conocemos sus ﬂujos) se puede replicar con
activos b´asicos, entonces el coste de una cartera replicante es un coste que
basta para replicar esos ﬂujos. Pero, tal y como hemos visto, podr´ıa haber
varias carteras replicantes.
Pero para dar precios a activos, necesitamos cerciorarnos de que no hay oportunidades
de arbitraje.
ejemplo base
Ya hemos comprobado que el modelo base es completo (p´agina 52). Y al menos num´ericamente
(p´agina 57), tambi´en hemos comprobado que no hay oportunidades de arbitraje. Valorar diversos
activos generales (los Arrow–Debreu, bono, etc.)
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
59

## Página 60

MFC 21-22
Valoraci´on. Fundamentos
Probabilidad de valoraci´on y numerarios
Introducimos aqu´ı el concepto de probabilidad de valoraci´on, que resuelve, conjunta
y eﬁcientemente, varias cuestiones pr´acticas planteadas. Se trata de un truco, casi
m´agico, que simpliﬁca algunas tareas descritas anteriormente (valoraci´on, comprobaci´on
de ausencia de oportunidades de arbitraje, etc.)
N´otese que, hasta ahora, para valorar instrumentos replicables, no hab´ıamos tenido
necesidad de introducir probabilidad alguna en el espacio de escenarios. Y que el
numerario no hab´ıa tenido papel alguno.
Probabilidad
Una probabilidad Q en el espacio de escenarios Ω = {ω1, . . . , ωN} es una ponderaci´on
de los escenarios:
qj = Q(ωj),
j = 1, 2, . . . , N.
Es decir, una colecci´on de n´umeros q1, . . . , qN > 0, cuya suma vale N
j=1 qj = 1.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
60

## Página 61

MFC 21-22
Valoraci´on. Fundamentos
Probabilidad de valoraci´on con respecto a un numerario
Fijamos un activo especial N como numerario. Una probabilidad Q en Ω se dice
probabilidad de valoraci´on respecto de N si
S0
i
N0 = EQ
 S1
i
N1

,
i = 1, 2, . . . , M.
Es decir, si el valor normalizado (con N) de tiempo 0 de cualquier activo b´asico es la
media de los ﬂujos normalizados de tiempo t = 1. Se deduce inmediatamente que, para
cualquier cartera λ = (λ1, . . . , λM)T se tiene asimismo que su proceso de valor cumple
V 0
λ
N0 = EQ
V 1
λ
N1

.
Observaci´on
EQ
 S1
i
N1

=
N

j=1
qj
S1
i (ωj)
N1(ωj)

EQ
V 1
λ
N1

=
N

j=1
qj
M
k=1 λkS1
k(ωj)
N1(ωj)
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
61

## Página 62

MFC 21-22
Valoraci´on. Fundamentos
C´alculo de una probabilidad de valoraci´on
Aceptemos, por ahora, que la noci´on de probabilidad de valoraci´on es relevante y ´util y
planteemos: ¿c´omo hallar una probabilidad de valoraci´on para un numerario dado?
En nuestro modelo, la condici´on de ser probabilidad de valoraci´on es un conjunto de M
ecuaciones (tantas como activos b´asicos):
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎩
S0
1
N0 = q1
S1
1(ω1)
N1(ω1) + · · · + qN
S1
1(ωN)
N1(ωN)
(ecuaci´on para el activo S1)
...
...
S0
M
N0 = q1
S1
M(ω1)
N1(ω1) + · · · + qN
S1
M(ωN)
N1(ωN)
(ecuaci´on para el activo SM)
adem´as de la exigencia de que las probabilidades q1, . . . , qN sean positivas y sumen 1.
⎛
⎜
⎜
⎜
⎜
⎜
⎜
⎝
S0
1
N0
S0
2
N0...
S0
M
N0
⎞
⎟
⎟
⎟
⎟
⎟
⎟
⎠
= 
S ·
⎛
⎜
⎜
⎝
q1
q2...
qN
⎞
⎟
⎟
⎠
Un sistema que se puede intentar resolver num´ericamente (con
solver). O bien algebraicamente. Basta escribirlo en forma
matricial, como hemos hecho a la derecha, donde S = S/N es
la matriz de ﬂujos normalizados en t´erminos del numerario N.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
62

## Página 63

MFC 21-22
Valoraci´on. Fundamentos
Salvo por la condici´on de que los qj sean probabilidades, el que el sistema tenga soluci´on
(una, muchas o ninguna) depender´a de si el rango de S es menor o mayor que N.
En el caso especial en el que N = M (y det(S) ̸= 0), la resoluci´on es, simplemente,
⎛
⎜
⎜
⎜
⎜
⎝
S0
1
N0
S0
2
N0...
S0
N
N0
⎞
⎟
⎟
⎟
⎟
⎠
= S ·
⎛
⎜
⎜
⎝
q1
q2...
qN
⎞
⎟
⎟
⎠
=⇒
⎛
⎜
⎜
⎝
q1
q2...
qN
⎞
⎟
⎟
⎠= S−1 ·
⎛
⎜
⎜
⎜
⎜
⎝
S0
1
N0
S0
2
N0...
S0
N
N0
⎞
⎟
⎟
⎟
⎟
⎠
Se puede comprobar (v´ease la p´agina 150) que, como el numerario es una cartera de
activos b´asicos, la condici´on de sumar 1 est´a garantizada.
Pero puede ocurrir que al resolver el sistema, los qj resultantes no sean todos positivos.
Eso querr´a decir que no hay probabilidad de valoraci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
63

## Página 64

MFC 21-22
Valoraci´on. Fundamentos
ejemplo base
Compru´ebese que, si consideramos el numerario N = S1, la probabilidad Q dada por
Q(ω1) = 13.33 % ,
Q(ω2) = 18.75 % ,
Q(ω3) = 21.25 % ,
Q(ω4) = 46.67 %
es probabilidad de valoraci´on respecto de N.
ejemplo base
Compru´ebese usando solver que si en el modelo base consideramos el numerario N = S1, pero
con precios iniciales:
S0
1 = 1,
S0
2 = 0,
S0
3 = 2
y
S0
4 = 1 ,
no hay probabilidad de valoraci´on respecto de N.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
64

## Página 65

MFC 21-22
Valoraci´on. Fundamentos
Relevancia de la probabilidad de valoraci´on
Si para un numerario tenemos una probabilidad de valoraci´on asociada, entonces
1.- En el modelo no hay oportunidades de arbitraje.
Y, por tanto, podremos aplicar el principio de valoraci´on por replicaci´on. Este criterio
resuelve la diﬁcultad aparente de comprobar que no hay oportunidades de arbitraje.
Observaci´on
detalle. Si una cartera λ es de arbitraje, entonces su valor en tiempo t = 0 es
V 0
λ = 0
y por tanto
V 0
λ
N0 = 0.
Pero como en tiempo t = 1 sus valores son no negativos, en alg´un escenario es positivo y Q da probabilidad positiva a
todos los escenarios, tendr´ıamos que
EQ
V 1
λ
N1

> 0
=⇒
V 0
λ
N0 ̸= EQ
V 1
λ
N1

,
que contradice que Q sea probabilidad de valoraci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
65

## Página 66

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
Determinar una probabilidad de valoraci´on requiere resolver un cierto sistema de ecuaciones (tantos como activos
b´asicos) y con tantas inc´ognitas como escenarios en el que hay ciertas restricciones (positividad y suma igual a 1).
Es un problema abordable.
Mientras que, con la propia deﬁnici´on de oportunidad de arbitraje, comprobar que no hay oportunidades de arbitraje
requiere dar un argumento que compruebe que para cualquier cartera imaginable no se tiene arbitraje.
Observaci´on
En realidad, se trata de una equivalencia:
Ausencia de oportunidades de arbitraje
⇐⇒
Existencia de probabilidad de valoraci´on
´Este es el contenido del teorema fundamental de valoraci´on. V´ease el detalle en la p´agina 142.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
66

## Página 67

MFC 21-22
Valoraci´on. Fundamentos
2.- El valor del activo (replicable) X que en tiempo t = 1 tiene ﬂujos X1 es (ha de ser)
X0
N0 = EQ
X1
N1

Aunque el c´alculo depende del numerario y de la probabilidad de valoraci´on, el resultado,
el valor de la cartera replicante, s´olo depende de (los ﬂujos de) X. El detalle del
argumento va como sigue: si λ es cartera replicante del activo X,

X0 no arbitraje
=
V 0
λ
probabilidad de valoraci´on
N0 · EQ
X1
N1
 replicaci´on
=
N0 · EQ
V 1
λ
N1

Observaci´on
Disponer de una probabilidad Q de valoraci´on permite calcular precios eﬁcientemente de cualquier activo replicable
siguiendo el paradigma de valoraci´on relativa, por replicaci´on, sin necesidad de calcular las distintas carteras replicantes,
tan s´olo sabiendo que se puede hacer.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
67

## Página 68

MFC 21-22
Valoraci´on. Fundamentos
3.- En la pr´actica se construyen modelos “certiﬁcables”de valoraci´on
1. decidiendo activos b´asicos;
2. especiﬁcando escenarios y determinando valores/ﬂujos de los activos b´asicos;
3. y determinando el numerario y la probabilidad de valoraci´on.
ejemplo base
Calc´ulese el valor de cualquier activo
calculando la cartera replicante, y su valor en tiempo t = 0;
con la probabilidad de valoraci´on respecto del numerario N = S1 y compru´ebese que coinciden.
Obt´engase la probabilidad de valoraci´on correspondiente al numerario N = 3S1 + S2, calc´ulese el
valor usando esta probabilidad y compru´ebese que coincide con los dos anteriores.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
68

## Página 69

MFC 21-22
Valoraci´on. Fundamentos
Cambio de numerario
Digamos que, para un cierto numerario N, tenemos ya calculada una probabilidad de
valoraci´on asociada, que denotamos por QN.
Ahora ﬁjamos otro numerario M. Queremos calcular una probabilidad de valoraci´on
asociada, digamos QM, a partir de QN y de la relaci´on entre los numerarios N y M).
• C´omo expresar QM a partir de QN.
Obs´ervese que, para cualquier cartera de inversi´on λ en los activos b´asicos, tendr´ıa que
darse que
M0 EQM
 V 1
λ
M1

= V 0
λ = N0 EQN
V 1
λ
N1

Para garantizar que esto va a cumplirse podemos deﬁnir QM mediante:
QM(ωj) =
M1(ωj)
M0
N0
N1(ωj)

QN(ωj)
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
69

## Página 70

MFC 21-22
Valoraci´on. Fundamentos
´Esta es la ecuaci´on de cambio de numerario: dados dos numerarios, podemos obtener la
probabilidad de uno a partir de una probabilidad de valoraci´on del otro.
Detalle:
N0 EQN
V 1
λ
N1

= N0
N

j=1
QN(ωj) V 1
λ(ωj)
N1(ωj) = M0
N

j=1
N0
M0
M1(ωj)
N1(ωj) QN(ωj)



=QM(ωj)
V 1
λ(ωj)
M1(ωj)
• C´omo pasar de valoraciones con QN a valoraciones con QM.
Con la deﬁnici´on de QM anterior, se tiene m´as que, para cualquier activo X (replicable),
X0 = M0 EQM
 X1
M1

= N0 EQN
X1
N1

.
ejemplo base
Ilustraci´on del cambio de numerario con N = S1 y M = 3S1 + S2.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
70

## Página 71

MFC 21-22
Valoraci´on. Fundamentos
Mercados completos
1. El modelo de mercado se dice completo cuando todos los activos posibles sobre el
espacio de escenarios Ω son replicables.
2. El modelo es completo cuando (y s´olo cuando) los activos de Arrow–Debreu son
replicables con los activos b´asicos.
3. Si el mercado es completo, comprobar que no hay oportunidades de arbitraje equivale
a cerciorarse de que los precios de los activos de Arrow–Debreu son positivos.
Observaci´on
(1) En t´erminos de la matriz S, la completitud equivale a que rango(S) = N = n´umero de escenarios.
(2) Basta recordar que los AD permiten replicar cualquier otro activo.
(3) Supongamos que los precios de todos los Arrow–Debreu son positivos. El mercado es completo. Todo activo X se
escribe como 
j αj ADj. Si X tiene en tiempo t = 1 ﬂujos no negativos (y alguno positivo), entonces los αj son
todos no negativos (y alguno es positivo), y el precio de X ha de ser positivo, excluyendo la posibilidad de que sea una
oportunidad de arbitraje. Rec´ıprocamente, si el precio de un cierto ADj fuera 0, ya ser´ıa una oportunidad de arbitraje.
Si fuera negativo, digamos −A, con A positivo, entonces invirtiendo A en el numerario tendr´ıamos una cartera de
precio hoy 0, pagos no negativos, y que al menos en el escenario j pagar´ıa positivo: una oportunidad de arbitraje.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
71

## Página 72

MFC 21-22
Valoraci´on. Fundamentos
4. En modelos de mercado completos, y bajo la hip´otesis de ausencia de oportunidad
de arbitraje, para cada numerario N hay una ´unica probabilidad de valoraci´on QN.
De hecho, esa probabilidad QN est´a impl´ıcita los precios de (ciertos) activos.
Observaci´on
Los ADj son activos replicables (mercado completo) y sus precios hoy son los respectivos costes de las carteras de
r´eplica (no hay arbitrajes). Si Q es de valoraci´on bajo N, estos precios, para j = 1, . . . , N, se pueden calcular
mediante:
AD0
j = N0 EQ
AD1
j
N1

= N0 Q(ωj)
N1(ωj)

=⇒
Q(ωj) = AD0
j ·
N1(ωj)
N0

Es decir, la probabilidad de valoraci´on viene dada por precios hoy y el numerario. ¡Es ´unica! Podemos poner: QN.
En el ejemplo matricial, si el mercado es completo y N = M, los precios de los Arrow–Debreu vienen dados por:
⎛
⎜
⎝
AD0
1
...
AD0
N
⎞
⎟
⎠= S−1 ·
⎛
⎜
⎝
S0
1...
S0
N
⎞
⎟
⎠
Una vez obtenida QN, disponemos de una f´ormula para valorar cualquier activo X.
ejemplo base
Obtener por este procedimiento la probabilidad de valoraci´on y la valoraci´on de cualquier activo.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
72

## Página 73

MFC 21-22
Valoraci´on. Fundamentos
Mercados no completos. Activos no replicables. Cotas
Consideramos un modelo de mercado con activos b´asicos (S1, . . . , SM). Suponemos que
no hay oportunidades de arbitraje.
En general, este modelo no ser´a completo; es decir, no se podr´an replicar todos los
instrumentos (ﬂujos en escenarios) posibles.
De manera que no podremos dar precio (indiscutible) a todos los activos, y habremos
de conformarnos con cotas para los precios, es decir, intervalos que contengan al precio.
• En un mercado no completo y sin oportunidades de arbitraje, para un numerario dado
hay m´as de una probabilidad de valoraci´on Q.
(V´eanse detalles en la p´agina 123).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
73

## Página 74

MFC 21-22
Valoraci´on. Fundamentos
Supongamos que hemos ﬁjado un numerario N y que estamos manejando una probabi-
lidad Q de valoraci´on asociada. A cada activo X podemos asignarle el “precio”
N0 × EQ
X1
N1

.
Si X es replicable, este precio ser´a incontestable;
y si no lo es, al menos es un “precio” dentro del rango razonable (por no arbitraje).
En pr´actica habitual, se ﬁja un numerario y de entre la colecci´on de probabilidades Q
que valoran consistentemente los instrumentos b´asicos, se escoge una probabilidad Qesp
que posea algunas otras propiedades que la hagan especialmente manejable.
N´otese c´omo la elecci´on de Qesp es lo mismo que determinar un procedimiento de
interpolaci´on para establecer los precios de lo no replicable: una suerte de mid entre el
rango bid-ask de sub- y super-replicaci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
74

## Página 75

MFC 21-22
Valoraci´on. Fundamentos
Ejemplo. Consideremos el siguiente modelo de mercado (3 activos y 4 escenarios):
⎛
⎝
S0
1
S0
2
S0
3
⎞
⎠=
⎛
⎝
0.9500
0.4750
0.7125
⎞
⎠,
S =
⎛
⎝
1
1
1
1
1
1
0
0
1
1
1
0
⎞
⎠
S1
S2
S3
ω1
ω2
ω3
ω4
Los precios en tiempo t = 0 aparecen a la izquierda.
a) Replicaci´on. Los ﬂujos de los activos en los dos primeros escenarios coinciden. As´ı que
solo se podr´an replicar los activos que den el mismo ﬂujo en los dos primeros escenarios.
Por ejemplo, los Arrow–Debreu AD3 y AD4 pueden replicarse (con (λ1, λ2, λ3) =
(0, −1, 1) y (λ1, λ2, λ3) = (1, 0, −1), respectivamente). Pero no as´ı AD1 y AD2.
b) Probabilidad de valoraci´on. Tomemos como numerario N = S1. Entonces, por
ejemplo, la probabilidad
Q(ω1) = Q(ω2) = Q[ω3] = Q[ω4] = 25 %
es de valoraci´on. Es decir, no hay arbitraje con los activos b´asicos.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
75

## Página 76

MFC 21-22
Valoraci´on. Fundamentos
Pero, de hecho, hay inﬁnitas probabilidades de valoraci´on para N. La probabilidad Q
ser´a de valoraci´on siempre que
Q(ω1) + Q(ω2) = 50 %;
Q[ω3] = 25 %;
Q[ω4] = 25 % .
c) Valoraci´on. El activo X que paga X = (1, 2, 0, 0) no es replicable. Dada un Q de
valoraci´on para el numerario N, la valoraci´on de X es
N0 × EQ
X1
N1

= 0.95 ·

Q[ω1] + 2 Q[ω2]

= 0.95

u + 2 · (1
2 −u)

,
donde hemos escrito Q[ω1] = u y hemos usado que Q[ω1] + Q[ω2] = 1/2.
Los posibles precios que se obtienen al variar u
entre 0 y 1/2
0
0,1
0,2
0,3
0,4
0,5
0,6
0,7
0,8
0,9
1
0%
5%
10%
15%
20%
25%
30%
35%
40%
45%
50%
Valores de X
valores de u
est´an entre 0.475 y 0.95. V´ease la
ﬁgura. Este rango de precios no genera arbitrajes.
Si escogemos como probabilidad (de valoraci´on)
Qesp la que asigna igual probabilidad a ω1 y ω2
(u = 25 %) entonces obtenemos el valor 0.7125,
una suerte de mid.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
76

## Página 77

Valoraci´on. Fundamentos
5. Modelo de varios periodos:
planteamiento
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
77

## Página 78

MFC 21-22
Valoraci´on. Fundamentos
Evoluciones en el tiempo: no arbitraje y martingalas
Hasta ahora hemos tratado un modelo simpliﬁcado con dos instantes de tiempo: “hoy”
y el “futuro”. Ahora vamos ahora a considerar evoluciones en el tiempo. De nuevo
establecemos un marco conceptual general:
hay una serie de variables b´asicas cuyos valores (en sucesivos instantes de tiempo)
determinan el universo ﬁnanciero. Estas variables pueden ser precios de activos, tipos
de inter´es, ratings, resultados de sorteos de una ruleta, valores de brownianos. . .
En cada instante de tiempo, tenemos una serie de estados. En cada uno de ellos, las
variables b´asicas tienen un cierto valor. Estos valores (en ese instante de tiempo y en
ese estado) determinan los de las dem´as variables de inter´es.
Determinar un escenario consiste en decidir cu´al es la sucesi´on de estados que se
producen en el tiempo.
Una probabilidad Q asigna probabilidades a cada uno de estos escenarios. Y en
particular contiene la informaci´on sobre: probabilidades de estar en un cierto estado
en un determinado instante de tiempo, probabilidades de transici´on entre estados de
tiempos sucesivos, etc.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
78

## Página 79

MFC 21-22
Valoraci´on. Fundamentos
Formalizamos.
Espacio de escenarios
Tenemos nuestro espacio de escenarios: Ω = {ω1, ω2, . . . , ωN}.
Estructura de tiempos
Tenemos tiempos t0 = 0, t1, t2, . . . , tH = T .
(T = tH es el horizonte temporal)
t1
t2
t3
t4
t5



estados en tiempo t5
escenario ω
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
79

## Página 80

MFC 21-22
Valoraci´on. Fundamentos
En esta secci´on, utilizaremos como gu´ıa el siguiente
ejemplo base
S´olo hay dos tiempos t1 y t2 (adem´as de t0 = 0).
En tiempo t1 tenemos tres estados, que etiquetamos con a, b y c.
En tiempo t2 hay otros tres estados, que rotulamos con 1, 2 y 3.
Representamos las 9 posibles evoluciones en un ´arbol:
t1
t2
a
b
c
1
2
3
7
-
w
-
-
j
*
j
*
-
j
*
a
b
c
(a, 1)
(a, 2)
(a, 3)
(b, 2)
(b, 1)
(b, 3)
(c, 1)
(c, 2)
(c, 3)
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
80

## Página 81

MFC 21-22
Valoraci´on. Fundamentos
Flujo de informaci´on
Con el paso del tiempo disponemos de cada vez m´as informaci´on sobre la evoluci´on
de los activos y de sus ﬂujos. Modelamos este ﬂujo de informaci´on con unas variables
discretas Y1, Y2, . . . , YH, que llamaremos variables de estado, una por cada tiempo de
t = t1 hasta t = tH, deﬁnidas en el espacio de escenarios:
F1 = σ(Y1) recoge aquellos eventos en Ω que son expresables en t´erminos de Y1,
F2 = σ(Y1, Y2) recoge aquellos eventos en Ω que son expresables en t´erminos de Y1, Y2,
...
Fk = σ(Y1, Y2, . . . , Yk) recoge los eventos en Ω expresables en t´erminos de Y1, Y2, . . . , Yk,
...
FH = σ(Y1, Y2, . . . , YH) recoge los eventos en Ω expresables en t´erminos de Y1, Y2, . . . , YH,
Adem´as, FH = σ(Y1, Y2, . . . , YH) es ya todo Ω. Es decir, al conocer todas los valores
de las variables Y1, Y2, . . . , YH queda completamente desvelado el escenario completo.
En otros t´erminos, cuando conocemos parcialmente, s´olo hasta tiempo tk, la sucesi´on
de valores Y1, Y2, . . . , Yk se conoce parcialmente el escenario: es la informaci´on hasta
Fk del escenario.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
81

## Página 82

MFC 21-22
Valoraci´on. Fundamentos
ejemplo base
La variable Y1 toma los valores a, b, c y la variable Y2 los valores 1, 2, 3. El espacio de escenarios
Ω queda entonces registrado por pares de valores (a, 1), (a, 2), . . . , (c, 3). Hay un total de 9
escenarios.
7
-
w
-
-
j
*
j
*
-
j
*
a
b
c
(a, 1)
(a, 2)
(a, 3)
(b, 2)
(b, 1)
(b, 3)
(c, 1)
(c, 2)
(c, 3)
escenarios
F1 tiene tres eventos b´asicos:
• Y1 = a (escenarios {(a, 1), (a, 2), (a, 3)});
• Y1 = b (escenarios {(b, 1), (b, 2), (b, 3)});
• Y1 = c (escenarios {(c, 1), (c, 2), (c, 3)}); .
Cuando se desvele el valor de Y1, digamos Y1 = a, conoceremos los
valores de los activos en t = t1, que depender´an de que se haya dado
ese valor de Y1 = a.
Cuando, despu´es, se desvele Y2, digamos Y2 = 2, quedar´a determina-
do todo el escenario de futuro, y conoceremos la evoluci´on completa de
todos los activos. A cada escenario corresponde una senda de valores
de los activos. F2 tiene nueve eventos b´asicos, que ya es todo Ω.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
82

## Página 83

MFC 21-22
Valoraci´on. Fundamentos
1. Activos b´asicos
Tenemos M activos b´asicos: S1, S2, . . . , SM. Cada uno de estos activos es un proceso
en el tiempo. La sucesi´on de variables
Stk
i ,
k = 0, 1, 2, . . . , H
recoge los valores del activo Si en los sucesivos tiempos tk, k = 0, 1, 2, . . . , H
Como es natural, Stk
i
es de Fk. Es decir, se ha de poder expresar en t´erminos de
Y1, Y2, . . . , Yk. En otras palabras, los valores de Si en tiempo tk dependen exclusivamente
de la informaci´on disponible en tiempo tk.
Usamos la notaci´on
Stk
i (ωj)
es el valor del activo
Si
en tiempo
tk
en el escenario
ωj
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
83

## Página 84

MFC 21-22
Valoraci´on. Fundamentos
ejemplo base
Recordemos que las variables de estado Y1 e Y2 toman valores
{a, b, c} y {1, 2, 3}, respectivamente. El espacio Ω = F2 consta
de nueve escenarios: (a, 1), (a, 2), . . . , (c, 3).
7
-
w
-
-
j
*
j
*
-
j
*
a
b
c
(a, 1)
(a, 2)
(a, 3)
(b, 2)
(b, 1)
(b, 3)
(c, 1)
(c, 2)
(c, 3)
escenarios
Tenemos tres activos: S1 (la cuenta bancaria), S2 y S3. Los valores
de los activos en los distintos nodos son los siguientes:
activo S1
1
1.02
1.04
1.04
1.04
1.02
1.04
1.04
1.04
1.02
1.04
1.04
1.04
activo S2
10
12
14
12
5
10
11
10
9
8
11
8
7
activo S3
12
6
5
7
10
11
4
12
26
20
11
19
29
La rentabilidad del dinero en los dos periodos es de 2 %. El activo S1 en tiempo t1 vale 1.02 en los
tres nodos, y vale 1.022 = 1.0404 en los nueve nodos ﬁnales.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
84

## Página 85

MFC 21-22
Valoraci´on. Fundamentos
2. Estrategias de inversi´on y estrategias autoﬁnanciadas
Las estrategias de inversi´on son ahora procesos. Se invierte en los activos din´amicamente,
cambiando en cada tk la composici´on de la cartera, usando la informaci´on disponible
hasta ese momento. En tiempos intermedios no hay posibilidad de alterar la cartera.
El n´umero de unidades del activo Si en tiempo tk se denota por λtk
i . La cantidad λtk
i se
ﬁja justo despu´es de tiempo tk−1 y se mantiene hasta tiempo tk, en que aparecen los
nuevos valores Stk
i .
La cantidad λtk
i s´olo depende de la informaci´on disponible en tiempo tk−1.
El valor de la cartera en tiempo tk viene dado por:
V tk =
M

i=1
λtk
i Stk
i .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
85

## Página 86

MFC 21-22
Valoraci´on. Fundamentos
En una cartera autoﬁnanciada, en cada tiempo tk la cartera se puede recomponer, es
decir, cambiar su composici´on, pero no se aportan ni se retiran fondos.
As´ı, en una cartera autoﬁnanciada
en tiempo tk
cartera ⇝
M
i=1 λtk
i Stk
i
justo despu´es de tk se recompone
cartera ⇝
M
i=1 λ
tk+1
i
Stk
i
y debe cumplirse que
M

i=1
λtk
i Stk
i =
M

i=1
λ
tk+1
i
Stk
i .
ejemplo base
Partimos de 100. Comp´arense las dos siguientes estrategias.
siempre tenemos un 50 % del valor de nuestra cartera invertido en el activo S1, un 25 % en S2
y otro 25 % en S3.
siempre tenemos 50 invertido en el activo S1, 25 en S2 y 25 en S3.
¿Es alguna de estas estrategias autoﬁnanciada?
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
86

## Página 87

MFC 21-22
Valoraci´on. Fundamentos
3. Activo replicable
Un activo general X paga en tiempo tH: X(ω), ﬂujo de X en escenario ω.
El activo es replicable si hay una estrategia de inversi´on autoﬁnanciada tal que
X(ω) = V tH(ω), para cada escenario ω;
es decir, pase lo que pase, al liquidar la cartera V tH en tiempo tH se obtienen
exactamente los ﬂujos de X.
Ahora no tenemos, en general, una replicaci´on est´atica en la que, como en el caso de un
´unico periodo, se determina una cartera al comienzo y queda ﬁja, sino una replicaci´on
din´amica en la que la cartera se ir´a recomponiendo para adaptarse a las cambiantes
condiciones de mercado.
Diremos que el modelo es completo si todos los activos son replicables.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
87

## Página 88

MFC 21-22
Valoraci´on. Fundamentos
C´alculo de una cartera replicante
La estrategia de replicaci´on se obtiene procediendo hacia atr´as en el ´arbol. Lo ilustramos
en el ejemplo base.
7
-
w
-
-
j
*
j
*
-
j
*
a
b
c
(a, 1)
(a, 2)
(a, 3)
(b, 2)
(b, 1)
(b, 3)
(c, 1)
(c, 2)
(c, 3)
escenarios
activo S1
1
1.02
1.04
1.04
1.04
1.02
1.04
1.04
1.04
1.02
1.04
1.04
1.04
activo S2
10
12
14
12
5
10
11
10
9
8
11
8
7
activo S3
12
6
5
7
10
11
4
12
26
20
11
19
29
activo X
1
0
0
1
0
0
1
0
0
Queremos replicar el activo X que en tiempo t2 paga: X =
⎧
⎪
⎨
⎪
⎩
1,
si Y2 = 1;
0,
si Y2 = 2;
0,
si Y2 = 3.
Se trata de cuatro modelos matriciales de un solo periodos: tres de tiempo 1 (nodos a,
b y c) y uno de tiempo 0 (nodo inicial).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
88

## Página 89

MFC 21-22
Valoraci´on. Fundamentos
Por ejemplo, en el nodo a, tendr´ıamos el siguiente modelo matricial:
S1
S2
S3
⎛
⎝
1.02
12.0
6.0
⎞
⎠
⎛
⎝
1.04
1.04
1.04
14
12
5
5
7
10
⎞
⎠
S1
S2
S3
(a, 1)
(a, 2)
(a, 3)
Buscamos la composici´on de la cartera de S1, S2 y S3 en ese nodo que cumpla que,
pase lo que pase, replique luego en tiempo t2 los valores de X.
Es decir, nos planteamos el sistema:
⎧
⎨
⎩
1
= (1.02)2 λ1
+14 λ2
+5 λ3
0
= (1.02)2 λ1
+12 λ2
+7 λ3
0
= (1.02)2 λ1
+5 λ2
+10 λ3
donde las inc´ognitas λ1, λ2, λ3 dan el n´umero de unidades de los activos S1, S2, S3. La
soluci´on del sistema anterior es λ1 = 10.21, λ2 = −0.37 y λ3 = −0.87, que supone un
coste de la cartera replicante (en el nodo a) de 0.66. An´alisis an´alogos para los nodos b
y c dan costes de la cartera replicante de 0.33 y 0.13, respectivamente.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
89

## Página 90

MFC 21-22
Valoraci´on. Fundamentos
7
-
w
-
-
j
*
j
*
-
j
*
valores cartera replicante
1
1
1
0
0
0
0
0
0
0.42
0.66
0.33
0.13
Seguimos hacia atr´as. Nos preguntamos qu´e cartera (en el
nodo inicial) es tal que pase lo que pase (sea cual sea el valor
de Y1), valga en t = 1 los costes que acabamos de calcular
de la cartera replicante. Planteamos el sistema
⎧
⎨
⎩
0.66
= (1.02)λ1
+12λ2
+6λ3
0.33
= (1.02)λ1
+10λ2
+11λ3
0.13
= (1.02)λ1
+8λ2
+20λ3
cuya soluci´on es λ1 = −2.565, λ2 = 0.2560 y λ3 = 0.035,
que supone un coste de la cartera replicante de 0.42.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
90

## Página 91

Valoraci´on. Fundamentos
6. Modelo de varios periodos:
valoraci´on
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
91

## Página 92

MFC 21-22
Valoraci´on. Fundamentos
Valoraci´on por replicaci´on
Si suponemos que no tenemos oportunidades de arbitraje, para valorar un activo X que
paga unos ciertos ﬂujos en tiempo T,
basta determinar la cartera que replica los pagos de X a vencimiento;
calcular el coste de formaci´on de esa cartera;
y ´ese ser´a el valor hoy del instrumento X.
Por cierto, una oportunidad de arbitraje es una estrategia de inversi´on autoﬁnanciada
para la que V t0 = 0 pero para la que
V tH[ω] ≥0, para todo escenario ω
y para alg´un escenario ω,
V tH[ω] > 0,
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
92

## Página 93

MFC 21-22
Valoraci´on. Fundamentos
Valoraci´on con probabilidades
Numerario
Un numerario N es un activo b´asico (o una cartera autoﬁnanciada de activos b´asicos)
que en todos los tiempos t0, t1, t2, . . . , tH y en todo escenario tenga valor positivo.
Probabilidad de valoraci´on
Una probabilidad de valoraci´on respecto de un numerario N es una probabilidad Q en Ω
que asigna probabilidad positiva a cada escenario (Q(ω) > 0), de manera que cada uno
de los activos (en t´erminos del numerario) es una martingala bajo Q:
 Stk
i
Ntk
!
k=1,2,...,H
es Q martingala
Es decir,
S
tk−1
i
Ntk−1 = EQ
 Stk
i
Ntk
Ftk−1

,
para k = 1, 2, . . . , H
para i = 1, 2, . . . , M
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
93

## Página 94

MFC 21-22
Valoraci´on. Fundamentos
Pero adem´as, si Q es probabilidad de valoraci´on, el proceso de valor de una cartera
autoﬁnanciada tambi´en es Q-martingala:
V tk−1
Ntk−1 = EQ
V tk
Ntk
Ftk−1

,
para k = 1, 2, . . . , H
Y, en particular,
V t0
Nt0 = EQ
V tk
Ntk

para todo tiempo tk.
detalle.
EQ
V tk
Ntk
Ftk−1

= EQ
 M

i=1
λtk
i
Stk
i
Ntk
Ftk−1

[martingala]
=
M

i=1
λtk
i
S
tk−1
i
Ntk−1
[autoﬁnanciada]
=
M

i=1
λ
tk−1
i
S
tk−1
i
Ntk−1 = V tk−1
Ntk−1
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
94

## Página 95

MFC 21-22
Valoraci´on. Fundamentos
Probabilidad de valoraci´on y no arbitraje
Si, ﬁjado un numerario, hay probabilidad de valoraci´on, ya hemos visto que el proceso
de valor de una cartera autoﬁnanciada es martingala. En particular,
EQ
V tH
NtH

= V t0
Nt0 .
Pero esto impide que pueda haber oportunidades de arbitraje, porque el lado derecho
ser´ıa 0, pero el izquierdo no.
existencia de probabilidad de valoraci´on
⇓
ausencia de oportunidades de arbitraje
Observaci´on
Una vez que se ha ﬁjado un numerario N, para comprobar que el modelo es libre de arbitraje y para valorar activos
replicables, basta con exhibir una probabilidad de valoraci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
95

## Página 96

MFC 21-22
Valoraci´on. Fundamentos
C´alculo de una probabilidad de valoraci´on
Fijamos un numerario N. Podemos construir una probabilidad de valoraci´on (que en
principio est´a deﬁnida para cada una de las sendas posibles) a partir de construcciones
locales (en cada nodo, que es un submodelo).
Si en cada nodo podemos encontrar una pro-
babilidad de valoraci´on, entonces podremos
deﬁnir una probabilidad de valoraci´on en ca-
da uno de los escenarios asignando a cada
uno de ellos, simplemente, la probabilidad
producto (v´ease el detalle del argumento en
la p´agina siguiente).
En el modelo base, el c´alculo de las proba-
bilidades de valoraci´on en cada nodo da el
resultado que aparece a la derecha.
7
-
w
-
-
j
*
j
*
-
j
*
a
b
c
(a, 1)
(a, 2)
(a, 3)
(b, 2)
(b, 1)
(b, 3)
(c, 1)
(c, 2)
(c, 3)
probabilidad de
cada escenario
53,5 %
3 %
43,5 %
68 %
16 %
16 %
33,7 %
52,7 %
13,7 %
13,6 %
61,5 %
24,9 %
...........
...........
...........
...........
...........
...........
...........
...........
...........
36,4 %
8,6 %
8,6 %
1,0 %
1,6 %
0,4 %
5,9 %
26,7 %
10,8 %
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
96

## Página 97

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
detalle del argumento. Lo ilustramos en el ejemplo base. Digamos que, para el modelo que comienza en a (con
notaci´on obvia), tenemos una probabilidad de valoraci´on
Qa =

pa→(a,1); pa→(a,2); pa→(a,3)

Si S es uno de los activos y N es el numerario tendremos (en notaci´on obvia) que
St1(a)
N(a) = pa→(a,1)
St1(a, 1)
N(a, 1) + pa→(a,2)
St1(a, 2)
N(a, 2) + pa→(a,3)
St1(a, 3)
N(a, 3)
Si ahora deﬁnimos Q sobre el conjunto de los escenarios asignando, por ejemplo, al escenario (a, 1) la probabilidad
producto:
p(nodo inicial→a) · pa→(a,1) ,
y as´ı sucesivamente, tendremos que para el activo S, por ejemplo,
EQ
 St2
Nt2
{Y1 = a}

= St2(a)
Nt2(a) ,
y en general que
EQ
 St2
Nt2
F1

= St2
Nt2 .
En suma, que St/Nt es martingala.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
97

## Página 98

MFC 21-22
Valoraci´on. Fundamentos
Valoraci´on de activos replicables
Para valorar un activo replicable no hace falta exhibir la cartera replicante, basta con
saber que es posible. Si X es activo replicable, existir´a una cartera (autoﬁnanciada)
replicante:
X ≡V tH .
El que no haya oportunidades de arbitraje nos dice que el valor hoy de X debe coincidir
con V t0. Pero como el proceso de precio de la cartera es martingala,
valorhoy(X)
no arbitraje
=
V t0 martingala
=
Nt0 · EQ
V tH
NtH
 replicaci´on
=
Nt0 · EQ
XtH
NtH

.
As´ı que el instrumento X se valora, simplemente, como
valorhoy(X) = Nt0 · EQ
XtH
NtH

ejemplo base
Val´orese el activo X que paga, en tiempo t2, 1 si Y2 = 1, y 0 en el resto de los casos.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
98

## Página 99

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
De nuevo, tenemos una equivalencia:
no hay oportunidades de arbitraje
⇐⇒
hay una probabilidad de valoraci´on
Ya hemos visto una implicaci´on, la parte del resultado que m´as usamos: comprobamos que un modelo el libre de
arbitraje exhibiendo una probabilidad de valoraci´on. Pero el rec´ıproco tambi´en es relevante. Ilustramos el argumento
que lo justiﬁca con el ejemplo concreto de nuestro modelo base, apoy´andonos en lo que ya sabemos para modelos de
un s´olo periodo: vamos de lo local a lo global.
Tenemos cuatro modelos locales de un solo periodo de tiempo, uno de tiempo t = t0 a t = t1 y tres de tiempo
t = t1 a t = t2. Si el modelo global no tiene arbitraje, tampoco lo tienen los modelos locales. Por ejemplo, si el
modelo que arranca en el nodo a tuviera una oportunidad de arbitraje, entonces podr´ıamos implementar la estrategia
global que arranca con inversi´on 0 en todos los activos. Si sucede Y1 = b ´o Y1 = c, mantenemos inversi´on nula y a
partir de ah´ı la ganancia ﬁnal ser´a 0. Pero si sucede Y1 = a, adonde llegamos con valor 0, acometemos la estrategia
(con inversi´on 0) que para alguno de los potenciales valores de Y2 consiguientes nos dar´a valor positivo, y siempre no
negativo. El resultado es una estrategia de inversion autoﬁnanciada que genera arbitraje.
Como los modelos locales son libres de arbitraje, tendremos probabilidades de valoraci´on para cada uno de ellos. Y
podemos construir una probabilidad global asignando las probabilidades producto.
Nota: el hecho de que la ausencia de arbitraje global sea consecuencia de la ausencia de arbitraje local es muy
´util para modelizaci´on. Habitualmente, los modelos generales se construyen concatenando piezas b´asicas que son
modelos de un ´unico periodo, muchas veces equivalentes entre s´ı. ´Ese es el caso, por ejemplo, del ´arbol binomial de
Cox-Ross-Rubinstein o del modelo de Hull-White en versi´on discreta.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
99

## Página 100

MFC 21-22
Valoraci´on. Fundamentos
Cambio de numerario
Si el mercado es completo y libre de arbitraje, entonces para cada numerario N hay una
´unica probabilidad de valoraci´on respecto de N, que denotamos por QN.
Supongamos que tenemos otro numerario M. Podemos usar N y M para valorar.
Para cualquier activo X de FtH,
EQN

X Nt0
NtH

= EQM

X Mt0
MtH

,
que abreviamos:
Nt0
NtH QN = Mt0
MtHQM .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
100

## Página 101

MFC 21-22
Valoraci´on. Fundamentos
Esto nos dice que si hemos obtenido y calculado la probabilidad QN, no necesitamos
repetir un c´alculo an´alogo para obtener QM, sino que basta con observar que
QM = MtH
Mt0
Nt0
NtHQN ,
es decir, que para cualquier X de FtH
EQM

X

= EQN

XMtH
Mt0
Nt0
NtH

´Esta es la expresi´on que nos da la nueva probabilidad de valoraci´on por cambio de
numerario.
Usaremos esta expresi´on del cambio de numerario con frecuencia.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
101

## Página 102

Valoraci´on. Fundamentos
7. Modelos continuos: valoraci´on
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
102

## Página 103

MFC 21-22
Valoraci´on. Fundamentos
El esquema de modelo de mercado ﬁnanciero anterior se extiende al caso de evoluci´on
continua del tiempo t para 0 ≤t ≤T.
Si enfocamos s´olo la cuesti´on de valoraci´on a mercado, como haremos aqu´ı, sin
atender a la replicaci´on, la trasposici´on (casi como paso al l´ımite) de tiempo discreto
a tiempo continuo es directa, como vamos a ver a continuaci´on.
Las estrategias de inversi´on, las carteras autoﬁnanciadas y la replicaci´on en tiempo
continuo requieren de nociones y conceptos de c´alculo estoc´astico.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
103

## Página 104

MFC 21-22
Valoraci´on. Fundamentos
Planteamos los ingredientes:
Tiempo y escenarios
El tiempo ahora va desde t = 0 hasta t = T de forma continua.
Llamamos Ω al espacio de escenarios.
Consideraremos probabilidades Q deﬁnidas en este espacio Ω de estados.
Filtraci´on de informaci´on
En Ω tenemos deﬁnidos uno (o varios) procesos que van generando una ﬁltraci´on de
informaci´on Ft.
Muy habitualmente, la ﬁltraci´on va siendo generada por un proceso browniano, o quiz´as
por varios
Ft = σ{Ws; s ≤t},
Ft = σ{W (1)
s
, . . . , W (k)
s
; s ≤t},
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
104

## Página 105

MFC 21-22
Valoraci´on. Fundamentos
Activos b´asicos
Tenemos una serie de activos b´asicos, S1, . . . , SM, que podemos comprar y vender sin
restricci´on en cada instante de tiempo t, 0 ≤t ≤T.
Para cada 1 ≤j ≤M y para cada tiempo 0 ≤t ≤T, denotamos por Sj(t) el valor del
activo j en tiempo t. Estos activos Sj est´an adaptados al ﬂujo de informaci´on, es decir,
Sj(t) es de Ft para cada t ≤T.
Nuestro abanico de activos (nuestro mercado) se compone, en principio, de estos
activos, y adem´as de las carteras (din´amica y autoﬁnanciadamente gestionadas) de
estos instrumentos.
Observaci´on
Cada escenario ω ∈Ω determina una evoluci´on conjunta de los M activos de referencia. Es decir, los valores de
S1(t)[ω], . . . , SM(t)[ω]
para cada tiempo t ≥0.
Podemos entender la ﬁltraci´on de informaci´on {Ft} como el conjunto de sucesos A (A ⊂Ω) que se pueden expresar
en t´erminos de los valores de S1, S2, . . . , SM desde tiempo 0 hasta tiempo t.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
105

## Página 106

MFC 21-22
Valoraci´on. Fundamentos
Numerario
De entre ese abanico de activos (b´asicos o carteras autoﬁnanciadas de estos), seleccio-
namos un activo especial N, el numerario, al que exigimos que en todo tiempo t sea
positivo con seguridad. Expresaremos los dem´as activos en unidades del numerario.
Observaci´on
• El ejemplo m´as tradicional es la cuenta bancaria, la capitalizaci´on a inter´es ﬁjo:
β(t) = ert
si el tipo a corto (instant´aneo) es ﬁjo;
β(t) = e
 t
0 r(u)du
si el tipo es una funci´on r(t) de tiempo;
β(t) = e
 t
0 rudu
si el tipo es un proceso aleatorio rt (ahora βt tambi´en es un proceso).
• Pero tambi´en podemos utilizar el bono cup´on cero de un vencimiento ﬁjo, T por ejemplo: P (t, T ) . Expresar
en unidades de P (t, T ) signiﬁca proyectar a tiempo t = T . Cuando usamos la cuenta bancaria como numerario
proyectamos a tiempo t = 0.
• Asimismo, podemos (y en ocasiones conviene) usar como numerario la cotizaci´on de una acci´on, o un bono cup´on
cero con riesgo de incumplimiento, o anualidades.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
106

## Página 107

MFC 21-22
Valoraci´on. Fundamentos
Ausencia de oportunidades de arbitraje y valoraci´on
Fijado un numerario N, si existe una probabilidad Q de manera que los activos
expresados en unidades del numerario sean martingala, es decir,
EQ
Sj(t)
N(t)
Fu

= Sj(u)
N(u)
para cada j = 1, . . . , M,
y para cada par de tiempos 0 ≤u ≤t,
(condici´on que abreviaremos diciendo que Q es una probabilidad de valoraci´on),
entonces
1.- El modelo ser´a certiﬁcado para valorar, es decir, estar´a libre de arbitrajes internos
(con activos b´asicos y carteras –din´amica y autoﬁnanciadamente gestionadas– de
activos b´asicos).
2.- Podremos valorar lo replicable.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
107

## Página 108

MFC 21-22
Valoraci´on. Fundamentos
¿Por qu´e libre de arbitraje?
Si los activos, en unidades del numerario, son martingala, entonces cualquier estrategia
de inversi´on autoﬁnanciada en estos activos (expresada en unidades del numerario)
tambi´en es martingala. Es decir, si C(t) denota el valor de esa cartera en tiempo t,
entonces C(t)/N(t) es martingala. Es decir,
EQ
C(t)
N(t)
Fu

= C(u)
N(u) .
En particular,
C(0)
N(0) = EQ
C(T)
N(T)

.
Observaci´on
argumento. Supongamos que hubiera una oportunidad de arbitraje. Es decir, una cartera C que hoy vale 0 y que en
tiempo T paga siempre ≥0 y, con probabilidad no nula, > 0. Pero entonces tendr´ıamos que
EQ
C(T )
N(T )

> 0 ;
esto contradice la condici´on de martingala (el valor hoy deber´ıa ser > 0). Por tanto, no hay oportunidades de arbitraje.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
108

## Página 109

MFC 21-22
Valoraci´on. Fundamentos
Valoraci´on de lo replicable
Llamemos X(T) a los ﬂujos de un activo en tiempo T y supongamos que podemos
dise˜nar una estrategia de inversi´on autoﬁnanciada que d´e lugar a una cartera C(t) que
replica X. Es decir:
X(T) ≡C(T)
“pase lo que pase” (en todo estado ω ∈Ω).
Por supuesto, X(0) debe coincidir con C(0). Pero
X(0)
N(0)
no arbitraje
=
C(0)
N(0)
martingala
=
EQ
C(T)
N(T)

replicaci´on
=
EQ
X(T)
N(T)

.
Es decir, sin necesidad de calcular expl´ıcitamente la cartera replicante (nos basta con
saber que existe), podemos calcular el valor X(0) mediante
X(0) = N(0)EQ
X(T)
N(T)

c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
109

## Página 110

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
M´as a´un, si denotamos por X(t) al valor del activo en tiempo t, entonces,
X(t) = N(t)EQ
X(T )
N(T )
Ft

y X(t)/N(t) tambi´en es martingala.
Observaci´on
El activo podr´ıa tener pagos en distintos tiempos. Digamos que el instrumento X paga en varias fechas T1, T2, . . . , TL
ﬂujos aleatorios X(T1), . . . , X(TL). Estos ﬂujos ser´ıan replicables cada uno por su lado.
En realidad, un tal instrumento puede verse como una cartera de instrumentos, y tendr´ıamos que
X(0) = N(0)
L

k=1
EQ
X(Tk)
N(Tk)

.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
110

## Página 111

MFC 21-22
Valoraci´on. Fundamentos
Notas adicionales
En realidad, la existencia de la probabilidad de valoraci´on Q y la ausencia de oportunidad
de arbitraje son equivalentes.
Ya hemos visto que, ﬁjado un numerario N, si existe una probabilidad de valoraci´on Q,
entonces no habr´a oportunidades de arbitraje.
Pero al rev´es tambi´en: dado un numerario N cualquiera, si no hay oportunidades de
arbitraje, entonces existe una probabilidad Q de manera que los activos expresados
en unidades de numerario son martingala.
Si adem´as el mercado es completo, es decir, si cualquier activo de tiempo T puede
replicarse con carteras autoﬁnanciada de los activos b´asicos S1, S2, . . . , Sn, entonces
esa probabilidad es ´unica (por eso a veces la denotaremos por QN).
En la pr´actica m´as habitual, se impone que no hay oportunidades de arbitraje y se
asume que todos los activos son replicables.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
111

## Página 112

MFC 21-22
Valoraci´on. Fundamentos
Gu´ıa de construcci´on de modelos (continuos)
Al construir un modelo de valoraci´on, empezaremos
especiﬁcando los activos b´asicos (¿cu´ales?, depender´a de los instrumentos que
queramos valorar);
y ﬁjando un numerario N (¿cu´al?, depender´a tambi´en; muchas veces, el que m´as nos
convenga para los c´alculos).
Llamemos Q a una probabilidad de valoraci´on asociada a N. Es decir, la evoluci´on
de los activos (en t´erminos del numerario) ser´a Q-martingala. Cu´al sea esa evoluci´on
concreta dar´a lugar a los diferentes modelos, que trataremos en sesiones posteriores.
(En ocasiones, no hace falta especiﬁcar el modelo para valorar un instrumento. O mejor,
cualquier modelo certiﬁcado debe asignar el mismo precio a ciertos instrumentos. V´ease
la p´agina 154).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
112

## Página 113

MFC 21-22
Valoraci´on. Fundamentos
Queremos valorar un instrumento, un cierto derivado (una call, o algo m´as soﬁsticado)
sobre un subyacente S. En nuestro mercado vamos a considerar el activo S y otro activo
(por ejemplo, la cuenta bancaria, un bono a cierto vencimiento), que tomaremos como
numerario N.
Queremos dise˜nar un modelo de evoluci´on para S y N que sea “certiﬁcado”, es decir,
que no cree internamente oportunidades de arbitraje.
Llamemos St y Nt a los valores de tiempo t de nuestros dos activos. Con quiz´as
exagerada ambici´on, proponemos una evoluci´on conjunta como la que sigue:

dSt = μS(t, St) · St dt + σS(t, St) · St dW (1)
t
,
dNt = μN(t, Nt) · Nt dt + σN(t, Nt) · Nt dW (2)
t
,
donde los saltos brownianos tienen, adem´as, correlaci´on instant´anea ρ(t). (Obs´ervese
que estamos modelando en realidad los rendimientos de St y Nt).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
113

## Página 114

MFC 21-22
Valoraci´on. Fundamentos
Tomamos Nt como numerario. El modelo ser´a certiﬁcado si el proceso Zt = St/Nt es
martingala.
Es decir, si la evoluci´on de Zt no tiene deriva. Usando el lema de Itˆo, tenemos
dZt = Zt
"
μS −μN −1
2 ρ σS σN + σ2
N
#
dt +

t´erminos brownianos

.
Observaci´on
detalle. La funci´on f(x, y) = x/y tiene las siguientes derivadas: fx(x, y) = 1/y, fy(x, y) = −x/y2,
fxy(x, y) = −1/y2, fxx(x, y) = 0 y fyy(x, y) = 2x/y3. El lema de Itˆo nos dice que
dZt = 1
Nt
dSt −St
N2
t
dNt −1
2
1
N2
t
dSt dNt + St
N3
t
(dNt)2
= St
Nt

μS dt + σS dW (1)
t

−St
Nt

μN dt + σN dW (2)
t

−1
2
St
Nt

μS dt + σS dW (1)
t
 
μN dt + σN dW (2)
t

+ St
Nt

μN dt + σN dW (2)
t
2
= dt Zt

μS −μN −1
2 ρ σS σN + σ2
N

+ t´erminos de volatilidad.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
114

## Página 115

MFC 21-22
Valoraci´on. Fundamentos
¡Vaya! Simpliﬁquemos un poco. Digamos el numerario es la cuenta bancaria con
rentabilidad r(t), donde r(t) es una cierta funci´on:
dNt = r(t) Nt dt ,
Ahora la evoluci´on
dSt = r(t) St dt + σS(t, St) St dWt
ya es un modelo certiﬁcado (libre de arbitrajes internos), por que Zt es martingala (su
deriva es 0 porque hemos elegido μS = μN = r(t) y ρ = σN = 0).
Y, desde luego, m´as manejable: s´olo hay que especiﬁcar el tipo de inter´es r(t) y una
funci´on de volatilidad σS(t, St) para, por ejemplo, poder simular trayectorias de St (hasta
el vencimiento de la opci´on, digamos) y calcular muestreando el precio del derivado.
En este caso, adem´as, nos gustar´ıa disponer de f´ormulas.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
115

## Página 116

MFC 21-22
Valoraci´on. Fundamentos
Digamos que el instrumento C paga una cierta funci´on C(ST). La regla de evoluci´on
anterior nos dice que ST es una variable aleatoria con cierta funci´on de densidad fST
(que, con suerte, quiz´as hasta podamos calcular expl´ıcitamente). El pricing del derivado
ser´a:
C0
N0
= E
C(ST)
NT

=
1
NT
$ ∞
−∞
C(x) fST(x) dx ,
una integral que se puede calcular num´ericamente, o incluso, en ciertos casos. . .
ejemplo 1. Si ponemos r(t) = r y σS(t, St) = σ, entonces tenemos la evoluci´on:
dSt = r St dt + σ St dWt
Aqu´ı, ST resulta ser una variable lognormal, y obtenemos las f´ormulas de Black–Scholes
para calls y puts.
ejemplo 2. Podr´ıamos considerar modelos de volatilidad local,
dSt = r St dt + σ(t, St) St dWt ,
donde σ(t, St) es una cierta funci´on dada.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
116

## Página 117

MFC 21-22
Valoraci´on. Fundamentos
O mejor: aquella que valora consistentemente calls y puts de distintos plazos y strikes.
Obs´ervese que esto supone ampliar nuestro mercado de activos b´asicos, incluyendo en
´el las calls y las puts.
El procedimiento podr´ıa ser el siguiente: disponemos de los precios de calls y puts para
“todos” los plazos y strikes. Traducimos esos precios en volatilidades v´ıa la formula de
Black–Scholes para obtener la superﬁcie de volatilidad Σ(T, K), de la que obtenemos,
con alg´un procedimiento, la funci´on σ(t, St):
T
K
Σ(T, K)
-
S
t
σ(t, S)
El m´etodo de Dupire sigue estas ideas.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
117

## Página 118

Valoraci´on. Fundamentos
8. Ap´endice: complementos
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
118

## Página 119

MFC 21-22
Valoraci´on. Fundamentos
A1. Ejemplos adicionales de valoraci´on por replicaci´on
(P´agina 35 y alrededores)
1. Call/put binaria.
Una cartera con una call y una put binarias, ambas con strike K y vencimiento T , paga 1 en T pase lo
que pase, as´ı que es equivalente a un bono cup´on cero de nominal 1 vencimiento T . Esto es,
preciocall binaria + precioput binaria = preciobono cup´on cero .
2. Tipos de cambio. Si
un d´olar se cambia por x euros;
un euro se cambia por y libras;
y una libra se cambia por z d´olares,
entonces x · y · z = 1 .
3. Equity swaps (intercambio de rendimientos de la Bolsa y del dinero). A posee una acci´on de Telef´onica,
cuya cotizaci´on hoy es 100. Firma un contrato con B (que cuesta hoy 0) por el que
A “vende” a B la acci´on hoy y se compromete a recomprarla al precio que est´e en T ;
B pagar´a un cierto precio (que se ﬁja hoy) al vencimiento T .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
119

## Página 120

MFC 21-22
Valoraci´on. Fundamentos
A vencimiento T , los ﬂujos del contrato anterior son
A recibir´a el pago acordado al principio, que escribimos como 100(1 + KT );
y deber´a pagar el precio de la acci´on ST = 100(1 + RendTelef´onicaT ).
O, liquidando por diferencias,
A recibe
→
100 K T
(un pago ﬁjo);
B recibe
→
100 RendTelef´onica T
(un pago aleatorio).
El ﬂujo para A ser´a
−→
100(K −RendTelef´onica)T .
¿Cu´al deber´a ser el valor de K?
Opci´on 1. Como el rendimiento de la acci´on de Telef´onica es una variable aleatoria, proponemos un
modelo probabil´ıstico para ese rendimiento, calculamos
E(RendTelef´onica)
y decidimos que
K = E(RendTelef´onica)
(el equivalente “cierto” de un rendimiento aleatorio). ¿Es ´este el precio correcto?
Opci´on 2. El tipo de inter´es a plazo T es R. Dise˜namos una estrategia para A, de coste total es 0:
compra hoy una acci´on de Telef´onica (que cuesta 100) con dinero prestado;
y entra en el equity swap.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
120

## Página 121

MFC 21-22
Valoraci´on. Fundamentos
A vencimiento T , la cartera paga
Equity Swap
Acci´on
Deuda
100(K −RendTelef´onica)T
100(1 + RendTelef´onicaT )
−100(1 + RT )
En total, A recibe 100 T (K −R). As´ı que K = R, o una de las dos partes tiene una oportunidad de
arbitraje.
Moraleja: para valorar consistentemente el equity swap, debemos “suponer” que el rendimiento medio de
la acci´on de Telef´onica coincide con el rendimiento del activo sin riesgo.
Ejercicio
Versi´on con dividendos (´esta es la raz´on de ser ﬁnanciera del equity swap: A, el poseedor de la acci´on, no desea cobrar
el dividendo). Supongamos que entre 0 y T la acci´on paga un dividendo 100 D. D es un porcentaje, por ejemplo el
3 %, que es conocido hoy. El contrato es como antes, pero B se queda el dividendo y paga a vencimiento
100(1 + (K + D)T ) .
Compru´ebese que, de nuevo, K = R −D.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
121

## Página 122

MFC 21-22
Valoraci´on. Fundamentos
Ejercicio
Intercambio de rentabilidades. La acci´on de Telef´onica vale hoy X0, y la de Endesa Y0. Se ﬁrma un contrato entre A y
B por el que, a vencimiento T ,
A paga a B el rendimiento simple de Telef´onica:
→
XT −X0
X0
;
B paga a A el rendimiento simple de Endesa:
→
YT −Y0
Y0
.
El coste de este contrato (hoy) es 0. Esto es, las rentabilidades de Endesa y Telef´onica con “equivalentes”.
Observaci´on
detalle. Ponemos los precios hoy de las acciones de Telef´onica y Endesa en una escala com´un. Es decir, calculamos
los n´umeros N0 y M0 tales que
N0 X0 = M0 Y0 = Δ .
Pedimos prestadas N0 acciones de Telef´onica, que vendemos por N0 X0. Con ese dinero podemos comprar M0
acciones de Endesa (inversi´on 0). A vencimiento T , la cartera vale
M0 YT −N0 XT = M0 YT −Δ + Δ −N0 XT = M0 YT −M0 Y0 + N0 X0 −N0 XT
= M0 Y0
YT −Y0
Y0
 
−N0 X0
XT −X0
X0
 
= Δ
YT −Y0
Y0
−XT −X0
X0
 
As´ı que paga lo mismo que Δ contratos de intercambio de rentabilidades.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
122

## Página 123

MFC 21-22
Valoraci´on. Fundamentos
A2. Sobre mercados incompletos
(P´agina 73 y alrededores).
Cotas para precios
Los activos que no pueden ser replicados con carteras de activos b´asicos no pueden ser valorados por
replicaci´on, claro.
Opci´on 1. Cotas por sub- y super-replicaci´on. Consideremos un activo general X, replicable o no.
Si aceptamos que el mercado no permite oportunidades de arbitraje invirtiendo en X y en los activos
b´asicos, el valor hoy de X habr´a de cumplir que
sup
Y replicables, Y ≤X
!
Y 0"



cota por sub-replicaci´on
≤X0 ≤
´ınf
Y replicables, Y ≥X
!
Y 0"



cota por super-replicaci´on
(Y
≥X signiﬁca que Y (ωj) ≥X(ωj), para j = 1, . . . , N). Estas cotas suponen la mejor
informaci´on sobre el valor hoy de X si nos atenemos al paradigma de valoraci´on por replicaci´on. El lado
izquierdo (derecho) nos da el valor del activo replicable cuyos ﬂujos quedan por debajo (encima) de los
de X, pero lo m´as aproximadamente posible.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
123

## Página 124

MFC 21-22
Valoraci´on. Fundamentos
Ilustraci´on
¿C´omo se implementar´ıa este procedimiento para los datos del ejemplo de la p´agina 75?
Opci´on 2. Cotas con probabilidades. Obs´ervese que, ﬁjado un numerario N y una probabilidad de
valoraci´on asociada QN, por no arbitraje, las cotas anteriores se traducen en
sup
Y replicables, Y ≤X
#
N0 · EQ
$
Y 1
N1
% &
e
´ınf
Y replicables, Y ≥X
#
N0 · EQ
$
Y 1
N1
% &
Un teorema nos garantiza que los extremos del rango anterior coinciden (respectivamente) con
´ınf
Q
#
N0 · EQ
$
X1
N1
% &
y
sup
Q
#
N0 · EQ
$
X1
N1
% &
.
donde Q recorre la colecci´on de todas las probabilidades de valoraci´on asociadas al numerario N.
Ilustraci´on
¿C´omo se implementar´ıa este procedimiento para los datos del ejemplo de la p´agina 75?
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
124

## Página 125

MFC 21-22
Valoraci´on. Fundamentos
A3. Ejemplos adicionales de modelaci´on
(P´agina 90 y alrededores)
Planteamos a continuaci´on un par de situaciones en las que vamos a aplicar la tecnolog´ıa vista hasta el
momento.
En el primero, dispondremos de precios cotizados de ciertos instrumentos ﬁnancieros. El ejercicio
consistir´a en determinar los activos b´asicos, los escenarios y la probabilidad de valoraci´on (impl´ıcita),
que nos permitir´a dar precios a otros instrumentos.
El segundo es un caso especialmente ´util de estos modelos matriciales, el m´as sencillo posible: cuando
tenemos ´unicamente dos escenarios.
Este sencillo esquema servir´a, ensamblado convenientemente, como pieza b´asica en la construcci´on
de los conocidos como modelos binomiales.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
125

## Página 126

MFC 21-22
Valoraci´on. Fundamentos
Probabilidad impl´ıcita. Calls binarias
Datos
Subyacente S, cuyo valor hoy es S0 = 100.
Tipo continuo r = 5 %.
Tres calls binarias C1, C2 y C3 con vencimiento T = 1 a˜no y strikes respectivos K1 = 90 · e5 %,
K2 = 100 · e5 %, K3 = 110 · e5 %.
Cada call Cj paga 1 si el subyacente queda por encima de Kj, y 0 en caso contrario.
Las volatilidades cotizadas (con Black–Scholes) de las tres calls son σ1 = 60 %, σ2 = 40 % y
σ3 = 20 %.
Valor de la call (digital):
e−rT Φ
ln (100/(Ke−rT ))
σ
√
T
−1
2σ
√
T

.
Objetivo: valorar el instrumento que paga, en T = 1, 50 si el subyacente est´a entre K1 y K3, y 150 en
caso contrario.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
126

## Página 127

MFC 21-22
Valoraci´on. Fundamentos
Activos b´asicos
• El activo b´asico sin riesgo, la cuenta bancaria CB, que vale 1 en t = 0 y valdr´a, en t = 1 y en
cualquier escenario, er. Ser´a nuestro numerario.
...................................................................................................
K1
K2
K3
-
-
-
• Las tres calls digitales C1, C2 y C3. No incluimos el
subyacente S com´un a esas calls entre los activos b´asicos.
Escenarios
Planteamos un espacio de escenarios con Ω = {ω1, ω2, ω3, ω4}; los escenarios vienen determinados por
el subyacente:
{
S ≤K1}
←→
ω1
{K1 < S ≤K2}
←→
ω2
{K2 < S ≤K3}
←→
ω3
{K3 < S
}
←→
ω4
CB
C1
C2
C3
⎛
⎜
⎜
⎝
er
er
er
er
0
1
1
1
0
0
1
1
0
0
0
1
⎞
⎟
⎟
⎠
ω1
ω2
ω3
ω4
Los activos aqu´ı son aquellos instrumentos que toman un ´unico valor en cada uno de los escenarios. En
t´erminos del subyacente S, cualquier activo de este modelo toma un valor ´unico en cada rango de los
que S determina.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
127

## Página 128

MFC 21-22
Valoraci´on. Fundamentos
Replicaci´on
El modelo de mercado es completo:
...................................................................................................
K1
K2
K3


       


ω1
ω2
ω3
ω4
q1
q2
q3
q4
si X toma los valores x1, x2, x3, x4 en los escenarios ω1, ω2, ω3, ω4,
entonces X se replica:
X ≡x1(e−r CB −C1) +
4

j=2
xj

Cj−1 −Cj

≡x1 e−r CB +
3

j=1

xj+1 −xj

Cj .
Llamemos c1, c2, c3 a los valores de las calls en tiempo 0. Si no hubiera oportunidades de arbitraje, la
valoraci´on del activo X ser´ıa, simplemente,
valorhoy(X) = x1e−r +
3

j=1

xj+1 −xj

cj .
Probabilidades
Buscamos la probabilidad de valoraci´on Q
respecto del numerario CB, con Q(ωj) =
qj para j = 1, 2, 3, 4. Los qj han de cum-
plir, por supuesto, que sean no negativos y
que su suma sea 1.
Estas probabilidades deben cumplir 4 ecuaciones, una por cada activo b´asico. Pero la correspondiente a
la CB es, simplemente, la condici´on de que q1 + q2 + q3 + q4 = 1:
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
128

## Página 129

MFC 21-22
Valoraci´on. Fundamentos
As´ı que s´olo nos quedar´ıan las tres siguientes ecuaciones:
C1 −→
c1
1 = q1 0
er + q2 1
er + q3 1
er + q4 1
er
=⇒
q2 + q3 + q4
=
er c1
C2 −→
c2
1 = q1 0
er + q2 0
er + q3 1
er + q4 1
er
=⇒
q3 + q4
=
er c2
C3 −→
c3
1 = q1 0
er + q2 0
er + q3 0
er + q4 1
er
=⇒
q4
=
er c3
Podemos expresar las probabilidades qj directamente en t´erminos de los valores hoy de las calls:
q4
=
er c3
q3
=
er (c2 −c3)
q2
=
er (c1 −c2)
q1
=
1 −er c1
Para que esto sea probabilidad de valoraci´on han de cumplirse las desigualdades:
er c3 > 0 ,
er (c2 −c3) > 0 ,
er (c1 −c2) > 0 ,
1 −er c1 > 0
(la condici´on de q1 + q2 + q3 + q4 = 1 se cumplir´ıa autom´aticamente).
Por tanto, el modelo es libre de arbitraje si y s´olo si se cumplen las condiciones anteriores. Si una sola de
ellas no se satisface habr´a (en el modelo) una oportunidad de arbitraje.
Por ejemplo, si se diera que c2 −c3 ≤0, entonces compramos C2, vendemos C3, la diferencia
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
129

## Página 130

MFC 21-22
Valoraci´on. Fundamentos
c3 −c2 ≥0 se invierte a plazo (inversi´on inicial de 0). En T = 1 tendr´ıamos 1 + er (c3 −c2) si el
subyacente acaba entre K2 y K3, y er (c3 −c2) en otro caso.
La f´ormula de valoraci´on de X ser´ıa, por supuesto, la misma que la obtenida por replicaci´on:
valorhoy(X)
1
= q1
x1
er + q2
x2
er + q3
x3
er + q4
x4
er
= (1 −erc1) x1
er + er (c1 −c2)x2
er + er (c2 −c3)x3
er + er c3
x4
er
= x1 e−r + c1 (x2 −x1) + c2 (x3 −x2) + c3 (x4 −x3).
Ilustraci´on
Obtener Q y valorar el activo que paga 150 si el subyacente a vencimiento est´a por debajo de K1 o por encima de K3
y 50 en caso contrario para los datos de los precios de las calls dados al principio.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
130

## Página 131

MFC 21-22
Valoraci´on. Fundamentos
Modelo (Bernoulli) de dos estados
´Este es el modelo m´as simple. Aqu´ı Ω contempla tan s´olo dos escenarios:
Ω = {ωup, ωdown} .
Hay s´olo dos activos b´asicos. Uno es la cuenta bancaria CB, el instrumento sin riesgo: vale 1 en t = 0
y vale 1 + r en los dos escenarios de tiempo t = 1.
El segundo activo, que denotamos por S, toma el valor S0 en t = 0 y, para tiempo t = 1, toma valores
en cada escenario que ya escribimos en t´erminos de rentabilidades:
'
S1[ωup] = S0(1 + ru)
S1[ωdown] = S0(1 + rd)
(suponemos, por ejemplo, que ru > rd).
S
CB
S0(1 + ru)
S0(1 + rd)
(1 + r)
(1 + r)

ωup
ωdown
en tiempo t = 0:
S
CB
S0
1

c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
131

## Página 132

MFC 21-22
Valoraci´on. Fundamentos
Caso 1: cuenta bancaria como numerario
La condici´on de no arbitraje equivale a que existan pu y pd (ambos positivos y que suman 1), que deﬁnen
una probabilidad P sobre Ω de manera que
S0
CB0 = EP
$
S1
CB1
%
(la condici´on de la probabilidad de valoraci´on sobre CB se cumple trivialmente). Esta condici´on se
traduce en hallar pu y pd (no nulos y con pu + pd = 1) tales que
S0
1 = pu
S0(1 + ru)
1 + r
+ pd
S0(1 + rd)
1 + r
=⇒
r = pu ru + pd rd
Observaci´on
Y podremos encontrar pu si y s´olo si rd < r < ru. Que es, por cierto, la condici´on de no arbitraje que podr´ıamos
haber anticipado con argumentos ﬁnancieros. Pi´ensese.
Por ejemplo, si tomamos ru = 10 %, r = 5 %, y rd = 1 %, entonces las probabilidades resultan ser
pu = 4/9 = 44.44 % y pd = 5/9 = 55.56 %.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
132

## Página 133

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
Si tomamos como numerario N a la cuenta bancaria,
que en tiempo 0 vale 1;
y que en tiempo t = 1 tiene siempre (en todos los escenarios) el valor 1 + r, as´ı que r es la rentabilidad simple en
el periodo de tiempo desde t = 0 hasta t = 1;
(estamos suponiendo que N es uno de los activos b´asicos), una probabilidad de valoraci´on Q cumplir´a que para
cualquier estrategia λ,
V 0
λ = EQ
 V 1
λ
1 + r

Y, por tanto,
EQ(rentabilidad Vλ) = EQ
V 1
λ −V 0
λ
V 0
λ

= (1 + r)
V 0
λ
EQ

V 1
λ
(1 + r)




=V 0
λ
−1 = r .
Por esto decimos que esta probabilidad Q es riesgo neutro: la rentabilidad media (promediada con Q) de cualquier
estrategia de inversi´on es la del activo sin riesgo.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
133

## Página 134

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
Otro caso habitual es aquel en el que tomamos como numerario N el bono cup´on cero de nominal 1 que vence en
tiempo t = 1. De nuevo suponemos que N es uno de los activos b´asicos.
En este caso, N1 vale 1 en cualquier escenario, y en tiempo t = 0 tiene un valor N0 que interpretamos como (es) el
descuento desde tiempo t = 1 a tiempo t = 0.
Una probabilidad de valoraci´on Q cumplir´a para cualquier estrategia λ que
V 0
λ = N0 · EQ(V 1
λ) .
Esta probabilidad Q es conocida como forward neutra: la esperanza EQ(V 1
λ) coincide con el valor forward V 0
λ/N0.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
134

## Página 135

MFC 21-22
Valoraci´on. Fundamentos
Caso 2: subyacente como numerario
Si los valores de S en t = 0 y t = 1 son positivos, podemos usar como numerario a S. Hay
una probabilidad de valoraci´on Q (respecto de N = S) dada por dos n´umeros qu y qd que vienen
determinados por la ecuaci´on:
1
S0 = qu
1 + r
S0(1 + ru) + qd
1 + r
S0(1 + rd)
=⇒
1 = qu
 1 + r
1 + ru

+ qd
 1 + r
1 + rd

(Ahora, la condici´on de la probabilidad de valoraci´on sobre S se cumple trivialmente.)
Por ejemplo, si como antes ru = 10 %, r = 5 %, y rd = 1 %, entonces
qu = 46.56 %
y
qd = 53.44 %.
Obs´ervese c´omo diﬁeren P y Q.
P es probabilidad riesgo neutro (la rentabilidad media del activo con riesgo es la del dinero), pero no
as´ı Q.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
135

## Página 136

MFC 21-22
Valoraci´on. Fundamentos
Caso 3: otro numerario
De igual modo (suponiendo S siempre positivo), podr´ıamos tomar como numerario N la cartera que
invierte 100 repartido a partes iguales entre CB y S:
λCB = 50,
λS = 50
S0.
En este caso la probabilidad Π (dada por πu y πd) de valoraci´on cumple la ecuaci´on
1
50 + 50
S0 S0 = πu
1 + r
50(1 + r) + 50
S0 S0(1 + ru) + πd
1 + r
50(1 + r) + 50
S0 S0(1 + rd)
=⇒
1
2 = πu
1 + r
(1 + r) + (1 + ru) + πd
1 + r
(1 + r) + (1 + rd)
(´Esta es la ecuaci´on que se obtiene de valorar CB; la ecuaci´on que se obtiene de valorar S es equivalente.)
Cuando ru = 10 %, r = 5 %, y rd = 1 %, entonces πu = 45.50 % y πd = 54.50 %.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
136

## Página 137

MFC 21-22
Valoraci´on. Fundamentos
Ejercicio
Tenemos un modelo de cuatro estados ω1, ω2, ω3, ω4 y cuatro activos. Uno (el activo S1 es la cuenta bancaria, dos
(el segundo y el tercero) est´an positivamente correlados entre s´ı, y un cuarto que est´a negativamente correlado con
estos otros dos:
S1
S2
S3
S4
⎛
⎜
⎜
⎝
1.05
1.05
1.05
1.05
30
20
10
5
60
10
5
5
10
20
30
40
⎞
⎟
⎟
⎠
ω1
ω2
ω3
ω4
en tiempo t = 0:
S1
S2
S3
S4
⎛
⎜
⎜
⎝
1
12.5
10
27
⎞
⎟
⎟
⎠
• Val´orese una call sobre el m´aximo de dos de ellos, S3 y S4, por replicaci´on. Obs´ervese si en la replicaci´on intervienen
o no otros activos adem´as de S3 y S4.
• Obt´engase la probabilidad Q1 de valoraci´on (tomando S1 como numerario) y val´orese la call.
• Compru´ebese que la rentabilidad media (usando Q1) de la call es la de la de la cuenta bancaria, el activo S1.
• Obt´engase la probabilidad de valoraci´on Q2 cuando se toma como numerario a S2. Val´orese con ella la call y
compru´ebese que se obtiene el mismo valor que cuando se usa el numerario S1.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
137

## Página 138

MFC 21-22
Valoraci´on. Fundamentos
A4. Procesos de ganancia y no arbitraje
a) Proceso de valor y de ganancia de una inversi´on
Para una cartera de inversi´on λ = (λ1, . . . , λM), su proceso de valor normalizado es
Vλ
N =
M

i=1
λi
Si
N .
En tiempo t = 0 es
Y en tiempo t = 1, es la variable
V 0
λ
N0 =
M

i=1
λi
S0
i
N0.
V 1
λ
N1(ωj) =
M

i=1
λi
S1
i (ωj)
N1(ωj),
j = 1, 2, . . . , N .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
138

## Página 139

MFC 21-22
Valoraci´on. Fundamentos
La ganancia de la cartera λ (en t´erminos del numerario N) es la variable Gλ deﬁnida en tiempo t = 1
por
Gλ(ωj) = V 1
λ
N1(ωj) −V 0
λ
N0 =
M

i=1
λi
S1
i
N1(ωj) −S0
i
N0

.
ejemplo base
Con numerario N = 3S1 + S2, la cartera λ = (1, 2, 3, 1)T tiene proceso de valor y proceso de
valor normalizado:
V 0
λ = 8
V 1
λ =
ω1
ω2
ω3
ω4
12.5
8
6
17.5
V 0
λ
N0 = 8/3
V 1
λ
N1 =
ω1
ω2
ω3
ω4
6.25
1.6
1.7
2.5
Finalmente, la ganancia es
Gλ =
ω1
ω2
ω3
ω4
3.58
-1.07
-0.95
-0.17
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
139

## Página 140

MFC 21-22
Valoraci´on. Fundamentos
b) No arbitraje, probabilidad de valoraci´on y ganancia
Seleccionamos un numerario N. Recordemos que un numerario N es simplemente un activo b´asico o una
cartera de inversi´on en los activos b´asicos, que siempre es positivo, tanto en tiempo t = 0 como en cada
uno de los escenarios de tiempo t = 1.
Lema 1. Hay arbitraje si y solo si hay una cartera de inversi´on λ para la que su ganancia (con respecto
a cualquier numerario) cumple:
Gλ(ωj) ≥0,
para todo j,
y
Gλ(ωj) > 0,
para alg´un j.
La variable ganancia nos permite expresar la condici´on de no arbitraje en t´erminos ´unicamente de valores
en tiempo t = 1. Esta expresi´on nos dice que hay arbitraje si hay inversiones en las que pase lo que pase
no se pierde, y en alg´un caso se gana. Las variables de ganancia dependen del numerario seleccionado,
pero la noci´on de ausencia de arbitraje es independiente del numerario.
Lema 2. Una probabilidad Q es de valoraci´on con respecto a un numerario N si y solo si
EQ(Gλ) = 0
para cualquier estrategia de inversi´on λ.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
140

## Página 141

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
Demostraci´on del lema 1. En un sentido, si hay una oportunidad de arbitraje, la ganancia de esa inversi´on
cumplir´a la condici´on se˜nalada.
Supongamos ahora que la cartera λ = (λ1, . . . , λN) cumple la condici´on se˜nalada sobre su ganancia Gλ.
Creamos ahora una cartera β = (β1, . . . , βN) (que va a ser de arbitraje) cambiando la composici´on de la cartera
anterior. De hecho, lo que hacemos es invertir adicionalmente en el numerario N, que es una cartera de los
activos b´asicos. En N se ha de invertir en tiempo t = 0 la cantidad V 0
λ/N0. Si N viene dado por la cartera
ν = (ν1, . . . , νM), entonces:
βi = λi −νi · V 0
λ
N0,
i = 1, 2, . . . , M.
El proceso de valor Vβ de esta nueva cartera β cumple que V 0
β = 0 y
V 1
β = V 1
λ −
V 0
β
N0 N1 = N1 · Gλ.
La condici´on sobre Gλ nos dice que β es de arbitraje.
Demostraci´on del lema 2. Obs´ervese que
EQ(Gλ) = EQ
V 1
λ
N1 −V 0
λ
N0

= EQ
V 1
λ
N1

−V 0
λ
N0.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
141

## Página 142

MFC 21-22
Valoraci´on. Fundamentos
A5. Teorema fundamental de valoraci´on
Son equivalentes:
i) no hay oportunidades de arbitraje;
ii) para todo numerario hay probabilidad de valoraci´on;
iii) para un cierto numerario, hay una probabilidad de valoraci´on.
→Para comprobar directamente que en un modelo no hay arbitraje, habr´ıa que comprobar que ninguna
estrategia de inversi´on (y de estas hay tantas como vectores en RM) genera una oportunidad de arbitraje.
→Pero es mucho m´as sencillo proceder indirectamente, ﬁjar un numerario, y veriﬁcar que hay una
probabilidad de valoraci´on. La comprobaci´on de que una probabilidad es de valoraci´on supone cerciorarse
de que se cumplen M ecuaciones lineales.
→Determinar una probabilidad de valoraci´on requiere resolver un cierto sistema de ecuaciones (tantos
como activos b´asicos) y con tantas inc´ognitas como escenarios en el que hay ciertas restricciones
(positividad y suma igual a 1). Es un problema abordable.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
142

## Página 143

MFC 21-22
Valoraci´on. Fundamentos
Demostraci´on.
II) ⇒III). Evidente.
III) ⇒I), Supongamos que Q es probabilidad de valoraci´on (respecto de un numerario N) Si una cartera
λ es de arbitraje, entonces su valor en tiempo t = 0 es
V 0
λ = 0
y por tanto
V 0
λ
N0 = 0.
Pero como en tiempo t = 1 sus valores son no negativos, en alg´un escenario es positivo y Q da
probabilidad positiva a todos los escenarios, tendr´ıamos que
EQ
V 1
λ
N1

> 0 ,
as´ı que se tendr´ıa
V 0
λ
N0 ̸= EQ
V 1
λ
N1

,
que contradice que Q sea probabilidad de valoraci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
143

## Página 144

MFC 21-22
Valoraci´on. Fundamentos
I) ⇒II). La colecci´on G de vectores de ganancia de las distintas estrategias constituyen un subespacio
vectorial de RN. Como, por hip´otesis, no hay oportunidades de arbitraje, ha de cumplirse que
G ∩{x1, x2, . . . , xN; xj ≥0} = {(0, 0, . . . , 0)}
...............................................................................
G
 ⃗ν
Y en particular G ∩K = ∅, donde
K =
(
⃗w ∈RN; wj ≥0, j = 1, 2, . . . , N,
N

j=1
wj = 1
)
.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
144

## Página 145

MFC 21-22
Valoraci´on. Fundamentos
Entonces (teorema de separaci´on), existe un vector ⃗ν tal que
N

j=1
νj · G(ωj) = 0 ,
y tal que
⃗ν · ⃗k > 0 ,
para cada ⃗k ∈K. En particular, se deduce que νj > 0, para j = 1, 2, . . . , N.
Si ahora deﬁnimos:
qj =
νj

k νk
tenemos una probabilidad Q:
Q(ωj) = qj
y se tiene que para cualquier estrategia de inversi´on, la ganancia media es 0: EQ(G) = 0.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
145

## Página 146

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
Teoremas de separaci´on (Minkowski). Siempre en RN.
a) Compacto K y convexo C.
Si K ∩C = ∅, existe una forma lineal f en RN y constantes α y δ > 0 tal que f(⃗k) ≥α + δ, para todo
⃗k ∈K y f(⃗c) ≤α −δ, para todo ⃗c ∈C. El hiperplano H = {f = a} separa a K y C.
Consid´erese la funci´on Λ deﬁnida en K:
Λ(⃗k) = dist(⃗k, C) = ´ınf{d(⃗k,⃗c);⃗c ∈C} .
Es f´acil ver que el ´ınf de la deﬁnici´on de f es un m´ın, que Λ es continua, que Λ(⃗k) > 0, para todo ⃗k ∈K, y,
usando que K es compacto, que existe ⃗k0 ∈K y ⃗c0 ∈C, tal que
d( ⃗k0, ⃗c0) ≤d(⃗k,⃗c) ,
para cualesquiera ⃗k ∈K,⃗c ∈C.
Sea H el hiperplano por el punto medio del segmento [ ⃗k0, ⃗c0]. Sea f una forma lineal de manera que
{f = α} = H para un cierto α. Podemos suponer que f( ⃗k0) > α, digamos f( ⃗k0) = α + δ con δ > 0. Por
simetr´ıa, se tiene que f(⃗c0) = α −δ. Se comprueba f´acilmente (argumento 2 dimensional) que f(⃗k) ≥α + δ,
para todo ⃗k ∈K, y f(⃗c) ≤α −δ, para todo ⃗c ∈C.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
146

## Página 147

MFC 21-22
Valoraci´on. Fundamentos
Observaci´on
b) Compacto K y subespacio L.
Si K ∩L = ∅, existe una formal lineal f en RN y constante β > 0 tal que f(⃗k) ≥β, para todo ⃗k ∈K y
f(⃗l) = 0, para todo ⃗l ∈L.
En particular,
L ⊂H = {f = 0}. Es decir, L est´a contenido en el subespacio vectorial H de dimensi´on N −1.
Existe un vector ⃗v ∈RN tal que para todo ⃗l ∈L
⃗v · ⃗l = 0 ,
y para todo ⃗k ∈K
⃗v · ⃗k ≥β .
Este segundo enunciado se sigue enseguida de que L es convexo cerrado y de que f(⃗l) ≤α −δ ≤0 y
f(−⃗l) ≤α −δ ≤0, para todo ⃗l ∈L, y, por tanto, f(⃗l) = 0 para todo ⃗l ∈L. De manera que α > δ y
β = α + δ > 2δ > 0.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
147

## Página 148

MFC 21-22
Valoraci´on. Fundamentos
A6. Sobre numerarios y probabilidades de valoraci´on
a) Por qu´e la probabilidad de valoraci´on hace innecesario el c´alculo de la replicaci´on
Tenemos un modelo matricial, un numerario N y su correspondiente probabilidad de valoraci´on Q
(respecto de N):
qj = Q(ωj),
j = 1, 2, . . . , N
El activo X es replicable y queremos valorarlo. Como es replicable, X ≡M
i=1 λi Si, es decir,
X1(ωj) =
M

i=1
λi S1
i (ωj)
j = 1, 2, . . . , N
o mejor, expandido:
ecuaci´on 1 ⇝
X1(ω1)
= λ1 S1
1(ω1) + λ2 S1
2(ω1) + · · · + λM S1
M(ω1)
ecuaci´on 2 ⇝
X1(ω2)
= λ1 S1
1(ω2) + λ2 S1
2(ω2) + · · · + λM S1
M(ω2)
...
...
...
ecuaci´on N ⇝
X1(ωN)
= λ1 S1
1(ωN) + λ2 S1
2(ωN) + · · · + λM S1
M(ωN)
Multiplicamos ahora la ecuaci´on j-´esima por qj, la dividimos por N1(ωj) y sumamos todas las ecuaciones
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
148

## Página 149

MFC 21-22
Valoraci´on. Fundamentos
resultantes para obtener:
N

j=1
qj
X1(ωj)
N1(ωj)

=
M

i=1
λi
S0
i
N0

=
M
i=1 λiS0
i
N0
.
O, en otros t´erminos,
EQ
X1
N1

= X0
N0
(¡los λj han desaparecido!)
b) Explicaci´on de por qu´e se usan numerarios
Tenemos un modelo matricial, un numerario N y su correspondiente probabilidad de valoraci´on Q
(respecto de N):
qj = Q(ωj),
j = 1, 2, . . . , N .
Si X es replicable, entonces
X0 = N0 · EQ
X1
N1

= N0
N

j=1
qj
X1(ωj)
N1(ωj) =
N

j=1
qj · N0
N1(ωj) X1(ωj) .
Obs´ervese que los pesos
πj = qj · N0
N1(ωj)
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
149

## Página 150

MFC 21-22
Valoraci´on. Fundamentos
permiten escribir el valor hoy de X como suma ponderada:
X0 =
N

j=1
πj X1(ωj) ,
una expresi´on, en principio, m´as sencilla. Pero entonces los pesos πj no suman 1, no son una probabilidad,
y no podr´ıamos apelar al c´alculo de probabilidades, como hemos hecho repetidamente.
c) Explicaci´on de por qu´e se exige que el numerario sea replicable
Supongamos ahora que partimos de un activo general, no necesariamente replicable, digamos Z, que en
tiempo t = 0 y en todos los escenarios de tiempo t = 1 toma valores positivos.
La pregunta es si podemos tener otros pesos (otras probabilidades) en Ω para que podamos valorar
normalizando en unidades de Z.
Veamos. Sabemos que
S0
i
N0 = EQN
S1
i
N1

=

j
qj
S1
i (ωj)
N1(ωj)
para cada i = 1, 2, . . . , M, con qj = QN(ωj), para j = 1, 2, . . . , N.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
150

## Página 151

MFC 21-22
Valoraci´on. Fundamentos
Entonces, si decidi´eramos usar Z escribir´ıamos:
S0
i
Z0 =

j
S1
i (ωj)
Z1(ωj)

qj
N0 Z1(ωj)
Z0 N1(ωj)

.
Podemos deﬁnir unos pesos (son positivos) pj por
pj =

qj
N0 Z1(ωj)
Z0 N1(ωj)

,
y tenemos
S0
i
Z0 =

j
S1
i (ωj)
Z1(ωj) pj .
Pero los pesos pj, en general no sumar´an 1, para darnos una probabilidad.
La condici´on de que los pj sumen 1 se puede reescribir:
1 =
N

j=1
pj =
N

j=1
qj
N0Z1(ωj)
Z0N1(ωj)
=⇒
Z0
N0 =
N

j=1
qj
Z1(ωj)
N1(ωj) = EQN
Z1
N1

,
as´ı que para garantizar que las pj suman 1, nos basta con saber que Z es un activo replicable. Por eso
exigiremos que los numerarios sean replicables.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
151

## Página 152

MFC 21-22
Valoraci´on. Fundamentos
A7. Probabilidad de valoraci´on ´unica
Un modelo de mercado es completo y sin ausencia de oportunidad de arbitraje si y solo si para cada
numerario existe una ´unica probabilidad de valoraci´on.
S´olo resta comprobar que si hay una ´unica probabilidad de valoraci´on para un numerario dado, entonces
el mercado es completo.
Supongamos que Q es probabilidad de valoraci´on para N (as´ı que no hay arbitraje) y que el modelo no
es completo. Vamos a comprobar que hay otras probabilidades de valoraci´on. Pongamos que
Q(ωj) = qj,
j = 1, 2, . . . , N .
Como el modelo no es completo, los activos replicables son un subespacio propio del total de activos. As´ı
que tiene que haber un vector R = (r1, r2, . . . , rN) (no nulo) tal que
0 =
N

j=1
X1(ωj)
N1(ωj) · rj ,
para cualquier X replicable.
Formamos, para ε > 0 y peque˜no, Qε dada por
Qε(ωj) = qj + εrj,
j = 1, 2, . . . , N .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
152

## Página 153

MFC 21-22
Valoraci´on. Fundamentos
Comprobamos ahora que si ε es peque˜no entonces Qε es probabilidad de valoraci´on respecto de N:
Si ε es peque˜no, entonces los pesos de Qε son positivos: Qε(ωj) > 0 para j = 1, 2, . . . , N.
Para cada i = 1, 2, . . . , M
EQε
Si
1
N 1

=
N

j=1
(qj + εrj)Si
1(ωj)
N 1(ωj) =
N

j=1
qj
Si
1(ωj)
N 1(ωj) = Si
0
N 0
Y, ﬁnalmente, los pesos de Qε suman 1. Aqu´ı el numerario desempe˜na un papel relevante. Como N
es un activo b´asico o una cartera de activos b´asicos, entonces:
0 =
N

j=1
N(ωj)
N(ωj) · rj ,
y, por tanto,
0 =
N

j=1
rj ,
as´ı que
N

j=1
Qε(ωj) =
N

j=1
(qj + εrj) =
N

j=1
qj = 1 .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
153

## Página 154

MFC 21-22
Valoraci´on. Fundamentos
A8. Algunos ejemplos generales de valoraci´on
En ocasiones, no hace falta especiﬁcar el modelo para valorar un instrumento. O mejor, cualquier modelo
certiﬁcado debe asignar el mismo precio a ciertos instrumentos.
ejemplo 1. Valoraci´on de un forward (independiente del modelo).
Tenemos dos activos b´asicos: el bono cup´on cero (de principal 1) que vence en tiempo T , que en tiempo
t vale P (t), y una acci´on (que no paga dividendos) S(t). El numerario es el propio bono. Queremos
valorar el ﬂujo S(T ) −K pagado en tiempo T .
Sea Q una probabilidad de valoraci´on, bajo la cual S(t)/P (t) es martingala. En particular, tendremos
que
EQ
S(T )
P (T )

= S(0)
P (0) .
La valoraci´on del forward es:
F wd(0)
P (0)
= EQ
S(T ) −K
P (T )

= EQ
S(T )
P (T )

−EQ

K
P (T )

= S(0)
P (0) −K
pues P (T ) ≡1. Es decir, F wd(0) = S(0) −K P (0). O bien, si queremos que F wd(0) = 0,
entonces debemos tomar K = S(0)/P (0).
Y todo esto, independientemente del modelo de evoluci´on que pudi´eramos asignar a S(t).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
154

## Página 155

MFC 21-22
Valoraci´on. Fundamentos
ejemplo 2. Activo replicable est´aticamente (independiente del modelo)
En realidad, si un activo es replicable est´aticamente con activos b´asicos, su valoraci´on no debe depender
del modelo de evoluci´on que seleccionemos para ´estos.
Digamos que el activo X que queremos valorar paga ﬂujos X(T ) en tiempo T . Y supongamos que
podemos formar una cartera (λ1, . . . , λM) de activos b´asicos S1, . . . , SM de manera que (sin cambiar
su composici´on) en tiempo T
X(T ) ≡
M

i=1
λiSi(T ) .
Fijemos un numerario N y consideremos la probabilidad de valoraci´on asociada Q. Entonces:
X(0)
N(0) = EQ
X(T )
N(T )

= EQ

i λi Si(T )
N(T )

=
M

i=1
λi EQ
Sj(T )
N(T )

=
M

i=1
λi
Si(0)
N(0) ,
de forma que X(0) = M
i= λi Sj(0), que es, claro, el coste de formaci´on de la cartera replicante. De
nuevo, la valoraci´on es independiente del modelo de valoraci´on.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
155

## Página 156

MFC 21-22
Valoraci´on. Fundamentos
ejemplo 3. Liquidar a mercado no altera el valor de la inversi´on (¡faltar´ıa m´as!)
Tenemos una estrategia de inversi´on din´amica y autoﬁnanciada en activos b´asicos. Fijados N y Q, si
llamamos V (t) al valor de la inversi´on, entonces
EQ
V (t)
N(t)

= V (0)
N(0) .
A˜nadimos ahora un ingrediente extra: una regla (tiempo de parada) por la que, si se cumplen ciertas
condiciones sobre los activos b´asicos, liquidamos la cartera (en ese momento, y a precio de mercado).
La formalizaci´on matem´atica pasa por considerar el tiempo de parada τ (que es aleatorio). Denotamos
el valor de la cartera con ese protocolo a˜nadido por V (τ). Pero sabemos que el proceso V (τ)/N(τ)
sigue siendo martingala, as´ı que
EQ
V (τ)
N(τ)

= V (0)
N(0) .
Por tanto,
valor hoy de estrategia con tiempo de parada = V (0) .
Es decir, la opci´on de parar y liquidar la cartera no altera el valor de la inversi´on.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
156

## Página 157

MFC 21-22
Valoraci´on. Fundamentos
Ejercicio
Consideremos la situaci´on en la que tenemos una acci´on S(t) (no paga dividendos) y el bono B(t) cup´on cero de
principal 1 que vence en tiempo T . Comp´arense:
una cartera formada por 1 acci´on comprada de activo S y K unidades del bono vendidos. La cartera se forma hoy
y se liquida a vencimiento T .
La misma cartera inicial, pero si en alg´un momento t ocurre que S(t) = KB(t), liquidamos la cartera (a 0). Si
no, liquidamos en T .
Compru´ebese que, en ambos casos, el valor de la cartera es S(0) −KB(0).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
157

## Página 158

Gracias

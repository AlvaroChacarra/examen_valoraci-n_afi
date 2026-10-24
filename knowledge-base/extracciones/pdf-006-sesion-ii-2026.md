# PDF-006: Sesion_II_2026.pdf

Original: [archivo raw](../../raw/fundamentos/sesion-ii-2026.pdf). SHA-256: `5ffb90e68a69a5b83ac5ba7fa639da3c48159b825427644f22086753ea523397`.

Texto por páginas, con OCR añadido donde el contenido está incrustado como imagen. El OCR puede alterar símbolos; las fórmulas revisadas están en conceptos y PDF-003.

## Página 1

Valoración: 
Modelos Discretos
Máster Executive Finanzas Cuantitativas
José María Contreras
Septiembre  2026

## Página 2

2
1. Modelos binomiales
•
El modelo binomial 
•
Especificación de Jarrow–Rudd 
2. Valoración de opciones en el modelo
•
Opciones europeas
•
Opciones path-dependent 
•
Opciones con barreras 
•
Opciones americanas
•
Replicación/cobertura
•
Dividendos
•
Eficiencia del número de pasos
3. Árbol consistente con la estructura temporal de volatilidad 
4. Construcción y calibración de un modelo discreto de tipos (unifactorial) 
•
Especificación de Black-Derman-Toy (BDT)
Índice

## Página 3

3
Modelos 
binomiales
01.

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

01. Modelos
binomiales

## Página 4

4
El modelo Binomial
t0

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

to At

u4So

u’dSo

u2d?So

ud? So

evolucién del activo d4So

## Página 5

5
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

En este modelo vamos a asumir diversas hipotesis:

Primero, que el tiempo es discreto, en unidades de un cierto At que fijaremos.

Los posibles valores del subyacente vendran dados por una regla multiplicativa
sencilla.

Se supondra que las variaciones del subyacente en distintos intervalos de tiempo son
independientes y que estamos en un entorno de tipos y volatilidad constantes.

Ademas, para los argumentos de replicacién, supondremos que tenemos liquidez
absoluta, que no hay costes de transaccién y que el subyacente no reparte dividendos
(aunque luego los incorporaremos).

## Página 6

6
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

El modelo presenta algunas ventajas:

= se implementa de manera sencilla en un Arbol binario;

= la condicién de no arbitraje en el modelo se traduce en una condicién sencilla (local,
en cada nodo del 4rbol);

= permite valorar opciones cancelables (americanas);

En cierto sentido, es una versién discreta del modelo de Black-Scholes.

## Página 7

7
El modelo Binomial
Objetivo (1):
•
Valorar una Call Europea
¿Ingredientes?

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

|
A

Objetivo (1):
¢ Valorar una Call Europea

QQAQA

iIngredientes?

## Página 8

8
El modelo Binomial
(*) Parámetro estructural. Cambiar este parámetro implica cambios en el precio.
*

## Página 9

9
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

Numerario |

La cuenta bancaria sera nuestro numerario.

Datos de mercado |

Como datos de mercado tendremos

= la cotizacién hoy del subyacente, So;
= el tipo de interés (continuo) anual R;

= la volatilidad anual o del activo subyacente.

Parametros del modelo

El modelo tiene tres parametros:

=» uy d (por “up” y “down”), que seran las magnitudes de los saltos del subyacente.
Digamos que 0 <d <u.

= p, una probabilidad (que sera de valoracién).

## Página 10

10
El modelo Binomial
Dispondremos de 2 datos de mercado (¿Cuáles?) y de 3 parámetros.
Consecuentemente, dispondremos de infinitos árboles que valoren 
nuestro derivado.
Tomaremos el que más nos guste, lo vemos con un ejemplo:

## Página 11

11
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

Evolucion de los activos basicos |

Postulamos la siguiente evolucién de los activos basicos:

A 2RAt

= la cuenta bancaria vale 1 hoy, vale e”4! en tiempo At, e en tiempo 2At, etc.:

By = eRGAD |

= En tiempo jAt, la cotizacién S; del activo subyacente puede tomar, en términos del
valor de tiempo anterior, dos tinicos valores:

s S;-1-u_ con probabilidad p;
7 | S;-1+d_ con probabilidad 1 — p.

11

## Página 12

12
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

Es cémodo representar los posibles valores del subyacente en un arbol binario como el
que sigue:

u'So

u2d2So

ud? So

evolucion del activo

at So

## Página 13

13
El modelo Binomial
En el esquema previo, ¿Cuántos escenarios tiene mi modelo? (ie. Nº 
sendas)
¿ Y si disponemos de 50 pasos?

## Página 14

14
El modelo Binomial
Ojo! Subir y bajar es equivalente a bajar y subir… (si no fuese así el 
problema sería difícil de implementar para un número de saltos 
elevados)
Consecuentemente, el árbol crece de forma lineal y no exponencial.
¿u y d?

## Página 15

15
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

La descripcién matematica de la estructura anterior es como sigue:

= Tenemos unos instantes de tiempo 0, At, 2At,.... Usaremos
referirnos al tiempo jAt.

= El espacio de escenarios 2 = {w1,w2,...} esta formado por
“bajadas” y “subidas” (“sendas” en el Arbol):

el subindice j para

istas w de sucesivas

w = (€1,€2,€3,€4,...), donde los ¢; son 4

Si paramos el drbol en tiempo A/At, tenemos 2™ escenarios:

wy =(-1,+1,..., +1)
Wom_, =(—1,-1,..., +1)
Wom =(—1,-1,..., —1).

15

## Página 16

16
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

= Tenemos una probabilidad P definida sobre cada uno de estos escenarios w, que
viene dada por la asignacion de probabilidad p a “subir’ y probabilidad 1 — p a
“bajar” (mds la independencia).

Asi, si w = (€4,€2,€3,€4,.--),
P(w) = pie ej=+t}, (1 —p) #AG: €3 = —1}

Esto es, p elevado al ntiimero de “subidas” por (1 — p) elevado al de “bajadas”.

Codificamos las sucesivas subidas y bajadas con unas variables de estado
Yi, Y2, Y3,..., independientes e idénticamente distribuidas. En un escenario w, la
variable Y; vale 1 o —1 en funcién de que en ese tiempo jAt haya una subida o una
bajada. De forma que
y= { +1 con probabilidad p;
J’ ~~ | —1. con probabilidad 1 — p.

La suma 7, Yj es un camino aleatorio (no simétrico, si p # 1/2). Estas variables de
estado determinan la evolucién de todos los activos.

16

## Página 17

17
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

— ,jRAt
L j= e! ;

y el activo subyacente S’,, que en tiempo 0 vale So y que, para tiempos posteriores, es
una variable S; que toma valores en cada nodo de generacién j con la ya mencionada

prescripcion
Ss.

J

_ J u-S;~1 con probabilidad p;
~ | d-$j-1 con probabilidad 1 — p.
Observacién

La filtraci6n F; = o(Yj,..., Yj) recoge la informacién desvelada hasta tiempo jAt.

Los activos basicos son la cuenta bancaria, que en tiempo jAt vale

La variable S; se puede escribir en funcién de S;_1 y la variable Y; de la siguiente manera:

8 = 5-a[6 (EF) -4(>)].

Esto supone que S; € Fj.

generacion j en el que el valor del activo es S; = S.

Finalmente, la variable C';(S') registra el valor del derivado C' en un nodo de la

17

## Página 18

18
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

Miramos hasta tiempo J/ At.

= Hay 2” posibles evoluciones del subyacente, cada una con su propia probabilidad.

= Pero en ocasiones (por ejemplo, para valorar opciones europeas) no nos interesard la
senda seguida, sino el valor final del subyacente, para el que tenemos solo MW/ +1
posibilidades. Podemos codificar estos AJ + 1 escenarios de 0 a M, en funcién del
numero de “subidas”.

RM At

—> la cuenta bancaria toma el valor 3); = e en todos ellos;

— mientras que el subyacente Sj, puede tomar los \/ + 1 valores siguientes:
SoutaM—*; k=0,1,...,M,

[ escenario | subyacente | probabilidad

M Sou p

con probabilidades

P(S\r=Sou*d!—*) = P(Bin(M, p) =k)
= (pha pr

k

18

## Página 19

19
El modelo Binomial (probabilidad)

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial (probabilidad)

Queremos que nuestro modelo de evolucidn sea certificado.

Numerario | La cuenta bancaria 3; = eJRAt ser nuestro numerario.
Probabilidad de valoracién |

Queremos que la probabilidad P sea de valoracion (para ese numerario). Es decir, que
los procesos de precios de los dos activos basicos, la cuenta bancaria y el subyacente,
escritos en unidades del numerario (es decir, descontados), sean martingala. La evolucién
de la CB descontada es obviamente una martingala. Para el subyacente, exigimos que

S;
J
Ep (sam

Sy ,
F)-1) = TG=pRAt para cada j = 1,2,...

Una expresién que parece aparatosa, pero que se traduce, simplemente, en la siguiente
condicién, que garantiza que P sea de valoracién:

(condicién de martingala) up + d(1— p) = e®™*

19

## Página 20

20
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

Observacién

DETALLE:

Bp (4 |F)-1) = aw Ep(Sj-1[5 (+1) -

= Saar Be( (5 +0) - 55-0] |Fi

1) =

d
297

Sj-

SRA

v} 7-2)

=z (5 BP( (Y;+D — SE p(y; 1) ))

[up + d(1 — p)] (utilizando que Ep(Y;) =2p—1).

20

## Página 21

21
El modelo Binomial
¿Sentido financiero?

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

~Sentido financiero?

up +d(1—p)=

¢ RAt

21

## Página 22

22
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

Valoracién de activos (replicables)

Si ahora C’' es un activo replicable (con activo y dinero), entonces su proceso de precios

en términos del numerario (es decir, descontado) serd también martingala:

C;

Y
E Cit
P\ CjRAt

F)-1) ~ CG-DRAt

Y, en particular,

Cj
Ep ( ej RAt

Co

C;
Fo) =F esto es, Ep (sz) = Cp.

O, como escribiremos habitualmente,

Co jRAt Ep(C;)

Esto es, el precio hoy es el promedio (descontado) de los flujos futuros.

Usaremos estas dos formulas constantemente en las siguientes valoraciones.

22

## Página 23

23
El modelo Binomial (calibrado del modelo)

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial (calibrado del modelo)

Tenemos tres datos de mercado: el tipo R, la cotizacién inicial So y la volatilidad anual
del activo o.

e Ya hemos calibrado al dato Sp exigiendo que la evolucién arranque en ese valor.

e Ahora vamos a exigir que la evolucién del subyacente acumule exactamente una
volatilidad anual o. Es decir, que la desviacién tipica de los rendimientos del activo en
un afio valga o:

. Sn
a= V(in -*) .
So
La rentabilidad (continua) en un afio se expresa directamente en términos de las

rentabilidades en los periodos At sucesivos:

Sn Si Sy Sn-1 Sn) _ Sj
namn(SP )= on -

Pero las rentabilidades parciales In(.S;/;~1) son variables independientes (e idéntica-
mente distribuidas). Asf que la varianza de la suma es NV veces una de las varianzas.

23

## Página 24

24
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

Estos rendimientos parciales son

in ( Sj ) _ { Inu con probabilidad p

Sit Ind_ con probabilidad 1 — p

y un pequefio calculo nos dice que esas varianzas individuales son

2

V[n ( Si | = p(1—p)(In(u) —In(d))? asf que a? = N p(1 —p)(In(w) — In(d))?.

Sj-4

Observacién

DETALLE:

E[ In ( Si )] = pin(u) + (1 — p) In(d); B| In? (= ) = pln?(u) +(1-—p) In?(d)
S51

2 cdlculos

S;
V[in( J )] = pln?(u) + (1 — p) In?(d) — (p n(u) + (1 — p))? ASS p(t — p)(In(u) — In(d))?.

24

## Página 25

25
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

Y como NAt = 1, obtenemos la segunda ecuacién:

(ajuste al dato de volatilidad) oVAt = Vp(1—p) [ In(w) — In(d) |

25

## Página 26

26
El modelo Binomial

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

El modelo Binomial

En resumen, dados los datos de mercado R, So y 7, podemos construir un modelo de
evolucién (de paso At)

a libre de arbitraje (certificado);

a de forma que la volatilidad anual sea exactamente o

sin mas que exigir que el activo arranque en el valor So y que los pardmetros u, d y p
verifiquen el par de ecuaciones:

eRAt — up + d(1—p)

o VAt = \/p(1 — p) (Inu — Ind)

Obsérvese que se trata de un sistema no lineal de dos ecuaciones. Y que hay tres
pardmetros en el modelo (uw, dy p).

26

## Página 27

27
Especificación de Jarrow–Rudd

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Especificacion de Jarrow—Rudd

Para empezar fijamos

Las dos ecuaciones son ahora

, ut+d
eRAt — 5) (condicién de martingala)
Inu —Ind
oVAt = —_ > (ajuste al dato de volatilidad)

La solucién explicita de este par de ecuaciones viene dada por:

u= eRAt ervAt 2
; erVAt + e-ovAt

d= eRAt eaoVAt 2
erVAt + e-ovAt

27

## Página 28

28
Valoración de 
opciones en el 
modelo
02.

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

02. Valoracion de
opciones en el
modelo

## Página 29

29
Opciones europeas
Objetivo: Valorar una opción call europea.
Recuerda, tal y como se vio en la página 22:

## Página 30

30
Opciones europeas

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones europeas

Método 1. Valoracién con formula

Hay A/ +1 posibles pagos de la opcidn, tantos como posibles valores del subyacente a
vencimiento (véase la pagina 14). Aplicamos directamente la formula

Co = eT MPA! Bp(Cyy) .

pues el valor medio de la derecha se puede calcular muy facilmente.

Notese primero que se trata de una suma (ponderada) con \/ + 1 términos. En cada
escenario,

= los valores que se promedian son los nimeros

f (Sou*a—*) :

’

= y se promedian con las probabilidades

(i: eae.

30

## Página 31

31
Opciones europeas

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones europeas

En el caso de la call con strike A’, los flujos son
Mk -\+
(Sou*a™ _ Kk)

y por tanto el valor hoy se obtiene con la siguiente formula:

M
M
Co= (eM RAY) . (Sou*a!—* —K)* (

descuento flujo

a —p)M-*

probabilidad

Calculo del valor hoy de la call de strike K = 84.

Calculo del valor hoy de una opcién europea con un payoff arbitrario.

31

## Página 32

32
Opciones europeas

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones europeas
Método 2. Valoracién en el arbol |

Se trata de interpretar la condicién

C5 .;
J . _ j-1 ae 1 _ ,—-RAt Y IZ.
Ep (ses Fi-1) co=pRaT? «qwe reescribimos Cj_1 = € Ep(C;|Fj-1)
como un procedimiento de cdlculo recursivo (hacia atrds) (M-1)At Mat

en el arbol. Nos fijamos, por ejemplo, en los dos nodos
superiores en tiempo A/At (vencimiento). Los valores C, y
Cy son conocidos. El valor C'y se obtiene aplicando la formula
de arriba, que aqui simplemente nos dice que

Cr= e RAL (pCa +(1- p)Cb) :

Se procede igual con los demas nodos de tiempo (JZ — 1)At, hasta tenerlos todos.
Luego se repite el proceso para los nodos de tiempo (A/ — 2)At, etc., hasta llegar a Co.

Arbol de valoracién de la call europea de strike K = 84.

32

## Página 33

33
Opciones europeas

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones europeas

Método 3. Simulacién |

Una manera alternativa de utilizar la férmula

Co =e MEAS Ep(Cuy)

pasa por interpretar la esperanza de la derecha como un promedio sobre todos los
posibles escenarios (sendas en el arbol). Ese promedio involucra 2“ términos, uno por
senda, cada uno con una cierta probabilidad (o la misma, en el caso p = 1/2).

Caben, pues, dos alternativas:

a Exhibir todos los escenarios/sendas, anotar el pago de la opcidn en cada una de ellas,
y promediar esos valores con las respectivas probabilidades (y descontar al final);

= o bien, si el universo de escenarios es demasiado grande, muestrearlo, simulando un
ntimero suficiente de escenarios.

Simulador en Excel para valoracién de europeas.

33

## Página 34

34
Opciones path-dependent

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones path-dependent

Valoraci6n de derivados path-dependent

Tenemos un instrumento C' que paga, a vencimiento J/ At, una cierta cantidad

que depende de (quizds) toda la senda de cotizaciones del subyacente.

Su valor hoy sera
Co = eM PAT Ep(Cy) = e MBO" Ep(f(51, S2,.--.Sar))-

a jValoracién con formula? La anterior es una férmula para el valor de la opcidn; pero
se trata de una suma con 2™ términos.

a {Valoracion en el arbol? En general, no es posible. Digamos que queremos valorar una
call asidtica en la que el flujo depende de la media aritmética A de las cotizaciones.
Consideremos un arbol binomial con sdlo dos periodos.

34

## Página 35

35
Opciones path-dependent

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones path-dependent

En una opcién usual, calculamos el flujo a partir de los nodos del ultimo nivel y
procedemos hacia atras en el Arbol. Pero ahora, aunque el activo en dos periodos
alcanza tres valores, la media A toma cuatro distintos, pues “distingue” entre:

2
; : 1 u ud urS
en el camino S > uS > udS, A vale S (a “ )

en el camino S > dS > udS, A vale S (=~). _

3

a |; Valoracién por simulaciédn? Es el método mas razonable: muestreamos el espacio
de los 2™ escenarios, sorteando sendas de cotizaciones del subyacente en el drbol,

anotamos en cada muestra el payoff de la opcién, y luego promediamos con media
aritmética (ademas de descontar).

35

## Página 36

36
Replicación/cobertura

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Replicaci6n/cobertura
Replicaci6n/cobertura en un solo periodo

Partimos de la situacién general:

cuenta bancaria subyacente derivado
eRAt uSo Cu
1 _ se —
eRAt dSo Ca
Los valores C,, y Ca son conocidos. Vamos a formar una cartera con a unidades en la
cuenta bancaria y 3 en subyacente. Los valores de a y 3 son la solucién del sistema de

ecuaciones

Cy = aePAt + Bu So
Ca= ae®! + Bd So

Una vez obtenidos los valores de a y 3, valoramos el derivado:

Co =at+BSo.

36

## Página 37

37
Replicación/cobertura

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Replicaci6n/cobertura

Resolviendo el sistema de ecuaciones anterior, deducimos que el activo C’ equivale a la
cartera que consta de (3 unidades de subyacente, donde

__Cy—Ca __ incremento de valor del derivado
~ Su—Sd_— incremento de valor del subyacente

B

Esta cantidad 3 se conoce, en la jerga habitual, como delta.

Se trata de cobertura estatica: un solo periodo de tiempo.

37

## Página 38

38
Opciones con barreras

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones con barreras
Valoraci6n de opciones con barrera

Veremos ahora cémo valorar opciones con barrera usando Arboles. Las opciones con
barrera mas simples tiene férmulas cerradas, pero sdlo las mas simples. En general,
cuando la estructura de la barrera (o barreras) es ligeramente compleja, es necesario
usar Arboles o simulaciédn Montecarlo, con cierto cuidado en cualquier caso.

Consideremos el activo que ya hemos usado anteriormente y que tiene el arbol de
evolucion siguiente:

oO 1 2 3 4 5 6

80,000 86,983 94,576 102,832 111,809 121,569 132,181
73,150 79,535 86,478 94,027 102,235 111,159

66,887 72,725 79,074 85,976 93,481

61,159 66,498 72,303 78,614

55,923 60,804 66,112

51,134 55,598

46,756

Y supongamos que queremos valorar una call con barrera con

= strike 84;

= barrera knock-out en 100.

38

## Página 39

39
Opciones con barreras

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones con barreras

Podemos incorporar estos datos al arbol. Los pagos a vencimiento o extincidn de la
opcidn son los siguientes:

strike 84
barrera KO 100

tiempo
0,0000 0,000 0,0000 0,0000
0,000 0,0000

Y ahora procedemos hacia atrds en el Arbol. Rellenamos los valores del nivel anterior
al vencimiento (que la barrera no haya determinado ya) y luego el nivel anterior. Y asf
sucesivamente. El resultado es:

strike 84
barrerakKO__100
tiempo 0 1 2 3 4 5 6

| 13266 _| 11,4753 1,1812 0,000 0,000 0,000 0,000

12,1802 1,718 2,3644 2,3663 0,0000 0,0000

0,5906 1,182 2,3663 4,7366 9,4811

0,0000 0,000 0,0000 0,0000

0,000 0,0000 0,0000

0,0000 0,0000

39

## Página 40

40
Opciones Americana
Quieres vender un coche.
Recibes ofertas (por ejemplo, un total de 10)
Problema, no puedes elegir entre todas las ofertas, tendrás que ir 
aceptando o rechazando una a una sin poder volver al pasado ni 
dispondrás de información sobre el futuro.

## Página 41

41
Opciones Americana

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones Americana

41

## Página 42

42
Opciones Americana

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones Americana

1
. eN
os

niim ex de ofertas zestantes

vabr
um bral

ntim ex de ofertas estantes

En general, el umbral para aceptar una oferta cuando quedan k: ofertas sera el valor
que se tiene cuando quedan k — 1 ofertas:

U; = Ve-1 -

De manera que

Vi = E(Ee|Fk > Vi-1)- P (Fk > Viet) + Vi- P (Fie < Vi-1)

de donde resulta que

1+V2,
y=.
k 2

## Página 43

43
Opciones Americana

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones Americana

Valoraci6n de opciones americanas en el arbol

En las opciones americanas, el poseedor de la opcidn tiene el derecho de ejercerla en
cualquier momento entre el comienzo del contrato y el vencimiento.

Valoracién de una put americana. Denotaremos por V,, los valores de la opcién put en
el paso n; 0, con mas precisién, por V;,(.5'), si queremos hacer explicita la dependencia
en la cotizacién S' en ese instante.

En el instante n, el poseedor de la put tiene dos opciones:

1) Ejercer en ese instante y obtener (K — S,,)*. Este es el valor de ejercicio, que

denotamos por VE,,:
VEn(S,) = Ue ~ Sn)t .

11) No ejercer: se tiene entonces un valor de continuacién VC,, que viene dado por el
valor medio (riesgo-neutro)

VC, (S,) = eT RAL [PVn+1(Sn . u) + (1 _ Pp) Vn4il Sn . d)| = e RAR (Vn4ilSn)

El valor V,, sera el maximo entre VE,, y VC,,.

43

## Página 44

44
Opciones Americana

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones Americana

De manera que
VER (Sn) = (ik _ Sn)t

Vin(Sp) = max
VCn (Sn) = e RACE (Vin+1|Sn)

Como ademas en el instante del vencimiento tenemos que
_(k -
y= (K- Sn)”,

podemos implementar un procedimiento recursivo (regresivamente) para calcular el valor
de la put americana en el instante 0.

44

## Página 45

45
Opciones Americana

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones Americana

Call americana vs. call europea

En principio, las opciones americanas han de ser mas valiosas que las correspondientes
europeas. Pero la call americana (sobre un subyacente que no reparte dividendos) vale
lo mismo que una call europea. Esto es, nunca conviene ejercer antes del vencimiento 7’.

La paridad call-put nos dice que, en cualquier instante t < T, el precio de la call europea
C(t), el precio de la put P(t) (ambas con strike [’) y el tipo R estan relacionados por:

C(t) = P(t) + S(t) -Ke RP) =5 C(t) > S(t)-Ke®T% > S(t) -K.

Es decir, la call europea es siempre mas valiosa que el ejercicio anticipado.

45

## Página 46

46
Opciones (Acelerador cálculos)

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Opciones (Acelerador calculos)

Arbol de precios de Arrow-Debreu

C={A-(1—p)+B-p]-e ®**

46

## Página 47

47
Dividendos

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Dividendos

Sp = Soel(R-@)-2?/2IT +e VTN (0,1)

Sacando un factor e eT, vemos que, si K, R, y T fijos:

Call con rentabilidad por dividendos @ y precio de activo Sg
equivale a
Call con rentabilidad por dividendos 0 y precio de activo e aT . So

47

## Página 48

48
Dividendos

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Dividendos

Dividendos fijos

Supongamos que en tiempo 7’ recibiremos un So St
Unico dividendo conocido D (por accién).  In- t
terpretamos que la cotizaci6n S; del activo tiene

dos partes: por un lado, el valor (descontado) del dividendo; y, por otro, la parte con

incertidumbre, que llamaremos S/*:

J dividendo D
|
T

|
i
0 T

S, =S*4+D e~RT-9 sit <T;
Ss =St sit > T.

El valor de la inversion en el activo en tiempo t viene dado por
SF +D e R(T -t) ,
que coincide con la cotizacién hasta la fecha de pago del dividendo. Queremos valorar

un derivado sobre este subyacente. Ndtese que el pago del derivado depende de la
cotizacion del activo.

48

## Página 49

49
Dividendos

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Dividendos

Implementacion en el arbol binomial

Supongamos que se van a recibir dos dividendo Dy dividendo Do

dividendos (conocidos hoy), D; y Do, 0 Ty Tn Pr
+—e=}—}

i | | | | i
en tiempos JT, y T>. La opcidén que SZ Te
queremos valorar vence en tiempo 7’.
Fijamos un At para nuestro Arbol binomial, de manera que \/At = T. Los inputs de

mercado son R, el tipo anual, o, la volatilidad del subyacente y So, la cotizacién hoy
del activo.

Para valorar el derivado necesitamos el arbol de la cotizacién S;, que consta de dos
partes: S*, con la incertidumbre, y PD;, el “proceso de dividendos” (sin incertidumbre):

S,= S'+PDz,
donde

PD, = D, e (1-HkR si t<T}, 4 Ds e7 (Ta-)R si t< Ts,
0 sit > 7), 0 sit > Td.

49

## Página 50

50
Dividendos

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Dividendos

Procedimiento:

1. Con los valores de R y o se determinan los valores de los parametros wu, d y p.

2. Con el valor S§ y los valores de u y d construimos el arbol de valores de S* hasta
tiempo T (esto supone que consideramos que a es la volatilidad de S*).

3. Calculamos los valores del proceso de dividendos PD; (nétese que es un vector fila
en Excel, pues no tiene incertidumbre).

4. Construimos el Arbol de cotizaciones S; a partir del de S* aumentando todos los
valores de los nodos de tiempo jAt con el correspondiente valor PDja;. Este arbol
no sera martingala (con p), pero nos servird para valorar la opcidn.

5. Podemos también construir el arbol del valor de la inversién en el activo, cuyos
valores vienen dados por S# + D, e~1~-9F 4 Dy e~(P2-OR

6. La valoracién del derivado utiliza el arbol de cotizaciones S; y los promedios se
calculan con p.

50

## Página 51

51
Eficiencia del número de pasos
Problema:
•
La naturaleza discreta infiere que el modelo valore un mismo producto con precios 
diferentes según el numero de pasos (equivalentemente el periodo temporal entre 
nodos del árbol). 
•
Valoración de una opción americana con vencimiento 1 año, valorada en base al 
número de saltos indicados en el eje X.

## Página 52

52
Eficiencia del número de pasos
Motivo:
•
La discontinuidad de la delta de la opción a vencimiento. 
Mejora en la eficiencia del número de pasos:
•
Emplear Black-Scholes (en lugar del valor esperado del árbol) en los nodos del árbol del 
instante previo al vencimiento de la opción.

## Página 53

53
Eficiencia del número de pasos
Consecuencia:
•
Este cambio en el modelo hace que se consiga una mejora considerable en la 
precisión de valoración de las opciones americanas.

## Página 54

54
Árbol consistente con 
la estructura temporal 
de volatilidad
03.

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

03. Arbol consistente con
la estructura temporal
de volatilidad

## Página 55

55

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Ajuste del arbol a la curva de volatilidades

Construiremos el arbol casi como en el caso general (de Jarrow—Rudd), pero para poder
captar la estructura de volatilidad y para que, ademas, el arbol sea recombinante, los
intervalos de tiempo de los pasos del arbol no serdn todos iguales.

Datos

= una curva de volatilidades spot a ciertos vencimientos t1, t2,..., 7. Supongamos, por
comodidad, que el ultimo vencimiento coincide con el de la opcién. Llamemos a estas
volatilidades

a(ti),o(t2),...,0(T)

™ una curva de tipos spot a ciertos vencimientos (por ejemplo, los mismos de antes):

R(t), R(t2),.... R(L)

Las varianzas acumuladas hasta tiempo t; son las cantidades V; = t;o7(t;). La varianza
acumulada hasta el plazo final es To?(T).

55

## Página 56

56

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Procedemos en etapas:

Fijamos una unidad de volatilidad A. Para ello, decidimos cudntos pasos N tendra el
arbol hasta tiempo IT. Tomamos A de manera que

NA? =To?(T).

Para ese nivel de referencia A, construimos el arbol
aditivo, con todas las probabilidades iguales a 50%,
pero sin especificar el intervalo de tiempo que abarca
cada paso.

La varianza acumulada hasta tiempo j es jA?.

56

## Página 57

57

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Buscamos ahora la serie de tiempos

T,.To,....Tn

tales que la varianza acumulada hasta tiempo J; sea justamente j A”. As/, la varianza
en cada intervalo [T;_1, 7] es A?.

(Los tiempos T; se obtienen interpolando en la tabla que relaciona los tiempos t; con
las varianzas acumuladas t;7(t;)).

Los tiempos que marcan los intervalos del arbol son los T;. Los valores del arbol son los
usuales, pero los intervalos de tiempo no son iguales.

Obtencién de intervalos de tiempo del érbol

57

## Página 58

58

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Calculamos las derivas que corresponden a los nodos de tiempo T;;, y que resultan ser:

T)RT}) |

2 j
deriva por tipos —> e ajuste de deriva por volatilidades —> ==]

eA+e-A

(para las primeras, habrd que interpolar en la curva de tipos).

Observacién

EI ajuste de la deriva proviene de que la esperanza de la variable que toma los valores eA y eA (con probabilidad 1/2
cada uno) es, obviamente, (e4 + e74)/2.

El Arbol del subyacente se construye combinando estos tres efectos, de la
m

anera habitual: 5 j
So kA ej R(T)) |
0 € € cA + CoA
(j depende del paso, & del nodo).

58

## Página 59

59
Construcción y 
calibración de un 
modelo discreto de 
tipos (unifactorial)
04.

## Página 60

60

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Vamos a prescribir una evolucién aleatoria en el tiempo de tipos de interés. El tiempo
estara discretizado y representaremos los posibles estados con un Arbol binomial.

Queremos que este modelo de evolucién esté libre de oportunidades de arbitraje, para
que permita valorar instrumentos cuyo precio se derive de los tipos (promediando flujos
adecuadamente descontados).

= Interesara que este esquema de valoracién sea capaz de dar correctamente los precios
de referencia del mercado, que en nuestro caso seran los bonos cupoén cero de los
sucesivos vencimientos (y, quizas, algunos instrumentos con opcionalidad, como caps,
swaptions). Es decir, calibraremos el modelo a los precios de mercado.

= Y argumentaremos que, una vez calibrado, el esquema sera también capaz de valorar
“adecuadamente” (jinterpolacidn!) los instrumentos que no estén en mercado.
Empezamos con toda generalidad. El paso temporal At esta fijado.

Vamos a construir un arbol binomial a la Jarrow—Rudd (todas las probabilidades son 1/2)
para el tipo (continuo, anual) a plazo At.

60

## Página 61

61

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Denotamos? por R;, al tipo (continuo, anual) a plazo At que tenemos en tiempo kAt.

En nuestro esquema binomial, 2; es aleatorio, y toma k +1 valores, uno en cada nodo.

tiempo 0 tiempo At tiempo 2At
1

Ro toma 1 valor
R , toma 2 valores

Rz toma 3 valores

Ro variable Ry variable Ro

3Una notacién més precisa para Ry, pero que aqui no usaremos, seria R(kAt, (Kk + 1)At). Elegimos tipos continuos
también por comodidad notacional, aunque también podrian ser tipos simples (y, de hecho, ésa suele ser la eleccién habitual).

61

## Página 62

62

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Elecci6n de numerario

Supongamos que ya tenemos construido el arbol con los valores de los tipos (mas
adelante propondremos un esquema para parametrizar esos valores).

Las consideraciones probabilisticas que haremos a continuacion se refieren a trayectorias
en el arbol anterior, a las que nos referiremos genéricamente como trayectorias w.

Ahora elegimos el numerario para descontar precios: la cuenta bancaria, cuyo valor en
tiempo k denotamos por 3(k).

B(k) es la variable aleatoria que recoge la capitalizacién de 1 euro de tiempo 0 (en
depésito rodante cada At) hasta tiempo kAt.

Por ejemplo, 3(0) = 1, mientras que 3(1) = e*04*. A partir de tiempo 2At es ya una
variable aleatoria.

Pero en general el valor de 3(k) no sdlo depende del nodo de tiempo k en el que
estemos (de entre los k + 1 posibles), sino también del camino w que nos haya Ilevado
a ese nodo (es path dependent).

62

## Página 63

63

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Por ejemplo, para tiempo 2 tenemos

Ry (nodo yj
B(2) = e( Rot Ri (nodo up)) At

trayectoria Ww

N

Ry (nodo up)
B(2) _ e( Rot Ri (nodo up)) At
trayectoria wa

trayectoria w3 B(2) — e(Ro+R1(nodo down)) At

(?

R 1 (nodo down)

trayectoria w4
B(2) _ e( Rot Ri (nodo down)) At

Ry (nodo d

y

Obsérvese la diferencia entre las trayectorias wo y wg, que llegan al mismo nodo central.

63

## Página 64

64

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Metodologia de valoracion

Instrumentos de mercado

Los instrumentos que vamos a considerar como “de mercado” son los bonos cupén cero
de distintos vencimientos*.

Es importante sefialar que todos los vencimientos deben ser multiplos de At, el paso
elegido en el arbol.

Denotaremos por
P(k,T)

el precio en tiempo At del bono cupon cero de nominal 1 y vencimiento T’ (un multiplo
de At).

De nuevo es una cantidad aleatoria que depende, ademas de k: y de J’, del nodo de
tiempo k en el que estemos y, quizas, de la trayectoria w que nos lleve hasta él.

4 Aunque luego incluiremos instrumentos con opcionalidad.

64

## Página 65

65

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

No arbitraje

Siguiendo nuestra idea general de valoracion por no arbitraje, pretendemos que el proceso
que da cuenta, en cada tiempo k, del precio (descontado con la cuenta bancaria) del

bono que vence en tiempo 7’,
( 2)
B(k) k

sea martingala (bajo la probabilidad considerada).

Esto supone que

&) p(2en

B(k)

— P(k 1,7)
Fe) =D

para cadak =1,2....

## Página 66

66

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Valoraci6n

Si se cumpliera (x), entonces, aplicdandola reiteradamente obtendriamos el precio hoy
del bono cupon cero de vencimiento 7’:

P(k.T)\  P(0,T)
B( B(R) )- B(0)

Analogamente, si X es cualquier instrumento (replicable en términos de estos bonos)
cuyo payoff conozcamos, por ejemplo, en tiempo k, entonces podriamos valorarlo de
manera andloga:

X(k)\ _ X(0)
e(S) = BO)"

Y si X no fuera replicable, esta metodologia atin nos proporcionaria un precio del
instrumento (por interpolacidn).

66

## Página 67

67

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

No arbitraje, ya en el arbol

Parece que (x) es una condicién muy aparatosa, dado que todas las cantidades
involucradas dependen de las trayectorias seguidas.

Pero obsérvese en qué se traduce en nuestro esquema binomial.

Digamos que estamos en un nodo de tiempo k:—1 (nodo tiempo kK—1 tiempo k

inicial) y consideremos sus dos vecinos de tiempo k
(nodos up y down).

nodo up

Al nodo inicial hemos Ilegado siguiendo una cierta
trayectoria, digamos w, que determina el valor 3(k—1)
correspondiente.

trayectoria w

En ese nodo inicial, R;,—1 tiene un cierto valor, el
correspondiente del arbol de tipos.

La condicién de martingala se escribe de la siguiente manera:

(4x) 1 P(nodo up,T) | 1 P(nodo down,T) — P(nodo inicial, T)
5 .

3(nodo up) 2  B(nodo down) 3(nodo inicial)

67

## Página 68

68

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

En esta formula, cuando escribimos nodo up (0 nodo down, 0 inicial), estamos conside-
rando no sdlo el nodo en el que estamos (y el tiempo al que corresponde), sino también
“cémo” hemos llegado a ellos.

Pero obsérvese que

B(nodo up) = B(nodo inicial) - e/**-144

B(nodo down) = 8(nodo inicial) - e**-14¢

De manera que la formula (*x), la condicién de martingala, se escribe simplemente
como

(* « x)

Penne Plnode up, 7’) + P(nodo down, T’)

5 ) = P(nodo inicial, T)

Esta sencilla observacién es clave, pues nos va a permitir valorar los bonos cupon cero
de los sucesivos vencimientos sin mas que utilizar recursivamente la formula («x « x)
anterior.

68

## Página 69

69

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Simplemente hay que observar que sabemos que el bono que vence

en tiempo J’ vale justamente 1 en todos los nodos de tiempo 7’.
Digamos, por ejemplo, que el drbol de valores de tipos empieza 0
como mostramos a la derecha.

Por ejemplo, el bono que vence en tiempo 1:
1

P(0,1) P(0,1) = e~RoAt
1

El que vence en tiempo 2:

=RDat 1
e

P(0, 2)

1 P(0,2) = e~Ro%

en RY At 4, e— RY At
2

A

—R at
ey

Y asi, sucesivamente, hasta obtener los precios de todos los bonos cupén cero de los
sucesivos vencimientos At, 2At,3At... Esto es, la curva cupon cero, CCC, de hoy.

69

## Página 70

70

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

jAtencidén!, los precios asi obtenidos son los que proporciona

a el Arbol de valores de los tipos;

m junto con la hipotesis de no arbitraje.

Los precios son tales que no hay manera de disefiar una oportunidad de arbitraje utili-
zando los instrumentos de mercado (los bonos cupén cero de los distintos vencimientos).

Pero ademas querriamos que la CCC que proporciona el modelo coincida con la CCC
que observamos hoy. Es decir, calibrar el modelo ajustandolo a los precios observados.

Para ello podriamos variar los valores del arbol de tipos hasta que la discrepancia (por
ejemplo, medida en términos cuadraticos) entre las dos curvas cupon cero fuera lo
menor posible.

Aunque para esto es mejor prescribir un modelo paramétrico para la evolucion de los
tipos. Una de estas prescripciones es el esquema Black-Derman-Toy, que pasamos a
describir a continuacion.

70

## Página 71

71

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

Esquema Black-Derman-Toy

Postulamos una evolucién lognormal de los tipos, analoga a los esquemas tipo Black—
Scholes. Digamos que tenemos, como datos,

= la curva cupon cero de hoy;

a y la volatilidad constante® o del tipo (continuo, anual) a plazo At.
tiempo k

oo. ., . j=k
Vamos a cambiar ligeramente la notacién para referirnos a los ]

tipos. Etiquetamos los k: + 1 nodos de tiempo k: con los valores pak?

@ j=k-4

—k,—-(k —2),-(k —4),....,k -4,k -2.k

Z . . =—k
(obsérvese que van de dos en dos), que indican el balan- JaTkes
ce de subidas y bajadas en el arbol. Llamaremos, para cada ja—k+2

j=-k

j=—k,-(k—2),...,k—2,k, R(k, 7) al valor del tipo en el nodo
j de tiempo k.

5EI caso de volatilidad no constante requiere un procedimiento mds complicado, que se verd en sesiones venideras.

71

## Página 72

72

**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**

La especificacién del valor de R(k, 7) es directa:

La funcidn positiva U(k) recoge diversos ajustes de convexidad. El factor con la
exponencial recoge la incertidumbre del modelo.

‘fancién 0 4,041% _1,953%]_¢ 9.641% 3.843%,

Para construir el arbol de tipos

e@ construimos, como es habitual, el arbol de
ruidos (el de los valores e7¥"7):

tipos (continuos,

e y luego incorporamos a cada nodo de tiempo
k: el factor U(k:) correspondiente.

Una vez construido el arbol de los tipos, aplicamos el esquema general de valoracién
para determinar los precios de los bonos cupén cero de los distintos vencimientos.

Finalmente, calibramos el modelo para que estos precios coincidan con la curva cupon
cero de hoy. Para ello, variamos la funcién U(k) hasta que la discrepancia entre las dos
curvas sea minima.

72

## Página 73

73
Véase para más detalle 
Documentación teórica del 
Curso

## Página 74

Gracias

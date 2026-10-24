# PDF-003: MFC-26-valoracion-arboles_Teoria.pdf

Original: [archivo raw](../../raw/fundamentos/mfc-26-valoracion-arboles-teoria.pdf). SHA-256: `ee31dff2be768db07c304834dec06717af2be84e3c7126914a18855e56234ef4`.

Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.

## Página 1

Máster Executive Finanzas Cuantitativas
Valoración: 
Modelos Discretos
José María Contreras
jcontreras@afi.es

## Página 2

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
´Indice
1. Modelos binomiales
El modelo binomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
Especiﬁcaci´on de Jarrow–Rudd . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Otras especiﬁcaciones. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .29
2. Valoraci´on de opciones en el modelo
Opciones europeas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .34
Opciones path-dependent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
Opciones con barreras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Opciones americanas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .45
Replicaci´on/cobertura. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .54
Dividendos y futuros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3. ´Arbol consistente con la estructura temporal de volatilidad . . . . . . . . . . . . . . . . 74
4. Construcci´on y calibraci´on de un modelo discreto de tipos (unifactorial) . . . 84
Especiﬁcaci´on de Black-Derman-Toy (BDT)
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
2

## Página 3

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
1. Modelos binomiales
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
3

## Página 4

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Vamos a construir un modelo discreto (en tiempo y valores) de evoluci´on de la cotizaci´on
de un subyacente, que ser´a libre de arbitraje y que nos permitir´a valorar activos derivados
(europeas, americanas, path-dependent, etc.).
En este modelo vamos a asumir diversas hip´otesis:
Primero, que el tiempo es discreto, en unidades de un cierto Δt que ﬁjaremos.
Los posibles valores del subyacente vendr´an dados por una regla multiplicativa
sencilla.
Se supondr´a que las variaciones del subyacente en distintos intervalos de tiempo son
independientes y que estamos en un entorno de tipos y volatilidad constantes.
Adem´as, para los argumentos de replicaci´on, supondremos que tenemos liquidez
absoluta, que no hay costes de transacci´on y que el subyacente no reparte dividendos
(aunque luego los incorporaremos).
Los par´ametros del modelo se calibrar´an a unos datos de mercado, R, el tipo continuo
anual, y σ, la volatilidad anual (desviaci´on t´ıpica de los rendimientos) del subyacente.
M´as adelante (p´agina 74) mostraremos c´omo construir un ´arbol de evoluci´on consistente
con una estructura temporal de tipos y volatilidades.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
4

## Página 5

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
El modelo presenta algunas ventajas:
se implementa de manera sencilla en un ´arbol binario;
la condici´on de no arbitraje en el modelo se traduce en una condici´on sencilla (local,
en cada nodo del ´arbol);
permite valorar opciones cancelables (americanas);
En cierto sentido, es una versi´on discreta del modelo de Black–Scholes.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
5

## Página 6

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
El modelo binomial
Tiempos
Fijamos de partida una unidad de tiempo Δt. Con N saltos de Δt tenemos 1 a˜no:
NΔt = 1 a˜no.
Llamaremos jΔt, para j = 0, 1, . . . , a los sucesivos instantes de tiempo.
Activos b´asicos
En nuestro mercado solo habr´a dos activos b´asicos:
un activo con riesgo, el subyacente. Llamaremos Sj a su cotizaci´on en tiempo jΔt.
el activo sin riesgo, la cuenta bancaria. Llamaremos βj a su valor en tiempo jΔt.
El objetivo ser´a, luego, valorar derivados sobre la cotizaci´on del subyacente.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
6

## Página 7

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Numerario
La cuenta bancaria ser´a nuestro numerario.
Datos de mercado
Como datos de mercado tendremos
la cotizaci´on hoy del subyacente, S0;
el tipo de inter´es (continuo) anual R;
la volatilidad anual σ del activo subyacente.
Par´ametros del modelo
El modelo tiene tres par´ametros:
u y d (por “up” y “down”), que ser´an las magnitudes de los saltos del subyacente.
Digamos que 0 < d ≤u.
p, una probabilidad (que ser´a de valoraci´on).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
7

## Página 8

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Evoluci´on de los activos b´asicos
Postulamos la siguiente evoluci´on de los activos b´asicos:
la cuenta bancaria vale 1 hoy, vale eRΔt en tiempo Δt, e2RΔt en tiempo 2Δt, etc.:
βj = eR(jΔt) .
En tiempo jΔt, la cotizaci´on Sj del activo subyacente puede tomar, en t´erminos del
valor de tiempo anterior, dos ´unicos valores:
Sj =

Sj−1 · u
con probabilidad p;
Sj−1 · d
con probabilidad 1 −p.
Observaci´on
Como veremos, s´olo tendremos dos condiciones y tres par´ametros, de manera que uno de ellos queda nuestra disposici´on.
En la especiﬁcaci´on de Jarrow–Rudd, que ser´a la que implementemos aqu´ı, se escoge p = 1/2. En los ´arboles de
Cox–Ross–Rubinstein escoger´ıamos d = 1/u. Pero en principio se podr´ıa ﬁjar uno cualquiera de los par´ametros como
quisi´eramos.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
8

## Página 9

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Implementaci´on en ´arboles binarios
Es c´omodo representar los posibles valores del subyacente en un ´arbol binario como el
que sigue:
S0
p
uS0
p
dS0
p
u2S0
p
udS0
p
d2S0
p
u3S0
p
u2dS0
p
ud2S0
p
d3S0
p
u4S0
u3dS0
u2d2S0
ud3S0
d4S0
evoluci´on del activo
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
9

## Página 10

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Observaciones:
→N´otese que el ´arbol se recombina:
S
Su
Sd
Sud
por ejemplo, “bajando” desde
Su o “subiendo” desde Sd se llega al mismo valor, Sud. Esto es muy
relevante desde el punto de vista num´erico, pues hace que el n´umero
de nodos del ´arbol crezca linealmente (y no exponencialmente, como
ocurrir´ıa si el ´arbol no se recombinara; por ejemplo, si u y d fueran
cambiando en el tiempo).
→La evoluci´on de la cuenta bancaria se puede representar, simplemente, con una lista.
→En principio, podemos extender el ´arbol tanto como deseemos. En la pr´actica lo
haremos hasta el vencimiento T = MΔt de la opci´on que pretendamos valorar.
→En Excel representaremos los
´arboles en forma triangular: “subir”
en el ´arbol ser´a quedarse en la mis-
ma ﬁla, “bajar” ser´a descender una
ﬁla.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
10

## Página 11

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Descripci´on matem´atica
La descripci´on matem´atica de la estructura anterior es como sigue:
Tenemos unos instantes de tiempo 0, Δt, 2Δt, . . . . Usaremos el sub´ındice j para
referirnos al tiempo jΔt.
El espacio de escenarios Ω = {ω1, ω2, . . . } est´a formado por listas ω de sucesivas
“bajadas” y “subidas” (“sendas” en el ´arbol):
ω = (ε1, ε2, ε3, ε4, . . . ),
donde los εj son ±1.
Si paramos el ´arbol en tiempo MΔt, tenemos 2M escenarios:
ω1 = (+1, +1, . . . , +1)
ω2 = (−1, +1, . . . , +1)
...
ω2M−1 = (−1, −1, . . . , +1).
ω2M = (−1, −1, . . . , −1).
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
11

## Página 12

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Tenemos una probabilidad P deﬁnida sobre cada uno de estos escenarios ω, que
viene dada por la asignaci´on de probabilidad p a “subir” y probabilidad 1 −p a
“bajar” (m´as la independencia).
As´ı, si ω = (ε1, ε2, ε3, ε4, . . . ),
P(ω) = p #{j: εj = +1} · (1 −p) #{j: εj = −1}
Esto es, p elevado al n´umero de “subidas” por (1 −p) elevado al de “bajadas”.
Codiﬁcamos las sucesivas subidas y bajadas con unas variables de estado
Y1, Y2, Y3, . . . , independientes e id´enticamente distribuidas. En un escenario ω, la
variable Yj vale 1 o −1 en funci´on de que en ese tiempo jΔt haya una subida o una
bajada. De forma que
Yj =

+1
con probabilidad p;
−1
con probabilidad 1 −p.
La suma 
j Yj es un camino aleatorio (no sim´etrico, si p ̸= 1/2). Estas variables de
estado determinan la evoluci´on de todos los activos.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
12

## Página 13

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
La ﬁltraci´on Fj = σ(Y1, . . . , Yj) recoge la informaci´on desvelada hasta tiempo jΔt.
Los activos b´asicos son la cuenta bancaria, que en tiempo jΔt vale
βj = ejRΔt ,
y el activo subyacente S, que en tiempo 0 vale S0 y que, para tiempos posteriores, es
una variable Sj que toma valores en cada nodo de generaci´on j con la ya mencionada
prescripci´on
Sj =

u · Sj−1
con probabilidad p;
d · Sj−1
con probabilidad 1 −p.
Observaci´on
La variable Sj se puede escribir en funci´on de Sj−1 y la variable Yj de la siguiente manera:
Sj = Sj−1

u
Yj + 1
2

−d
Yj −1
2

.
Esto supone que Sj ∈Fj.
Finalmente, la variable Cj(S) registra el valor del derivado C en un nodo de la
generaci´on j en el que el valor del activo es Sj = S.
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
13

## Página 14

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Distribuci´on de probabilidad a vencimiento del subyacente
Miramos hasta tiempo MΔt.
Hay 2M posibles evoluciones del subyacente, cada una con su propia probabilidad.
Pero en ocasiones (por ejemplo, para valorar opciones europeas) no nos interesar´a la
senda seguida, sino el valor ﬁnal del subyacente, para el que tenemos s´olo M + 1
posibilidades. Podemos codiﬁcar estos M + 1 escenarios de 0 a M, en funci´on del
n´umero de “subidas”.
→la cuenta bancaria toma el valor βM = eRMΔt en todos ellos;
escenario
subyacente
probabilidad
M
S0uM
pM
M −1
S0uM−1d
 M
M−1

pM−1(1 −p)1
...
...
...
k
S0ukdM−k
M
k

pk(1−p)M−k
...
...
...
0
S0dM
(1−p)M
→mientras que el subyacente SM puede tomar los M + 1 valores siguientes:
S0 uk dM−k;
k = 0, 1, . . . , M,
con probabilidades
P(SM =S0ukdM−k) = P(bin(M, p)=k)
=
M
k

pk(1 −p)M−k .
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
14

## Página 15

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Simulaci´on en el ´arbol
Como veremos, para ciertos an´alisis y valoraciones resultar´a conveniente simular el
proceso de sucesivos precios del activo directamente.
Para ello, obtendremos muestras independientes de las Yj y, a partir de ellas, muestras
de la evoluci´on de Sj, de las que, ﬁnalmente, obtendremos muestras de los ﬂujos del
instrumento derivado de inter´es. A esto lo denominaremos simular en el ´arbol.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
15

## Página 16

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Probabilidad de valoraci´on
Queremos que nuestro modelo de evoluci´on sea certiﬁcado.
Numerario
La cuenta bancaria βj = ejRΔt ser´a nuestro numerario.
Probabilidad de valoraci´on
Queremos que la probabilidad P sea de valoraci´on (para ese numerario). Es decir, que
los procesos de precios de los dos activos b´asicos, la cuenta bancaria y el subyacente,
escritos en unidades del numerario (es decir, descontados), sean martingala. La evoluci´on
de la CB descontada es obviamente una martingala. Para el subyacente, exigimos que
EP
 Sj
ejRΔt
Fj−1
	
=
Sj−1
e(j−1)RΔt
para cada j = 1, 2, . . .
Una expresi´on que parece aparatosa, pero que se traduce, simplemente, en la siguiente
condici´on, que garantiza que P sea de valoraci´on:
(condici´on de martingala)
up + d(1 −p) = eRΔt
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
16

## Página 17

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Observaci´on
detalle:
EP

Sj
ejRΔt
Fj−1

=
1
ejRΔt EP

Sj−1
u
2 (Yj +1) −d
2 (Yj −1)
Fj−1

= Sj−1
ejRΔt EP(
u
2 (Yj +1) −d
2 (Yj −1)
Fj−1) = Sj−1
ejRΔt
u
2 EP(Yj +1) −d
2 EP(Yj −1)

= Sj−1
ejRΔt
	up + d(1 −p)
(utilizando que EP(Yj)=2p−1).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
17

## Página 18

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Observaci´on
La probabilidad p es “riesgo-neutro”, aquella para la
que la capitalizaci´on promediada del activo subyacente es
justamente la del activo sin riesgo; la probabilidad subjetiva
que un inversor indiferente al riesgo le adjudicar´ıa a la
evoluci´on de B.
1
u
d
1
eRΔt
eRΔt
revalorizaci´on de 1
euro en subyacente
revalorizaci´on de 1 euro
en cuenta bancaria
Por otro lado, es f´acil argumentar, ﬁnancieramente, la ecuaci´on anterior,
que simplemente nos dice que la rentabilidad del activo sin riesgo
debe estar entre las dos posibles rentabilidades del activo con riesgo:
d < eRΔt < u.
1/u
u
w
eRΔt
  



1 −p
p
Construye la estrategia de arbitraje si, por ejemplo,
la rentabilidad del activo sin riesgo estuviera por debajo de d.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
18

## Página 19

MFC 2021-2022
Valoraci´on. Modelos discretos. ´Arboles
Valoraci´on de activos (replicables)
Si ahora C es un activo replicable (con activo y dinero), entonces su proceso de precios
en t´erminos del numerario (es decir, descontado) ser´a tambi´en martingala:
EP
 Cj
ejRΔt
Fj−1
	
=
Cj−1
e(j−1)RΔt
Y, en particular,
EP
 Cj
ejRΔt
F0
	
= C0
1 ,
esto es,
EP
 Cj
ejRΔt
	
= C0.
O, como escribiremos habitualmente,
C0 = e−jRΔt EP(Cj)
Esto es, el precio hoy es el promedio (descontado) de los ﬂujos futuros.
Usaremos estas dos f´ormulas constantemente en las siguientes valoraciones.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
19

## Página 20

Valoraci´on. Modelos discretos. ´Arboles
Calibraci´on del modelo
Tenemos tres datos de mercado: el tipo R, la cotizaci´on inicial S0 y la volatilidad anual
del activo σ.
• Ya hemos calibrado al dato S0 exigiendo que la evoluci´on arranque en ese valor.
• Ahora vamos a exigir que la evoluci´on del subyacente acumule exactamente una
volatilidad anual σ. Es decir, que la desviaci´on t´ıpica de los rendimientos del activo en
un a˜no valga σ:
σ2 = V

ln SN
S0
	
.
La rentabilidad (continua) en un a˜no se expresa directamente en t´erminos de las
rentabilidades en los periodos Δt sucesivos:
ln SN
S0
= ln
S1
S0
S2
S1
· · · SN−1
SN−2
SN
SN−1
	
=
N

j=1
ln Sj
Sj−1
.
Pero las rentabilidades parciales ln(Sj/Sj−1) son variables independientes (e id´entica-
mente distribuidas). As´ı que la varianza de la suma es N veces una de las varianzas.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
20

## Página 21

Valoraci´on. Modelos discretos. ´Arboles
Estos rendimientos parciales son
ln
 Sj
Sj−1
	
=
 ln u
con probabilidad p
ln d
con probabilidad 1 −p
y un peque˜no c´alculo nos dice que esas varianzas individuales son
V

ln
 Sj
Sj−1
	
= p(1 −p)(ln(u) −ln(d))2
as´ı que
σ2 = N p(1 −p)(ln(u) −ln(d))2.
Observaci´on
Detalle:
E

ln
 Sj
Sj−1

= p ln(u) + (1 −p) ln(d);
E

ln2  Sj
Sj−1

= p ln2(u) + (1 −p) ln2(d)
V

ln
 Sj
Sj−1

= p ln2(u) + (1 −p) ln2(d) −(p ln(u) + (1 −p))2 c´alculos
=
p(1 −p)(ln(u) −ln(d))2.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
21

## Página 22

Valoraci´on. Modelos discretos. ´Arboles
Y como NΔt = 1, obtenemos la segunda ecuaci´on:
(ajuste al dato de volatilidad)
σ
√
Δt =

p(1 −p)

ln(u) −ln(d)

c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
22

## Página 23

Valoraci´on. Modelos discretos. ´Arboles
En resumen, dados los datos de mercado R, S0 y σ, podemos construir un modelo de
evoluci´on (de paso Δt)
libre de arbitraje (certiﬁcado);
de forma que la volatilidad anual sea exactamente σ
sin m´as que exigir que el activo arranque en el valor S0 y que los par´ametros u, d y p
veriﬁquen el par de ecuaciones:
⎧
⎪
⎨
⎪
⎩
eRΔt = up + d(1 −p)
σ
√
Δt =

p(1 −p) (ln u −ln d)
Obs´ervese que se trata de un sistema no lineal de dos ecuaciones. Y que hay tres
par´ametros en el modelo (u, d y p).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
23

## Página 24

Valoraci´on. Modelos discretos. ´Arboles
Especiﬁcaci´on de Jarrow–Rudd
Para empezar ﬁjamos
p = 50 %
Las dos ecuaciones son ahora
⎧
⎪
⎪
⎨
⎪
⎪
⎩
eRΔt
=
u + d
2
(condici´on de martingala)
σ
√
Δt =
ln u −ln d
2
(ajuste al dato de volatilidad)
La soluci´on expl´ıcita de este par de ecuaciones viene dada por:
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎩
u = eRΔt eσ
√
Δt

2
eσ
√
Δt + e−σ
√
Δt

d = eRΔt e−σ
√
Δt

2
eσ
√
Δt + e−σ
√
Δt

c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
24

## Página 25

Valoraci´on. Modelos discretos. ´Arboles
Observaci´on
• Basta exponenciar la segunda ecuaci´on y resolver el sistema de ecuaciones resultante.
• Recu´erdese que
cosh(σ
√
Δt) = eσ
√
Δt + e−σ
√
Δt
2
.
Observaci´on
Una soluci´on (aproximada, pero a veces conveniente) viene dada por
u = e(R−σ2/2)Δteσ
√
Δt
d = e(R−σ2/2)Δte−σ
√
Δt
Con esta aproximaci´on, el ajuste al dato de la volatilidad es, de nuevo, exacto. Pero ahora la condici´on de martingala
s´olo se cumple aproximadamente:
u + d
2
= eRΔte−(σ2/2)Δt
 eσ
√
Δt + e−σ
√
Δt
2




≈e(σ2/2)Δt
≈eRΔt
(para Δt peque˜no).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
25

## Página 26

Valoraci´on. Modelos discretos. ´Arboles
ejemplo base
Datos de mercado
⎧
⎨
⎩
R
=
1 %
σ
=
30 %
S0
=
80
Datos de modelo
Δt = 1
12
(esto es, N = 12).
Vencimiento
T = 6 meses.
Los valores de los par´ametros (que dependen del N especiﬁcado) y la evoluci´on del
activo hasta tiempo T = 6/12 resultan ser:
p = 50 %
u = 1.0872924
d = 0.9143750
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
26

## Página 27

Valoraci´on. Modelos discretos. ´Arboles
Separando deriva de ruido
La construcci´on anterior es r´apida y directa. Pero, como preparaci´on para versiones m´as
generales del ´arbol (con tipos/volatilidades no constantes), vamos a reinterpretar la
construcci´on del ´arbol como un proceso en tres etapas:
una primera etapa, en la que con un ´arbol aditivo se recoge la volatilidad, y toda la
incertidumbre.
0
σ
√
Δt
−σ
√
Δt
2σ
√
Δt
0
−2σ
√
Δt
3σ
√
Δt
σ
√
Δt
−σ
√
Δt
−3σ
√
Δt
(o bien el ´arbol aditivo donde se suma 1 en las transiciones hacia arriba, y −1 hacia
abajo). Todas las probabilidades de transici´on son 50 %.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
27

## Página 28

Valoraci´on. Modelos discretos. ´Arboles
Aparte, calculamos la parte determinista que, para los nodos del paso j, se acumula
hasta:
deriva por tipos
−→
ejRΔt
ajuste de deriva por volatilidades
−→

2
eσ
√
Δt + e−σ
√
Δt
j
Finalmente, se exponencian los valores en los nodos de los ´arboles y se multiplican
por el valor inicial del subyacente y por los valores de las derivas acumuladas:
S0 ekσ
√
Δt ejRΔt

2
eσ
√
Δt + e−σ
√
Δt
j
(j depende del paso, k del nodo).
ejemplo base
Construir el ´arbol JR con este procedimiento.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
28

## Página 29

Valoraci´on. Modelos discretos. ´Arboles
Otras especiﬁcaciones
La ventaja de los ´arboles de Jarrow–Rudd es, justamente, la elecci´on de p = 1/2. Esto
los hace especialmente ﬂexibles. En particular, se pueden adaptar bastante bien al caso
en el que los tipos y las volatilidades tengan una cierta estructura temporal (v´ease la
p´agina 74 y siguientes).
Pero como hay tres par´ametros y solo dos condiciones, tenemos entera libertad para
elegir uno de ellos. Podr´ıamos poner, por ejemplo, p = 80 %, o quiz´as u = 5, o
quiz´as. . .
Cuando Δt →0, todos estos ´arboles convergen al mismo proceso (el proceso lognormal
de Black–Scholes).
Algunas de las especiﬁcaciones son cl´asicas, como por ejemplo:
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
29

## Página 30

Valoraci´on. Modelos discretos. ´Arboles
´Arboles de Cox–Ross–Rubinstein
Para empezar ﬁjamos
d = 1
u
Las dos ecuaciones son ahora
(condici´on de martingala)
eRΔt
=
pu + (1 −p)1
u
(ajuste al dato de volatilidad)
σ
√
Δt
=
2

p(1 −p) ln u
El sistema se puede resolver num´ericamente. Pero, si Δt es peque˜no, podemos resolver
aproximadamente1 la segunda ecuaci´on (de volatilidad) y luego expl´ıcitamente la primera:
u ∼eσ
√
Δt ←−aproximaci´on
p = eRΔt −1/u
(u −1/u)
1Si p ≈1/2, la segunda ecuaci´on es σ
√
Δt ≈ln(u). Con esta aproximaci´on, el ajuste a la volatilidad no ser´a perfecto.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
30

## Página 31

Valoraci´on. Modelos discretos. ´Arboles
ejemplo base
Datos de mercado
⎧
⎨
⎩
R
=
1 %
σ
=
30 %
S0
=
80
Datos de modelo
Δt = 1
12
(esto es, N = 12).
Vencimiento
T = 6 meses.
Los valores de los par´ametros (que dependen del N especiﬁcado) y la evoluci´on del
activo hasta tiempo T = 6/12 resultan ser:
p = 48.3170 %
u = 1.0904632
d = 0.9170415
Como ud = 1, el ´arbol est´a centrado en el valor inicial del subyacente.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
31

## Página 32

Valoraci´on. Modelos discretos. ´Arboles
2. Valoraci´on de derivados
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
32

## Página 33

Valoraci´on. Modelos discretos. ´Arboles
Vamos a valorar, en un modelo binomial, derivados de cuatro tipos diferentes:
Opciones europeas, cuyo pago s´olo depende de la cotizaci´on del subyacente a
vencimiento. Las podremos valorar con f´ormula (sumaproducto de valores por proba-
bilidades), o con un ´arbol de evoluci´on del valor del derivado (que se ir´a construyendo
de atr´as hacia adelante).
Opciones path-dependent, cuyo pago depende, en principio, de toda la senda de
cotizaciones hasta vencimiento. Las valoraremos por simulaci´on (en el ´arbol).
Opciones con barrera. Con el ´arbol de evoluci´on del valor del derivado.
Opciones americanas, que incluyen la opci´on de ejercicio anticipado. Tambi´en con el
´arbol de evoluci´on del valor del derivado.
Para su valoraci´on emplearemos repetidamente las condiciones de martingala,
EP
 Cj
ejRΔt
Fj−1
	
=
Cj−1
e(j−1)RΔt
y, en particular,
C0 = e−jRΔt EP(Cj)
Adem´as, daremos el procedimiento para calcular las estrategias de replicaci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
33

## Página 34

Valoraci´on. Modelos discretos. ´Arboles
Valoraci´on de opciones europeas
Valorar un derivado con un modelo binomial consiste en calcular un valor medio,
esperanza, de los ﬂujos potenciales de ese instrumento. El c´alculo de ese valor medio se
puede llevar a cabo de distintas maneras.
Ya tenemos construido el ´arbol de evoluci´on del activo, como por ejemplo el de la
p´agina 26.
Digamos que C es una opci´on europea con vencimiento T = MΔt.
El valor CM, el pago de la opci´on, depende, mediante una cierta f´ormula CM = f(SM)
del valor de SM.
Si, por ejemplo, es una call con strike K, entonces
CM = (SM −K)+ .
Disponemos, para la valoraci´on de este tipo de opciones, de tres metodolog´ıas.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
34

## Página 35

Valoraci´on. Modelos discretos. ´Arboles
M´etodo 1. Valoraci´on con f´ormula
Hay M + 1 posibles pagos de la opci´on, tantos como posibles valores del subyacente a
vencimiento (v´ease la p´agina 14). Aplicamos directamente la f´ormula
C0 = e−MRΔt EP(CM) ,
pues el valor medio de la derecha se puede calcular muy f´acilmente.
N´otese primero que se trata de una suma (ponderada) con M + 1 t´erminos. En cada
escenario,
los valores que se promedian son los n´umeros
f

S0ukdM−k
;
y se promedian con las probabilidades
M
k

pk(1 −p)M−k .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
35

## Página 36

Valoraci´on. Modelos discretos. ´Arboles
En el caso de la call con strike K, los ﬂujos son

S0ukdM−k −K
+
y por tanto el valor hoy se obtiene con la siguiente f´ormula:
C0 =

e−MRΔt



descuento
·
M

k=0

S0ukdM−k −K
+



ﬂujo
M
k

pk(1 −p)M−k



probabilidad
ejemplo base
C´alculo del valor hoy de la call de strike K = 84.
ejemplo base
C´alculo del valor hoy de una opci´on europea con un payoﬀarbitrario.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
36

## Página 37

Valoraci´on. Modelos discretos. ´Arboles
Observaci´on
Pasando al l´ımite N →∞, o lo que es lo mismo, haciendo que Δt tienda a cero, obtenemos la f´ormula de
Black–Scholes:
Callahora = S0 · Φ(d+) −Ke−RT Φ(d−)
donde
d± = ln (S0

K) + (R ± (σ2/2))T
σ
√
T
=
ln

S0
Ke−R·T

σ
√
T
± 1
2σ
√
T
y donde Φ es la funci´on de distribuci´on de la normal est´andar.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
37

## Página 38

Valoraci´on. Modelos discretos. ´Arboles
M´etodo 2. Valoraci´on en el ´arbol
Se trata de interpretar la condici´on
EP
 Cj
ejRΔt
Fj−1
	
=
Cj−1
e(j−1)RΔt ,
que reescribimos
Cj−1 = e−RΔt EP

Cj
Fj−1

como un procedimiento de c´alculo recursivo (hacia atr´as)
en el ´arbol.
Cf
Ca
Cb
MΔt
(M −1)Δt
Nos ﬁjamos, por ejemplo, en los dos nodos
superiores en tiempo MΔt (vencimiento). Los valores Ca y
Cb son conocidos. El valor Cf se obtiene aplicando la f´ormula
de arriba, que aqu´ı simplemente nos dice que
Cf = e−RΔt 
pCa + (1 −p)Cb

.
Se procede igual con los dem´as nodos de tiempo (M −1)Δt, hasta tenerlos todos.
Luego se repite el proceso para los nodos de tiempo (M −2)Δt, etc., hasta llegar a C0.
ejemplo base
´Arbol de valoraci´on de la call europea de strike K = 84.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
38

## Página 39

Valoraci´on. Modelos discretos. ´Arboles
M´etodo 3. Simulaci´on
Una manera alternativa de utilizar la f´ormula
C0 = e−MRΔt EP(CM)
pasa por interpretar la esperanza de la derecha como un promedio sobre todos los
posibles escenarios (sendas en el ´arbol). Ese promedio involucra 2M t´erminos, uno por
senda, cada uno con una cierta probabilidad (o la misma, en el caso p = 1/2).
Caben, pues, dos alternativas:
Exhibir todos los escenarios/sendas, anotar el pago de la opci´on en cada una de ellas,
y promediar esos valores con las respectivas probabilidades (y descontar al ﬁnal);
o bien, si el universo de escenarios es demasiado grande, muestrearlo, simulando un
n´umero suﬁciente de escenarios.
ejemplo base
Simulador en Excel para valoraci´on de europeas.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
39

## Página 40

Valoraci´on. Modelos discretos. ´Arboles
Valoraci´on de derivados path-dependent
Tenemos un instrumento C que paga, a vencimiento MΔt, una cierta cantidad
f(S1, S2, . . . , SM)
que depende de (quiz´as) toda la senda de cotizaciones del subyacente.
Su valor hoy ser´a
C0 = e−MRΔt EP(CM) = e−MRΔt EP(f(S1, S2, . . . , SM)) .
¿Valoraci´on con f´ormula? La anterior es una f´ormula para el valor de la opci´on; pero
se trata de una suma con 2M t´erminos.
¿Valoraci´on en el ´arbol? En general, no es posible. Digamos que queremos valorar una
call asi´atica en la que el ﬂujo depende de la media aritm´etica A de las cotizaciones.
Consideremos un ´arbol binomial con s´olo dos per´ıodos.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
40

## Página 41

Valoraci´on. Modelos discretos. ´Arboles
En una opci´on usual, calculamos el ﬂujo a partir de los nodos del ´ultimo nivel y
procedemos hacia atr´as en el ´arbol. Pero ahora, aunque el activo en dos per´ıodos
alcanza tres valores, la media A toma cuatro distintos, pues “distingue” entre:
S
u2S
udS
d2S
en el camino S →uS →udS, A vale S
1 + u + ud
3

en el camino S →dS →udS, A vale S
1 + d + ud
3u

.
¿Valoraci´on por simulaci´on? Es el m´etodo m´as razonable: muestreamos el espacio
de los 2M escenarios, sorteando sendas de cotizaciones del subyacente en el ´arbol,
anotamos en cada muestra el payoﬀde la opci´on, y luego promediamos con media
aritm´etica (adem´as de descontar).
ejemplo base
• Valorar una opci´on asi´atica de tipo call de media aritm´etica. El strike es K = 92. El vencimiento
es 3 meses. La media aritm´etica lo es de las tres cotizaciones al ﬁnal de los meses 1, 2 y 3.
Determinar los 8 posibles escenarios y los payoﬀs de la opci´on en cada uno de ellos.
• Valoraci´on de opci´on lookback (monitorizaci´on semanal) a 1 a˜no por simulaci´on en el ´arbol.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
41

## Página 42

Valoraci´on. Modelos discretos. ´Arboles
Valoraci´on de opciones con barrera
Veremos ahora c´omo valorar opciones con barrera usando ´arboles. Las opciones con
barrera m´as simples tiene f´ormulas cerradas, pero s´olo las m´as simples. En general,
cuando la estructura de la barrera (o barreras) es ligeramente compleja, es necesario
usar ´arboles o simulaci´on Montecarlo, con cierto cuidado en cualquier caso.
Consideremos el activo que ya hemos usado anteriormente y que tiene el ´arbol de
evoluci´on siguiente:
Y supongamos que queremos valorar una call con barrera con
strike 84;
barrera knock-out en 100.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
42

## Página 43

Valoraci´on. Modelos discretos. ´Arboles
Podemos incorporar estos datos al ´arbol. Los pagos a vencimiento o extinci´on de la
opci´on son los siguientes:
Y ahora procedemos hacia atr´as en el ´arbol. Rellenamos los valores del nivel anterior
al vencimiento (que la barrera no haya determinado ya) y luego el nivel anterior. Y as´ı
sucesivamente. El resultado es:
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
43

## Página 44

Valoraci´on. Modelos discretos. ´Arboles
Observaci´on
Este procedimiento puede ser muy sensible a la ubicaci´on de, por ejemplo, la barrera.
Hemos obtenido la valoraci´on: Call(K = 84, B = 100) = 1.3266.
Y se obtiene la misma valoraci´on para cualquier barrera B que est´e situada entre, por ejemplo, 100 y 102.23 (pese a
que, por supuesto, cuanto m´as alta est´e esa barrera, m´as cara deber´ıa ser la prima).
O tambi´en: si la barrera B se mueve de 102.23 a 102.24, la valoraci´on pasa del 1.3266 de antes a 1.7688, un aumento
de casi el 33 %.
Para evitar esto, podr´ıamos, por ejemplo, dada una barrera B, tomar un Δt peque˜no y hacer que la barrera sea uno de
los niveles del subyacente.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
44

## Página 45

Valoraci´on. Modelos discretos. ´Arboles
Valoraci´on de opciones americanas
Decisi´on y ejercicio anticipado
Ejemplo. Sabemos que se van a recibir 10 ofertas para comprar un bien que poseemos.
Las ofertas (¡qu´e cosas!) van a ser aleatorias, obtenidas de una distribuci´on uniforme
entre 0 y 1. 2
Las ofertas se recibir´an secuencialmente. Cuando se recibe una oferta hay que decidir
si se acepta o se rechaza. En cuanto se acepte una, se termina el proceso. Vamos a
aceptar una.
¿Cu´al es el valor de la venta mediante este proceso de oferta secuencial? O dicho de
otro modo, ¿cu´al es la estrategia ´optima?
Si la primera oferta es de, pongamos por caso, 0.6, ¿debemos aceptarla o esperar? La
opci´on, ante una oferta, es siempre la misma: aceptarla o rechazarla.
2Las unidades en las que se expresa el precio no son relevantes.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
45

## Página 46

Valoraci´on. Modelos discretos. ´Arboles
Obs´ervese que en media cada una de las ofertas tiene valor 0.5, y podr´ıa parecer, a
primera vista, que el valor es de 0.5. Pero, no, sabemos (intuimos) que recibir una serie
de sucesivas ofertas le dar´a m´as valor.
¿C´omo procedemos? Aceptamos una oferta si es suﬁcientemente alta, por encima de un
nivel y la rechazamos si est´a por debajo de ese nivel. Y al principio (con las primeras
ofertas) somos m´as exigentes (es decir, ponemos un umbral de aceptaci´on m´as alto)
que para las ofertas ﬁnales, cuando quedan pocas. La decisi´on de aceptar o no depende
de las ofertas que esperamos recibir m´as adelante.
Comenzamos por el ﬁnal. Denotaremos las ofertas por F10, F9, F8, . . . , F1, donde
numeramos en funci´on de qu´e lugar ocupan desde el ﬁnal. La primera oferta es F10, la
´ultima F1.
Supongamos que s´olo nos queda una oferta (y que hemos rechazado las 9 anteriores).
El umbral de aceptaci´on es 0; tenemos que aceptar la oferta. Y el valor medio de lo
que vamos a obtener es 0.5. Ponemos notaci´on, U1 = 0 (umbral cuando queda una
oferta) y V1 = 0.5 (valor cuando queda una oferta).
Supongamos que quedan dos ofertas. Si rechazamos la oferta inmediata ya sabemos
lo que nos espera, un valor de 0.5. De manera que el umbral U2 de aceptaci´on debe
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
46

## Página 47

Valoraci´on. Modelos discretos. ´Arboles
ser 0.5. ¿Y el valor? Ser´a mayor que 0.5, porque si rechazamos nos quedamos con
algo que hemos valorado en 0.5. El c´alculo preciso es el siguiente:
V2 = E (F2|F2 ≥0.5) · P (F2 ≥0.5) + V1 · P (F2 < 0.5) ,
es decir,
V2 = 0.75 · 0.5 + 0.5 · 0.5 = 0.625 .
En general, el umbral para aceptar una oferta cuando quedan k ofertas ser´a el valor
que se tiene cuando quedan k −1 ofertas:
Uk = Vk−1 .
De manera que
Vk = E (Fk|Fk ≥Vk−1) · P (Fk ≥Vk−1) + Vk−1 · P (Fk < Vk−1) ,
de donde resulta que
Vk = 1 + V 2
k−1
2
.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
47

## Página 48

Valoraci´on. Modelos discretos. ´Arboles
0
0,25
0,5
0,75
1
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
núm ero de ofertas restantes 
valor
0
0,25
0,5
0,75
1
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
núm ero de ofertas restantes 
um bral
Ilustraci´on
Simular en Excel la llegada de ofertas. Comprobar mediante simulaci´on que la regla en cuesti´on es ´optima.
Ejercicio
Supongamos que las ofertas que vamos a recibir vienen dadas por variables normales de media μ y desviaci´on t´ıpica σ
(esto permite ofertas negativas). Construir un esquema en Excel que permita obtener los correspondientes umbrales de
decisi´on Un y valores Vn.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
48

## Página 49

Valoraci´on. Modelos discretos. ´Arboles
Valoraci´on de opciones americanas en el ´arbol
En las opciones americanas, el poseedor de la opci´on tiene el derecho de ejercerla en
cualquier momento entre el comienzo del contrato y el vencimiento.
Valoraci´on de una put americana. Denotaremos por Vn los valores de la opci´on put en
el paso n; o, con m´as precisi´on, por Vn(S), si queremos hacer expl´ıcita la dependencia
en la cotizaci´on S en ese instante.
En el instante n, el poseedor de la put tiene dos opciones:
i) Ejercer en ese instante y obtener (K −Sn)+. ´Este es el valor de ejercicio, que
denotamos por VEn:
VEn(Sn) = (K −Sn)+ .
ii) No ejercer: se tiene entonces un valor de continuaci´on VCn que viene dado por el
valor medio (riesgo-neutro)
VCn(Sn) = e−RΔt [p Vn+1(Sn · u) + (1 −p) Vn+1(Sn · d)] = e−RΔtE (Vn+1|Sn)
El valor Vn ser´a el m´aximo entre VEn y VCn.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
49

## Página 50

Valoraci´on. Modelos discretos. ´Arboles
De manera que
Vn(Sn) = m´ax
⎧
⎨
⎩
VEn(Sn)
= (K −Sn)+
VCn(Sn)
= e−RΔtE (Vn+1|Sn)
Como adem´as en el instante del vencimiento tenemos que
VN = (K −SN)+ ,
podemos implementar un procedimiento recursivo (regresivamente) para calcular el valor
de la put americana en el instante 0.
ejemplo base
Valoraci´on de una put americana de strike K = 84.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
50

## Página 51

Valoraci´on. Modelos discretos. ´Arboles
Call americana vs. call europea
En principio, las opciones americanas han de ser m´as valiosas que las correspondientes
europeas. Pero la call americana (sobre un subyacente que no reparte dividendos) vale
lo mismo que una call europea. Esto es, nunca conviene ejercer antes del vencimiento T.
La paridad call-put nos dice que, en cualquier instante t < T, el precio de la call europea
C(t), el precio de la put P(t) (ambas con strike K) y el tipo R est´an relacionados por:
C(t) = P(t) + S(t) −Ke−R (T −t)
=⇒
C(t) ≥S(t) −K e−R (T −t) > S(t) −K .
Es decir, la call europea es siempre m´as valiosa que el ejercicio anticipado.
Observaci´on
• Aqu´ı suponemos tipos positivos.
•
La put americana es siempre m´as valiosa que la europea. El argumento de antes dar´ıa ahora P (t) ≥
K e−R(T −t) −S(t) , de donde no se puede deducir que P (t) sea mayor que K −S(t).
• Si hay dividendos, entonces las opciones americanas (call o put) son m´as valiosas que las europeas.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
51

## Página 52

Valoraci´on. Modelos discretos. ´Arboles
´Arbol de precios de Arrow-Debreu
El ´arbol de precios de Arrow-Debreu es muy ´util en la implementaci´on num´erica de
esquemas de valoraci´on.
Los precios de Arrow-Debreu est´an asociados a los nodos: en cada uno de ellos,
calculamos el precio hoy del instrumento que vence en el tiempo de ese nivel de nodos
y que paga 1 en ese nodo y 0 en todos los dem´as.
Los precios de Arrow-Debreu de un paso de tiempo han de sumar el factor de descuento
desde ese tiempo a tiempo 0.
El ´arbol se construye recursivamente, pero hacia adelante. En un nodo que no sea borde,
el precio Arrow-Debreu C se obtiene de los precios de Arrow-Debreu que ya se han
calculado en los nodos de los que proviene con el esquema:
1 −p
p
A
j
B
* C
−→
C = [A · (1 −p) + B · p] · e−RΔt
En un nodo que es borde, s´olo una rama aporta al valor C.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
52

## Página 53

Valoraci´on. Modelos discretos. ´Arboles
Una vez calculado el ´arbol de precios de Arrow-Debreu, basta con determinar los ﬂujos
del instrumento en cada nodo (en el que haya ﬂujo) y multiplicar ese ﬂujo por el precio
Arrow-Debreu correspondiente.
ejemplo base
Valoraci´on de una cartera de tres opciones europeas:
una call de strike 86 y vencimiento 6 meses;
una call de strike 75 y vencimiento 5 meses;
una call de strike 68 y vencimiento 4 meses;
utilizando el ´arbol de precios de Arrow-Debreu.
Ejercicio
Valorar el contrato que paga un cup´on del 0.3 % siempre que el subyacente est´e en la franja de valores 75-95.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
53

## Página 54

Valoraci´on. Modelos discretos. ´Arboles
Replicaci´on/cobertura
En las p´aginas anteriores hemos conseguido valorar una gran cantidad de derivados
utilizando la probabilidad de valoraci´on bajo un numerario.
Pero el argumento ﬁnanciero en el que se sostiene esta metodolog´ıa de valoraci´on, la
ausencia de oportunidades de arbitraje, se basa en la existencia de carteras replicantes.
Para dar precio a los derivados, no nos ha hecho falta calcular esa cartera replicante.
Pero imaginemos que nos interesa la estrategia de cobertura de la opci´on: hemos
calculado su precio hoy C0, y ahora se trata de dise˜nar la cartera, de coste hoy C0,
que, gestionada autoﬁnanciadamente, nos permita hacer frente a los pagos de la opci´on
“pase lo que pase”.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
54

## Página 55

Valoraci´on. Modelos discretos. ´Arboles
Replicaci´on/cobertura en un solo periodo
Partimos de la situaci´on general:
1
eRΔt
eRΔt
S0
uS0
dS0
C0
Cu
Cd
cuenta bancaria
subyacente
derivado
Los valores Cu y Cd son conocidos. Vamos a formar una cartera con α unidades en la
cuenta bancaria y β en subyacente. Los valores de α y β son la soluci´on del sistema de
ecuaciones
 Cu =
αeRΔt + βu S0
Cd =
αeRΔt + βd S0
Una vez obtenidos los valores de α y β, valoramos el derivado:
C0 = α + β S0 .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
55

## Página 56

Valoraci´on. Modelos discretos. ´Arboles
Cobertura
Resolviendo el sistema de ecuaciones anterior, deducimos que el activo C equivale a la
cartera que consta de β unidades de subyacente, donde
β = Cu −Cd
Su −Sd =
incremento de valor del derivado
incremento de valor del subyacente
Esta cantidad β se conoce, en la jerga habitual, como delta.
Se trata de cobertura est´atica: un solo per´ıodo de tiempo.
Observaci´on
Tambi´en se puede calcular el n´umero de unidades de dinero de la cartera replicante. En concreto, el resultado es
α = e−RΔt d Cu−u Cd
d−u
. Pero, en la pr´actica, se conoce C0 y se obtiene α como diferencia.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
56

## Página 57

Valoraci´on. Modelos discretos. ´Arboles
Eliminaci´on del riesgo
Otro punto de vista de la valoraci´on es la eliminaci´on del riesgo.
Comenzamos con el activo (derivado) C y buscamos formar una cartera con el propio
C y β unidades del activo subyacente S de manera que la cartera C −βS no tenga
riesgo, es decir, no tenga incertidumbre. O, lo que es lo mismo, en los dos escenarios
futuros se tenga el mismo valor.
Traducido en ecuaciones:
Cu −βSu = Cd −βSd ,
que nos da directamente que
β = Cu −Cd
Su −Sd
.
Pero, entonces, con ese valor de β, la cartera C −βS ha de ser (por ausencia de
arbitraje), el activo sin riesgo, es decir, α unidades del activo sin riesgo:
Cu −βSu = Cd −βSd = αeRΔt
=⇒
α = e−RΔt d Cu −u Cd
d −u
.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
57

## Página 58

Valoraci´on. Modelos discretos. ´Arboles
Cobertura din´amica
El precio del derivado es la cantidad de que se precisa para formar una cartera de
subyacente y dinero, que de manera autoﬁnanciada y con reajuste en cuanto a la
proporci´on de activo subyacente y dinero, permite en cualquier evoluci´on replicar los
ﬂujos del derivado.
En tiempo 0. El derivado vale C0. Formamos una cartera de cobertura. La cartera
tiene α0 de dinero y β0 unidades de activo. El dinero se presta o se ha tomado
prestado a plazo Δt. As´ı,
C0 = α0 + β0S0 .
La situaci´on inicial es
tiempo
en dinero
n´umero de acciones
valor cartera
0
α0
β0
α0 + β0S0 = C0
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
58

## Página 59

Valoraci´on. Modelos discretos. ´Arboles
En tiempo Δt. Para la cobertura ocurren dos cosas:
Primero. Cambia la cotizaci´on del subyacente. ´Este pasa a ser S1. Y la situaci´on de
la cartera es
tiempo
en dinero
n´umero de acciones
valor cartera
justo antes de Δt
α0
β0
α0eRΔt + β0S1 = C1
La composici´on de la cartera es tal que, sea cual sea la nueva cotizaci´on de S1, la
cartera vale lo que el derivado C1. La composici´on que ahora tiene la cartera no
es la adecuada para el periodo siguiente, pero su valor es exactamente el que se
precisa para la replicaci´on para el paso siguiente.
Segundo. Se recompone la cartera (de manera autoﬁnanciada).
tiempo
en dinero
n´umero de acciones
valor cartera
justo despu´es de Δt
α1
β1
α1eRΔt + β1S1 = C1
Sucesivos periodos Se procede an´alogamente.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
59

## Página 60

Valoraci´on. Modelos discretos. ´Arboles
Ilustraci´on
Obtener los ´arboles de replicaci´on de una opci´on europea. En el primero, en cada nodo aparece la cantidad de dinero, y
en el segundo la cantidad de acciones.
Simular una senda de cotizaciones en el ´arbol y comprobar que la cartera replicante cubre los pagos de la opci´on en
todos los casos.
Ilustraci´on
Ejercicio an´alogo para una opci´on path-dependent y para una americana.
Ejercicio
Supongamos que hemos emitido una opci´on put americana, que estamos cubriendo. Supongamos que sabemos que
el tenedor de la opci´on ejercer´a siempre un periodo de tiempo despu´es del momento de ejercicio ´optimo. Dise˜nar la
estratega de cobertura. Calcular con el ´arbol la ganancia que supone para el emisor.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
60

## Página 61

Valoraci´on. Modelos discretos. ´Arboles
Dividendos y futuros
La inclusi´on de los dividendos en el modelo binomial es algo delicada. Analizaremos dos
casos: cuando interpretamos que recibimos una tasa continua de dividendos, y cuando
tenemos previsto recibir un dividendo ﬁjo en un determinado instante de tiempo.
Tasa continua de dividendos
Es habitual considerar que el activo tiene una rentabilidad continua por dividendos Q
por unidad de tiempo. Se trata de una idealizaci´on que facilita mucho los c´alculos, sobre
todo en los modelos de evoluci´on continua del entorno Black–Scholes.
Si en tiempo t la cotizaci´on es St, entonces, en tiempo t + dt
St
−→
St+dt
  
cambio cotizaci´on
+ St+dtQdt



por dividendo
Si se reinvierte en activo este rendimiento extra por dividendo, el valor St+dt(1 + Qdt)
supone que tenemos (1 + Qdt) unidades de subyacente.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
61

## Página 62

Valoraci´on. Modelos discretos. ´Arboles
A m´as plazo, desde tiempo 0 hasta Mdt,
S0
−→
SMdt
M

j=1
(1 + Qdt) ≈SMdt eQMdt
De manera que es como si en tiempo Mdt tuvi´eramos eQMdt unidades de subyacente.
Replicaci´on. Dividimos la unidad de tiempo (el a˜no) en N intervalos de tiempo de
tama˜no Δt. La tasa continua por dividendos es Q. La situaci´on, en un paso de tiempo, es
S0
S0ueQΔt
S0deQΔt
´arbol de valores
1
eRΔt
¿C0?
Cu
Cd
eRΔt
S0
S0u
S0d
´arbol de cotizaciones
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
62

## Página 63

Valoraci´on. Modelos discretos. ´Arboles
Buscamos α y β para que la cartera de precio α + βS0 replique los pagos de la opci´on:

Cu = αeRΔt + β(S0u eQΔt)
Cd = αeRΔt + β(S0d eQΔt)
un sistema de ecuaciones cuya soluci´on es
β = Cu −Cd
(u −d)
1
S0eQΔt
y
α = e−RΔt dCu −uCd
d −u
.
Obs´ervese c´omo reinvertimos los dividendos (la cartera es autoﬁnanciada).
Valoraci´on con probabilidades. La ecuaci´on de no arbitraje es
p S0 u eQΔt
eRΔt
+ (1 −p) S0 d eQΔt
eRΔt
= S0
que se simpliﬁca para obtener
p u + (1 −p) d = e(R−Q)Δt.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
63

## Página 64

Valoraci´on. Modelos discretos. ´Arboles
Se trata de la f´ormula habitual, en la que hemos cambiado R por R −Q. Aunque,
¡atenci´on!, en las valoraciones seguiremos descontando con R.
En el caso Jarrow–Rudd, las dos ecuaciones que determinar´ıan los valores de u y d
ser´ıan:
e(R−Q)Δt = u + d
2
y
σ
√
Δt = ln u −ln d
2
,
cuya soluci´on es:
u = e(R−Q)Δteσ
√
Δt

2
eσ
√
Δt + e−σ
√
Δt

,
d = e(R−Q)Δte−σ
√
Δt

2
eσ
√
Δt + e−σ
√
Δt

Ejercicio
Aplicar el mismo an´alisis a opciones sobre divisas. Aqu´ı Q queda reemplazado por Re, el tipo de inter´es extranjero.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
64

## Página 65

Valoraci´on. Modelos discretos. ´Arboles
Observaci´on
Esto da, al pasar al caso continuo, que el precio del activo en tiempo T , ST , y bajo riesgo neutro satisface que
ST = S0e[(R−Q)−σ2/2]T +σ
√
T N (0,1)
Sacando un factor e−QT , vemos que, si K, R, y T ﬁjos:
Call con rentabilidad por dividendos Q y precio de activo S0
equivale a
Call con rentabilidad por dividendos 0 y precio de activo e−QT · S0
Alternativamente, como el valor de una call es
Call = e−RT E (m´ax (ST −K, 0))
que podemos reescribir como
Call = e−QT 
e−(R−Q)T · E (m´ax (ST −K, 0))

deducimos que, para S0, K y T ﬁjos:
Call con rentabilidad por dividendos Q y tipo de inter´es R
equivale a
e−QT × Call con rentabilidad por dividendos 0 y tipo de inter´es R −Q
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
65

## Página 66

Valoraci´on. Modelos discretos. ´Arboles
Dividendos ﬁjos
Supongamos que en tiempo T recibiremos un
´unico dividendo conocido D (por acci´on).
0
t
T
S0
St

dividendo D
In-
terpretamos que la cotizaci´on St del activo tiene
dos partes: por un lado, el valor (descontado) del dividendo; y, por otro, la parte con
incertidumbre, que llamaremos S∗
t :

St
= S∗
t + D e−R(T −t)
si t ≤T;
St
= S∗
t
si t > T.
El valor de la inversi´on en el activo en tiempo t viene dado por
S∗
t + D e−R(T −t) ,
que coincide con la cotizaci´on hasta la fecha de pago del dividendo. Queremos valorar
un derivado sobre este subyacente. N´otese que el pago del derivado depende de la
cotizaci´on del activo.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
66

## Página 67

Valoraci´on. Modelos discretos. ´Arboles
Dividendos en el esquema binomial de un paso
Supongamos que el dividendo D se paga en tiempo Δt/3. La cotizaci´on hoy es
S0 = S∗
0 + D e−RΔt/3 .
Proponemos la habitual evoluci´on, pero ´unicamente para la parte con incertidumbre:
S∗
0
S∗
0u
S∗
0d
1
eRΔt
eRΔt
¿C0?
Cu
Cd
La replicaci´on va como sigue. Formamos una cartera con α unidades de dinero y β de
subyacente, cuyo precio hoy es
α + βS0 ,
y buscamos los valores de α y β para los que esta cartera replique los pagos del derivado
en cualquiera de las posibilidades.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
67

## Página 68

Valoraci´on. Modelos discretos. ´Arboles
Obs´ervese que las β acciones, tras tiempo Δt, dan lugar a
o bien βS∗
0u, o bien βS∗
0d;
y la parte sin riesgo βDeRΔt 2/3 (el dividendo recibido en Δt/3, capitalizado).
Buscamos los valores de α y β para los que

Cu
=
αeRΔt + β(S∗
0u + DeRΔt2/3)
Cd
=
αeRΔt + β(S∗
0d + DeRΔt2/3)
El resultado es
β = Cu −Cd
S∗
0(u −d)
α = e−RΔt dCu −uCd
d −u
−D e−RΔt/3 Cu −Cd
S∗
0(u −d)
¿Y el c´alculo con probabilidades?
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
68

## Página 69

Valoraci´on. Modelos discretos. ´Arboles
Buscamos primero p tal que
pu + (1 −p)d = eRΔt .
¡Atenci´on!, esto har´a que el ´arbol de S∗
t sea martingala, pero no as´ı el de las cotizacio-
nes St (aunque s´ı lo ser´a el ´arbol de valores de la inversi´on).
Ahora multiplicamos la primera ecuaci´on por p y la segunda por (1 −p) para obtener
que
pCu + (1 −p)Cd = αeRΔt + βS∗
0eRΔt + βDeRΔt2/3
Esto es,
e−RΔt(pCu + (1 −p)Cd) = α + βS∗
0 + βDe−RΔt/3
= α + β(S∗
0 + De−RΔt/3)
= α + βS0 = inversi´on para la replicaci´on = C0
Conclusi´on: p es la probabilidad que hace que S∗(y no S) sea riesgo neutro, pero a´un
as´ı es la que usamos para valorar los derivados (cuyo pago depende de S).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
69

## Página 70

Valoraci´on. Modelos discretos. ´Arboles
Implementaci´on en el ´arbol binomial
Supongamos que se van a recibir dos
dividendos (conocidos hoy), D1 y D2,
en tiempos T1 y T2. La opci´on que
queremos valorar vence en tiempo T.
Fijamos un Δt para nuestro ´arbol binomial, de manera que MΔt = T.
+
T1
T2
dividendo D1

dividendo D2
0
T

Δt
Los inputs de
mercado son R, el tipo anual, σ, la volatilidad del subyacente y S0, la cotizaci´on hoy
del activo.
Para valorar el derivado necesitamos el ´arbol de la cotizaci´on St, que consta de dos
partes: S∗
t , con la incertidumbre, y PDt, el “proceso de dividendos” (sin incertidumbre):
St = S∗
t + PDt ,
donde
PDt =

D1 e−(T1−t)R
si t ≤T1,
0
si t > T1,
+

D2 e−(T2−t)R
si t ≤T2,
0
si t > T2.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
70

## Página 71

Valoraci´on. Modelos discretos. ´Arboles
Procedimiento:
1. Con los valores de R y σ se determinan los valores de los par´ametros u, d y p.
2. Con el valor S∗
0 y los valores de u y d construimos el ´arbol de valores de S∗
t hasta
tiempo T (esto supone que consideramos que σ es la volatilidad de S∗).
3. Calculamos los valores del proceso de dividendos PDt (n´otese que es un vector ﬁla
en Excel, pues no tiene incertidumbre).
4. Construimos el ´arbol de cotizaciones St a partir del de S∗
t aumentando todos los
valores de los nodos de tiempo jΔt con el correspondiente valor PDjΔt. Este ´arbol
no ser´a martingala (con p), pero nos servir´a para valorar la opci´on.
5. Podemos tambi´en construir el ´arbol del valor de la inversi´on en el activo, cuyos
valores vienen dados por S∗
t + D1 e−(T1−t)R + D2 e−(T2−t)R
6. La valoraci´on del derivado utiliza el ´arbol de cotizaciones St y los promedios se
calculan con p.
Ilustraci´on
C´alculo de la prima de una put americana con y sin dividendos. Comparaci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
71

## Página 72

Valoraci´on. Modelos discretos. ´Arboles
Futuros
Consideremos ahora el caso de una opci´on C cuyo subyacente sea un futuro F.
Planteamos el esquema habitual para el argumento de replicaci´on:
0
F0u −F0
F0d −F0
´arbol de valores
1
eRΔt
¿C0?
Cu
Cd
eRΔt
F0
F0u
F0d
´arbol de cotizaciones
Queremos formar una cartera con α unidades de dinero y β futuros que replique los
pagos de la opci´on. ¡Atenci´on!, el precio hoy de esta cartera es α. Un contrato de futuro
(que hoy cuesta 0) paga, en tiempo Δt, liquidando por diferencias,
o bien F0u −F0 ,
o bien F0d −F0 .
El precio de la cartera de r´eplica es el valor de α que se obtiene al resolver

Cu
=
αeRΔt + β(F0u −F0) .
Cd
=
αeRΔt + β(F0d −F0) .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
72

## Página 73

Valoraci´on. Modelos discretos. ´Arboles
Valoraci´on con probabilidades
La condici´on de no arbitraje es que el promedio de los ﬂujos (descontados) en tiempo Δt
sea el precio hoy (que es 0). Es decir,
0 = p F0u −F0
eRΔt
+ (1 −p) F0d −F0
eRΔt
.
Esto es,
F0 = p F0u + (1 −p) F0d .
Observaci´on
Bajo la probabilidad de valoraci´on, la probabilidad riesgo-neutro, la cotizaci´on del futuro (sin descontar) es martingala.
Los futuros son martingala.
De lo anterior se deduce que la ecuaci´on de no arbitraje ser´ıa, simplemente,
p u + (1 −p) d = 1 .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
73

## Página 74

Valoraci´on. Modelos discretos. ´Arboles
3. ´Arbol consistente con la estructura
temporal de tipos y volatilidades
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
74

## Página 75

Valoraci´on. Modelos discretos. ´Arboles
Pretendemos ahora construir un ´arbol de evoluci´on del subyacente (libre de arbitraje y
que arranque en S0), pero que adem´as sea consistente
con una curva de tipos (spot, por ejemplo) a distintos plazos;
y con unos datos de volatilidad (impl´ıcita, spot) a distintos plazos.
Es decir, cuando en lugar de r y σ constantes, tenemos una estructura temporal en
tipos y volatilidades.
En realidad, que los tipos no sean constantes, como veremos en un momento, se puede
resolver f´acilmente. Sin embargo, la soluci´on m´as simple que se nos ocurrir´ıa para ajustar
la estructura temporal de las volatilidades har´ıa que el ´arbol ya no fuera recombinante.
Tendremos que idear algo mejor.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
75

## Página 76

Valoraci´on. Modelos discretos. ´Arboles
Ajustando a la curva de tipos
Supongamos que tenemos un dato de volatilidad constante σ y los tipos forward
(continuos) Rj para cada uno de los periodos de tiempo j Δt hasta (j + 1) Δt.
En cada tiempo j, con los valores de Rj y σ podemos determinar la magnitud de los
saltos:
⎧
⎪
⎨
⎪
⎩
uj = eRjΔteσ
√
Δt factor(σ)
dj = eRjΔte−σ
√
Δt factor(σ)
donde
factor(σ) =

2
eσ
√
Δt + e−σ
√
Δt

.
Nos preocupar´ıa si el ´arbol no se recombinara.
S0
u0S0
u0u1S0
d0S0
d0d1S0
u0d1S0
d0u1S0
R0
?
R1
?
Es decir,
si, por ejemplo, los valores de u0d1S0 y d0u1S0 no coinci-
dieran. Pero no es el caso, pues tanto u0 como d0 llevan
un factor eR0Δt, y u1 y d1 llevan el correspondiente eR1Δt.
As´ı que la construcci´on del ´arbol ser´ıa inmediata.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
76

## Página 77

Valoraci´on. Modelos discretos. ´Arboles
Ajustando a la curva de volatilidades
Partimos de una asignaci´on de volatilidad para cada vencimiento T, por ejemplo, la
media ponderada de las volatilidades impl´ıcitas para distintos strikes con el mismo
vencimiento T (o, simplemente, la volatilidad ATM para cada vencimiento T).
Digamos que de estos datos somos capaces de extraer las volatilidades (impl´ıcitas)
forward, es decir, para cada periodo. Con el tipo forward y la volatilidad forward de cada
periodo podr´ıamos calcular los saltos uj y dj.
Pero el ´arbol no se recombinar´ıa. Por ejemplo,
u0d1 = e(R0+R1)Δt · factor(σ0) · factor(σ1) e(σ0−σ1)
√
Δt
d0u1 = e(R0+R1)Δt · factor(σ0) · factor(σ1) e(σ1−σ0)
√
Δt
que no coinciden.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
77

## Página 78

Valoraci´on. Modelos discretos. ´Arboles
Pero si el ´arbol no se recombina, entonces el n´umero de nodos crece exponencialmente
con el n´umero de pasos del ´arbol, y el esquema num´erico es intratable.
En los dos esquemas siguientes planteamos las dos situaciones posibles: en la primera,
la volatilidad del segundo periodo es mayor que la del primero, haciendo que el ´arbol se
“abra” m´as de lo necesario. En la segunda, la volatilidad del segundo periodo es menor
de la del primero, y el ´arbol no se abre lo suﬁciente:
0
0
Δt
2Δt
Δt
2Δt
¿Alguna sugerencia?
Para solucionarlo, renunciaremos a una caracter´ıstica del modelo, como es que el paso
de tiempo sea un Δt ﬁjo. Una elecci´on c´omoda, pero no imprescindible.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
78

## Página 79

Valoraci´on. Modelos discretos. ´Arboles
Ajuste del ´arbol a la curva de volatilidades
Construiremos el ´arbol casi como en el caso general (de Jarrow–Rudd), pero para poder
captar la estructura de volatilidad y para que, adem´as, el ´arbol sea recombinante, los
intervalos de tiempo de los pasos del ´arbol no ser´an todos iguales.
Datos
una curva de volatilidades spot a ciertos vencimientos t1, t2, . . . , T. Supongamos, por
comodidad, que el ´ultimo vencimiento coincide con el de la opci´on. Llamemos a estas
volatilidades
σ(t1), σ(t2), . . . , σ(T)
una curva de tipos spot a ciertos vencimientos (por ejemplo, los mismos de antes):
R(t1), R(t2), . . . , R(T)
Las varianzas acumuladas hasta tiempo tj son las cantidades Vj = tjσ2(tj). La varianza
acumulada hasta el plazo ﬁnal es Tσ2(T).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
79

## Página 80

Valoraci´on. Modelos discretos. ´Arboles
Procedemos en etapas:
Etapa 1
Fijamos una unidad de volatilidad A. Para ello, decidimos cu´antos pasos N tendr´a el
´arbol hasta tiempo T. Tomamos A de manera que
0
A
−A
2A
0
−2A
3A
A
−A
−3A
NA2 = Tσ2(T).
Etapa 2
Para ese nivel de referencia A, construimos el ´arbol
aditivo, con todas las probabilidades iguales a 50 %,
pero sin especiﬁcar el intervalo de tiempo que abarca
cada paso.
La varianza acumulada hasta tiempo j es jA2.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
80

## Página 81

Valoraci´on. Modelos discretos. ´Arboles
Etapa 3
Buscamos ahora la serie de tiempos
T1, T2, . . . , TN
tales que la varianza acumulada hasta tiempo Tj sea justamente jA2. As´ı, la varianza
en cada intervalo [Tj−1, Tj] es A2.
(Los tiempos Tj se obtienen interpolando en la tabla que relaciona los tiempos tj con
las varianzas acumuladas tjσ2(tj)).
Los tiempos que marcan los intervalos del ´arbol son los Tj. Los valores del ´arbol son los
usuales, pero los intervalos de tiempo no son iguales.
Obtención de intervalos de tiempo del árbol
0,00
0,04
0,08
0,12
0,16
0,20
0,24
0,25
0,5
0,75
1
1,25
1,5
1,75
2
tiempos
varianzas implícitas acumuladas
Unidad de 
volatilidad=
0,04
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
81

## Página 82

Valoraci´on. Modelos discretos. ´Arboles
Etapa 4
Calculamos las derivas que corresponden a los nodos de tiempo Tj, y que resultan ser:
deriva por tipos −→eTjR(Tj) ,
ajuste de deriva por volatilidades −→

2
eA + e−A
j
(para las primeras, habr´a que interpolar en la curva de tipos).
Observaci´on
El ajuste de la deriva proviene de que la esperanza de la variable que toma los valores eA y e−A (con probabilidad 1/2
cada uno) es, obviamente, (eA + e−A)/2.
Etapa 5
El ´arbol del subyacente se construye combinando estos tres efectos, de la
manera habitual:
S0 ekA eTjR(Tj) 
2
eA + e−A
j
(j depende del paso, k del nodo).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
82

## Página 83

Valoraci´on. Modelos discretos. ´Arboles
Ilustraci´on
Disponemos de la curva cup´on cero y de una curva de volatilidades spot.
Construir el ´arbol de Jarrow–Rudd consistente con esta informaci´on.
Util´ıcese para valorar una opci´on range accrual, que paga, a vencimiento, en funci´on de la proporci´on de d´ıas que
el subyacente haya estado en una cierta franja. N´otese que el ´arbol est´a construido para una cierta lista de fechas.
¿C´omo interpretamos lo que ocurre “entre medias”?
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
83

## Página 84

Valoraci´on. Modelos discretos. ´Arboles
4. Construcci´on de un modelo discreto
de tipos
c  Aﬁ Escuela de Finanzas. Todos los derechos reservados
84

## Página 85

Valoraci´on. Modelos discretos. ´Arboles
Vamos a prescribir una evoluci´on aleatoria en el tiempo de tipos de inter´es. El tiempo
estar´a discretizado y representaremos los posibles estados con un ´arbol binomial.
Queremos que este modelo de evoluci´on est´e libre de oportunidades de arbitraje, para
que permita valorar instrumentos cuyo precio se derive de los tipos (promediando ﬂujos
adecuadamente descontados).
Interesar´a que este esquema de valoraci´on sea capaz de dar correctamente los precios
de referencia del mercado, que en nuestro caso ser´an los bonos cup´on cero de los
sucesivos vencimientos (y, quiz´as, algunos instrumentos con opcionalidad, como caps,
swaptions). Es decir, calibraremos el modelo a los precios de mercado.
Y argumentaremos que, una vez calibrado, el esquema ser´a tambi´en capaz de valorar
“adecuadamente” (¡interpolaci´on!) los instrumentos que no est´en en mercado.
Empezamos con toda generalidad. El paso temporal Δt est´a ﬁjado.
Vamos a construir un ´arbol binomial a la Jarrow–Rudd (todas las probabilidades son 1/2)
para el tipo (continuo, anual) a plazo Δt.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
85

## Página 86

Valoraci´on. Modelos discretos. ´Arboles
Denotamos3 por Rk al tipo (continuo, anual) a plazo Δt que tenemos en tiempo kΔt.
En nuestro esquema binomial, Rk es aleatorio, y toma k + 1 valores, uno en cada nodo.
tiempo 0
tiempo Δt tiempo 2Δt
6
6
6
R0
variable R1 variable R2
1/2
1/2
1/2
1/2
1/2
1/2
1/2
1/2
1/2
1/2
1/2
1/2
R0 toma 1 valor
R1 toma 2 valores
R2 toma 3 valores
...
3Una notaci´on m´as precisa para Rk, pero que aqu´ı no usaremos, ser´ıa R(kΔt, (k + 1)Δt). Elegimos tipos continuos
tambi´en por comodidad notacional, aunque tambi´en podr´ıan ser tipos simples (y, de hecho, ´esa suele ser la elecci´on habitual).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
86

## Página 87

Valoraci´on. Modelos discretos. ´Arboles
Elecci´on de numerario
Supongamos que ya tenemos construido el ´arbol con los valores de los tipos (m´as
adelante propondremos un esquema para parametrizar esos valores).
Las consideraciones probabil´ısticas que haremos a continuaci´on se reﬁeren a trayectorias
en el ´arbol anterior, a las que nos referiremos gen´ericamente como trayectorias ω.
Ahora elegimos el numerario para descontar precios: la cuenta bancaria, cuyo valor en
tiempo k denotamos por β(k).
β(k) es la variable aleatoria que recoge la capitalizaci´on de 1 euro de tiempo 0 (en
dep´osito rodante cada Δt) hasta tiempo kΔt.
Por ejemplo, β(0) = 1, mientras que β(1) = eR0Δt. A partir de tiempo 2Δt es ya una
variable aleatoria.
Pero en general el valor de β(k) no s´olo depende del nodo de tiempo k en el que
estemos (de entre los k + 1 posibles), sino tambi´en del camino ω que nos haya llevado
a ese nodo (es path dependent).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
87

## Página 88

Valoraci´on. Modelos discretos. ´Arboles
Por ejemplo, para tiempo 2 tenemos
trayectoria ω2
trayectoria ω3
R0
R1(nodo up)
R1(nodo down)
R0
β(2) = e(R0+R1(nodo up)) Δt
β(2) = e(R0+R1(nodo down)) Δt
trayectoria ω1
R0
R1(nodo up)
β(2) = e(R0+R1(nodo up)) Δt
trayectoria ω4
R1(nodo down)
R0
β(2) = e(R0+R1(nodo down)) Δt
Obs´ervese la diferencia entre las trayectorias ω2 y ω3, que llegan al mismo nodo central.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
88

## Página 89

Valoraci´on. Modelos discretos. ´Arboles
Metodolog´ıa de valoraci´on
Instrumentos de mercado
Los instrumentos que vamos a considerar como “de mercado” son los bonos cup´on cero
de distintos vencimientos4.
Es importante se˜nalar que todos los vencimientos deben ser m´ultiplos de Δt, el paso
elegido en el ´arbol.
Denotaremos por
P(k, T)
el precio en tiempo kΔt del bono cup´on cero de nominal 1 y vencimiento T (un m´ultiplo
de Δt).
De nuevo es una cantidad aleatoria que depende, adem´as de k y de T, del nodo de
tiempo k en el que estemos y, quiz´as, de la trayectoria ω que nos lleve hasta ´el.
4Aunque luego incluiremos instrumentos con opcionalidad.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
89

## Página 90

Valoraci´on. Modelos discretos. ´Arboles
No arbitraje
Siguiendo nuestra idea general de valoraci´on por no arbitraje, pretendemos que el proceso
que da cuenta, en cada tiempo k, del precio (descontado con la cuenta bancaria) del
bono que vence en tiempo T,
P(k, T)
β(k)

k
sea martingala (bajo la probabilidad considerada).
Esto supone que
(⋆)
E
P(k, T)
β(k)
 Fk−1

= P(k −1, T)
β(k −1)
para cada k = 1, 2 . . . .
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
90

## Página 91

Valoraci´on. Modelos discretos. ´Arboles
Valoraci´on
Si se cumpliera (⋆), entonces, aplic´andola reiteradamente obtendr´ıamos el precio hoy
del bono cup´on cero de vencimiento T:
E
P(k, T)
β(k)

= P(0, T)
β(0)
.
An´alogamente, si X es cualquier instrumento (replicable en t´erminos de estos bonos)
cuyo payoﬀconozcamos, por ejemplo, en tiempo k, entonces podr´ıamos valorarlo de
manera an´aloga:
E
X(k)
β(k)

= X(0)
β(0) .
Y si X no fuera replicable, esta metodolog´ıa a´un nos proporcionar´ıa un precio del
instrumento (por interpolaci´on).
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
91

## Página 92

Valoraci´on. Modelos discretos. ´Arboles
No arbitraje, ya en el ´arbol
Parece que (⋆) es una condici´on muy aparatosa, dado que todas las cantidades
involucradas dependen de las trayectorias seguidas.
Pero obs´ervese en qu´e se traduce en nuestro esquema binomial.
nodo up
nodo down
nodo inicial
trayectoria ω
tiempo k−1
tiempo k
Digamos que estamos en un nodo de tiempo k−1 (nodo
inicial) y consideremos sus dos vecinos de tiempo k
(nodos up y down).
Al nodo inicial hemos llegado siguiendo una cierta
trayectoria, digamos ω, que determina el valor β(k−1)
correspondiente.
En ese nodo inicial, Rk−1 tiene un cierto valor, el
correspondiente del ´arbol de tipos.
La condici´on de martingala se escribe de la siguiente manera:
(⋆⋆)
1
2
P(nodo up, T)
β(nodo up)
+ 1
2
P(nodo down, T)
β(nodo down)
= P(nodo inicial, T)
β(nodo inicial)
.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
92

## Página 93

Valoraci´on. Modelos discretos. ´Arboles
En esta f´ormula, cuando escribimos nodo up (o nodo down, o inicial), estamos conside-
rando no s´olo el nodo en el que estamos (y el tiempo al que corresponde), sino tambi´en
“c´omo” hemos llegado a ellos.
Pero obs´ervese que
β(nodo up) = β(nodo inicial) · eRk−1Δt
β(nodo down) = β(nodo inicial) · eRk−1Δt
De manera que la f´ormula (⋆⋆), la condici´on de martingala, se escribe simplemente
como
(⋆⋆⋆)
e−Rk−1ΔtP(nodo up, T) + P(nodo down, T)
2
	
= P(nodo inicial, T)
Esta sencilla observaci´on es clave, pues nos va a permitir valorar los bonos cup´on cero
de los sucesivos vencimientos sin m´as que utilizar recursivamente la f´ormula (⋆⋆⋆)
anterior.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
93

## Página 94

Valoraci´on. Modelos discretos. ´Arboles
Simplemente hay que observar que sabemos que el bono que vence
en tiempo T vale justamente 1 en todos los nodos de tiempo T.
Digamos, por ejemplo, que el ´arbol de valores de tipos empieza
como mostramos a la derecha.
R0
R(1)
1
R(2)
1
Por ejemplo, el bono que vence en tiempo 1:
1
1
P (0, 1)
P(0, 1) = e−R0Δt
El que vence en tiempo 2:
1
1
1
P (0, 2)
e−R(1)
1
Δt
s
e−R(2)
1
Δt
>
P(0, 2) = e−R0Δt
e−R(1)
1 Δt + e−R(2)
1 Δt
2

Y as´ı, sucesivamente, hasta obtener los precios de todos los bonos cup´on cero de los
sucesivos vencimientos Δt, 2Δt, 3Δt . . . Esto es, la curva cup´on cero, CCC, de hoy.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
94

## Página 95

Valoraci´on. Modelos discretos. ´Arboles
¡Atenci´on!, los precios as´ı obtenidos son los que proporciona
el ´arbol de valores de los tipos;
junto con la hip´otesis de no arbitraje.
Los precios son tales que no hay manera de dise˜nar una oportunidad de arbitraje utili-
zando los instrumentos de mercado (los bonos cup´on cero de los distintos vencimientos).
Pero adem´as querr´ıamos que la CCC que proporciona el modelo coincida con la CCC
que observamos hoy. Es decir, calibrar el modelo ajust´andolo a los precios observados.
Para ello podr´ıamos variar los valores del ´arbol de tipos hasta que la discrepancia (por
ejemplo, medida en t´erminos cuadr´aticos) entre las dos curvas cup´on cero fuera lo
menor posible.
Aunque para esto es mejor prescribir un modelo param´etrico para la evoluci´on de los
tipos. Una de estas prescripciones es el esquema Black-Derman-Toy, que pasamos a
describir a continuaci´on.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
95

## Página 96

Valoraci´on. Modelos discretos. ´Arboles
Esquema Black-Derman-Toy
Postulamos una evoluci´on lognormal de los tipos, an´aloga a los esquemas tipo Black–
Scholes. Digamos que tenemos, como datos,
la curva cup´on cero de hoy;
y la volatilidad constante5 σ del tipo (continuo, anual) a plazo Δt.
tiempo k
j =k
j =k−2
j =−k
j =−k+2
j =k−4
j =−k+4
Vamos a cambiar ligeramente la notaci´on para referirnos a los
tipos. Etiquetamos los k + 1 nodos de tiempo k con los valores
−k, −(k −2), −(k −4), . . . , k −4, k −2, k
(obs´ervese que van de dos en dos), que indican el balan-
ce de subidas y bajadas en el ´arbol. Llamaremos, para cada
j = −k, −(k −2), . . . , k −2, k, R(k, j) al valor del tipo en el nodo
j de tiempo k.
5El caso de volatilidad no constante requiere un procedimiento m´as complicado, que se ver´a en sesiones venideras.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
96

## Página 97

Valoraci´on. Modelos discretos. ´Arboles
La especiﬁcaci´on del valor de R(k, j) es directa:
R(k, j) = U(k) ej
√
Δt σ .
La funci´on positiva U(k) recoge diversos ajustes de convexidad. El factor con la
exponencial recoge la incertidumbre del modelo.
Para construir el ´arbol de tipos
• construimos, como es habitual, el ´arbol de
ruidos (el de los valores ej
√
Δt σ);
• y luego incorporamos a cada nodo de tiempo
k el factor U(k) correspondiente.
Una vez construido el ´arbol de los tipos, aplicamos el esquema general de valoraci´on
para determinar los precios de los bonos cup´on cero de los distintos vencimientos.
Finalmente, calibramos el modelo para que estos precios coincidan con la curva cup´on
cero de hoy. Para ello, variamos la funci´on U(k) hasta que la discrepancia entre las dos
curvas sea m´ınima.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
97

## Página 98

Valoraci´on. Modelos discretos. ´Arboles
La curva cup´on cero en cada nodo
En este marco de incertidumbre que hemos ido construyendo s´olo hay una variable de
estado, el tipo a plazo Δt (por ejemplo, 3 meses).
En cada estado (cada nodo) hay una curva cup´on cero ´unica y completa, que podemos
calcular una vez construido el ´arbol.
Por tanto, de los tipos a plazo Δt debemos ser capaces de obtener tipos a otros
plazos. En este modelo, el tipo a 3 meses y el tipo a 6 meses, por ejemplo, tienen una
dependencia completa uno del otro.
Ilustraci´on
Dados σ y la CCC hoy, constr´uyase el ´arbol para el tipo a Δt = 3 meses.
(a) H´allense las CCC en nodos futuros.
(b) Obt´engase el ´arbol del tipo a plazo 6 meses.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
98

## Página 99

Valoraci´on. Modelos discretos. ´Arboles
Algunos ejemplos de valoraci´on
Rama variable de un FRA
En tiempo k se ﬁja el tipo (atenci´on, simple), que denotamos por Rs(k). El payoﬀdel
instrumento (de nominal 100 %) es Rs(k) Δt, que se hace efectivo en tiempo k + 1.
En principio, habr´ıa que calcular
E
Rs(k) Δt
β(k + 1)
	
(pues se paga en tiempo k + 1).
Pero como Rs(k) se “conoce” en tiempo k, es m´as razonable y adecuado calcular
E

Rs(k) Δt
1 + Δt Rs(k)
1
β(k)
	
(que est´a en tiempo k).
Ilustraci´on
(a) C´alculo del ´arbol de tipos simples. (b) C´alculo del precio de la rama variable del FRA.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
99

## Página 100

Valoraci´on. Modelos discretos. ´Arboles
Versi´on “in arrears”
En el caso anterior, el precio debe coincidir con la diferencia de precios entre los
bonos de tiempos k + 1 y k. Esto es, es independiente de σ. Y, de hecho, del modelo
propuesto, pues la estrategia habitual de replicaci´on no requiere especiﬁcaci´on de modelo
de evoluci´on alguno. (Y al rev´es: cualquier modelo (de no arbitraje) debe ser consistente
con el precio obtenido con la estrategia habitual de replicaci´on).
Comp´arese con el instrumento (de nominal 100 %) que, una vez ﬁjado en tiempo k el
tipo (simple) Rs(k), paga Rs(k) Δt, pero ahora se hace efectivo en tiempo k.
Caplet
El strike es K. En tiempo k se ﬁja el tipo (simple) Rs(k). El payoﬀdel instrumento (de
nominal 100 %), que se hace efectivo en tiempo k + 1, es

Rs(k) −K
+Δt.
Ilustraci´on
C´alculo en el ´arbol. ¿Qu´e ocurre si cambiamos σ?
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
100

## Página 101

Valoraci´on. Modelos discretos. ´Arboles
Replicaci´on
Las valoraciones que proporciona el modelo est´an basadas en la hip´otesis de no arbitraje
y, por tanto, en argumentos de replicaci´on.
El ejercicio ﬁnal consiste en
construir la estrategia de replicaci´on (con bonos de los tiempos adecuados) para el
caplet.
Y comprobar que se recupera la habitual estrategia de replicaci´on en el caso de la
rama variable del FRA.
c 2022 AﬁEscuela de Finanzas. Todos los derechos reservados
101

## Página 102

Gracias

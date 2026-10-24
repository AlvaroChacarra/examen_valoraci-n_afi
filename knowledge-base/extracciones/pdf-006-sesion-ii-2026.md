# PDF-006: Sesion_II_2026.pdf

Original: [archivo raw](../../raw/fundamentos/sesion-ii-2026.pdf). SHA-256: `5ffb90e68a69a5b83ac5ba7fa639da3c48159b825427644f22086753ea523397`.

Texto nativo y OCR auxiliar por página. El OCR puede alterar símbolos; no sustituye las fórmulas revisadas de conceptos ni las demostraciones de los PDF teóricos. Todas las páginas de esta sesión tienen ambos canales separados.

## Página 1

### Texto nativo

```text
Valoración: 
Modelos Discretos
Máster Executive Finanzas Cuantitativas
José María Contreras
Septiembre  2026
```

### OCR auxiliar

```text
Master Executive Finanzas Cuantitativas

Valoracion:
Modelos Discretos

José Maria Contreras

Septiembre 2026
```

## Página 2

### Texto nativo

```text
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
```

### OCR auxiliar

```text
Indice
1. Modelos binomiales
¢ El modelo binomial
* Especificacion de Jarrow-Rudd
2. Valoracion de opciones en el modelo
* Opciones europeas
* Opciones path-dependent
* Opciones con barreras
* Opciones americanas
* Replicacién/cobertura
* Dividendos
¢ Eficiencia del numero de pasos
3. Arbol consistente con la estructura temporal de volatilidad
4. Construccion y calibracion de un modelo discreto de tipos (unifactorial)
* Especificacion de Black-Derman-Toy (BDT)

em
```

## Página 3

### Texto nativo

```text
3
Modelos 
binomiales
01.
```

### OCR auxiliar

```text
01. Modelos
binomiales
```

## Página 4

### Texto nativo

```text
4
El modelo Binomial
t0
```

### OCR auxiliar

```text
El modelo Binomial

to At

evolucién del activo
```

## Página 5

### Texto nativo

```text
5
El modelo Binomial
```

### OCR auxiliar

```text
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
```

## Página 6

### Texto nativo

```text
6
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

El modelo presenta algunas ventajas:

= se implementa de manera sencilla en un Arbol binario;

= la condicién de no arbitraje en el modelo se traduce en una condicion sencilla (local,
en cada nodo del Arbol);

= permite valorar opciones cancelables (americanas);

En cierto sentido, es una versién discreta del modelo de Black-Scholes.
```

## Página 7

### Texto nativo

```text
7
El modelo Binomial
Objetivo (1):
•
Valorar una Call Europea
¿Ingredientes?
```

### OCR auxiliar

```text
El modelo Binomial

|
4

Objetivo (1):
¢ Valorar una Call Europea

AQAA

iIngredientes?
```

## Página 8

### Texto nativo

```text
8
El modelo Binomial
(*) Parámetro estructural. Cambiar este parámetro implica cambios en el precio.
*
```

### OCR auxiliar

```text
El modelo Binomial

Fijamos de partida una unidad de tiempo At® Con N saltos de At tenemos 1 afio:

NAt = 1 afio. |

Llamaremos jAt, para 7 = 0.1,..., a los sucesivos instantes de tiempo.

Activos basicos

En nuestro mercado solo habra dos activos basicos:

= un activo con riesgo, el subyacente. Llamaremos 5; a su cotizacion en tiempo jAt.

= el activo sin riesgo, la cuenta bancaria. Llamaremos (3; a su valor en tiempo jAt.

El objetivo sera, luego, valorar derivados sobre la cotizacién del subyacente.

(*) Parametro estructural. Cambiar este parametro implica cambios en el precio.

foe
```

## Página 9

### Texto nativo

```text
9
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

Numerario |

La cuenta bancaria sera nuestro numerario.

Datos de mercado

Como datos de mercado tendremos

a la cotizacién hoy del subyacente, So;
= el tipo de interés (continuo) anual R;

= la volatilidad anual o del activo subyacente.

Parametros del modelo

El modelo tiene tres parametros:

= uy d(por “up” y “down’), que seran las magnitudes de los saltos del subyacente.
Digamos que0<d<u.

= p, una probabilidad (que sera de valoracidn).

foe
```

## Página 10

### Texto nativo

```text
10
El modelo Binomial
Dispondremos de 2 datos de mercado (¿Cuáles?) y de 3 parámetros.
Consecuentemente, dispondremos de infinitos árboles que valoren 
nuestro derivado.
Tomaremos el que más nos guste, lo vemos con un ejemplo:
```

### OCR auxiliar

```text
El modelo Binomial

Dispondremos de 2 datos de mercado (;Cuales?) y de 3 parametros.

Consecuentemente, dispondremos de infinitos arboles que valoren
nuestro derivado.

Tomaremos el que mas nos guste, lo vemos con un ejemplo:

10
```

## Página 11

### Texto nativo

```text
11
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

Evolucién de los activos basicos |

Postulamos la siguiente evolucién de los activos basicos:

A

= la cuenta bancaria vale 1 hoy, vale ePRAt en tiempo At, e?”4! en tiempo 2At, etc.:

= En tiempo jAt, la cotizacién S; del activo subyacente puede tomar, en términos del
valor de tiempo anterior, dos tnicos valores:

s S;-1-u con probabilidad p;
7 | S;-1-d con probabilidad 1 — p.

11
```

## Página 12

### Texto nativo

```text
12
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

Es cémodo representar los posibles valores del subyacente en un Arbol binario como el
que sigue:

u2d?So

ud? So

evolucién del activo

d'So
```

## Página 13

### Texto nativo

```text
13
El modelo Binomial
En el esquema previo, ¿Cuántos escenarios tiene mi modelo? (ie. Nº 
sendas)
¿ Y si disponemos de 50 pasos?
```

### OCR auxiliar

```text
El modelo Binomial

En el esquema previo, ;Cuantos escenarios tiene mi modelo? (ie. N°
sendas)

é Y si disponemos de 50 pasos?

13
```

## Página 14

### Texto nativo

```text
14
El modelo Binomial
Ojo! Subir y bajar es equivalente a bajar y subir… (si no fuese así el 
problema sería difícil de implementar para un número de saltos 
elevados)
Consecuentemente, el árbol crece de forma lineal y no exponencial.
¿u y d?
```

### OCR auxiliar

```text
El modelo Binomial

Ojo! Subir y bajar es equivalente a bajar y subir... (si no fuese asi el
problema seria dificil de implementar para un numero de saltos
elevados)

Consecuentemente, el arbol crece de forma lineal y no exponencial.

guy d?

14
```

## Página 15

### Texto nativo

```text
15
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

La descripciédn matematica de la estructura anterior es como sigue:

= Tenemos unos instantes de tiempo 0, At, 2At,.... Usaremos el subindice j para
referirnos al tiempo jAt.

= El espacio de escenarios 2. = {w1,w2,...} esta formado por listas w de sucesivas
“bajadas” y “subidas” (‘sendas” en el arbol):

w = (€1,€2,€3,€4,-.-), donde los e; son +1.
Si paramos el drbol en tiempo A/At, tenemos 2™ escenarios:

w, = (41,41,...,41)
w= (-1,4+1,.. ., +1)
```

## Página 16

### Texto nativo

```text
16
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

= Tenemos una probabilidad P definida sobre cada uno de estos escenarios w, que
viene dada por la asignacién de probabilidad p a “subir” y probabilidad 1 — pa
“bajar” (mas la independencia).

Asi, si w = (€1,22,€3,€4,---),
P(w) = pitts =+1}, (1—p) #s: ©; = —1}

Esto es, p elevado al niimero de “subidas” por (1 — p) elevado al de “bajadas” .

= Codificamos las sucesivas subidas y bajadas con unas variables de estado
Yi, Y2, Y3,..., independientes e idénticamente distribuidas. En un escenario w, la
variable Y; vale 1 o —1 en funcién de que en ese tiempo jAt haya una subida o una
bajada. De forma que
Y= { +1 con probabilidad p;
J ~~) =1. con probabilidad 1 — p.

La suma >°; Yj es un camino aleatorio (no simétrico, si p # 1/2). Estas variables de
estado determinan la evolucién de todos los activos.

16
```

## Página 17

### Texto nativo

```text
17
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

= La filtracién F; = o(Yi,.... Yj) recoge la informacion desvelada hasta tiempo jAt.

a Los activos basicos son la cuenta bancaria, que en tiempo jAt vale

B; = ei RAt
y el activo subyacente S,, que en tiempo 0 vale So y que, para tiempos posteriores, es
una variable S; que toma valores en cada nodo de generacién j con la ya mencionada
prescripcion
S,= { u-S;_; con probabilidad Di
J d+Sj;-, con probabilidad 1 — p.

Observacion

La variable Sj se puede escribir en funcién de Sj_1 y la variable Yj de la siguiente manera:

5) = s)-4[v HEY) -4 (SEY)

Esto supone que Sj € Fj.

= Finalmente, la variable C'j(S) registra el valor del derivado C’ en un nodo de la
generacién j en el que el valor del activo es S; = S.

17
```

## Página 18

### Texto nativo

```text
18
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

Miramos hasta tiempo At.

= Hay 2” posibles evoluciones del subyacente, cada una con su propia probabilidad.

= Pero en ocasiones (por ejemplo, para valorar opciones europeas) no nos interesard la
senda seguida, sino el valor final del subyacente, para el que tenemos sdlo A/ + 1
posibilidades. Podemos codificar estos MJ + 1 escenarios de 0 a A, en funcidn del
numero de “subidas’’.

RMAt

— la cuenta bancaria toma el valor 3,, = e en todos ellos;

— mientras que el subyacente Sj, puede tomar los A/ + 1 valores siguientes:

Sou’dM—*,  k =0,1,...,1 M,

[ escenario | subyacente probabilidad

con probabilidades

P(S\r=Sou*d!—*) = P(BIN(M, p) =k)

MY , Ik
= (oka =i

18
```

## Página 19

### Texto nativo

```text
19
El modelo Binomial (probabilidad)
```

### OCR auxiliar

```text
El modelo Binomial (probabilidad)

Queremos que nuestro modelo de evolucién sea certificado.

Numerario | La cuenta bancaria 8; = e/®4* ser4 nuestro numerario.

Probabilidad de valoracién |

Queremos que la probabilidad P sea de valoracién (para ese numerario). Es decir, que
os procesos de precios de los dos activos basicos, la cuenta bancaria y el subyacente,
escritos en unidades del numerario (es decir, descontados), sean martingala. La evolucién
de la CB descontada es obviamente una martingala. Para el subyacente, exigimos que

Si
Ep (sam

Una expresién que parece aparatosa, pero que se traduce, simplemente, en la siguiente
condicién, que garantiza que P sea de valoracién:

Sj-1 fog
Fj-1) = GRA para cada j = 1,2,...

(condicién de martingala) up + d(1 — p) = e®**

19
```

## Página 20

### Texto nativo

```text
20
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

Observacién

DETALLE:

Ep(—_|r,_;) = + wp (s,_1[“ (vy) 41
(Sra j-1) = ojRAt p(Sj-1[5( gt) -

Sj

Ss.

~ CjRAt

= Shar Be([5 (Yj +1) - cu 5-)]|F-) = “i

d
3 G-

ej RAt

vz)

= (5 Ep(Y; +1) - SEp(Y) ;-1))

Jot [up +d(1—- p)| (utilizando que Ep(Y;)=2p-1).

20
```

## Página 21

### Texto nativo

```text
21
El modelo Binomial
¿Sentido financiero?
```

### OCR auxiliar

```text
El modelo Binomial

_Sentido financiero?

up+d(1—p)=

eRAt

21
```

## Página 22

### Texto nativo

```text
22
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

Valoracién de activos (replicables)

Si ahora C’' es un activo replicable (con activo y dinero), entonces su proceso de precios

en términos del numerario (es decir, descontado) sera también martingala:

_)\ 2. _Gizt |
j-1}) ~ GG-1)RAt

Y, en particular,

Ep(

C Ci
J |Fo) =>: esto es, Ep( )= 0.

co oa ei RAt

O, como escribiremos habitualmente,

_ = RAt Ep(C})

Esto es, el precio hoy es el promedio (descontado) de los flujos futuros.

Usaremos estas dos férmulas constantemente en las siguientes valoraciones.

22
```

## Página 23

### Texto nativo

```text
23
El modelo Binomial (calibrado del modelo)
```

### OCR auxiliar

```text
El modelo Binomial (calibrado del modelo)

Tenemos tres datos de mercado: el tipo R, la cotizacién inicial So y la volatilidad anual
del activo oc.

e Ya hemos calibrado al dato Sp exigiendo que la evolucién arranque en ese valor.

e Ahora vamos a exigir que la evolucién del subyacente acumule exactamente una
volatilidad anual o. Es decir, que la desviacién tipica de los rendimientos del activo en

un afio valga o:
. S
2 V(in —*) .
So
La rentabilidad (continua) en un afio se expresa directamente en términos de las
rentabilidades en los periodos At sucesivos:

Sw S1 So _SN- 1
m2X =] ( . X) = l
"3 NSS, Soo a Yong "

Pero las rentabilidades parciales In(.5;/S;_1) son variables independientes (e idéntica-
mente distribuidas). Asi que la varianza de la suma es N veces una de las varianzas.

23
```

## Página 24

### Texto nativo

```text
24
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

Estos rendimientos parciales son

in ( Sj ) _ Inu con probabilidad p
S Ind_ con probabilidad 1 — p

j-1

y un pequefio calculo nos dice que esas varianzas individuales son

Vv [in ( Si | = p(1—p)(In(u) —In(d))? asi que a? = N p(1 —p)(In(w) — In(d))?.

Si

Observacién

DETALLE:

B| In ( a )] = pln(u) + (1 — p) In(d); b[n? (2 )] = pln?(u) + (1 — p) In?(d)

Sj-1 Sj-1
V[in ( Si )] = pin? (w) + 1 = p) in? (a) = (PIn(u) + 1 = p))? FS pa = p)(An(w) = In(a))?..
Sia

24
```

## Página 25

### Texto nativo

```text
25
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

Y como NAt = 1, obtenemos la segunda ecuacién:

(ajuste al dato de volatilidad) oVAt = Vp(1—p) [In(u) — In(d)]

25
```

## Página 26

### Texto nativo

```text
26
El modelo Binomial
```

### OCR auxiliar

```text
El modelo Binomial

En resumen, dados los datos de mercado R, So y 0, podemos construir un modelo de
evolucién (de paso At)

a libre de arbitraje (certificado);

= de forma que la volatilidad anual sea exactamente o

sin mas que exigir que el activo arranque en el valor So y que los pardmetros u, d y p
verifiquen el par de ecuaciones:

eRAt = upt d(1—p)

oa VAt = \V/p(1 — p) (nu — Ind)

Obsérvese que se trata de un sistema no lineal de dos ecuaciones. Y que hay tres
parametros en el modelo (u, dy p).

26
```

## Página 27

### Texto nativo

```text
27
Especificación de Jarrow–Rudd
```

### OCR auxiliar

```text
Especificacion de Jarrow—Rudd

Para empezar fijamos
p=50%

Las dos ecuaciones son ahora

u+d
eRAt — 5) (condicién de martingala)
Inu — Ind
oVAt = —_ (ajuste al dato de volatilidad)

La solucién explicita de este par de ecuaciones viene dada por:

y — cRAt eoVAt 2
eo VAt 4 e—oVAt

d= ehAt eo VAt | 2 |

ovat 4 p-oVAt

27
```

## Página 28

### Texto nativo

```text
28
Valoración de 
opciones en el 
modelo
02.
```

### OCR auxiliar

```text
02. Valoracion de
opciones en el
modelo
```

## Página 29

### Texto nativo

```text
29
Opciones europeas
Objetivo: Valorar una opción call europea.
Recuerda, tal y como se vio en la página 22:
```

### OCR auxiliar

```text
Opciones europeas

Objetivo: Valorar una opcion call europea.

Recuerda, tal y como se vio en la pagina 22:

. —jRAt -
=e? Ep(C;)

Esto es, el precio hoy es el promedio (descontado) de los flujos futuros.

29
```

## Página 30

### Texto nativo

```text
30
Opciones europeas
```

### OCR auxiliar

```text
Opciones europeas

Método 1. Valoracién con férmula

Hay Af + 1 posibles pagos de la opcidn, tantos como posibles valores del subyacente a
vencimiento (véase la pagina 14). Aplicamos directamente la formula

Co _ eo MRAt Ep(Cy) .

pues el valor medio de la derecha se puede calcular muy facilmente.

Notese primero que se trata de una suma (ponderada) con Af + 1 términos. En cada
escenario,

a los valores que se promedian son los nimeros

f(SoutaM);

’

= y se promedian con las probabilidades

(eta —p)M-k

30
```

## Página 31

### Texto nativo

```text
31
Opciones europeas
```

### OCR auxiliar

```text
Opciones europeas

En el caso de la call con strike A’, los flujos son
+k gM—k  pe\t
(Sou*a™ _ Kk)

y por tanto el valor hoy se obtiene con la siguiente formula:

M
oy Mok at (MY 4 -k
C= (« MRALY . S (Souka™ k —K) ( oka —p) k
——"" rm —__—_---- k
descuento = flujo
probabilidad

EJEMPLO BASE

Calculo del valor hoy de la call de strike K = 84.

EJEMPLO BASE

Calculo del valor hoy de una opcidén europea con un payoff arbitrario.
```

## Página 32

### Texto nativo

```text
32
Opciones europeas
```

### OCR auxiliar

```text
Opciones europeas

Método 2. Valoraci6n en el arbol

Se trata de interpretar la condicién

Ci C;
j . _ j=l wpe yo _ -RAt 7 .
Er( Fi) == que reescribimos Cj—1 = « Ep (Cj|Fj-1)
como un procedimiento de cdlculo recursivo (hacia atrds) (M-1)At MAt

en el drbol. Nos fijamos, por ejemplo, en los dos nodos
superiores en tiempo J/At (vencimiento). Los valores Cy y
C son conocidos. El valor C’y se obtiene aplicando la formula
de arriba, que aqui simplemente nos dice que

Cr =e "4! (pC, + (1—p)Cs).

Se procede igual con los demas nodos de tiempo (A/ — 1)At, hasta tenerlos todos.
Luego se repite el proceso para los nodos de tiempo (Af — 2)At, etc., hasta llegar a Co.

Arbol de valoracién de la call europea de strike K = 84.

32
```

## Página 33

### Texto nativo

```text
33
Opciones europeas
```

### OCR auxiliar

```text
Opciones europeas

Método 3. Simulacién

Una manera alternativa de utilizar la formula
—MRAt
Co =e Ep(Cuv)

pasa por interpretar la esperanza de la derecha como un promedio sobre todos los
posibles escenarios (sendas en el arbol). Ese promedio involucra 2 términos, uno por
senda, cada uno con una cierta probabilidad (o la misma, en el caso p = 1/2).

Caben, pues, dos alternativas:

a Exhibir todos los escenarios/sendas, anotar el pago de la opcidn en cada una de ellas,
y promediar esos valores con las respectivas probabilidades (y descontar al final);

= o bien, si el universo de escenarios es demasiado grande, muestrearlo, simulando un
numero suficiente de escenarios.

Simulador en Excel para valoracién de europeas.

33
```

## Página 34

### Texto nativo

```text
34
Opciones path-dependent
```

### OCR auxiliar

```text
Opciones path-dependent
Valoracién de derivados path-dependent

Tenemos un instrumento C' que paga, a vencimiento J/ At, una cierta cantidad

f(S1,S2,..-, Sar)

que depende de (quizds) toda la senda de cotizaciones del subyacente.

Su valor hoy sera

Co =e MEA! Ep(Cur) = "A" Ep(f(S1, 52, ---. Sur).

= jValoracion con férmula? La anterior es una formula para el valor de la opcidn; pero
se trata de una suma con 2™ términos.

= jValoracion en el Arbol? En general, no es posible. Digamos que queremos valorar una
call asidtica en la que el flujo depende de la media aritmética A de las cotizaciones.

Consideremos un arbol binomial con sdélo dos periodos.

34
```

## Página 35

### Texto nativo

```text
35
Opciones path-dependent
```

### OCR auxiliar

```text
Opciones path-dependent

En una opcidn usual, calculamos el flujo a partir de los nodos del ultimo nivel y
procedemos hacia atrds en el arbol. Pero ahora, aunque el activo en dos perfodos
alcanza tres valores, la media A toma cuatro distintos, pues “distingue” entre:

2
5 5 . ,[{! id urs
en el camino S + uS > udS, A vale S (a)
udS
en el camino S + dS > udS, A vale S (a + “+ “.
2s

a |; Valoracién por simulacién? Es el método mas razonable: muestreamos el espacio
de los 2 escenarios, sorteando sendas de cotizaciones del subyacente en el drbol,
anotamos en cada muestra el payoff de la opcidn, y luego promediamos con media
aritmética (ademas de descontar).

35
```

## Página 36

### Texto nativo

```text
36
Replicación/cobertura
```

### OCR auxiliar

```text
Replicacion/cobertura

Replicacién/cobertura en un solo periodo

Partimos de la situacién general:

cuenta bancaria subyacente derivado
eRAt uSo Cu
eRAt dSo Ca
Los valores C,, y Cy son conocidos. Vamos a formar una cartera con a unidades en la
cuenta bancaria y 3 en subyacente. Los valores de a y ( son la solucién del sistema de

ecuaciones

= aeFAt + Bu So
Ca= ae®*t + Bd So

Una vez obtenidos los valores de a y 3, valoramos el derivado:

Co=atBSo.

36
```

## Página 37

### Texto nativo

```text
37
Replicación/cobertura
```

### OCR auxiliar

```text
Replicacion/cobertura

Resolviendo el sistema de ecuaciones anterior, deducimos que el activo C’ equivale a la
cartera que consta de 3 unidades de subyacente, donde

3 Cu—Ca __ incremento de valor del derivado
° Su— Sd incremento de valor del subyacente

Esta cantidad 3 se conoce, en la jerga habitual, como delta.

Se trata de cobertura estatica: un solo periodo de tiempo.

37
```

## Página 38

### Texto nativo

```text
38
Opciones con barreras
```

### OCR auxiliar

```text
Opciones con barreras
Valoraci6n de opciones con barrera

Veremos ahora cémo valorar opciones con barrera usando Arboles. Las opciones con
barrera mas simples tiene formulas cerradas, pero sdlo las mas simples. En general,
cuando la estructura de la barrera (o barreras) es ligeramente compleja, es necesario
usar Arboles o simulacién Montecarlo, con cierto cuidado en cualquier caso.

Consideremos el activo que ya hemos usado anteriormente y que tiene el drbol de
evolucion siguiente:

0 1 2 3 4 5 6
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
```

## Página 39

### Texto nativo

```text
39
Opciones con barreras
```

### OCR auxiliar

```text
Opciones con barreras

Podemos incorporar estos datos al Arbol. Los pagos a vencimiento o extincién de la
opcidn son los siguientes:

strike 34
barrera KO 100

tiempo
0,0000 0,000 19,0000 _0,0000

,0000 _0,0000

94811

,0000

,0000

0,0000

0,000

Y ahora procedemos hacia atrds en el arbol. Rellenamos los valores del nivel anterior
al vencimiento (que la barrera no haya determinado ya) y luego el nivel anterior. Y asf
sucesivamente. El resultado es:

strike 84
barrerakO___100
tiempo 0 1 2 3 4 5 6

| 13266 | 11,4753 1,1812 0,0000 0,0000 0,0000 0,0000

41,1802 L778 2,3644 2,3663, 0,0000 0,000

0,5906 11822 2,3663 4,7366 94811

0,000 0,0000 0,000 0,0000

0,0000 0,0000 ,0000

0,000 ,0000

0,0000

39
```

## Página 40

### Texto nativo

```text
40
Opciones Americana
Quieres vender un coche.
Recibes ofertas (por ejemplo, un total de 10)
Problema, no puedes elegir entre todas las ofertas, tendrás que ir 
aceptando o rechazando una a una sin poder volver al pasado ni 
dispondrás de información sobre el futuro.
```

### OCR auxiliar

```text
Opciones Americana

Quieres vender un coche.
Recibes ofertas (por ejemplo, un total de 10)
Problema, no puedes elegir entre todas las ofertas, tendras que ir

aceptando o rechazando una a una sin poder volver al pasado ni
dispondras de informacion sobre el futuro.

40
```

## Página 41

### Texto nativo

```text
41
Opciones Americana
```

### OCR auxiliar

```text
Opciones Americana

41
```

## Página 42

### Texto nativo

```text
42
Opciones Americana
```

### OCR auxiliar

```text
Opciones Americana

0,75 one
.
4 os
8

um bral

niim ero de ofertas restantes

nim ex de ofertas restantes

En general, el umbral para aceptar una oferta cuando quedan k: ofertas sera el valor
que se tiene cuando quedan /; — | ofertas:

Up = Ve-1-

De manera que

Vi = E(Fu|Fie > Vi-1) »P (Fie > Vi-1) + Vien» P (Fe < Vie-1) ,

de donde resulta que ;
14+V2,
=:

Vie =

42
```

## Página 43

### Texto nativo

```text
43
Opciones Americana
```

### OCR auxiliar

```text
Opciones Americana

Valoracién de opciones americanas en el arbol

En las opciones americanas, el poseedor de la opcidn tiene el derecho de ejercerla en
cualquier momento entre el comienzo del contrato y el vencimiento.

Valoracién de una put americana. Denotaremos por V,, los valores de la opcién put en
el paso 7; 0, con mas precision, por V,,(), si queremos hacer explicita la dependencia
en la cotizacidn S en ese instante.

En el instante n, el poseedor de la put tiene dos opciones:

1) Ejercer en ese instante y obtener (K — S,,)*. Este es el valor de ejercicio, que

denotamos por VE,,:
VEn(Sn) = (kK _ Sn)*.

11) No ejercer: se tiene entonces un valor de continuacién VC,, que viene dado por el
valor medio (riesgo-neutro)

VEn(Sn) =e F*! [pVingi(Sn + ¥) + (1 =p) Vnei(Sn +d) = eB 4'E (Vig i] Sn)

El valor V,, sera el maximo entre VE, y VC,,.

43
```

## Página 44

### Texto nativo

```text
44
Opciones Americana
```

### OCR auxiliar

```text
Opciones Americana

De manera que

VEn (Sn) = (k ~~ Sn)*
Vi(Sp) = max
VC, (Sn) = e RATE (Vin4i|Sn)

Como ademas en el instante del vencimiento tenemos que
aa +
v =(K —Sy)*,

podemos implementar un procedimiento recursivo (regresivamente) para calcular el valor
de la put americana en el instante 0.

44
```

## Página 45

### Texto nativo

```text
45
Opciones Americana
```

### OCR auxiliar

```text
Opciones Americana

Call americana vs. call europea

En principio, las opciones americanas han de ser mas valiosas que las correspondientes
europeas. Pero la call americana (sobre un subyacente que no reparte dividendos) vale
lo mismo que una call europea. Esto es, nunca conviene ejercer antes del vencimiento 7’.

La paridad call-put nos dice que, en cualquier instante t < T’, el precio de la call europea
C(t), el precio de la put P(t) (ambas con strike Hv) y el tipo R estan relacionados por:

C(t)=P(t)+S(t)-—Ke"®T-9 = C(t) >S(t)-Ke® TOs S(t) -—K.

Es decir, la call europea es siempre mas valiosa que el ejercicio anticipado.

45
```

## Página 46

### Texto nativo

```text
46
Opciones (Acelerador cálculos)
```

### OCR auxiliar

```text
Opciones (Acelerador calculos)
Arbol de precios de Arrow-Debreu

he Pp

“>C —3|C=[A-(1—p)+B-p]-e7®**

Bo

46
```

## Página 47

### Texto nativo

```text
47
Dividendos
```

### OCR auxiliar

```text
Dividendos

Spe Soel(R-@)-0? /2IT +e VTN (0,1)

Sacando un factor e QT vemos que, si A’, R, y T fijos:

Call con rentabilidad por dividendos Q y precio de activo Sg
equivale a
Call con rentabilidad por dividendos 0 y precio de activo e~@7 - Sp

47
```

## Página 48

### Texto nativo

```text
48
Dividendos
```

### OCR auxiliar

```text
Dividendos

Dividendos fijos

. a: dividendo D
Supongamos que en tiempo T’ recibiremos un So St SL, meen

tinico dividendo conocido D (por accién).  In-
terpretamos que la cotizaci6n S; del activo tiene
dos partes: por un lado, el valor (descontado) del dividendo; y, por otro, la parte con
incertidumbre, que llamaremos S/:

it |
|
0 t T

S, =S¥+De-RT-) sit <T;
S, = St sit >T.

El valor de la inversién en el activo en tiempo t viene dado por
St+ De RE-9

que coincide con la cotizacién hasta la fecha de pago del dividendo. Queremos valorar
un derivado sobre este subyacente. Ndtese que el pago del derivado depende de la
cotizacién del activo.

48
```

## Página 49

### Texto nativo

```text
49
Dividendos
```

### OCR auxiliar

```text
Dividendos

Implementaci6én en el arbol binomial

Supongamos que se van a recibir dos dividendo D1 dividendo Do
dividendos (conocidos hoy), Dy y Do, o TA, 4 Ro | ; r
en tiempos JT; y T>. La opcidn que a

. At
queremos valorar vence en tiempo J’.

Fijamos un At para nuestro arbol binomial, de manera que \/ At = T. Los inputs de

mercado son R, el tipo anual, o, la volatilidad del subyacente y Sp, la cotizacién hoy
del activo.

Para valorar el derivado necesitamos el arbol de la cotizacién S;, que consta de dos
partes: S;*, con la incertidumbre, y PD;, el “proceso de dividendos” (sin incertidumbre):

S,= Si +PD:,
donde
_ dD, eH T-OR sit < Ti, Dy e(R-OR sit < Th,
Pr={ 4 + {i

sit >T\, sit > Td.
49
```

## Página 50

### Texto nativo

```text
50
Dividendos
```

### OCR auxiliar

```text
Dividendos

Procedimiento:

1. Con los valores de R y o se determinan los valores de los parametros u, d y p.

2. Con el valor Sj y los valores de u y d construimos el arbol de valores de S;* hasta
tiempo T’ (esto supone que consideramos que a es la volatilidad de S*).

3. Calculamos los valores del proceso de dividendos PD; (ndotese que es un vector fila
en Excel, pues no tiene incertidumbre).

4. Construimos el 4rbol de cotizaciones S; a partir del de S* aumentando todos los
valores de los nodos de tiempo jAt con el correspondiente valor PD; +. Este arbol
no sera martingala (con p), pero nos servird para valorar la opcidn.

5. Podemos también construir el arbol del valor de la inversiédn en el activo, cuyos
valores vienen dados por S;* + D, eT-9OR + —)y e~(T2-OR

6. La valoracién del derivado utiliza el arbol de cotizaciones 5; y los promedios se
calculan con p.

50
```

## Página 51

### Texto nativo

```text
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
```

### OCR auxiliar

```text
Eficiencia del numero de pasos

Problema:
¢ La naturaleza discreta infiere que el modelo valore un mismo producto con precios

diferentes segun el numero de pasos (equivalentemente el periodo temporal entre
nodos del arbol).

Valor Opcién

Num_pasos

¢ Valoracion de una opcién americana con vencimiento 1 afio, valorada en base al
numero de saltos indicados en el eje X.

51
```

## Página 52

### Texto nativo

```text
52
Eficiencia del número de pasos
Motivo:
•
La discontinuidad de la delta de la opción a vencimiento. 
Mejora en la eficiencia del número de pasos:
•
Emplear Black-Scholes (en lugar del valor esperado del árbol) en los nodos del árbol del 
instante previo al vencimiento de la opción.
```

### OCR auxiliar

```text
Eficiencia del numero de pasos

Motivo:

¢ La discontinuidad de la delta de la opcién a vencimiento.

Mejora en la eficiencia del numero de pasos:

* Emplear Black-Scholes (en lugar del valor esperado del arbol) en los nodos del arbol del
instante previo al vencimiento de la opcidn.

Valoracion en arbol

Tiempo i!) as 2 3 4 5 6 7 8 9 10 i 12

9.109 12.865 17.791 24.053 31.749 40.882 51.359 63.048 75.865 89.853 105.114 121.764 139.925
5.407 8.014 11.632 16.497 22.802 30.643 39.971 50.599 62.321 75.116 89.079 104.314

2.832 4,442 6.836 10.289 15.094 21.493 29.576 39.173 49.889 61.592 74.365

1.238 2.074 3.423 5.544 8.783 13.536 20.152 28.686 38.477 49.180

0.409 0.739 1.321 2.338 4.080 7.000 11.736 19.062 27.999

0.082 0.160 0.312 0.609 1.185 2.304 4.473 10.188

0.004 0.009 0.018 0.036 0.072 0.144 0.000

0.000 0.000 0.000 0.000 0.000 0.000

0.000 0.000 0.000 0.000 0.000

0.000 0.000 0.000 0.000

0.000 0.000 0.000

0.000 0.000

0.000

52
```

## Página 53

### Texto nativo

```text
53
Eficiencia del número de pasos
Consecuencia:
•
Este cambio en el modelo hace que se consiga una mejora considerable en la 
precisión de valoración de las opciones americanas.
```

### OCR auxiliar

```text
Eficiencia del numero de pasos

Consecuencia:
Este cambio en el modelo hace que se consiga una mejora considerable en la

precision de valoracién de las opciones americanas.

Valor Opcién

Num_pasos

53
```

## Página 54

### Texto nativo

```text
54
Árbol consistente con 
la estructura temporal 
de volatilidad
03.
```

### OCR auxiliar

```text
03. Arbol consistente con
la estructura temporal
de volatilidad
```

## Página 55

### Texto nativo

```text
55
```

### OCR auxiliar

```text
Ajuste del arbol a la curva de volatilidades

Construiremos el Arbol casi como en el caso general (de Jarrow—Rudd), pero para poder
captar la estructura de volatilidad y para que, ademas, el arbol sea recombinante, los
intervalos de tiempo de los pasos del Arbol no seran todos iguales.

Datos

= una curva de volatilidades spot a ciertos vencimientos ft, t2,..., 7’. Supongamos, por
comodidad, que el tiltimo vencimiento coincide con el de la opcidén. Llamemos a estas

volatilidades

Las varianzas acumuladas hasta tiempo t, son las cantidades V; = t;o(t;). La varianza
acumulada hasta el plazo final es T'o?(T’).

55
```

## Página 56

### Texto nativo

```text
56
```

### OCR auxiliar

```text
Procedemos en etapas:

Fijamos una unidad de volatilidad A. Para ello, decidimos
Arbol hasta tiempo 7’. Tomamos A de manera que

NA? =To?(T).

Para ese nivel de referencia A, construimos el arbol
aditivo, con todas las probabilidades iguales a 50%,
pero sin especificar el intervalo de tiempo que abarca
cada paso.

La varianza acumulada hasta tiempo j es jA?.

cudntos pasos NV tendrd el

56
```

## Página 57

### Texto nativo

```text
57
```

### OCR auxiliar

```text
Buscamos ahora la serie de tiempos

T,To,.... Tn

tales que la varianza acumulada hasta tiempo 7; sea justamente jA?. Asi, la varianza
en cada intervalo [71,7] es A?.

(Los tiempos T; se obtienen interpolando en la tabla que relaciona los tiempos ¢; con
las varianzas acumuladas t;o7(t;)).

Los tiempos que marcan los intervalos del arbol son los 7. Los valores del arbol son los
usuales, pero los intervalos de tiempo no son iguales.

|Obtencién de intervalos de tiempo del érbo!

57
```

## Página 58

### Texto nativo

```text
58
```

### OCR auxiliar

```text
Etapa 4 |

Calculamos las derivas que corresponden a los nodos de tiempo 7, y que resultan ser:

2 j
Tj R(Tj) | ajuste de deriva por volatilidades —+ =]

deriva por tipos —> e
p p cA 4 eA

(para las primeras, habra que interpolar en la curva de tipos).

Observacién

El ajuste de la deriva proviene de que la esperanza de la variable que toma los valores eA y eA (con probabilidad 1/2
cada uno) es, obviamente, (eA + e7A)/2.

Etapa 5 | El arbol del subyacente se construye combinando estos tres efectos, de la

manera habitual:

2 Jj
1 kA (T;R(T;)
Soe c ; [a + =a

(j depende del paso, / del nodo).

58
```

## Página 59

### Texto nativo

```text
59
Construcción y 
calibración de un 
modelo discreto de 
tipos (unifactorial)
04.
```

### OCR auxiliar

```text
04. Construccion y
calibracion de un
modelo discreto de
tipos (unifactorial)
```

## Página 60

### Texto nativo

```text
60
```

### OCR auxiliar

```text
Vamos a prescribir una evolucion aleatoria en el tiempo de tipos de interés. El tiempo
estard discretizado y representaremos los posibles estados con un Arbol binomial.

Queremos que este modelo de evolucién esté libre de oportunidades de arbitraje, para
que permita valorar instrumentos cuyo precio se derive de los tipos (promediando flujos
adecuadamente descontados).

= Interesara que este esquema de valoracién sea capaz de dar correctamente los precios
de referencia del mercado, que en nuestro caso serdn los bonos cupon cero de los
sucesivos vencimientos (y, quizds, algunos instrumentos con opcionalidad, como caps,
swaptions). Es decir, calibraremos el modelo a los precios de mercado.

= Y argumentaremos que, una vez calibrado, el esquema sera también capaz de valorar
“adecuadamente” (jinterpolacién!) los instrumentos que no estén en mercado.

Empezamos con toda generalidad. El paso temporal At esta fijado.

Vamos a construir un arbol binomial a la Jarrow—Rudd (todas las probabilidades son 1/2)
para el tipo (continuo, anual) a plazo At.

60
```

## Página 61

### Texto nativo

```text
61
```

### OCR auxiliar

```text
Denotamos? por R;, al tipo (continuo, anual) a plazo At que tenemos en tiempo kAt.
En nuestro esquema binomial, ;, es aleatorio, y toma k +1 valores, uno en cada nodo.

tiempo 0 tiempo At tiempo 2At

1

Ro toma 1 valor
Ry toma 2 valores

Ry toma 3 valores

| fi

Ro variable Ry variable Ro

3Una notacién mas precisa para Rx, pero que aqui no usaremos, seria R(kAt, (k + 1)At). Elegimos tipos continuos
también por comodidad notacional, aunque también podrian ser tipos simples (y, de hecho, ésa suele ser la eleccién habitual).

61
```

## Página 62

### Texto nativo

```text
62
```

### OCR auxiliar

```text
Eleccién de numerario

Supongamos que ya tenemos construido el Arbol con los valores de los tipos (mas
adelante propondremos un esquema para parametrizar esos valores).

Las consideraciones probabilisticas que haremos a continuacion se refieren a trayectorias
en el arbol anterior, a las que nos referiremos genéricamente como trayectorias w.

Ahora elegimos el numerario para descontar precios: la cuenta bancaria, cuyo valor en
tiempo k denotamos por 3(k).

B(k) es la variable aleatoria que recoge la capitalizacién de 1 euro de tiempo 0 (en
depdsito rodante cada At) hasta tiempo kAt.

Por ejemplo, 3(0) = 1, mientras que 3(1) = e*%04". A partir de tiempo 2A¢t es ya una
variable aleatoria.

Pero en general el valor de 3(k) no sdlo depende del nodo de tiempo k en el que
estemos (de entre los k + 1 posibles), sino también del camino w que nos haya Ilevado
a ese nodo (es path dependent).

62
```

## Página 63

### Texto nativo

```text
63
```

### OCR auxiliar

```text
Por ejemplo, para tiempo 2 tenemos

Ry (nodo
B(2) = e( Rot Ri (nodo up)) At

trayectoria w

‘

Ry (nodo up)

B(2) = e(Ro+Ri(nodo up)) At
trayectoria wo

trayectoria w3 B(2) = e(RotRi(nodo down)) At

C?

Ry (nodo down)

trayectoria w4
B(2) = e(Ro+ Ri (nodo down)) At

Ry(nodo d

/

Obsérvese la diferencia entre las trayectorias w y w3, que Ilegan al mismo nodo central.

63
```

## Página 64

### Texto nativo

```text
64
```

### OCR auxiliar

```text
Metodologia de valoracién

Instrumentos de mercado

Los instrumentos que vamos a considerar como “de mercado” son los bonos cupon cero
de distintos vencimientos*.

Es importante sefialar que todos los vencimientos deben ser multiplos de At, el paso
elegido en el Arbol.

Denotaremos por

P(k,T)

el precio en tiempo k:At del bono cupén cero de nominal 1 y vencimiento 7 (un multiplo
de At).

De nuevo es una cantidad aleatoria que depende, ademas de k y de JT’, del nodo de
tiempo k en el que estemos y, quizds, de la trayectoria w que nos lleve hasta él.

4 Aunque luego incluiremos instrumentos con opcionalidad.

64
```

## Página 65

### Texto nativo

```text
65
```

### OCR auxiliar

```text
No arbitraje

Siguiendo nuestra idea general de valoracién por no arbitraje, pretendemos que el proceso
que da cuenta, en cada tiempo k, del precio (descontado con la cuenta bancaria) del

bono que vence en tiempo 7’,
( 2)
B(k) k

sea martingala (bajo la probabilidad considerada).

Esto supone que

P(k,T) _ P(k=1,T)
() B( BUR) | Fes) = BR 1)

para cada k =1,2....
```

## Página 66

### Texto nativo

```text
66
```

### OCR auxiliar

```text
Valoracié6n

Si se cumpliera (x), entonces, aplicandola reiteradamente obtendriamos el precio hoy
del bono cupon cero de vencimiento T’:

P(k.T)\ P(0,T)
B( Bm) )- B(0)

Andlogamente, si X es cualquier instrumento (replicable en términos de estos bonos)
cuyo payoff conozcamos, por ejemplo, en tiempo k, entonces podriamos valorarlo de
manera analoga:

e(S) = Fy

Y si X no fuera replicable, esta metodologia atin nos proporcionaria un precio del
instrumento (por interpolacién).

66
```

## Página 67

### Texto nativo

```text
67
```

### OCR auxiliar

```text
No arbitraje, ya en el arbol

Parece que (x) es una condicién muy aparatosa, dado que todas las cantidades
involucradas dependen de las trayectorias seguidas.

Pero obsérvese en qué se traduce en nuestro esquema binomial.

Digamos que estamos en un nodo de tiempo k;—1 (nodo tiempo k—1 tiempo k
inicial) y consideremos sus dos vecinos de tiempo k
(nodos up y down).

nodo up

Al nodo inicial hemos Ilegado siguiendo una cierta
trayectoria, digamos w, que determina el valor 3(k — 1)
correspondiente.

trayectoria w

En ese nodo inicial, R;,—1 tiene un cierto valor, el
correspondiente del Arbol de tipos.

La condicién de martingala se escribe de la siguiente manera:

1 P(nodo up,T) | 1 P(nodo down,T) _ P(nodo inicial, 7)

(+) 2 B(nodo up) a) B(nodo down) ~~ B(nodo inicial)

67
```

## Página 68

### Texto nativo

```text
68
```

### OCR auxiliar

```text
En esta formula, cuando escribimos nodo up (0 nodo down, 0 inicial), estamos conside-
rando no sélo el nodo en el que estamos (y el tiempo al que corresponde), sino también
“cémo” hemos llegado a ellos.

Pero obsérvese que
3(nodo up) = 8(nodo inicial) - e®*—14¢

B(nodo down) = 3(nodo inicial) - ePr-1At

De manera que la formula (x*), la condiciédn de martingala, se escribe simplemente
como

(c+) o~eaae (Pinode up, J’) + P(nodo down, T)

5 ) = P(nodo inicial, T)

Esta sencilla observacién es clave, pues nos va a permitir valorar los bonos cupén cero
de los sucesivos vencimientos sin mas que utilizar recursivamente la formula (* * x)
anterior.

68
```

## Página 69

### Texto nativo

```text
69
```

### OCR auxiliar

```text
Simplemente hay que observar que sabemos que el bono que vence
en tiempo T vale justamente 1 en todos los nodos de tiempo 7’. 1
Digamos, por ejemplo, que el drbol de valores de tipos empieza %o
como mostramos a la derecha.

Por ejemplo, el bono que vence en tiempo 1:
1

P(0,1) P(0,1) = e~ Rot
1

El que vence en tiempo 2:

—RY AL 1
e i

(1) (2)
RYPAt yy eR at

P(0,2) 1 P(0,2) = e~Ro et 5

C

Rat
e 1

Y asi, sucesivamente, hasta obtener los precios de todos los bonos cupén cero de los
sucesivos vencimientos At, 2At, 3At... Esto es, la curva cupon cero, CCC, de hoy.

69
```

## Página 70

### Texto nativo

```text
70
```

### OCR auxiliar

```text
jAtencién!, los precios asi obtenidos son los que proporciona

= el Arbol de valores de los tipos;

= junto con la hipotesis de no arbitraje.

Los precios son tales que no hay manera de disefiar una oportunidad de arbitraje utili-
zando los instrumentos de mercado (los bonos cupén cero de los distintos vencimientos).

Pero ademas querriamos que la CCC que proporciona el modelo coincida con la CCC
que observamos hoy. Es decir, calibrar el modelo ajustandolo a los precios observados.

Para ello podriamos variar los valores del arbol de tipos hasta que la discrepancia (por
ejemplo, medida en términos cuadraticos) entre las dos curvas cupon cero fuera lo
menor posible.

Aunque para esto es mejor prescribir un modelo paramétrico para la evolucién de los
tipos. Una de estas prescripciones es el esquema Black-Derman-Toy, que pasamos a
describir a continuacidn.

70
```

## Página 71

### Texto nativo

```text
71
```

### OCR auxiliar

```text
Esquema Black-Derman- Toy

Postulamos una evolucién lognormal de los tipos, andloga a los esquemas tipo Black—
Scholes. Digamos que tenemos, como datos,

2
= la curva cupén cero de hoy;

m y la volatilidad constante® o del tipo (continuo, anual) a plazo At.

tiempo k:
Vamos a cambiar ligeramente la notacién para referirnos a los j=k
tipos. Etiquetamos los k + 1 nodos de tiempo con los valores e ake
j=k-4
—k,—(k —2),-(k—4),..., k—-4,k-—2,k
(obsérvese que van de dos en dos), que indican el balan- ea okt4
ce de subidas y bajadas en el Arbol. Llamaremos, para cada e j=—k+2
j=-k

j =—k,—-(k—2),...,k—2,k, R(k, 7) al valor del tipo en el nodo
j de tiempo k.

5EI caso de volatilidad no constante requiere un procedimiento mas complicado, que se vera en sesiones venideras.

71
```

## Página 72

### Texto nativo

```text
72
```

### OCR auxiliar

```text
La especificacién del valor de R(k:, 7) es directa:

R(k,j) = U(k) VA

La funcién positiva U(k) recoge diversos ajustes de convexidad. El factor con la
exponencial recoge la incertidumbre del modelo.

Geren | 4.081% 1.953%) y 9.681% 3.843%

Para construir el 4rbol de tipos

@ construimos, como es habitual, el arbol de
ruidos (el de los valores e7¥4‘7)

e y luego incorporamos a cada nodo de tiempo
k: el factor U(k) correspondiente.

Una vez construido el arbol de los tipos, aplicamos el esquema general de valoracién
para determinar los precios de los bonos cupon cero de los distintos vencimientos.

Finalmente, calibramos el modelo para que estos precios coincidan con la curva cupon
cero de hoy. Para ello, variamos la funcién U(k) hasta que la discrepancia entre las dos
curvas sea minima.

72
```

## Página 73

### Texto nativo

```text
73
Véase para más detalle 
Documentación teórica del 
Curso
```

### OCR auxiliar

```text
Véase para mas detalle
Documentacion teorica del
Curso

73
```

## Página 74

### Texto nativo

```text
Gracias
```

### OCR auxiliar

```text
Gracias
```

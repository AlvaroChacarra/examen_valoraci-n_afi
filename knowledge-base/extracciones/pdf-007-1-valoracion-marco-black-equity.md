# PDF-007: 1.Valoración. Marco Black Equity.pdf

Original: [archivo raw](../../raw/marco-black/1-valoracion-marco-black-equity/1-valoracion-marco-black-equity.pdf). SHA-256: `64bb0c4fc8e4b5ea75da1c0b2fd9625242cdacf0ef9de97a81e3643dd7bed97b`.

Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.

## Página 1

Modelización Black.
Modelos estándar para Equity
Valoración
José Javier Calderón jcalderon@afi.es

## Página 2

Valoración. Marco Black
2
1. Introducción
2. Marco Black en equity
3. Marco Black en tipos de interés
1. Para tipos forward
2. Para tipos swap
Anexo I. Nuevo marco tipos
Anexo II. Marco Black en FX
Índice

## Página 3

Valoración. Marco Black
3
Introducción
01.

## Página 4

Valoración. Marco Black
4
Enfoque
El marco Black de modelización es un enfoque general para construir modelos de mercado libres de arbitraje.
Es el enfoque estándar con el que “cotizan” las opciones básicas (vanilla) de equity, de tipos de interés y de tipo de cambio.
En la práctica, el marco Black es un diccionario que traduce precios de opciones en volatilidades y viceversa, permitiendo así 
la comparación homogénea de opciones con distintos subyacentes, vencimientos, strikes, etc.
La volatilidad de los derivados en el marco Black desempeña un papel análogo al de la TIR en el descuento de flujos de 
instrumentos de deuda:
•
Con la TIR se comparan rentabilidades,
•
Con la volatilidad se comparan riesgos
1. Introducción

## Página 5

Valoración. Marco Black
5
Enfoque
Como en cualquier enfoque de valoración:
1.
Se seleccionan los activos básicos pertinentes (normalmente, aquellos indispensables para la replicación del instrumento 
en cuestión);
2.
se selecciona un numerario conveniente;
3.
se postula que los (procesos de precios de los) activos básicos, expresados en el numerario seleccionado, son 
martingalas, garantizando así que el modelo es (internamente) libre de arbitraje.
4.
Cada evolución partirá de los valores actuales cotizados de los activos básicos (para garantizar que no haya arbitrajes 
externos con los activos básicos del modelo).
Pero además, y esto es lo especial del marco Black
5.
se postula que los activos expresados en el numerario siguen una evolución lognormal browniana sin deriva (que 
garantiza la condición de martingala), y con volatilidad constante.
1. Introducción

## Página 6

Valoración. Marco Black
6
Enfoque
Es decir, para cada activo se postulan evoluciones de la forma
𝑑𝑉𝑡= 𝜎𝑉𝑡𝑑𝑊𝑡 donde 
𝑉𝑡=
𝑎𝑐𝑡𝑖𝑣𝑜
𝑛𝑢𝑚𝑒𝑟𝑎𝑟𝑖𝑜𝑡
y se incorpora la estructura de correlación entre los brownianos de los distintos activos que sea precisa.
Como no tienen deriva, cada uno de los procesos 𝑉𝑡 será martingala.
En el caso (habitual) en que la volatilidad 𝝈 sea constante se tendrá, además, que, para cada 𝑡,
𝑉𝑡= 𝑉0 · 𝑒𝜎𝑡𝑍−𝜎2
2 𝑡
donde 𝑍 una normal estándar (distinta para cada 𝑡). Cada 𝑉𝑡 es, por tanto, una variable lognormal.
1. Introducción

## Página 7

Valoración. Marco Black
7
Fórmulas
En cada caso de aplicación del marco Black, la elección juiciosa (estandarizada) del numerario y la hipótesis de martingala 
lognormal nos conducirán a que las opciones vanilla,
• calls y puts (equity);
• caplets y floorlets, swaptions (tipos);
• opciones sobre FX;
admiten, dentro de este marco Black de modelización, fórmulas analíticas: fórmulas de Black-Scholes, todas con una misma 
estructura estandarizada
1. Introducción

## Página 8

Valoración. Marco Black
8
Volatilidad
La volatilidad 𝜎 de la evolución lognormal del subyacente en términos del numerario es el parámetro esencial en las 
fórmulas.
En los mercados se ha estandarizado la cotización de la volatilidad que hay que imputar en la fórmula de Black–Scholes para 
obtener el precio. Las cotizaciones (vía Black) de estos instrumentos vanilla son luego inputs para la valoración de 
instrumentos más complejos.
1. Introducción

## Página 9

Valoración. Marco Black
9
Observación. Cálculos de Black-Scholes
Repetidamente apelaremos al siguiente cálculo, que requeriremos en valoraciones de distintos instrumentos de tipo call, dando 
lugar en cada caso a una fórmula de tipo Black–Scholes. Supongamos que 𝑊 es una normal 𝑁(−𝜂2/2, 𝜂). Es decir,
𝑊 = −𝜂2
2 + 𝜂𝑍, con 𝑍 ∼ 𝑁(0, 1).
Obsérvese que la media de 𝑊 ha sido elegida para que Ε 𝑒𝑊= 1. Entonces:
Ε
𝐴𝑒𝑊−𝐾+ = 𝐴Φ 𝑑+ −𝐾Φ 𝑑− donde 𝑑± =
ln 𝐴
𝐾
𝜂
± 𝜂
2
Como 𝐴𝑒𝑊−𝐾+ −𝐾−𝐴𝑒𝑊+ = 𝐴𝑒𝑊−𝐾, y además Ε 𝐴𝑒𝑊−𝐾= 𝐴−𝐾, se deduce que 
Ε
𝐾−𝐴𝑒𝑊+ = Ε
𝐴𝑒𝑊−𝐾+ −𝐴−𝐾,
Donde, finalmente:
Ε
𝐾−𝐴𝑒𝑊+ = 𝐾Φ −𝑑−−𝐴Φ −𝑑+
1. Introducción

## Página 10

Valoración. Marco Black
10
Observación. Cálculos de Margrabe
Ocasionalmente apelaremos al siguiente cálculo:
si 𝑋 e 𝑌 son variables positivas;
si 𝑋/𝑌 e 𝑌 son lognormales;
y si ln(𝑋/𝑌) tiene desviación típica 𝜂,
entonces
Ε
𝑋−𝑌+ = Ε 𝑋Φ d+ −Ε 𝑌Φ d− donde d± =
ln Ε 𝑋
Ε 𝑌
𝜂
± 𝜂
2
El cálculo Black–Scholes es un caso particular.
Si 𝑋 e 𝑌 son lognormales cuyos logaritmos tienen desviaciones típicas 𝜎𝑋 y 𝜎𝑌 y correlación 𝜌, entonces 𝑋/𝑌
es lognormal y tiene desviación típica:
𝜎𝑋
2 + 𝜎𝑌
2 −2𝜌𝜎𝑋𝜎𝑌
Para obtener el resultado, basta cambiar de la probabilidad P dada a Q, 𝑑𝑄 =
𝑌
𝐸𝑌
𝑑𝑃 y usar el cálculo
Black–Scholes. Nótese que 𝑋/𝑌 sigue siendo lognormal (con la misma desviación típica) bajo Q.
1. Introducción

## Página 11

Valoración. Marco Black
11
Marco Black 
en equity
02.

## Página 12

Valoración. Marco Black
12
El modelo
Recordemos lo dicho anteriormente:
1.
Se seleccionan los activos básicos pertinentes (normalmente, aquellos indispensables para la replicación del instrumento en 
cuestión);
2.
se selecciona un numerario conveniente;
3.
se postula que los (procesos de precios de los) activos básicos, expresados en el numerario seleccionado, son martingalas, 
garantizando así que el modelo es (internamente) libre de arbitraje.
4.
Cada evolución partirá de los valores actuales cotizados de los activos básicos (para garantizar que no haya arbitrajes externos 
con los activos básicos del modelo).
Pero además, y esto es lo especial del marco Black
5.
se postula que los activos expresados en el numerario siguen una evolución lognormal browniana sin deriva (que garantiza 
la condición de martingala), y con volatilidad constante.
2. Marco Black en equity

## Página 13

Valoración. Marco Black
13
El modelo
Activos básicos
Tenemos dos activos básicos:
• Una acción o índice subyacente de referencia (por ahora sin dividendos), cuya cotización en tiempo 𝑡 denotaremos por 
𝑆𝑡
• Y la cuenta bancaria 𝛽𝑡, que usaremos como numerario. Suponemos que 𝛽𝑡 tiene una rentabilidad continua determinista 𝑟 
por unidad de tiempo; es decir, 𝛽𝑡= 𝑒𝑟𝑡
Numerario
Usaremos como numerario la cuenta bancaria 𝛽𝑡= 𝑒𝑟𝑡. Nótese que 𝛽0 = 1
2. Marco Black en equity

## Página 14

Valoración. Marco Black
14
El modelo
Probabilidad de valoración
Modelizamos imponiendo una probabilidad Q bajo la cual 𝑆𝑡/𝛽𝑡 es Q-martingala (por supuesto, 
𝛽𝑡
𝛽𝑡= 1 es también Q-
martingala)
Así garantizamos que no hay oportunidades de arbitraje invirtiendo autofinanciadamente en esos activos básicos.
Para obtener el valor 𝑌0 a mercado de un activo 𝑌 (replicable con 𝑆 y cuenta bancaria 𝛽) que paga 𝑌𝑇 en tiempo 𝑇, 
calcularemos
𝑌0
𝛽0
= Ε𝑄
𝑌𝑇
𝛽𝑇
Es decir
𝑌0 = 𝑒−𝑟𝑇Ε𝑄𝑌𝑇
Pues 𝛽0 = 1 y 𝛽𝑇= 𝑒𝑟𝑇. En palabras, el precio del activo (replicable) es el promedio (con Q) descontado de los flujos en 
tiempo 𝑇.
2. Marco Black en equity

## Página 15

Valoración. Marco Black
15
El modelo
Evolución lognormal Black
Se propone la evolución
𝑑
𝑆𝑡
𝛽𝑡
= 𝜎·
𝑆𝑡
𝛽𝑡
𝑑𝑊𝑡
que, como no tiene deriva, garantiza que 𝑆𝑡/𝛽𝑡 es martingala. El lema de Itô nos dice entonces que
∗
𝑆𝑇
𝛽𝑇
= 𝑆0
𝛽0
𝑒−𝜎2
2 𝑇𝑒𝜎𝑇𝑍
donde 𝑍 es una normal estándar, y también que
∗∗ 𝑑𝑆𝑡 =  𝑟𝑆𝑡 𝑑𝑡 +  𝜎𝑆𝑡 𝑑𝑊𝑡
De (∗) (simplemente despejando) o de ∗∗ (vía una nueva aplicación del lema de Itô) se obtiene la forma explícita de la 
variable 𝑆𝑇 en un vencimiento 𝑇:
𝑆𝑇= 𝑆0𝑒
𝑟−𝜎2
2
𝑇
𝑒𝜎𝑇𝑍
2. Marco Black en equity

## Página 16

Valoración. Marco Black
16
Observación 1
Para resolver (∗): hay que comprobar que
𝑑𝐴𝑡= 𝜎𝐴𝑡𝑑𝑊𝑡 → 𝐴𝑡= 𝐴0𝑒−𝑡𝜎2
2 𝑒𝜎𝑡𝑍
Tomamos 𝐵𝑡= ln 𝐴𝑡. Es decir, 𝐵𝑡= 𝑓𝑡, 𝐴𝑡, con 𝑓𝑡, 𝑥= ln 𝑥. Las derivadas de interés son
𝑓𝑡= 0
𝑓𝑥= 1
𝑥
𝑓𝑥𝑥= −1
𝑥2
Entonces
𝑑𝐵𝑡= 𝑓𝑡𝑡, 𝐴𝑡𝑑𝑡+ 𝑓𝑥𝑡, 𝐴𝑡𝑑𝐴𝑡+ 1
2 𝑓𝑥𝑥𝑡, 𝐴𝑡
𝑑𝐴𝑡2 = 1
𝐴𝑡
𝜎𝐴𝑡𝑑𝑊𝑡−1
2
1
𝐴𝑡
2 𝜎2𝐴𝑡
2𝑑𝑡= −𝜎2
2 𝑑𝑡+ 𝜎𝑑𝑊𝑡
La resolución, directa, de esta regla estocástica, da 
𝐵𝑡= 𝐵0 −𝜎2
2 𝑡+ 𝜎𝑡𝑍
y tras exponenciar, se obtiene el resultado buscado.
2. Marco Black en equity

## Página 17

Valoración. Marco Black
17
Observación 2
Para resolver (∗∗): Llamamos
𝐴𝑡= 𝑆𝑡
𝑒𝑟𝑡
Cuya evolución es 
𝑑𝐴𝑡= 𝜎𝐴𝑡𝑑𝑊𝑡
Tenemos que 𝑆𝑡= 𝑒𝑟𝑡𝐴𝑡= 𝑓(𝑡, 𝐴𝑡), con 𝑓𝑡, 𝑥= 𝑒𝑟𝑡𝑥. Las derivadas que nos interesan son:
𝑓𝑡= 𝑟𝑒𝑟𝑡𝑥
𝑓𝑥= 𝑒𝑡
𝑓𝑥𝑥= 0
𝑑𝑆𝑡= 𝑟𝑒𝑟𝑡𝐴𝑡𝑑𝑡+ 𝑒𝑟𝑡𝑑𝐴𝑡= 𝑟𝑒𝑟𝑡𝑆𝑡
𝑒𝑟𝑡𝑑𝑡+ 𝑒𝑟𝑡𝜎𝑆𝑡
𝑒𝑟𝑡𝑑𝑊𝑡= 𝑟𝑆𝑡𝑑𝑡+ 𝜎𝑆𝑡𝑑𝑊𝑡
2. Marco Black en equity

## Página 18

Valoración. Marco Black
18
El argumento de cartera replicante
1. Carteras de inversión
La composición de una cartera de inversión en tiempo 𝑡 vienen dada por 𝑎𝑡 unidades de activo 𝑆 y 𝑏𝑡 unidades de la cuenta 
bancaria 𝛽. Aquí, 𝑎𝑡 y 𝑏𝑡 son dos procesos.
El valor de la cartera en tiempo 𝑡 es el proceso
𝑉𝑡= 𝑎𝑡𝑆𝑡+ 𝑏𝑡𝛽𝑡
Recordemos que:
𝑑𝛽𝑡= 𝑟𝛽𝑡𝑑𝑡⟹𝛽𝑡= 𝑒𝑟𝑡
𝑑𝑆𝑡= 𝑟𝑆𝑡𝑑𝑡+ 𝜎𝑆𝑡 𝑑𝑊𝑡
2. Marco Black en equity

## Página 19

Valoración. Marco Black
19
El argumento de cartera replicante
2. Carteras autofinanciadas
Decimos que la cartera es autofinanciada si
𝑑𝑉𝑡= 𝑎𝑡𝑑𝑆𝑡+ 𝑏𝑡𝑑𝛽𝑡
Observación
Supongamos ℎ pequeño. La cartera es autofinanciada si
𝑎𝑡+ℎ𝑆𝑡+ℎ+ 𝑏𝑡+ℎ𝛽𝑡+ℎ≈𝑎𝑡𝑆𝑡+ℎ+ 𝑏𝑡𝛽𝑡+ℎ
Esto supone que
𝑉𝑡+ℎ−𝑉𝑡= 𝑎𝑡+ℎ𝑆𝑡+ℎ+ 𝑏𝑡+ℎ𝛽𝑡+ℎ−𝑎𝑡𝑆𝑡+ 𝑏𝑡𝛽𝑡=
= 𝑎𝑡𝑆𝑡+ℎ−𝑆𝑡+ 𝑏𝑡𝛽𝑡+ℎ−𝛽𝑡
+ 𝑎𝑡+ℎ𝑆𝑡+ℎ+ 𝑏𝑡+ℎ𝛽𝑡+ℎ−𝑎𝑡𝑆𝑡+ℎ+ 𝑏𝑡𝛽𝑡+ℎ
2. Marco Black en equity
𝑑𝑉𝑡
≈0

## Página 20

Valoración. Marco Black
20
El argumento de cartera replicante
3. Carteras autofinanciadas y martingalas
El proceso de valor de una cartera autofinanciada, en términos del numerario,
𝑍𝑡= 𝑉𝑡
𝛽𝑡
= 𝑒−𝑟𝑡𝑉𝑡
Es martingala. De hecho,
𝑑𝑍𝑡= 𝑎𝑡
𝑆𝑡
𝛽𝑡
𝜎𝑑𝑊𝑡
Ejercicio: demostrar esta última igualdad.
2. Marco Black en equity

## Página 21

Valoración. Marco Black
21
El argumento de cartera replicante
4. No hay arbitraje
Una oportunidad de arbitraje es una cartera de inversión autofinanciada tal que
𝑉0 = 0,
 
𝑉𝑇≥0,
 𝑦 P VT > 0 > 0.
Como el proceso 
𝑉𝑡
𝛽𝑡 es martingala para todo 𝑡, tenemos que
EQ
𝑉𝑇
𝛽𝑇
= 𝑉0
1
2. Marco Black en equity
> 0
= 0

## Página 22

Valoración. Marco Black
22
El argumento de cartera replicante
5. Cartera replicante
Tenemos un derivado 𝐶, de vencimiento 𝑇, cuyo precio en tiempo 𝑡viene dado por 
𝐶𝑡= 𝑓𝑡, 𝑆𝑡,
Donde 𝑓𝑡, 𝑥 es una cierta función de dos variables. Queremos hallar una cartera autofinanciada, de valor,
𝑉𝑡= 𝑎𝑡𝑆𝑡+ 𝑏𝑡𝛽𝑡
Tal que 𝑉𝑇= 𝐶𝑇 (y, de hecho, tal que 𝑉𝑡= 𝐶𝑡 para todo 𝑡≤𝑇)
2. Marco Black en equity

## Página 23

Valoración. Marco Black
23
El argumento de cartera replicante
5. Cartera replicante
Primero, por ser cartera autofinanciada (3),
∗ 𝑑
𝑉𝑡
𝛽𝑡
= 𝑎𝑡
𝑆𝑡
𝛽𝑡
𝜎𝑑𝑊𝑡
Por otro lado, usando el lema de Itô,
∗∗ 𝑑𝑉𝑡
𝛽𝑡
= 1
𝛽𝑡
−𝑟𝑓𝑡, 𝑆𝑡+ 𝑓𝑡+ 𝑟𝑓𝑥𝑡, 𝑆𝑡𝑆𝑡+ 1
2 𝑓𝑥𝑥𝑡, 𝑆𝑡𝜎2𝑆𝑡
2 𝑑𝑡+ 𝜎𝑓𝑥𝑡, 𝑆𝑡𝑆𝑡𝑑𝑊𝑡
Por tanto:
𝑎𝑡= 𝑓𝑥𝑡, 𝑆𝑡,
 
𝑏𝑡= 1
𝛽𝑡
𝑓𝑡, 𝑆𝑡−𝑓𝑥𝑡, 𝑆𝑡𝑆𝑡
2. Marco Black en equity

## Página 24

Valoración. Marco Black
24
Valoración de opciones
1. Valoración de una call/put europea de strike 𝑲 (sin dividendos)
El pago de una call 𝑋 sobre 𝑆 a vencimiento 𝑇 es 𝑋𝑇= 𝑆𝑇−𝐾+. Su precio hoy viene dado por 
valorhoycall = 𝑒−𝑟𝑇EQ
𝑆𝑇−𝐾+
Como
𝑆𝑇= 𝑆0 · 𝑒
𝑟−𝜎2
2
𝑇
𝑒𝜎𝑇𝑁0,1
Podemos resolver el cálculo como en la página 9, con
𝐴= 𝑆0𝑒𝑟𝑇,
 𝜂= 𝜎𝑇,
 𝑦 𝑊= 𝜎𝑇𝑍−𝜎2
2
𝑇
Llevándonos a la fórmula
valorhoycall = 𝑆0Φ 𝑑+ −𝐾𝑒−𝑟𝑇Φ 𝑑−,
 
𝑑± =
ln
𝑆0
𝐾𝑒−𝑟𝑇
𝜎𝑇
± 1
2 𝜎𝑇
2. Marco Black en equity

## Página 25

Valoración. Marco Black
25
Valoración de opciones
1. Valoración de una call/put europea de strike 𝑲 (sin dividendos)
La correspondiente fórmula para la put es:
valorhoyput = 𝐾𝑒−𝑟𝑇Φ −𝑑−−𝑆0Φ −𝑑+ ,
 
𝑑± =
ln
𝑆0
𝐾𝑒−𝑟𝑇
𝜎𝑇
± 1
2 𝜎𝑇
Ejercicio: Montar la calculadora en Excel correspondiente. Obtener las gráficas de la prima en función de strike, volatilidad, 
vencimiento y tipo
2. Marco Black en equity

## Página 26

Valoración. Marco Black
26
Valoración de opciones
Observación. Prima en función de moneyness y de volatilidad acumulada
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑐𝑎𝑙𝑙
𝑆0
= Φ 𝑑+ −𝐾𝑒−𝑟𝑇
𝑆0
Φ 𝑑−
Si escribimos la fórmula en función de las variables 𝑚 (moneyness) y de 𝜎𝑇 (volatilidad acumulada):
𝑚= ln 𝑆0𝑒𝑟𝑇
𝐾
,
 𝜎𝑇
Obtenemos:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑐𝑎𝑙𝑙
𝑆0
= Φ
𝑚
𝜎𝑇
+ 𝜎𝑇
2
−𝑒−𝑚Φ
𝑚
𝜎𝑇
−𝜎𝑇
2
2. Marco Black en equity

## Página 27

Valoración. Marco Black
27
Valoración de opciones
2. Valoración de una call/put europea de strike 𝑲 (con dividendos)
Modelamos suponiendo dividendos “continuos” :
1.
Recibimos una cantidad de dividendos a una tasa 𝑞 por unidad de tiempo sobre la cotización;
2.
Los dividendos se reinvierten continuamente en el subyacente.
Entonces, el valor de invertir (autofinanciadamente) en una unidad de 𝑆 vale en tiempo 𝑡:
𝑆𝑡𝑒𝑞𝑡
Para que no haya arbitraje, ha de darse que 
𝑌𝑡= 𝑆𝑡𝑒𝑞𝑡
𝛽𝑡
= 𝑆𝑡𝑒𝑞𝑡
𝑒𝑟𝑡
Sea martingala.
2. Marco Black en equity

## Página 28

Valoración. Marco Black
28
Valoración de opciones
2. Valoración de una call/put europea de strike 𝑲 (con dividendos)
Se impone la evolución
𝑑𝑌𝑡= 𝜎𝑌𝑡𝑑𝑊𝑡
Por tanto, por Itô:
𝑑𝑆𝑡= 𝑟−𝑞𝑆𝑡𝑑𝑡+ 𝜎𝑆𝑡𝑑𝑊𝑡
Y por tanto, en 𝑡= 𝑇
𝑆𝑇= 𝑆0𝑒(𝑟−𝑞−𝜎2
2 )𝑇𝑒𝜎𝑇𝑁0,1
Y, usando de nuevo el cálculo de la página 9:
valorhoycall = 𝑆0𝑒−𝑞𝑇Φ 𝑑+ −𝐾𝑒−𝑟𝑇Φ 𝑑−,
 
𝑑± =
ln 𝑆0𝑒−𝑞𝑇
𝐾𝑒−𝑟𝑇
𝜎𝑇
± 1
2 𝜎𝑇
2. Marco Black en equity

## Página 29

Valoración. Marco Black
29
Valoración de opciones
3. Valoración de una opción (europea) general
El valor de un derivado que paga 𝑋𝑇= 𝑓𝑆𝑇, para una cierta función 𝑓, viene dado por:
valorhoyderivado = 𝑒−𝑟𝑇EQ 𝑓𝑆𝑇
Para calcular esa esperanza, caben varias posibilidades:
• En ocasiones seremos capaces de calcular analíticamente la integral correspondiente, como en calls/puts, calls/puts 
digitales, etc.
• En otras, el flujo 𝑓 se puede descomponer como combinación de calls, puts, etc. (desestructuración), y aplicar las habituales 
fórmulas de Black–Scholes (véase el perfil tipo butterfly que veremos a continuación).
• En todo caso, como conocemos la distribución de 𝑆𝑇 , podemos calcular la esperanza por simulación.
• O, directamente, calcular numéricamente (discretizando) la integral
2. Marco Black en equity

## Página 30

Valoración. Marco Black
30
Valoración de opciones
3. Valoración de una opción (europea) general
Normalmente, se toma la cotización de la call vanilla para extraer con qué volatilidad se está cotizando (la volatilidad 
implícita), para luego usar esa información de volatilidad en la valoración de un instrumento como este derivado con perfil de 
flujos 𝑓𝑆𝑇.
Ilustración
• Calcúlese numéricamente:
• Discretizando la integral
• Y por simulación MonteCarlo
El precio de la opción cuyo perfil de pagos aparece en la figura (la altura del “triángulo” es 10). Calcúlese también su precio 
por desestructuración (escribiéndolo, por ejemplo, como combinación de calls compradas y vendidas).
2. Marco Black en equity

## Página 31

Valoración. Marco Black
31
Valoración de opciones
4. Dividendo previsto 𝑫 en tiempo 𝑻
Queremos valorar una opción europea que vence en un tiempo 𝑇′ sobre un subyacente que pagará un cierto dividendo 𝐷 en 
un tiempo 𝑇 anterior. El perfil de pagos de la opción es 𝑓.
• Entre 𝑇 y 𝑇′, es decir, después del pago del dividendo, la cotización sigue la evolución
𝑑𝑆𝑡= 𝑟𝑆𝑡𝑑𝑡+ 𝜎𝑆𝑡𝑑𝑊𝑡
Si condicionamos sobre el valor 𝑆𝑇, en tiempo 𝑇′ tendremos:
𝑆𝑇′ = 𝑆𝑇𝑒
𝑟−𝜎2
2
𝑇′−𝑇
𝑒𝜎𝑇′−𝑇𝑁0,1
El valor en tiempo 𝑇 condicionado sobre 𝑆𝑇 de un derivado que paga 𝑓𝑆𝑇′  es
valorT condicionado a 𝑆𝑇= 𝑒−𝑟𝑇′−𝑇න
−∞
+∞
𝑓𝑆𝑇𝑒
𝑟−𝜎2
2
𝑇′−𝑇
𝑒𝜎𝑇′−𝑇
𝑒−𝑢2
2
2𝜋
𝑑𝑢
2. Marco Black en equity

## Página 32

Valoración. Marco Black
32
Valoración de opciones
4. Dividendo previsto 𝑫 en tiempo 𝑻
Desde tiempo 0 hasta tiempo 𝑇, pero justo antes del pago del dividendo, la cotización evoluciona también como
𝑑𝑆𝑡= 𝑟𝑆𝑡𝑑𝑡+ 𝜎𝑆𝑡𝑑𝑊𝑡
Denotamos por ෪
𝑆𝑇 la cotización en tiempo 𝑇 justo antes de pagar el dividendo y por 𝑆𝑇 la cotización justo después de ese 
pago. Tenemos que
෪
𝑆𝑇= 𝑆0𝑒
𝑟−𝜎2
2
𝑇
𝑒𝜎𝑇𝑁0,1
Y por tanto:
𝑆𝑇= ෪
𝑆𝑇−𝐷
2. Marco Black en equity

## Página 33

Valoración. Marco Black
33
Valoración de opciones
4. Dividendo previsto 𝑫 en tiempo 𝑻
Así que
Valor = 𝑒−𝑟𝑇𝐸𝑣𝑎𝑙𝑜𝑟𝑇𝑐𝑜𝑛𝑑𝑖𝑐𝑖𝑜𝑛𝑎𝑑𝑜 𝑎 𝑆𝑇
=
𝑒−𝑟𝑇′ ඵ𝑓
𝑆0𝑒
𝜎𝑇𝑣+ 𝑟−𝜎2
2
𝑇
−𝐷𝑒
𝜎𝑇′−𝑇𝑢+ 𝑟−𝜎2
2
𝑇′−𝑇
𝑒−𝑢2+𝑣2
2𝜋
𝑑𝑢𝑑𝑣
Si hay varias fechas de pago de dividendos, hay que iterar el argumento anterior (dando lugar a una integral en más 
dimensiones).
2. Marco Black en equity

## Página 34

Valoración. Marco Black
34
Valoración de opciones
5. Varios subyacentes
Si hay dos subyacentes (el caso de más de dos subyacentes es análogo), digamos 𝑋 e 𝑌, se postulan las evoluciones
𝑑𝑋𝑡
𝛽𝑡
= 𝜎𝑋
𝑋𝑡
𝛽𝑡
𝑑𝑊𝑡
𝑋
𝑑
𝑌𝑡
𝛽𝑡
= 𝜎𝑌
𝑌𝑡
𝛽𝑡
𝑑𝑊𝑡
𝑌
Con correlación instantánea 𝜌 entre los brownianos. Los activos básicos son las dos acciones y la cuenta bancaria. Esto da que, 
en tiempo 𝑇,
𝑋𝑇= 𝑋0𝑒𝑟−𝜎𝑋
2
2
𝑇𝑒𝜎𝑋𝑇𝑁𝑋
𝑌𝑇= 𝑌0𝑒𝑟−𝜎𝑌
2
2
𝑇𝑒𝜎𝑌𝑇𝑁𝑌
Con 𝑍𝑋 y 𝑍𝑌 son normales estándar con correlación 𝜌
2. Marco Black en equity

## Página 35

Valoración. Marco Black
35
Valoración de opciones
5. Varios subyacentes
Si un instrumento paga una cierta función de la cotización a vencimiento 𝑇 de ambas acciones, 𝑓𝑋𝑇, 𝑌𝑇, la prima será
𝑒−𝑟𝑇E 𝑓𝑋𝑇, 𝑌𝑇
Que se puede calcular:
• Analíticamente, para obtener una fórmula cerrada (muy inusual);
• Discretizando la integral;
• O por simulación Montecarlo.
2. Marco Black en equity

## Página 36

Valoración. Marco Black
36
Otros numerarios
1. Bono cupón cero como numerario: valoración forward neutra
Queremos valorar opciones europeas, de vencimiento 𝑇, sobre un subyacente 𝑆. Podemos usar como numerario el bono 𝐵𝑇 
cupón cero de principal 1 que vence en ese tiempo futuro 𝑇, cuyo precio en tiempo 𝑡 denotamos por 𝑃𝑡, 𝑇.
Activos básicos
Tenemos dos activos básicos, el activo subyacente y el bono 𝐵𝑇. 
Ahora los precios, tanto de 𝑆 como de 𝐵𝑇, son aleatorios.
2. Marco Black en equity

## Página 37

Valoración. Marco Black
37
Otros numerarios
1. Bono cupón cero como numerario: valoración forward neutra
Probabilidad de valoración y numerario
Usamos como numerario al bono 𝐵𝑇 (que, obsérvese, es sólo válido hasta tiempo 𝑇). Se impone que:
𝑆𝑡
𝑃𝑡, 𝑇
Sea martingala hasta tiempo 𝑇.
La probabilidad de valoración asociada a ese numerario, que denotamos por QF, se conoce como probabilidad forward neutra. 
Para valorar un derivado 𝑋 de 𝑆 que paga 𝑋𝑇 en tiempo 𝑇,
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑋
𝑃0, 𝑇
= EQF
𝑋𝑇
𝑃𝑇, 𝑇
= EQF 𝑋𝑇
Es decir,
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑋= 𝑃0, 𝑇EQF 𝑋𝑇
2. Marco Black en equity

## Página 38

Valoración. Marco Black
38
Otros numerarios
1. Bono cupón cero como numerario: valoración forward neutra
Evolución lognormal
Se impone que 𝑆𝑡/𝑃(𝑡, 𝑇) sigue una evolución lognormal
𝑑
𝑆𝑡
𝑃𝑡, 𝑇
=
𝑆𝑡
𝑃𝑡, 𝑇
𝜎𝑑𝑊𝑡
Eso nos dice que, en cualquier tiempo 𝑡, el cociente 𝑆𝑡/𝑃(𝑡, 𝑇) es una variable lognormal. Si queremos valorar un derivado 
europeo que vence en un tiempo 𝑡, el flujo de ese derivado dependerá de 𝑆𝑡, pero nosotros tenemos información sobre la 
distribución de valores del cociente 𝑆𝑡/𝑃(𝑡, 𝑇).
Sin embargo, para tiempo 𝑇, tenemos que 𝑃(𝑇, 𝑇) ≡1. De manera que
𝑆𝑇=
𝑆𝑇
𝑃𝑇, 𝑇=
𝑆0
𝑃0, 𝑇𝑒−𝜎2
2 𝑇𝑒𝜎𝑇𝑁0,1
2. Marco Black en equity

## Página 39

Valoración. Marco Black
39
Otros numerarios
1. Bono cupón cero como numerario: valoración forward neutra
Evolución lognormal
Para la call obtenemos la fórmula de Black-Scholes, aunque escrita en la forma
valorhoycall = 𝑃0, 𝑇
𝑆0
𝑃0, 𝑇Φ 𝑑+ −𝐾Φ 𝑑−
Donde
𝑑± =
ln
𝑆0
𝑃0, 𝑇
𝐾
𝜎𝑇
± 1
2 𝜎𝑇
Si el tipo es constante, entonces 𝑃(0, 𝑇) es simplemente 𝑒−𝑟𝑇 , y recuperamos la habitual fórmula de Black–Scholes. Pero aquí 
podemos admitir tipos estocásticos.
2. Marco Black en equity

## Página 40

Valoración. Marco Black
40
Otros numerarios
2. El propio subyacente como numerario
De nuevo, el activo de referencia es 𝑆𝑡, además de la cuenta bancaria 𝛽𝑡 = 𝑒𝑟𝑡. Usamos ahora a 𝑆𝑡 como numerario; sea QS la 
probabilidad de valoración asociada, de manera que
𝑆𝑡
𝑆𝑡
 
𝑦 
𝛽𝑡
𝑆𝑡
son martingalas bajo QS. La valoración de un derivado 𝑋 que paga 𝑋𝑇 en tiempo 𝑇 es entonces
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑋
𝑆0
= EQ𝑆
𝑋𝑇
𝑆𝑇
Se propone una evolución martingala lognormal para el cociente (𝛽𝑡/𝑆𝑡):
𝑑𝛽𝑡
𝑆𝑡
 =
𝛽𝑡
𝑆𝑡
𝜎 𝑑𝑊𝑡 
2. Marco Black en equity

## Página 41

Valoración. Marco Black
41
Otros numerarios
2. El propio subyacente como numerario
Esto implica, por Itô, que 𝑆𝑡 tiene la evolución
𝑑𝑆𝑡= 𝑟+ 𝜎2 𝑆𝑡𝑑𝑡+ 𝜎𝑆𝑡𝑑𝑊𝑡
Lo que supone que, 
𝑆𝑡= 𝑆0𝑒
𝑟+𝜎2
2
𝑡
𝑒𝜎𝑡𝑁0,1
Ejercicio: Demostrar la última igualdad
2. Marco Black en equity

## Página 42

Valoración. Marco Black
42
Otros numerarios
2. El propio subyacente como numerario
Ejemplo 1. 𝑿𝑻= 𝑺𝑻 si 𝑺𝑻> 𝑲
Bajo QS, valoramos como sigue:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑋
𝑆0
= EQ𝑆
𝑋𝑇
𝑆𝑇
= EQ𝑆1 𝑆𝑇>𝐾
= QS 𝑆𝑇> 𝐾
Bajo 𝑄𝑆, tenemos que 𝑆𝑇= 𝑆0𝑒
𝑟+𝜎2
2
𝑇𝑒𝜎𝑇𝑁0,1. Esto nos da
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑋= 𝑆0 න
−∞
+∞
1
𝑆0𝑒𝑟+𝜎2
2
𝑇𝑒𝜎𝑇𝑥
𝑒−𝑥2
2
2𝜋𝑑𝑥
De donde deducimos que
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑋= 𝑆0Φ
ln 𝑠0
𝐾
+
𝑟+ 𝜎2
2
𝑇
𝜎𝑇
2. Marco Black en equity

## Página 43

Valoración. Marco Black
43
Otros numerarios
2. El propio subyacente como numerario
Ejemplo 2. Opción sobre el máximo de dos activos
Tenemos dos activos 𝑋 e 𝑌. Denotaremos por 𝑋𝑡 e 𝑌𝑡 a los valores potenciales en tiempo 𝑡. Además tenemos la cuenta 
bancaria, con tipo de interés 𝛽𝑡= 𝑒𝑟𝑇.
Interesa valorar el derivado 𝑍 que paga el máximo entre 𝑿𝑻 e 𝒀𝑻 en tiempo 𝑻
𝑍𝑇= max 𝑋𝑇, 𝑌𝑇
Veamos ahora cómo, usando como numerario uno de los activos, por ejemplo, 𝑌𝑡, podemos llegar a una fórmula de valoración 
cerrada. Modelamos postulando la existencia de una probabilidad 𝑄𝑌 bajo la cual
𝑌𝑡
𝑌𝑡
,
𝑋𝑡
𝑌𝑡
,
 𝑦 
𝑒𝑟𝑡
𝑌𝑡
 
son martingalas
2. Marco Black en equity

## Página 44

Valoración. Marco Black
44
Otros numerarios
2. El propio subyacente como numerario
Ejemplo 2. Opción sobre el máximo de dos activos
Se proponen ahora evoluciones lognormales correladas a 𝑋𝑡 y 𝑌𝑡, y se ajustan sus derivas para que 𝑋𝑡/𝑌𝑡 y 𝛽𝑡/𝑌𝑡 resulten 
martingalas.
Al final, resulta que 𝑋𝑇/𝑌𝑇 es una lognormal de la siguiente forma:
𝑋𝑇
𝑌𝑇
=
𝑋0
𝑌0
𝑒−ෝ𝜎2
2 𝑇𝑒ෝ𝜎𝑇𝑁0,1,
 
ො𝜎2 = 𝜎𝑋
2 + 𝜎𝑌
2 −2𝜌𝜎𝑋𝜎𝑌
Reescribimos ahora el flujo del derivado como sigue:
𝑍𝑇= max 𝑋𝑇, 𝑌𝑇= 𝑌𝑇+ 𝑋𝑇−𝑌𝑇+
2. Marco Black en equity

## Página 45

Valoración. Marco Black
45
Otros numerarios
2. El propio subyacente como numerario
Ejemplo 2. Opción sobre el máximo de dos activos
La fórmula de valoración sería ahora
valorhoy 𝑍= 𝑌0EQY
𝑌𝑇+ 𝑋𝑇−𝑌𝑇+
𝑌𝑇
= 𝑌0EQY
1 +
𝑋𝑇
𝑌𝑇
−1
+
= 𝑌0 + 𝑌0EQY
𝑋𝑇
𝑌𝑇
−1
+
Aplicando Black/Margrabe
valorhoy 𝑍= 𝑌0 + 𝑋0 · Φ 𝑑+ −𝑌0Φ 𝑑−= 𝑋0Φ 𝑑+ + 𝑌0Φ(𝑑−)
Con
𝑑± =
ln 𝑋0
𝑌0
𝜎𝑇
± 1
2 𝜎𝑇,
 𝜎= 𝜎𝑋
2 + 𝜎𝑌
2 −2𝜌𝜎𝑥𝜎𝑌
2. Marco Black en equity

## Página 46

Gracias

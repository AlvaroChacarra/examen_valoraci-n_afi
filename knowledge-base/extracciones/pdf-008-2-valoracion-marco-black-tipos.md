# PDF-008: 2.Valoración. Marco Black Tipos.pdf

Original: [archivo raw](../../raw/marco-black/2-valoracion-marco-black-tipos/2-valoracion-marco-black-tipos.pdf). SHA-256: `db75579a412c6f87e759df3cf829aaf5be4c2d7c2a0ade8ce3f908c4a4ccf2f1`.

Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.

## Página 1

Modelización Black.
Modelos estándar para tipos de 
interés
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
Marco Black en 
tipos de interés.
03.

## Página 4

Valoración. Marco Black
4
Marco Black en 
tipos de interés.
Tipos forward
3.1.

## Página 5

Valoración. Marco Black
5
Modelo de Black para tipos forward
Nos interesa construir un modelo sin arbitraje para valorar instrumentos que, en tiempo 𝑇, pagan flujos en función del tipo 
simple 𝑅(𝑇, 𝑇′) que se fija en tiempo 𝑇 (con 𝑇< 𝑇′) y que vence en tiempo 𝑇′. Habitualmente escribiremos Δ𝑇 =  𝑇′ − 𝑇.
Por ejemplo, instrumentos como
• FRA con strike 𝐾 y nominal 𝑁𝑜𝑚, que paga 𝑁𝑜𝑚· Δ𝑇 · (𝑅(𝑇, 𝑇′) −𝐾) en tiempo 𝑇′;
• caplet/floorlet con strike 𝐾, cuyos flujos, en tiempo 𝑇′, son 𝑁𝑜𝑚· Δ𝑇· 𝑅𝑇, 𝑇′ −𝐾+ y 𝑁𝑜𝑚·  Δ𝑇 ·
𝐾 − 𝑅𝑇, 𝑇′
+, 
respectivamente.
• Además de carteras de estos últimos instrumentos (caps, floors).
Veremos también cómo valorar, dentro del modelo, versiones de los anteriores instrumentos que llamaremos in-arrears, que 
pagan los flujos en tiempo 𝑇.
3.1. Marco Black en tipos de interés. Tipos forward

## Página 6

Valoración. Marco Black
6
Modelo de Black para tipos forward
Activos básicos
Los bonos cupón cero, 𝐵𝑇 y 𝐵𝑇′, que vencen en tiempos 𝑇 y 𝑇′, respectivamente.
Denotamos sus precios en tiempo 𝑡 como 𝑃(𝑡, 𝑇) y 𝑃𝑡, 𝑇′  respectivamente.
Numerario
Vamos a tomar como numerario el precio 𝑃𝑡, 𝑇′  del bono 𝐵𝑇′(el de más largo plazo)
Probabilidad de valoración
Postulamos que, bajo una probabilidad 𝑄𝑇′, los procesos siguientes son martingalas
𝑃𝑡, 𝑇
𝑃𝑡, 𝑇′ ,
𝑃𝑡, 𝑇′
𝑃𝑡, 𝑇′ ≡1
3.1. Marco Black en tipos de interés. Tipos forward

## Página 7

Valoración. Marco Black
7
Modelo de Black para tipos forward
Probabilidad de valoración. Cambio de notación.
Obsérvese que
Así que 
𝑃𝑡, 𝑇
𝑃𝑡, 𝑇′ = 1 + Δ𝑇· 𝐹𝑡, 𝑇, 𝑇′
de manera que exigir que 𝑃(𝑡, 𝑇)/𝑃(𝑡, 𝑇’) sea martingala es lo mismo que exigir que lo sea el tipo forward simple 𝐹(𝑡, 𝑇, 𝑇’).
3.1. Marco Black en tipos de interés. Tipos forward

## Página 8

Valoración. Marco Black
8
Modelo de Black para tipos forward
Probabilidad de valoración. Cambio de notación.
Los tiempos 𝑇 y 𝑇′ están fijos. A partir de ahora simplificamos la notación escribiendo
𝐹𝑡= 𝐹𝑡, 𝑇, 𝑇′ ,
 𝑡≤𝑇
A la vista de que:
• 𝑃(𝑡, 𝑇)/𝑃(𝑡, 𝑇′) sea martingala es equivalente a que el tipo forward 𝐹𝑡 lo sea;
• Y de que 𝐹𝑇= 𝑅(𝑇, 𝑇′) (a vencimiento 𝑇, el tipo forward se convierte en spot), de manera que los flujos de los instrumentos 
se podrán escribir en términos del tipo forward 𝐹𝑇
resulta razonable imponer una dinámica directamente al tipo forward 𝐹𝑡
3.1. Marco Black en tipos de interés. Tipos forward

## Página 9

Valoración. Marco Black
9
Modelo de Black para tipos forward
Lognormalidad Black.
Se impone que 𝐹𝑡𝑡≤𝑇 siga una evolución lognormal y que sea martingala:
𝑑𝐹𝑡= 𝐹𝑡𝜎𝑑𝑊𝑡
Esto supone, con la habitual aplicación del lema de Itô, que ln 𝐹𝑡 es una normal de media −
𝜎2
2 𝑡 y desviación típica 𝜎𝑡. Y de 
ahí, que
𝐹𝑡= 𝐹0𝑒−𝜎2
2 𝑡𝑒𝜎𝑡𝑁0,1
3.1. Marco Black en tipos de interés. Tipos forward

## Página 10

Valoración. Marco Black
10
Modelo de Black para tipos forward
Observación
En Black se impone que 𝐹𝑡𝑡 sea martingala. Esto es equivalente a exigir que el proceso 
𝑃𝑡,𝑇
𝑃𝑡,𝑇′
𝑡 lo sea.
Llamemos 𝜎𝑡𝑖𝑝𝑜 a la volatilidad de 𝐹𝑡𝑡. Entonces, la evolución Black de la martingala es, por Itô:
𝑑
𝑃𝑡, 𝑇
𝑃𝑡, 𝑇′
=
𝑃𝑡, 𝑇
𝑃𝑡, 𝑇′
·
𝜎𝑡𝑖𝑝𝑜
Δ𝑇𝐹𝑡
1 + Δ𝑇𝐹𝑡
𝑑𝑊𝑡
Es decir, la volatilidad del proceso “cociente de precios de los bonos” es estocástica
𝜎𝑏𝑜𝑛𝑜𝑠= 𝜎𝑡𝑖𝑝𝑜
Δ𝑇𝐹𝑡
1 + Δ𝑇𝐹𝑡
3.1. Marco Black en tipos de interés. Tipos forward

## Página 11

Valoración. Marco Black
11
Valoración de opciones
1. Valoración de un caplet de strike 𝑲
En el caplet, se fija el tipo simple 𝑅(𝑇, 𝑇′) en tiempo 𝑇 y se para en tiempo 𝑇′, la cantidad
𝑁𝑜𝑚· 𝑅𝑇, 𝑇′ −𝐾+ · Δ𝑇
Esto es, en tiempo 𝑇′, el flujo del caplet es
𝑁𝑜𝑚· 𝐹𝑇−𝐾+ · Δ𝑇
Por tanto:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑐𝑎𝑝𝑙𝑒𝑡
𝑃0, 𝑇′
= 𝑁𝑜𝑚· 𝐸𝑄𝑇′
Δ𝑇𝐹𝑇−𝐾+
𝑃𝑇, 𝑇′
= 𝑁𝑜𝑚· Δ𝑇· 𝐸𝑄𝑇′
𝐹𝑇−𝐾+
Ya que 𝑃𝑇′, 𝑇′ = 1
3.1. Marco Black en tipos de interés. Tipos forward

## Página 12

Valoración. Marco Black
12
Valoración de opciones
1. Valoración de un caplet de strike 𝑲
Aplicando el cálculo de Black-Scholes, da
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑐𝑎𝑝𝑙𝑒𝑡= 𝑁𝑜𝑚·  Δ𝑇 ·  𝑃0, 𝑇′  · 
𝐹0Φ 𝑑+ −𝐾Φ 𝑑−
Con
𝑑± =
ln 𝐹0
𝐾
𝜎𝑇
± 1
2 𝜎𝑇
Obsérvese que:
• Se descuenta desde 𝑇′
• Se acumula volatilidad hasta 𝑇
3.1. Marco Black en tipos de interés. Tipos forward

## Página 13

Valoración. Marco Black
13
Valoración de opciones
2. Valoración de un FRA
El FRA se replica estáticamente, así que, en cualquier modelo, su precio debe coincidir con el coste de su replicación.
Pongamos que queremos valorar el FRA (recibe variable) de nominal 𝑁𝑜𝑚, con strike 𝐾, para el periodo (𝑇, 𝑇′). El flujo del 
FRA en tiempo 𝑇′ es 𝑁𝑜𝑚· Δ𝑇· (𝐹𝑇−𝐾), por lo que
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝐹𝑅𝐴= 𝑁𝑜𝑚· 𝑃0, 𝑇′ · 𝐸𝑄𝑇′
Δ𝑇𝐹𝑇−𝐾
𝑃𝑇′, 𝑇′
= 𝑁𝑜𝑚· 𝑃0, 𝑇′ · Δ𝑇· 𝐸𝑄𝑇′
𝐹𝑇−𝐾
Como 𝐹𝑡 es martingala
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝐹𝑅𝐴= 𝑁𝑜𝑚· 𝑃0, 𝑇′ · Δ𝑇· 𝐹0 −𝐾
Como ya sabíamos.
3.1. Marco Black en tipos de interés. Tipos forward

## Página 14

Valoración. Marco Black
14
Valoración de opciones
3. Valoración de un FRA in arrears
Los siguientes esquemas comparan los contratos usuales e in-arreas
En el FRA in-arrears, el flujo en tiempo 𝑇 para la parte que recibe variable es:
𝑁𝑜𝑚· 𝐹𝑇−𝐾· Δ𝑇
3.1. Marco Black en tipos de interés. Tipos forward

## Página 15

Valoración. Marco Black
15
Valoración de opciones
3. Valoración de un FRA in arrears
Para calcular la prima, partimos de la fórmula habitual:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝐹𝑅𝐴𝑖𝑛−𝑎𝑟𝑟𝑒𝑎𝑟𝑠= 𝑁𝑜𝑚· 𝑃0, 𝑇′ · 𝐸𝑄𝑇′
Δ𝑇𝐹𝑇−𝐾
𝑃𝑇, 𝑇′
que se puede reescribir como
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝐹𝑅𝐴𝑖𝑛−𝑎𝑟𝑟𝑒𝑎𝑟𝑠= 𝑁𝑜𝑚· 𝑃0, 𝑇′ · Δ𝑇· 𝐸𝑄𝑇′
𝐹𝑇−𝐾· 1 + Δ𝑇· 𝐹𝑇
Nótese que el factor de descuento 𝑃(0, 𝑇′) que aparece no es el “natural”.
En esta esperanza aparece 𝐹𝑇, pero también 𝐹𝑇
2. 
Pero ambas variables aleatorias son lognormales, lo que nos permitirá hacer los cálculos explícitos. La media de la 𝐹𝑇
2 resulta 
ser 𝐹0
2𝑒𝜎2𝑇
3.1. Marco Black en tipos de interés. Tipos forward

## Página 16

Valoración. Marco Black
16
Valoración de opciones
3. Valoración de un FRA in arrears
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝐹𝑅𝐴𝑖𝑛−𝑎𝑟𝑟𝑒𝑎𝑟𝑠= 𝑁𝑜𝑚· 𝑃0, 𝑇′ · Δ𝑇· 𝐸𝑄𝑇′
𝐹𝑇−𝐾· 1 + Δ𝑇· 𝐹𝑇
Por tanto:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝐹𝑅𝐴𝑖𝑛−𝑎𝑟𝑟𝑒𝑎𝑟𝑠= 𝑁𝑜𝑚· 𝑃0, 𝑇′ · Δ𝑇· 𝐸𝑄𝑇′ 𝐹𝑇−𝐾+ 𝐸𝑄𝑇′
𝐹𝑇−𝐾· Δ𝑇· 𝐹𝑇
=
= 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝜟𝑻· 𝑬𝑸𝑻′
𝑭𝑻−𝑲
+ 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝚫𝑻𝟐· 𝑬𝑸𝑻′
𝑭𝑻−𝑲· 𝑭𝑻
El primer término es el precio del FRA usual. La corrección suele ser pequeña. El cálculo explícito de este segundo término 
nos da:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝐹𝑅𝐴𝑖𝑛−𝑎𝑟𝑟𝑒𝑎𝑟𝑠= 𝒗𝒂𝒍𝒐𝒓𝒉𝒐𝒚𝑭𝑹𝑨+ 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝚫𝑻𝟐· 𝑭𝟎
𝟐𝒆 𝝈𝟐𝑻−𝑲· 𝑭𝟎
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝐹𝑅𝐴𝑖𝑛−𝑎𝑟𝑟𝑒𝑎𝑟𝑠= 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝜟𝑻· 𝑬𝑸𝑻′
𝑭𝑻−𝑲
+ 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝚫𝑻𝟐· 𝑭𝟎
𝟐𝒆 𝝈𝟐𝑻−𝑲· 𝑭𝟎
3.1. Marco Black en tipos de interés. Tipos forward

## Página 17

Valoración. Marco Black
17
Valoración de opciones
3. Valoración de un FRA in arreas
Strike de equilibrio
𝐾= 𝐹0
1 + Δ𝑇𝐹0𝑒𝜎2𝑇
(1 + Δ𝑇𝐹0)
Esto es habitual llamarlo un “ajuste de convexidad o timing” al tipo forward de mercado.
3.1. Marco Black en tipos de interés. Tipos forward

## Página 18

Valoración. Marco Black
18
Valoración de opciones
4. Valoración de un caplet in-arrears
Con el mismo argumento del FRA in-arrears, la prima del caplet in-arrears es:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑐𝑎𝑝𝑙𝑒𝑡𝑖𝑛−𝑎𝑟𝑟𝑒𝑎𝑟𝑠= 𝑁𝑜𝑚· 𝑃0, 𝑇′ · Δ𝑇· 𝐸𝑄𝑇′ 𝐹𝑇−𝐾+ · 1 + Δ𝑇· 𝐹𝑇
=
= 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝜟𝑻· 𝑬𝑸𝑻′
𝑭𝑻−𝑲+ + 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝚫𝑻𝟐· 𝑬𝑸𝑻′
𝑭𝑻−𝑲+ · 𝑭𝑻
El término nuevo de “corrección” exige calcular una nueva integral, cuyo resultado es
𝐸𝑄𝑇′
𝐹𝑇−𝐾+𝐹𝑇= 𝐹0
2𝑒𝜎2𝑇Φ 𝑑∗−𝐾𝐹0Φ 𝑑+
Donde 𝑑+ tiene el significado habitual y
𝑑∗=
ln 𝐹0
𝐾
𝜎𝑇
+ 3
2 𝜎𝑇
3.1. Marco Black en tipos de interés. Tipos forward

## Página 19

Valoración. Marco Black
19
Valoración de opciones
4. Valoración de un caplet in-arrears
De manera que el valor del caplet in-arreas resulta ser:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑐𝑎𝑝𝑙𝑒𝑡𝑖𝑛−𝑎𝑟𝑟𝑒𝑎𝑟𝑠= 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝜟𝑻· 𝑭𝟎𝚽𝒅+ −𝑲𝚽𝒅−
+
 
+ 𝑵𝒐𝒎· 𝑷𝟎, 𝑻′ · 𝚫𝑻𝟐· 𝑭𝟎
𝟐𝒆𝝈𝟐𝑻𝚽𝒅∗−𝑲𝑭𝟎𝚽𝒅+
Donde
𝑑± =
ln 𝐹0
𝐾
𝜎𝑇
± 1
2 𝜎𝑇,
𝑑∗=
ln 𝐹0
𝐾
𝜎𝑇
+ 3
2 𝜎𝑇
3.1. Marco Black en tipos de interés. Tipos forward

## Página 20

Valoración. Marco Black
20
Marco Black en 
tipos de interés.
Tipos swap
3.2.

## Página 21

Valoración. Marco Black
21
Modelo de Black para tipos swap
Swaps
El instrumento financiero de interés será el swap de nominal 100% (en el que se paga tipo fijo y se recibe variable) con la 
siguiente estructura de fechas:
En cada fecha 𝑡𝑗 se fija el tipo simple 𝑅𝑡𝑗, 𝑡𝑗+1  para el periodo correspondiente
En cada tiempo 𝑡𝑗+1:
• se recibe 𝑅𝑡𝑗, 𝑡𝑗+1 (𝑡𝑗+1 −𝑡𝑗)
• se paga 𝐾· 𝑡𝑗+1 −𝑡𝑗
3.1. Marco Black en tipos de interés. Tipos swap

## Página 22

Valoración. Marco Black
22
Modelo de Black para tipos swap
Tipo forward swap
En tiempo 𝒕= 𝟎. El tipo forward-swap hoy es el tipo 𝐾 que hace que contratar este swap (hoy) cueste 0
𝑆𝑤𝑎𝑝0 = 𝑆𝑤𝑎𝑝0; 𝑡0, 𝑡1, … , 𝑡𝑛=
𝑃0, 𝑡0 −𝑃0, 𝑡𝑛
σ𝑗=1
𝑛
𝑃0, 𝑡𝑗· 𝑡𝑗−𝑡𝑗−1
En tiempo 𝒕< 𝒕𝟎. En cualquier tiempo hasta 𝑡0, podemos considerar el tipo forward swap para la misma estructura de 
fechas:
𝑆𝑤𝑎𝑝𝑡= 𝑆𝑤𝑎𝑝𝑡; 𝑡0, 𝑡1, … , 𝑡𝑛=
𝑃𝑡, 𝑡0 −𝑃𝑡, 𝑡𝑛
σ𝑗=1
𝑛
𝑃𝑡, 𝑡𝑗· 𝑡𝑗−𝑡𝑗−1
Que será el tipo de equilibrio en tiempo 𝑡
3.1. Marco Black en tipos de interés. Tipos swap

## Página 23

Valoración. Marco Black
23
Modelo de Black para tipos swap
Swaption
Un contrato swaption da derecho a entrar, en tiempo 𝑡0, en un swap en el que se recibirá variable y se pagará tipo fijo 𝐾.
En tiempo 𝑡0, recibir tipo variable y recibir el tipo 𝑆𝑤𝑎𝑝𝑡0 (tipo swap spot) de esa fecha será equivalente.
Así que sólo ejerceremos el swaption si 𝑆𝑤𝑎𝑝𝑡0 > 𝐾. En caso de entrar, intercambiaremos, en cada una de las fechas 
prescritas, el tipo 𝐾 por el tipo 𝑆𝑤𝑎𝑝𝑡0.
Por tanto, los flujos del swaption equivalen a un pago, en 𝑡0, de
𝑆𝑤𝑎𝑝𝑡0 −𝐾
+
෍
𝑗=1
𝑛
𝑃𝑡0, 𝑡𝑗· 𝑡𝑗−𝑡𝑗−1
3.1. Marco Black en tipos de interés. Tipos swap

## Página 24

Valoración. Marco Black
24
Modelo de Black para tipos swap
Activos básicos
Para valorar este swaption, tomaremos como activos básicos los bonos cupón cero de nominal 1 que vencen en las fechas 
sucesivas desde 𝑡0 hasta 𝑡𝑛:
𝐵𝑡𝑗,
 𝑗= 0,1,2, … , 𝑛
Numerario
El numerario más conveniente en este caso es el instrumento 𝐴 (la anualidad) que paga 1 por año repartido en las fechas 
desde 𝑡1 hasta 𝑡𝑛
𝐴𝑡= ෍
𝑗=1
𝑛
𝑃𝑡, 𝑡𝑗· 𝑡𝑗−𝑡𝑗−1
Por tanto, el valor del swaption queda
𝑆𝑤𝑎𝑝𝑡0 −𝐾
+𝐴𝑡0
3.1. Marco Black en tipos de interés. Tipos swap

## Página 25

Valoración. Marco Black
25
Modelo de Black para tipos swap
Probabilidad de valoración
Llamamos QA a la probabilidad tal que, para cada 𝑗= 1,2, … , 𝑛.
𝑃𝑡, 𝑡𝑗
𝐴𝑡
,
 son QA−martingalas para tiempos 𝑡≤𝑡0
Obsérvese que, en particular,
𝑆𝑤𝑎𝑝𝑡= 𝑃𝑡, 𝑡0 −𝑃𝑡, 𝑡𝑛
𝐴𝑡
 es QA−martingala
3.1. Marco Black en tipos de interés. Tipos swap

## Página 26

Valoración. Marco Black
26
Modelo de Black para tipos swap
Valoración
Todo activo 𝑋 replicable (con los bonos seleccionados) es martingala. Si su payoff en tiempo 𝑇 es 𝑋𝑇, su precio hoy se calcula 
como
𝑋0 = 𝐴0 · 𝐸𝑄𝐴
𝑋𝑇
𝐴𝑇
En particular, para el swaption,
𝐴0𝐸𝑄𝐴
𝑆𝑤𝑎𝑝𝑡0 −𝐾
+ · 𝐴0
𝐴𝑡0
= 𝐴0𝐸𝑄𝐴
𝑆𝑤𝑎𝑝𝑡0 −𝐾
+
(Obsérvese cuán conveniente es que se hayan cancelado los factores 𝐴𝑡0).
3.1. Marco Black en tipos de interés. Tipos swap

## Página 27

Valoración. Marco Black
27
Modelo de Black para tipos swap
Marco Black
Si se impone ahora una evolución lognormal para el tipo 𝑆𝑤𝑎𝑝𝑡:
𝑑𝑆𝑤𝑎𝑝𝑡= 𝑆𝑤𝑎𝑝𝑡𝜎𝑑𝑊𝑡
Resultando la fórmula de valoración
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑠𝑤𝑎𝑝𝑡𝑖𝑜𝑛= 𝐴0 𝑆𝑤𝑎𝑝0Φ 𝑑+ −𝐾Φ 𝑑−
Donde
𝑑± =
ln 𝑆𝑤𝑎𝑝0
𝐾
𝜎𝑡0
± 1
2 𝜎𝑡
¿cómo quedaría el swaption ATM?
3.1. Marco Black en tipos de interés. Tipos swap

## Página 28

Valoración. Marco Black
28
Modelo de Black para tipos swap
Ejercicio
Un bono paga cupones anuales y vence dentro de 10 años. Los 5 primeros años paga un cupón del 4%. Los cinco siguientes 
paga un cupón dado por:
ቐ
9%,
 
si S < 6%
3% + 3x 𝑆−6% ,
si S está entre 6% y 8%
9%,
 
si S > 8%
Donde 𝑆 es el tipo swap (anual) a 5 años que se fije dentro de 5 años.
1.
Valoración por integración numérica (𝜎= 25%)
2.
Valoración  desestructurándolo
3.
Valoración  con smile de volatilidad (𝜎6% = 26% y 𝜎8% = 24%)
3.1. Marco Black en tipos de interés. Tipos swap

## Página 29

Valoración. Marco Black
29
Modelo de Black para CMS (Constant Maturity Swap)
Hay contratos en los que los flujos periódicos, por ejemplo, trimestrales, no van vinculados al tipo a plazo de ese periodo sino, 
por ejemplo, al tipo swap a 10 años.
Consideremos, por ejemplo, un constant maturity swap en el que, al comienzo de cada trimestre:
la rama fija paga intereses con un tipo fijo (sobre un nominal);
la rama variable paga intereses según el tipo swap a 10 años de ese comienzo de trimestre.
En cada fecha 𝑇𝑖 la pata variable paga intereses según el tipo 𝑆𝑤𝑎𝑝𝑇𝑖 que se haya fijado en ese tiempo 𝑇𝑖 (el pago efectivo se 
multiplicando por el periodo de devengo y el nominal). 
Es un único pago (en cada fecha 𝑇𝑖), no periodificado en las fechas del swap.
3.1. Marco Black en tipos de interés. Tipos swap

## Página 30

Valoración. Marco Black
30
Modelo de Black para CMS (Constant Maturity Swap)
Para la valoración de (la rama variable) de este tipo de instrumentos, habrá que valorar cada uno de los flujos, uno por fecha de 
pago. El tipo swap que se usa en el contrato tiene un plazo (y una estructura de fechas) que está fija.
Digamos que una de esas fechas de pago es 𝑇. Usando la anualidad como numerario, la regla general nos dice que debemos 
calcular (con las notaciones ya usadas) esperanzas del tipo
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦𝑓𝑙𝑢𝑗𝑜= 𝐴0𝐸𝑄𝐴
𝑆𝑤𝑎𝑝𝑇
𝐴𝑇
(cuyo resultado habrá que multiplicar por el nominal y el periodo de devengo).
Nótese que, en la esperanza anterior ya no se produce la (mágica y conveniente) cancelación del factor 𝐴𝑇 , pues en este 
contrato el tipo 𝑆𝑤𝑎𝑝𝑇 se paga una única vez.
Conocemos la dinámica del tipo forward swap, y de hecho cómo es la variable aleatoria 𝑆𝑤𝑎𝑝𝑇. Pero ahora aparece 
multiplicada por el factor adicional 1/𝐴𝑇 .
3.1. Marco Black en tipos de interés. Tipos swap

## Página 31

Valoración. Marco Black
31
Modelo de Black para CMS (Constant Maturity Swap)
Observación. Si para un swap anual (a 𝑁 años) aproximamos
Por otro lado, tiene que ser consistente con la probabilidad de valoración, por lo que debe cumplirse:
𝑃0, 𝑇
𝐴0
= 𝐸𝑄𝐴
1
𝐴𝑇
= 𝐸𝑄𝐴𝛼+ 𝛽𝑆𝑤𝑎𝑝𝑇= 𝛼+ 𝛽𝐸𝑄𝐴𝑆𝑤𝑎𝑝𝑇
Lo cual nos dice que
𝑃0, 𝑇
𝐴0
= 𝛼+ 𝛽𝑆𝑤𝑎𝑝0
Por tanto
𝛽=
1
𝑆𝑤𝑎𝑝0
𝑃0, 𝑇
𝐴0
−
1
𝑝𝑙𝑎𝑧𝑜
3.1. Marco Black en tipos de interés. Tipos swap
También se usa el ajuste desarrollado por Brotherton-Ratcliffe-Iben

## Página 32

Valoración. Marco Black
32
Modelo de Black para CMS (Constant Maturity Swap)
Con la aproximación vista
𝐴0𝐸𝑄𝐴
𝑆𝑤𝑎𝑝𝑇
𝐴𝑇
= 𝐴0𝐸𝑄𝐴(𝑆𝑤𝑎𝑝𝑇𝛼+ 𝛽𝑆𝑤𝑎𝑝𝑇= 𝐴0 𝛼𝑆𝑤𝑎𝑝0 + 𝛽𝑆𝑤𝑎𝑝0
2𝑒𝜎2𝑇
= 𝐴0𝑆𝑤𝑎𝑝0 𝛼+ 𝛽𝑆𝑤𝑎𝑝0 + 𝛽𝑆𝑤𝑎𝑝0 𝑒𝜎2𝑇−1
=
= 𝑃0, 𝑇𝑆𝑤𝑎𝑝0(1 +
𝛽𝑆𝑤𝑎𝑝0
𝛼+ 𝛽𝑆𝑤𝑎𝑝0
𝑒𝜎2𝑇−1
3.1. Marco Black en tipos de interés. Tipos swap

## Página 33

Gracias

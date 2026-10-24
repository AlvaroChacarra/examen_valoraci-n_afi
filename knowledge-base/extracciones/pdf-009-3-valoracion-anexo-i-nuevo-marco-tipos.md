# PDF-009: 3.Valoración. Anexo I. Nuevo Marco Tipos.pdf

Original: [archivo raw](../../raw/marco-black/anexos-valoracion/3-valoracion-anexo-i-nuevo-marco-tipos.pdf). SHA-256: `25999f5dad0f46d42d35bb7ff4e41c61297bcd30744c3c3f98d6fc91fec1020a`.

Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.

## Página 1

Modelización Black.
Modelos de cotización para 
instrumentos 
de tipos en el nuevo marco 
financiero
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
Marco marco 
tipos
Anexo I.

## Página 4

Valoración. Marco Black
4
Introducción
1.

## Página 5

Valoración. Marco Black
5
Introducción
El modelo de Black para instrumentos de tipos de interés ha sido el estándar de cotización durante un buen número de años:
• permite traducir precios de opciones con distintos plazos, strikes, etc., al lenguaje común de la volatilidad;
• y gestionar/cubrir el riesgo del derivado.
El modelo Black (para instrumentos sobre tipos como caplets/floorlets o swaptions) sigue el planteamiento habitual:
• se eligen unos instrumentos de mercado (bonos cupón cero a los plazos de interés);
• se elige numerario (bonos o anualidades);
• y se postula una evolución de martingala lognormal para los procesos de precios de los instrumentos de mercado en 
términos del numerario.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 6

Valoración. Marco Black
6
Introducción
Algunas observaciones:
1.
Se utiliza una única curva, que sirve a su vez para descontar flujos y para calcular niveles de tipos implícitos. 
2.
Como las evoluciones de los tipos son lognormales, el modelo sólo genera tipos de interés positivos.
3.
Tipos forward lognormales no son compatibles con tipos swap también lognormales
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 7

Valoración. Marco Black
7
“Nuevas” condiciones de mercado
Entorno multicurva
Desde el verano del 2007, el mercado de tipos ha experimentado fuertes cambios que dan cuenta de nuevos riesgos (por 
ejemplo, crédito y liquidez) que ahora se reflejan en las cotizaciones.
En cuanto a la modelación matemática, esto supone introducir un marco multicurva, en el que conviven:
• una curva para descontar;
• y varias curvas de niveles de tipos, cada una asociada a cada subyacente o plazo.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 8

Valoración. Marco Black
8
“Nuevas” condiciones de mercado
Tipos negativos
Desde 2013 (con precedentes como franco suizo, yen japonés), con la caída de tipos de interés del euro, surge la necesidad de 
valorar opciones, por ejemplo, puts, con strike negativo; o directamente la necesidad de considerar tipos de interés negativos.
El modelo lognormal, recordemos, sólo puede dar lugar a tipos positivos, y en particular, todas las puts con strike negativo han 
de tener valor 0.
Para ajustarse a esta nueva realidad, debemos cambiar el modelo subyacente. Las alternativas que han ido adoptando los 
mercados son:
• modelos lognormales con shift;
• modelos normales.
En lo que sigue, veremos cómo podemos incorporar estos cambios a nuestro marco general de valoración.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 9

Valoración. Marco Black
9
Marco Black multicurva
1.

## Página 10

Valoración. Marco Black
10
Marco general de valoración
Nuestro objetivo: Valorar:
• productos estándar sin opcionalidad que dependen de cupones variables o fijos (que admiten replicación estática con 
objetos que pueden depender de varios subyacentes);
• productos estándar con opcionalidad (caplets/floorlets, swaptions) a través de fórmulas a la Black cuyos inputs dependerán 
de varias curvas.
En lo que sigue consideraremos productos que dependan de un único subyacente, el
Euribor a plazo Δ𝑇.
El plazo Δ𝑇 queda fijo en lo que sigue.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 11

Valoración. Marco Black
11
Marco general de valoración
1. Instrumentos de mercado
• Una colección de bonos cupón cero (𝑩𝑻𝒌), con vencimiento en la colección de fechas (𝑇𝑘) (que habitualmente serán 
múltiplos consecutivos de Δ𝑇). Cada 𝐵𝑇𝑘 paga 1 en fecha 𝑇𝑘.
• Una colección de instrumentos (𝑳𝑻𝒌).
 
Cada 𝐿𝑇𝑘 paga en función del Euribor a plazo Δ𝑇 que se fije en la fecha 𝑇𝑘, al que nos referiremos como 
𝑅(𝑇𝑘, 𝑇𝑘+ Δ𝑇)
 
El pago es de montante
𝑅𝑇𝑘, 𝑇𝑘+ Δ𝑇· Δ𝑇
 
en fecha 𝑇𝑘+ Δ𝑇.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 12

Valoración. Marco Black
12
Marco general de valoración
1. Instrumentos de mercado. Notaciones
El precio en tiempo 𝑡∈[0, 𝑇𝑘] del bono 𝐵𝑇𝑘 se denota como
𝑃(𝑡, 𝑇𝑘)
El precio en tiempo 𝑡∈[0, 𝑇𝑘+ Δ𝑇] del instrumento 𝐿𝑇𝑘 se denota como
𝑉(𝑡, 𝑇𝑘)
Para 𝑡= 𝑇𝑘+ Δ𝑇
𝑉𝑇𝑘+ Δ𝑇, 𝑇𝑘= 𝑅𝑇𝑘, 𝑇𝑘+ Δ𝑇· Δ𝑇
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 13

Valoración. Marco Black
13
Marco general de valoración
2. Numerarios
Como numerario elegiremos, en función del derivado de interés, un bono 𝐵𝑇𝑘 , o quizás la cuenta bancaria 𝛽(𝑡), o la anualidad 
asociada a un cierto intervalo de tiempo (el instrumento que paga 1 por año durante el intervalo).
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 14

Valoración. Marco Black
14
Marco general de valoración
3. Datos de mercado
Disponemos de la colección de precios
𝑃0, 𝑇1 , 𝑃0, 𝑇2 , … 
 
(la curva de descuento libre de riesgo).
Y de la colección de precios de cada 𝐿𝑇𝑘:
𝑉0, 𝑇1 , 𝑉0, 𝑇2 , …
Definimos:
𝑣𝑎𝑙𝑜𝑟ℎ𝑜𝑦(𝐿𝑇𝑘) =  𝑉(0, 𝑇𝑘) =  Δ𝑇· 𝑃(0, 𝑇𝑘+ Δ𝑇) · 𝐿(0, 𝑇𝑘, 𝑇𝑘+ Δ𝑇) .
Estos tipos 𝐿 desempeñan el papel de los tipos implícitos.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 15

Valoración. Marco Black
15
Marco general de valoración
4. Valoración por replicación
Cupón Cero (válido para cupón fijo)
El instrumento que en tiempo 𝑇𝑘 paga 𝑁𝑜𝑚 se valora como
𝑃0, 𝑇𝑘· 𝑁𝑜𝑚
Es decir, un descuento de flujos
Cupón Variable
El instrumento que en tiempo 𝑇𝑘+ Δ𝑇paga el Euribor fijado en 𝑇𝑘 de nominal 𝑁𝑜𝑚
Δ𝑇· 𝑃(0, 𝑇𝑘+ Δ𝑇) · 𝐿(0, 𝑇𝑘, 𝑇𝑘+ Δ𝑇) · 𝑁𝑜𝑚
FRA de strike 𝑲 que paga en tiempo 𝑻𝒌+ 𝜟𝑻
𝑁𝑜𝑚· Δ𝑇· 𝑃(0, 𝑇𝑘+ Δ𝑇) · (𝐿0, 𝑇𝑘, 𝑇𝑘+ Δ𝑇−𝐾)
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 16

Valoración. Marco Black
16
Marco general de valoración
4. Valoración por replicación
Swap de strike 𝑲 que fija en 𝒕𝟎, … , 𝒕𝒏−𝟏 y paga en 𝒕𝟏, … , 𝒕𝒏
Se valora como
𝑁𝑜𝑚· ෍
𝑖=0
𝑛−1
Δ𝑇· 𝑃0, 𝑡𝑖+ Δ𝑇· [𝐿0, 𝑡𝑖, 𝑡𝑖+ Δ𝑇−𝐾]
Cuyo strike de equilibrio es
𝑇𝑆= σ𝑖=0
𝑛−1 Δ𝑇· 𝑃0, 𝑡𝑖+ Δ𝑇· 𝐿0, 𝑡𝑖, 𝑡𝑖+ Δ𝑇
σ𝑖=0
𝑛−1 Δ𝑇· 𝑃(0, 𝑡𝑖+ Δ𝑇)
Suponemos aquí que todos los periodos son de Δ𝑇. Una notación más cuidadosa tendría en cuenta cada intervalo 𝑡𝑖+1 −𝑡𝑖. 
Podría darse también el caso de que las frecuencias de pago no coincidieran para las patas fija y variable.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 17

Valoración. Marco Black
17
Marco general de valoración
5. Modelo de valoración para caplets/floorlets
Instrumentos de mercado
𝐵𝑇+Δ𝑇,
 
𝐿𝑇
Numerario
Tomamos 𝐵𝑇+Δ𝑇 como numerario
Probabilidad de valoración y martingalas
Imponemos que, bajo una cierta probabilidad, que denotamos por 𝐐𝐓+𝚫𝐓 , el proceso
𝑉𝑡, 𝑇
𝑃𝑡, 𝑇+ Δ𝑇
Sea martingala en 0 ≤𝑡≤𝑇+ Δ𝑇
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 18

Valoración. Marco Black
18
Marco general de valoración
5. Modelo de valoración para caplets/floorlets
Si denotamos
𝐿𝑡, 𝑇, 𝑇+ Δ𝑇≡
𝑉𝑡, 𝑇
Δ𝑇· 𝑃𝑡, 𝑇+ Δ𝑇
Entonces 𝐿𝑡, 𝑇, 𝑇+ Δ𝑇 es también martingala
Obsérvese que:
• Para 𝑡= 0, el valor 𝐿0, 𝑇, 𝑇+ Δ𝑇 es un dato de mercado
• Y que para 𝑡= 𝑇
𝐿𝑇, 𝑇, 𝑇+ Δ𝑇≡
𝑉𝑇, 𝑇
Δ𝑇· 𝑃𝑇, 𝑇+ Δ𝑇= 𝑅(𝑇, 𝑇+ ΔT)
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 19

Valoración. Marco Black
19
Marco general de valoración
5. Modelo de valoración para caplets/floorlets
I) Para el instrumento 𝐿𝑇 tenemos que
𝑉0, 𝑇
𝑃0, 𝑇+ Δ𝑇= E
𝑅𝑇, 𝑇+ Δ𝑇· Δ𝑇
𝑃𝑇+ Δ𝑇, 𝑇+ Δ𝑇
= Δ𝑇· E 𝑅𝑇, 𝑇+ Δ𝑇
De manera que
𝐿0, 𝑇, 𝑇+ Δ𝑇= E 𝑅𝑇, 𝑇+ Δ𝑇
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 20

Valoración. Marco Black
20
Marco general de valoración
5. Modelo de valoración para caplets/floorlets
II) Para el instrumento FRA con strike 𝐾 y nominal 𝑁𝑜𝑚
𝑝𝑟𝑒𝑐𝑖𝑜ℎ𝑜𝑦𝐹𝑅𝐴𝐾
𝑃0, 𝑇+ Δ𝑇
= E
𝑅𝑇, 𝑇+ Δ𝑇−𝐾· Δ𝑇· 𝑁𝑜𝑚
𝑃𝑇+ Δ𝑇, 𝑇+ Δ𝑇
= Δ𝑇· 𝑁𝑜𝑚· E
𝑅𝑇, 𝑇+ Δ𝑇−𝐾
De manera que
𝑝𝑟𝑒𝑐𝑖𝑜ℎ𝑜𝑦𝐹𝑅𝐴𝐾= Δ𝑇· 𝑁𝑜𝑚· 𝑃0, 𝑇+ Δ𝑇· 𝐿0, 𝑇, 𝑇+ Δ𝑇−𝐾
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 21

Valoración. Marco Black
21
Marco general de valoración
5. Modelo de valoración para caplets/floorlets
III) Para el instrumento caplet con strike 𝐾 y nominal 𝑁𝑜𝑚
𝑝𝑟𝑒𝑐𝑖𝑜ℎ𝑜𝑦𝑐𝑎𝑝𝑙𝑒𝑡𝐾
𝑃0, 𝑇+ Δ𝑇
= E
𝑅𝑇, 𝑇+ Δ𝑇−𝐾+ · Δ𝑇· 𝑁𝑜𝑚
𝑃𝑇+ Δ𝑇, 𝑇+ Δ𝑇
De manera que
𝑝𝑟𝑒𝑐𝑖𝑜ℎ𝑜𝑦𝑐𝑎𝑝𝑙𝑒𝑡𝐾= Δ𝑇· 𝑁𝑜𝑚· 𝑃0, 𝑇+ Δ𝑇· E
𝑅𝑇, 𝑇+ Δ𝑇−𝐾+
Que requiere de un modelo
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 22

Valoración. Marco Black
22
Marco general de valoración
5. Modelo de valoración para caplets/floorlets
III) Para el instrumento caplet con strike 𝐾 y nominal 𝑁𝑜𝑚
Imponemos una dinámica lognormal a 𝐿𝑡≡𝐿(𝑡, 𝑇, 𝑇+ Δ𝑇)
𝑑𝐿𝑡= 𝜎𝐿𝑡𝑑𝑊𝑡
Tenemos
𝐿𝑇= 𝑅𝑇, 𝑇+ Δ𝑇= 𝐿0𝑒−𝜎2
2 𝑇𝑒𝜎𝑇𝑁0,1
Llegando con cálculos B-S
𝑝𝑟𝑒𝑐𝑖𝑜ℎ𝑜𝑦𝑐𝑎𝑝𝑙𝑒𝑡𝐾= Δ𝑇· 𝑁𝑜𝑚· 𝑃0, 𝑇+ Δ𝑇· [𝐿0Φ 𝑑+ −𝐾Φ 𝑑−]
Donde
𝑑± =
ln 𝐿0
𝐾
𝜎𝑇
± 1
2 𝜎𝑇
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 23

Valoración. Marco Black
23
Marco general de valoración
6. Modelo de valoración para swaptions
El swaption que consideramos es el contrato que da opción a entrar en un swap (con intercambio de intereses devengados 
por Euribor a plazo Δ𝑇 por intereses devengados por un tipo fijo) con estructura de fechas 𝑡0, 𝑡1, … , 𝑡𝑛. Aquí, 𝑡0 es primera 
fecha de fijación de Euribor, y 𝑡1, … , 𝑡𝑛 son fechas de intercambio de intereses.
Denotamos por 𝑅(𝑡𝑖, 𝑡𝑖+ Δ𝑇) a los tipos Euribor (a plazo Δ𝑇) que se van fijando en
las sucesivas fechas 𝑡0, … , 𝑡𝑛−1.
Como instrumentos de mercado consideramos los bonos 𝐵𝑡1, … , 𝐵𝑡𝑛(que vencen en las fechas de intercambio de intereses), y 
los instrumentos𝐿𝑡0, … , 𝐿𝑡𝑛−1. Sean
𝑃𝑡, 𝑡1 , … , 𝑃𝑡, 𝑡𝑛,
 𝑉𝑡, 𝑡0 , … , 𝑉(𝑡, 𝑡𝑛−1)
sus respectivos procesos de precios.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 24

Valoración. Marco Black
24
Marco general de valoración
6. Modelo de valoración para swaptions
Consideramos el instrumento 𝐴, la anualidad, que paga 1 por año entre 𝑡1 y 𝑡𝑛. Su proceso de precios es
𝐴𝑡= ෍
𝑖=1
𝑛
Δ𝑇· 𝑃𝑡, 𝑡𝑖
Los datos de mercado son
los precios 𝑃0, 𝑡1 , … , 𝑃0, 𝑡𝑛de donde obtenemos 𝐴0;
y los precios 𝑉0, 𝑡0 , … , 𝑉(0, 𝑡𝑛−1);
de lo anterior deducimos 𝐿0, 𝑡0, 𝑡0 + Δ𝑇, … , 𝐿(0, 𝑡𝑛−1, 𝑡𝑛−1 + Δ𝑇) mediante
𝑉0, 𝑡𝑖= Δ𝑇· 𝑃0, 𝑡𝑖+ Δ𝑇· 𝐿(0, 𝑡𝑖, 𝑡𝑖+ Δ𝑇)
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 25

Valoración. Marco Black
25
Marco general de valoración
6. Modelo de valoración para swaptions
Definimos el proceso del tipo swap
𝑇𝑆𝑡= σ𝑖=0
𝑛−1 Δ𝑇· 𝑃𝑡, 𝑡𝑖+ Δ𝑇· 𝐿(𝑡, 𝑡𝑖, 𝑡𝑖+ Δ𝑇)
𝐴𝑡
Numerario
Tomamos la anualidad como numerario
Probabilidad de valoración y martingalas
Imponemos que, bajo cierta probabilidad, los procesos
𝑃𝑡, 𝑡𝑖
𝐴𝑡
,
𝑉𝑡, 𝑡𝑖
𝐴𝑡
Sean martingala
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 26

Valoración. Marco Black
26
Marco general de valoración
6. Modelo de valoración para swaptions
I) Valoración del swap con strike 𝐾 y nominal 𝑁𝑜𝑚
La pata fija se valora, en tiempo 0 ≤𝑡≤𝑡0
𝑁𝑜𝑚· 𝐾෍
𝑖=0
𝑛−1
Δ𝑇· 𝑃𝑡, 𝑡𝑖+ Δ𝑇= 𝐾· 𝐴𝑡
La pata variable será
𝑁𝑜𝑚· 𝐾෍
𝑖=0
𝑛−1
Δ𝑇· 𝑃𝑡, 𝑡𝑖+ Δ𝑇· 𝐿(𝑡, 𝑡𝑖, 𝑡𝑖+ Δ𝑇)
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 27

Valoración. Marco Black
27
Marco general de valoración
6. Modelo de valoración para swaptions
II) Valoración del swaption con strike 𝐾 y nominal 𝑁𝑜𝑚
El payoff del instrumento se puede escribir como 𝑇𝑆𝑡0 −𝐾
+𝐴𝑡0 · 𝑁𝑜𝑚, por tanto, la valoración es
𝑝𝑟𝑒𝑐𝑖𝑜ℎ𝑜𝑦𝑠𝑤𝑎𝑝𝑡𝑖𝑜𝑛𝐾
𝐴0
= E
𝑇𝑆𝑡0 −𝐾
+𝐴𝑡0 · 𝑁𝑜𝑚
𝐴𝑡0
Un cálculo que requiere, de nuevo, un modelo
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 28

Valoración. Marco Black
28
Marco general de valoración
6. Modelo de valoración para swaptions
II) Valoración del swaption con strike 𝐾 y nominal 𝑁𝑜𝑚
Si imponemos dinámica lognormal al proceso 𝑇𝑆𝑡
𝑑𝑇𝑆𝑡= 𝜎𝑇𝑆𝑡𝑑𝑊𝑡
Se tiene
𝑇𝑆𝑡0 = 𝑇𝑆0𝑒−𝜎2
2 𝑇𝑒𝜎𝑡0𝑁0,1
Llegando con cálculos B-S
𝑝𝑟𝑒𝑐𝑖𝑜ℎ𝑜𝑦𝑠𝑤𝑎𝑝𝑡𝑖𝑜𝑛𝐾= 𝑁𝑜𝑚· A0 TS0Φ 𝑑+ −𝐾Φ 𝑑−
Donde
𝑑± =
ln 𝑇𝑆0
𝐾
𝜎𝑡0
± 1
2 𝜎𝑡0
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 29

Valoración. Marco Black
29
Entorno de tipos 
negativos
2.

## Página 30

Valoración. Marco Black
30
Contexto
En el marco Black (una sola curva), modelizamos el forward 𝐹𝑡 (correspondiente al periodo 𝑇 → 𝑇+ Δ𝑇) como martingala 
lognormal:
𝐹𝑡= 𝐹0𝑒−𝜎2
2 𝑡𝑒𝜎𝑡𝑁0,1
lo que nos lleva a la fórmula del caplet con strike 𝐾 y fecha de pago 𝑇 + Δ𝑇:
𝑐𝑎𝑝𝑙𝑒𝑡= Δ𝑇· 𝑃0, 𝑇+ Δ𝑇𝐹0Φ 𝑑+ −𝐾Φ 𝑑−
,
 
𝑑± =
ln 𝐹0
𝐾
𝜎𝑇
± 1
2 𝜎𝑇
• El modelo solo genera valores de tipos positivos;
• la fórmula no permite cotizar opciones con strike negativo.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 31

Valoración. Marco Black
31
Modelo shifted lognormal
En este modelo, postulamos la evolución del forward 𝐹𝑡 (correspondiente al periodo 𝑇 → 𝑇 + Δ𝑇) como sigue:
𝑑𝐹𝑡= 𝜎𝑠ℎ𝐹𝑡+ 𝑠ℎ𝑑𝑊𝑡
con valor inicial 𝐹0  +  𝑠ℎ. Aquí, 𝜎𝑠ℎ> 0 y 𝜎𝑠ℎ≥0 son dos parámetros. Distinguimos con un subíndice la volatilidad en este 
modelo.
La evolución anterior nos da que
𝐹𝑡+ 𝑠ℎ= 𝐹0 + 𝑠ℎ𝑒−𝜎𝑠ℎ
2
2 𝑡𝑒𝜎𝑠ℎ
𝑡𝑁0,1
El caso en el que 𝑠ℎ =  0 es el marco Black habitual
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 32

Valoración. Marco Black
32
Modelo shifted lognormal
Esto nos da la siguiente fórmula del precio del caplet con strike 𝐾, nominal 1, y fecha de pago 𝑇+ Δ𝑇:
𝑝𝑟𝑒𝑐𝑖𝑜 𝑐𝑎𝑝𝑙𝑒𝑡= Δ𝑇𝑃0, 𝑇+ Δ𝑇
𝐹0 + 𝑠ℎΦ 𝑑+ −𝐾+ 𝑠ℎΦ 𝑑−
Con
𝑑± =
ln 𝐹0 + 𝑠ℎ
𝐾+ 𝑠ℎ
𝜎𝑠ℎ𝑇
± 𝜎𝑠ℎ𝑇
Y la delta resulta ser:
Δ𝑠ℎ= 𝜕
𝜕𝐹0
𝑝𝑟𝑒𝑐𝑖𝑜 𝑐𝑎𝑝𝑙𝑒𝑡= Δ𝑇· 𝑃0, 𝑇+ Δ𝑇· Φ(𝑑+)
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 33

Valoración. Marco Black
33
Modelo shifted lognormal
La variable aleatoria
𝐹𝑡= 𝐹0 + 𝑠ℎ𝑒−𝜎𝑠ℎ
2
2 𝑡𝑒𝜎𝑠ℎ
𝑡𝑁0,1 −𝑠ℎ
Toma valores entre −𝑠ℎ e infinito. Así que el modelo contempla tipos negativos de valor hasta −𝑠ℎ
Además, la fórmula de valoración del caplet permite imputar valores de 𝐹0 y 𝐾 negativos, siempre que no se supere el umbral 
de −𝑠ℎ.
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 34

Valoración. Marco Black
34
Modelo shifted lognormal
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 35

Valoración. Marco Black
35
Modelo normal
Louis Bachelier, 1900, Théorie de la Spéculation
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 36

Valoración. Marco Black
36
Modelo normal
Louis Bachelier, 1900, Théorie de la Spéculation
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 37

Valoración. Marco Black
37
Modelo normal
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 38

Valoración. Marco Black
38
Modelo normal
En este modelo, postulamos la evolución del forward 𝐹𝑡 (correspondiente al periodo 𝑇 → 𝑇 + Δ𝑇) como una martingala 
normal
𝑑𝐹𝑡= 𝜎𝑛𝑑𝑊𝑡
Con valor inicial 𝐹0
Hay un único parámetro, 𝜎𝑛 > 0, que de nuevo distinguimos con un subíndice. Obsérvese, a efectos de comparación de escala, 
que 𝜎𝑛 es una volatilidad absoluta (y no relativa, como en el modelo lognormal).
La evolución anterior nos da que
𝐹𝑡= 𝐹0 + 𝜎𝑛𝑡𝑁0,1
El modelo permite generar tipos negativos de valor arbitrario
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 39

Valoración. Marco Black
39
Modelo normal
Siguiendo el paradigma de valoración habitual, para el caplet con strike 𝐾, nominal 1 y fecha de pago 𝑇 + Δ𝑇, tenemos que 
precio caplet
𝑝𝑟𝑒𝑐𝑖𝑜 𝑐𝑎𝑝𝑙𝑒𝑡
𝑃0, 𝑇+ Δ𝑇
= E
Δ𝑇· 𝑅𝑇, 𝑇+ Δ𝑇−𝐾+
𝑃𝑇+ Δ𝑇, 𝑡+ Δ𝑇
= Δ𝑇· E
𝑅𝑇, 𝑇+ Δ𝑇−𝐾+
de donde obtenemos:
𝑝𝑟𝑒𝑐𝑖𝑜 𝑐𝑎𝑝𝑙𝑒𝑡= Δ𝑇· 𝑃0, 𝑇+ Δ𝑇
𝐹0 −𝐾Φ 𝑑+ 𝜎𝑛·
𝑇𝜙𝑑
Donde Φ y 𝜙 son, respectivamente, la función de distribución y la función de densidad de la normal estándar, y donde
𝑑= 𝐹0 −𝐾
𝜎𝑛𝑇
¿Cómo quedaría el ATM? ¿Y la delta?
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 40

Valoración. Marco Black
40
Modelo normal
Las volatilidades en un modelo (shifted)lognormal son volatilidades relativas. Las volatilidades normales son absolutas. La 
escala de las segundas debería ser del mismo orden de magnitud que el de los niveles del subyacente (porcentajes, en el caso 
de tipos).
En principio, sólo podemos relacionar 𝜎𝑠ℎ y 𝜎𝑛 a través de los precios (de mercado) de los caplets.
En algún caso, se pueden obtener aproximaciones. Por ejemplo, en el caso ATM, donde𝐹0 = 𝐾, entonces
(shifted lognormal): 𝑝𝑟𝑒𝑐𝑖𝑜 𝑐𝑎𝑝𝑙𝑒𝑡 =  Δ𝑇 ·  𝑃0, 𝑇 + Δ𝑇· 𝐹0  +  𝑠ℎ
2Φ
𝜎𝑠ℎ𝑇
2
−1
(normal): precio caplet = Δ𝑇· 𝑃0, 𝑇+ Δ𝑇· 𝜎𝑛
𝑇
2𝜋
Si T es pequeño (la opción vence pronto), usando una aproximación del tipo Φ 𝑥≈
1
2 +
𝑥
2𝜋, adecuada si 𝑥 es pequeño, se 
obtiene que
𝜎𝑛≈𝐹0 + 𝑠ℎ𝜎𝑠ℎ
Modelos de cotización para instrumentos de tipos en el nuevo marco financiero

## Página 41

Gracias

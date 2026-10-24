# PDF-010: 4.Valoración. Anexo II. Marco Black Tipo de Cambio.pdf

Original: [archivo raw](../../raw/marco-black/anexos-valoracion/4-valoracion-anexo-ii-marco-black-tipo-de-cambio.pdf). SHA-256: `e0b3df0f0d90077ca87632416e90f37d437a63c57d2409788442da0424c05b74`.

Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.

## Página 1

Modelización Black.
Modelos estándar para tipos de 
cambio
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
FX
Anexo II.

## Página 4

Valoración. Marco Black
4
Introducción
Esta sección está dedicada al marco Black para la valoración de derivados sobre tipos de cambio. En todo lo que sigue, la 
moneda local será el euro; es decir, el punto de vista será el de un inversor en euros.
Denotaremos por 
𝐹𝑋(𝑡)
el tipo de cambio euros por dólar de tiempo 𝑡, es decir, el número de euros que se paga por 1 dólar en tiempo 𝑡.
El tipo de cambio de dólares por euros es, claro
1
𝐹𝑋𝑡
Importante: FX tiene unidades 
𝑒𝑢𝑟𝑜𝑠
𝑑ó𝑙𝑎𝑟𝑒𝑠. Es decir, si se multiplica FX por un montante en dólares devuelve euros.
En lo que sigue, seremos especialmente cuidadosos con las unidades en las que están expresados los pagos, sobre todo por la 
existencia de contratos quanto.
Marco Black en FX

## Página 5

Valoración. Marco Black
5
Notación
Las curvas de descuento en euros y en dólares se denotarán, respectivamente, por:
Así,
𝑃𝑒𝑢𝑟(𝑡, 𝑠) es el precio (en euros) que se paga en tiempo t por un euro de tiempo s.
𝑃𝑑𝑜𝑙(𝑡, 𝑠) es el precio (en dólares) que se paga en tiempo t por un dólar de tiempo s.
Marco Black en FX

## Página 6

Valoración. Marco Black
6
Contrato forward
En un contrato forward sobre FX (con un nominal, vencimiento T y strike K), 
• una parte se compromete a comprar un cierto montante (nominal) de dólares a un tipo de cambio K (que tiene unidades 
𝑒𝑢𝑟𝑜𝑠
𝑑ó𝑙𝑎𝑟𝑒𝑠) fijado a inicio;
• la otra parte se compromete a vender dólares a ese tipo de cambio K
en una fecha futura T.
Desde el punto de vista de la parte que compra dólares, el resultado neto en euros a vencimiento T es:
pues se compran dólares a tipo de cambio prefijado K y se pueden vender a tipo de cambio FX(T).
Marco Black en FX

## Página 7

Valoración. Marco Black
7
Replicación estática y valoración
La valoración del contrato forward no requiere modelo, porque se puede replicar estáticamente.
Digamos que el nominal es de 1M dólares.
La replicación (desde el punto de vista de quien compra dólares) va como sigue:
Al inicio:
compramos el bono (en dólares) de nominal [1M dólares]. El coste (en euros) es
vendemos el bono (en euros) de nominal K · [1M dólares]. Recibimos (en euros)
Marco Black en FX

## Página 8

Valoración. Marco Black
8
Replicación estática y valoración
En total, el coste (en euros) de formar esta cartera es
Liquidación en tiempo T:
• Recibiremos 1M dólares, que equivaldrán, en euros, a FX(T) · 
𝑒𝑢𝑟𝑜𝑠
𝑑ó𝑙𝑎𝑟𝑒𝑠· [1M dólares];
• pagaremos un montante (en euros) de K ·
𝑒𝑢𝑟𝑜𝑠
𝑑ó𝑙𝑎𝑟𝑒𝑠 · [1M dólares].
Así que en total recibiremos, en euros,
que es justo el flujo del forward.
Concluimos que la prima del forward ha de coincidir con el coste de formación de la cartera de réplica, es decir, en euros,
Marco Black en FX

## Página 9

Valoración. Marco Black
9
Tipo de cambio forward
El tipo de cambio forward (visto hoy, 𝑡 =  0) para el vencimiento 𝑇, que denotaremos por 𝐹𝑋𝑓𝑤𝑑(0 →𝑇), es justo el K que 
hace que el contrato forward a inicio valga 0.
En general, el tipo de cambio forward visto en tiempo t para el vencimiento T es
Marco Black en FX

## Página 10

Valoración. Marco Black
10
Call y put sobre el tipo de cambio
Una call de vencimiento T y con strike K sobre el tipo de cambio con nominal 1M dólares da derecho a comprar 1M dólares a 
tipo de cambio K.
La call equivale a recibir en tiempo T:
que, insistimos, es un montante en euros. 
Por su parte, la put da derecho a vender en fecha futura T a un determinado tipo de cambio prefijado, y equivale a recibir el 
montante (en euros)
Marco Black en FX

## Página 11

Valoración. Marco Black
11
Call y put sobre el tipo de cambio
Activos básicos
Los activos que constituyen el mercado de referencia son
• el bono cupón cero en dólares que vence en tiempo T, con precio (en dólares) en tiempo t dado por 𝑃𝑑𝑜𝑙(𝑡, 𝑇)
• el bono cupón cero en euros que vence en tiempo T, con precio (en euros) en tiempo t dado por 𝑃𝑒𝑢𝑟(𝑡, 𝑇)
Numerario
Tomamos como numerario a 𝑃𝑒𝑢𝑟(𝑡, 𝑇)
Marco Black en FX

## Página 12

Valoración. Marco Black
12
Marco Black
Condición de martingala
Los valores (en euros) de ambos activos, expresados en unidades del numerario, han de
ser martingala:
Estas dos condiciones se reducen a la exigencia de que
sea martingala. A partir de ahora, como T está fijo, abreviaremos la notación:
Marco Black en FX

## Página 13

Valoración. Marco Black
13
Marco Black
Lognormalidad Black
En el marco Black se postula que la evolución de 𝐹𝑋𝑓𝑤𝑑𝑡 es martingala lognormal. El único parámetro es la volatilidad
Esto supone que:
1) conocemos explícitamente cómo es la variable 𝐹𝑋𝑓𝑤𝑑𝑡, una lognormal:
2) En particular, en 𝑡 =  𝑇,
3) Por ser martingala,
Marco Black en FX

## Página 14

Valoración. Marco Black
14
Marco Black
Lognormalidad Black
4) Finalmente, recordamos que el tipo de cambio forward 𝐹𝑋𝑓𝑤𝑑𝑡 coincidirá con el tipo de cambio spot FX(T) de esa fecha 
T, que será el que determine los pagos de los instrumentos
Marco Black en FX

## Página 15

Valoración. Marco Black
15
Marco Black
Valoración del forward
La prima (en euros, para la parte que compra dólares) es
pues el numerario se hace 1 en tiempo T. Es decir,
que se puede reescribir como
como ya sabíamos.
Marco Black en FX

## Página 16

Valoración. Marco Black
16
Marco Black
Valoración de la call
Adoptamos, de nuevo, el punto de vista del inversor en euros que tiene derecho a comprar dólares.
La prima de la call (en euros) vendrá dada por
de donde se obtiene la siguiente fórmula tipo Black:
Marco Black en FX

## Página 17

Valoración. Marco Black
17
Marco Black
Valoración de la call
En términos de los datos de mercado hoy:
Donde:
Marco Black en FX

## Página 18

Valoración. Marco Black
18
Marco Black. Quanto
Un derivado quanto es un derivado sobre tipo de cambio que paga el flujo en la moneda que no le es “natural”.
1. Forward quanto
Por ejemplo, el forward habitual sobre tipo de cambio con nominal 1M de dólares paga (obviando la rama fija)
así que, si resulta que FX(T) = 0.8, entonces se reciben 800,000 euros.
En la versión quanto, el contrato paga
así que si el número FX(T) resulta ser 0.8, se reciben 800,000 ¡dólares!, es decir, 640,000 euros.
Marco Black en FX

## Página 19

Valoración. Marco Black
19
Marco Black. Quanto
1. Forward quanto
En el forward quanto se recibe (desde el punto de vista de quien compra dólares)
que pasamos a euros (que es nuestra moneda natural, la del numerario y la probabilidad de valoración) de la siguiente forma:
Para la valoración, usamos que 𝐹𝑋𝑓𝑤𝑑𝑡 es martingala lognormal para, con un argumento análogo al que usamos en el FRA in 
arrears, obtener que la prima (obviando el nominal) es
Marco Black en FX

## Página 20

Valoración. Marco Black
20
Marco Black. Quanto
2. Call quanto
En la call quanto se recibe (desde el punto de vista de quien compra dólares)
que de nuevo pasamos a euros de la siguiente forma:
La valoración (obviando el nominal) consistiría en calcular
es un cálculo análogo al que abordamos con el caplet in arrears
Marco Black en FX

## Página 21

Valoración. Marco Black
21
Marco Black. Quanto
3. Call binaria quanto
Comparamos los contratos en los que, si en tiempo T el tipo de cambio FX(T) supera un nivel K,
• el contrato 1 paga 1M dólares;
• el contrato 2 paga 1M euros.
La primera del contrato 1 sería
La prima del contrato 2, por su parte, se calcularía
Marco Black en FX

## Página 22

Gracias

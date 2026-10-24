# PPT-001: Ejercicio 3. Desarrollo.pptx

Original: [archivo raw](../../raw/encargo/ejercicio-3-desarrollo.pptx).

Extracción por diapositiva, incluidas las ecuaciones OfficeMath. Los huecos de la plantilla se conservan. La notación lineal se debe leer junto a la ficha de fuente.

## Diapositiva 1

Modelización BlackEjercicio 3

Nombre(s):

## Diapositiva 2

Opciones Quanto

## Diapositiva 3

Objetivo

Marco Black

Construir un modelo para valorar forwards y opciones (usuales y quanto) sobre una acción cotizada en dólares. La cotización en dólares en tiempo 𝑡 se denotará por {𝑆}_{𝑡}.

El vencimiento de todos los instrumentos es 𝑇 años.

La cotización actual es {𝑆}_{0} dólares.

La tasa (continua) de dividendos estimada es 𝑞.

La volatilidad cotizada es de {𝜎}_{𝑆}.

El punto de vista para valoración, replicación, cobertura, etc., será siempre el de un inversor en euros.

3

## Diapositiva 4

Instrumentos que queremos valorar a mercado

Marco Black

Este es el forward usual (en dólares). El instrumento paga al inversor:

{𝑆}_{𝑇}−𝐾 dólares

Es decir, con un strike 𝐾=130 dólares, si {𝑆}_{𝑇} fuera 135 dólares, el inversor recibiría 5 dólares; y si fuera 125 pagaría 5 dólares.

Este no es el forward usual. El instrumento paga al inversor

{𝑆}_{𝑇}−𝐾 euros

Digamos, de nuevo, que el strike es 𝐾=130 dólares. Entonces, si {𝑆}_{𝑇} fuera 135 dólares, el inversor recibiría 5 ¡euros!, y si fuera {𝑆}_{𝑇}=125 dólares, el inversor pagaría 5 ¡euros!

4

F

FQ

## Diapositiva 5

Instrumentos que queremos valorar a mercado

Marco Black

Esta es la call usual (en dólares). El instrumento paga al inversor:

{{𝑆}_{𝑇}−𝐾}^{+} dólares

Es decir, con un strike 𝐾=130 dólares, si {𝑆}_{𝑇} fuera 135 dólares, el inversor recibiría 5 dólares; y si fuera 125 el inversor recibe 0 dólares.

Esta no es la call usual. El instrumento paga al inversor

{{𝑆}_{𝑇}−𝐾}^{+} euros

Digamos, de nuevo, que el strike es 𝐾=130 dólares. Entonces, si {𝑆}_{𝑇} fuera 135 dólares, el inversor recibiría 5 ¡euros!, y si fuera {𝑆}_{𝑇}=125 dólares, el inversor recibe 0 euros

5

C

CQ

## Diapositiva 6

Tipos de interés

Marco Black

Supondremos que los tipos de interés (tanto en euros como en dólares) son constantes:

Tipo en dólares: {𝑟}_{$}

Tipo en euros: {𝑟}_{€}

Cuenta bancaria en dólares: {𝛽}_{$}𝑡={𝑒}^{{𝑟}_{$}·𝑡}

Cuenta bancaria en euros: {𝛽}_{€}𝑡={𝑒}^{{𝑟}_{€}·𝑡}

Las curvas de descuento en euros y dólares se denotarán por

{𝑃}_{𝑒𝑢𝑟}𝑡,𝑇,   {𝑃}_{𝑑𝑜𝑙}𝑡,𝑇

Así, {𝑃}_{𝑑𝑜𝑙}𝑡,𝑇 es el precio (en dólares) que se paga en tiempo 𝑡 por un dólar de tiempo 𝑇

6

## Diapositiva 7

Tipo de cambio

Marco Black

Denotaremos por:

𝐹𝑋𝑡= 𝐹{𝑋}_{𝑡}

el tipo de cambio spot euro por dólar de tiempo 𝑡, es decir, el número de euros que se paga por 1 dólar en tiempo 𝑡.

La moneda local es el euro, es decir, el punto de vista será el de un inversor en euros.

Datos: el valor de 𝐹{𝑋}_{0} y la volatilidad {𝜎}_{𝐹} de 𝐹{𝑋}_{𝑡}

7

## Diapositiva 8

Tipo de cambio

Marco Black

Sobre unidades

FX tiene unidades \frac{𝑒𝑢𝑟𝑜𝑠}{𝑑ó𝑙𝑎𝑟𝑒𝑠}. Es decir, si multiplica FX por un montante en dólares devuelve euros.

Sobre flujos

Los valores (en euros) de los flujos de los cuatro instrumentos viene dados por

𝑭→{𝑆}_{𝑇}−𝐾·𝐹{𝑋}_{𝑇}

𝑭𝑸→{𝑆}_{𝑇}−𝐾

𝑪→{{𝑆}_{𝑇}−𝐾}^{+}·𝐹{𝑋}_{𝑇}

𝑪𝑸→{{𝑆}_{𝑇}−𝐾}^{+}

8

## Diapositiva 9

Marco Black

Marco Black

Numerario

La cuenta bancaria en euros: {𝛽}_{€}𝑡={𝑒}^{{𝑟}_{€}·𝑡}

Activos básicos

Cuenta bancaria en euros

Cuenta bancaria en dólares

El activo subyacente

9

## Diapositiva 10

Marco Black

Marco Black

Martingalas

El valor (en euros) de invertir en cada activo básico, expresado en términos del numerario, ha de ser martingala. Estas tres inversiones son: 1 euro en cuenta bancaria europea, 1 dólar en cuenta bancaria en dólares, y una acción del subyacente.

Es decir, los tres siguientes procesos:

\frac{{𝛽}_{€}𝑡}{{𝛽}_{€}𝑡}≡1,  \frac{{𝛽}_{$}𝑡·𝐹{𝑋}_{𝑡}}{{𝛽}_{€}𝑡}≡{𝑀}_{𝑡},  \frac{{𝑒}^{𝑞·𝑡 }{𝑆}_{𝑡}·𝐹{𝑋}_{𝑡}}{{𝛽}_{€}𝑡}≡{𝑁}_{𝑡}

Han de ser martingala.

10

## Diapositiva 11

Marco Black

Marco Black

Dinámicas Black

En el marco Black, imponemos que {𝑀}_{𝑡} y {𝑁}_{𝑡} sean martingalas lognormales de volatilidad constante y correladas:

𝑑{𝑀}_{𝑡}=𝑑{𝑁}_{𝑡}=

Donde {𝑈}_{𝑡} y {𝑉}_{𝑡} son movimientos brownianos con correlación instantánea {𝜌}_{𝑀,𝑁}. Es decir,

𝑑{𝑈}_{𝑡}·𝑑{𝑉}_{𝑡}={𝜌}_{𝑀,𝑁}𝑑𝑡

Esto supone que

{𝑀}_{𝑡}={𝑁}_{𝑡}=

Donde las normales estándar tienen correlación {𝜌}_{𝑀,𝑁}

11

(1)

(2)

Definir los brownianos como {𝑈}_{𝑡} y {𝑉}_{𝑡}

## Diapositiva 12

Marco Black

Marco Black

Diccionarios entre los procesos anteriores y el par 𝑭{𝑿}_{𝒕},{𝑺}_{𝒕}

Las relaciones

{𝐹𝑋}_{𝑡}={𝑆}_{𝑡}=

Ya dan implícitamente la distribución a vencimiento de ambas variables. Esto implica que:

Bastaría simular valores de {𝑀}_{𝑇} y {𝑁}_{𝑇} y trasladar en valores de 𝐹{𝑋}_{𝑇} y {𝑆}_{𝑇}

Para obtener sendas conjuntas de 𝐹{𝑋}_{𝑡} y {𝑆}_{𝑡} bastaría con simular sendas conjuntas de {𝑀}_{𝑡} y {𝑁}_{𝑡}

Pero ¿cuáles son los valores de {𝜎}_{𝑀}, de {𝜎}_{𝑁} y de {𝜌}_{𝑀,𝑁}? Es necesario hacer explícitos los procesos de 𝐹{𝑋}_{𝑡} y {𝑆}_{𝑡}, porque son los observables en mercado, y porque son las volatilidades de estos procesos las que cotizan y no, claro, las de {𝑀}_{𝑡} y {𝑁}_{𝑡}

12

(3)

Poner 𝐹{𝑋}_{𝑡} y {𝑆}_{𝑡} en función de {𝑀}_{𝑡} y {𝑁}_{𝑡}

## Diapositiva 13

Marco Black

Marco Black

Evolución explícita de 𝑭{𝑿}_{𝒕} y de {𝑺}_{𝒕}

Buscamos las evoluciones de 𝐹{𝑋}_{𝑡} y de {𝑆}_{𝑡} del tipo

𝑑{𝐹𝑋}_{𝑡}={𝜇}_{𝐹}𝐹{𝑋}_{𝑡}𝑑𝑡+{𝜎}_{𝐹}𝐹{𝑋}_{𝑡}𝑑{𝑊}_{𝑡}𝑑{𝑆}_{𝑡}={𝜇}_{𝑆}{𝑆}_{𝑡}𝑑𝑡+{𝜎}_{𝑆}{𝑆}_{𝑡}𝑑{𝑍}_{𝑡}

con correlación {𝜌}_{𝐹,𝑆} entre los dos brownianos, que hacen que las correspondientes evoluciones de los procesos anteriores (inversión en activos básicos en términos del numerario) sean martingalas.

Obsérvese que {𝜎}_{𝑠}, {𝜎}_{𝐹}, e incluso {𝜌}_{𝐹,𝑆}, son datos que se pueden considerar de mercado.

Queda sólo la cuestión de determinar qué derivas {𝜇}_{𝐹} y {𝜇}_{𝑆} hacen que {𝑀}_{𝑡} y {𝑁}_{𝑡} sean martingalas

13

## Diapositiva 14

Marco Black

Marco Black

Evolución explícita de 𝑭{𝑿}_{𝒕} y de {𝑺}_{𝒕}

En {𝑀}_{𝑡} solo interviene 𝐹{𝑋}_{𝑡} y el lema de Itô da directamente que

{𝜇}_{𝐹}=

En {𝑁}_{𝑡} intervienen 𝐹{𝑋}_{𝑡}, cuya deriva ya está determinada, y {𝑆}_{𝑡}. El lema de Itô, aplicado al producto

{𝑆}_{𝑡}·𝐹{𝑋}_{𝑡}, nos da que

{𝜇}_{𝑆}=

14

(4)

(5)

## Diapositiva 15

Marco Black

Marco Black

Desarrollo matemático de (4)

15

## Diapositiva 16

Marco Black

Desarrollo matemático de (5)

16

Marco Black

## Diapositiva 17

Marco Black

Evolución explícita de 𝑭{𝑿}_{𝒕} y de {𝑺}_{𝒕}

En tiempo 𝑇 tendremos que

{𝐹𝑋}_{𝑡}=𝐹{𝑋}_{0}·{𝑆}_{𝑡}={𝑆}_{0}·

Donde las normales estándar {𝑍}_{𝐹} y {𝑍}_{𝑆} tienen correlación {𝜌}_{𝐹,𝑆}

17

(6)

Marco Black

## Diapositiva 18

Marco Black

Fórmulas de valoración

F.- Forward usual en dólares

El coste en dólares de replicación de este instrumento es

{𝑆}_{0}{𝑒}^{−𝑞𝑇}−𝐾{𝑒}^{−{𝑟}_{$}𝑇}

Por tanto, en euros, es:

𝐹{𝑋}_{0}{𝑆}_{0}{𝑒}^{−𝑞𝑇}−𝐾{𝑒}^{−{𝑟}_{$}𝑇}

La valoración anterior no requiere modelo alguno. Vamos a comprobar que, con la modelación Black anterior, se obtiene el mismo resultado.

18

Marco Black

## Diapositiva 19

Marco Black

Fórmulas de valoración

F.- Forward usual en dólares

El valor del flujo del forward (pasado a euros) es {X}_{T}={𝑆}_{𝑇}−𝐾·𝐹{𝑋}_{𝑡} así que, el valor hoy en términos del numerario es

\frac{{𝑋}_{0}}{{𝛽}_{€0}}=\frac{𝐸{𝑋}_{𝑇}}{{𝛽}_{€}𝑡}→

19

(7)

Marco Black

## Diapositiva 20

Marco Black

Desarrollo matemático de (7). Llegar a la ecuación vista en la página 18.

Nota: Usar que tanto {𝑁}_{𝑡} como {𝑀}_{𝑡} son martingalas

20

Marco Black

## Diapositiva 21

Marco Black

Fórmulas de valoración

FQ.- Forward quanto en euros

El valor del flujo del forward es directamente {X}_{T}={𝑆}_{𝑇}−𝐾 (montante ya en euros) así que, el valor hoy en términos del numerario es

\frac{{𝑋}_{0}}{{𝛽}_{€0}}=\frac{𝐸{𝑋}_{𝑇}}{{𝛽}_{€}𝑡}→

21

(8)

Marco Black

## Diapositiva 22

Marco Black

Desarrollo matemático de (8).

22

Marco Black

## Diapositiva 23

Marco Black

Fórmulas de valoración

CQ.- Call quanto en euros

El valor del flujo de la call es directamente {X}_{T}={{𝑆}_{𝑇}−𝐾}^{+} (montante ya en euros) así que, el valor hoy en términos del numerario es

\frac{{𝑋}_{0}}{{𝛽}_{€0}}=\frac{𝐸{𝑋}_{𝑇}}{{𝛽}_{€}𝑡}→

𝑣𝑎𝑙𝑜𝑟=\frac{𝐸{{𝑆}_{𝑇}−𝐾}^{+}}{{𝛽}_{€}𝑡}=

23

(9)

Marco Black

## Diapositiva 24

Marco Black

Desarrollo matemático de (9).

24

Marco Black

## Diapositiva 25

Marco Black

Fórmulas de valoración

C.- Call usual en dólares

El valor ha de ser el valor de la call (en dólares) pasado a euros, es decir,

𝑣𝑎𝑙𝑜𝑟=𝐹{𝑋}_{0}{𝑆}_{0}{𝑒}^{−𝑞𝑇}Φ{𝑑}_{+}−𝐾{𝑒}^{−{𝑟}_{$}𝑇}Φ{𝑑}_{−}

Con

{𝑑}_{±}=\frac{ln\frac{{𝑆}_{0}{𝑒}^{−𝑞𝑇}}{𝐾{𝑒}^{{𝑟}_{$}𝑇}}}{{𝜎}_{𝑆}\sqrt{𝑇}}±\frac{1}{2}{𝜎}_{𝑆}\sqrt{𝑇}

Replicar este cálculo bajo nuestro marco Black.

25

(10)

+0.5 puntos adicionales

Marco Black

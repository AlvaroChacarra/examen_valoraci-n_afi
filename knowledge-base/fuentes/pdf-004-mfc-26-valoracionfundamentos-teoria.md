# PDF-004: MFC_26_ValoracionFundamentos_Teoría.pdf

[Original](../../raw/fundamentos/mfc-26-valoracionfundamentos-teoria.pdf) · [Texto por páginas](../extracciones/pdf-004-mfc-26-valoracionfundamentos-teoria.md) · [Mapa del curso](../MAPA_RELACIONES.md)

Páginas PDF: **158**. Las referencias usan la página física del PDF, no el número del nombre de un Excel.

## Contenido y navegación

| Páginas | Bloque |
|---|---|
| 1–6 | Plan, martingalas y guía del modelo |
| 7–21 | Paradigmas de valoración y grandes números |
| 22–36 | Réplica estática y arbitraje |
| 37–57 | Mercado matricial y numerarios |
| 58–76 | Probabilidades, completitud, cambio de numerario y cotas |
| 77–90 | Modelo multiperiodo y carteras dinámicas |
| 91–101 | Valoración dinámica y cambio de numerario |
| 102–117 | Modelos continuos y guía de construcción |
| 118–122 | Apéndice A1: réplicas adicionales |
| 123–124 | A2: mercados incompletos |
| 125–137 | A3: modelización y probabilidades implícitas |
| 138–141 | A4: procesos de ganancia |
| 142–147 | A5: teorema fundamental |
| 148–151 | A6: numerarios y probabilidades |
| 152–153 | A7: unicidad de probabilidad |
| 154–157 | A8: ejemplos generales de valoración |
| 158–158 | Cierre |

## Relaciones con los ejercicios

- **Ley de los grandes números con pagos independientes**: [XLS-001](../fuentes/xls-001-grandes-numeros-1-iid.md)
- **Correlación y límites de la diversificación**: [XLS-002](../fuentes/xls-002-grandes-numeros-2-correlacion.md)
- **Mercado matricial: réplica, arbitraje y numerarios**: [XLS-003](../fuentes/xls-003-plantilla1.md), [XLS-007](../fuentes/xls-007-plantilla1-solucion.md)
- **Réplica dinámica y cambio de numerario**: [XLS-004](../fuentes/xls-004-plantilla2.md), [XLS-008](../fuentes/xls-008-plantilla2-solucion.md)
- **Distribución implícita en calls y puts**: [XLS-015](../fuentes/xls-015-pag-1-33-probs-implicitas-con-calls-puts.md), [XLS-020](../fuentes/xls-020-1-3-probs-implicitas-con-calls-puts-plantilla.md)

## Cómo interpretarlo

Este documento aporta teoría y ejemplos de clase. Las relaciones de navegación no convierten automáticamente esos ejemplos en soluciones del encargo. Las fórmulas fundamentales se han reescrito en los [conceptos](../conceptos/README.md) para evitar depender del orden de glifos de una extracción PDF.

El nombre del archivo sitúa el material en el curso 2026, pero varias páginas conservan referencias internas a 2021–2022. Se preservan tal cual; no se ha supuesto una actualización de su contenido.

## Índice de todas las páginas

Los títulos siguientes son extractos breves para recuperación. El texto completo queda en la extracción.

| Página | Inicio de contenido |
|---:|---|
| 1 | Máster Executive Finanzas Cuantitativas / Valoración: / Fundamentos |
| 2 | Plan y resumen / Se pretende dar un marco general de modelos estoc´asticos que permiten valorar a / mercado (por replicaci´on) instrumentos derivados. |
| 3 | (La modelaci´on matem´atica) En la pr´actica, / →si el modelo incorpora una probabilidad P (que diremos de valoraci´on) en el espacio / de escenarios de evoluci´on de manera que, para cada u |
| 4 | As´ı que si en un modelo tenemos / un numerario; / una probabilidad de valoraci´on; |
| 5 | Discutiremos primero los distintos paradigmas de valoraci´on, centr´andonos en (e ilus- / trando con ejemplos sencillos) el de valoraci´on por replicaci´on (no arbitraje). / A continuaci´on, |
| 6 | ´Indice / 1 Paradigmas de valoraci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 / 2 Valoraci´on por replicaci´on. . . . .  |
| 7 | 1. Paradigmas de valoraci´on |
| 8 | ¿Qu´e es valorar? / Por instrumento ﬁnanciero entendemos un contrato entre dos partes por el que se / estipulan unos ﬂujos en ciertas fechas futuras, y por el que en la fecha de hoy se |
| 9 | Valoraci´on de lo cierto / Digamos que el instrumento paga cantidades seguras / f1, . . . , fN |
| 10 | La expresi´on anterior es bien natural. Pero, ¡atenci´on!, vista desde otro punto de vista, / la cantidad / f1 FD(t1) + f2 FD(t2) + · · · + fN FD(tN) |
| 11 | Valoraci´on de lo incierto: ingredientes / Los ﬂujos de los instrumentos ﬁnancieros generales son inciertos y no seguros. El enfoque / general de valoraci´on de instrumentos ﬁnancieros – en  |
| 12 | 1. Escenarios / Se trata de determinar qu´e puede ocurrir en el futuro. Decidir qu´e eventos futuros / (relevantes para el instrumento, o mejor, para una cierta colecci´on de instrumentos) h |
| 13 | 2. Flujos y descuentos / Para cada escenario habr´a que precisar a continuaci´on / Flujo, el montante que se recibir´a o pagar´a en cada escenario concreto. |
| 14 | 3. Probabilidad / El ´ultimo ingrediente es el m´as delicado. Si entendemos que estamos en un contexto / de incertidumbre, debemos asignarle a cada escenario de futuro una probabilidad de |
| 15 | En suma, tendremos una asignaci´on / escenario e −→ / ⎧ |
| 16 | Valoraci´on de lo incierto: paradigmas / Paradigma de valoraci´on actuarial / Si tenemos buena informaci´on estad´ıstica de la frecuencia con la que cada escenario ha |
| 17 | Digamos que las variables aleatorias X1, . . . , XN codiﬁcan / los premios obtenidos en sucesivas partidas de un juego de azar, / o los pagos a N mutualistas por los siniestros sufridos dura |
| 18 | →Pero si, adem´as, las variables con independientes (basta con que sean incorreladas), / entonces las leyes de los grandes n´umeros nos dicen que, si N es grande, / N |
| 19 | A´un m´as, el teorema del l´ımite central permite cuantiﬁcar c´omo de probable es que YN / se aparte de la cantidad NE(X). Por ejemplo, permite calcular (aproximadamente) / cantidades como P |
| 20 | As´ı que / si se sabe de manera objetiva que los ﬂujos de un instrumento (juego) son aleatorios; / si se conoce con precisi´on la distribuci´on de probabilidad de los resultados; |
| 21 | Pero digamos ahora que tenemos un ´unico contrato. Por simpliﬁcar, supongamos que / hay una ´unica fecha de pago y que el ﬂujo del instrumento es f. / Disponemos de largas series de datos hi |
| 22 | 2. Valoraci´on por replicaci´on |
| 23 | Par´abola de la porra / Supongamos que s´olo hay dos resultados (por ejemplo, una ﬁnal de Copa): victoria de X / o victoria de Y. Cada apuesta es de 1 euro. |
| 24 | En el mecanismo de la porra, una apuesta por X supone que / su precio es 1; / no hay descuento; |
| 25 | ¿C´omo valorar esta oferta OTC? ¿C´omo obtener su precio? (hacemos caso omiso de / comisiones). / Queremos aplicar el paradigma de valoraci´on habitual. Esto es, promediar los posibles |
| 26 | Justiﬁcaci´on: formamos una cartera con 1.5 boletos de X y 2.1 boletos de Y. / Formar esta cartera cuesta precisamente 3.6 euros. Pero la cartera equivale al contrato / que ofrece el revende |
| 27 | Valoraci´on a mercado / Los “mercados” dan ya precio a una gran variedad de instrumentos. / Observaci´on |
| 28 | Replicaci´on/arbitraje/valoraci´on (relativa) / 1. Mercado / Disponemos de una serie de activos, A, B, C, . . . cuyos precios hoy son conocidos, y |
| 29 | 3. Replicaci´on / Replicar (de manera exacta y est´atica) el activo X con los activos A, B, C, . . . signiﬁca / hallar una cartera de estos ´ultimos de manera que, pase lo que pase (sea cual |
| 30 | Consecuencia 1. / Dos carteras que tienen los mismos ﬂujos han de tener el mismo precio hoy. / Observaci´on |
| 31 | Comentarios / Si X se replica con una cartera con α unidades de A, β de B, γ de C, etc., y si no / hay arbitraje, entonces |
| 32 | Ilustraciones de valoraci´on por replicaci´on / Veamos algunos ejemplos de valoraci´on por replicaci´on (exacta) est´atica, en los que / se constituye una cartera al inicio que, sin alteraci |
| 33 | 2. Contrato forward. El forward con strike K paga ST −K sobre S, que no paga / dividendos. La replicaci´on se obtiene con una acci´on comprada y un bono (de / principal K, cup´on cero y venc |
| 34 | a) Instrumentos de mercado: dos bonos cup´on cero / El primer bono (cup´on cero) es BT, que vence en tiempo T. Si su nominal es Nom, / su precio hoy es Nom · P(0, T). |
| 35 | c) Flujos de la cartera (en tiempo T + ΔT) / Tras tiempo T, tenemos 100 de contado, procedentes del primer bono (y prestamos esa / cantidad al tipo simple que se ﬁje entonces), y seguimos te |
| 36 | 4. Activo no replicable (est´aticamente) / -4 / -2 |
| 37 | 3. Modelo matricial de un s´olo periodo de tiempo: / planteamiento |
| 38 | Vamos a exhibir a continuaci´on los ingredientes de nuestro primer modelo (un solo / periodo de tiempo, modelo matricial): / escenarios; |
| 39 | Escenarios. Tiempos e incertidumbre / En este modelo matricial de mercado ﬁnanciero, el tiempo desempe˜na un papel menor: / s´olo hay dos instantes de tiempo, que convencionalmente denotarem |
| 40 | Activos / 1.- Activos b´asicos / Tenemos M activos, que se pueden comprar y vender en tiempo t = 0 y comprar y |
| 41 | Tiempo t = 0. Los activos en tiempo 0 valen / S0 / 1, S0 |
| 42 | Conviene considerar a cada S1 / i como un vector de RN que recoge sus valores en los N / escenarios: |
| 43 | ejemplo base / En lo que sigue, argumentaremos e ilustraremos las sucesivas nociones que ir´an apareciendo / con este modelo, en el que tenemos |
| 44 | 2.- Activos generales / Un activo (general) es un instrumento X que en tiempo t = 1 tiene ﬂujos/valores dados / en cada escenario: X(ωj), j = 1, . . . , N. Un activo es, pues, un vector arbi |
| 45 | ejemplo. Activos Arrow–Debreu y bonos. / Un par de activos especiales (no necesariamente b´asicos) son: / Los activos Arrow–Debreu. Hay un activo Arrow–Debreu por cada escenario. El |
| 46 | 3.- Carteras de activos b´asicos y de activos generales / Una cartera de inversi´on en los activos b´asicos es un vector que registra las unidades / invertidas en cada activo, es decir, un v |
| 47 | Carteras de activos generales / Asimismo se pueden formar carteras de activos generales. / N´otese, por ejemplo, que el bono es una cartera de Arrow–Debreu: |
| 48 | 4.- Numerarios / Los valores son siempre relativos. Necesitaremos comparar valores de tiempos distintos, / y para ello expresar los valores en unidades homog´eneas. Lo m´as habitual es utili |
| 49 | Elecciones habituales: / El numerario m´as habitual es el bono, el activo D, que suele aparecer como uno de / los activos b´asicos. |
| 50 | Replicaci´on con activos b´asicos / Un activo X es replicable con los activos b´asicos si hay una cartera de inversi´on / λ = (λ1, . . . , λM)T en ellos que genera exactamente el mismo ﬂujo  |
| 51 | Que, en notaci´on matricial, se expresa: / (λ1, . . . , λM) · / ⎛ |
| 52 | Replicabilidad de activos. Mercados completos / Dado un modelo, un activo puede / no ser replicable con los activos b´asicos; |
| 53 | Ilustraci´on / Consid´erese el modelo S = / ⎛ |
| 54 | Observaci´on / Notas matriciales. En el modelo matricial, todo lo relacionado con replicabilidad (o no) son cuestiones sobre resoluci´on / de sistemas de ecuaciones: |
| 55 | Observaci´on / N´umero de activos b´asicos y n´umero de escenarios. / • Para que el modelo sea completo hace falta que haya al menos tantos activos b´asicos como escenarios. Pero puede |
| 56 | Oportunidades de arbitraje / Una oportunidad de arbitraje con los activos b´asicos es una cartera que tiene / un valor de 0 en t = 0; |
| 57 | Obs´ervese que, en contra de lo que ocurr´ıa con la noci´on de la replicaci´on, en el concepto / de oportunidad de arbitraje s´ı intervienen los valores de los activos b´asicos en t = 0. / N |
| 58 | 4. Modelo matricial de un s´olo periodo de tiempo: / valoraci´on |
| 59 | La replicaci´on interesa para valoraci´on: / si un activo (del que tan s´olo conocemos sus ﬂujos) se puede replicar con / activos b´asicos, entonces el coste de una cartera replicante es un  |
| 60 | Probabilidad de valoraci´on y numerarios / Introducimos aqu´ı el concepto de probabilidad de valoraci´on, que resuelve, conjunta / y eﬁcientemente, varias cuestiones pr´acticas planteadas. S |
| 61 | Probabilidad de valoraci´on con respecto a un numerario / Fijamos un activo especial N como numerario. Una probabilidad Q en Ω se dice / probabilidad de valoraci´on respecto de N si |
| 62 | C´alculo de una probabilidad de valoraci´on / Aceptemos, por ahora, que la noci´on de probabilidad de valoraci´on es relevante y ´util y / planteemos: ¿c´omo hallar una probabilidad de valor |
| 63 | Salvo por la condici´on de que los qj sean probabilidades, el que el sistema tenga soluci´on / (una, muchas o ninguna) depender´a de si el rango de / S es menor o mayor que N. |
| 64 | ejemplo base / Compru´ebese que, si consideramos el numerario N = S1, la probabilidad Q dada por / Q(ω1) = 13.33 % , |
| 65 | Relevancia de la probabilidad de valoraci´on / Si para un numerario tenemos una probabilidad de valoraci´on asociada, entonces / 1.- En el modelo no hay oportunidades de arbitraje. |
| 66 | Observaci´on / Determinar una probabilidad de valoraci´on requiere resolver un cierto sistema de ecuaciones (tantos como activos / b´asicos) y con tantas inc´ognitas como escenarios en el qu |
| 67 | 2.- El valor del activo (replicable) X que en tiempo t = 1 tiene ﬂujos X1 es (ha de ser) / X0 / N0 = EQ |
| 68 | 3.- En la pr´actica se construyen modelos “certiﬁcables”de valoraci´on / 1. decidiendo activos b´asicos; / 2. especiﬁcando escenarios y determinando valores/ﬂujos de los activos b´asicos; |
| 69 | Cambio de numerario / Digamos que, para un cierto numerario N, tenemos ya calculada una probabilidad de / valoraci´on asociada, que denotamos por QN. |
| 70 | ´Esta es la ecuaci´on de cambio de numerario: dados dos numerarios, podemos obtener la / probabilidad de uno a partir de una probabilidad de valoraci´on del otro. / Detalle: |
| 71 | Mercados completos / 1. El modelo de mercado se dice completo cuando todos los activos posibles sobre el / espacio de escenarios Ω son replicables. |
| 72 | 4. En modelos de mercado completos, y bajo la hip´otesis de ausencia de oportunidad / de arbitraje, para cada numerario N hay una ´unica probabilidad de valoraci´on QN. / De hecho, esa proba |
| 73 | Mercados no completos. Activos no replicables. Cotas / Consideramos un modelo de mercado con activos b´asicos (S1, . . . , SM). Suponemos que / no hay oportunidades de arbitraje. |
| 74 | Supongamos que hemos ﬁjado un numerario N y que estamos manejando una probabi- / lidad Q de valoraci´on asociada. A cada activo X podemos asignarle el “precio” / N0 × EQ |
| 75 | Ejemplo. Consideremos el siguiente modelo de mercado (3 activos y 4 escenarios): / ⎛ / ⎝ |
| 76 | Pero, de hecho, hay inﬁnitas probabilidades de valoraci´on para N. La probabilidad Q / ser´a de valoraci´on siempre que / Q(ω1) + Q(ω2) = 50 %; |
| 77 | 5. Modelo de varios periodos: / planteamiento |
| 78 | Evoluciones en el tiempo: no arbitraje y martingalas / Hasta ahora hemos tratado un modelo simpliﬁcado con dos instantes de tiempo: “hoy” / y el “futuro”. Ahora vamos ahora a considerar evol |
| 79 | Formalizamos. / Espacio de escenarios / Tenemos nuestro espacio de escenarios: Ω = {ω1, ω2, . . . , ωN}. |
| 80 | En esta secci´on, utilizaremos como gu´ıa el siguiente / ejemplo base / S´olo hay dos tiempos t1 y t2 (adem´as de t0 = 0). |
| 81 | Flujo de informaci´on / Con el paso del tiempo disponemos de cada vez m´as informaci´on sobre la evoluci´on / de los activos y de sus ﬂujos. Modelamos este ﬂujo de informaci´on con unas vari |
| 82 | ejemplo base / La variable Y1 toma los valores a, b, c y la variable Y2 los valores 1, 2, 3. El espacio de escenarios / Ω queda entonces registrado por pares de valores (a, 1), (a, 2), . . . |
| 83 | 1. Activos b´asicos / Tenemos M activos b´asicos: S1, S2, . . . , SM. Cada uno de estos activos es un proceso / en el tiempo. La sucesi´on de variables |
| 84 | ejemplo base / Recordemos que las variables de estado Y1 e Y2 toman valores / {a, b, c} y {1, 2, 3}, respectivamente. El espacio Ω = F2 consta |
| 85 | 2. Estrategias de inversi´on y estrategias autoﬁnanciadas / Las estrategias de inversi´on son ahora procesos. Se invierte en los activos din´amicamente, / cambiando en cada tk la composici´o |
| 86 | En una cartera autoﬁnanciada, en cada tiempo tk la cartera se puede recomponer, es / decir, cambiar su composici´on, pero no se aportan ni se retiran fondos. / As´ı, en una cartera autoﬁnanc |
| 87 | 3. Activo replicable / Un activo general X paga en tiempo tH: X(ω), ﬂujo de X en escenario ω. / El activo es replicable si hay una estrategia de inversi´on autoﬁnanciada tal que |
| 88 | C´alculo de una cartera replicante / La estrategia de replicaci´on se obtiene procediendo hacia atr´as en el ´arbol. Lo ilustramos / en el ejemplo base. |
| 89 | Por ejemplo, en el nodo a, tendr´ıamos el siguiente modelo matricial: / S1 / S2 |
| 90 | - / w / - |
| 91 | 6. Modelo de varios periodos: / valoraci´on |
| 92 | Valoraci´on por replicaci´on / Si suponemos que no tenemos oportunidades de arbitraje, para valorar un activo X que / paga unos ciertos ﬂujos en tiempo T, |
| 93 | Valoraci´on con probabilidades / Numerario / Un numerario N es un activo b´asico (o una cartera autoﬁnanciada de activos b´asicos) |
| 94 | Pero adem´as, si Q es probabilidad de valoraci´on, el proceso de valor de una cartera / autoﬁnanciada tambi´en es Q-martingala: / V tk−1 |
| 95 | Probabilidad de valoraci´on y no arbitraje / Si, ﬁjado un numerario, hay probabilidad de valoraci´on, ya hemos visto que el proceso / de valor de una cartera autoﬁnanciada es martingala. En  |
| 96 | C´alculo de una probabilidad de valoraci´on / Fijamos un numerario N. Podemos construir una probabilidad de valoraci´on (que en / principio est´a deﬁnida para cada una de las sendas posibles |
| 97 | Observaci´on / detalle del argumento. Lo ilustramos en el ejemplo base. Digamos que, para el modelo que comienza en a (con / notaci´on obvia), tenemos una probabilidad de valoraci´on |
| 98 | Valoraci´on de activos replicables / Para valorar un activo replicable no hace falta exhibir la cartera replicante, basta con / saber que es posible. Si X es activo replicable, existir´a una |
| 99 | Observaci´on / De nuevo, tenemos una equivalencia: / no hay oportunidades de arbitraje |
| 100 | Cambio de numerario / Si el mercado es completo y libre de arbitraje, entonces para cada numerario N hay una / ´unica probabilidad de valoraci´on respecto de N, que denotamos por QN. |
| 101 | Esto nos dice que si hemos obtenido y calculado la probabilidad QN, no necesitamos / repetir un c´alculo an´alogo para obtener QM, sino que basta con observar que / QM = MtH |
| 102 | 7. Modelos continuos: valoraci´on |
| 103 | El esquema de modelo de mercado ﬁnanciero anterior se extiende al caso de evoluci´on / continua del tiempo t para 0 ≤t ≤T. / Si enfocamos s´olo la cuesti´on de valoraci´on a mercado, como ha |
| 104 | Planteamos los ingredientes: / Tiempo y escenarios / El tiempo ahora va desde t = 0 hasta t = T de forma continua. |
| 105 | Activos b´asicos / Tenemos una serie de activos b´asicos, S1, . . . , SM, que podemos comprar y vender sin / restricci´on en cada instante de tiempo t, 0 ≤t ≤T. |
| 106 | Numerario / De entre ese abanico de activos (b´asicos o carteras autoﬁnanciadas de estos), seleccio- / namos un activo especial N, el numerario, al que exigimos que en todo tiempo t sea |
| 107 | Ausencia de oportunidades de arbitraje y valoraci´on / Fijado un numerario N, si existe una probabilidad Q de manera que los activos / expresados en unidades del numerario sean martingala, e |
| 108 | ¿Por qu´e libre de arbitraje? / Si los activos, en unidades del numerario, son martingala, entonces cualquier estrategia / de inversi´on autoﬁnanciada en estos activos (expresada en unidades |
| 109 | Valoraci´on de lo replicable / Llamemos X(T) a los ﬂujos de un activo en tiempo T y supongamos que podemos / dise˜nar una estrategia de inversi´on autoﬁnanciada que d´e lugar a una cartera C |
| 110 | Observaci´on / M´as a´un, si denotamos por X(t) al valor del activo en tiempo t, entonces, / X(t) = N(t)EQ |
| 111 | Notas adicionales / En realidad, la existencia de la probabilidad de valoraci´on Q y la ausencia de oportunidad / de arbitraje son equivalentes. |
| 112 | Gu´ıa de construcci´on de modelos (continuos) / Al construir un modelo de valoraci´on, empezaremos / especiﬁcando los activos b´asicos (¿cu´ales?, depender´a de los instrumentos que |
| 113 | Queremos valorar un instrumento, un cierto derivado (una call, o algo m´as soﬁsticado) / sobre un subyacente S. En nuestro mercado vamos a considerar el activo S y otro activo / (por ejemplo |
| 114 | Tomamos Nt como numerario. El modelo ser´a certiﬁcado si el proceso Zt = St/Nt es / martingala. / Es decir, si la evoluci´on de Zt no tiene deriva. Usando el lema de Itˆo, tenemos |
| 115 | ¡Vaya! Simpliﬁquemos un poco. Digamos el numerario es la cuenta bancaria con / rentabilidad r(t), donde r(t) es una cierta funci´on: / dNt = r(t) Nt dt , |
| 116 | Digamos que el instrumento C paga una cierta funci´on C(ST). La regla de evoluci´on / anterior nos dice que ST es una variable aleatoria con cierta funci´on de densidad fST / (que, con suert |
| 117 | O mejor: aquella que valora consistentemente calls y puts de distintos plazos y strikes. / Obs´ervese que esto supone ampliar nuestro mercado de activos b´asicos, incluyendo en / ´el las cal |
| 118 | 8. Ap´endice: complementos |
| 119 | A1. Ejemplos adicionales de valoraci´on por replicaci´on / (P´agina 35 y alrededores) / 1. Call/put binaria. |
| 120 | A vencimiento T , los ﬂujos del contrato anterior son / A recibir´a el pago acordado al principio, que escribimos como 100(1 + KT ); / y deber´a pagar el precio de la acci´on ST = 100(1 + Re |
| 121 | A vencimiento T , la cartera paga / Equity Swap / Acci´on |
| 122 | Ejercicio / Intercambio de rentabilidades. La acci´on de Telef´onica vale hoy X0, y la de Endesa Y0. Se ﬁrma un contrato entre A y / B por el que, a vencimiento T , |
| 123 | A2. Sobre mercados incompletos / (P´agina 73 y alrededores). / Cotas para precios |
| 124 | Ilustraci´on / ¿C´omo se implementar´ıa este procedimiento para los datos del ejemplo de la p´agina 75? / Opci´on 2. Cotas con probabilidades. Obs´ervese que, ﬁjado un numerario N y una prob |
| 125 | A3. Ejemplos adicionales de modelaci´on / (P´agina 90 y alrededores) / Planteamos a continuaci´on un par de situaciones en las que vamos a aplicar la tecnolog´ıa vista hasta el |
| 126 | Probabilidad impl´ıcita. Calls binarias / Datos / Subyacente S, cuyo valor hoy es S0 = 100. |
| 127 | Activos b´asicos / • El activo b´asico sin riesgo, la cuenta bancaria CB, que vale 1 en t = 0 y valdr´a, en t = 1 y en / cualquier escenario, er. Ser´a nuestro numerario. |
| 128 | Replicaci´on / El modelo de mercado es completo: / ................................................................................................... |
| 129 | As´ı que s´olo nos quedar´ıan las tres siguientes ecuaciones: / C1 −→ / c1 |
| 130 | c3 −c2 ≥0 se invierte a plazo (inversi´on inicial de 0). En T = 1 tendr´ıamos 1 + er (c3 −c2) si el / subyacente acaba entre K2 y K3, y er (c3 −c2) en otro caso. / La f´ormula de valoraci´on |
| 131 | Modelo (Bernoulli) de dos estados / ´Este es el modelo m´as simple. Aqu´ı Ω contempla tan s´olo dos escenarios: / Ω = {ωup, ωdown} . |
| 132 | Caso 1: cuenta bancaria como numerario / La condici´on de no arbitraje equivale a que existan pu y pd (ambos positivos y que suman 1), que deﬁnen / una probabilidad P sobre Ω de manera que |
| 133 | Observaci´on / Si tomamos como numerario N a la cuenta bancaria, / que en tiempo 0 vale 1; |
| 134 | Observaci´on / Otro caso habitual es aquel en el que tomamos como numerario N el bono cup´on cero de nominal 1 que vence en / tiempo t = 1. De nuevo suponemos que N es uno de los activos b´a |
| 135 | Caso 2: subyacente como numerario / Si los valores de S en t = 0 y t = 1 son positivos, podemos usar como numerario a S. Hay / una probabilidad de valoraci´on Q (respecto de N = S) dada por  |
| 136 | Caso 3: otro numerario / De igual modo (suponiendo S siempre positivo), podr´ıamos tomar como numerario N la cartera que / invierte 100 repartido a partes iguales entre CB y S: |
| 137 | Ejercicio / Tenemos un modelo de cuatro estados ω1, ω2, ω3, ω4 y cuatro activos. Uno (el activo S1 es la cuenta bancaria, dos / (el segundo y el tercero) est´an positivamente correlados entr |
| 138 | A4. Procesos de ganancia y no arbitraje / a) Proceso de valor y de ganancia de una inversi´on / Para una cartera de inversi´on λ = (λ1, . . . , λM), su proceso de valor normalizado es |
| 139 | La ganancia de la cartera λ (en t´erminos del numerario N) es la variable Gλ deﬁnida en tiempo t = 1 / por / Gλ(ωj) = V 1 |
| 140 | b) No arbitraje, probabilidad de valoraci´on y ganancia / Seleccionamos un numerario N. Recordemos que un numerario N es simplemente un activo b´asico o una / cartera de inversi´on en los ac |
| 141 | Observaci´on / Demostraci´on del lema 1. En un sentido, si hay una oportunidad de arbitraje, la ganancia de esa inversi´on / cumplir´a la condici´on se˜nalada. |
| 142 | A5. Teorema fundamental de valoraci´on / Son equivalentes: / i) no hay oportunidades de arbitraje; |
| 143 | Demostraci´on. / II) ⇒III). Evidente. / III) ⇒I), Supongamos que Q es probabilidad de valoraci´on (respecto de un numerario N) Si una cartera |
| 144 | I) ⇒II). La colecci´on G de vectores de ganancia de las distintas estrategias constituyen un subespacio / vectorial de RN. Como, por hip´otesis, no hay oportunidades de arbitraje, ha de cump |
| 145 | Entonces (teorema de separaci´on), existe un vector ⃗ν tal que / N / j=1 |
| 146 | Observaci´on / Teoremas de separaci´on (Minkowski). Siempre en RN. / a) Compacto K y convexo C. |
| 147 | Observaci´on / b) Compacto K y subespacio L. / Si K ∩L = ∅, existe una formal lineal f en RN y constante β > 0 tal que f(⃗k) ≥β, para todo ⃗k ∈K y |
| 148 | A6. Sobre numerarios y probabilidades de valoraci´on / a) Por qu´e la probabilidad de valoraci´on hace innecesario el c´alculo de la replicaci´on / Tenemos un modelo matricial, un numerario  |
| 149 | resultantes para obtener: / N / j=1 |
| 150 | permiten escribir el valor hoy de X como suma ponderada: / X0 = / N |
| 151 | Entonces, si decidi´eramos usar Z escribir´ıamos: / S0 / i |
| 152 | A7. Probabilidad de valoraci´on ´unica / Un modelo de mercado es completo y sin ausencia de oportunidad de arbitraje si y solo si para cada / numerario existe una ´unica probabilidad de valo |
| 153 | Comprobamos ahora que si ε es peque˜no entonces Qε es probabilidad de valoraci´on respecto de N: / Si ε es peque˜no, entonces los pesos de Qε son positivos: Qε(ωj) > 0 para j = 1, 2, . . . , |
| 154 | A8. Algunos ejemplos generales de valoraci´on / En ocasiones, no hace falta especiﬁcar el modelo para valorar un instrumento. O mejor, cualquier modelo / certiﬁcado debe asignar el mismo pre |
| 155 | ejemplo 2. Activo replicable est´aticamente (independiente del modelo) / En realidad, si un activo es replicable est´aticamente con activos b´asicos, su valoraci´on no debe depender / del mo |
| 156 | ejemplo 3. Liquidar a mercado no altera el valor de la inversi´on (¡faltar´ıa m´as!) / Tenemos una estrategia de inversi´on din´amica y autoﬁnanciada en activos b´asicos. Fijados N y Q, si / |
| 157 | Ejercicio / Consideremos la situaci´on en la que tenemos una acci´on S(t) (no paga dividendos) y el bono B(t) cup´on cero de / principal 1 que vence en tiempo T . Comp´arense: |
| 158 | Gracias |

# PDF-003: MFC-26-valoracion-arboles_Teoria.pdf

[Original](../../raw/fundamentos/mfc-26-valoracion-arboles-teoria.pdf) · [Texto por páginas](../extracciones/pdf-003-mfc-26-valoracion-arboles-teoria.md) · [Mapa del curso](../MAPA_RELACIONES.md)

Páginas PDF: **102**. Las referencias usan la página física del PDF, no el número del nombre de un Excel.

## Contenido y navegación

| Páginas | Bloque |
|---|---|
| 1–3 | Introducción e índice |
| 4–31 | Modelo binomial, calibración, JR y CRR |
| 32–44 | Europeas, Monte Carlo, path dependence y barreras |
| 45–53 | Americanas y Arrow–Debreu |
| 54–60 | Replicación y cobertura |
| 61–73 | Dividendos y futuros |
| 74–83 | Estructura temporal de tipos y volatilidades |
| 84–101 | Árboles de tipos, BDT, FRA y caplets |
| 102–102 | Cierre |

## Relaciones con los ejercicios

- **Jarrow–Rudd: árbol, simulación, valoración y réplica**: [XLS-005](../fuentes/xls-005-plantilla-3-solucion1.md), [XLS-006](../fuentes/xls-006-plantilla-3.md)
- **Dividendos discretos y ejercicio americano**: [XLS-009](../fuentes/xls-009-americana-con-dividendos.md)
- **Árbol de precios de Arrow–Debreu**: [XLS-010](../fuentes/xls-010-arbol-arrow-debreu.md)
- **Árbol recombinante con curva de volatilidad**: [XLS-011](../fuentes/xls-011-arbol-volas-no-ctes.md)
- **Calibración Black–Derman–Toy y derivados de tipos**: [XLS-012](../fuentes/xls-012-bdt.md)

## Cómo interpretarlo

Este documento aporta teoría y ejemplos de clase. Las relaciones de navegación no convierten automáticamente esos ejemplos en soluciones del encargo. Las fórmulas fundamentales se han reescrito en los [conceptos](../conceptos/README.md) para evitar depender del orden de glifos de una extracción PDF.

El nombre del archivo sitúa el material en el curso 2026, pero varias páginas conservan referencias internas a 2021–2022. Se preservan tal cual; no se ha supuesto una actualización de su contenido.

## Índice de todas las páginas

Los títulos siguientes son extractos breves para recuperación. El texto completo queda en la extracción.

| Página | Inicio de contenido |
|---:|---|
| 1 | Máster Executive Finanzas Cuantitativas / Valoración: / Modelos Discretos |
| 2 | ´Indice / 1. Modelos binomiales / El modelo binomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . |
| 3 | 1. Modelos binomiales |
| 4 | Vamos a construir un modelo discreto (en tiempo y valores) de evoluci´on de la cotizaci´on / de un subyacente, que ser´a libre de arbitraje y que nos permitir´a valorar activos derivados / ( |
| 5 | El modelo presenta algunas ventajas: / se implementa de manera sencilla en un ´arbol binario; / la condici´on de no arbitraje en el modelo se traduce en una condici´on sencilla (local, |
| 6 | El modelo binomial / Tiempos / Fijamos de partida una unidad de tiempo Δt. Con N saltos de Δt tenemos 1 a˜no: |
| 7 | Numerario / La cuenta bancaria ser´a nuestro numerario. / Datos de mercado |
| 8 | Evoluci´on de los activos b´asicos / Postulamos la siguiente evoluci´on de los activos b´asicos: / la cuenta bancaria vale 1 hoy, vale eRΔt en tiempo Δt, e2RΔt en tiempo 2Δt, etc.: |
| 9 | Implementaci´on en ´arboles binarios / Es c´omodo representar los posibles valores del subyacente en un ´arbol binario como el / que sigue: |
| 10 | Observaciones: / →N´otese que el ´arbol se recombina: / S |
| 11 | Descripci´on matem´atica / La descripci´on matem´atica de la estructura anterior es como sigue: / Tenemos unos instantes de tiempo 0, Δt, 2Δt, . . . . Usaremos el sub´ındice j para |
| 12 | Tenemos una probabilidad P deﬁnida sobre cada uno de estos escenarios ω, que / viene dada por la asignaci´on de probabilidad p a “subir” y probabilidad 1 −p a / “bajar” (m´as la independenci |
| 13 | La ﬁltraci´on Fj = σ(Y1, . . . , Yj) recoge la informaci´on desvelada hasta tiempo jΔt. / Los activos b´asicos son la cuenta bancaria, que en tiempo jΔt vale / βj = ejRΔt , |
| 14 | Distribuci´on de probabilidad a vencimiento del subyacente / Miramos hasta tiempo MΔt. / Hay 2M posibles evoluciones del subyacente, cada una con su propia probabilidad. |
| 15 | Simulaci´on en el ´arbol / Como veremos, para ciertos an´alisis y valoraciones resultar´a conveniente simular el / proceso de sucesivos precios del activo directamente. |
| 16 | Probabilidad de valoraci´on / Queremos que nuestro modelo de evoluci´on sea certiﬁcado. / Numerario |
| 17 | Observaci´on / detalle: / EP |
| 18 | Observaci´on / La probabilidad p es “riesgo-neutro”, aquella para la / que la capitalizaci´on promediada del activo subyacente es |
| 19 | Valoraci´on de activos (replicables) / Si ahora C es un activo replicable (con activo y dinero), entonces su proceso de precios / en t´erminos del numerario (es decir, descontado) ser´a tamb |
| 20 | Calibraci´on del modelo / Tenemos tres datos de mercado: el tipo R, la cotizaci´on inicial S0 y la volatilidad anual / del activo σ. |
| 21 | Estos rendimientos parciales son / ln /  Sj |
| 22 | Y como NΔt = 1, obtenemos la segunda ecuaci´on: / (ajuste al dato de volatilidad) / σ |
| 23 | En resumen, dados los datos de mercado R, S0 y σ, podemos construir un modelo de / evoluci´on (de paso Δt) / libre de arbitraje (certiﬁcado); |
| 24 | Especiﬁcaci´on de Jarrow–Rudd / Para empezar ﬁjamos / p = 50 % |
| 25 | Observaci´on / • Basta exponenciar la segunda ecuaci´on y resolver el sistema de ecuaciones resultante. / • Recu´erdese que |
| 26 | ejemplo base / Datos de mercado / ⎧ |
| 27 | Separando deriva de ruido / La construcci´on anterior es r´apida y directa. Pero, como preparaci´on para versiones m´as / generales del ´arbol (con tipos/volatilidades no constantes), vamos  |
| 28 | Aparte, calculamos la parte determinista que, para los nodos del paso j, se acumula / hasta: / deriva por tipos |
| 29 | Otras especiﬁcaciones / La ventaja de los ´arboles de Jarrow–Rudd es, justamente, la elecci´on de p = 1/2. Esto / los hace especialmente ﬂexibles. En particular, se pueden adaptar bastante b |
| 30 | ´Arboles de Cox–Ross–Rubinstein / Para empezar ﬁjamos / d = 1 |
| 31 | ejemplo base / Datos de mercado / ⎧ |
| 32 | 2. Valoraci´on de derivados |
| 33 | Vamos a valorar, en un modelo binomial, derivados de cuatro tipos diferentes: / Opciones europeas, cuyo pago s´olo depende de la cotizaci´on del subyacente a / vencimiento. Las podremos valo |
| 34 | Valoraci´on de opciones europeas / Valorar un derivado con un modelo binomial consiste en calcular un valor medio, / esperanza, de los ﬂujos potenciales de ese instrumento. El c´alculo de es |
| 35 | M´etodo 1. Valoraci´on con f´ormula / Hay M + 1 posibles pagos de la opci´on, tantos como posibles valores del subyacente a / vencimiento (v´ease la p´agina 14). Aplicamos directamente la f´ |
| 36 | En el caso de la call con strike K, los ﬂujos son /  / S0ukdM−k −K |
| 37 | Observaci´on / Pasando al l´ımite N →∞, o lo que es lo mismo, haciendo que Δt tienda a cero, obtenemos la f´ormula de / Black–Scholes: |
| 38 | M´etodo 2. Valoraci´on en el ´arbol / Se trata de interpretar la condici´on / EP |
| 39 | M´etodo 3. Simulaci´on / Una manera alternativa de utilizar la f´ormula / C0 = e−MRΔt EP(CM) |
| 40 | Valoraci´on de derivados path-dependent / Tenemos un instrumento C que paga, a vencimiento MΔt, una cierta cantidad / f(S1, S2, . . . , SM) |
| 41 | En una opci´on usual, calculamos el ﬂujo a partir de los nodos del ´ultimo nivel y / procedemos hacia atr´as en el ´arbol. Pero ahora, aunque el activo en dos per´ıodos / alcanza tres valore |
| 42 | Valoraci´on de opciones con barrera / Veremos ahora c´omo valorar opciones con barrera usando ´arboles. Las opciones con / barrera m´as simples tiene f´ormulas cerradas, pero s´olo las m´as  |
| 43 | Podemos incorporar estos datos al ´arbol. Los pagos a vencimiento o extinci´on de la / opci´on son los siguientes: / Y ahora procedemos hacia atr´as en el ´arbol. Rellenamos los valores del  |
| 44 | Observaci´on / Este procedimiento puede ser muy sensible a la ubicaci´on de, por ejemplo, la barrera. / Hemos obtenido la valoraci´on: Call(K = 84, B = 100) = 1.3266. |
| 45 | Valoraci´on de opciones americanas / Decisi´on y ejercicio anticipado / Ejemplo. Sabemos que se van a recibir 10 ofertas para comprar un bien que poseemos. |
| 46 | Obs´ervese que en media cada una de las ofertas tiene valor 0.5, y podr´ıa parecer, a / primera vista, que el valor es de 0.5. Pero, no, sabemos (intuimos) que recibir una serie / de sucesiv |
| 47 | ser 0.5. ¿Y el valor? Ser´a mayor que 0.5, porque si rechazamos nos quedamos con / algo que hemos valorado en 0.5. El c´alculo preciso es el siguiente: / V2 = E (F2\|F2 ≥0.5) · P (F2 ≥0.5) +  |
| 48 | 0,25 / 0,5 / 0,75 |
| 49 | Valoraci´on de opciones americanas en el ´arbol / En las opciones americanas, el poseedor de la opci´on tiene el derecho de ejercerla en / cualquier momento entre el comienzo del contrato y  |
| 50 | De manera que / Vn(Sn) = m´ax / ⎧ |
| 51 | Call americana vs. call europea / En principio, las opciones americanas han de ser m´as valiosas que las correspondientes / europeas. Pero la call americana (sobre un subyacente que no repar |
| 52 | ´Arbol de precios de Arrow-Debreu / El ´arbol de precios de Arrow-Debreu es muy ´util en la implementaci´on num´erica de / esquemas de valoraci´on. |
| 53 | Una vez calculado el ´arbol de precios de Arrow-Debreu, basta con determinar los ﬂujos / del instrumento en cada nodo (en el que haya ﬂujo) y multiplicar ese ﬂujo por el precio / Arrow-Debre |
| 54 | Replicaci´on/cobertura / En las p´aginas anteriores hemos conseguido valorar una gran cantidad de derivados / utilizando la probabilidad de valoraci´on bajo un numerario. |
| 55 | Replicaci´on/cobertura en un solo periodo / Partimos de la situaci´on general: / eRΔt |
| 56 | Cobertura / Resolviendo el sistema de ecuaciones anterior, deducimos que el activo C equivale a la / cartera que consta de β unidades de subyacente, donde |
| 57 | Eliminaci´on del riesgo / Otro punto de vista de la valoraci´on es la eliminaci´on del riesgo. / Comenzamos con el activo (derivado) C y buscamos formar una cartera con el propio |
| 58 | Cobertura din´amica / El precio del derivado es la cantidad de que se precisa para formar una cartera de / subyacente y dinero, que de manera autoﬁnanciada y con reajuste en cuanto a la |
| 59 | En tiempo Δt. Para la cobertura ocurren dos cosas: / Primero. Cambia la cotizaci´on del subyacente. ´Este pasa a ser S1. Y la situaci´on de / la cartera es |
| 60 | Ilustraci´on / Obtener los ´arboles de replicaci´on de una opci´on europea. En el primero, en cada nodo aparece la cantidad de dinero, y / en el segundo la cantidad de acciones. |
| 61 | Dividendos y futuros / La inclusi´on de los dividendos en el modelo binomial es algo delicada. Analizaremos dos / casos: cuando interpretamos que recibimos una tasa continua de dividendos, y |
| 62 | A m´as plazo, desde tiempo 0 hasta Mdt, / S0 / −→ |
| 63 | Buscamos α y β para que la cartera de precio α + βS0 replique los pagos de la opci´on: /  / Cu = αeRΔt + β(S0u eQΔt) |
| 64 | Se trata de la f´ormula habitual, en la que hemos cambiado R por R −Q. Aunque, / ¡atenci´on!, en las valoraciones seguiremos descontando con R. / En el caso Jarrow–Rudd, las dos ecuaciones q |
| 65 | Observaci´on / Esto da, al pasar al caso continuo, que el precio del activo en tiempo T , ST , y bajo riesgo neutro satisface que / ST = S0e[(R−Q)−σ2/2]T +σ |
| 66 | Dividendos ﬁjos / Supongamos que en tiempo T recibiremos un / ´unico dividendo conocido D (por acci´on). |
| 67 | Dividendos en el esquema binomial de un paso / Supongamos que el dividendo D se paga en tiempo Δt/3. La cotizaci´on hoy es / S0 = S∗ |
| 68 | Obs´ervese que las β acciones, tras tiempo Δt, dan lugar a / o bien βS∗ / 0u, o bien βS∗ |
| 69 | Buscamos primero p tal que / pu + (1 −p)d = eRΔt . / ¡Atenci´on!, esto har´a que el ´arbol de S∗ |
| 70 | Implementaci´on en el ´arbol binomial / Supongamos que se van a recibir dos / dividendos (conocidos hoy), D1 y D2, |
| 71 | Procedimiento: / 1. Con los valores de R y σ se determinan los valores de los par´ametros u, d y p. / 2. Con el valor S∗ |
| 72 | Futuros / Consideremos ahora el caso de una opci´on C cuyo subyacente sea un futuro F. / Planteamos el esquema habitual para el argumento de replicaci´on: |
| 73 | Valoraci´on con probabilidades / La condici´on de no arbitraje es que el promedio de los ﬂujos (descontados) en tiempo Δt / sea el precio hoy (que es 0). Es decir, |
| 74 | 3. ´Arbol consistente con la estructura / temporal de tipos y volatilidades |
| 75 | Pretendemos ahora construir un ´arbol de evoluci´on del subyacente (libre de arbitraje y / que arranque en S0), pero que adem´as sea consistente / con una curva de tipos (spot, por ejemplo)  |
| 76 | Ajustando a la curva de tipos / Supongamos que tenemos un dato de volatilidad constante σ y los tipos forward / (continuos) Rj para cada uno de los periodos de tiempo j Δt hasta (j + 1) Δt. |
| 77 | Ajustando a la curva de volatilidades / Partimos de una asignaci´on de volatilidad para cada vencimiento T, por ejemplo, la / media ponderada de las volatilidades impl´ıcitas para distintos  |
| 78 | Pero si el ´arbol no se recombina, entonces el n´umero de nodos crece exponencialmente / con el n´umero de pasos del ´arbol, y el esquema num´erico es intratable. / En los dos esquemas sigui |
| 79 | Ajuste del ´arbol a la curva de volatilidades / Construiremos el ´arbol casi como en el caso general (de Jarrow–Rudd), pero para poder / captar la estructura de volatilidad y para que, adem´ |
| 80 | Procedemos en etapas: / Etapa 1 / Fijamos una unidad de volatilidad A. Para ello, decidimos cu´antos pasos N tendr´a el |
| 81 | Etapa 3 / Buscamos ahora la serie de tiempos / T1, T2, . . . , TN |
| 82 | Etapa 4 / Calculamos las derivas que corresponden a los nodos de tiempo Tj, y que resultan ser: / deriva por tipos −→eTjR(Tj) , |
| 83 | Ilustraci´on / Disponemos de la curva cup´on cero y de una curva de volatilidades spot. / Construir el ´arbol de Jarrow–Rudd consistente con esta informaci´on. |
| 84 | 4. Construcci´on de un modelo discreto / de tipos |
| 85 | Vamos a prescribir una evoluci´on aleatoria en el tiempo de tipos de inter´es. El tiempo / estar´a discretizado y representaremos los posibles estados con un ´arbol binomial. / Queremos que  |
| 86 | Denotamos3 por Rk al tipo (continuo, anual) a plazo Δt que tenemos en tiempo kΔt. / En nuestro esquema binomial, Rk es aleatorio, y toma k + 1 valores, uno en cada nodo. / tiempo 0 |
| 87 | Elecci´on de numerario / Supongamos que ya tenemos construido el ´arbol con los valores de los tipos (m´as / adelante propondremos un esquema para parametrizar esos valores). |
| 88 | Por ejemplo, para tiempo 2 tenemos / trayectoria ω2 / trayectoria ω3 |
| 89 | Metodolog´ıa de valoraci´on / Instrumentos de mercado / Los instrumentos que vamos a considerar como “de mercado” son los bonos cup´on cero |
| 90 | No arbitraje / Siguiendo nuestra idea general de valoraci´on por no arbitraje, pretendemos que el proceso / que da cuenta, en cada tiempo k, del precio (descontado con la cuenta bancaria) de |
| 91 | Valoraci´on / Si se cumpliera (⋆), entonces, aplic´andola reiteradamente obtendr´ıamos el precio hoy / del bono cup´on cero de vencimiento T: |
| 92 | No arbitraje, ya en el ´arbol / Parece que (⋆) es una condici´on muy aparatosa, dado que todas las cantidades / involucradas dependen de las trayectorias seguidas. |
| 93 | En esta f´ormula, cuando escribimos nodo up (o nodo down, o inicial), estamos conside- / rando no s´olo el nodo en el que estamos (y el tiempo al que corresponde), sino tambi´en / “c´omo” he |
| 94 | Simplemente hay que observar que sabemos que el bono que vence / en tiempo T vale justamente 1 en todos los nodos de tiempo T. / Digamos, por ejemplo, que el ´arbol de valores de tipos empie |
| 95 | ¡Atenci´on!, los precios as´ı obtenidos son los que proporciona / el ´arbol de valores de los tipos; / junto con la hip´otesis de no arbitraje. |
| 96 | Esquema Black-Derman-Toy / Postulamos una evoluci´on lognormal de los tipos, an´aloga a los esquemas tipo Black– / Scholes. Digamos que tenemos, como datos, |
| 97 | La especiﬁcaci´on del valor de R(k, j) es directa: / R(k, j) = U(k) ej / √ |
| 98 | La curva cup´on cero en cada nodo / En este marco de incertidumbre que hemos ido construyendo s´olo hay una variable de / estado, el tipo a plazo Δt (por ejemplo, 3 meses). |
| 99 | Algunos ejemplos de valoraci´on / Rama variable de un FRA / En tiempo k se ﬁja el tipo (atenci´on, simple), que denotamos por Rs(k). El payoﬀdel |
| 100 | Versi´on “in arrears” / En el caso anterior, el precio debe coincidir con la diferencia de precios entre los / bonos de tiempos k + 1 y k. Esto es, es independiente de σ. Y, de hecho, del mo |
| 101 | Replicaci´on / Las valoraciones que proporciona el modelo est´an basadas en la hip´otesis de no arbitraje / y, por tanto, en argumentos de replicaci´on. |
| 102 | Gracias |

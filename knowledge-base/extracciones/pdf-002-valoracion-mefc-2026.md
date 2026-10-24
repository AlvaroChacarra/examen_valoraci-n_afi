# PDF-002: Valoracion MEFC 2026.pdf

Original: [archivo raw](../../raw/encargo/valoracion-mefc-2026.pdf). SHA-256: `1366027affc9a0a4ec236c96418921641ef55a7489b69f7b951561275a620bdb`.

Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.

## Página 1

Máster Executive en Finanzas Cuantitativas 2026 
Entregable de fundamentos de valoración 
Profesores: José Javier Calderón Coronado 
  José María Contreras Beltrán 
Entregables 
Se deberá elaborar una memoria explicativa que contendrá: 
• 
Los desarrollos teóricos de los ejercicios que lo requieran 
• 
Explicación, comentarios, resúmenes, gráficas, etc., sobre los ejercicios 
resueltos mediante hojas de cálculo 
Se subirán al campus del curso: 
• 
El archivo que contenga la memoria (preferiblemente pdf) 
• 
Junto con todas las hojas de cálculo creadas en el trabajo. Estas hojas 
deberán estar convenientemente identificadas (en función del ejercicio a que 
se refieran) 
El trabajo se realizará en grupos de entre 4 y 6 personas, presentando un único 
entregable por grupo. 
La defensa por vídeo será a nivel individual.

## Página 2

Ejercicio 1. El objetivo de este ejercicio es valorar una opción bermuda mediante el 
modelo binomial de Jarrow-Rudd. 
Como arranque del ejercicio, tendrás que construir un árbol de Jarrow-Rudd para la 
evolución riesgo-neutro del subyacente con horizonte de 3 años y paso mensual. Los datos 
son los siguientes: 
𝑆0 = 50, 𝑟= 2.1% 𝑦 𝜎1 = 37.5%, 𝜎2 = 42.5%, 𝜎3 = 39%. 
 
Donde 𝜎1 hace referencia a la volatilidad durante el primer año, 𝜎2 volatilidad para el 
segundo año y 𝜎3 para el tercer año. El subyacente no reparte dividendos. 
El derivado de interés es una put bermuda de strike 𝐾= 45 y con fechas de derecho de 
ejercicio en 1 año, 2 años y entre el 2 años y 3 años de forma mensual. Por supuesto, a 
vencimiento también se dispone de dicho derecho de ejercicio. En esta opción sólo se 
puede ejercer en las catorce fechas señaladas. 
a) Calcula la prima de la opción con el árbol, y compárala con las correspondientes 
primas de la put europea y la americana. ¿Tiene sentido el resultado optenido? 
 
b) Si transcurre medio mes (15 días naturales) y todos los datos de mercados se 
mantienen constante, excepto el spot, el cual sufre un movimiento ascendente hasta 
el nivel de 52.5, ¿Cuál de las tres opciones (europea, bermuda o americana) 
hubieses preferido tener en tu cartera? Indica el motivo respaldado en algún dato 
cuantitativo. 
 
c) Volviendo al escenario incial (t=0), simula sendas del subyacente, construye la 
cartera de réplica correspondiete y comprueba si hay cobertura perfecta. Estima, por 
simulación, la probabilidad de ejercer en el primer instante de posible ejercicio (1 
año) y en el último (vencimiento). 
 
d) La valoración de opciones bermudas mediante modelos discretos es dependiente 
del número de pasos (delta t) empleado en su implementación. Mejora el resultado 
de valoración de la opción bermuda sin incrementar el número de pasos empleados 
en dicha valoración.

## Página 3

Ejercicio 2. Para tiempos 𝑇 y 𝑇 + ∆𝑇, llamamos 𝑅(𝑇, 𝑇 + ∆𝑇) al Euribor a plazo ∆𝑇 que 
se observa en tiempo 𝑇. Fijamos un strike 𝐾 y un nominal 𝑁𝑜𝑚, y consideramos los 
instrumentos: 
• 
(fra in arrears) el instrumento que paga, en tiempo 𝑇, la cantidad 
𝑁𝑜𝑚 · ∆𝑇 · (𝑅(𝑇, 𝑇 + ∆𝑇) − 𝐾), 
• 
(caplet in arrears) el instrumento que paga, en tiempo 𝑇, la cantidad 
𝑁𝑜𝑚 · ∆𝑇 · (𝑅(𝑇, 𝑇 + ∆𝑇) − 𝐾)+ 
Observa que los pagos no se producen en la fecha “natural”, 𝑇 + ∆𝑇. Se pide obtener 
fórmulas de valoración para ambos instrumentos suponiendo que la dinámica del forward 
para el periodo 𝑇 → 𝑇 + ∆𝑇 sigue una martingala normal con una cierta volatilidad 𝜎𝑛. 
Observaciones: 
• 
El caso lognormal está resuelto en detalle en la documentación del curso. 
• 
Suponemos que estamos en el entorno de una única curva (niveles de tipos 
implícitos se obtienen de los propios factores de descuento).

## Página 4

Ejercicio 3. Construir un modelo para valorar forwards y opciones (usuales y quanto) 
sobre una acción cotizada en dólares. 
Para ello, se pide completar el desarrollo de la presentación adjunta (la entrega de este 
documento puede hacerse por ppt o en cualquier otro formato). 
--(+1 punto extra)-- 
Valorar (en Excel) a fecha 31/03/2026 el producto que se detalla a continuación: 
max(50% · Δ𝐵𝑎𝑠𝑘𝑒𝑡; 0) 
Donde: 
Δ𝐵𝑎𝑠𝑘𝑒𝑡= 1
2 ∑Δ𝐼𝑛𝑑𝑒𝑥𝑗
2
𝑗=1
 
Donde: 
Δ𝐼𝑛𝑑𝑒𝑥𝑗= 1
12 ∑(
𝐼𝑛𝑑𝑒𝑥𝑗
𝑖
𝐼𝑛𝑑𝑒𝑥𝑗
0 −1)
12
𝑖=1
 
𝐼𝑛𝑑𝑒𝑥𝑗
𝑖 es el precio de cierre de cada mes del año 2027, siendo 𝐼𝑛𝑑𝑒𝑥𝑗
0 el precio de 
cierre del 31 de diciembre de 2026. 
Además: 
• 
𝐼𝑛𝑑𝑒𝑥1= EURO STOXX 50® Index (SX5E) 
• 
𝐼𝑛𝑑𝑒𝑥2= Standard & Poor’s 500 Index (SPX) 
Datos: 
• 
𝑆𝑋5𝐸= 4930€ 
• 
𝑆𝑃𝑋= 5100 $ 
• 
𝑟$ = 2% 
• 
𝑟€ = 3% 
• 
𝐹𝑋0 = 0.84
𝑒𝑢𝑟𝑜𝑠
𝑑ó𝑙𝑎𝑟𝑒𝑠 
• 
𝜎𝑆𝑋5𝐸= 23% 
• 
𝜎𝑆𝑃𝑋= 25% 
• 
𝜎𝐹𝑋= 7% 
• 
Matriz de correlaciones: 40%, excepto la diagonal (que es 100%) 
Resolver este problema mediante simulación. 
¿Cómo afecta la correlación en la valoración? Gráficas.

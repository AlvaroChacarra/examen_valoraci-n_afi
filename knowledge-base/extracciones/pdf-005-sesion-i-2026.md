# PDF-005: Sesion_I_2026.pdf

Original: [archivo raw](../../raw/fundamentos/sesion-i-2026.pdf). SHA-256: `92982aa8f31c79e14ce0068de70fdc7f47daef38db7c0d07315049c866262a34`.

Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.

## Página 1

Valoración: 
Fundamentos
Máster Executive Finanzas Cuantitativas
José María Contreras
Septiembre 2026

## Página 2

Pie de página
2
0. Plan y Resumen
1. Paradigmas de valoración
2. Valoración por replicación
3. Modelo matricial de un solo periodo de tiempo: planteamiento
•
Escenarios, activos, carteras
•
Replicación
•
Oportunidades de arbitraje
4. Modelo matricial de un solo periodo de tiempo: valoración
•
Probabilidad de valoración
•
Mercados completos/mercados incompletos
5. Modelo de varios periodos de tiempo: planteamiento
6. Modelo de varios periodos de tiempo: valoración
7. Modelos continuos
8. Apéndice: complementos
Índice

## Página 3

Pie de página
3
Plan y resumen
00.

## Página 4

4
Plan y resumen
Objetivo:
Se pretende dar un marco general de modelos estocásticos que permiten 
valorar a mercado (por replicación) instrumentos derivados.

## Página 5

5
Plan y resumen
Ingredientes:
•
Activos básicos
•
Numerario
•
Escenarios de evolución

## Página 6

6
Plan y resumen
Ingredientes:
•
Activos básicos
Sj en los que podemos invertir (comprar y vender) y que 
constituyen el mercado subyacente.
Acciones, Bonos, Cuenta Bancaria, etc.

## Página 7

7
Plan y resumen
Ingredientes:
•
Numerario
Es un activo básico que se toma como referencia que 
cumple cierta propiedad.

## Página 8

8
Plan y resumen
Ingredientes:
•
Escenarios de evolución
Sj(t) de los activos en el tiempo. 
Evolución que podrá ser discreta (lanzamiento de moneda por 
ejemplo) o evoluciones continuas (descritas por un proceso de 
Itô por ejemplo),

## Página 9

9
Plan y resumen
Requisitos Financieros para que un modelo sea 
“certificado”:
•
Libre de oportunidad de arbitraje
•
Consistente con el mercado
Comestible

## Página 10

10
Plan y resumen
Requisitos Financieros para que un modelo sea “certificado”:
•
Libre de oportunidad de arbitraje
No existe posibilidad de construir estrategias en las que sin 
asumir riesgo se obtenga o se pueda obtener beneficios

## Página 11

11
Plan y resumen
Requisitos Financieros para que un modelo sea “certificado”:
•
Consistente con el mercado
Basado (calibrado) con precios de mercado.

## Página 12

12
Plan y resumen
Requisitos:
•
Libre de oportunidad de arbitraje
•
Consistente con el mercado
¿Cómo conseguimos esto?

## Página 13

13
Plan y resumen
¿Cómo conseguimos esto en modelización matemática?
¿Martingala?
¿Cómo sabemos si un proceso de Itô es martingala?

## Página 14

14
Plan y resumen
Si estos instrumentos vencen en tiempo T y llamamos X a sus flujos, entonces la 
valoración vendrá dada, simplemente, por
Valorar = Cálculo de esperanza (del payoff,descontado)

## Página 15

15
Plan y resumen
Activos 
básicos (t = 
0) = valor de 
mercado
Una
probabilidad
de valoración
Un 
numerario
El modelo permitirá “valorar” de manera 
eficiente y consistente con el mercado los
instrumentos derivados replicables con 
activos básicos.
Modelo que 
dispone de:

## Página 16

16
Plan y resumen
Discretos
con solo un 
periodo de 
tiempo
Discretos
con varios
periodos de 
tiempo
Continuos
1
3
2
Valoración por replicación:

## Página 17

Pie de página
17
Paradigmas de 
valoración
01.

## Página 18

18
Paradigmas de valoración
1.
¿Instrumento financiero?
2.
¿Valorar?

## Página 19

19
Paradigmas de valoración
1.
¿Instrumento financiero?
2.
¿Valorar?
t0
ts
¿€?

## Página 20

20
Paradigmas de valoración
Puntos a tener en cuenta en la valoración:
1.
Valor temporal del dinero (FD(t))
2.
Flujos (cuantía y fecha de liquidación y sus posibles incertidumbres).

## Página 21

21
Paradigmas de valoración
Flujos Ciertos
El instrumento paga cantidades conocidas:
En fechas conocidas:
La valoración del producto es:

## Página 22

22
Paradigmas de valoración
Flujos Ciertos
tn
t0
fn
f3
f2
f1
t3
t2
t1

## Página 23

23
Paradigmas de valoración
Flujos Ciertos
 
            
 
    ??
Valor de un bono cupón cero, que paga 1 EUR en tj
tj
t0
1€

## Página 24

24
Paradigmas de valoración
Valoración de lo cierto
¿Cómo replicamos los flujos futuros?
Comprando:
Si el precio del instrumento no fuera el valor determinado más arriba, entonces 
(en principio) se podría arbitrar.

## Página 25

25
Paradigmas de valoración
Valoración de lo cierto
¿Cuánto vale la cartera réplica?

## Página 26

26
Paradigmas de valoración
Valoración de lo incierto
 
Ingredientes:
• Las cosas que pueden ocurrir (incertidumbre)
Escenarios
• Los Flujos del contrato que vamos a valorar y sus respectivos FD.
Flujos y 
Descuentos
• Cuan probable es que ocurra cada escenario.
Probabilidades

## Página 27

27
Paradigmas de valoración
Ejemplo:
Lanzamos una moneda. 
Escenarios: Cara o Cruz
Flujos: Si sale cara Pago 100 y si sale Cruz gano 50.
¿Entráis?

## Página 28

28
Paradigmas de valoración
Ejemplo:
Lanzamos una moneda. 
Escenarios: Cara o Cruz
Flujos: Si sale cara Pago 100 y si sale Cruz gano 50.
¿Qué tipo de moneda es?¿Quién la elige? Es decir, ¿con qué probabilidad sale 
cara?

## Página 29

29
Paradigmas de valoración
Valoración de lo incierto
 
Ingredientes:
• Futuro potencial completo en el que se recoge una posible evolución de las variables de las que 
dependen los flujos del instrumento.
• Discrecionalidad en decision de qué eventos futuros se tienen en cuenta.
Escenarios
• Flujos: el montante que se recibirá o pagará en cada escenario concreto.
• Descuento: que se ha de aplicar a ese flujo. Se trata del descuento por efecto del valor temporal del 
dinero.
• Ambos dependen del escenario. 
Flujos y 
Descuentos
• Probabilidad de un escenario es la frecuencia (relativa) con la que puede ocurrir.
• La suma de estas probabilidades sobre todos los escenarios posibles ha de ser 100%.
• Criterio experto, acontecido historia, Mercado. 
Probabilidades

## Página 30

30
Paradigmas de valoración
Valoración de lo incierto
 
Ingredientes:
En suma, tendremos una asignación
El esquema de valoración usual asigna, como valor del instrumento, el valor 
medio (valor esperado, esperanza) de los flujos descontados ponderados con las 
probabilidades asignadas:

## Página 31

31
Paradigmas de valoración
Valoración de lo incierto
       Paradigma de valoración actuarial:
Buena información
estadísitica de la 
frecuencia con la 
que cada escenario
ha ocurrido
El entorno se 
mantiene
Se puede entender
que la frecuencia
del pasado es
válida para el 
futuro.

## Página 32

32
Paradigmas de valoración
Valoración de lo incierto
 
Paradigmas:
Este esquema de valoración se fundamenta en las leyes de los grandes números, 
es decir, en la repetición del experimento aleatorio en cuestión.
Veamos esto en detalle:

## Página 33

33
Paradigmas de valoración
Valoración de lo incierto
 
Paradigmas:
Digamos que las variables aleatorias X1, . . . , XN codifican:
•
Los premios obtenidos en sucesivas partidas de un juego de azar,
•
o los pagos a N mutualistas por los siniestros sufridos durante el próximo año,
•
o los impagos de los préstamos de una cartera hipotecaria, etc.
Interesa la variable aleatoria que registra el premio tras N partidas (o el pago total 
a los mutualistas, o el número de defaults en la cartera, etc.):

## Página 34

34
Paradigmas de valoración
Valoración de lo incierto
 
Paradigmas:
Hipótesis:
•
Si las variables Xi son idénticas (tienen la misma distribución que una X de 
referencia), entonces:
(Partidas se juegan en igualdad de condiciones, mutualistas/hipotecados que son 
clientes “homogéneos”, etc.)
•
Pero si, además, las variables son independientes (basta con que sean 
incorreladas), entonces las leyes de los grandes números nos dicen que, si N es 
grande,

## Página 35

35
Paradigmas de valoración
Valoración de lo incierto
 
Paradigmas:
•
Es decir, los pagos individuales son aleatorios, pero al agregarse son “casi 
ciertos”.
•
Lo que, traducido en valoración, nos dice que recibir los flujos aleatorios YN de 
un número grande de partidas es equivalente (con probabilidad elevada y 
aproximadamente) a recibir por partida la cantidad fija E(X), el valor medio de 
los flujos.

## Página 36

36
Paradigmas de valoración
Valoración de lo incierto
 
Paradigmas:
•
Aún más, el teorema del límite central permite cuantificar cómo de probable es 
que YN se aleje de la cantidad NE(X). Por ejemplo, permite calcular 
(aproximadamente) cantidades como P(|YN − NE(X)| > a) sin necesidad de 
conocer la distribución concreta de YN (bastan la media y la desviación típica 
de las Xj): si N es grande (con variables independientes e idénticas),

## Página 37

37
Paradigmas de valoración
Valoración de lo incierto

## Página 38

38
Paradigmas de valoración
Valoración de lo incierto
Si: 
•
Se sabe de manera objetiva que los flujos de un instrumento (juego) son 
aleatorios,
•
se conoce con precisión la distribución de probabilidad de los resultados,
•
y vamos a invertir en él un número grande de veces en condiciones idénticas 
(jugar muchas partidas):
Entonces (y solo entonces) la esperanza es un equivalente (casi cierto) de los 
flujos futuros.

## Página 39

39
Paradigmas de valoración
Valoración de lo incierto
 
CUIDADO!!
Pero digamos ahora que tenemos un único contrato. Por simplificar, supongamos 
que hay una única fecha de pago y que el flujo del instrumento es f.
Disponemos de largas series de datos históricos anteriores valores de f, en las que 
observamos que f paga 10 en el 50% de los casos, 3 en el 30% de las ocasiones y 
−1 en el restante 20 %. La tentación (y el pecado) consiste en calcular
valor hoy = 10 × 50% + 3 × 30% + (−1) × 20% = 5.7 .
¿Qué sentido tiene esto? Esta “esperanza” no se justifica por las leyes de los 
grandes números (que no son de aplicación en esta situación). No hay un 
“equivalente cierto”.
En la valoración de derivados financieros: se aplicará la valoración por 
replicación.

## Página 40

Pie de página
40
Valoración por 
replicación
02.

## Página 41

41
Parábola de la porra
Supongamos que sólo hay dos resultados (por ejemplo, una final de Copa): 
•
victoria de X
•
victoria de Y. 
Cada apuesta es de 1 euro.
Disponemos de la siguiente información:
Datos históricos: victoria de X = 40%; victoria de Y = 60 %.
Nuestra opinión experta: victoria de X = 20%; victoria de Y = 80 %.
El mercado (hay, hasta el momento, 1 millón de apuestas):
victoria de X = 30%; victoria de Y = 70 %.
La decisión de apostar por un equipo ya recoge toda la información.

## Página 42

42
Parábola de la porra
Mecanismo de la porra.
Apostar por X supone que
•
su precio es 1; no hay descuento; los pagos son;
Análogamente, cada apuesta por Y paga 10/7 en caso de victoria de Y, y 0 en caso 
contrario.
¿Cuánto vale el derivado?

## Página 43

43
Parábola de la porra

## Página 44

44
Parábola de la porra
¿Cuál es la correcta?

## Página 45

45
Parábola de la porra
¿Cuál es la correcta?

## Página 46

46
Parábola de la porra

## Página 47

47
Parábola de la porra
Conclusión

## Página 48

48
Valoración a mercado
•
Los “mercados” dan ya precio a una gran variedad de instrumentos
•
Por supuesto, lo que ya está en mercado no hace falta valorarlo a mercado
•
Lo que pretenderemos será valorar instrumentos OTC “como si estuvieran 
en el mercado”.

## Página 49

49
Replicación/arbitraje/valoración (relativa)
Mercado
Arbitraje

## Página 50

50
Replicación/arbitraje/valoración (relativa)
Replicación
Paradigma de valoración relativa (o por no arbitraje)
Hipótesis: Ausencia oportunidad de arbitraje

## Página 51

51
Replicación/arbitraje/valoración (relativa)

## Página 52

52
Replicación/arbitraje/valoración (relativa)

## Página 53

53
Ilustraciones Valoración por Replicación 
Estática

## Página 54

54
Ilustraciones Valoración por Replicación 
Estática

## Página 55

55
Ilustraciones Valoración por Replicación 
Estática

## Página 56

56
Ilustraciones Valoración por Replicación 
Estática

## Página 57

57
Ilustraciones Valoración por Replicación 
Estática

## Página 58

58
Ilustraciones Valoración por Replicación 
Estática

## Página 59

Pie de página
59
Modelo matricial de 
un sólo periodo de 
tiempo:
planteamiento
03.

## Página 60

60
Escenarios. Tiempos e incertidumbre

## Página 61

61
Escenarios. Tiempos e incertidumbre

## Página 62

62
Activos
Activos Básicos

## Página 63

63
Activos
Activos Básicos

## Página 64

64
Activos
Activos Básicos

## Página 65

65
Excel: Plantilla 1

## Página 66

66
Replicación con activos básicos

## Página 67

67
Replicación con activos básicos

## Página 68

68
Activos
Activos Básicos (Ejemplo):

## Página 69

69
Activos
Activos Generales:
Activos Generales (Ejemplo):

## Página 70

70
Replicación con activos básicos
Ejemplo

## Página 71

71
Activos
Activos Especiales

## Página 72

72
Carteras
Carteras de activos básicos y de activos generales

## Página 73

73
Oportunidades de Arbitraje

## Página 74

74
Oportunidades de Arbitraje

## Página 75

75
Carteras
Numerarios

## Página 76

76
Carteras
Numerarios

## Página 77

Pie de página
77
Modelo matricial de 
un sólo periodo de 
tiempo:
Valoración
04.

## Página 78

78
Probabilidad
Probabilidad de valoración con respecto a un numerario

## Página 79

79
Probabilidad

## Página 80

80
Probabilidad
Cálculo de una probabilidad de valoración

## Página 81

81
Probabilidad

## Página 82

82
Probabilidad

## Página 83

83
Probabilidad

## Página 84

84
Probabilidad

## Página 85

85
Cambio de Numerario

## Página 86

86
Cambio de Numerario

## Página 87

87
Mercados Completos

## Página 88

88
Mercados Completos / No Completos
¿Qué ocurre si disponemos de solo 3 activos en el 
ejemplo?¿Y si se dispone de 5 activos?

## Página 89

89
Mercados No Completos. Activos no 
replicables. Cotas

## Página 90

90
Mercados No Completos. Activos no 
replicables. Cotas

## Página 91

91
Mercados No Completos. Activos no 
replicables. Cotas

## Página 92

92
Mercados No Completos. Activos no 
replicables. Cotas

## Página 93

Pie de página
93
Modelo de varios 
periodos:
Planteamiento
05.

## Página 94

94
Evoluciones en el tiempo: no arbitraje y 
martingalas

## Página 95

95
Evoluciones en el tiempo

## Página 96

96
Evoluciones en el tiempo
Ejemplo Base

## Página 97

97
Evoluciones en el tiempo

## Página 98

98
Evoluciones en el tiempo
Ejemplo Base

## Página 99

99
Evoluciones en el tiempo

## Página 100

100
Evoluciones en el tiempo
Ejemplo Base

## Página 101

101
Evoluciones en el tiempo: Estrategias

## Página 102

102
Evoluciones en el tiempo: Estrategias

## Página 103

103
Evoluciones en el tiempo: Activos 
Replicables

## Página 104

104
Cartera Replicantes

## Página 105

105
Cartera Replicantes

## Página 106

106
Cartera Replicantes

## Página 107

Pie de página
107
Modelo de varios 
periodos:
Valoración
06.

## Página 108

108
Valoración por Replicación

## Página 109

109
Valoración con probabilidades
Numerario
Probabilidad de Valoración

## Página 110

110
Valoración con probabilidades

## Página 111

111
Valoración con probabilidades
Detalle

## Página 112

112
Valoración con probabilidades
Probabilidad de valoración y no arbitraje

## Página 113

113
Cálculo de una probabilidad de valoración

## Página 114

114
Cálculo de una probabilidad de valoración

## Página 115

115
Cálculo de una probabilidad de valoración
Valoración de activos replicables

## Página 116

116
Cálculo de una probabilidad de valoración

## Página 117

117
Cambio de Numerario

## Página 118

118
Cambio de Numerario

## Página 119

Pie de página
119
Modelo Continuos:
Valoración
07.

## Página 120

120
Modelos Continuos

## Página 121

121
Modelos Continuos

## Página 122

122
Modelos Continuos

## Página 123

123
Modelos Continuos

## Página 124

124
Ausencia de oportunidades de arbitraje y 
valoración

## Página 125

125
¿Por qué libre de arbitraje?

## Página 126

126
Valoración de lo replicable

## Página 127

127
Valoración de lo replicable

## Página 128

128
Notas adicionales

## Página 129

129
Guía de construcción de modelos (continuos)

## Página 130

130
Guía de construcción de modelos (continuos)

## Página 131

131
Guía de construcción de modelos (continuos)

## Página 132

132
Guía de construcción de modelos (continuos)

## Página 133

133
Guía de construcción de modelos (continuos)

## Página 134

134
Guía de construcción de modelos (continuos)

## Página 135

135
Guía de construcción de modelos (continuos)

## Página 136

Pie de página
136
Apéndice: 
Complementos
08.

## Página 137

137
Véase para más detalle 
Documentación teórica del 
Curso

## Página 138

Gracias

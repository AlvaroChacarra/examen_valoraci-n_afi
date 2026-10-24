# Encargo de valoración: contrato y rutas de lectura

Estado: **pendiente de resolver**. Esta base organiza el material recibido; las soluciones de clase no son una entrega nueva del trabajo.

Fuentes vinculantes: PDF-002 (enunciado), PPT-001 (desarrollo del ejercicio 3), PDF-001 (entrega y defensa). Los tres originales están en `raw/encargo/`; sus textos completos y fichas se localizan en el [catálogo](../CATALOGO.md).

La [segunda revisión de preparación](../REVISION_PREPARACION.md) certifica el alcance documental y reúne decisiones y pruebas que deben cerrarse al resolver.

## Ejercicio 1: put bermuda con Jarrow–Rudd

| Dato | Valor |
|---|---|
| S0 | 50 |
| K | 45 |
| T | 3 años |
| Paso | Mensual: 36 pasos |
| r | 2,1% |
| Volatilidad año 1 / 2 / 3 | 37,5% / 42,5% / 39% |
| Dividendos | No paga |
| Ejercicio bermuda | Meses 12, 24 y 25–36: 14 fechas |

Tareas exigidas:

1. Valorar europea, bermuda y americana equivalentes y explicar el orden de precios.
2. Revalorar tras 15 días naturales con S=52,5 y los otros datos de mercado constantes. Comparar resultados económicos y justificar cuál habría convenido tener.
3. Simular el subyacente, construir la réplica y comprobar cobertura. Estimar probabilidad de ejercicio al año y a vencimiento.
4. Mejorar la valoración bermuda sin aumentar pasos.

### Lectura dirigida

- JR y valor hacia atrás: PDF-003 pp. 24–39; XLS-005/006.
- Ejercicio temprano: PDF-003 pp. 45–51; PDF-006 pp. 40–45; XLS-009.
- Réplica: PDF-003 pp. 54–60; XLS-005 y, como contraste de hedge continuo discretizado, XLS-013/018.
- Volatilidad no constante: PDF-003 pp. 74–83; XLS-011.
- Mejora numérica: PDF-006 pp. 51–53 propone Black–Scholes en los nodos del penúltimo instante.
- [Conceptos de árboles](../conceptos/arboles.md).

### Decisiones que habrá que documentar al resolver

Las volatilidades del encargo son por periodo anual; XLS-011 usa volatilidades spot y varianzas acumuladas. Su malla uniforme en varianza cambia fechas, mientras el encargo exige paso mensual y fechas de ejercicio concretas. Hay que elegir y justificar una implementación que respete ese contrato, sin imponer recombinación incorrectamente.

Para el escenario de 15 días hay que mantener las fechas contractuales, acortar correctamente los intervalos hasta ellas y explicitar la base temporal elegida. Para las probabilidades de ejercicio se usa la política óptima y se detiene cada senda al primer ejercicio; aclarar si son incondicionales o condicionadas a supervivencia. El enunciado no fija el número de simulaciones ni una semilla.

## Ejercicio 2: FRA y caplet in arrears normales

Definir U=T+delta y R=R(T,U). Los pagos se producen en T:

- FRA: `Nom delta(R-K)`.
- Caplet: `Nom delta max(R-K,0)`.

Se piden fórmulas teóricas en una sola curva, con el forward como martingala normal de volatilidad absoluta sigma_n.

### Lectura dirigida

1. Medida forward y pago usual: PDF-008 pp. 5–13; XLS-024/031.
2. Derivación in arrears lognormal: PDF-008 pp. 14–19; XLS-025/033.
3. Bachelier y escala normal: PDF-009 pp. 38–40; XLS-037/038/045/046.
4. [Tipos](../conceptos/tipos.md) y [normal/multicurva](../conceptos/normal-multicurva.md).

La estructura del argumento de pago temprano se reutiliza, pero hay que sustituir los momentos lognormales por los normales y desarrollar el momento truncado del caplet. No se han producido aquí las fórmulas finales del ejercicio evaluable. El entorno multicurva de otras hojas aporta contexto, pero el encargo fija una sola curva.

## Ejercicio 3: acción en dólares, valoración en euros

Completar el PPT o desarrollar su contenido en otro formato. El documento pide dinámicas de martingalas, relación con los observables S y FX, aplicación de Itô, distribuciones y valoraciones usuales/quanto.

| Diapositivas | Desarrollo requerido |
|---|---|
| 11–12 | Dinámicas y soluciones de M,N; diccionario con FX,S |
| 13–17 | Derivas de FX,S y desarrollos de Itô; fórmulas explícitas |
| 18–20 | Forward usual y coherencia con réplica |
| 21–22 | Forward quanto |
| 23–24 | Call quanto |
| 25 | Call usual bajo el mismo modelo, marcada +0,5 puntos |

Leer PDF-007 (equity, martingalas y numerarios), PDF-010 (FX y cuanto), XLS-042/048 (pagos y monedas) y [FX/quanto](../conceptos/fx-quanto.md). El quanto de FX del anexo no sustituye la covariación acción-FX requerida por el PPT.

## Extra: simulación de cesta, +1 punto

Valorar en Excel a 31/03/2026 un pago `max(0.5 DeltaBasket,0)`, con:

`DeltaBasket=(DeltaIndex_1+DeltaIndex_2)/2`

`DeltaIndex_j=(1/12) sum_{i=1}^{12}(Index_j,i / Index_j,0 - 1)`.

Cada observación i es el cierre mensual de 2027; el denominador es el cierre de 31/12/2026, que es futuro a la fecha de valoración.

| Parámetro | Dato del enunciado |
|---|---|
| Índices | EURO STOXX 50 SX5E y S&P 500 SPX |
| Spots | 4.930 EUR y 5.100 USD |
| Tipos USD / EUR | 2% / 3% |
| FX0 | 0,84 EUR/USD |
| Volatilidades SX5E / SPX / FX | 23% / 25% / 7% |
| Correlaciones | Todas 40%, diagonal 100% |

Simular desde valoración hasta la referencia de diciembre de 2026 y todos los cierres de 2027. Calcular medias de niveles relativos a esa referencia, no una media de retornos mensuales consecutivos. Analizar correlación con gráficas.

Base práctica: XLS-017/022 (dos activos correlacionados), XLS-014/019 (payoff y Monte Carlo), XLS-042/048 (moneda) y [métodos numéricos](../conceptos/metodos-numericos.md).

Antes de fijar un precio final, aclarar o declarar supuestos sobre moneda/nominal del pago, fecha de liquidación, dividendos y tratamiento quanto del índice en dólares. El enunciado no lo detalla completamente. También hay que definir qué correlación se varía en cada gráfica.

## Entregables y defensa

Preparar memoria explicativa, preferiblemente PDF, con desarrollos, comentarios y gráficas, junto a todas las hojas de cálculo identificadas por ejercicio. Trabajo en grupo de 4–6. El contenido es común, pero PDF-001 exige que cada alumno suba los archivos y haga una defensa individual.

Ventana: **1–8 de noviembre de 2026, hasta las 23:59**. Preparar Zoom de escritorio, grabación local y SMOWL antes del intento.

1. Iniciar grabación antes de subir el trabajo. En Zoom: cámara apagada, micrófono activo y pantalla completa compartida; SMOWL usa la cámara.
2. Subir archivos, entrar al cuestionario de un único intento, leer la pregunta y exponer.
3. Enviar y terminar el cuestionario; detener grabación de máximo 30 minutos.
4. Subir MP4 a OneDrive o Google Drive con acceso para cualquiera con el enlace y comprobarlo.
5. Enviar enlace a jcontreras@afi.es y jcalderon@afi.es, copia a jmedina@afi.es. Asunto: `MEFC_Defensa Trabajo de Valoración_Nombre Apellidos`.

El límite global de 60 minutos incluye subida del trabajo, preparación/exposición, vídeo, subida a Drive y correo. Todo debe terminar antes del plazo. La alternativa presencial requiere cita con al menos tres días de antelación según PDF-001.

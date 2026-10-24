#!/usr/bin/env python3
"""Build reviewed reading guides around traceable static source extractions."""
import collections,json,re
from pathlib import Path
from normalize_sources import ROOT,write,md

# Topic descriptions are editorial interpretations, checked against cell formulas,
# labels, embedded statements and the referenced course pages.
TOPICS=[
('ley-grandes-numeros',[1], 'Ley de los grandes números con pagos independientes', 'PDF-004 pp. 16–21; PDF-005 pp. 30–39',
 'Simular sumas de pagos iid y estimar la proporción que queda dentro de una tolerancia relativa respecto a su esperanza.',
 'Definir valores y probabilidades de X; calcular E(X) y su desviación; generar X mediante una uniforme y la tabla acumulada; sumar N pagos; repetir y comparar la desviación relativa con la tolerancia.',
 'Proporción dentro del margen y distribución de pagos agregados. Se busca entender cuándo la diversificación justifica un promedio actuarial, antes de introducir valoración por réplica.',
 'N y tolerancia son controles. Las tablas What-If y RAND guardan realizaciones, no una muestra nueva verificada.','fundamentos'),
('dependencia-diversificacion',[2], 'Correlación y límites de la diversificación','PDF-004 pp. 16–21; PDF-005 pp. 30–39',
 'Comparar la concentración de sumas de Bernoulli cuando comparten un factor normal y dejan de ser independientes.',
 'Generar una normal común y normales idiosincráticas; construir Y_i=sqrt(rho) Z_común+sqrt(1-rho) Z_i; transformar por umbral normal a Bernoulli(p); sumar; repetir y contrastar con el intervalo y la aproximación TLC.',
 'Media, desviación y proporción dentro de un intervalo. La correlación del factor normal no coincide automáticamente con la correlación de las Bernoulli.',
 'La construcción de raíz cuadrada exige 0≤rho≤1. No extrapolar esta fórmula a correlaciones negativas.','fundamentos'),
('mercado-matricial',[3,7], 'Mercado matricial: réplica, arbitraje y numerarios','PDF-004 pp. 37–76; PDF-005 pp. 59–92',
 'Usar precios actuales y flujos en cuatro escenarios para buscar arbitraje, replicar activos y calcular probabilidades de valoración.',
 'Formar la matriz de pagos; proponer pesos de cartera; comparar flujos con el activo objetivo; resolver por Solver o inversión matricial; valorar la réplica con los precios actuales; imponer ecuaciones de martingala tras elegir numerario.',
 'Pesos, coste de la réplica, errores por escenario y probabilidades por numerario. Las soluciones usan MMULT, MINVERSE y MDETERM.',
 'Una probabilidad válida debe sumar uno y ser positiva bajo los supuestos de equivalencia usados en clase. Un sistema algebraico con solución no basta.','fundamentos'),
('mercado-multiperiodo',[4,8], 'Réplica dinámica y cambio de numerario','PDF-004 pp. 77–101; PDF-005 pp. 93–118',
 'Valorar un flujo terminal en un árbol de varios periodos y demostrar que el precio coincide usando distintos numerarios.',
 'Leer los activos en cada nodo; construir carteras replicantes desde los nodos finales; calcular probabilidades condicionadas bajo S1; repetir usando S2; aplicar el cambio de numerario y comparar los precios.',
 'Carteras locales, probabilidades por nodo, precio inicial y errores de réplica. La solución explicita cuatro tareas en J10:J13.',
 'Distinguir probabilidades condicionadas por nodo de probabilidades de trayectorias. Una estrategia debe ser adaptada y autofinanciada.','fundamentos'),
('jarrow-rudd',[5,6], 'Jarrow–Rudd: árbol, simulación, valoración y réplica','PDF-003 pp. 6–60; PDF-006 pp. 4–46',
 'Construir un árbol binomial calibrado a tipo y volatilidad y comparar distintos métodos de valoración de una opción europea.',
 'Calcular u,d,p=1/2 y descuentos; construir el árbol de S; comprobar la distribución y varianza de log-retornos; simular sendas; valorar por fórmula binomial, backward induction y simulación; obtener las posiciones de réplica.',
 'Prima, comparación con Black–Scholes, árboles de cash/delta y simulación de cobertura. La solución contiene el JR con ajuste exacto de martingala mediante cosh.',
 'Plantilla de seis pasos, no solución del encargo de 36 pasos. No sustituir la especificación exacta por su aproximación exponencial sin decirlo.','arboles'),
('dividendos-americana',[9], 'Dividendos discretos y ejercicio americano','PDF-003 pp. 49–71; PDF-006 pp. 40–50',
 'Separar cotización ex-dividendo, valor de dividendos y ganancia total para valorar y cubrir una opción americana.',
 'Descontar los dividendos futuros y definir S*; construir su árbol; recomponer la cotización S y la inversión total incluyendo dividendos; simular las tres series; comparar continuación y ejercicio; formar la cartera de cobertura.',
 'Árboles de subyacente, dividendos, valor de inversión, opción y cartera. Hoja1 y Hoja2 tienen distinto grado de desarrollo.',
 'Hay errores guardados en la fuente. No interpretarlos como resultados válidos. No usar la cotización ex-dividendo como si fuera el proceso de ganancia.','arboles'),
('arrow-debreu',[10], 'Árbol de precios de Arrow–Debreu','PDF-003 pp. 52–53; PDF-006 p. 46',
 'Reutilizar precios de estado descontados para valorar una cartera con varios pagos y vencimientos.',
 'Construir el JR; inicializar el precio de estado raíz; propagar precios descontados por las dos ramas y sumar contribuciones que recombinan; formar el árbol de payoffs de dos calls y una put; sumar precio de estado por flujo.',
 'Valor de la cartera y comprobación de que la suma de precios de estado a un plazo coincide con su descuento.',
 'El archivo conserva zonas de plantilla y hojas vacías. Los precios de estado no son probabilidades sin descontar.','arboles'),
('volatilidad-temporal',[11], 'Árbol recombinante con curva de volatilidad','PDF-003 pp. 74–83; PDF-006 pp. 54–58',
 'Ajustar el árbol a una estructura temporal de tipos y volatilidades manteniendo un tamaño recombinante.',
 'Transformar volatilidad spot en varianza acumulada t sigma(t)^2; fijar un paso uniforme de varianza; invertir por interpolación la relación tiempo-varianza; interpolar los tipos en los nuevos plazos; combinar ruido, deriva de tipos y corrección cosh; valorar y cubrir.',
 'Nueva malla temporal, árbol ajustado, comprobación de volatilidad y valoración. La VBA InterPola distingue interpolación lineal y logarítmica.',
 'Este método cambia la malla de tiempo. El encargo pide paso mensual y volatilidades de cada año: no son automáticamente los mismos inputs ni las mismas fechas de ejercicio.','arboles'),
('bdt',[12], 'Calibración Black–Derman–Toy y derivados de tipos','PDF-003 pp. 84–101; PDF-006 pp. 59–72',
 'Calibrar un árbol de tipos a la curva cupón cero y usarlo para comparar flujos usuales e in arrears.',
 'Construir ruido lognormal y la función U por nivel; producir tipos cortos; valorar bonos por backward induction con descuento local; ajustar U a los descuentos de mercado mediante Solver; construir flujos de FRA y caplet; comparar fechas de pago y carteras replicantes.',
 'Errores de calibración, curva implícita, valores de FRA/caplet usuales e in arrears y réplica local.',
 'El descuento depende del nodo y de la trayectoria. Sheet1 es parcial; Sheet2 desarrolla más cálculos. Hay un error guardado en la fuente.','tipos'),
('cobertura-discreta',[13,18], 'Call Black–Scholes y error de cobertura discreta','PDF-007 pp. 18–28',
 'Medir por simulación el descasamiento entre una call y una cartera que se rebalancea con frecuencia finita, y calcular una prima con un criterio de cobertura del 95%.',
 'Valorar call, put y forward; simular S lognormal; calcular delta con plazo restante; actualizar acciones y cash autofinanciados; comparar valor final con payoff; repetir, construir histograma y estudiar el percentil del error.',
 'Distribución del descasamiento y prima necesaria para que el saldo sea positivo con probabilidad 95%, según el enunciado incrustado.',
 'El texto incrustado menciona rebalanceo mensual, pero el control guardado G28=1/50. Distinguir contrato didáctico de parametrización guardada.','equity'),
('payoff-arbitrario',[14,19], 'Payoff arbitrario: integral, Monte Carlo y descomposición','PDF-007 pp. 29–30',
 'Valorar un payoff triangular y contrastar tres procedimientos que deben representar el mismo flujo.',
 'Leer los tres cortes; implementar f(S_T); integrar contra una normal transformada a S_T; simular S_T y promediar pagos; descomponer el payoff en una call comprada, dos vendidas y otra comprada; descontar y comparar.',
 'Precio por cuadratura, por simulación y por cartera de calls. La equivalencia de la mariposa exige la relación apropiada entre los cortes.',
 'La hoja contiene una tasa de dividendos pero las fórmulas muestreadas de simulación y calls usan tipo, sin restar div. Comprobar el caso con q≠0 antes de reutilizarlo.','equity'),
('probabilidades-implicitas',[15,20], 'Distribución implícita en calls y puts','PDF-007 pp. 29–30; PDF-004 pp. 125–130',
 'Extraer una aproximación a probabilidades riesgo-neutras desde precios o volatilidades por strike y compararla con volatilidad ATM constante.',
 'Calcular precios de calls y puts para la parrilla de strikes; formar spreads de primas entre strikes vecinos; dividir por el paso para aproximar digitales; deshacer el descuento; comparar probabilidades obtenidas con smile y con vola plana.',
 'Probabilidades aproximadas por nivel, suma de masas representadas y comparación gráfica.',
 'Son probabilidades de valoración, no frecuencias históricas. La parrilla finita y la convención del spread afectan la aproximación y las colas.','equity'),
('dividendo-discreto-black',[16,21], 'Call con dividendo discreto por condicionamiento','PDF-007 pp. 31–33',
 'Valorar una call cuyo dividendo se paga antes del vencimiento, comparando condicionamiento e integración doble.',
 'Generar escenarios del spot en la fecha del dividendo; aplicar la regla ex-dividendo del archivo; valorar condicionalmente la call durante el periodo restante; integrar y descontar; contrastar con la cuadratura bivariante y con la call sin dividendos.',
 'Precio con dividendo y comparación de procedimientos. La solución añade la hoja integral doble que no está en la plantilla.',
 'La regla de dividendo cuando S es menor que D tiene ramas particulares en la fuente; no sustituirlas silenciosamente por un dividendo garantizado.','equity'),
('dos-activos',[17,22], 'Opciones sobre el máximo de dos activos','PDF-007 pp. 34–35 y 40–45',
 'Valorar max(X_T,Y_T) y max(max(X_T,Y_T)-K,0), y estudiar la influencia de la correlación.',
 'Generar normales independientes; correlacionarlas con Z2=rho Z1+sqrt(1-rho²) epsilon; transformar en dos spots lognormales; calcular el payoff; comparar Monte Carlo con integral doble; usar cambio de numerario/Margrabe cuando corresponda; variar rho.',
 'Primas por distintos métodos y tabla de sensibilidad a correlación. La fórmula I48 de la solución corresponde al máximo sin strike, no a la segunda variante.',
 'No transferir automáticamente el efecto de correlación de un máximo a una cesta promedio. El signo depende del payoff.','equity'),
('cap',[23,30], 'Cap como cartera de caplets','PDF-008 pp. 5–13',
 'Valorar un cap semestral a cinco años y analizar su sensibilidad a strike y volatilidad.',
 'Derivar forwards de la curva de descuentos; distinguir el primer flujo ya fijado; calcular Black por caplet usando tiempo de fixing y descuento de pago; sumar; variar strike y volatilidad con tablas de datos.',
 'Prima total Q20 en la solución, primas parciales y sensibilidades.',
 'No confundir fixing con pago ni volatilidad de un cap con una estructura de volatilidades caplet calibrada.','tipos'),
('caplet-floorlet',[24,31], 'Caplet, floorlet y FRA usuales','PDF-008 pp. 5–13',
 'Valorar instrumentos que comparten fixing y pago y comprobar la paridad caplet-floorlet.',
 'Obtener F0=(P(0,T)/P(0,T+delta)-1)/delta; calcular moneyness y sigma sqrt(T); obtener d+ y d-; valorar call y put sobre forward descontando al pago; comprobar que caplet-floorlet=FRA.',
 'Primas y comprobación de paridad. La solución usa E19:G19 y F20.',
 'La volatilidad Black es relativa y requiere el dominio positivo de forward y strike en la fórmula logarítmica.','tipos'),
('fra-caplet-arrears',[25,33], 'FRA y caplet in arrears lognormales','PDF-008 pp. 14–19',
 'Cuantificar el ajuste de timing al pagar en T un flujo ligado al forward del periodo que termina en T+delta.',
 'Valorar las versiones usuales; expresar el pago temprano bajo la medida T+delta usando 1/P(T,T+delta)=1+delta F_T; calcular momentos lognormales; obtener el forward corregido y su aproximación; valorar la corrección del caplet y comparar.',
 'FRA usual, forward corregido D25, prima in arrears D26 y caplet corregido D34 en la solución.',
 'El Excel desarrolla el caso lognormal. El ejercicio 2 del encargo exige normal: sirve de estructura de derivación, no de respuesta final.','tipos'),
('swap-arrears',[26,34], 'Swap usual frente a swap in arrears','PDF-008 pp. 14–19 y 21–22',
 'Construir flujos de un swap y comparar valoración ingenua y corregida de la rama in arrears.',
 'Interpolar factores de descuento; construir forwards por periodo; calcular anualidad y tipo swap par; valorar ambas ramas del swap usual; corregir los forwards de cada pago temprano; calcular el spread que equilibra el swap modificado con Solver.',
 'Valores de ramas, valor total y spread de equilibrio. La solución compara O14 (naive), P14 y Q14.',
 'VBA recuperada: interpolación. El modo 0 interpola logaritmos y el 1 niveles. Conservar la convención elegida en cada llamada.','tipos'),
('swaption',[27,35], 'Swaption payer bajo numerario anualidad','PDF-008 pp. 21–28',
 'Valorar el derecho a entrar en un swap payer comparando Black con integración normal.',
 'Construir la curva interpolada; obtener anualidad y forward swap; usar la anualidad como numerario; modelizar el swap rate lognormal; aplicar la fórmula call y compararla con la integral del payoff.',
 'Prima de swaption N24 y contraste numérico T12 en la solución.',
 'La anualidad corresponde a las fechas del swap subyacente; el tiempo de volatilidad corresponde al vencimiento de la opción.','tipos'),
('bono-cupones',[28,36], 'Cupones estructurados ligados al tipo swap','PDF-008 pp. 21–32',
 'Valorar una estructura de cupones por integración y por descomposición en instrumentos sencillos, incluyendo una versión con smile.',
 'Calcular anualidad y forward swap; identificar los tramos del cupón; integrar los pagos bajo la medida anualidad; separar pago fijo y opciones de strike distinto; aplicar Black por tramo; comparar el precio con volatilidades por strike.',
 'Valor de cupones y comparación entre integración y descomposición; fórmula de contraste AE16 en la solución.',
 'Las volatilidades distintas se asignan por strike a cada instrumento; no crean por sí solas una única distribución lognormal común.','tipos'),
('cms',[29,32], 'CMS 10 años y ajuste de convexidad','PDF-008 pp. 29–32',
 'Valorar un bono de cupones trimestrales referidos al CMS 10Y y comparar con descuento por forward swap sin ajuste.',
 'Interpolar descuentos; calcular para cada fixing la anualidad de diez años y su forward swap; aproximar la inversa de anualidad por alpha+beta S; calcular la corrección de convexidad; sumar cupones descontados y principal; variar volatilidad.',
 'Valor total corregido R6 frente al valor naive; tabla del impacto de volatilidad.',
 'El ajuste usa una aproximación de anualidad, no una fórmula exacta de CMS para cualquier curva.','tipos'),
('vola-plazos',[37,45], 'Cotizador de volatilidades por vencimiento','PDF-009 pp. 30–40',
 'Recuperar volatilidades shifted y normales que reproducen precios de caplets para una estructura de plazos.',
 'Obtener forwards y devengos desde descuentos; leer primas de mercado; valorar con shifted Black y con Bachelier; ajustar cada volatilidad a su precio; calcular deltas y comparar escalas por vencimiento.',
 'Curvas de volatilidad, errores de precio y deltas en dos convenciones.',
 'La conversión entre volatilidades se hace igualando precios. La aproximación sigma_n≈(F+shift)sigma_sh es local, no una identidad global.','normal-multicurva'),
('vola-strikes',[38,46], 'Cotizador de volatilidades por strike','PDF-009 pp. 30–40',
 'Comparar smiles de volatilidad asociados a los mismos precios bajo lognormal, shifted lognormal y normal.',
 'Leer precios y strikes; calcular precio shifted con distintos shifts; ajustar volatilidades por strike; calcular precios Bachelier y ajustar sigma normal; comparar errores y factores de escala.',
 'Sonrisas por convención y controles de reproducción de precios.',
 'El shift cambia la parametrización, no autoriza cambiar las primas de mercado objetivo.','normal-multicurva'),
('escenarios-shifted',[39,47], 'Escenarios shifted lognormal y valoración de caplet','PDF-009 pp. 30–34',
 'Visualizar tipos negativos permitidos por un desplazamiento y contrastar precio analítico con cuadratura.',
 'Construir una rejilla normal y sus pesos; transformar F_T=(F0+shift)exp(-sigma² T/2+sigma sqrt(T) Z)-shift; aplicar el payoff de caplet; integrar y descontar; comparar con shifted Black.',
 'Distribución de forward, payoff y prima por fórmula frente a cuadratura.',
 'La fórmula guardada K31 usa volash*T donde la volatilidad acumulada general exige volash*sqrt(T). Como T=1, el caso guardado puede ocultar la diferencia. No se ha corregido el original.','normal-multicurva'),
('swap-multicurva',[40,43], 'Valoración de swap con curvas distintas','PDF-009 pp. 7–16',
 'Separar curva de proyección del Euribor y curva de descuento al valorar un swap.',
 'Leer las dos curvas de Inputs; generar calendarios de fixing, inicio y fin; ajustar fechas y devengos; interpolar descuentos de proyección para calcular forwards; descontar los flujos con Eonia; sumar ambas ramas y obtener el cupón par.',
 'Valor de rama variable, fija, neto y cupón de equilibrio en Valoracion!H2:H6 en la solución.',
 'Existen llamadas externas [1]!interpol y una etiqueta EUR006M junto a una curva EUR3M. La disponibilidad de una función VBA de nombre parecido no resuelve automáticamente el vínculo externo.','normal-multicurva'),
('tipo-swap-multicurva',[41,44], 'Tipo swap par en marco multicurva','PDF-009 pp. 15–16',
 'Comparar el tipo swap calculado con proyección y descuento separados frente a usar una sola curva.',
 'Interpolar las curvas EUR3M y Eonia; obtener forwards de cada una; calcular la anualidad descontada; sumar forwards EUR3M por descuentos Eonia; dividir por anualidad; comparar con todo Eonia y todo EUR3M.',
 'Tipo swap mixto Y19 y comparaciones AB19 y AE19 en la solución.',
 'La fórmula telescópica de una sola curva no debe trasladarse sin cambios al caso multicurva.','normal-multicurva'),
('fx',[42,48], 'Forwards, opciones y pagos quanto sobre FX','PDF-010 pp. 4–21',
 'Comparar contratos sobre FX que pagan en euros o dólares y comprobar fórmulas con integración numérica.',
 'Definir FX como euros por dólar; obtener el forward desde spot y descuentos; calcular call, put y forward usuales; convertir cada payoff a euros; obtener momentos y opciones quanto; contrastar con una rejilla normal y su descuento.',
 'Primas usuales, quanto y binarias, comparadas en la cabecera Q7:X8 en la solución.',
 'Este anexo trata quanto sobre el propio FX. El ejercicio 3 añade una acción en dólares y requiere también correlación acción-FX. No confundir ambos contratos.','fx-quanto'),
]

PDF_SECTIONS={
'PDF-001':[(1,1,'Requisitos técnicos, entrega e inicio de defensa'),(2,2,'Envío del vídeo, permisos y plazo global')],
'PDF-002':[(1,1,'Entregables y grupos'),(2,2,'Ejercicio 1: bermuda JR'),(3,3,'Ejercicio 2: in arrears normal'),(4,4,'Ejercicio 3 y extra de cesta')],
'PDF-003':[(1,3,'Introducción e índice'),(4,31,'Modelo binomial, calibración, JR y CRR'),(32,44,'Europeas, Monte Carlo, path dependence y barreras'),(45,53,'Americanas y Arrow–Debreu'),(54,60,'Replicación y cobertura'),(61,73,'Dividendos y futuros'),(74,83,'Estructura temporal de tipos y volatilidades'),(84,101,'Árboles de tipos, BDT, FRA y caplets'),(102,102,'Cierre')],
'PDF-004':[(1,6,'Plan, martingalas y guía del modelo'),(7,21,'Paradigmas de valoración y grandes números'),(22,36,'Réplica estática y arbitraje'),(37,57,'Mercado matricial y numerarios'),(58,76,'Probabilidades, completitud, cambio de numerario y cotas'),(77,90,'Modelo multiperiodo y carteras dinámicas'),(91,101,'Valoración dinámica y cambio de numerario'),(102,117,'Modelos continuos y guía de construcción'),(118,122,'Apéndice A1: réplicas adicionales'),(123,124,'A2: mercados incompletos'),(125,137,'A3: modelización y probabilidades implícitas'),(138,141,'A4: procesos de ganancia'),(142,147,'A5: teorema fundamental'),(148,151,'A6: numerarios y probabilidades'),(152,153,'A7: unicidad de probabilidad'),(154,157,'A8: ejemplos generales de valoración'),(158,158,'Cierre')],
'PDF-005':[(1,16,'Resumen y modelo certificado'),(17,39,'Paradigmas y límites de la valoración actuarial'),(40,58,'Réplica estática'),(59,76,'Modelo matricial, arbitraje y numerarios'),(77,92,'Probabilidades de valoración, completitud y cotas'),(93,106,'Árbol multiperiodo y carteras'),(107,118,'Martingalas y valoración dinámica'),(119,135,'Modelo continuo y construcción'),(136,138,'Apéndice y cierre')],
'PDF-006':[(1,3,'Índice'),(4,27,'Modelo binomial, calibración y JR'),(28,39,'Europeas, path dependence, cobertura y barreras'),(40,46,'Americanas y aceleración por precios de estado'),(47,50,'Dividendos'),(51,53,'Mejora sin más pasos: Black–Scholes en el penúltimo nivel'),(54,58,'Árbol con curva de volatilidad'),(59,72,'Árbol de tipos y BDT'),(73,74,'Referencias y cierre')],
'PDF-007':[(1,10,'Marco Black, volatilidad, Black–Scholes y Margrabe'),(11,17,'Modelo equity y dinámica lognormal'),(18,23,'Autofinanciación y réplica'),(24,28,'Calls y puts con/sin dividendos'),(29,30,'Payoff europeo general'),(31,33,'Dividendo discreto'),(34,35,'Varios subyacentes'),(36,39,'Numerario bono y medida forward'),(40,45,'Numerario subyacente y opciones de intercambio'),(46,46,'Cierre')],
'PDF-008':[(1,4,'Introducción'),(5,10,'Forward Euribor y medida de pago'),(11,13,'Caplet y FRA usuales'),(14,17,'FRA in arrears y convexidad'),(18,19,'Caplet in arrears'),(20,28,'Forward swap, anualidad y swaption'),(29,32,'CMS y aproximación de convexidad'),(33,33,'Cierre')],
'PDF-009':[(1,8,'Multicurva y tipos negativos'),(9,16,'Activos, numerarios, FRA y swap multicurva'),(17,22,'Caplet/floorlet multicurva'),(23,28,'Swaption multicurva'),(29,34,'Shifted lognormal'),(35,40,'Bachelier, volatilidad normal y comparación de escalas'),(41,41,'Cierre')],
'PDF-010':[(1,5,'Convención FX y curvas'),(6,9,'Forward FX y réplica estática'),(10,17,'Calls, puts y Black FX'),(18,21,'Quanto sobre FX y binarias'),(22,22,'Cierre')],
}

def relative_doc(r,field='dossier'):return '../'+r[field].split('knowledge-base/',1)[1]

def main():
    manifest=json.loads((ROOT/'catalogo.json').read_text());sources=manifest['sources'];byid={r['id']:r for r in sources}
    topics={f'XLS-{i:03d}':t for t in TOPICS for i in t[1]}
    index=['# Catálogo de fuentes','','59 fuentes originales. Las fichas interpretativas son la entrada habitual; la extracción permite consultar ecuaciones, etiquetas y datos sin abrir los binarios. Los originales mantienen sus bytes.','','| ID | Fuente | Papel | Ficha | Extracción |','|---|---|---|---|---|']
    for r in sources:
        sid=r['id'];role='documentación'
        if sid.startswith('XLS'):
            t=topics[sid];role='plantilla' if ('plantilla' in r['original_name'].lower() and 'solucion' not in r['original_name'].lower()) else 'solución o ejemplo desarrollado'
            if r['group']=='marco-black' and 'ejercicios' in '/'.join(r['archive_chain']).lower():role='plantilla de ejercicios'
            if sid in ['XLS-009','XLS-010','XLS-011','XLS-012']:role='ejemplo con hojas de distinto grado de desarrollo'
            data=json.loads((ROOT/'metadata'/f'{sid.lower()}.json').read_text())
            lines=[f'# {sid}: {t[2]}','',f'Archivo: **{r["original_name"]}**. Papel: **{role}**.','',f'[Original](../../{r["path"]}) · [Extracción detallada]({relative_doc(r,"extraction")}) · [Mapa del curso](../MAPA_RELACIONES.md)','',
                '## Qué ejercicio plantea y qué busca','',t[4],'',t[6],'',
                '## Método observado','',t[5],'',
                '## Teoría relacionada','',t[3]+'. Véase el [catálogo](../CATALOGO.md) para abrir la ficha y consultar las páginas.','',
                '## Precaución concreta','',t[7],'',
                '## Hojas e información recuperada','','| Hoja | Estado | Rango usado | Fórmulas | Familias | Errores guardados |','|---|---|---|---:|---:|---:|']
            lines += [f'| {md(s["name"])} | {s["state"]} | `{s["dimension"]}` | {s["formulas"]} | {len(s["formula_families"])} | {len(s["cached_errors"])} |' for s in data['sheets']]
            lines+=['','## Entradas y resultados localizables','', 'Los nombres siguientes son referencias exactas del archivo. Pueden designar inputs, resultados o rangos auxiliares; el sentido lo determina el método anterior.','','| Nombre | Celda o rango |','|---|---|']
            lines += [f'| `{md(x["name"])}` | `{md(x["ref"])}` |' for x in data['names']]
            if not data['names']:lines += ['| Sin nombres definidos | Consultar etiquetas y fórmulas en la extracción |']
            lines+=['','## Cálculos representativos de este archivo','', 'Fórmulas literales con valores guardados. No son una nueva valoración; se seleccionan familias de cálculo, no filas repetidas.','']
            for s in data['sheets']:
                fs=s['formula_families']
                lines += [f'### {s["name"]}','','| Celda | Fórmula | Valor guardado |','|---|---|---|']
                # Keep first representative for each semantic formula family; full list remains in extraction.
                selected=fs[:12]+[x for x in fs[12:] if any(v in x['formula'].upper() for v in ['SUMPRODUCT','AVERAGE(','MAX(','MMULT','INTERPOL'])][:8]
                lines += [f'| `{x["first"]}` | `{md(x["formula"])}` | {md(x["cached_first"])} |' for x in selected]
                if not fs:lines+=['| — | No hay fórmulas de celda en esta hoja | — |']
            related=[byid[f'XLS-{i:03d}'] for i in t[1] if f'XLS-{i:03d}'!=sid]
            if related:lines+=['','## Plantilla / solución relacionada','']+[f'- [{x["id"]}: {x["original_name"]}]({relative_doc(x)})' for x in related]
            lines+=['','## Macros, imágenes y dependencias','',f'Proyecto VBA presente: **{data["vba"]}**. Vínculos externos declarados: **{data["external_links"]}**. Los módulos recuperados y los textos de objetos están en la extracción.','',
                'Las ecuaciones y enunciados incrustados como imágenes se recuperan por separado en [imágenes de Excel](../extracciones/imagenes-excel.md); este documento permite consultarlos sin reabrir el libro.']
            if data['vba']:
                procedures=[name for mod in data.get('vba_modules',[]) for name in re.findall(r'(?im)^\s*(?:Public |Private )?(?:Function|Sub)\s+(\w+)',mod['source'])]
                lines+=['','Procedimientos recuperados: '+', '.join('`'+x+'`' for x in procedures)+'.',
                    'La interpolación del curso busca el tramo mediante bisección. Modo 0: lineal en logaritmos del valor. Modo 1: lineal en niveles. El fuente se conserva, incluidos posibles problemas de argumentos opcionales y extrapolación.']
            broken=[x['name'] for x in data['names'] if '#REF!' in x['ref']]
            if broken:lines+=['','Nombres con referencia rota: '+', '.join('`'+x+'`' for x in broken)+'. Ver [limitaciones](../LIMITACIONES.md).']
        elif sid.startswith('PDF'):
            data=json.loads((ROOT/'metadata'/f'{sid.lower()}.json').read_text());sections=PDF_SECTIONS[sid]
            lines=[f'# {sid}: {r["original_name"]}','',f'[Original](../../{r["path"]}) · [Texto por páginas]({relative_doc(r,"extraction")}) · [Mapa del curso](../MAPA_RELACIONES.md)','',
                f'Páginas PDF: **{r["pages"]}**. Las referencias usan la página física del PDF, no el número del nombre de un Excel.','',
                '## Contenido y navegación','','| Páginas | Bloque |','|---|---|']
            lines += [f'| {a}–{b} | {title} |' for a,b,title in sections]
            lines += ['','## Relaciones con los ejercicios','']
            linked=[t for t in TOPICS if sid in t[3]]
            lines += [f'- **{t[2]}**: '+', '.join(f'[{byid[f"XLS-{i:03d}"]["id"]}]({relative_doc(byid[f"XLS-{i:03d}"])})' for i in t[1]) for t in linked]
            if sid in ['PDF-001','PDF-002']:lines+=['- Contrato del trabajo: [guía del encargo](../ejercicios/ENCARGO.md).']
            lines+=['','## Cómo interpretarlo','',
                'Este documento aporta teoría y ejemplos de clase. Las relaciones de navegación no convierten automáticamente esos ejemplos en soluciones del encargo. Las fórmulas fundamentales se han reescrito en los [conceptos](../conceptos/README.md) para evitar depender del orden de glifos de una extracción PDF.']
            if sid in ['PDF-003','PDF-004']:lines+=['','El nombre del archivo sitúa el material en el curso 2026, pero varias páginas conservan referencias internas a 2021–2022. Se preservan tal cual; no se ha supuesto una actualización de su contenido.']
            if sid=='PDF-006':lines+=['','Muchas páginas contienen capturas con fórmulas. Se ha añadido OCR al texto por páginas; los símbolos OCR requieren contraste con PDF-003 y los conceptos normalizados.']
            lines+=['','## Índice de todas las páginas','','Los títulos siguientes son extractos breves para recuperación. El texto completo queda en la extracción.','','| Página | Inicio de contenido |','|---:|---|']
            for pg in data['pages']:
                ls=[x.strip() for x in pg['text'].splitlines() if x.strip() and not x.strip().isdigit()]
                ls=[x for x in ls if not any(k in x for k in ['MFC','Valoraci´on.','derechos reservados','Pie de página','©'])]
                title=' / '.join(ls[:3])[:190] or 'Página gráfica; consultar OCR o documento original'
                lines+=[f'| {pg["page"]} | {md(title)} |']
        else:
            role='plantilla de desarrollo del encargo'
            lines=[f'# {sid}: Ejercicio 3, desarrollo Black y quanto','',f'[Original](../../{r["path"]}) · [Extracción de 25 diapositivas]({relative_doc(r,"extraction")})','',
                '## Qué hay que completar','',
                'El punto de vista es euros. Se modelizan una acción en dólares y FX en euros por dólar; se usa la cuenta bancaria en euros como numerario. Hay cuatro payoffs: forward y call usuales (pagos en dólares convertidos con FX_T), y forward y call quanto (mismo número pagado directamente en euros).','',
                '| Diapositivas | Trabajo |','|---|---|',
                '| 1–10 | Objetivo, contratos, unidades, numerario y definición de M y N |',
                '| 11–12 | Completar dinámicas y soluciones de M,N y relacionarlas con FX,S |',
                '| 13–17 | Derivar mu_F y mu_S con Itô; demostraciones 15 y 16; distribuciones explícitas |',
                '| 18–20 | Forward usual y prueba de consistencia con la réplica estática |',
                '| 21–22 | Forward quanto y desarrollo matemático |',
                '| 23–24 | Call quanto y desarrollo matemático |',
                '| 25 | Reproducir call usual en el mismo marco, marcado +0,5 puntos |','',
                '## Relación con la clase','',
                'Leer PDF-007 (equity y cambio de numerario), PDF-010 (convención FX y quanto sobre FX) y [conceptos FX/quanto](../conceptos/fx-quanto.md). El Excel FX no contiene por sí solo el modelo conjunto acción-FX.','',
                '## Estado','', 'Plantilla sin resolver. Los huecos se conservan en la extracción; no se ha presentado una solución nueva como contenido de clase.']
        write(ROOT/r['dossier'],'\n'.join(lines))
        index += [f'| {sid} | {md(r["original_name"])} | {role} | [Ficha]({r["dossier"].split("knowledge-base/")[1]}) | [Texto]({r["extraction"].split("knowledge-base/")[1]}) |']
    write(ROOT/'knowledge-base/CATALOGO.md','\n'.join(index))
    rel=['# Mapa de contenidos y relaciones','','Las relaciones son una guía de lectura revisada, no enlaces inferidos únicamente por nombres de archivo.','','## Ruta conceptual','',
         '1. Fundamentos: escenarios, flujos y numerario; réplica, arbitraje y probabilidad de valoración.',
         '2. Modelo matricial y multiperiodo: pasar de resolver una cartera estática a estrategias adaptadas y autofinanciadas.',
         '3. Árboles: materializar esas condiciones en Jarrow–Rudd, americanas, dividendos y precios de estado.',
         '4. Black equity: expresar dinámicas martingala y valorar por fórmulas, integración o simulación.',
         '5. Tipos: elegir el bono de pago o la anualidad como numerario; explicar por qué cambia la valoración al cambiar la fecha del flujo.',
         '6. Multicurva y Bachelier: separar proyección/descuento y distinguir volatilidad relativa de absoluta.',
         '7. FX y quanto: mantener moneda, unidades, correlaciones y medida de valoración consistentes.','',
         '## Teoría, práctica y uso en el encargo','','| Bloque práctico | Teoría | Archivos normalizados | Uso |','|---|---|---|']
    for t in TOPICS:
        purpose={'fundamentos':'Base común de los tres ejercicios','arboles':'Ejercicio 1','equity':'Ejercicio 3 y simulación del extra','tipos':'Ejercicio 2; CMS/swaption amplían contexto','normal-multicurva':'Normal para ejercicio 2; multicurva como contraste','fx-quanto':'Ejercicio 3 y componente extranjero del extra'}[t[8]]
        rel += [f'| {t[2]} | {t[3]} | '+', '.join(f'[{byid[f"XLS-{i:03d}"]["id"]}]({byid[f"XLS-{i:03d}"]["dossier"].split("knowledge-base/")[1]})' for i in t[1])+f' | {purpose} |']
    rel+=['','## Relaciones que evitan errores','',
          '- **JR exacto y JR aproximado:** PDF-003 pp. 24–25 los distingue. Los Excel de fundamentos usan la versión exacta.',
          '- **Volatilidad por año y spot por vencimiento:** el encargo da volatilidades de periodos; el Excel de curva trabaja con t sigma_spot(t)^2. Convertir antes de comparar.',
          '- **Réplica exacta en árbol y hedge discreto Black:** un mercado binomial de dos sucesores admite réplica local exacta; discretizar el hedge de un modelo continuo genera descasamiento.',
          '- **Pago usual e in arrears:** el activo subyacente puede ser el mismo y el numerario conveniente cambiar con la fecha de pago.',
          '- **In arrears lognormal y normal:** reutilizar el cambio de numeraire y sustituir la distribución/momentos, no copiar los resultados lognormales.',
          '- **Quanto FX y quanto equity:** el primero puede involucrar FX² al convertir un pago en dólares. El segundo exige el término de covariación entre acción y FX.',
          '- **Máximo y cesta promedio:** comparten simulación correlacionada; no necesariamente comparten el signo de sensibilidad a correlación.',
          '- **Plantilla y solución:** son versiones pedagógicas distintas; una solución del curso puede conservar errores o parámetros no alineados con el enunciado.']
    write(ROOT/'knowledge-base/MAPA_RELACIONES.md','\n'.join(rel))

if __name__=='__main__':main()

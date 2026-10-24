# Árboles binomiales, ejercicio y cobertura

Fuentes: PDF-003 completo, PDF-006. Práctica: XLS-005/006 y XLS-009–012. [Catálogo](../CATALOGO.md).

## JR exacto de clase

Con h=delta t, a=sigma sqrt(h), p=1/2 y sin dividendos:

$$u=\frac{e^{rh+a}}{\cosh(a)},\qquad d=\frac{e^{rh-a}}{\cosh(a)}.$$

Así `(u+d)/2=e^{rh}` y la desviación del log-retorno de un paso es sigma sqrt(h). PDF-003 pp. 24–25 distingue esta solución exacta de `exp((r-sigma²/2)h ± sigma sqrt(h))`, que sólo cumple aproximadamente la martingala. No mezclar probabilidades CRR con multiplicadores JR.

## Valor y ejercicio

Continuación: `C=e^{-rh}[p V_up+(1-p)V_down]`. Payoff put: `max(K-S,0)`.

- Europea: sólo payoff terminal.
- Bermuda: `V=max(payoff,C)` únicamente en fechas autorizadas; fuera de ellas, `V=C`.
- Americana del árbol: esa comparación en todos sus nodos temporales.

Con idéntico modelo y datos: `V_europea≤V_bermuda≤V_americana`. Esto compara precios; la preferencia tras un escenario exige comparar cambios de valor y definir el criterio de P&L.

## Réplica local

En un nodo sin dividendos con dos sucesores distintos:

$$\Delta=\frac{V_u-V_d}{S_u-S_d},\qquad B=e^{-rh}(V_d-\Delta S_d).$$

Comprobar `Delta S+B=V` antes del ejercicio y liquidar al ejercerse. La réplica binomial no prueba cobertura perfecta de trayectorias continuas entre nodos. Detener cada contrato en su primer ejercicio; no contar como ejercicio terminal los caminos ya ejercidos. Las probabilidades obtenidas bajo la medida del árbol son riesgo-neutras.

## Arrow–Debreu

Inicializar precio de estado raíz en 1. Cada rama propaga `precio_estado × probabilidad × descuento`; un nodo recombinado suma contribuciones de sus padres. Valorar sumando `precio_estado × flujo`. Con tipos deterministas, la suma de precios de estado a T coincide con P(0,T).

## Dividendos

El ejemplo define PD_t como valor de dividendos pendientes y `S_t=S*_t+PD_t`. La inversión total incluye los dividendos recibidos. Precisar si cada nodo es anterior o posterior al pago y qué se hace si el spot no alcanza el dividendo.

## Curva de volatilidad y recombinación

PDF-003 pp. 79–83 y XLS-011 usan `v(t)=t sigma_spot(t)^2`, fijan `n A²=v(T)` y eligen tiempos t_j con `v(t_j)=j A²`. El ruido es ±A y:

$$S_{j,k}=S_0 e^{kA}e^{t_jR(t_j)}\cosh(A)^{-j}.$$

La malla es uniforme en varianza, normalmente irregular en tiempo. Para volatilidades por periodos, integrar primero `v(t)=integral sigma(s)^2 ds`. Cambiar sigma en un árbol mensual estándar de índices up/down no conserva automáticamente la recombinación al cruzar periodos.

## Mejora sin aumentar pasos

PDF-006 pp. 51–53 propone usar Black–Scholes en el penúltimo nivel para calcular la continuación en vez de discretizar el último payoff. Si hay ejercicio en ese nivel, todavía se compara continuación con ejercicio. Adaptar la última volatilidad y el intervalo restante.

## BDT

PDF-003 pp. 84–101 y XLS-012 usan `R(k,j)=U(k)exp(j sigma sqrt(h))`, con j recorriendo los niveles de ruido. Calibrar U(k) a descuentos cupón cero. La cuenta bancaria depende de la trayectoria y se descuenta por nodo. Es útil para FRA/caplet usuales e in arrears, pero no resuelve la derivación normal del ejercicio 2.

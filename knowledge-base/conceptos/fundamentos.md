# Fundamentos: réplica, martingalas y numerarios

Fuentes: PDF-004 pp. 22–117 y apéndices; PDF-005 pp. 40–135. Práctica: XLS-003/007 y XLS-004/008. [Catálogo](../CATALOGO.md).

## Regla de valoración

Para un pago replicable X_T, un numerario positivo N y su medida Q^N:

$$V_t=N_t E^{Q^N}[X_T/N_T\mid\mathcal F_t].$$

Los activos básicos, expresados en el numerario, deben ser martingalas bajo la misma medida. Con dividendos se usa el proceso de inversión/ganancia adecuado, no la cotización ex-dividendo sin sus flujos.

## Mercado de un periodo

Si S tiene activos por filas y escenarios por columnas, una cartera lambda replica X si `lambda^T S=X`. Si S es cuadrada e invertible, `lambda^T=X S^{-1}`. Su precio es el producto de los pesos por precios actuales.

$$S_i(0)/N_0=\sum_j q_j S_i(T,\omega_j)/N_T(\omega_j),\qquad \sum_j q_j=1.$$

Comprobar positividad y las condiciones de equivalencia usadas por el modelo. En mercados incompletos puede haber varios precios consistentes para un activo no replicable; elegir una medida no lo convierte en replicable.

La búsqueda de arbitraje del ejemplo impone coste cero, flujos no negativos y una normalización de la suma de sus cuadrados a uno para excluir la cartera nula. Solver es una herramienta para encontrar la cartera, no la definición de arbitraje.

## Cambio de numerario

$$\frac{dQ^M}{dQ^N}\Big|_{\mathcal F_T}=\frac{M_T/N_T}{M_0/N_0}.$$

En el ejemplo discreto se multiplica cada probabilidad por ese cociente. Cambian los pesos probabilísticos, no el valor económico del mismo flujo.

## Varios periodos

Resolver carteras locales hacia atrás. Los pesos elegidos en t sólo usan información conocida en t. El rebalanceo se financia con la cartera existente. Multiplicar probabilidades condicionadas por nodo para obtener probabilidades de una trayectoria.

## Grandes números

XLS-001 modeliza `Y_N=sum X_i`, con esperanza `N E[X]` y varianza `N Var(X)` para independientes. XLS-002 usa `Z_i=sqrt(rho)Y+sqrt(1-rho)epsilon_i` y `X_i=1_{Z_i<Phi^{-1}(p)}`. La dependencia común puede impedir que el riesgo relativo desaparezca. La correlación normal latente no coincide necesariamente con la correlación de Bernoulli. Ese argumento actuarial no sustituye la réplica de mercado.

# Black equity y payoffs generales

Fuente: PDF-007 pp. 12–45. Práctica: XLS-013–022. [Catálogo](../CATALOGO.md).

## Dinámica y opciones

Bajo cuenta bancaria, tipos constantes r y tasa continua de dividendo q:

$$S_T=S_0\exp[(r-q-\tfrac12\sigma^2)T+\sigma\sqrt T Z].$$

$$d_\pm=\frac{\ln(S_0/K)+(r-q)T}{\sigma\sqrt T}\pm\tfrac12\sigma\sqrt T.$$

$$C=S_0e^{-qT}\Phi(d_+)-Ke^{-rT}\Phi(d_-),\qquad C-P=S_0e^{-qT}-Ke^{-rT}.$$

Delta de call: `exp(-qT)Phi(d+)`. La imagen de clase `Phi(d+)` corresponde a q=0. Distinguir el hedge continuo ideal del rebalanceo finito de XLS-013.

## Payoff general

$$V_0=e^{-rT}\int f(S_0e^{(r-q-\sigma^2/2)T+\sigma\sqrt T z})\phi(z)\,dz.$$

Comparar cuadratura, Monte Carlo y descomposición estática. El gráfico de XLS-014/019 es una mariposa: cero hasta 30, máximo en 40 y cero desde 50; corresponde a `call(30)-2call(40)+call(50)`. No ignorar q porque una implementación del ejemplo no lo use.

## Probabilidades implícitas

Las diferencias de primas entre strikes aproximan digitales; al deshacer el descuento aproximan colas o masas. En el límite suave, `-exp(rT)dC/dK` es la cola riesgo-neutra y `exp(rT)d²C/dK²` la densidad. El Excel usa diferencias finitas y compara smile de mercado con vola ATM plana. No estima frecuencias históricas.

## Dividendo discreto

Condicionar en el spot a la fecha del dividendo, aplicar la política de pago y valorar el periodo restante. Integrar ese valor y descontar. La doble integral usa las dos innovaciones de los periodos separados. XLS-016 tiene ramas particulares si S<D; no cambiarlas silenciosamente por un dividendo garantizado.

## Dos activos

Usar `Z_X=epsilon1`, `Z_Y=rho epsilon1+sqrt(1-rho²)epsilon2` y sus respectivas volatilidades y derivas. XLS-017/022 estudian `max(X_T,Y_T)` y `max(max(X_T,Y_T)-K,0)`. La fórmula I48 de la solución corresponde al primero.

Para intercambio, Margrabe usa `sigma_eff=sqrt(sigma_X²+sigma_Y²-2rho sigma_X sigma_Y)`. Con dividendos nulos y ratio de intercambio unitario:

$$V[(X_T-Y_T)^+]=X_0\Phi(d_1)-Y_0\Phi(d_2),\quad d_1=\frac{\ln(X_0/Y_0)}{\sigma_{eff}\sqrt T}+\tfrac12\sigma_{eff}\sqrt T,\quad d_2=d_1-\sigma_{eff}\sqrt T.$$

Esto no es una fórmula directa para la call de strike monetario sobre un máximo. El máximo sin strike puede relacionarse con una opción de intercambio mediante `max(X,Y)=Y+(X-Y)^+`.

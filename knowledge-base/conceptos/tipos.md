# Tipos: forward, in arrears, anualidad y CMS

Fuente: PDF-008 pp. 5–32. Práctica: XLS-023–036; apoyo discreto XLS-012. [Catálogo](../CATALOGO.md).

## Forward y fecha natural

Sea delta el devengo, T el fixing y U=T+delta el pago. En una sola curva:

$$F_0=\frac{P(0,T)/P(0,U)-1}{\delta}.$$

El forward F_t es martingala bajo Q^U, cuyo numerario es P(t,U). Con Black, `dF=sigma F dW^U`; su sigma es relativa. El FRA usual paga `Nom delta(F_T-K)` en U:

$$V_{FRA}=Nom\,\delta P(0,U)(F_0-K).$$

El caplet usual:

$$V_C=Nom\,\delta P(0,U)[F_0\Phi(d_+)-K\Phi(d_-)],\quad d_\pm=\frac{\ln(F_0/K)}{\sigma\sqrt T}\pm\tfrac12\sigma\sqrt T.$$

Floorlet: `Nom delta P(0,U)[K Phi(-d-)-F0 Phi(-d+)]`. Caplet-floorlet=FRA. Un cap es la suma de sus caplets, atendiendo al primer flujo si ya está fijado.

## Pago en T: in arrears de esta asignatura

El contrato paga en T el flujo que depende del forward de [T,U]. No introducir el denominador de liquidación de otro contrato comercial: aquí se usa exactamente el payoff del enunciado.

Bajo Q^U:

$$V_0=Nom\,P(0,U)E^{Q^U}[\delta g(F_T)(1+\delta F_T)].$$

Esto usa `1/P(T,U)=1+delta F_T` en una curva. g(F)=F-K para FRA y g(F)=(F-K)^+ para caplet. No sustituir sin justificación por `P(0,T)E^{Q^U}[delta g(F_T)]`: la medida no corresponde al nuevo descuento.

Para Black lognormal:

$$E[F_T^2]=F_0^2e^{\sigma^2T},\qquad F_{corr}=F_0\frac{1+\delta F_0e^{\sigma^2T}}{1+\delta F_0}.$$

FRA in arrears: `Nom delta P(0,T)(F_corr-K)`. Su aproximación de volatilidad pequeña es `F0[1+delta F0 sigma²T/(1+delta F0)]` para F_corr. El caplet usa además:

$$E[(F_T-K)^+F_T]=F_0^2e^{\sigma^2T}\Phi(d_*)-KF_0\Phi(d_+),\quad d_*=\frac{\ln(F_0/K)}{\sigma\sqrt T}+\tfrac32\sigma\sqrt T.$$

Sumar este momento por `Nom delta²P(0,U)` al caplet usual. El ejercicio 2 pide una distribución normal, así que estos momentos no son su respuesta.

## Swap y swaption

En una curva, para fechas t0,...,tn y devengos delta_i:

$$A_0=\sum_i\delta_iP(0,t_i),\qquad S_0=\frac{P(0,t_0)-P(0,t_n)}{A_0}.$$

Bajo numerario anualidad A, modelizar el forward swap como martingala lognormal. La swaption payer con ejercicio T tiene valor `Nom A0[S0 Phi(d+)-K Phi(d-)]`. La volatilidad se acumula hasta T, no hasta el vencimiento del swap.

## Cupones estructurados

El gráfico de XLS-028/036 define cupón h(S): 3% si S≤6%; `3%+3(S-6%)` entre 6% y 8%; 9% desde 8%. Equivalentemente:

$$h(S)=0.03+3(S-0.06)^+-3(S-0.08)^+.$$

Valorar la parte fija y cada opción por separado, con la anualidad/fechas del contrato. La versión con smile asigna volatilidad distinta a cada strike; no representa una sola lognormal con dos volatilidades simultáneas.

## CMS

Un CMS paga una sola vez el tipo swap de cierto tenor. Al usar la anualidad como numerario no se cancela su inversa. Clase aproxima `1/A_T≈alpha+beta S_T`; para plazo anual N, alpha≈1/N y:

$$\beta=\frac{1}{S_0}\left(\frac{P(0,T)}{A_0}-\alpha\right).$$

El flujo unitario de CMS vale aproximadamente:

$$P(0,T)S_0\left[1+\frac{\beta S_0}{\alpha+\beta S_0}(e^{\sigma^2T}-1)\right].$$

Multiplicar por devengo y nominal y sumar pagos del bono. La aproximación está ligada al supuesto de anualidad; no es una fórmula exacta general.

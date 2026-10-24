# FX y quanto: moneda y numerario

Fuentes: PDF-010 pp. 4–21; PDF-007 pp. 12–23 y 36–45; PPT-001 diapositivas 3–25. Práctica: XLS-042/048. [Catálogo](../CATALOGO.md).

## Convención de unidades

X_t=FX_t significa euros por dólar. Multiplicar un pago en dólares por X_t lo convierte a euros. Invertir la cotización cambia las unidades y el signo de las correlaciones pertinentes; no conservar mecánicamente un rho al invertir FX.

## Forward y opciones usuales sobre FX

$$F_{FX}(0,T)=X_0\frac{P_\$(0,T)}{P_\text{€}(0,T)}.$$

El forward de nominal Nom dólares y strike K paga en euros `Nom(X_T-K)`. Su valor es `Nom P_eur(0,T)(F_FX-K)`. La call usual:

$$C=Nom\,P_\text{€}(0,T)[F_{FX}\Phi(d_+)-K\Phi(d_-)],\quad d_\pm=\frac{\ln(F_{FX}/K)}{\sigma_X\sqrt T}\pm\tfrac12\sigma_X\sqrt T.$$

En XLS-042 se comparan también fórmulas e integración numérica. Algunos tipos de la hoja usan descuento simple; al trasladar la fórmula a tipos continuos se utilizan factores exponenciales consistentes, no se mezclan convenciones.

## Quanto del propio FX en el anexo

Un pago `Nom(X_T-K)` en dólares se convierte a `Nom X_T(X_T-K)` euros. Una call quanto del anexo requiere `X_T(X_T-K)^+`. Aparece un segundo momento como en in arrears. La binaria que paga dólares al superar K necesita también multiplicar por X_T; la que paga euros usa sólo el indicador. Son contratos distintos.

## Acción en dólares: ejercicio 3

La presentación define S_t en dólares y X_t en euros/dólar. Los cuatro pagos en euros son:

| Contrato | Flujo en euros |
|---|---|
| Forward usual | X_T(S_T-K) |
| Forward quanto con conversión fija 1 | S_T-K |
| Call usual | X_T(S_T-K)^+ |
| Call quanto con conversión fija 1 | (S_T-K)^+ |

El valor numérico en dólares se interpreta contractualmente como euros en la versión quanto; no se multiplica además por el FX observado.

Con beta_eur=exp(r_eur t), beta_dol=exp(r_dol t), la presentación exige que sean martingalas:

$$M_t=\frac{\beta_\$(t)X_t}{\beta_\text{€}(t)},\qquad N_t=\frac{e^{qt}S_tX_t}{\beta_\text{€}(t)}.$$

El factor exp(qt) incorpora reinversión de dividendos continuos. El desarrollo pendiente aplica Itô al producto S_t X_t, incluyendo su covariación, y relaciona las volatilidades de M,N con las de mercado S,X. El ajuste quanto de la acción procede de esa covariación, no de copiar la fórmula de FX² del anexo.

Comprobaciones al desarrollar el modelo: la réplica del forward usual debe dar el mismo precio que la esperanza; al anular correlación o volatilidad FX debe desaparecer el término de ajuste correspondiente. Conservar la moneda del descuento y la del payoff en cada paso.

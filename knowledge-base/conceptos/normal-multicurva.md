# Multicurva, shifted lognormal y normal

Fuente: PDF-009 pp. 7–40. Práctica: XLS-037–041 y XLS-043–047. [Catálogo](../CATALOGO.md).

## Multicurva

La curva de proyección produce forwards L_i y la curva de descuento aporta D_i. La rama variable se valora `Nom sum delta_i D_i L_i`; la fija `Nom K sum delta_i D_i`. Por tanto el tipo par es el cociente entre esas dos sumas sin Nom ni K.

La fórmula telescópica `(P(0,t0)-P(0,tn))/A0` sólo se traslada directamente al caso consistente de una misma curva. Los ejemplos comparan proyección EUR3M con descuento Eonia frente a todo Eonia o todo EUR3M. Los nombres históricos se conservan como material de clase; no representan datos actuales de mercado.

## Shifted lognormal

$$dF_t=\sigma_{sh}(F_t+sh)dW_t,\quad F_T=(F_0+sh)e^{-\sigma_{sh}^2T/2+\sigma_{sh}\sqrt T Z}-sh.$$

Su dominio es F>-sh y necesita F0+sh>0. Para strike K+sh>0:

$$C=Nom\,\delta P(0,T+\delta)[(F_0+sh)\Phi(d_+)-(K+sh)\Phi(d_-)],$$

$$d_\pm=\frac{\ln[(F_0+sh)/(K+sh)]}{\sigma_{sh}\sqrt T}\pm\tfrac12\sigma_{sh}\sqrt T.$$

La volatilidad acumulada lleva sqrt(T); la extracción de algunas diapositivas pierde raíces y fracciones. Se han reescrito aquí contrastando las imágenes de Excel y las fórmulas de celdas.

## Normal de Bachelier

$$dF_t=\sigma_n dW_t,\qquad F_T=F_0+\sigma_n\sqrt T Z.$$

sigma_n es absoluta, en unidades de tipo por raíz de año; no es una volatilidad porcentual relativa al nivel. Definir s=sigma_n sqrt(T) y d=(F0-K)/s:

$$C=Nom\,\delta P(0,T+\delta)[(F_0-K)\Phi(d)+s\phi(d)].$$

ATM: `Nom delta P(0,T+delta) s/sqrt(2pi)`. Delta frente a F0: `Nom delta P(0,T+delta)Phi(d)`.

Para el ejercicio normal in arrears, la regla de pago temprano del documento [tipos](tipos.md) conserva el factor `1+delta F_T`, pero sus momentos deben calcularse bajo esta distribución normal, no bajo Black.

## Conversión de volatilidades

XLS-037/045 calibran por plazo y XLS-038/046 por strike a las mismas primas. Sólo se comparan de forma exacta igualando precios. Aproximación ATM y de volatilidad acumulada pequeña: `sigma_n≈(F0+sh)sigma_sh`. No aplicarla como una conversión universal de toda la sonrisa.

## VBA de interpolación

Los módulos recuperados buscan el tramo mediante bisección. Modo 0 interpola log(valor); modo 1 interpola el nivel. Deben revisarse los bordes de curva y la convención de extrapolación. XLS-040/043 aún llaman a una función externa `[1]!interpol`, aunque contengan una función local de nombre parecido.

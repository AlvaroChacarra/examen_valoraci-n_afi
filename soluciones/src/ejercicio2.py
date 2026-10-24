"""Fórmulas normales formales in arrears; pago T, medida U y una curva."""
import json
from pathlib import Path
import numpy as np
from scipy.special import ndtr
from scipy.integrate import quad

def prices(f,k,variance,delta,p_u,nominal=1.):
    if variance<0 or delta<=0 or p_u<=0: raise ValueError('Dominio incorrecto')
    s=np.sqrt(variance)
    if s:
        d=(f-k)/s;phi=np.exp(-.5*d*d)/np.sqrt(2*np.pi)
        a=(f-k)*ndtr(d)+s*phi;b=(k-f)*ndtr(-d)+s*phi
        cap=(1+delta*f)*a+delta*variance*ndtr(d)
        floor=(1+delta*f)*b-delta*variance*ndtr(-d)
    else:
        cap=(1+delta*f)*max(f-k,0);floor=(1+delta*f)*max(k-f,0)
    scale=nominal*delta*p_u
    fra=(f-k)*(1+delta*f)+delta*variance
    return dict(fra=scale*fra,caplet=scale*cap,floorlet=scale*floor,
                par_strike=f+delta*variance/(1+delta*f))

def integrate(f,k,variance,delta,p_u,nominal=1.):
    # Integración del payoff original ponderado; no reutiliza momentos cerrados.
    s=np.sqrt(variance);cut=(k-f)/s
    def integrand(z,kind):
        x=f+s*z
        g={'fra':x-k,'caplet':max(x-k,0),'floorlet':max(k-x,0)}[kind]
        return g*(1+delta*x)*np.exp(-z*z/2)/np.sqrt(2*np.pi)
    out={}
    for kind in ['fra','caplet','floorlet']:
        val=sum(quad(lambda z:integrand(z,kind),a,b,epsabs=1e-13,epsrel=1e-11)[0] for a,b in [(-np.inf,cut),(cut,np.inf)])
        out[kind]=nominal*delta*p_u*val
    return out

def main():
    # Sólo ejemplo ilustrativo: NO son datos del enunciado.
    f=.03;k=.032;delta=.5;t=2.;sigma=.01;pu=np.exp(-.03*(t+delta));nom=1e6
    inputs=dict(f=f,k=k,variance=sigma*sigma*t,delta=delta,p_u=pu,nominal=nom)
    out=dict(label='Ejemplo ilustrativo, no datos del enunciado',inputs=inputs,T=t,sigma_n=sigma,closed=prices(**inputs),quadrature=integrate(**inputs))
    (Path(__file__).resolve().parents[1]/'resultados/ejercicio2.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()

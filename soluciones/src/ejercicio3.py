"""Acción USD y FX EUR/USD, ambos simulados bajo Q doméstica EUR."""
import json
from pathlib import Path
import numpy as np
from scipy.special import ndtr
from scipy.integrate import quad


def prices(s0,k,x0,rd,rf,q,ss,sx,rho,t):
    if not -1<=rho<=1 or min(ss,sx,t)<0 or min(s0,k,x0)<=0: raise ValueError('Dominio incorrecto')
    mu=rf-q-rho*ss*sx;fq=s0*np.exp(mu*t);f=s0*np.exp((rf-q)*t);D=np.exp(-rd*t)
    def call(F):
        vol=ss*np.sqrt(t)
        if vol==0:return max(F-k,0)
        d1=np.log(F/k)/vol+vol/2;d2=d1-vol
        return F*ndtr(d1)-k*ndtr(d2)
    usual=x0*np.exp(-rf*t)*call(f);quanto=D*call(fq)
    forward=x0*(s0*np.exp(-q*t)-k*np.exp(-rf*t));forwardq=D*(fq-k)
    sn=np.sqrt(sx*sx+ss*ss+2*rho*sx*ss)
    return dict(forward=forward,forward_quanto=forwardq,call=usual,call_quanto=quanto,
                put=usual-forward,put_quanto=quanto-forwardq,mu_s=mu,sigma_m=sx,sigma_n=sn,
                rho_mn=(sx+rho*ss)/sn if sn>0 and sx>0 else None)


def integrate(s0,k,x0,rd,rf,q,ss,sx,rho,t):
    # Integra payoff original condicionado en Z_S, reteniendo conversión FX terminal.
    mu=rf-q-rho*ss*sx
    def fn(z,kind):
        stock=s0*np.exp((mu-ss*ss/2)*t+ss*np.sqrt(t)*z)
        # E[X_T|Z_S=z] integra la otra normal independiente.
        ex=x0*np.exp((rd-rf-.5*sx*sx*rho*rho)*t+sx*np.sqrt(t)*rho*z)
        payoff=stock-k
        if 'call' in kind:payoff=max(payoff,0)
        elif 'put' in kind:payoff=max(-payoff,0)
        if 'quanto' not in kind:payoff*=ex
        return np.exp(-rd*t)*payoff*np.exp(-z*z/2)/np.sqrt(2*np.pi)
    cut=(np.log(k/s0)-(mu-ss*ss/2)*t)/(ss*np.sqrt(t)) if ss*t else 0.
    cuts=sorted(set([-12.,float(np.clip(cut,-12,12)),12.]))
    return {kind:sum(quad(lambda z:fn(z,kind),a,b,epsabs=1e-10,epsrel=1e-11)[0] for a,b in zip(cuts[:-1],cuts[1:])) for kind in ['forward','forward_quanto','call','call_quanto','put','put_quanto']}


def simulate(s0,k,x0,rd,rf,q,ss,sx,rho,t,n=1000000,seed=20261025):
    rng=np.random.default_rng(seed);zf,zi=rng.standard_normal((2,n));zs=rho*zf+np.sqrt(max(0.,1-rho*rho))*zi
    x=x0*np.exp((rd-rf-sx*sx/2)*t+sx*np.sqrt(t)*zf)
    s=s0*np.exp((rf-q-rho*ss*sx-ss*ss/2)*t+ss*np.sqrt(t)*zs)
    D=np.exp(-rd*t);pay=s-k
    samples=dict(forward=D*x*pay,forward_quanto=D*pay,call=D*x*np.maximum(pay,0),call_quanto=D*np.maximum(pay,0),put=D*x*np.maximum(-pay,0),put_quanto=D*np.maximum(-pay,0),M=np.exp((rf-rd)*t)*x,N=np.exp((q-rd)*t)*s*x)
    out={}
    for name,v in samples.items():
        mean=float(v.mean());se=float(v.std(ddof=1)/np.sqrt(n));out[name]=dict(mean=mean,se=se,ci95=[mean-1.959964*se,mean+1.959964*se])
    out['corr_log_mn']=float(np.corrcoef(np.log(samples['M']),np.log(samples['N']))[0,1])
    out['corr_log_sx']=float(np.corrcoef(np.log(s),np.log(x))[0,1])
    return dict(n=n,seed=seed,estimates=out)


def main():
    inputs=dict(s0=100.,k=105.,x0=.9,rd=.03,rf=.02,q=.01,ss=.25,sx=.12,rho=.4,t=2.)
    out=dict(label='Ejemplo ilustrativo, no datos del enunciado ni de la cesta',inputs=inputs,closed=prices(**inputs),quadrature=integrate(**inputs),mc=simulate(**inputs))
    (Path(__file__).resolve().parents[1]/'resultados/ejercicio3.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()

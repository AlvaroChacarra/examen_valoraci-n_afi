"""Derivación nueva: JR exacto mensual con recombinación sólo por bloque de igual a."""
from dataclasses import dataclass
from pathlib import Path
import json
import numpy as np
from scipy.special import ndtr
from scipy.signal import fftconvolve
from scipy.stats import binom

EXERCISE = {12, 24, *range(25, 37)}
R, K = .021, 45.


def bs_put(s, k, r, var, h):
    s = np.asarray(s)
    if var == 0:
        return np.maximum(k*np.exp(-r*h)-s, 0)
    z = (np.log(s/k)+r*h+.5*var)/np.sqrt(var)
    return k*np.exp(-r*h)*ndtr(-z+np.sqrt(var))-s*ndtr(-z)


@dataclass
class Layer:
    t: float
    spot: np.ndarray
    value: np.ndarray
    stop: np.ndarray
    delta: np.ndarray | None = None
    cash: np.ndarray | None = None


class Tree:
    def __init__(self, spot=50., elapsed=0., style='bermuda', smooth=False):
        self.times = np.r_[elapsed, np.arange(1,37)/12]
        if not 0 <= elapsed < 1/12:
            raise ValueError('Este escenario requiere 0<=elapsed<primer mes')
        self.h = np.diff(self.times)
        self.sigmas = np.repeat([.375, .425, .39], 12)
        self.a = self.sigmas*np.sqrt(self.h)
        # Igualdad numérica tolerada sólo para los h mensuales del mismo bloque.
        self.groups, amplitudes = [], []
        for a in self.a:
            matches = [i for i,v in enumerate(amplitudes) if abs(a-v)<1e-13]
            if not matches: amplitudes.append(a)
            self.groups.append(matches[0] if matches else len(amplitudes)-1)
        self.amplitudes = np.array(amplitudes)
        self.u = np.exp(R*self.h+self.a)/np.cosh(self.a)
        self.d = np.exp(R*self.h-self.a)/np.cosh(self.a)
        counts = np.zeros(len(amplitudes), dtype=int)
        self.layers = []
        drift=0.
        for j in range(37):
            noise = np.zeros(tuple(counts+1))
            for g, n in enumerate(counts):
                shape=[1]*len(counts); shape[g]=n+1
                noise += ((2*np.arange(n+1)-n)*amplitudes[g]).reshape(shape)
            s=spot*np.exp(drift+noise)
            self.layers.append(Layer(self.times[j], s, np.maximum(K-s,0), np.zeros(s.shape,bool)))
            if j<36:
                counts[self.groups[j]]+=1
                drift+=R*self.h[j]-np.log(np.cosh(self.a[j]))
        terminal=self.layers[-1]
        terminal.stop = terminal.spot < K  # payoff nulo: expira sin ejercicio
        self.max_local_error=0.
        self.max_budget_error=0.
        for j in range(35,-1,-1):
            l, nxt=self.layers[j:j+2]; g=self.groups[j]
            down=[slice(None)]*len(counts); up=down.copy()
            down[g]=slice(0,-1);up[g]=slice(1,None)
            vd,vu=nxt.value[tuple(down)],nxt.value[tuple(up)]
            continuation=np.exp(-R*self.h[j])*(vu+vd)/2
            if smooth and j==35:
                continuation=bs_put(l.spot,K,R,self.sigmas[j]**2*self.h[j],self.h[j])
            eligible = (style=='american' or (style=='bermuda' and j in EXERCISE))
            intrinsic=np.maximum(K-l.spot,0)
            l.stop = eligible & (intrinsic>0) & (intrinsic>continuation+1e-12)
            l.value=np.where(l.stop,intrinsic,continuation)
            # Réplica sólo para árbol puro; BS final cambia el modelo de continuación.
            l.delta=(vu-vd)/(l.spot*(self.u[j]-self.d[j]))
            l.cash=np.exp(-R*self.h[j])*(vd-l.delta*l.spot*self.d[j])
            if not smooth:
                err=np.maximum(abs(l.delta*l.spot*self.u[j]+l.cash*np.exp(R*self.h[j])-vu),abs(l.delta*l.spot*self.d[j]+l.cash*np.exp(R*self.h[j])-vd))
                self.max_local_error=max(self.max_local_error,float(err.max()))
                self.max_budget_error=max(self.max_budget_error,float(np.max(abs((l.delta*l.spot+l.cash-continuation)))))
        self.price=float(self.layers[0].value.item())

    def exact_exercise(self):
        mass=np.ones_like(self.layers[0].spot); out=[]; pv=0.
        for j,l in enumerate(self.layers):
            surviving=float(mass.sum()); stopped=mass*l.stop
            prob=float(stopped.sum());pv+=float(np.sum(stopped*np.maximum(K-l.spot,0)))*np.exp(-R*(l.t-self.times[0]))
            out.append(dict(month=j, survival=surviving, first=prob, conditional=prob/surviving if surviving else 0.))
            if j<36:
                nxt=np.zeros_like(self.layers[j+1].spot);live=mass*(~l.stop)/2;g=self.groups[j]
                dn=[slice(None)]*mass.ndim;up=dn.copy();dn[g]=slice(0,-1);up[g]=slice(1,None)
                nxt[tuple(dn)]+=live;nxt[tuple(up)]+=live;mass=nxt
            else:
                expired=float(np.sum(mass*(~l.stop)))
        return dict(by_month=out, expire_without_exercise=expired, pv=pv)

    def simulate(self, n=200000, seed=20261024):
        rng=np.random.default_rng(seed); counts=np.zeros((len(self.amplitudes),n),int)
        live=np.ones(n,bool); first=np.full(n,-1,int);wealth=np.full(n,self.price)
        cash=np.zeros(n);delta=np.zeros(n);max_error=0.;max_self=0.; examples=[]
        for j,l in enumerate(self.layers):
            ix=tuple(counts);s=l.spot[ix];v=l.value[ix]
            if j:
                wealth=delta*s+cash*np.exp(R*self.h[j-1])
                max_error=max(max_error,float(np.max(abs(wealth[live]-v[live]))) if live.any() else 0.)
            stop=live & l.stop[ix];first[stop]=j;live[stop]=False
            if j==36: break
            new_delta=l.delta[ix];new_cash=l.cash[ix]
            # El coste de rebalanceo es Δnueva*S+Bnueva - riqueza disponible.
            residual=new_delta*s+new_cash-wealth
            max_self=max(max_self,float(np.max(abs(residual[live]))) if live.any() else 0.)
            if j<36:
                examples.append(dict(month=j,spot=float(s[0]),value=float(v[0]),delta=float(new_delta[0]),cash=float(new_cash[0]),alive=bool(live[0])))
            delta=np.where(live,new_delta,0.);cash=np.where(live,wealth-new_delta*s,0.)
            counts[self.groups[j]]+=rng.integers(0,2,n)
        summary=[]
        for j in sorted(EXERCISE):
            k=int(np.sum(first==j));p=k/n;z=1.95996398454
            center=(p+z*z/(2*n))/(1+z*z/n);half=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n)
            surv=int(np.sum((first>=j)|(first==-1)))
            summary.append(dict(month=j,count=k,prob=p,ci95=[center-half,center+half],survival=surv/n,conditional=k/surv if surv else 0.))
        return dict(n=n,seed=seed,first_exercise=summary,expire_without_exercise=float(np.mean(first==-1)),max_replication_error=max_error,max_self_financing_error=max_self,path_start=examples)


def european_convolution(tree):
    # Distribución terminal por convolución de binomiales, no retroceso de valores.
    law={0.:1.}
    for g,a in enumerate(tree.amplitudes):
        n=tree.groups.count(g)
        law={x+(2*k-n)*a:p*binom.pmf(k,n,.5) for x,p in law.items() for k in range(n+1)}
    drift=sum(R*tree.h-np.log(np.cosh(tree.a)))
    return sum(p*max(K-50*np.exp(drift+x),0) for x,p in law.items())*np.exp(-3*R)


def diffusion_reference(dx, european=False, extent=8):
    # Semigrupo lognormal por convolución gaussiana en logS; sólo 14 fechas de parada.
    x=np.arange(-extent,extent+dx/2,dx);spot=50*np.exp(x);v=np.maximum(K-spot,0)
    times=[0]+[m/12 for m in sorted(EXERCISE)]
    for left,right in reversed(list(zip(times[:-1],times[1:]))):
        var=sum(sig**2*max(0.,min(right,y+1)-max(left,y)) for y,sig in enumerate([.375,.425,.39]))
        h=right-left;std=np.sqrt(var);k=int(np.ceil(9*std/dx))
        grid=np.arange(-k,k+1)*dx;kernel=np.exp(-.5*(grid/std)**2);kernel/=kernel.sum()
        padded=np.pad(v,k,mode='edge')
        conv=fftconvolve(padded,kernel,mode='same')[k:-k]
        v=np.exp(-R*h)*np.interp(x+R*h-.5*var,x,conv)
        if left>0 and not european: v=np.maximum(v,K-spot)
    return float(np.interp(0,x,v))


def main():
    out={}
    for style in ['european','bermuda','american']:
        t=Tree(style=style);later=Tree(spot=52.5,elapsed=15/365,style=style)
        out[style]=dict(initial=t.price,after15=later.price,change=later.price-t.price,financed=later.price-t.price*np.exp(R*15/365))
    tree=Tree();out['exact']=tree.exact_exercise();out['simulation']=tree.simulate()
    out['local_residual']=tree.max_local_error;out['budget_residual']=tree.max_budget_error
    out['european_convolution']=european_convolution(tree)
    out['smoothed']=Tree(smooth=True).price
    out['diffusion_references']={str(dx):diffusion_reference(dx) for dx in [.004,.002,.001,.0005,.00025]}
    out['states']=sum(l.spot.size for l in tree.layers)
    dest=Path(__file__).resolve().parents[1]/'resultados/ejercicio1.json';dest.write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k not in ['exact','simulation']},indent=2))

if __name__=='__main__':main()

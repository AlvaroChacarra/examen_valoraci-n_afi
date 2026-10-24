"""Read-only independent mathematical checks of commit 5c0e1df. No source imports for pricing."""
from functools import lru_cache
from math import exp, log, sqrt, cosh
import numpy as np
from scipy.linalg import solve_banded
from pathlib import Path
import json
r=.021;K=45.; ex={12,24,*range(25,37)}
def scalar_tree(s0=50.,elapsed=0.,style='bermuda'):
    times=[elapsed]+[j/12 for j in range(1,37)]
    dt=[times[j+1]-times[j] for j in range(36)]
    sig=[ [.375,.425,.39][j//12] for j in range(36)]
    a=[sig[j]*sqrt(dt[j]) for j in range(36)]
    groups=([0]+[1]*11+[2]*12+[3]*12) if elapsed else ([0]*12+[1]*12+[2]*12)
    ng=max(groups)+1
    amps=[next(a[j] for j in range(36) if groups[j]==g) for g in range(ng)]
    nd=[tuple(groups[:j].count(g) for g in range(ng)) for j in range(37)]
    logs=[sum(r*dt[i]-log(cosh(a[i])) for i in range(j)) for j in range(37)]
    def spot(j,k): return s0*exp(logs[j]+sum((2*k[g]-nd[j][g])*amps[g] for g in range(ng)))
    @lru_cache(None)
    def price(j,k):
        s=spot(j,k);intr=max(K-s,0.)
        if j==36:return intr
        kup=list(k);kup[groups[j]]+=1
        cont=exp(-r*dt[j])*.5*(price(j+1,k)+price(j+1,tuple(kup)))
        elig=style=='american' or (style=='bermuda' and j in ex)
        return max(intr,cont) if elig else cont
    root=(0,)*ng;val=price(0,root)
    mass={root:1.}; first={};pv=0.
    for j in range(37):
        alive={};st=0.
        for k,p in mass.items():
            s=spot(j,k);intr=max(K-s,0.)
            if j==36: stop=intr>0
            else:
                ku=list(k);ku[groups[j]]+=1
                c=exp(-r*dt[j])*.5*(price(j+1,k)+price(j+1,tuple(ku)))
                stop=(style=='american' or style=='bermuda' and j in ex) and intr>c+1e-12 and intr>0
            if stop:st+=p;pv+=p*intr*exp(-r*(times[j]-elapsed))
            elif j<36:
                ku=list(k);ku[groups[j]]+=1;ku=tuple(ku)
                alive[k]=alive.get(k,0)+p/2;alive[ku]=alive.get(ku,0)+p/2
        first[j]=st;mass=alive
    return {'price':val,'first_12':first[12],'first_36':first[36],'pv':pv,'states':price.cache_info().currsize}

def pde(dx=.001,steps_per_year=2400,european=False):
    # CN finite differences for v_tau=.5*sigma²v_xx+(r-.5*sigma²)v_x-rv.
    n=round(12/dx);dx=12/n;x=np.linspace(-6,6,n+1);s=50*np.exp(x)
    v=np.maximum(K-s,0.)
    events=[0,1,2]+[m/12 for m in range(25,37)]
    if european:events=[0,1,2,3]
    for left,right in reversed(list(zip(events[:-1],events[1:]))):
        sigma=[.375,.425,.39][min(2,int((left+right)/2))]
        alpha=.5*sigma*sigma/dx**2-(r-.5*sigma*sigma)/(2*dx)
        beta=-sigma*sigma/dx**2-r
        gamma=.5*sigma*sigma/dx**2+(r-.5*sigma*sigma)/(2*dx)
        steps=round((right-left)*steps_per_year);dt=(right-left)/steps
        # At payoff kinks apply four implicit half steps, then CN.
        mesh=[(dt/2,1.)]*4+[(dt,.5)]*(steps-2)
        now=right
        for h,theta in mesh:
            now-=h
            lnew=max(K*exp(-r*((3 if european else right)-now))-s[0],0.)
            diag=np.empty((3,n-1));diag[0,:]=-theta*h*gamma;diag[1,:]=1-theta*h*beta;diag[2,:]=-theta*h*alpha
            rhs=(1+(1-theta)*h*beta)*v[1:-1]+(1-theta)*h*(alpha*v[:-2]+gamma*v[2:])
            rhs[0]+=theta*h*alpha*lnew
            v[1:-1]=solve_banded((1,1),diag,rhs);v[0]=lnew;v[-1]=0
        if left>0 and not european:v=np.maximum(v,K-s)
    return float(np.interp(0,x,v))

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    out={'commit':'5c0e1df','scalar':{}}
    for sty in ['european','bermuda','american']:
        out['scalar'][sty]=dict(initial=scalar_tree(style=sty),after15=scalar_tree(52.5,15/365,sty))
    out['pde']={str(dx):pde(dx=dx) for dx in [.004,.002,.001,.0005]}
    out['pde_european']=pde(.001,european=True)
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

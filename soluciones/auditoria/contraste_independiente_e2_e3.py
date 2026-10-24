"""Contrastes independientes de payoff; carga exactamente el código del commit indicado."""
import argparse
import json
from pathlib import Path
import subprocess
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[2]

def prices_from_commit(commit,exercise):
    source=subprocess.check_output(['git','show',f'{commit}:soluciones/src/ejercicio{exercise}.py'],cwd=ROOT,text=True)
    namespace={'__name__':'audit_snapshot','__file__':str(ROOT/f'soluciones/src/ejercicio{exercise}.py')}
    exec(compile(source,f'{commit}:ejercicio{exercise}.py','exec'),namespace)
    return namespace['prices']

def run(commit):
    p2=prices_from_commit(commit,2);p3=prices_from_commit(commit,3)
    rng=np.random.default_rng(21731)
    maxerr2=0.;maxerr3=0.
    for _ in range(50):
        f,k=rng.uniform(-.04,.10,2);delta=rng.uniform(.05,2.);sd=rng.uniform(.001,.15);pu=rng.uniform(.6,1.1)
        a=p2(f,k,sd**2,delta,pu,1e6)
        for name,sgn,lo,hi in [('caplet',1,k,np.inf),('floorlet',-1,-np.inf,k),('fra',1,-np.inf,np.inf)]:
            val=quad(lambda x:sgn*(x-k)*(1+delta*x)*norm.pdf(x,loc=f,scale=sd),lo,hi,epsabs=1e-10,epsrel=1e-10)[0]*1e6*delta*pu
            maxerr2=max(maxerr2,abs(a[name]-val))
    for _ in range(12):
        s0=rng.uniform(30,200);k=rng.uniform(30,200);x0=rng.uniform(.5,1.5);rd,rf,q=rng.uniform(-.02,.08,3)
        ss=rng.uniform(.10,.6);sx=rng.uniform(.05,.3);rho=rng.uniform(-.9,.9);t=rng.uniform(.1,5.)
        a=p3(s0,k,x0,rd,rf,q,ss,sx,rho,t)
        mu=rf-q-rho*ss*sx;w=ss*np.sqrt(t)
        def outer(zx):
            x=x0*np.exp((rd-rf-sx*sx/2)*t+sx*np.sqrt(t)*zx)
            lo=(np.log(k/s0)-(mu-ss*ss/2)*t-w*rho*zx)/(w*np.sqrt(1-rho*rho))
            val=quad(lambda zi:max(s0*np.exp((mu-ss*ss/2)*t+w*(rho*zx+np.sqrt(1-rho*rho)*zi))-k,0)*norm.pdf(zi),max(lo,-11),11,epsabs=2e-9)[0] if lo<11 else 0.
            return np.exp(-rd*t)*x*val*norm.pdf(zx)
        val=quad(outer,-11,11,epsabs=5e-8,epsrel=2e-10)[0]
        maxerr3=max(maxerr3,abs(a['call']-val))
    assert maxerr2<1e-6
    assert maxerr3<1e-7
    return dict(commit=commit,seed=21731,E2_scenarios=50,E2_max_error_currency_nominal_1e6=float(maxerr2),E3_scenarios=12,E3_call_usual_max_error_eur=float(maxerr3),scope='Payoff integration checks; does not replace analytic audit or full test suite.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--commit',default='5c0e1df515917a57dad2a718ef30765f97c85998')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();out=run(args.commit)
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

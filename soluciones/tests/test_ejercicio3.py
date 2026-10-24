import unittest
import numpy as np
from soluciones.src.ejercicio3 import prices,integrate,simulate
class TestQuanto(unittest.TestCase):
 def setUp(self):self.p=dict(s0=100.,k=105.,x0=.9,rd=.03,rf=.02,q=.01,ss=.25,sx=.12,rho=.4,t=2.)
 def test_quadrature_and_parities(self):
  for rho in [-1.,-.4,0,.4,1.]:
   p=self.p|dict(rho=rho);a=prices(**p);b=integrate(**p)
   for key in b:self.assertAlmostEqual(a[key],b[key],places=9)
   self.assertAlmostEqual(a['call']-a['put'],a['forward'],places=12)
   self.assertAlmostEqual(a['call_quanto']-a['put_quanto'],a['forward_quanto'],places=12)
 def test_simulation_martingales(self):
  a=prices(**self.p);mc=simulate(**self.p)['estimates']
  truth=a|dict(M=.9,N=90.)
  for k in mc:
   if isinstance(mc[k],dict):self.assertLess(abs(mc[k]['mean']-truth[k]),5*mc[k]['se'])
  self.assertLess(abs(mc['corr_log_mn']-a['rho_mn']),.003)
  self.assertLess(abs(mc['corr_log_sx']-.4),.003)
 def test_limits_and_sign(self):
  p=self.p;a=prices(**p)
  # Precio usual no depende de rEUR, rho ni volatilidad FX a spot FX constante.
  b=prices(**(p|dict(rd=.08,sx=.5,rho=-.8)))
  self.assertAlmostEqual(a['call'],b['call'],places=12)
  zero=prices(**(p|dict(rho=0.)));positive=prices(**(p|dict(rho=.8)))
  self.assertLess(positive['forward_quanto'],zero['forward_quanto'])
  for changes in [dict(t=0.),dict(ss=0.),dict(sx=0.),dict(ss=.12,sx=.12,rho=-1.)]:
   x=prices(**(p|changes));y=integrate(**(p|changes))
   for key in y:self.assertAlmostEqual(x[key],y[key],places=8)
  self.assertAlmostEqual(prices(**(p|dict(t=0.)))['call'],p['x0']*max(p['s0']-p['k'],0),places=12)
if __name__=='__main__':unittest.main()

import unittest
import numpy as np
from soluciones.src.ejercicio2 import prices,integrate
class TestNormal(unittest.TestCase):
 def test_quadrature_and_parity(self):
  for f in [-.01,.0,.03]:
   for k in [-.02,.0,.04]:
    for sigma in [.003,.02]:
     args=(f,k,sigma*sigma*2,.5,.96,1e6)
     a=prices(*args);b=integrate(*args)
     for key in b:self.assertAlmostEqual(a[key],b[key],places=7)
     self.assertAlmostEqual(a['caplet']-a['floorlet'],a['fra'],places=9)
 def test_limits_and_scaling(self):
  for f,k in [(.03,.04),(.04,.03),(.03,.03)]:
   zero=prices(f,k,0,.5,.97)
   for var in [1e-16,1e-20]:
    a=prices(f,k,var,.5,.97)
    for key in ['fra','caplet','floorlet']:self.assertLess(abs(a[key]-zero[key]),3e-9)
   a=prices(f,k,.0001,.5,.97);b=prices(f,k,.0001,.5,.97,1e6)
   self.assertAlmostEqual(a['caplet']*1e6,b['caplet'],places=8)
 def test_quadrature_small_variance(self):
  # Regresión C-01: antes la cuadratura perdía la masa alrededor de cero.
  import warnings
  for f,k in [(.03,.032),(.032,.03),(.03,.03)]:
   for var in [0.,1e-20,1e-16,1e-12,1e-10,1e-8]:
    with warnings.catch_warnings():
     warnings.simplefilter('error')
     a=prices(f,k,var,.5,.95,1e6);b=integrate(f,k,var,.5,.95,1e6)
    for key in b:
     self.assertTrue(np.isfinite(b[key]))
     self.assertAlmostEqual(a[key],b[key],places=7)
  self.assertAlmostEqual(integrate(.03,.032,1e-10,.5,.95,1e6)['fra'],
                         -964.24997625,places=7)
 def test_quadrature_rejects_invalid_variance(self):
  with self.assertRaises(ValueError):integrate(.03,.032,-1.,.5,.95)
 def test_zero_time_and_par_strike(self):
  for t in [0,1,3]:
   a=prices(.03,.02,.01**2*t,.5,.95)
   self.assertAlmostEqual(prices(.03,a['par_strike'],.01**2*t,.5,.95)['fra'],0,places=14)
if __name__=='__main__':unittest.main()

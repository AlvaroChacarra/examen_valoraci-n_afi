import unittest
import numpy as np
from soluciones.src.ejercicio1 import Tree,EXERCISE,european_convolution,diffusion_reference
class TestJR(unittest.TestCase):
 def test_contract_and_martingale(self):
  for elapsed in [0,15/365]:
   t=Tree(elapsed=elapsed)
   self.assertEqual(len(t.h),36);self.assertAlmostEqual(sum(t.h),3-elapsed)
   np.testing.assert_allclose((t.u+t.d)/2,np.exp(.021*t.h),rtol=2e-15)
   self.assertEqual({j for j,l in enumerate(t.layers[:-1]) if l.stop.any()}|{36},EXERCISE)
   self.assertAlmostEqual(sum(t.sigmas**2*t.h),sum(np.array([.375,.425,.39])**2)-.375**2*elapsed)
 def test_values_and_exact_probabilities(self):
  e,b,a=[Tree(style=s) for s in ['european','bermuda','american']]
  self.assertLessEqual(e.price,b.price);self.assertLessEqual(b.price,a.price)
  self.assertAlmostEqual(e.price,european_convolution(e),places=11)
  out=b.exact_exercise()
  self.assertAlmostEqual(out['pv'],b.price,places=11)
  self.assertAlmostEqual(sum(x['first'] for x in out['by_month'])+out['expire_without_exercise'],1,places=13)
 def test_replication_and_simulation(self):
  t=Tree();s=t.simulate(n=200000)
  self.assertLess(t.max_local_error,1e-10);self.assertLess(t.max_budget_error,1e-10)
  self.assertLess(s['max_replication_error'],1e-10);self.assertLess(s['max_self_financing_error'],1e-10)
  exact=t.exact_exercise()['by_month']
  for row in s['first_exercise']:
   p=exact[row['month']]['first'];se=np.sqrt(max(p*(1-p),1e-10)/s['n'])
   self.assertLess(abs(p-row['prob']),5*se+1/s['n'])
 def test_reference_semigroup(self):
  from soluciones.src.ejercicio1 import bs_put
  analytic=bs_put(50,45,.021,sum(x*x for x in [.375,.425,.39]),3)
  self.assertLess(abs(diffusion_reference(.00025,european=True)-analytic),2e-6)
  self.assertLess(abs(diffusion_reference(.001,extent=6)-diffusion_reference(.001)),1e-8)
 def test_smoothing_precision(self):
  ref=diffusion_reference(.0005);ref2=diffusion_reference(.00025)
  self.assertLess(abs(ref-ref2),2e-5)
  self.assertLess(abs(Tree(smooth=True).price-ref2),abs(Tree().price-ref2))
if __name__=='__main__':unittest.main()

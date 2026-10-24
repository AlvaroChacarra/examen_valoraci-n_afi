"""Regresión del fallo real: conversión con cachés no acredita recálculo."""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
import openpyxl
import xlsxwriter
from soluciones.src.verifica_hojas import force_profile

class TestRecalculo(unittest.TestCase):
 @unittest.skipUnless(shutil.which('soffice'),'LibreOffice no disponible: prueba de motor omitida')
 def test_stale_cache_and_normal_are_actually_calculated(self):
  with tempfile.TemporaryDirectory(prefix='afi_recalc_') as name:
   root=Path(name);dest=root/'salida';dest.mkdir();profile=root/'perfil';force_profile(profile)
   w=xlsxwriter.Workbook(root/'fixture.xlsx');s=w.add_worksheet()
   s.write('A1',2);s.write_formula('A2','=A1^2',None,-999)
   s.write_formula('A3','=NORMDIST(0,0,1,TRUE)',None,-999);w.close()
   subprocess.run(['soffice',f'-env:UserInstallation={profile.as_uri()}','--headless','--convert-to','xlsx','--outdir',str(dest),str(root/'fixture.xlsx')],check=True,timeout=60,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
   result=openpyxl.load_workbook(dest/'fixture.xlsx',data_only=True)
   self.assertEqual(result.active['A2'].value,4)
   self.assertAlmostEqual(result.active['A3'].value,.5,places=14)
   result.close()
if __name__=='__main__':unittest.main()

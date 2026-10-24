"""Recálculo real con LibreOffice y cotejo de resultados/estados con Python."""
from pathlib import Path
import argparse,json,subprocess,shutil,time
import openpyxl
import numpy as np
from scipy.special import ndtr
from .ejercicio2 import prices as normal_prices
from .ejercicio3 import prices as fx_prices
from .ejercicio1 import Tree,EXERCISE
ROOT=Path(__file__).resolve().parents[1]

def verify(folder):
 out={}
 for filename in ['Ejercicio1.xlsx','Ejercicio2.xlsx','Ejercicio3.xlsx']:
  book=openpyxl.load_workbook(folder/filename,data_only=True,read_only=True)
  errors=[];cells=0
  for sheet in book:
   for row in sheet:
    for cell in row:
     if cell.data_type=='e':errors.append(f'{sheet.title}!{cell.coordinate}: {cell.value}')
     cells+=cell.value is not None
  assert not errors, errors[:20]
  out[filename]={'nonempty_cells':cells,'formula_errors':errors}
  if filename=='Ejercicio1.xlsx':
   maxdiff=0.;nodecount=0
   for suffix,elapsed,spot in [('0',0.,50.),('15',15/365,52.5)]:
    trees=[Tree(spot=spot,elapsed=elapsed,style=sty) for sty in ['european','bermuda','american']];smooth=Tree(spot=spot,elapsed=elapsed,smooth=True)
    mass=np.ones_like(trees[1].layers[0].spot)
    rows=iter(book[f'Arbol{suffix}'].iter_rows(min_row=2,values_only=True))
    for j,l in enumerate(trees[1].layers):
     for ix in np.ndindex(l.spot.shape):
      row=next(rows);expected=[l.spot[ix],*(t.layers[j].value[ix] for t in trees),smooth.layers[j].value[ix]];actual=[row[5],*row[9:13]]
      diff=max(abs(float(a)-float(b)) for a,b in zip(actual,expected));maxdiff=max(maxdiff,diff);nodecount+=1
      assert bool(row[16])==bool(l.stop[ix]),(suffix,j,ix,'politica')
      assert abs(row[15]-mass[ix])<1e-12,(suffix,j,ix,'masa viva',row[15],mass[ix])
      assert abs(row[17]-mass[ix]*l.stop[ix])<1e-12
      if j<36:
       assert abs(row[13]-l.delta[ix])<1e-10
       assert abs(row[14]-l.cash[ix])<1e-9
       if j==35:
        from .ejercicio1 import bs_put,R,K
        assert abs(row[20]-bs_put(l.spot[ix],K,R,trees[1].sigmas[j]**2*trees[1].h[j],trees[1].h[j]))<1e-9
      if j<36:
       assert abs(row[18])<1e-10 and abs(row[19])<1e-10
     if j<36:
      nxt=np.zeros_like(trees[1].layers[j+1].spot);g=trees[1].groups[j]
      dn=[slice(None)]*mass.ndim;up=dn.copy();dn[g]=slice(0,-1);up[g]=slice(1,None)
      nxt[tuple(dn)]+=mass*(~l.stop)/2;nxt[tuple(up)]+=mass*(~l.stop)/2;mass=nxt
    assert maxdiff<1e-9,maxdiff
   exact=Tree().exact_exercise()
   for row,j in zip(book['Probabilidades'].iter_rows(min_row=2,max_row=15,values_only=True),sorted(EXERCISE)):
    r=exact['by_month'][j]
    assert abs(row[1]-r['survival'])<1e-12 and abs(row[2]-r['first'])<1e-12 and abs(row[3]-r['conditional'])<1e-12
   out[filename].update(max_node_error=maxdiff,states_verified=nodecount,probabilities_verified=14)
  else:
   e=int(filename[9]);ref=json.loads((ROOT/f'resultados/ejercicio{e}.json').read_text());s=book['Calculo'];pairs=[(17,'fra'),(18,'caplet'),(19,'floorlet')] if e==2 else [(24,'forward'),(25,'forward_quanto'),(26,'call'),(27,'call_quanto'),(28,'put'),(29,'put_quanto')]
   diffs={key:abs(s[f'B{row}'].value-ref['closed'][key]) for row,key in pairs}
   assert max(diffs.values())<1e-7,diffs
   out[filename]['price_errors']=diffs
   aux=auxiliary_values(e,s)
   auxdiff={str(row):abs(float(s[f'B{row}'].value)-val) for row,val in aux.items()}
   assert max(auxdiff.values())<1e-7,(filename,auxdiff)
   out[filename]['auxiliary_cells_verified']=len(auxdiff)
   out[filename]['max_auxiliary_error']=max(auxdiff.values())
  book.close()
 return out

def auxiliary_values(e,s):
 def b(row):return s[f'B{row}'].value
 if e==2:
  f,k,t,delta,sigma,pu,nom=[b(i) for i in range(2,9)]
  v=sigma*sigma*t;std=np.sqrt(v);d=(f-k)/std if std else 0.;Phi=ndtr(d);phi=np.exp(-d*d/2)/np.sqrt(2*np.pi)
  a=(f-k)*Phi+std*phi if std else max(f-k,0)
  bb=(k-f)*(1-Phi)+std*phi if std else max(k-f,0)
  p=normal_prices(f,k,v,delta,pu,nom)
  return {9:v,10:std,11:d,12:Phi,13:phi,14:a,15:bb,16:pu*(1+delta*f),17:p['fra'],18:p['caplet'],19:p['floorlet'],20:0.,21:p['par_strike'],23:p['caplet']-b(22)}
 s0,k,x,rd,rf,q,ss,sx,rho,t,lam=[b(i) for i in range(2,13)]
 p=fx_prices(s0,k,x,rd,rf,q,ss,sx,rho,t);fu=s0*np.exp((rf-q)*t);fq=s0*np.exp(p['mu_s']*t);w=ss*np.sqrt(t)
 d1=np.log(fu/k)/w+w/2 if w else 0.;d1q=np.log(fq/k)/w+w/2 if w else 0.
 out={13:p['mu_s'],14:sx,15:p['sigma_n'],17:fu,18:fq,19:w,20:d1,21:d1-w,22:d1q,23:d1q-w,24:p['forward'],25:lam*p['forward_quanto'],26:p['call'],27:lam*p['call_quanto'],28:p['put'],29:lam*p['put_quanto'],30:0.,31:0.}
 if p['rho_mn'] is not None:out[16]=p['rho_mn']
 return out

def force_profile(profile):
 # OOXMLRecalcMode=0 equivale a recálculo completo al abrir; 1 conserva cachés.
 user=profile/'user';user.mkdir(parents=True,exist_ok=True)
 (user/'registrymodifications.xcu').write_text('''<?xml version="1.0" encoding="UTF-8"?><oor:items xmlns:oor="http://openoffice.org/2001/registry"><item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="OOXMLRecalcMode" oor:op="fuse"><value>0</value></prop></item></oor:items>''')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--recalculate',action='store_true');ap.add_argument('--folder',type=Path,default=ROOT/'hojas');args=ap.parse_args()
 if args.recalculate:
  dest=ROOT.parent/'tmp/recalculadas';dest.mkdir(parents=True,exist_ok=True)
  for i in [1,2,3]:
   target=dest/f'Ejercicio{i}.xlsx'
   if target.exists():target.unlink()
  profile=ROOT.parent/'tmp/lo-profile';force_profile(profile)
  cmd=['soffice',f'-env:UserInstallation={profile.as_uri()}','--headless','--convert-to','xlsx','--outdir',str(dest),*[str(ROOT/'hojas'/f'Ejercicio{i}.xlsx') for i in [1,2,3]]]
  subprocess.run(cmd,check=True,timeout=300)
  # Detectar fallos aunque LibreOffice retorne cero.
  for i in [1,2,3]:assert (dest/f'Ejercicio{i}.xlsx').stat().st_size>0
  out=verify(dest)
  for i in [1,2,3]:shutil.copy2(dest/f'Ejercicio{i}.xlsx',ROOT/'hojas')
 else:out=verify(args.folder)
 (ROOT/'resultados/hojas_verificadas.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
if __name__=='__main__':main()

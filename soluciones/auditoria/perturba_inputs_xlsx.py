"""Edita copias de los XLSX de un commit, fuerza recálculo y contrasta dependencias.

No modifica entregables. Requiere LibreOffice y las dependencias Python del proyecto.
"""
import argparse
from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import openpyxl
import numpy as np

ROOT=Path(__file__).resolve().parents[2]

def code_snapshot(commit,exercise):
    mod=types.ModuleType(f'audit_e{exercise}')
    sys.modules[mod.__name__]=mod
    source=subprocess.check_output(['git','show',f'{commit}:soluciones/src/ejercicio{exercise}.py'],cwd=ROOT,text=True)
    exec(compile(source,f'{commit}:ejercicio{exercise}.py','exec'),mod.__dict__)
    return mod

def run(commit,base):
    src=base/'input';dst=base/'output';profile=base/'profile'
    src.mkdir(parents=True);dst.mkdir();(profile/'user').mkdir(parents=True)
    (profile/'user/registrymodifications.xcu').write_text('''<?xml version="1.0" encoding="UTF-8"?><oor:items xmlns:oor="http://openoffice.org/2001/registry"><item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="OOXMLRecalcMode" oor:op="fuse"><value>0</value></prop></item></oor:items>''')
    edits={1:{'B2':55.},2:{'B6':.02},3:{'B10':-.3,'B4':1.1}}
    for i in [1,2,3]:
        blob=subprocess.check_output(['git','show',f'{commit}:soluciones/hojas/Ejercicio{i}.xlsx'],cwd=ROOT)
        w=openpyxl.load_workbook(BytesIO(blob));sheet=w['Entradas' if i==1 else 'Calculo']
        for cell,value in edits[i].items():sheet[cell]=value
        w.save(src/f'Ejercicio{i}.xlsx');w.close()
    result=subprocess.run(['soffice',f'-env:UserInstallation={profile.as_uri()}','--headless','--convert-to','xlsx','--outdir',str(dst),*[str(src/f'Ejercicio{i}.xlsx') for i in [1,2,3]]],check=True,timeout=300,capture_output=True,text=True)
    out={'commit':commit,'directory':str(base),'edits':edits,'engine_stdout':result.stdout,'observed':{},'checks':{},'errors':{}}
    for i in [1,2,3]:
        w=openpyxl.load_workbook(dst/f'Ejercicio{i}.xlsx',data_only=True,read_only=True)
        if i==1:
            s=w['Arbol0'];rows={'J2':'european','K2':'bermuda','L2':'american','M2':'smoothed'}
            mod=code_snapshot(commit,1)
            expected={cell:(mod.Tree(spot=55.,smooth=True) if style=='smoothed' else mod.Tree(spot=55.,style=style)).price for cell,style in rows.items()}
            expected.update({'P2':1.,'P3':.5,'P4':.5})
        elif i==2:
            s=w['Calculo'];ref=code_snapshot(commit,2).prices(.03,.032,.02**2*2,.5,np.exp(-.075),1e6)
            expected={f'B{r}':ref[k] for r,k in [(17,'fra'),(18,'caplet'),(19,'floorlet')]}
            expected.update({'B9':.0008,'B10':np.sqrt(.0008)})
        else:
            s=w['Calculo'];ref=code_snapshot(commit,3).prices(100,105,1.1,.03,.02,.01,.25,.12,-.3,2)
            expected={f'B{r}':ref[k] for r,k in [(24,'forward'),(25,'forward_quanto'),(26,'call'),(27,'call_quanto'),(28,'put'),(29,'put_quanto')]}
            expected.update({'B13':ref['mu_s'],'B15':ref['sigma_n']})
        observed={cell:s[cell].value for cell in expected}
        checks={cell:bool(isinstance(observed[cell],(int,float)) and abs(observed[cell]-value)<(1e-7 if i in [2,3] else 1e-9)) for cell,value in expected.items()}
        errors=[]
        for sheet in w:
            for row in sheet:
                for cell in row:
                    if cell.data_type=='e':
                        if len(errors)<25:errors.append(f'{sheet.title}!{cell.coordinate}: {cell.value}')
        out['observed'][f'E{i}']=observed;out['checks'][f'E{i}']=checks;out['errors'][f'E{i}']=errors
        w.close()
    out['passed']=all(all(v.values()) for v in out['checks'].values()) and not any(out['errors'].values())
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--commit',required=True)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();base=Path(tempfile.mkdtemp(prefix='mefc_audit_input_'))
    out=run(args.commit,base)
    if args.output:args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    if not out['passed']:raise SystemExit(1)

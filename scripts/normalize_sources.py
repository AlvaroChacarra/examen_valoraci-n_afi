#!/usr/bin/env python3
"""Normalize supplied course archives without recalculating or editing workbooks."""
from __future__ import annotations
import argparse
import collections
import hashlib
import io
import json
import posixpath
import re
import shutil
import unicodedata
import warnings
from pathlib import Path, PurePosixPath
from zipfile import ZipFile
from concurrent.futures import ThreadPoolExecutor
import fitz
import openpyxl
from openpyxl.formula.translate import Translator
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
NS = {'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
      'm':'http://schemas.openxmlformats.org/officeDocument/2006/math'}

def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-') or 'sin-nombre'

def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text.rstrip()+'\n',encoding='utf-8')

def md(s):
    return str(s if s is not None else '').replace('|','\\|').replace('\n','<br>')

def show(x):
    if hasattr(x,'isoformat'): return x.isoformat()
    return x if isinstance(x,(str,int,float,bool,type(None))) else str(x)

def ingest(input_dir):
    records=[]
    archives=[]
    def unpack(data,group,folders,chain):
        with ZipFile(io.BytesIO(data)) as z:
            for item in sorted(z.infolist(),key=lambda i:i.filename.casefold()):
                if item.is_dir() or '__MACOSX' in item.filename or PurePosixPath(item.filename).name.startswith('._'):continue
                pp=PurePosixPath(item.filename)
                if pp.is_absolute() or '..' in pp.parts:raise ValueError('Unsafe archive member')
                b=z.read(item)
                provenance=chain+[item.filename]
                if pp.suffix.lower()=='.zip':
                    archives.append({'chain':provenance,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
                    unpack(b,group,folders+[slug(pp.stem)],provenance)
                    continue
                filename=slug(pp.stem)+pp.suffix.lower()
                rel=Path('raw')/group/Path(*folders)/filename
                target=ROOT/rel
                if target.exists() and target.read_bytes()!=b:
                    rel=rel.with_name(slug(pp.stem)+'-'+hashlib.sha256(b).hexdigest()[:8]+pp.suffix.lower())
                    target=ROOT/rel
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(b)
                records.append({'path':rel.as_posix(),'original_name':pp.name,'archive_chain':provenance,
                    'group':group,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'extension':pp.suffix.lower()})
    for p in sorted(input_dir.glob('*.zip')):
        group='fundamentos' if p.name.startswith('Fundamentos') else 'marco-black'
        b=p.read_bytes()
        archives.append({'chain':[p.name],'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
        unpack(b,group,[],[p.name])
    for name in ['Valoracion MEFC 2026.pdf','Instrucciones para la entrega del trabajo.pdf','Ejercicio 3. Desarrollo.pptx']:
        p=input_dir/name
        if not p.exists():raise FileNotFoundError(p)
        rel=Path('raw/encargo')/(slug(p.stem)+p.suffix.lower())
        (ROOT/rel).parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(p,ROOT/rel)
        records.append({'path':rel.as_posix(),'original_name':name,'archive_chain':[name],
            'group':'encargo','bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'extension':p.suffix.lower()})
    counts=collections.Counter()
    for r in sorted(records,key=lambda r:r['path']):
        kind={'.pdf':'PDF','.xlsx':'XLS','.xlsm':'XLS','.pptx':'PPT'}.get(r['extension'],'SRC')
        counts[kind]+=1
        r['id']=f'{kind}-{counts[kind]:03d}'
        r['extraction']=f'knowledge-base/extracciones/{r["id"].lower()}-{Path(r["path"]).stem}.md'
        r['dossier']=f'knowledge-base/fuentes/{r["id"].lower()}-{Path(r["path"]).stem}.md'
    manifest={'schema_version':1,'ingested_on':'2026-10-24','archives':archives,'sources':sorted(records,key=lambda r:r['id'])}
    write(ROOT/'catalogo.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    return manifest

def pdf_extract(r):
    doc=fitz.open(ROOT/r['path'])
    pages=[]
    out=[f'# {r["id"]}: {r["original_name"]}', '',
        f'Original: [archivo raw](../../{r["path"]}). SHA-256: `{r["sha256"]}`.',
        '', 'Extracción de texto por página. Conserva la paginación PDF; la notación matemática puede perder estructura. Las fichas de fuente y de conceptos contienen la interpretación revisada.', '']
    for i,p in enumerate(doc,1):
        text=p.get_text(sort=False).strip()
        pages.append({'page':i,'characters':len(text),'images':len(p.get_images()),'text':text})
        out += [f'## Página {i}', '', text or '**SIN TEXTO EXTRAÍBLE: requiere lectura visual del original.**','']
    r['pages']=len(pages)
    r['low_text_pages']=[x['page'] for x in pages if x['characters']<80]
    write(ROOT/r['extraction'],'\n'.join(out))
    write(ROOT/'metadata'/f'{r["id"].lower()}.json',json.dumps({'source_id':r['id'],'pages':pages},ensure_ascii=False,indent=2))
    return {'id':r['id'],'name':r['original_name'],'pages':len(pages),'low_text':r['low_text_pages']}

def formula_text(v):
    if isinstance(v,str):return v
    if hasattr(v,'text'):return v.text
    return f'<{type(v).__name__}: {vars(v)}>'

def compact_labels(strings):
    groups=collections.defaultdict(list);plain=[]
    for item in strings:
        match=re.fullmatch(r'(sim|X|Y|Z)(\d+)',item['text'].strip(),re.I)
        if match:groups[(match.group(1),re.match(r'[A-Z]+',item['cell']).group())].append((int(match.group(2)),item))
        else:plain.append(item)
    for (prefix,col),items in groups.items():
        nums=[n for n,_ in items]
        if len(items)>10 and nums==list(range(nums[0],nums[-1]+1)):
            plain.append({'cell':items[0][1]['cell']+' … '+items[-1][1]['cell'],
                          'text':f'{prefix}{nums[0]} … {prefix}{nums[-1]} ({len(items)} etiquetas consecutivas, compactadas)'})
        else:plain.extend(item for _,item in items)
    return plain

def xlsx_extract(r):
    warnings.filterwarnings('ignore',category=UserWarning,module='openpyxl')
    wb=openpyxl.load_workbook(ROOT/r['path'],data_only=False,read_only=False,keep_links=True)
    cached=openpyxl.load_workbook(ROOT/r['path'],data_only=True,read_only=False,keep_links=False)
    meta={'source_id':r['id'],'names':[], 'sheets':[], 'vba':False,'external_links':0,'functions':{}}
    for k,v in wb.defined_names.items():meta['names'].append({'name':k,'ref':v.attr_text})
    with ZipFile(ROOT/r['path']) as z:
        meta['vba']='xl/vbaProject.bin' in z.namelist()
        meta['external_links']=len([n for n in z.namelist() if re.fullmatch(r'xl/externalLinks/externalLink\d+\.xml',n)])
        meta['embeddings']=[n for n in z.namelist() if n.startswith('xl/embeddings/')]
        meta['media']=[n for n in z.namelist() if n.startswith('xl/media/')]
        meta['calc_properties']=str(wb.calculation)
    out=[f'# {r["id"]}: {r["original_name"]}', '',f'Original: [archivo raw](../../{r["path"]}). SHA-256: `{r["sha256"]}`.', '',
        'Lectura estática: fórmulas, etiquetas, notas, valores guardados y dependencias. No se han recalculado fórmulas ni ejecutado macros. Los valores guardados son evidencia del archivo, no resultados verificados de una nueva ejecución.', '',
        f'Macros VBA: **{meta["vba"]}**. Vínculos externos: **{meta["external_links"]}**. Objetos incrustados: **{len(meta["embeddings"])}**.', '']
    if meta['names']:
        out+=['## Nombres definidos','','| Nombre | Referencia |','|---|---|']
        out += [f'| `{md(x["name"])}` | `{md(x["ref"])}` |' for x in meta['names']]
        out+=['']
    funcs=collections.Counter()
    for ws in wb.worksheets:
        cs=cached[ws.title]
        cells=sorted([c for c in ws._cells.values() if c.value is not None or c.comment],key=lambda c:(c.row,c.column))
        strings=[];constants=[];families={};errors=[];comments=[];formula_count=0;rawform=[]
        for c in cells:
            v=c.value
            if c.comment:comments.append({'cell':c.coordinate,'text':c.comment.text,'author':c.comment.author})
            if c.data_type=='f' or (v is not None and not isinstance(v,(str,float,int,bool)) and hasattr(v,'text')):
                f=formula_text(v);formula_count+=1
                try:key=Translator(f,origin=c.coordinate).translate_formula('XFD1048576')
                except Exception:key=re.sub(r'(\$?[A-Z]{1,3})\d+',r'\1#',f)
                d=families.setdefault(key,{'count':0,'first':c.coordinate,'last':c.coordinate,'formula':f,'examples':[],'cached_first':show(cs[c.coordinate].value)})
                d['count']+=1;d['last']=c.coordinate
                if len(d['examples'])<3:d['examples'].append({'cell':c.coordinate,'formula':f,'cached':show(cs[c.coordinate].value)})
                rawform.append((c.coordinate,f,show(cs[c.coordinate].value)))
                funcs.update(re.findall(r'(?<![A-Z0-9_.])([A-Z_][A-Z0-9_.]*)\s*\(',f.upper()))
            elif isinstance(v,str):
                if c.data_type=='e':errors.append({'cell':c.coordinate,'value':v})
                else:strings.append({'cell':c.coordinate,'text':v})
            elif v is not None:constants.append({'cell':c.coordinate,'value':show(v),'format':c.number_format})
        cached_errors=[]
        for c in cs._cells.values():
            if c.data_type=='e':cached_errors.append({'cell':c.coordinate,'value':c.value})
        charts=[]
        for ch in ws._charts:
            def texts(x):
                if x is None:return ''
                try:return ' '.join(t.text for p in x.tx.rich.p for t in p.r if t.text)
                except Exception:return str(type(x).__name__)
            series=[]
            for ser in ch.series:
                sr={}
                for field in ['val','cat','xVal','yVal']:
                    ob=getattr(ser,field,None)
                    if ob:
                        for rf in ['numRef','strRef']:
                            ref=getattr(ob,rf,None)
                            if ref is not None:sr[field]=ref.f
                series.append(sr)
            charts.append({'type':type(ch).__name__,'title':texts(ch.title),'series':series})
        sheet={'name':ws.title,'state':ws.sheet_state,'dimension':ws.calculate_dimension(),'nonempty':len(cells),'formulas':formula_count,
            'strings':strings,'constants':constants,'formula_families':list(families.values()),'comments':comments,
            'cached_errors':cached_errors,'charts':charts,'merged':list(map(str,ws.merged_cells.ranges)),
            'dependencies':sorted(set(m for _,f,_ in rawform for m in re.findall(r"(?:'([^']+)'|([A-Za-z_][A-Za-z0-9_ .]*))!",f) for m in m if m))}
        meta['sheets'].append(sheet)
        out += [f'## Hoja: {ws.title}', '',f'Estado: `{ws.sheet_state}`. Rango usado: `{sheet["dimension"]}`. Celdas con contenido: {len(cells)}. Fórmulas: {formula_count}. Familias: {len(families)}.', '',
            '### Etiquetas y enunciados completos','','| Celda | Texto |','|---|---|']
        out += [f'| `{x["cell"]}` | {md(x["text"])} |' for x in compact_labels(strings)] or ['| — | No hay etiquetas de texto |']
        out += ['','### Constantes e inputs guardados','','Los números también pueden ser escenarios o resultados pegados. Su papel se determina por las etiquetas y la ficha interpretativa.','','| Celda | Valor | Formato |','|---|---|---|']
        # Large numeric series: retain all first 100 rows and column/range summaries beyond.
        head=[x for x in constants if int(re.search(r'\d+',x['cell']).group())<=100]
        tail=[x for x in constants if x not in head]
        out += [f'| `{x["cell"]}` | {md(x["value"])} | `{md(x["format"])}` |' for x in head]
        if tail:
            groups=collections.defaultdict(list)
            for x in tail:groups[re.match(r'[A-Z]+',x['cell']).group()].append(x)
            out+=['','Series numéricas posteriores a la fila 100 (compactadas, sin presentarlas como inputs):','','| Columna | Primera / última celda | N | Primer / último valor |','|---|---|---:|---|']
            out += [f'| {k} | `{v[0]["cell"]}` / `{v[-1]["cell"]}` | {len(v)} | {md(v[0]["value"])} / {md(v[-1]["value"])} |' for k,v in groups.items()]
        out+=['','### Familias de fórmulas','','Cada fila agrupa fórmulas trasladables por referencias relativas. Primera y última celda delimitan posiciones, no garantizan un rectángulo sin huecos. Se conserva un ejemplo literal y su valor guardado.','','| Primera | Última | N | Fórmula literal de la primera | Valor guardado |','|---|---|---:|---|---|']
        out += [f'| `{x["first"]}` | `{x["last"]}` | {x["count"]} | `{md(x["formula"])}` | {md(x["cached_first"])} |' for x in families.values()]
        if comments:
            out+=['','### Notas de celdas','']+[f'- `{x["cell"]}`: {x["text"]}' for x in comments]
        if charts:out+=['','### Gráficos y rangos de origen','','```json',json.dumps(charts,ensure_ascii=False,indent=2),'```']
        if cached_errors:out+=['','### Errores guardados','','Se detectan '+str(len(cached_errors))+' celdas de error. No se han corregido.','','```json',json.dumps(cached_errors[:80],ensure_ascii=False,indent=2),'```']
        out+=['']
    meta['functions']=dict(funcs)
    r['sheets']=len(meta['sheets']);r['formulas']=sum(s['formulas'] for s in meta['sheets']);r['vba']=meta['vba']
    write(ROOT/r['extraction'],'\n'.join(out))
    write(ROOT/'metadata'/f'{r["id"].lower()}.json',json.dumps(meta,ensure_ascii=False,indent=2,default=show))
    wb.close();cached.close()
    return {'id':r['id'],'name':r['original_name'],'sheets':[(s['name'],s['nonempty'],s['formulas'],len(s['formula_families'])) for s in meta['sheets']],'vba':meta['vba'],'functions':list(funcs)}

def math_text(e):
    tag=etree.QName(e).localname
    children=list(e)
    def sub(name):
        x=next((x for x in children if etree.QName(x).localname==name),None)
        return ''.join(math_text(y) for y in x) if x is not None else ''
    if tag in ['t']:return e.text or ''
    if tag=='f':return r'\frac{'+sub('num')+'}{'+sub('den')+'}'
    if tag=='sSub':return '{'+sub('e')+'}_{'+sub('sub')+'}'
    if tag=='sSup':return '{'+sub('e')+'}^{'+sub('sup')+'}'
    if tag=='sSubSup':return '{'+sub('e')+'}_{'+sub('sub')+'}^{'+sub('sup')+'}'
    if tag=='rad':return r'\sqrt{'+sub('e')+'}'
    if tag.endswith('Pr'):return ''
    return ''.join(math_text(x) for x in children)

def ppt_extract(r):
    out=[f'# {r["id"]}: {r["original_name"]}', '',f'Original: [archivo raw](../../{r["path"]}).', '',
        'Extracción por diapositiva, incluidas las ecuaciones OfficeMath. Los huecos de la plantilla se conservan. La notación lineal se debe leer junto a la ficha de fuente.', '']
    with ZipFile(ROOT/r['path']) as z:
        slides=sorted([n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)],key=lambda n:int(re.search(r'(\d+)\.xml',n).group(1)))
        for i,n in enumerate(slides,1):
            root=etree.fromstring(z.read(n));out += [f'## Diapositiva {i}','']
            for para in root.findall('.//a:p',NS):
                txt=math_text(para).strip()
                if txt:out += [txt,'']
    r['slides']=len(slides)
    write(ROOT/r['extraction'],'\n'.join(out))
    return {'id':r['id'],'name':r['original_name'],'slides':len(slides)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input-dir',type=Path);ap.add_argument('--extract-only',action='store_true');args=ap.parse_args()
    manifest=json.loads((ROOT/'catalogo.json').read_text()) if args.extract_only else ingest(args.input_dir)
    def run(r):
        f={'.pdf':pdf_extract,'.xlsx':xlsx_extract,'.xlsm':xlsx_extract,'.pptx':ppt_extract}.get(r['extension'])
        if not f:raise ValueError('Unsupported source '+r['path'])
        result=f(r);print(json.dumps(result,ensure_ascii=False),flush=True);return result
    with ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(run,manifest['sources']))
    write(ROOT/'catalogo.json',json.dumps(manifest,ensure_ascii=False,indent=2))

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Supplement both image-heavy sessions, preserving native text and source bytes."""
import argparse,hashlib,json,os,subprocess,tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import fitz
from normalize_sources import ROOT,write

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--workers',type=int,default=4);args=parser.parse_args()
    manifest=json.loads((ROOT/'catalogo.json').read_text())
    for r in manifest['sources']:
        if r['id'] not in ['PDF-005','PDF-006']:continue
        assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
        cache=ROOT/'metadata/ocr-cache'/r['id'];cache.mkdir(parents=True,exist_ok=True)
        tag=cache/'source.sha256'
        reuse=tag.exists() and tag.read_text().strip()==r['sha256']
        doc=fitz.open(ROOT/r['path']);pages=[{'page':i+1,'text':p.get_text(sort=False).strip()} for i,p in enumerate(doc)]
        def recover(x):
            p=cache/f"{x['page']:03d}.txt"
            if reuse and p.exists():return p.read_text()
            with fitz.open(ROOT/r['path']) as d:
                png=d[x['page']-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8)).tobytes('png')
            env=dict(os.environ,OMP_THREAD_LIMIT='1')
            result=subprocess.run(['tesseract','stdin','stdout','-l','eng','--psm','3'],input=png,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env,check=True)
            text=result.stdout.decode();p.write_text(text);return text
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            recovered=list(pool.map(recover,pages))
        tag.write_text(r['sha256'])
        out=[f"# {r['id']}: {r['original_name']}",'',f"Original: [archivo raw](../../{r['path']}). SHA-256: `{r['sha256']}`.",'',
             'Texto nativo y OCR auxiliar por página. El OCR puede alterar símbolos; no sustituye las fórmulas revisadas de conceptos ni las demostraciones de los PDF teóricos. Todas las páginas de esta sesión tienen ambos canales separados.','']
        for page,ocr in zip(pages,recovered):
            out += [f"## Página {page['page']}",'','### Texto nativo','','```text',page['text'],'```','','### OCR auxiliar','','```text',ocr.strip(),'```','']
        write(ROOT/r['extraction'],'\n'.join(out));r['ocr_pages']=len(pages)
        write(ROOT/'metadata'/f"{r['id'].lower()}-review-ocr.json",json.dumps({'sha256':r['sha256'],'pages':pages,'ocr':recovered},ensure_ascii=False))
        print(r['id'],'OCR pages',len(pages),'chars',sum(map(len,recovered)),flush=True)
    write(ROOT/'catalogo.json',json.dumps(manifest,ensure_ascii=False,indent=2))

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Recover image-only pages, image labels and VBA source, without execution."""
import collections,hashlib,io,json,math,re,struct,subprocess,tempfile
from pathlib import Path
from zipfile import ZipFile
from concurrent.futures import ThreadPoolExecutor
import fitz
from lxml import etree
from xlrd.compdoc import CompDoc
from PIL import Image
from normalize_sources import ROOT,write

def decompress_vba(data):
    if not data or data[0]!=1:raise ValueError('signature')
    pos=1;out=bytearray()
    while pos<len(data):
        head=struct.unpack_from('<H',data,pos)[0];start=pos;pos+=2
        if (head>>12)&7!=3:raise ValueError('chunk signature')
        end=min(start+(head&0xfff)+3,len(data));chunkstart=len(out)
        if not head&0x8000:
            out.extend(data[pos:end]);pos=end;continue
        while pos<end:
            flags=data[pos];pos+=1
            for bit in range(8):
                if pos>=end:break
                if flags&(1<<bit):
                    token=struct.unpack_from('<H',data,pos)[0];pos+=2
                    n=max(4,(len(out)-chunkstart-1).bit_length());mask=0xffff>>n
                    length=(token&mask)+3;offset=(token>>(16-n))+1
                    if offset>len(out)-chunkstart:raise ValueError('offset')
                    for _ in range(length):out.append(out[-offset])
                else:out.append(data[pos]);pos+=1
                if len(out)>5_000_000:raise ValueError('too long')
        pos=end
    return bytes(out)

def vba_modules(data):
    cd=CompDoc(data,logfile=io.StringIO());result=[]
    for node in cd.dirlist:
        if node.etype!=2 or node.name in ['dir','PROJECT','PROJECTwm','_VBA_PROJECT'] or node.name.startswith('__SRP'):continue
        try:b=cd.get_named_stream('VBA/'+node.name)
        except Exception:continue
        if not b:continue
        for offset in range(len(b)-2):
            if b[offset]!=1 or ((int.from_bytes(b[offset+1:offset+3],'little')>>12)&7)!=3:continue
            try:s=decompress_vba(b[offset:]).decode('cp1252')
            except Exception:continue
            if 'Attribute VB_Name' in s:
                result.append({'module':node.name,'source':s});break
    return result

def emf_text(b):
    pos=0;out=[]
    while pos+8<=len(b):
        typ,size=struct.unpack_from('<II',b,pos)
        if size<8 or pos+size>len(b):break
        if typ in [83,84] and size>=76:
            count,offset=struct.unpack_from('<II',b,pos+44)
            try:
                text=b[pos+offset:pos+offset+count*(2 if typ==84 else 1)].decode('utf-16le' if typ==84 else 'cp1252')
                if text.strip():out.append(text)
            except Exception:pass
        pos+=size
    return ' '.join(out)

def emf_bitmap(b):
    pos=0
    while pos+8<=len(b):
        typ,size=struct.unpack_from('<II',b,pos)
        if size<8 or pos+size>len(b):break
        if typ==81 and size>=80:
            offinfo,ninfo,offbits,nbits=struct.unpack_from('<IIII',b,pos+48)
            dib=b[pos+offinfo:pos+offinfo+ninfo]+b[pos+offbits:pos+offbits+nbits]
            header=b'BM'+struct.pack('<IHHI',14+len(dib),0,0,14+ninfo)
            im=Image.open(io.BytesIO(header+dib)).convert('RGB');out=io.BytesIO();im.save(out,format='PNG')
            return out.getvalue()
        pos+=size
    return None

def ocr_png(data,psm=6):
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        f.write(data);f.flush()
        r=subprocess.run(['tesseract',f.name,'stdout','-l','eng','--psm',str(psm)],capture_output=True,text=True)
    return r.stdout.strip()

def main():
    manifest=json.loads((ROOT/'catalogo.json').read_text());assets={};asset_sources=collections.defaultdict(list)
    for r in manifest['sources']:
        if r['extension'] not in ['.xlsx','.xlsm']:continue
        path=ROOT/'metadata'/f'{r["id"].lower()}.json';meta=json.loads(path.read_text());extra=[]
        with ZipFile(ROOT/r['path']) as z:
            if meta['vba']:
                mods=vba_modules(z.read('xl/vbaProject.bin'));meta['vba_modules']=mods
                extra+=['## Código VBA recuperado','', 'Código fuente leído estáticamente del contenedor VBA. No se ha ejecutado. Los módulos de interfaz sin procedimientos no añaden lógica de cálculo.','']
                for mod in mods:extra += [f'### Módulo {mod["module"]}','','```vb',mod['source'],'```','']
            drawings=[]
            for n in z.namelist():
                if n.startswith('xl/drawings/') and n.endswith('.xml'):
                    root=etree.fromstring(z.read(n));texts=root.xpath('//*[local-name()="t"]/text()')
                    if texts:drawings.append({'part':n,'text':texts})
                if n.startswith('xl/media/'):
                    b=z.read(n);h=hashlib.sha256(b).hexdigest();asset_sources[h].append((r['id'],n))
                    assets.setdefault(h,{'bytes':b,'name':n})
            meta['drawing_text']=drawings
            if drawings:extra+=['## Textos en objetos de dibujo','','```json',json.dumps(drawings,ensure_ascii=False,indent=2),'```','']
        write(path,json.dumps(meta,ensure_ascii=False,indent=2))
        base=(ROOT/r['extraction']).read_text()
        for marker in ['## Código VBA recuperado','## Textos en objetos de dibujo']:
            base=base.split(marker,1)[0]
        write(ROOT/r['extraction'],base.rstrip()+'\n\n'+'\n'.join(extra))
    def asset_extract(item):
        h,a=item
        if a['name'].endswith('.emf'):
            png=emf_bitmap(a['bytes'])
            text=emf_text(a['bytes']) or (ocr_png(png) if png else '')
        else:
            im=Image.open(io.BytesIO(a['bytes'])).convert('RGB');f=io.BytesIO();im.save(f,format='PNG');png=f.getvalue()
            text=ocr_png(png)
        if png:
            dest=ROOT/'knowledge-base/assets/excel'/f'{h[:12]}.png';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(png)
        return h,text
    with ThreadPoolExecutor(max_workers=3) as pool:parsed=dict(pool.map(asset_extract,assets.items()))
    out=['# Texto recuperado de imágenes incrustadas en Excel','','Las imágenes EMF se leen a través de sus registros de texto; las imágenes raster mediante OCR. El orden y los símbolos de las ecuaciones pueden ser imperfectos. Los hashes deduplican la misma imagen entre plantilla y solución.','']
    for h,text in parsed.items():
        out += [f'## Imagen {h[:12]}','','Fuentes: '+', '.join(f'`{a}` / `{b}`' for a,b in asset_sources[h]),'',f'![Imagen extraída](../assets/excel/{h[:12]}.png)','',text or '**Sin texto recuperable por este método. Ver los conceptos y las fórmulas de celdas asociados.**','']
    write(ROOT/'knowledge-base/extracciones/imagenes-excel.md','\n'.join(out))
    print('IMAGES',len(parsed),'RECOVERED',sum(bool(x) for x in parsed.values()),flush=True)
    for r in manifest['sources']:
        if r['id']!='PDF-006':continue
        meta_path=ROOT/'metadata'/f'{r["id"].lower()}.json';meta=json.loads(meta_path.read_text());doc=fitz.open(ROOT/r['path'])
        tasks=[x for x in meta['pages'] if x['characters']<80 and x['page']<73]
        def page_extract(x):
            # Separate document per worker: MuPDF documents are not thread-safe.
            d=fitz.open(ROOT/r['path']);png=d[x['page']-1].get_pixmap(matrix=fitz.Matrix(2,2)).tobytes('png')
            return x['page'],ocr_png(png,3)
        cached_ocr={x['page']:x['ocr'] for x in tasks if x.get('ocr')}
        with ThreadPoolExecutor(max_workers=3) as pool:ocr=dict(pool.map(page_extract,[x for x in tasks if x['page'] not in cached_ocr]))
        ocr.update(cached_ocr)
        for x in meta['pages']:
            if x['page'] in ocr:x.update({'ocr':ocr[x['page']],'ocr_engine':'tesseract-eng'})
        write(meta_path,json.dumps(meta,ensure_ascii=False,indent=2))
        text=[f'# {r["id"]}: {r["original_name"]}','',f'Original: [archivo raw](../../{r["path"]}). SHA-256: `{r["sha256"]}`.','',
              'Texto por páginas, con OCR añadido donde el contenido está incrustado como imagen. El OCR puede alterar símbolos; las fórmulas revisadas están en conceptos y PDF-003.','']
        for x in meta['pages']:
            text += [f'## Página {x["page"]}','',x['text'] or '(Página imagen)','']
            if x['page'] in ocr:text += ['**OCR de página imagen. Revisar símbolos antes de usar ecuaciones.**','',ocr[x['page']],'']
        write(ROOT/r['extraction'],'\n'.join(text))
        print('OCR PAGES',len(ocr),'CHARS',sum(map(len,ocr.values())),flush=True)

if __name__=='__main__':main()

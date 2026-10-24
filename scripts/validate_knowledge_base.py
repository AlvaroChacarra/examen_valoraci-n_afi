#!/usr/bin/env python3
"""Check source integrity, extraction coverage, links and cold-start entry points."""
import collections,hashlib,json,re,sys
from pathlib import Path
from normalize_sources import ROOT,write

def main():
    catalog=json.loads((ROOT/'catalogo.json').read_text());sources=catalog['sources'];errors=[]
    report_path=ROOT/'knowledge-base/CONTROL_COBERTURA.md'
    if not report_path.exists():write(report_path,'# Control de cobertura\n')
    required=['README.md','AGENTS.md','knowledge-base/README.md','knowledge-base/CATALOGO.md',
              'knowledge-base/MAPA_RELACIONES.md','knowledge-base/LIMITACIONES.md',
              'knowledge-base/OPERACION.md','knowledge-base/ejercicios/ENCARGO.md']
    for p in required:
        if not (ROOT/p).is_file():errors.append('Missing entry point: '+p)
    ids=[r['id'] for r in sources]
    if len(ids)!=len(set(ids)):errors.append('Duplicate source IDs')
    for r in sources:
        for field in ['path','dossier','extraction']:
            if not (ROOT/r[field]).is_file():errors.append(f'{r["id"]} missing {field}')
        if not (ROOT/r['path']).is_file():continue
        actual=hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()
        if actual!=r['sha256']:errors.append(r['id']+' raw hash mismatch')
        s=(ROOT/r['extraction']).read_text()
        if r['extension']=='.pdf':
            pages=list(map(int,re.findall(r'^## Página (\d+)$',s,re.M)))
            if pages!=list(range(1,r['pages']+1)):errors.append(r['id']+' page coverage mismatch')
        if r['extension']=='.pptx':
            if len(re.findall(r'^## Diapositiva ',s,re.M))!=r['slides']:errors.append(r['id']+' slide coverage mismatch')
        if r['extension'] in ['.xlsx','.xlsm']:
            if len(re.findall(r'^## Hoja:',s,re.M))!=r['sheets']:errors.append(r['id']+' sheet coverage mismatch')
            if r.get('vba') and s.count('## Código VBA recuperado')!=1:errors.append(r['id']+' missing/duplicated VBA source')
    raw={p.relative_to(ROOT).as_posix() for p in (ROOT/'raw').rglob('*') if p.is_file()}
    if raw!={r['path'] for r in sources}:errors.append('Uncatalogued or missing raw files')
    checked_links=0
    for f in ROOT.rglob('*.md'):
        if '.git' in f.parts:continue
        s=f.read_text()
        for dest in re.findall(r'!?\[[^\]]*\]\(([^)\n]+)\)',s):
            if re.match(r'^(https?:|mailto:|#)',dest):continue
            target=dest.split('#')[0]
            if not target:continue
            checked_links+=1
            if not (f.parent/target).exists():errors.append(f'{f.relative_to(ROOT)} broken link {dest}')
    for f in (ROOT/'knowledge-base/fuentes').glob('*.md'):
        if '## ' not in f.read_text():errors.append(f.name+' empty dossier')
    counts=collections.Counter(r['extension'] for r in sources)
    data={'sources':len(sources),'source_counts':dict(counts),'pdf_pages':sum(r.get('pages',0) for r in sources),
          'ppt_slides':sum(r.get('slides',0) for r in sources),'workbook_sheets':sum(r.get('sheets',0) for r in sources),
          'cell_formulas':sum(r.get('formulas',0) for r in sources),'vba_workbooks':sum(bool(r.get('vba')) for r in sources),
          'dossiers':len(list((ROOT/'knowledge-base/fuentes').glob('*.md'))),'markdown_files':len(list(ROOT.rglob('*.md'))),
          'assets':len(list((ROOT/'knowledge-base/assets/excel').glob('*.png'))),'checked_links':checked_links,'errors':errors}
    report=['# Control de cobertura','', 'Comprobación estructural y de integridad, no recalculación de los modelos financieros. Fecha de incorporación: 24/10/2026.','',
            '| Control | Resultado |','|---|---|',f'| Archivos fuente y hashes SHA-256 | {len(sources)} |',
            f'| PDF y páginas cubiertas | {counts[".pdf"]} / {data["pdf_pages"]} |',
            f'| Excel / hojas | {counts[".xlsx"]+counts[".xlsm"]} / {data["workbook_sheets"]} |',
            f'| Fórmulas de celda inspeccionadas estáticamente | {data["cell_formulas"]} |',
            f'| Libros con fuente VBA recuperada | {data["vba_workbooks"]} |',
            f'| PPT / diapositivas | {counts[".pptx"]} / {data["ppt_slides"]} |',
            f'| Fichas interpretativas | {data["dossiers"]} |',f'| Imágenes Excel deduplicadas | {data["assets"]} |',
            f'| Enlaces relativos comprobados | {checked_links} |',f'| Fallos estructurales | {len(errors)} |','',
            '## Alcance de la revisión','',
            'Las fichas enlazan cada fuente con objetivo, método y relaciones. Se revisaron los bloques teóricos, las familias de fórmulas y las imágenes incrustadas; los conceptos centrales se reescribieron con notación estructurada. La teoría completa permanece en las extracciones por página.','',
            'El control no prueba que cada fórmula docente sea correcta ni que el OCR reproduzca cada símbolo. Las diferencias concretas detectadas, los vínculos externos y los errores guardados están en [LIMITACIONES](LIMITACIONES.md).','',
            '## Arranque de un agente sin historial','',
            '- README y AGENTS explican el objetivo y la entrada.',
            '- El índice distingue fuentes, fichas, conceptos y encargo.',
            '- El mapa conecta teoría, plantillas y soluciones.',
            '- El encargo diferencia trabajo pendiente y material ya proporcionado.',
            '- Las limitaciones explicitan convenciones y defectos de fuente.',
            '- OPERACION documenta reproducción, validación y mantenimiento.']
    if errors:report+=['','## Errores','']+['- '+e for e in errors]
    write(ROOT/'knowledge-base/CONTROL_COBERTURA.md','\n'.join(report))
    print(json.dumps(data,ensure_ascii=False,indent=2))
    return bool(errors)

if __name__=='__main__':sys.exit(main())

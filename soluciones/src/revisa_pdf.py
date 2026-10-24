"""Controles mecánicos y renders para inspección humana; no sustituyen la revisión visual."""
from pathlib import Path
import json
import fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]

def main():
 d=fitz.open(ROOT/'MEMORIA.pdf');dest=ROOT.parent/'tmp/revision_pdf';dest.mkdir(parents=True,exist_ok=True)
 outside=[];pages=[]
 for i,p in enumerate(d):
  for b in p.get_text('blocks'):
   if b[0]<15 or b[2]>p.rect.width-15 or b[1]<15 or b[3]>p.rect.height-15:outside.append(dict(page=i+1,bbox=b[:4],text=b[4][:100]))
  pix=p.get_pixmap(matrix=fitz.Matrix(1.4,1.4));pix.save(dest/f'pagina-{i+1:02}.png')
  pages.append(dict(page=i+1,characters=len(p.get_text()),images=len(p.get_images())))
 for start in range(0,len(d),6):
  subset=range(start,min(len(d),start+6));sheet=Image.new('RGB',(1500,740*((len(subset)+2)//3)),'#999');draw=ImageDraw.Draw(sheet)
  for j in subset:
   im=Image.open(dest/f'pagina-{j+1:02}.png');im.thumbnail((490,700));x=((j-start)%3)*500;y=((j-start)//3)*740;sheet.paste(im,(x,y+25));draw.text((x+10,y+5),str(j+1),fill='black')
  sheet.save(dest/f'contacto-{start//6+1}.png')
 out=dict(pages=pages,blocks_outside_safe_area=outside,pdf_pages=len(d),pdf_bytes=(ROOT/'MEMORIA.pdf').stat().st_size,note='Renders para revisión visual en tmp/revision_pdf; la detección de márgenes no certifica el diseño.')
 assert not outside,outside
 (ROOT/'resultados/revision_pdf.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
if __name__=='__main__':main()

"""Ejecutar desde la raíz: python -m soluciones.src.reproduce [--deliverables]."""
import argparse, subprocess, sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--deliverables',action='store_true');args=ap.parse_args()
    root=Path(__file__).resolve().parents[2]
    modules=['ejercicio1','ejercicio2','ejercicio3','figuras']
    for name in modules:subprocess.run([sys.executable,'-m','soluciones.src.'+name],cwd=root,check=True)
    subprocess.run([sys.executable,'-m','unittest','discover','-s','soluciones/tests','-v'],cwd=root,check=True)
    if args.deliverables:
        subprocess.run([sys.executable,'-m','soluciones.src.hojas'],cwd=root,check=True)
        subprocess.run([sys.executable,'-m','soluciones.src.verifica_hojas','--recalculate'],cwd=root,check=True)
        subprocess.run(['pandoc','soluciones/MEMORIA.md','--resource-path=soluciones','--pdf-engine=xelatex','-V','mainfont=DejaVu Serif','-V','sansfont=DejaVu Sans','-V','monofont=DejaVu Sans Mono','--toc','-o','soluciones/MEMORIA.pdf'],cwd=root,check=True)
        subprocess.run([sys.executable,'-m','soluciones.src.revisa_pdf'],cwd=root,check=True)
if __name__=='__main__':main()

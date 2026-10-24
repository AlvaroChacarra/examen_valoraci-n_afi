import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
x=json.loads((ROOT/'resultados/ejercicio1.json').read_text());rows=x['exact']['by_month'];months=[r['month'] for r in rows if r['month'] in [12,24,*range(25,37)]];p=[rows[j]['first']*100 for j in months]
fig,ax=plt.subplots(figsize=(8,3));ax.bar([str(j) for j in months],p,color='#0070a8');ax.set(xlabel='Mes contractual',ylabel='Probabilidad de primera parada (%)',title='Bermuda: distribución exacta bajo Q del árbol');fig.tight_layout();fig.savefig(ROOT/'figuras/primer_ejercicio.png',dpi=180);plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(9,3.2));names=['european','bermuda','american'];axes[0].bar(['Europea','Bermuda','Americana'],[x[n]['financed'] for n in names],color=['#0070a8','#66aaca','#9bd4e8']);axes[0].set(ylabel='P&L financiado (u.m.)',title='Escenario después de 15 días')
ref=x['diffusion_references']['0.00025'];axes[1].bar(['JR mensual','JR + BS final'],[abs(x['bermuda']['initial']-ref),abs(x['smoothed']-ref)],color=['#0070a8','#66aaca']);axes[1].set(ylabel='Error absoluto (u.m.)',title='Frente a referencia de difusión');fig.tight_layout();fig.savefig(ROOT/'figuras/resultado_y_mejora.png',dpi=180)

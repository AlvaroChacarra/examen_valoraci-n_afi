"""Hojas nuevas con fórmulas visibles; cachés generadas y recálculo externo verificado."""
from pathlib import Path
import json
import numpy as np
import xlsxwriter
from .ejercicio1 import Tree,R,K,EXERCISE
from .ejercicio2 import prices as normal_prices
from .ejercicio3 import prices as fx_prices

ROOT=Path(__file__).resolve().parents[1]

def setup(path):
    w=xlsxwriter.Workbook(path);w.set_calc_mode('auto')
    w.formats_afi={
      'head':w.add_format({'bold':True,'bg_color':'#004481','font_color':'white','text_wrap':True}),
      'input':w.add_format({'bg_color':'#e8f5fa','num_format':'0.000000000'}),
      'num':w.add_format({'num_format':'0.000000000'}),
      'text':w.add_format({'text_wrap':True,'valign':'top'})}
    return w

def sheet(w,name,headers):
    s=w.add_worksheet(name);s.freeze_panes(1,1);s.write_row(0,0,headers,w.formats_afi['head']);s.set_row(0,32);s.set_column(0,len(headers)-1,18,w.formats_afi['num']);return s

def note(w,lines):
    s=sheet(w,'LEEME',['Guía del libro']);s.set_column(0,0,115,w.formats_afi['text'])
    for j,line in enumerate(lines,1):s.write(j,0,line);s.set_row(j,40)

def e1():
    w=setup(ROOT/'hojas/Ejercicio1.xlsx')
    note(w,['Derivación nueva. PDF-002 p.2; JR exacto PDF-003 pp.24–25. Unidad monetaria sin especificar.',
     'Inputs azules en Entradas. Calendarios mantienen t=m/12, t*=15/365. Volatilidades por año contractual. No alterar número de pasos ni estructura de grupos.',
     'Arbol0 y Arbol15: una fila por estado. Hasta cuatro conteos de grupos, hijos por número de fila. Precios, delta, efectivo, probabilidades y residuos por fórmulas.',
     'Estructura y enlaces de estados se generan en Python. Cambiar σ manteniendo grupos anuales funciona; cambiar la estructura/calendario requiere regenerar.',
     'M = precio suavizado, no prueba de réplica binaria. P = probabilidad viva antes de ejercicio; Q política de primera parada, positiva y estricta (tol 1e-12).',
     'La fila terminal sin payoff no se cuenta como ejercicio. El nivel0, aunque no ejercitable para bermuda, inicia masa viva1.',
     'Simulacion y Referencia contienen evidencia calculada por Python, rotulada: no sustituyen fórmulas del árbol. Reproducir con README.',
     'Fórmulas con cachés Python y recálculo real verificado con LibreOffice; véase VALIDACION.md.'])
    s=sheet(w,'Entradas',['Dato','Valor','Unidades / fuente'])
    inputs=[('Spot0',50,'u.m.'),('Spot15',52.5,'u.m.'),('K',45,'u.m.'),('r',R,'continuo/año'),('sigma1',.375,'año^-1/2'),('sigma2',.425,'año^-1/2'),('sigma3',.39,'año^-1/2'),('dias',15,'días naturales'),('base',365,'días/año')]
    for i,(k,v,u) in enumerate(inputs,1):s.write(i,0,k);s.write(i,1,v,w.formats_afi['input']);s.write(i,2,u)
    roots=[]
    for suffix,elapsed,spot in [('0',0.,50.),('15',15/365,52.5)]:
        trees={style:Tree(spot=spot,elapsed=elapsed,style=style) for style in ['european','bermuda','american']};t=trees['bermuda'];sm=Tree(spot=spot,elapsed=elapsed,smooth=True)
        cs=f'Calendario{suffix}';ts=f'Arbol{suffix}'
        c=sheet(w,cs,['mes','t','h siguiente','sigma siguiente','a','u','d','descuento','grupo (0 base)','log deriva','n1','n2','n3','n4'])
        first=[t.groups.index(g)+2 for g in range(len(t.amplitudes))]
        for j in range(37):
            row=j+2;c.write(j+1,0,j)
            tf='=0' if suffix=='0' else '=Entradas!B9/Entradas!B10'
            c.write_formula(j+1,1,tf if j==0 else f'=A{row}/12',None,float(t.times[j]))
            drift=sum(R*t.h[:j]-np.log(np.cosh(t.a[:j])))
            c.write_formula(j+1,9,'=0' if j==0 else f'=J{row-1}+Entradas!$B$5*C{row-1}-LN(COSH(E{row-1}))',None,drift)
            for g in range(4):
                col=xlsxwriter.utility.xl_col_to_name(10+g)
                count=t.groups[:j].count(g)
                c.write_formula(j+1,10+g,'=0' if j==0 else f'={col}{row-1}+IF(I{row-1}={g},1,0)',None,count)
            if j==36:continue
            c.write_formula(j+1,2,f'=B{row+1}-B{row}',None,float(t.h[j]))
            c.write_formula(j+1,3,f'=Entradas!B{6+j//12}',None,float(t.sigmas[j]))
            c.write_formula(j+1,4,f'=D{row}*SQRT(C{row})',None,float(t.a[j]))
            c.write_formula(j+1,5,f'=EXP(Entradas!$B$5*C{row}+E{row})/COSH(E{row})',None,float(t.u[j]))
            c.write_formula(j+1,6,f'=EXP(Entradas!$B$5*C{row}-E{row})/COSH(E{row})',None,float(t.d[j]))
            c.write_formula(j+1,7,f'=EXP(-Entradas!$B$5*C{row})',None,float(np.exp(-R*t.h[j])))
            c.write(j+1,8,t.groups[j])
        a=sheet(w,ts,['mes','k1','k2','k3','k4','S','intrinseco','fila hijo d','fila hijo u','europea','bermuda','americana','mejorada','delta berm','cash berm','masa viva','ejercer berm','masa primer ej','error local','error presupuesto','continuacion BS'])
        starts=[];maps=[];row=2
        for layer in t.layers:
            starts.append(row);mp={}
            for ix in np.ndindex(layer.spot.shape):mp[ix]=row;row+=1
            maps.append(mp)
        parents={}
        for j,l in enumerate(t.layers[:-1]):
            for ix,row in maps[j].items():
                for up in [0,1]:
                    child=list(ix);child[t.groups[j]]+=up;cr=maps[j+1][tuple(child)];parents.setdefault(cr,[]).append(row)
        for j,l in enumerate(t.layers):
            for ix,row in maps[j].items():
                rr=row-1;cal=j+2;a.write(rr,0,j)
                for g in range(4):a.write(rr,g+1,int(ix[g]) if g<len(ix) else 0)
                terms=[]
                for g,fr in enumerate(first):
                    kg=xlsxwriter.utility.xl_col_to_name(g+1);ng=xlsxwriter.utility.xl_col_to_name(g+10)
                    terms.append(f'(2*{kg}{row}-{cs}!{ng}{cal})*{cs}!E{fr}')
                sp=f'=Entradas!B{2 if suffix=="0" else 3}*EXP({cs}!J{cal}+'+'+'.join(terms)+')'
                a.write_formula(rr,5,sp,None,float(l.spot[ix]));a.write_formula(rr,6,f'=MAX(Entradas!$B$4-F{row},0)',None,float(max(K-l.spot[ix],0)))
                if j<36:
                    child=list(ix);child[t.groups[j]]+=1;dn=maps[j+1][ix];up=maps[j+1][tuple(child)];a.write(rr,7,dn);a.write(rr,8,up)
                    ce=lambda col:f'{cs}!H{cal}*({col}{dn}+{col}{up})/2'
                    a.write_formula(rr,9,'='+ce('J'),None,float(trees['european'].layers[j].value[ix]))
                    a.write_formula(rr,10,f'=IF(Q{row},G{row},'+ce('K')+')',None,float(l.value[ix]))
                    a.write_formula(rr,11,f'=MAX(G{row},'+ce('L')+')',None,float(trees['american'].layers[j].value[ix]))
                    continuation=f'U{row}' if j==35 else ce('M')
                    a.write_formula(rr,12,f'=MAX(G{row},{continuation})' if j in EXERCISE else '='+continuation,None,float(sm.layers[j].value[ix]))
                    a.write_formula(rr,13,f'=(K{up}-K{dn})/(F{row}*({cs}!F{cal}-{cs}!G{cal}))',None,float(l.delta[ix]))
                    a.write_formula(rr,14,f'={cs}!H{cal}*(K{dn}-N{row}*F{row}*{cs}!G{cal})',None,float(l.cash[ix]))
                    eligible=1 if j in EXERCISE else 0
                    a.write_formula(rr,16,f'=AND({eligible}=1,G{row}>0,G{row}>('+ce('K')+')+1E-12)',None,bool(l.stop[ix]))
                    a.write_formula(rr,18,f'=MAX(ABS(N{row}*F{row}*{cs}!F{cal}+O{row}/{cs}!H{cal}-K{up}),ABS(N{row}*F{row}*{cs}!G{cal}+O{row}/{cs}!H{cal}-K{dn}))',None,0.)
                    a.write_formula(rr,19,f'=N{row}*F{row}+O{row}-('+ce('K')+')',None,0.)
                    if j==35:
                        # Black-Scholes un mes; Φ por NORM.S.DIST en formato de archivo.
                        d1=f'((LN(F{row}/Entradas!$B$4)+(Entradas!$B$5+{cs}!D{cal}^2/2)*{cs}!C{cal})/({cs}!D{cal}*SQRT({cs}!C{cal})))'
                        f=f'=Entradas!$B$4*{cs}!H{cal}*NORM.S.DIST(-{d1}+{cs}!D{cal}*SQRT({cs}!C{cal}),TRUE)-F{row}*NORM.S.DIST(-{d1},TRUE)'
                        from .ejercicio1 import bs_put
                        a.write_formula(rr,20,f,None,float(bs_put(l.spot[ix],K,R,t.sigmas[j]**2*t.h[j],t.h[j])))
                else:
                    for col,style in [(9,'european'),(10,'bermuda'),(11,'american')]:a.write_formula(rr,col,f'=G{row}',None,float(l.value[ix]))
                    a.write_formula(rr,12,f'=G{row}',None,float(l.value[ix]));a.write_formula(rr,16,f'=G{row}>0',None,bool(l.stop[ix]))
                pf='=1' if j==0 else '='+ '+'.join(f'P{pr}*(1-Q{pr})/2' for pr in parents[row])
                a.write_formula(rr,15,pf,None,0. if j else 1.)
                a.write_formula(rr,17,f'=P{row}*Q{row}',None,0.)
        roots.append((ts,trees))
    s=sheet(w,'Resumen',['Contrato','Inicial','15 dias','Cambio','Financiado','Objetivo Python','Error'])
    for i,(style,col) in enumerate([('european','J'),('bermuda','K'),('american','L')],2):
        s.write(i-1,0,style);v0=roots[0][1][style].price;v1=roots[1][1][style].price
        for c,f,val in [(1,f'=Arbol0!{col}2',v0),(2,f'=Arbol15!{col}2',v1),(3,f'=C{i}-B{i}',v1-v0),(4,f'=C{i}-B{i}*EXP(Entradas!B5*Entradas!B9/Entradas!B10)',v1-v0*np.exp(R*15/365)),(5,f'={v0:.16g}',v0),(6,f'=B{i}-F{i}',0.)]:s.write_formula(i-1,c,f,None,val)
    s.write(5,0,'Bermuda mejorada');s.write_formula(5,1,'=Arbol0!M2',None,Tree(smooth=True).price)
    s=sheet(w,'Probabilidades',['Mes','Viva exacta','Primer ejercicio','Condicionada','MC','IC95 inferior','IC95 superior'])
    data=json.loads((ROOT/'resultados/ejercicio1.json').read_text())
    for i,j in enumerate(sorted(EXERCISE),2):
        t=roots[0][1]['bermuda'];start=2+sum(l.spot.size for l in t.layers[:j]);end=start+t.layers[j].spot.size-1
        exact=data['exact']['by_month'][j];mc=next(r for r in data['simulation']['first_exercise'] if r['month']==j)
        s.write(i-1,0,j)
        for col,f,v in [(1,f'=SUM(Arbol0!P{start}:P{end})',exact['survival']),(2,f'=SUM(Arbol0!R{start}:R{end})',exact['first']),(3,f'=C{i}/B{i}',exact['conditional'])]:s.write_formula(i-1,col,f,None,v)
        s.write_row(i-1,4,[mc['prob'],*mc['ci95']])
    s=sheet(w,'Simulacion',['Mes','Spot senda 0','Valor','Delta','Cash','Viva'])
    for i,r in enumerate(data['simulation']['path_start'],1):s.write_row(i,0,list(r.values()))
    s=sheet(w,'Referencia',['dx logS','Bermuda difusión (Python)'])
    for i,(dx,val) in enumerate(data['diffusion_references'].items(),1):s.write_row(i,0,[float(dx),val])
    w.close()


def e2():
    w=setup(ROOT/'hojas/Ejercicio2.xlsx');note(w,['Ejemplo ilustrativo, no datos de PDF-002. Pago T, fixing [T,U], una curva; σ absoluta.',
     'Inputs editables azules; P(t,T) se deriva de P(t,U) y f. Varianza constante σ²(T−t). Fórmulas generales en MEMORIA §2.',
     'No truncar la normal. Limitación: cola bajo −1/δ incompatible globalmente con bonos positivos. Paridad entre contratos de idéntica fecha de pago.',
     'Cuadratura contiene sólo evidencia Python original; se debe regenerar tras editar inputs para renovar ese control.'])
    s=sheet(w,'Calculo',['Símbolo','Valor / fórmula','Unidad']);s.set_column(0,0,32);s.set_column(1,2,24)
    entries=[('f',.03),('K',.032),('T-t',2.),('delta',.5),('sigma_n',.01),('P(t,U)',np.exp(-.075)),('Nom',1e6)]
    for row,(name,v) in enumerate(entries,2):s.write(row-1,0,name);s.write(row-1,1,v,w.formats_afi['input'])
    formulas={9:('v','=B6^2*B4'),10:('s','=SQRT(B9)'),11:('d','=IF(B10=0,0,(B2-B3)/B10)'),12:('Phi(d)','=NORM.S.DIST(B11,TRUE)'),13:('phi(d)','=NORM.S.DIST(B11,FALSE)'),14:('A','=IF(B10=0,MAX(B2-B3,0),(B2-B3)*B12+B10*B13)'),15:('B','=IF(B10=0,MAX(B3-B2,0),(B3-B2)*(1-B12)+B10*B13)'),16:('P(t,T)','=B7*(1+B5*B2)'),17:('FRA','=B8*B5*B7*((1+B5*B2)*(B2-B3)+B5*B9)'),18:('caplet','=B8*B5*B7*((1+B5*B2)*B14+B5*B9*B12)'),19:('floorlet','=B8*B5*B7*((1+B5*B2)*B15-B5*B9*(1-B12))'),20:('paridad residual','=B18-B19-B17'),21:('K equilibrio','=B2+B5*B9/(1+B5*B2)'),22:('caplet cuadratura Python',None),23:('diferencia control','=B18-B22')}
    result=json.loads((ROOT/'resultados/ejercicio2.json').read_text())
    # Las cachés se actualizan por recálculo real; las salidas principales sí llevan valor Python.
    cached={17:result['closed']['fra'],18:result['closed']['caplet'],19:result['closed']['floorlet']}
    for row,(name,f) in formulas.items():
        s.write(row-1,0,name)
        if f:s.write_formula(row-1,1,f,None,cached.get(row,0.))
        else:s.write(row-1,1,result['quadrature']['caplet'])
    units=['tipo/año','tipo/año','años','años','tipo/raíz año','adimensional','moneda']
    for i,u in enumerate(units,1):s.write(i,2,u)
    w.close()


def e3():
    w=setup(ROOT/'hojas/Ejercicio3.xlsx');note(w,['Ejemplo ilustrativo, no datos del enunciado ni de la cesta. S USD; X EUR/USD; valoración Q EUR.',
     'Conversión quanto fija λ=1 EUR/USD. q, rd, rf continuos. Inputs azules. μS=rf−q−ρσSσX.',
     'Desarrollos (1)–(10) y corrección de d en diap.25 en MEMORIA §3. Fórmulas usuales convierten todo el precio por X0.',
     'Las filas Python son controles originales; regenerar si se cambian inputs. Un denominador σN cero se marca sin correlación.'])
    s=sheet(w,'Calculo',['Símbolo','Valor / fórmula','Unidad']);s.set_column(0,0,32);s.set_column(1,2,24)
    vals=[('S0',100,'USD'),('K',105,'USD'),('X0',.9,'EUR/USD'),('rd',.03,'1/año'),('rf',.02,'1/año'),('q',.01,'1/año'),('sigmaS',.25,'1/raíz año'),('sigmaX',.12,'1/raíz año'),('rho',.4,'adim.'),('T',2,'años'),('lambda',1,'EUR/USD fijo')]
    for row,(k,v,u) in enumerate(vals,2):s.write(row-1,0,k);s.write(row-1,1,v,w.formats_afi['input']);s.write(row-1,2,u)
    fs={13:('muS','=B6-B7-B10*B8*B9'),14:('sigmaM','=B9'),15:('sigmaN','=SQRT(B8^2+B9^2+2*B10*B8*B9)'),16:('rhoMN','=IF(OR(B15=0,B9=0),"No definida",(B9+B10*B8)/B15)'),17:('F usual USD','=B2*EXP((B6-B7)*B11)'),18:('F quanto USD','=B2*EXP(B13*B11)'),19:('w','=B8*SQRT(B11)'),20:('d1 usual','=IF(B19=0,0,LN(B17/B3)/B19+B19/2)'),21:('d2 usual','=B20-B19'),22:('d1 quanto','=IF(B19=0,0,LN(B18/B3)/B19+B19/2)'),23:('d2 quanto','=B22-B19'),24:('Forward usual EUR','=B4*(B2*EXP(-B7*B11)-B3*EXP(-B6*B11))'),25:('Forward quanto EUR','=B12*EXP(-B5*B11)*(B18-B3)'),26:('Call usual EUR','=B4*EXP(-B6*B11)*IF(B19=0,MAX(B17-B3,0),B17*NORM.S.DIST(B20,TRUE)-B3*NORM.S.DIST(B21,TRUE))'),27:('Call quanto EUR','=B12*EXP(-B5*B11)*IF(B19=0,MAX(B18-B3,0),B18*NORM.S.DIST(B22,TRUE)-B3*NORM.S.DIST(B23,TRUE))'),28:('Put usual EUR','=B4*EXP(-B6*B11)*IF(B19=0,MAX(B3-B17,0),B3*NORM.S.DIST(-B21,TRUE)-B17*NORM.S.DIST(-B20,TRUE))'),29:('Put quanto EUR','=B12*EXP(-B5*B11)*IF(B19=0,MAX(B3-B18,0),B3*NORM.S.DIST(-B23,TRUE)-B18*NORM.S.DIST(-B22,TRUE))'),30:('Paridad usual','=B26-B28-B24'),31:('Paridad quanto','=B27-B29-B25')}
    res=json.loads((ROOT/'resultados/ejercicio3.json').read_text());cache={24:res['closed']['forward'],25:res['closed']['forward_quanto'],26:res['closed']['call'],27:res['closed']['call_quanto'],28:res['closed']['put'],29:res['closed']['put_quanto']}
    for row,(label,f) in fs.items():s.write(row-1,0,label);s.write_formula(row-1,1,f,None,cache.get(row,0.))
    s=sheet(w,'Contrastes',['Contrato','Fórmula Python','Cuadratura','MC','IC95 inferior','IC95 superior'])
    for row,k in enumerate(res['quadrature'],1):s.write_row(row,0,[k,res['closed'][k],res['quadrature'][k],res['mc']['estimates'][k]['mean'],*res['mc']['estimates'][k]['ci95']])
    w.close()

if __name__=='__main__':
    e1();e2();e3();print('Tres libros generados con fórmulas')

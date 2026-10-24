# Paquete para auditoría en otra conversación

La revisión exacta de entrega queda fijada en la sección de cierre al final de este documento. No se debe auditar un `HEAD` móvil sin anotar su SHA. El commit de partida del encargo es `25b879067144d380edd08b0ecf19dd861410d628`; rama de trabajo `solucion/mefc-2026`, sin modificar main.

## Orden de lectura y archivos

1. `AGENTS.md`, índice y documentos obligatorios de `knowledge-base/`; `raw/encargo/valoracion-mefc-2026.pdf`, las 25diapositivas de `ejercicio-3-desarrollo.pptx` y PDF de instrucciones. Las extracciones son ayuda, originales son autoridad.
2. [Matriz](MATRIZ_CUMPLIMIENTO.md), [memoria](MEMORIA.md), [validación](VALIDACION.md), [guía de defensa](DEFENSA.md).
3. `src/ejercicio1.py`, `ejercicio2.py`, `ejercicio3.py`, `hojas.py`, `verifica_hojas.py`, `figuras.py`, `reproduce.py` y `tests/` completos.
4. `hojas/Ejercicio1.xlsx`, `Ejercicio2.xlsx`, `Ejercicio3.xlsx`, PDF, JSON y logs de `resultados/`.
5. `auditoria/` conserva la primera revisión independiente, sus scripts y contrastes; no usar su veredicto como sustituto de comprobar el contrato.

## Decisiones que merecen challenge

- E1: JR exacto con p=.5 y cosh; mensual y volatilidad por intervalos anuales. Estados por conteos en grupos de amplitud común. No recombinación global falsa ni malla uniforme en varianza.
- E1b: t*=15/365, fechasj/12 inalteradas; primer intervalo residual como nuevo grupo. Preferencia medida por P&L por unidad y coste financiado, no por nueva prima.
- E1c: política con tolerancia1e−12, continuar empates, payoff cero expira; primera parada bajoQ; riqueza autofinanciada sin reiniciar cash teórico. Contrastar probabilidades tanto incondicionales como dadas supervivencia.
- E1d: BS sólo en continuación del mes35, conservando ejercicio inmediato y36 intervalos. Referencia de difusión con las mismas14 fechas, convergencia espacial y contraste PDE independiente. No usar la referencia como solución solicitada ni extender a ella la réplica binaria.
- E2: pagoT, medida del bonoU, factor multiplicativo1+δF, momentos normales de volatilidad absoluta; sin denominador extra ni momentos lognormales. Normal ilimitada declarada como aproximación, con incompatibilidad global respecto de bonos positivos.
- E3: FX EUR/USD, Q EUR; retorno total conq. Derivar ambas martingalas y todas las covariaciones; transformarρMN frente aρS,FX; ajuste quanto negativo. Usual convertido porFXterminal, quanto porλfijo. Corregir signo de rf dentro de d en diap25 y t/T donde corresponde.
- E2/E3: sólo desarrollos simbólicos exigidos; los ejemplos numéricos son ilustraciones expresamente rotuladas, no inputs docentes.

## Resultados a contrastar

|Magnitud|Resultado|
|---|---:|
|E1 europea inicial|8,921639042394|
|E1 bermuda inicial|9,162907590996|
|E1 americana mensual inicial|9,197452168513|
|E1 europea / bermuda / americana tras15d|8,175125718868 / 8,390743020599 / 8,419723401651|
|E1 bermuda suavizada|9,139201101421|
|Referencia difusión FFT dx=.00025|9,113667958805|
|Primera parada exacta mes12 / mes36|.019287109375 / .060647827864159|
|E2 FRA simbólico / (Nom δ P_U)|(1+δf)(f−K)+δv|
|E2 caplet simbólico / (Nom δ P_U)|(1+δf)[(f−K)Φ(d)+sφ(d)]+δvΦ(d)|
|E3 derivaS bajoQEUR|rf−q−ρσSσX|
|E3 forward usual|X0[S0exp(−qT)−Kexp(−rfT)]|
|E3 call usual|BlackUSD porX0 completo|

## Reproducción y preguntas de revisión

Comandos completos y dependencias en [README](README.md). Ejecutar `python -m soluciones.src.reproduce` y los dos validadores documentales. Para acreditar además el motor Excel y PDF: `python -m soluciones.src.reproduce --deliverables` (requiere LibreOffice, Pandoc y XeLaTeX). Para repetir contrastes independientes, consultar los scripts de `auditoria/`.

Priorizar revisión material: ¿son fieles los calendarios y monedas? ¿la simulación replica el modelo valorado? ¿las masas se absorben una sola vez? ¿el factor de pago anticipado se encuentra en el lugar correcto? ¿las covariaciones fijan el signo quanto? ¿se justifica la referencia de mejora? ¿las hojas recalculan de verdad? ¿los límites y paridades usan contratos equivalentes? Separar errores, evidencia insuficiente y mejoras editoriales. No modificar raw ni aceptar caches docentes como solución.

La auditoría posterior está preparada pero no se afirma realizada en otra conversación. La revisión independiente de esta ejecución y sus límites se documentan por separado.

## Cierre: versión exacta para auditar

**Código, entradas, fórmulas y entregables auditados:** `92be7d90c6d1961e90e6a308eb9980accbd17156`. Consultar esa revisión exacta para reproducir el paquete técnico; los commits posteriores de cierre sólo incorporan este dictamen y sus punteros/evidencias.

**Dictamen integrado: PASS**, sin hallazgos materiales abiertos, en [REVISION_INTEGRADA.md](auditoria/REVISION_INTEGRADA.md). Incluye reproducción completa aislada, 12 pruebas, recálculo completo forzado y cambio de entradas en los tres libros. [Hashes de los entregables](auditoria/artefactos_92be7d9.json), [cotejo XLSX](auditoria/xlsx_verificados_92be7d9.json), [sensibilidad de entradas](auditoria/perturbacion_92be7d9.json) y [log de reproducción](auditoria/reproduccion_92be7d9.log) fijan la evidencia.

La versión `7bc599d` no debe usarse como entrega aceptada: su [revisión integrada fallida](auditoria/REVISION_INTEGRADA_7bc599d.md) detectó conservación de cachés y una función normal incompatible al cálculo efectivo. La corrección en `92be7d9` recalcula, verifica auxiliares y supera los controles con inputs modificados; el núcleo matemático mantiene los mismos resultados. Conservar el fallo es parte de la trazabilidad, no un pendiente abierto.

Para repetir la prueba de entradas sobre el commit exacto:

```bash
python soluciones/auditoria/perturba_inputs_xlsx.py --commit 92be7d90c6d1961e90e6a308eb9980accbd17156 --output /tmp/inputs_92be7d9.json
```

No queda trabajo técnico abierto en los tres ejercicios y la call usual adicional. Los nombres de integrantes y la entrega/defensa personal son tareas del alumno; la cesta permanece opcional pendiente. Main y raw se conservan intactos.

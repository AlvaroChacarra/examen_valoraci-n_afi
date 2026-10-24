# Revisión independiente de la entrega corregida

**VERDICT: PASS.** Modo standard. Conformidad FULL dentro del alcance aprobado. Confianza HIGH. La entrega integrada de código y artefactos en **`92be7d90c6d1961e90e6a308eb9980accbd17156`** resuelve los dos hallazgos materiales de la versión anterior y es apta para su uso académico declarado. No quedan BLOCKER, HIGH ni MEDIUM abiertos.

Este dictamen **supersede el FAIL de `7bc599d` exclusivamente para la versión corregida `92be7d9`**, después de verificar sus cambios y binarios. El [informe histórico](REVISION_INTEGRADA_7bc599d.md), su log y sus observaciones se conservan sin convertir el fallo en un supuesto éxito anterior. El PASS del [núcleo matemático](REVISION_5c0e1df.md) permanece vigente; los cambios posteriores no alteran las primas ni las derivaciones financieras aprobadas.

## Contrato, alcance y versión exacta

Auditoría realizada el 24/10/2026, aproximadamente 22:37–22:41 UTC, sobre el commit completo anterior, rama `solucion/mefc-2026`. Baseline del encargo: `25b879067144d380edd08b0ecf19dd861410d628`.

Se conservó el contrato congelado desde PDF-002 pp.1–4, PPT-001 diap.1–25 y PDF-001 pp.1–2. Se revisaron el delta desde `7bc599d`, los XLSX comprometidos, fórmulas y valores guardados, PDF de 18 páginas, README, ruta `reproduce --deliverables`, defensa, matriz, validación y separación de evidencia. La cesta excluida y los nombres del grupo no forman parte de este gate. No se modificó implementación ni se sobrescribieron los binarios auditados: toda regeneración y perturbación se hizo en copias aisladas.

## Cierre de hallazgos materiales

|ID anterior|Corrección verificada|Estado|
|---|---|---|
|I-01, función normal no reconocida|Las fórmulas usan `NORMDIST(x,0,1,acumulada)`. Al editar inputs y recalcular efectivamente funcionan la continuación BS E1, caplet/floorlet E2 y calls/puts E3.|CLOSED|
|I-02, cachés iniciales admitidas como recálculo|Perfil aislado con `OOXMLRecalcMode=0`; cotejo por nodo de masa viva/absorbida, delta/cash y BS; auxiliares E2/E3; fixture con cachés deliberadamente falsas. El nuevo gate rechaza `7bc599d` en `Arbol0!P3=0` frente a 0,5 esperado.|CLOSED|

La documentación retira expresamente la conversión inicial con perfil por defecto como evidencia suficiente y explica la corrección. No se cerraron hallazgos rellenando más cachés Python: se acreditó cálculo efectivo del motor.

## Evidencia ejecutada sobre la corrección

**Binarios comprometidos.** Se comprobaron los bytes de los cuatro entregables contra `git show 92be7d9`, conservando SHA-256 y tamaños en [artefactos_92be7d9.json](artefactos_92be7d9.json). La lectura `data_only` observa, entre otros:

- E1 `Arbol0!P3=P4=0,5` y `M2=9,13920110142147`.
- E2 varianza `B9=0,0002`, `Phi(d)=0,443768541990857`, strike de equilibrio `0,0300985221674877`.
- E3 `muS=-0,002`, `sigmaM=0,12`, `sigmaN=0,317647603485372` y `rhoMN=0,692591405022615`.

Se ejecutó el verificador ampliado sobre **los XLSX exactos de la entrega**, sin regenerarlos: 46.868 estados, 14 probabilidades y 33 auxiliares E2/E3 pasan; no hay errores de fórmula. Máximo error de valores de nodo: **6,139089236967266e-12**, frente a tolerancia 1e-9. Se verifican además masas, política, delta/cash, continuación BS y residuos locales/presupuesto. Evidencia en [xlsx_verificados_92be7d9.json](xlsx_verificados_92be7d9.json).

**Edición real de inputs.** El [script independiente](perturba_inputs_xlsx.py) extrae los libros del commit por `git show`, edita copias, elimina las cachés al guardarlas con openpyxl, recalcula con un perfil aislado y contrasta resultados con el código del mismo commit. Pasan todos los controles numéricos y el escaneo de errores de los tres libros:

|Cambio en copia|Resultado recalculado observado|
|---|---:|
|E1, S0=55: europea / bermuda / americana|7,60554124101848 / 7,80067246982206 / 7,82663204067586|
|E1, S0=55: bermuda mejorada|7,82194183667965|
|E2, sigma_n=0,02: caplet / floorlet|4.942,73658202677 / 5.698,84752338454|
|E3, rho=-0,3 y FX0=1,1: call usual / quanto|13,8257741163786 / 13,2764848330199|

Inputs, salidas, checks y ausencia de errores se conservan en [perturbacion_92be7d9.json](perturbacion_92be7d9.json). Esto demuestra que las celdas calculan y propagan inputs; no se limita a comparar precios precargados.

**Reproducción completa.** Se extrajo un archivo del commit en `/tmp/mefc_integrated_audit_92be7d9` y se ejecutó desde allí `python -m soluciones.src.reproduce --deliverables`: **exit 0**, generación de JSON/figuras, 12 tests, fixture de recálculo, generación y recálculo de los tres libros, cotejo ampliado, compilación y revisión mecánica del PDF. El [log completo](reproduccion_92be7d9.log) queda preservado. El fixture de cachés −999 produce 4 para el cuadrado y 0,5 para Phi(0).

**PDF.** El PDF comprometido tiene 18 páginas y SHA-256 `09a280ec183c61fc7d4440874f948f2b469b070d5c554f08caa4300c517cb5e7`. Se comprobó que sus 18 renders son idénticos píxel a píxel a los de `7bc599d`, cuyas páginas completas ya se habían revisado visualmente. También el PDF regenerado en la copia aislada coincide visualmente en las 18 páginas con el PDF comprometido. Las diferencias binarias son metadatos. No se identifican recortes ni pérdida de contenido material; la tabla de convergencia se conserva completa.

**Fuentes y documentos.** Ambos validadores documentales pasan en la copia del commit: 59 fuentes, 620 páginas PDF, 25 diapositivas, 60 hojas originales, 60.701 fórmulas docentes, 797 nombres y 771 enlaces, sin errores ni huérfanos. No hay cambios de `raw/` frente al baseline. README, matriz y guía de defensa son coherentes con el contrato; distinguen ejemplos ilustrativos, evidencia Python, cálculos de hoja y tareas personales del alumno.

## Reproducción de esta auditoría

Desde la raíz del repositorio:

```bash
python soluciones/auditoria/perturba_inputs_xlsx.py --commit 92be7d90c6d1961e90e6a308eb9980accbd17156 --output /tmp/inputs_92be7d9.json
```

Para repetir la ruta completa preservando los binarios entregados, crear una copia o worktree del commit explícito y ejecutar allí:

```bash
python -m soluciones.src.reproduce --deliverables
python scripts/validate_knowledge_base.py
python scripts/review_readiness.py
```

Las pruebas matemáticas independientes y sus comandos se conservan en la primera revisión: recursión escalar y propagación E1, PDE Crank–Nicolson frente a FFT, integración directa E2 y bidimensional E3. Los tests existentes no se usaron como único oráculo.

## Límites, riesgo residual y siguiente paso

No se ha ejecutado Microsoft Excel: la prueba efectiva usa el motor LibreOffice declarado y funciones compatibles. No se exige identidad binaria tras regenerar; sí identidad numérica y visual del contenido. Las ediciones verificadas preservan la estructura de estados/calendario; cambios estructurales exigen regenerar, como explica README. La evidencia Python/MC y la memoria editorial no se actualizan al editar aisladamente un input en Excel.

Se mantienen los límites metodológicos ya declarados: americana en malla mensual; cobertura perfecta del árbol puro; probabilidades bajo Q; normal formal de E2 sin bonos globalmente positivos; referencia de difusión convergida empíricamente y cuadratura validada en las escalas estudiadas. No son hallazgos nuevos ni reclamaciones de universalidad.

**Required before next step: None en el alcance técnico auditado.** Puede cerrarse con referencias a este SHA y evidencia sin cambios funcionales. Completar nombres y realizar entrega/defensa siguen siendo tareas personales del alumno. Cualquier cambio posterior de código, inputs, fórmulas, artefactos o método necesita una revisión proporcional; un commit posterior sólo documental debe identificarse como tal. Mejoras no bloqueantes adicionales: ninguna necesaria para el encargo.

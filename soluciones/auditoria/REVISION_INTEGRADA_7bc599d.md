# Revisión independiente de la entrega integrada

## Dictamen vigente sobre la versión revisada

**FAIL para la entrega integrada del commit `7bc599d39a34def20e3e633309167db68d29a3cd`.** Modo standard; conformidad PARTIAL por el requisito material de hojas recalculadas y reproducibles. El núcleo matemático conserva el PASS de [REVISION_5c0e1df.md](REVISION_5c0e1df.md). Las fórmulas normales de los XLSX fallan al recalcular efectivamente y el procedimiento declarado como recálculo puede conservar las cachés iniciales sin detectar el problema. Se requiere corregir y volver a auditar esos artefactos antes de entregar este paquete.

Revisión ejecutada el 24/10/2026, aproximadamente 22:30–22:35 UTC. El avance anterior del núcleo se auditó por separado. No se alteraron implementación ni binarios; la generación y las perturbaciones se realizaron en copias bajo `/tmp/`. Sólo se escriben los artefactos de auditoría autorizados dentro de `soluciones/auditoria/`.

## Alcance y baseline

Fuentes y contrato conservan la jerarquía de la primera revisión: PDF-002 pp.1–4, PPT-001 diap.1–25 y PDF-001 pp.1–2. Se revisó el delta desde `5c0e1df`, los tres XLSX del commit, sus fórmulas y valores guardados, el PDF de 18 páginas, README, `reproduce --deliverables`, generador y verificador de hojas, guía de defensa, matriz de cumplimiento, validación y separación de evidencia. La cesta excluida y los nombres del grupo no son parte de este gate.

La corrección de acumulación de masa en `european_convolution` y el acotamiento de la senda ilustrativa a su primera parada no alteran precios ni la estrategia de réplica. Los cambios de memoria son editoriales y aclaran el número de escenarios de E2. La valoración matemática aprobada no se reabre por el defecto del empaquetado Excel.

## Hallazgos materiales

### I-01 — BLOCKER: las opciones de los XLSX fallan al calcular sus fórmulas

**Evidencia.** En copias de los libros comprometidos, se editaron inputs mediante openpyxl y se guardaron sin cachés; después se abrió y guardó con LibreOffice mediante el comando documentado. El cálculo efectivo da:

|Libro|Edición y celda afectada|Resultado guardado|
|---|---|---|
|E1|Spot inicial 55; `Arbol0!M2` y `Arbol0!U14275`|`#NAME?`|
|E2|sigma_n 0,02; `Calculo!B12`, `B13`, `B18`, `B19`|`#NAME?`|
|E3|rho −0,3 y FX0 1,1; `Calculo!B26:B29`|`#NAME?`|

Las fórmulas guardadas llaman a `norm.s.dist(...)`, que el motor probado no reconoce en esa representación OOXML. La generación se localiza en `src/hojas.py`: continuación BS E1 alrededor de líneas 102–105; momentos E2 en línea 141; calls/puts E3 en línea 162 (líneas del commit auditado). Las raíces ordinarias de E1 sí se actualizan al cambiar el spot: el problema no es una copia sin ninguna dependencia de cálculo.

**Impacto.** No funcionan de forma reproducible el suavizado BS ni caplet/floorlet ni calls/puts al usar el recálculo de la entrega. Las cifras principales guardadas en el primer paquete no acreditan que esas fórmulas se hayan evaluado.

**Corrección mínima.** Emitir una función de distribución normal compatible con el formato OOXML y el motor utilizado, recalcular efectivamente todos los libros y sustituirlos sólo tras verificar valores y ausencia de errores.

**Verificación requerida.** Abrir una copia sin cachés, cambiar al menos un input por libro, forzar cálculo y guardar; cotejar todas las salidas, incluida la mejorada de E1, y escanear errores. Confirmar además que los libros finales ya guardados contienen esos valores calculados.

### I-02 — HIGH: el gate permite un falso positivo de recálculo

**Evidencia.** En los binarios exactos de `7bc599d`, `openpyxl(..., data_only=True)` observa:

- E1 `Arbol0!P2=1`, `P3=P4=0`; las dos masas del primer mes deben ser 0,5. Las probabilidades agregadas muestran cifras correctas porque proceden de otra caché inicial.
- E2 `Calculo!B9=B10=B11=B12=B14=B16=B21=0`; por ejemplo la varianza B9 debe ser 0,0002. Los precios principales sí contienen las cachés Python iniciales.
- E3 `Calculo!B13:B23=0`; por ejemplo muS debe ser −0,002, sigmaM 0,12 y sigmaN aproximadamente 0,3176476. Las cuatro primas guardadas son las cachés Python.

`hojas.py` inicializa esos auxiliares a cero (E1 líneas 109–111, E2 143–147, E3 163–164). `verifica_hojas.py` valida spots/valores cacheados y agregados que también traen su caché, pero omite masas vivas completas y auxiliares E2/E3 (líneas 28–42). La conversión de LibreOffice de las líneas 54–58 conserva dichos valores; no garantiza cálculo efectivo.

Se reprodujo **`python -m soluciones.src.reproduce --deliverables` con exit 0** en una copia extraída del commit bajo `/tmp/mefc_integrated_audit_7bc599d`. El resultado vuelve a mostrar las masas 0 y los auxiliares 0. Log completo de esa ejecución: [reproduccion_7bc599d.log](reproduccion_7bc599d.log). La posterior perturbación efectiva expuso I-01; sus observaciones quedan en [perturbacion_7bc599d.json](perturbacion_7bc599d.json).

**Impacto.** El informe de cotejo y las afirmaciones de recálculo completo no están acreditados por el gate actual; un usuario que consulte valores guardados recibe una hoja internamente inconsistente.

**Corrección mínima.** Forzar recálculo duro del motor, ampliar el gate a auxiliares, masas y continuaciones que no traigan ya la cifra Python, y corregir la descripción de evidencia hasta que el nuevo proceso pase. No basta con rellenar más cachés desde Python y conservar la misma afirmación de recálculo independiente.

**Verificación requerida.** Un libro con cachés iniciales incorrectas o ausentes debe recalcularse correctamente o hacer fallar el proceso. El verificador debe rechazar expresamente los libros del commit `7bc599d` por sus masas/auxiliares incorrectos.

## Reproducción mínima de I-01 / I-02

Lectura de evidencia guardada, desde la raíz del checkout de `7bc599d`:

```python
import openpyxl
w = openpyxl.load_workbook('soluciones/hojas/Ejercicio2.xlsx', data_only=True)
print(w['Calculo']['B9'].value)   # 0; debería 0.0002
print(w['Calculo']['B18'].value)  # 2232.64768967118, caché inicial
```

Para aislar la prueba de edición y cálculo del commit histórico desde cualquier checkout posterior:

```python
from pathlib import Path
from io import BytesIO
import subprocess, openpyxl
base = Path('/tmp/mefc_7bc_input'); src = base/'input'; dst = base/'output'
src.mkdir(parents=True, exist_ok=True); dst.mkdir(exist_ok=True)
blob = subprocess.check_output(['git', 'show',
  '7bc599d39a34def20e3e633309167db68d29a3cd:soluciones/hojas/Ejercicio2.xlsx'])
w = openpyxl.load_workbook(BytesIO(blob)); w['Calculo']['B6'] = .02
w.save(src/'Ejercicio2.xlsx')
subprocess.run(['soffice', '-env:UserInstallation=file:///tmp/mefc_7bc_minimal_profile',
  '--headless', '--convert-to', 'xlsx', '--outdir', str(dst),
  str(src/'Ejercicio2.xlsx')], check=True, timeout=300)
w = openpyxl.load_workbook(dst/'Ejercicio2.xlsx', data_only=True)
print(w['Calculo']['B9'].value, w['Calculo']['B18'].value)
# Observado: 0.0008, '#NAME?'
```

## Evidencia de las áreas restantes

**PDF.** El binario inspeccionado coincide exactamente con el del commit: SHA-256 `71738e5931a07c7dd99d04b6bff9b057f6bcd105f2eee78b5eca59ef9aeb3bf5`. Son 18 páginas. Se renderizaron desde ese binario y se revisaron todas mediante tres contactos de seis páginas, además del texto extraído. No se identifican recortes, ecuaciones desaparecidas ni tablas ilegibles que afecten a comprensión; la tabla de convergencia está completa en una página. Los renders independientes están bajo `/tmp/mefc_integrated_pdf`.

**XLSX exactos.** Se compararon bytes contra `git show` y se escanearon los XML. E1 contiene 591.018 fórmulas; E2 14 y E3 19. No hay VBA, vínculos externos ni errores de celda guardados en los originales, pero esa ausencia no detecta I-01 cuando se conservan las cachés. El escaneo original está en [scan_xlsx_7bc599d.json](scan_xlsx_7bc599d.json).

**Pruebas y documentos.** Los 11 tests vuelven a pasar en la copia aislada. Los dos validadores documentales pasan: 59 fuentes originales, 620 páginas PDF, 25 diapositivas, 60 hojas, 60.701 fórmulas docentes, 797 nombres, 767 enlaces, sin errores ni huérfanos. `git diff` entre baseline y entrega no modifica `raw/`. La guía de defensa conserva correctamente el proceso y los límites de PDF-001. README separa ejemplos de E2/E3, evidencia Python, memoria editorial y pasos manuales del alumno. Su afirmación de hojas ya recalculadas queda condicionada a corregir I-01/I-02.

## Riesgo residual, límites y siguiente paso

No se ha ejecutado Excel de Microsoft; se probó el motor LibreOffice declarado por el proyecto. No se exige compatibilidad universal ni se audita la cesta excluida. Se mantienen los límites financieros de la primera revisión: americana mensual, probabilidad de valoración, normal formal sin bonos globalmente positivos y precisión de difusión empírica.

**Antes de entregar:** resolver I-01/I-02, congelar un commit nuevo y revisar delta, libros recalculados y evidencia nueva. No hace falta rehacer las matemáticas aprobadas ni ampliar la arquitectura. Confianza HIGH en los hallazgos, que están reproducidos; no se emite todavía PASS para una versión posterior no inspeccionada.

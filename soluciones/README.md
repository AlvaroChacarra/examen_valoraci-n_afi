# Entrega de Valoración MEFC 2026

Resolución nueva de los tres ejercicios obligatorios y la call usual de +0,5. El extra independiente de cesta de +1 queda **opcional pendiente**. Los originales docentes no se modifican. Ningún ejemplo de E2/E3 es un dato del enunciado.

- [Memoria canónica](MEMORIA.md) y [PDF](MEMORIA.pdf).
- [Hojas E1](hojas/Ejercicio1.xlsx), [E2](hojas/Ejercicio2.xlsx), [E3](hojas/Ejercicio3.xlsx): consultar LEEME antes de editar. Se entregan recalculadas realmente con LibreOffice, con fórmulas y valores guardados actuales.
- [Matriz de cumplimiento](MATRIZ_CUMPLIMIENTO.md), [validación](VALIDACION.md), [defensa individual](DEFENSA.md) y [auditoría posterior](AUDITORIA.md).
- [Estado operativo](ESTADO.md), `src/` para código, `tests/`, `resultados/` y `figuras/` para evidencia.

## Reproducir desde la raíz del repositorio

Entorno probado: Python 3.12.14, dependencias fijadas en requirements.txt. Instalar en un entorno virtual si se prepara otra máquina:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r soluciones/requirements.txt
python -m soluciones.src.reproduce
```

El comando ejecuta E1, E2 y E3, regenera sus JSON y figuras y pasa las pruebas. Por separado:

```bash
python -m soluciones.src.ejercicio1
python -m soluciones.src.ejercicio2
python -m soluciones.src.ejercicio3
python -m unittest discover -s soluciones/tests -v
python scripts/validate_knowledge_base.py
python scripts/review_readiness.py
```

Para regenerar también hojas, recalcularlas y compilar PDF, se necesitan **LibreOffice/soffice, Pandoc, XeLaTeX y fuentes DejaVu** instalados en el sistema:

```bash
python -m soluciones.src.reproduce --deliverables
```

La generación completa tarda unos minutos; E1 contiene 46.868 estados entre sus dos escenarios y más de 900.000 celdas no vacías. No ejecutar dos instancias de recálculo simultáneas sobre los mismos archivos. La versión final de las hojas es la recalculada, tras el cotejo de todos los spots y valores de cada estado con Python. Para comprobar las hojas ya entregadas sin LibreOffice:

```bash
python -m soluciones.src.verifica_hojas
```

Para el ciclo manual de hojas:

```bash
python -m soluciones.src.hojas
python -m soluciones.src.verifica_hojas --recalculate
```

El primer comando genera fórmulas con cachés iniciales parciales; **es necesario el segundo antes de distribuir los libros**. Sin él, algunas celdas auxiliares no tienen aún su valor recalculado. El segundo configura un perfil aislado de LibreOffice con `OOXMLRecalcMode=0` para forzar recálculo completo al abrir, convierte en `tmp/recalculadas`, coteja valores principales y auxiliares, y sustituye las hojas de entrega. La conversión con el perfil por defecto puede conservar cachés sin recalcular: por sí sola no acredita cálculo real. Falla ante errores de fórmula o desviaciones materiales; no presupone éxito sólo por el código de salida de soffice.

Las fórmulas Excel permiten cambiar inputs preservando la estructura del contrato. La estructura de estados/hijos depende del calendario y de los grupos de volatilidad: para cambiar éstos hay que regenerar el libro. Las columnas de evidencia Python (MC, referencia y controles) se renuevan al ejecutar el código, no por editar inputs de Excel. Los libros son .xlsx sin macros ni vínculos externos. La normal se implementa con la función compatible `NORMDIST(x,0,1,acumulada)`.

Los números son reproducibles con las semillas indicadas; el binario PDF/XLSX puede cambiar por metadatos de fecha, versión de fuentes u ofimática. No se promete identidad binaria. La memoria se mantiene editorialmente: los scripts no reescriben automáticamente sus tablas si se cambian los inputs del encargo. Los tests y el cotejo de hojas detectan diferencias; cualquier cambio metodológico requiere reconciliar la memoria y repetir revisión visual.

## Preparación académica pendiente del alumno

Completar nombres reales del grupo (4–6), estudiar y ensayar DEFENSA.md, verificar Zoom/SMOWL y entregar personalmente dentro de la ventana de PDF-001. No se ha subido al campus ni enviado ningún correo. El paquete está preparado para revisión técnica; la defensa individual requiere comprensión del alumno.

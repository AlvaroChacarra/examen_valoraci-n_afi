# Validación vigente

Esta página identifica controles actuales, defectos corregidos y límites. La resolución está sólo en MEMORIA; la teoría docente original sigue intacta. Las revisiones antiguas se conservan en [histórico](auditoria/historico/README.md); no usar un dictamen de otra versión como gate del HEAD.

## C-01: cuadratura con baja volatilidad — corregido

La revisión crítica de fb72703 detectó pérdida silenciosa de masa normal al integrar sólo a ambos lados del strike remoto. Con f=.03, K=.032, v=1e-10, δ=.5, P_U=.95 y nominal1e6, el integrador devolvía FRA/floorlet0 en lugar de −964,24997625 y +964,24997625. Con v=0 y f=K devolvía NaN. El [informe anterior](auditoria/historico/REVISION_CRITICA_fb72703.md) y su [contraejemplo](auditoria/historico/hallazgo_integrador_e2_fb72703.json) conservan el hallazgo.

`src/ejercicio2.py` ahora trata explícitamente v=0 y parte la cuadratura también por −8,0,+8 desviaciones, además del strike. Los paneles exteriores siguen siendo infinitos: no se trunca ni renormaliza la distribución. Las regresiones cubren ATM/ITM/OTM con varianzas0,1e-20,1e-16,1e-12,1e-10,1e-8; exigen finitud, ausencia de advertencias y error<1e-7u.m. frente a las fórmulas; se conserva también la cifra de control independiente del contraejemplo. Varianza negativa se rechaza explícitamente.

## Pruebas de valoración

Suite actual: **14 tests**, con casos múltiples dentro de cada prueba. Resultado de ejecución en `resultados/reproduccion.log` y `resultados/pruebas.log`.

|Bloque|Qué verifica|
|---|---|
|E1 contrato|36intervalos,14fechas; martingala exacta y varianza residual|
|E1 precios|Orden europea≤bermuda≤americana; europea por producto binomial; PV de pagos absorbidos|
|E1 réplica|Delta/cash, riqueza acumulada, autofinanciación y primera parada; tolerancia1e-10u.m.|
|E1 probabilidades|200000sendas,semilla20261024; exacta frente a MC y masa total1 con expiración|
|E1 referencia|Convolución gaussiana de mismas14fechas; convergencia espacial, dominio y europea analítica|
|E1 mejora|Error de JR+BS menor en el origen; no se promete en toda revaloración|
|E2|Cuadratura independiente,paridad,nominal,strike par,límites y nuevas regresiones C-01|
|E3|Cuadratura,1e6pares MC,medias de M/N,paridades,correlaciones,casos degenerados y signo quanto|
|Motor XLSX|Fixture con cachés erróneas que deben recalcular realmente a4 y Φ(0)=.5|

Los tests no son el único oráculo. Los scripts reutilizables de `auditoria/` contrastan E1 por recursión escalar/PDE y E2/E3 por integración alternativa. Sus outputs antiguos se archivan con su revisión exacta; se pueden volver a ejecutar según AUDITORIA.md.

## Hojas y PDF

`reproduce --deliverables` genera y recalcula los tres libros mediante LibreOffice con perfil aislado `OOXMLRecalcMode=0`. Convertir sin forzar recálculo no es prueba suficiente. Se cotejan 46.868 estados entre los dos escenarios E1, spots/precios/política, masas vivas/absorbidas, delta/cash y continuación BS,14probabilidades y33auxiliares E2/E3. Se detectan errores de fórmula en todos los libros. Las fórmulas usan NORMDIST compatible; no hay macros ni vínculos externos. Evidencia: `resultados/hojas_verificadas.json`.

El PDF se compila desde la memoria y se renderiza con PyMuPDF para inspección visual. El control mecánico de márgenes ayuda a detectar recortes, pero no sustituye la lectura de las páginas. Evidencia: `resultados/revision_pdf.json`.

## Integridad documental y límites

Los dos validadores del repositorio comprueban hashes de59fuentes, fórmulas/nombres docentes, enlaces y alcanzabilidad. Sus logs actuales están en resultados. No ejecutan VBA ni recalculan raw. No se usa --archives-dir: los ZIP de entrada no forman parte del checkout.

Límites que debe explicar un agente:

- Americana sólo de malla; réplica exacta del árbol puro, no de una difusión ni del híbrido BS.
- t*=15/365 con meses j/12; reconstrucción de JR fuera de malla, no condicionamiento único entre fechas.
- Mejora BS demostrada en el origen; en escenario15d su error es mayor, como precisa la memoria.
- E2 normal formal incompatible globalmente con bonos positivos; no se modifica su distribución.
- E2/E3 numéricos ilustrativos. La cuadratura E3 en±12normales se valida en las escalas estudiadas, no como API universal.
- Recálculo probado en LibreOffice, no Microsoft Excel; semillas fijadas, sin garantía de identidad binaria de PDF/XLSX por metadatos.
- Nombres y defensa personal pendientes; cesta extra excluida.

## Cierre de esta actualización

Reproducción completa ejecutada con 14 tests aprobados y hojas recalculadas sin errores de fórmula: máximo error de nodo6,14e-12u.m.; 46.868estados y33auxiliares contrastados. PDF final de18páginas leído visualmente; márgenes sin recortes detectados. Las precisiones editoriales finales se recompilaron después de la reproducción numérica. Otro agente ha contrastado C-01 contra la versión anterior y ha revisado las rutas de estudio sin modificar la solución.

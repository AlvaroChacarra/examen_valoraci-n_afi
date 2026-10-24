# Entrada para agentes

## Primera lectura

Leer [knowledge-base/README.md](knowledge-base/README.md), [mapa de relaciones](knowledge-base/MAPA_RELACIONES.md) y [limitaciones](knowledge-base/LIMITACIONES.md). Si la consulta es sobre el trabajo, leer además [ENCARGO](knowledge-base/ejercicios/ENCARGO.md).

Antes de comenzar una solución, leer [la segunda revisión](knowledge-base/REVISION_PREPARACION.md): contiene la matriz de obligaciones y controles por ejercicio.

## Recuperación progresiva

1. Elegir el concepto en [conceptos/README](knowledge-base/conceptos/README.md).
2. Localizar la fuente en [CATALOGO](knowledge-base/CATALOGO.md).
3. Abrir su ficha en `knowledge-base/fuentes/`. Contiene objetivo, método, resultados y relación plantilla/solución.
4. Consultar `knowledge-base/extracciones/` para celdas, fórmulas, etiquetas, páginas y VBA. Las fórmulas repetidas se agrupan en familias con ejemplos literales y valores guardados.
5. Consultar el binario `raw/` sólo si la extracción y las imágenes recuperadas no resuelven una ambigüedad concreta. No reabrir todos los Excel al iniciar cada consulta.

Buscar con `rg -n -i 'termino' knowledge-base`. Usar IDs de fuente y página PDF, diapositiva o `Hoja!Celda` al justificar una respuesta.

## Invariantes

- `raw/` es evidencia inmutable. Verificar sus hashes con el catálogo; no recalcular, reparar ni sobrescribir los originales.
- Diferenciar contenido original, interpretación editorial y derivación nueva. La extracción literal puede contener errores de OCR, fórmulas o ejemplos parciales.
- Los valores Excel son cachés guardadas, no verificaciones actuales. Hay macros y vínculos externos documentados.
- Los nombres locales prevalecen en su hoja sobre los de libro; consultar el ámbito en la extracción, incluidas las hojas ocultas.
- Las plantillas sin fórmulas o con blancos no son fuentes de resultados cero.
- La probabilidad de valoración depende del numerario; no llamarla probabilidad histórica.
- Mantener moneda, unidades FX, fixing/pago, dividendos y volatilidad absoluta/relativa explícitos.
- Para el encargo prevalecen PDF-002 y PPT-001. PDF-001 detalla la entrega individual. No presentar ejercicios de clase como solución del encargo.
- No sustituir paso mensual por malla de varianza sin señalar el cambio; no copiar ajustes lognormales para un ejercicio normal.
- No ejecutar VBA para explicar una fórmula. Su fuente ya está recuperada.

## Cambios y definición de terminado

Leer [OPERACION](knowledge-base/OPERACION.md). Actualizar la ficha que posee la información, las relaciones si cambian y el catálogo si se añade una fuente. Ejecutar `python scripts/validate_knowledge_base.py` y `python scripts/review_readiness.py`; revisar el diff. Mantener una sola ficha canónica por fuente y no añadir transcripciones de conversaciones como evidencia docente.

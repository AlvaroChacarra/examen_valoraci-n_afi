# Normalización y mantenimiento

## Proceso aplicado

1. Inspeccionar ambos ZIP y sus ZIP anidados. Descomprimir sólo archivos finales, evitando rutas inseguras.
2. Guardar cada binario bajo `raw/`, normalizando la ruta pero conservando bytes; registrar procedencia completa y SHA-256 en `catalogo.json`.
3. Extraer los PDF por página respetando su orden de lectura interno. Leer por separado texto y objetos de ecuaciones OfficeMath del PPT.
4. Leer los Excel estáticamente: hojas incluidas ocultas, etiquetas, constantes, fórmulas, cachés, nombres definidos, comentarios, gráficos y dependencias.
5. Agrupar fórmulas equivalentes por traslación para evitar miles de filas repetidas. Conservar ejemplos literales y límites de posición.
6. Recuperar VBA desde el contenedor OLE sin ejecutarlo. Extraer bitmaps de los EMF y las demás imágenes; deduplicar por hash, aplicar OCR y conservar imágenes para contraste.
7. Añadir OCR a las páginas imagen de Sesion_II. Reescribir en conceptos las fórmulas centrales que la extracción desordena.
8. Crear una ficha editorial por fuente y enlazar plantilla, solución, teoría y ejercicios del encargo.
9. Validar cobertura, hashes y enlaces antes de publicar.

## Reproducción

Dependencias Python: PyMuPDF, openpyxl, xlrd, lxml y Pillow. Para OCR se requiere Tesseract con idioma inglés disponible. openpyxl se utiliza para lectura estática; no se guardan ni recalculan libros.

Desde la raíz, con los cinco archivos originales adjuntos en un directorio de entrada:

```bash
python scripts/normalize_sources.py --input-dir /ruta/a/adjuntos
python scripts/supplement_extraction.py
python scripts/build_knowledge_base.py
python scripts/validate_knowledge_base.py
```

Si `raw/` y `catalogo.json` ya están presentes, sustituir el primer comando por:

```bash
python scripts/normalize_sources.py --extract-only
```

`metadata/` es una salida intermedia local, excluida de Git: se regenera desde los originales. Los conceptos y la guía del encargo son Markdown editorial versionado. Revisarlos si se sustituye una fuente: el extractor no prueba automáticamente la corrección económica de una explicación.

## Añadir o corregir conocimiento

No regenerar todas las fichas ante una duda puntual. Cambiar la ficha que posee el hecho y enlazarla desde el índice. Para un error del profesor, conservar la fórmula original en la extracción y documentar la observación en LIMITACIONES con celda/página. Cualquier derivación propia nueva debe marcarse como tal y guardarse separada de la extracción literal.

## Comprobación desde cero

El repositorio debe permitir descubrir el propósito, alcance, fuentes, marco metodológico, estado del encargo, limitaciones, procedimiento de regeneración y validación sin disponer del chat previo. AGENTS actúa como ruta de entrada, no como enciclopedia.

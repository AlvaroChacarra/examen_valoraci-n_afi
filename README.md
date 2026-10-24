# Proyecto Valoración AFI · MEFC 2026

Base de conocimiento de los materiales de José María Contreras y Javier Calderón, preparada para consultar la teoría y los ejercicios sin interpretar de nuevo los Excel.

## Empezar

1. [Entrada para agentes](AGENTS.md).
2. [Índice de conocimiento](knowledge-base/README.md).
3. [Mapa de relaciones](knowledge-base/MAPA_RELACIONES.md).
4. [Encargo y rutas para los tres ejercicios](knowledge-base/ejercicios/ENCARGO.md).
5. [Catálogo de las 59 fuentes](knowledge-base/CATALOGO.md).

## Organización

| Ruta | Contenido |
|---|---|
| `raw/fundamentos/` | Todos los archivos finales de los ZIP de Contreras, descomprimidos recursivamente |
| `raw/marco-black/` | Teoría, plantillas y soluciones de Calderón |
| `raw/encargo/` | Enunciado, instrucciones de defensa y PowerPoint de desarrollo |
| `knowledge-base/fuentes/` | Una ficha interpretativa por fuente: objetivo, método, entradas, fórmulas, resultados y relaciones |
| `knowledge-base/extracciones/` | PDF por páginas, PPT por diapositivas y Excel por hojas/familias de fórmulas; incluye VBA recuperado |
| `knowledge-base/conceptos/` | Notación y fórmulas revisadas, con referencias a clase |
| `knowledge-base/assets/` | Imágenes matemáticas y enunciados recuperados de los Excel, deduplicados |
| `catalogo.json` | Procedencia dentro de los ZIP, nombres originales, rutas normalizadas y SHA-256 |
| `scripts/` | Normalización y validación reproducibles |

Se han normalizado los nombres de ruta; los bytes de los 59 documentos originales se conservan. Las cadenas de ZIP se registran sin duplicar archivos comprimidos y descomprimidos en Git.

## Alcance

La base contiene **10 PDF (620 páginas), 48 libros Excel y un PPT de 25 diapositivas**. La extracción es estática: no se han recalculado libros, ejecutado macros ni resuelto el trabajo evaluable. Las soluciones incluidas son las suministradas en clase. Las observaciones sobre errores y convenciones están en [limitaciones](knowledge-base/LIMITACIONES.md).

## Mantenimiento

Leer [proceso y comprobaciones](knowledge-base/OPERACION.md). Mantener juntas la evidencia y su ficha; no editar `raw/` para corregir un ejemplo del profesor.

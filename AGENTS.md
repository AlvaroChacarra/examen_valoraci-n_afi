# Entrada para agentes

## Si vienes a explicar el trabajo al alumno

1. Leer [guía de aprendizaje y localización](soluciones/GUIA_PARA_EL_AGENTE.md).
2. Leer [estado actual](soluciones/ESTADO.md) y la sección pertinente de [la memoria canónica](soluciones/MEMORIA.md).
3. Consultar la teoría docente progresivamente por las rutas de la guía. No empezar releyendo todas las extracciones ni auditorías históricas.

## Si vienes a modificar o auditar

Leer [ejecución y entregables](soluciones/README.md), [validación](soluciones/VALIDACION.md), [matriz de requisitos](soluciones/MATRIZ_CUMPLIMIENTO.md) y [decisiones](soluciones/DECISIONES.md). Para el contrato prevalecen PDF-002 y las 25 diapositivas de PPT-001; PDF-001 define entrega/defensa. Originales en raw/encargo; fichas y extracciones en knowledge-base. La [guía del encargo](knowledge-base/ejercicios/ENCARGO.md) enlaza las fuentes.

## Invariantes

- `raw/` es evidencia inmutable; no recalcular ni guardar originales. Verificar hashes con el catálogo.
- Separar contenido docente, interpretación y derivación nueva. Los cachés de Excel docente no son resultados verificados.
- Mantener calendario contractual, moneda, unidades, numerario y volatilidad absoluta/relativa explícitos.
- E1: no sustituir meses por una malla de varianza; réplica exacta sólo en el árbol puro. La reconstrucción de 15 días es una convención y el suavizado sólo demuestra mejora en el origen.
- E2: pago en T, bono U como numerario, normal formal sin truncar. La normal no define globalmente bonos positivos.
- E3: FX EUR/USD, transformar correlaciones M,N frente a observables; quanto con conversión fija.
- Cesta extra diferida. Nombres de alumnos y entrega/defensa son personales. No campus ni correos. La integración de la resolución en main está autorizada por el usuario.

## Cambios y definición de terminado

La memoria es la única resolución canónica; no mantener soluciones paralelas en fichas docentes. Registrar decisiones duraderas en DECISIONES y estado mutable en ESTADO. Repetir pruebas afectadas, recálculo de hojas y revisión visual si cambia la memoria. Ejecutar los dos validadores del repositorio y revisar el diff. Comandos en soluciones/README.

Para cambios en las fuentes normalizadas, leer [índice docente](knowledge-base/README.md), [mapa](knowledge-base/MAPA_RELACIONES.md), [limitaciones](knowledge-base/LIMITACIONES.md), [preparación documental](knowledge-base/REVISION_PREPARACION.md) y [operación](knowledge-base/OPERACION.md). No regenerar todas las fichas ante una duda puntual. Buscar con `rg` y citar fuente/página/diapositiva/celda.

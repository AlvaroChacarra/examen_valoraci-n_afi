# Revisar la versión actual

Empezar por [ESTADO](ESTADO.md), [matriz](MATRIZ_CUMPLIMIENTO.md), [memoria](MEMORIA.md), [decisiones](DECISIONES.md) y [validación](VALIDACION.md). Para estudiar con el alumno usar [la guía pedagógica](GUIA_PARA_EL_AGENTE.md), no los informes históricos.

Anotar `git rev-parse HEAD` antes de auditar: no dar por revisado un HEAD móvil. Fuentes vinculantes: PDF-002, PPT-001 completo y PDF-001, en raw/encargo. Baseline de la primera resolución:25b879067144d380edd08b0ecf19dd861410d628. La actualización actual cierra C-01 de la revisión crítica de fb72703 y precisa la memoria; los dictámenes históricos siguen limitados a sus SHA.

Comandos desde la raíz (reproducción completa en una copia aislada para preservar binarios):

```bash
python -m unittest discover -s soluciones/tests -v
python -m soluciones.src.reproduce --deliverables
python scripts/validate_knowledge_base.py
python scripts/review_readiness.py
python soluciones/auditoria/contraste_independiente_e1.py --output /tmp/e1_independiente.json
python soluciones/auditoria/contraste_independiente_e2_e3.py --commit HEAD --output /tmp/e2_e3_independientes.json
python soluciones/auditoria/perturba_inputs_xlsx.py --commit HEAD --output /tmp/inputs_audit.json
```

Los scripts de contraste son auxiliares reutilizables. El de E1 conserva una etiqueta histórica interna: registrar el SHA desde el que se ejecuta. El de E2/E3 y el de inputs cargan la revisión indicada por Git, no cambios sin commit.

Priorizar: calendario/volatilidades por periodo, primera parada y réplica autofinanciada; diferencia entre árbol y difusión; factor de pagoT bajo medidaU; integrador cerca de v=0; transformación de correlaciones y unidades FX. Comprobar también que otro chat localice cada respuesta con la guía y reconstruya el motivo de las decisiones.

[Histórico de auditorías](auditoria/historico/README.md): conserva fallos y cierres anteriores, separado de la navegación de estudio. No es una segunda resolución ni una aprobación automática de cambios posteriores.

## Última revisión

[Revisión de C-01 y navegación de estudio](auditoria/REVISION_ACTUAL.md): PASS en ese alcance, con hashes de los archivos inspeccionados. Los controles de entregables ejecutados por el responsable se registran en VALIDACION y resultados. El código/tests revisados se fijaron en `23aa1b3`; el commit posterior de cierre añade evidencia y el ajuste editorial final, sin cambios de cálculo.

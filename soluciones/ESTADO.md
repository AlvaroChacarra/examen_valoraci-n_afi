# Estado operativo de la entrega

**Completada y validada.** Versión técnica exacta `92be7d90c6d1961e90e6a308eb9980accbd17156`; [revisión integrada PASS](auditoria/REVISION_INTEGRADA.md), sin hallazgos materiales abiertos. Los commits posteriores sólo incorporan evidencia y metadatos de cierre. No quedan procesos de desarrollo o recálculo en ejecución.

Rama: `solucion/mefc-2026`. Baseline: `25b879067144d380edd08b0ecf19dd861410d628`. Checkout inicial limpio; ningún cambio del usuario desplazado. Inicio 2026-10-24 17:24 UTC. El usuario autorizó reanudación con «Continua»; primera acción posterior observada el 24/10 a las 22:25 UTC, con límite del tramo de cierre a las 01:25 UTC del 25/10. Sin cambios de selector de modelo; revisión por otro agente con contexto inicial limpio.

Los tres ejercicios y la call usual de +0,5 están resueltos en [MEMORIA.md](MEMORIA.md). Código, JSON, figuras, tres hojas recalculadas y PDF en este directorio. [README](README.md) contiene los comandos de reproducción y edición; [VALIDACION](VALIDACION.md) separa evidencia, límites y pruebas documentales. [AUDITORIA](AUDITORIA.md) fija el commit exacto y las preguntas para otra conversación.

Decisiones vigentes: JR exacto, estados por bloques y calendario mensual; t*=15/365 sin mover fechas; prueba de réplica sólo sobre árbol puro; BS final con referencia de difusión de mismas14 fechas; normal formal de pagoT bajo medidaU; FX EUR/USD y ajuste quanto fijado por martingalas. Las derivaciones nuevas no modifican raw ni la evidencia docente.

Validación específica: 12 tests pasan; cotejo XLSX de 46.868 estados y 14 probabilidades; validadores de base documental pasan sin enlaces rotos ni huérfanos. Revisión independiente matemática de `5c0e1df` sin hallazgos materiales; la integración `7bc599d` detectó cachés sin recalcular y una función normal incompatible, corregidas con recálculo forzado y verificador ampliado; scripts en auditoria/. La revisión integrada acredita la corrección, reproducción completa y cambios de entradas; el commit definitivo se fija en AUDITORIA.md.

Pendientes reales: completar nombres del grupo y realizar personalmente entrega/defensa; auditoría en otra conversación preparada, no realizada aquí. Extra de cesta+1 opcional pendiente. Sin campus, correos, merge ni publicación en main. El SHA remoto y la limpieza de Git se verifican al cerrar.

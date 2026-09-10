# WEB4™ · Gaming virtualizado / Virtualized Gaming

**Estado:** PUBLIC-SOURCE · READY-FOR-WEB4-ADAPTER · NO-LIVE-DEPLOY  
**Fecha:** 2026-09-10

Esta carpeta define la **fuente pública** para una futura sección WEB4™ sobre compatibilidad de juegos en configuraciones Linux virtualizadas con GPU RTX dedicada mediante passthrough y Steam/Proton.

No se plantea como un ranking de potencia ni como «juegos para Rocinante». **Rocinante™ es la plataforma de referencia y validación**, mientras que el objeto público es reproducible por otras configuraciones Rocinante-like.

## Fuente documental

- [Matriz pública completa ES/EN](../../analisis/publicos/2026-09-10_matriz_compatibilidad_gaming_vm_linux_dlss4_dlss5_ES_EN.md)
- [Datos estructurados JSON](./compatibility.json)

## Contrato visual propuesto

WEB4™ debería presentar cuatro estados visibles:

- `R0 · VERIFIED_ROCINANTE`: prueba material registrada en la plataforma de referencia.
- `R1 · STRONG_CANDIDATE`: sin bloqueo VM conocido y con ruta DLSS/Proton técnicamente plausible.
- `R2 · CONDITIONAL`: requiere prueba local por versión, anticheat, online o ruta DLSS concreta.
- `BLOCKED`: bloqueo conocido por VM o Proton/Linux.

La sección debe permitir filtrar por `DLSS 5`, `DLSS 4/4.5`, `MFG`, `Ray Reconstruction`, `Ray Tracing`, `Path Tracing`, estado Proton y política de VM.

## Principio de publicación

```text
FUENTE PÚBLICA VERSIONADA
→ adaptador WEB4
→ tabla/fichas/filtros
→ evidencia por juego
→ revisión periódica
```

El dato publicable no debe afirmar validación local sin evidencia. `R0` sólo se concede después de una ejecución real con registro de versión de juego, Proton, driver, kernel, GPU, resolución y funciones DLSS observadas.

La implementación viva de WEB4™ se realiza en el workspace privado conforme a las reglas de fuente y proyección; esta carpeta pública actúa como **fuente de datos, contrato de superficie y genealogía pública**, no como baseline de implementación.

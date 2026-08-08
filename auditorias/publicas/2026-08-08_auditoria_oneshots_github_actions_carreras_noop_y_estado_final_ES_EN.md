# Auditoría de One-Shots GitHub Actions · carreras, no-op y estado final
# GitHub Actions One-Shot Audit · races, no-op failures and final state

**Fecha / Date:** 2026-08-08  
**Repositorio / Repository:** `PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC`  
**Estado / Status:** fallos históricos explicados · sincronización posterior completada · one-shots obsoletos retirados / historical failures explained · later synchronization completed · obsolete one-shots removed

---

# ES · Castellano

## 1. Motivo de revisión

El correo recibió múltiples notificaciones de GitHub Actions con estados `failed` o `No jobs were run` para workflows one-shot relacionados con:

- `one-shot-readmes-v3`;
- `one-shot-readmes-v4`;
- `one-shot-homogenize-all-readmes-manifestos`;
- `one-shot-repair-spanish-index-xlix`;
- y one-shots anteriores de postcheck/sincronización.

La acumulación visual de avisos podía sugerir que el estado actual del repositorio seguía roto. La lectura de commits demuestra que no es esa la interpretación correcta.

## 2. Causa principal detectada

El commit `f617f2f6f6f8bbdb7f8c499bd60e9cfd12cb652e` registró `one-shot-readmes-v4` con:

```yaml
on: [push]
```

El mismo workflow:

1. ejecutaba un script de homogeneización;
2. hacía `git add -A`;
3. ejecutaba un `git commit` sin comprobar primero si existían cambios;
4. hacía `git push`;
5. y después eliminaba varios workflows one-shot y volvía a hacer push.

Ese diseño genera dos riesgos combinados.

### A. Fallo por no-op

Si otro workflow paralelo ya aplicó los mismos cambios, `git commit` encuentra el árbol limpio y devuelve código de salida distinto de cero.

```text
MISMA TAREA EN PARALELO
→ PRIMER RUN HACE EL CAMBIO
→ SEGUNDO RUN YA NO TIENE DELTA
→ git commit SIN GUARDIA
→ FAILURE AUNQUE EL ESTADO DOCUMENTAL SEA CORRECTO
```

### B. Carrera por múltiples pushes

Un workflow activado con `on: [push]` hace nuevos pushes al:

- publicar la corrección;
- eliminar one-shots;
- o actualizar ficheros relacionados.

Esos pushes pueden activar otros workflows que todavía existían en el commit de origen o generar ejecuciones que se resuelven cuando el workflow ya ha sido eliminado. Esto explica parte de los avisos `No jobs were run` y de la repetición de notificaciones.

## 3. Evidencia de corrección posterior

Los fallos de notificación no representan el último estado documental.

Posteriormente existen commits de resultado correcto:

- `ba0fcece6a5ca478e3d2240bb5805624075779db` · `docs: homogenize all READMEs with complete I-L manifesto network`;
- `0e8426fff85d90474c7c7f4a1340822b645e9436` · retirada de one-shots de homogeneización completados;
- `493452f913e6ba2cef0fd4a25121041b637e81a4` · integración de LI en navegación canónica y READMEs;
- `2e40e055df26bd965764f5fe97f52d484a42674b` · sincronización de READMEs y enlaces hasta LI;
- `b1f78a8821a919af83ec26b2fca92b590eccb1fe` · retirada de los one-shots de sincronización LI.

La búsqueda actual de código por `name: one-shot` no devuelve workflows activos y la ruta `.github/workflows/one-shot-readmes-v4.yml` devuelve `404`, coherente con su eliminación posterior.

## 4. Dictamen

```text
NOTIFICACIONES DE FAILURE
→ reales como ejecuciones históricas

ESTADO DOCUMENTAL FINAL DE ESAS OPERACIONES
→ corregido posteriormente

ONE-SHOTS OBSOLETOS
→ retirados

FALLO ACTUAL PERSISTENTE DEMOSTRADO
→ no detectado en esta revisión

CAUSA SISTÉMICA PRINCIPAL
→ workflows one-shot concurrentes + trigger demasiado amplio + commit no-op no protegido
```

Por tanto, no debe repararse otra vez el contenido simplemente porque Gmail conserve avisos rojos de ejecuciones anteriores.

## 5. Norma para futuros one-shots

Los próximos one-shots deberán cumplir como mínimo:

1. **trigger limitado al propio archivo**, no `on: [push]` global;
2. **idempotencia**: ejecutar dos veces debe producir el mismo estado;
3. **commit protegido**:

```bash
git add -A
if ! git diff --cached --quiet; then
  git commit -m "..."
  git pull --rebase origin main
  git push origin main
fi
```

4. **concurrency group** para impedir dos escritores simultáneos sobre la misma operación;
5. una única implementación activa por tarea, evitando `v2`, `v3`, `v4` concurrentes;
6. cleanup sólo después de postcheck correcto;
7. validación del estado final, no interpretación del color de una ejecución aislada;
8. cuando el conector GitHub permita efectuar la modificación directamente con trazabilidad suficiente, preferir la escritura directa y reservar Actions para transformaciones realmente masivas o reproducibles.

## 6. Patrón recomendado

```text
CREAR ONE-SHOT ÚNICO
→ TRIGGER SOBRE SU PROPIO PATH
→ CHECKOUT
→ TRANSFORMACIÓN IDEMPOTENTE
→ VALIDACIÓN
→ COMMIT SÓLO SI HAY DELTA
→ REBASE
→ PUSH
→ POSTCHECK
→ RETIRADA DEL ONE-SHOT
→ NO NUEVAS EJECUCIONES EN CASCADA
```

## 7. Relación con la Auditoría Conjunta Perpetua™

Este incidente es un ejemplo útil de la diferencia entre:

```text
SEÑAL DE ERROR
≠
ESTADO FINAL ERRÓNEO
```

El sistema debe conservar el error histórico porque informa sobre fragilidad del proceso, pero debe distinguirlo del estado final validado para no entrar en ciclos de reparación infinita.

---

# EN · English

## 1. Reason for review

Gmail received multiple GitHub Actions notifications marked `failed` or `No jobs were run` for one-shot workflows including `one-shot-readmes-v3`, `one-shot-readmes-v4`, `one-shot-homogenize-all-readmes-manifestos`, `one-shot-repair-spanish-index-xlix` and earlier postcheck/synchronisation one-shots.

The volume of red notifications could falsely suggest that the repository remained broken.

## 2. Main cause found

Commit `f617f2f6f6f8bbdb7f8c499bd60e9cfd12cb652e` registered `one-shot-readmes-v4` with a broad `on: [push]` trigger. The workflow ran a homogenisation script, executed an unguarded `git commit`, pushed, then removed several one-shot workflows and pushed again.

This creates two coupled failure modes:

- **no-op commit failure:** another concurrent run may already have produced the same state, causing `git commit` to exit non-zero on a clean tree;
- **push-trigger race:** correction and cleanup pushes can trigger sibling workflows or leave queued events referring to workflows that have already been removed.

## 3. Evidence of later correction

The notification failures are not the final documentary state. Later successful commits include:

- `ba0fcece6a5ca478e3d2240bb5805624075779db` · complete I–L README homogenisation;
- `0e8426fff85d90474c7c7f4a1340822b645e9436` · removal of completed homogenisation one-shots;
- `493452f913e6ba2cef0fd4a25121041b637e81a4` · LI integration;
- `2e40e055df26bd965764f5fe97f52d484a42674b` · README/link synchronisation through LI;
- `b1f78a8821a919af83ec26b2fca92b590eccb1fe` · removal of LI synchronisation one-shots.

A current code search for `name: one-shot` returns no active workflow and `.github/workflows/one-shot-readmes-v4.yml` now returns `404`, consistent with cleanup.

## 4. Finding

```text
FAILED NOTIFICATIONS
→ genuine historical run failures

FINAL DOCUMENTARY STATE OF THOSE OPERATIONS
→ corrected later

OBSOLETE ONE-SHOTS
→ removed

DEMONSTRATED CURRENT PERSISTENT FAILURE
→ none detected in this review

PRIMARY SYSTEMIC CAUSE
→ concurrent one-shots + overbroad push trigger + unguarded no-op commit
```

## 5. Rule for future one-shots

Future one-shots should use a path-limited trigger, idempotent transformation, guarded commits, a concurrency group, only one active implementation per task, cleanup after successful postcheck and validation of final repository state rather than the colour of an isolated historical run.

Where the GitHub connector can perform the required write directly with sufficient traceability, direct writes should be preferred over temporary Actions workflows.

## 6. Recommended pattern

```text
CREATE ONE UNIQUE ONE-SHOT
→ TRIGGER ONLY ON ITS OWN PATH
→ CHECKOUT
→ IDEMPOTENT TRANSFORMATION
→ VALIDATION
→ COMMIT ONLY IF DELTA EXISTS
→ REBASE
→ PUSH
→ POSTCHECK
→ REMOVE ONE-SHOT
→ NO CASCADING RUNS
```

## 7. Relation to Perpetual Joint Audit™

This incident demonstrates the distinction:

```text
ERROR SIGNAL
≠
ERRONEOUS FINAL STATE
```

Historical failures should remain documented because they reveal process fragility, while the validated final state must be kept distinct to avoid infinite repair loops.

---

**Pedro Martínez Alhambra · Innova_N**
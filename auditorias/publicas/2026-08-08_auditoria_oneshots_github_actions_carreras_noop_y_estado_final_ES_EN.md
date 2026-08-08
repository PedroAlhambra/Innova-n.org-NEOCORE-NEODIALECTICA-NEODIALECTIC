# Auditoría de One-Shots GitHub Actions · carreras, non-fast-forward, no-op y estado final
# GitHub Actions One-Shot Audit · races, non-fast-forward, no-op and final state

**Fecha / Date:** 2026-08-08  
**Repositorio / Repository:** `PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC`  
**Estado / Status:** causa de fallo confirmada en logs · sincronización posterior completada · one-shots obsoletos retirados / failure cause confirmed in logs · later synchronization completed · obsolete one-shots removed

---

# ES · Castellano

## 1. Motivo de revisión

El correo recibió múltiples notificaciones de GitHub Actions con estados `failed` o `No jobs were run` para workflows one-shot relacionados con:

- `one-shot-readmes-v3`;
- `one-shot-readmes-v4`;
- `one-shot-homogenize-all-readmes-manifestos`;
- `one-shot-repair-spanish-index-xlix`;
- y one-shots anteriores de postcheck/sincronización.

La acumulación visual de avisos podía sugerir que el estado actual del repositorio seguía roto. La revisión de commits y, después, de los **logs reales de ejecución** demuestra que no es esa la interpretación correcta.

## 2. Fallo confirmado en `one-shot-readmes-v4`

Se abrió la ejecución indicada por el correo de GitHub:

- **Workflow run:** `31258964815`
- **Job:** `93106666045` · `homogenize`
- **Commit de origen:** `f617f2f6f6f8bbdb7f8c499bd60e9cfd12cb652e`

El job muestra:

```text
checkout
→ SUCCESS

Homogenize and validate
→ SUCCESS
→ 13 READMEs modificados
→ POSTCHECK OK: 50/50 manifiestos enlazados

Commit changes
→ COMMIT LOCAL CREADO: 9ca9f44
→ PUSH RECHAZADO: non-fast-forward

Cleanup one-shots
→ SKIPPED por el fallo anterior
```

La línea material del log es:

```text
! [rejected] main -> main (non-fast-forward)
Updates were rejected because the tip of your current branch is behind its remote counterpart.
```

Por tanto, para esta ejecución concreta la causa del `failure` **no fue un error del script documental ni un postcheck fallido**. Fue una **carrera de escritura**: mientras este runner trabajaba sobre `f617f2f`, la rama `main` avanzó por otra operación y el `git push` sin `pull --rebase` previo fue rechazado.

## 3. Diseño que permitió la carrera

El commit `f617f2f6f6f8bbdb7f8c499bd60e9cfd12cb652e` registró `one-shot-readmes-v4` con:

```yaml
on: [push]
```

El workflow:

1. ejecutaba el script de homogeneización;
2. hacía `git add -A`;
3. creaba commit;
4. hacía `git push` **sin integrar primero cambios remotos concurrentes**;
5. y, sólo después, pretendía eliminar varios one-shots y volver a hacer push.

Con varios one-shots activos y pushes sucesivos, el patrón podía producir runners trabajando sobre bases distintas.

```text
RUN A Y RUN B PARTEN DE ESTADOS PRÓXIMOS
→ AMBOS GENERAN DELTA
→ A PUBLICA PRIMERO
→ main AVANZA
→ B INTENTA PUSH SOBRE BASE ANTIGUA
→ NON-FAST-FORWARD
→ FAILURE
```

## 4. Riesgo secundario de no-op

El workflow también contenía un `git commit` sin comprobar si existían cambios staged.

Eso no fue la causa del run `31258964815`, porque en ese run sí se creó el commit local `9ca9f44`.

Sin embargo, era un riesgo adicional: si otro runner hubiera aplicado antes exactamente el mismo delta, el script podía terminar correctamente pero `git commit` fallar por árbol limpio.

Por tanto se distinguen:

```text
CAUSA CONFIRMADA DEL RUN ANALIZADO
→ carrera + push non-fast-forward

RIESGO DE DISEÑO ADICIONAL
→ commit no-op no protegido
```

## 5. Por qué aparecen también `No jobs were run`

Los workflows temporales se creaban, ejecutaban, modificaban y eliminaban mediante nuevos pushes. Algunas notificaciones corresponden a eventos generados cuando el archivo del workflow ya había cambiado o desaparecido, o cuando sus condiciones ya no permitían ejecutar jobs.

Ese ruido de ejecución es coherente con una arquitectura de múltiples one-shots efímeros encadenados por pushes. No constituye por sí mismo evidencia de que el contenido final quedara sin sincronizar.

## 6. Evidencia de corrección posterior

Los avisos rojos no representan el último estado documental.

Posteriormente existen commits de resultado correcto:

- `ba0fcece6a5ca478e3d2240bb5805624075779db` · `docs: homogenize all READMEs with complete I-L manifesto network`;
- `0e8426fff85d90474c7c7f4a1340822b645e9436` · retirada de one-shots de homogeneización completados;
- `493452f913e6ba2cef0fd4a25121041b637e81a4` · integración de LI en navegación canónica y READMEs;
- `2e40e055df26bd965764f5fe97f52d484a42674b` · sincronización de READMEs y enlaces hasta LI;
- `b1f78a8821a919af83ec26b2fca92b590eccb1fe` · retirada de los one-shots de sincronización LI.

La búsqueda actual de código por `name: one-shot` no devuelve workflows activos y la ruta `.github/workflows/one-shot-readmes-v4.yml` devuelve `404`, coherente con su eliminación posterior.

## 7. Dictamen

```text
NOTIFICACIONES DE FAILURE
→ ejecuciones históricas realmente fallidas

SCRIPT DE HOMOGENEIZACIÓN DEL RUN 31258964815
→ correcto

POSTCHECK DEL MISMO RUN
→ correcto: 50/50

CAUSA DEL FAILURE
→ push non-fast-forward por carrera concurrente

ESTADO DOCUMENTAL FINAL DE ESAS OPERACIONES
→ corregido posteriormente

ONE-SHOTS OBSOLETOS
→ retirados

FALLO ACTUAL PERSISTENTE DEMOSTRADO
→ no detectado en esta revisión
```

No debe repararse otra vez el contenido simplemente porque Gmail conserve avisos rojos de ejecuciones anteriores.

## 8. Norma para futuros one-shots

Los próximos one-shots deberán cumplir como mínimo:

1. **trigger limitado al propio archivo**, no `on: [push]` global;
2. **idempotencia**: ejecutar dos veces debe producir el mismo estado;
3. **concurrency group** para impedir dos escritores simultáneos de la misma familia;
4. **actualización de rama antes de publicar**;
5. **commit protegido**;
6. una única implementación activa por tarea, evitando `v2`, `v3`, `v4` concurrentes;
7. cleanup sólo después de postcheck correcto y push confirmado;
8. validación del estado final, no interpretación del color de una ejecución aislada;
9. cuando el conector GitHub permita efectuar la modificación directamente con trazabilidad suficiente, preferir la escritura directa y reservar Actions para transformaciones realmente masivas o reproducibles.

Patrón mínimo recomendado:

```bash
git add -A
if ! git diff --cached --quiet; then
  git commit -m "..."
  git pull --rebase origin main
  git push origin main
fi
```

Y a nivel de workflow:

```yaml
concurrency:
  group: one-shot-<operacion>
  cancel-in-progress: false
```

## 9. Patrón recomendado

```text
CREAR ONE-SHOT ÚNICO
→ TRIGGER SOBRE SU PROPIO PATH
→ CHECKOUT
→ TRANSFORMACIÓN IDEMPOTENTE
→ VALIDACIÓN
→ COMMIT SÓLO SI HAY DELTA
→ PULL --REBASE
→ PUSH
→ POSTCHECK
→ RETIRADA DEL ONE-SHOT
→ NO NUEVAS EJECUCIONES EN CASCADA
```

## 10. Relación con la Auditoría Conjunta Perpetua™

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

The volume of red notifications could falsely suggest that the repository remained broken. Commit inspection followed by direct workflow-log inspection shows otherwise.

## 2. Confirmed failure in `one-shot-readmes-v4`

The GitHub notification led to:

- **Workflow run:** `31258964815`
- **Job:** `93106666045` · `homogenize`
- **Source commit:** `f617f2f6f6f8bbdb7f8c499bd60e9cfd12cb652e`

The actual job log shows that checkout succeeded, `Homogenize and validate` succeeded, all 13 target READMEs were changed, and the postcheck reported `50/50 manifestos linked`.

The workflow then created local commit `9ca9f44` but its push was rejected:

```text
! [rejected] main -> main (non-fast-forward)
Updates were rejected because the tip of your current branch is behind its remote counterpart.
```

The confirmed cause of this run failure is therefore a **concurrent-write race**, not a failed documentary transformation.

## 3. Design allowing the race

The workflow used a broad `on: [push]` trigger, committed changes and attempted to push without first rebasing against concurrent remote updates. It then intended to remove several one-shot workflows with another push.

With several temporary workflows active at once, two runners could produce valid local deltas from nearby but different repository states; the first push advances `main`, and the second is rejected as non-fast-forward.

## 4. Secondary no-op risk

The workflow also used an unguarded `git commit`. This was **not** the cause of run `31258964815`, because that run successfully created local commit `9ca9f44`.

It remained a separate design risk: another runner applying the identical delta first could leave a clean tree and make the later unguarded commit exit non-zero.

## 5. `No jobs were run` notifications

Temporary workflows were created, triggered, changed and deleted through additional pushes. Some queued events therefore referred to workflows whose files or conditions had already changed. This is consistent with the observed notification noise and does not by itself establish an incorrect final repository state.

## 6. Evidence of later correction

Later successful commits include:

- `ba0fcece6a5ca478e3d2240bb5805624075779db` · complete I–L README homogenisation;
- `0e8426fff85d90474c7c7f4a1340822b645e9436` · removal of completed homogenisation one-shots;
- `493452f913e6ba2cef0fd4a25121041b637e81a4` · LI integration;
- `2e40e055df26bd965764f5fe97f52d484a42674b` · README/link synchronisation through LI;
- `b1f78a8821a919af83ec26b2fca92b590eccb1fe` · removal of LI synchronisation one-shots.

A current code search for `name: one-shot` returns no active workflow and `.github/workflows/one-shot-readmes-v4.yml` now returns `404`, consistent with cleanup.

## 7. Finding

```text
FAILED NOTIFICATIONS
→ genuine historical failed runs

TRANSFORMATION SCRIPT IN RUN 31258964815
→ successful

POSTCHECK IN THAT RUN
→ successful: 50/50

FAILURE CAUSE
→ non-fast-forward push caused by concurrent write race

FINAL DOCUMENTARY STATE OF THOSE OPERATIONS
→ corrected later

OBSOLETE ONE-SHOTS
→ removed

DEMONSTRATED CURRENT PERSISTENT FAILURE
→ none detected in this review
```

## 8. Rule for future one-shots

Future one-shots should use a path-limited trigger, idempotent transformation, a concurrency group, rebasing before push, guarded commits, only one active implementation per task, cleanup after successful postcheck and confirmed push, and validation of final repository state rather than the colour of an isolated historical run.

Where the GitHub connector can perform the required write directly with sufficient traceability, direct writes should be preferred over temporary Actions workflows.

## 9. Recommended pattern

```text
CREATE ONE UNIQUE ONE-SHOT
→ TRIGGER ONLY ON ITS OWN PATH
→ CHECKOUT
→ IDEMPOTENT TRANSFORMATION
→ VALIDATION
→ COMMIT ONLY IF DELTA EXISTS
→ PULL --REBASE
→ PUSH
→ POSTCHECK
→ REMOVE ONE-SHOT
→ NO CASCADING RUNS
```

## 10. Relation to Perpetual Joint Audit™

This incident demonstrates the distinction:

```text
ERROR SIGNAL
≠
ERRONEOUS FINAL STATE
```

Historical failures should remain documented because they reveal process fragility, while the validated final state must be kept distinct to avoid infinite repair loops.

---

**Pedro Martínez Alhambra · Innova_N**
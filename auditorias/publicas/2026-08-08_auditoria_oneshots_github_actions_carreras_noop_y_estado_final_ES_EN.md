# Auditoría de One-Shots GitHub Actions · carreras, non-fast-forward, no-op y estado final
# GitHub Actions One-Shot Audit · races, non-fast-forward, no-op and final state

**Fecha / Date:** 2026-08-08  
**Repositorio / Repository:** `PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC`  
**Estado / Status:** causa de fallo confirmada en logs · sincronización posterior completada · one-shots obsoletos retirados / failure cause confirmed in logs · later synchronization completed · obsolete one-shots removed

---

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

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

Email received multiple GitHub Actions notifications with `failed` or `No jobs were run` states for one-shot workflows related to:

- `one-shot-readmes-v3`;
- `one-shot-readmes-v4`;
- `one-shot-homogenize-all-readmes-manifestos`;
- `one-shot-repair-spanish-index-xlix`;
- and earlier postcheck/synchronisation one-shots.

The visual accumulation of notices could suggest that the repository's current state remained broken. Reviewing commits and then the **actual execution logs** shows that this is not the correct interpretation.

## 2. Confirmed failure in `one-shot-readmes-v4`

The execution indicated by the GitHub email was opened:

- **Workflow run:** `31258964815`
- **Job:** `93106666045` · `homogenize`
- **Source commit:** `f617f2f6f6f8bbdb7f8c499bd60e9cfd12cb652e`

The job shows:

```text
checkout
→ SUCCESS

Homogenize and validate
→ SUCCESS
→ 13 READMEs modified
→ POSTCHECK OK: 50/50 manifestos linked

Commit changes
→ LOCAL COMMIT CREATED: 9ca9f44
→ PUSH REJECTED: non-fast-forward

Cleanup one-shots
→ SKIPPED because of the preceding failure
```

The material line in the log is:

```text
! [rejected] main -> main (non-fast-forward)
Updates were rejected because the tip of your current branch is behind its remote counterpart.
```

Therefore, for this specific run, the cause of the `failure` **was not an error in the documentary script or a failed postcheck**. It was a **write race**: while this runner was working from `f617f2f`, the `main` branch advanced through another operation and `git push` without a preceding `pull --rebase` was rejected.

## 3. Design that allowed the race

Commit `f617f2f6f6f8bbdb7f8c499bd60e9cfd12cb652e` registered `one-shot-readmes-v4` with:

```yaml
on: [push]
```

The workflow:

1. ran the homogenisation script;
2. ran `git add -A`;
3. created a commit;
4. ran `git push` **without first integrating concurrent remote changes**;
5. and only afterwards intended to remove several one-shots and push again.

With several one-shots active and successive pushes, the pattern could produce runners working from different bases.

```text
RUN A AND RUN B START FROM NEARBY STATES
→ BOTH GENERATE A DELTA
→ A PUBLISHES FIRST
→ main ADVANCES
→ B TRIES TO PUSH FROM AN OLD BASE
→ NON-FAST-FORWARD
→ FAILURE
```

## 4. Secondary no-op risk

The workflow also contained a `git commit` without checking whether staged changes existed.

That was not the cause of run `31258964815`, because that run did create local commit `9ca9f44`.

However, it was an additional risk: if another runner had already applied exactly the same delta, the script could finish correctly while `git commit` failed because the tree was clean.

The distinction is therefore:

```text
CONFIRMED CAUSE OF THE ANALYSED RUN
→ race + non-fast-forward push

ADDITIONAL DESIGN RISK
→ unguarded no-op commit
```

## 5. Why `No jobs were run` also appears

Temporary workflows were created, executed, modified and deleted through new pushes. Some notifications correspond to events generated after the workflow file had already changed or disappeared, or when its conditions no longer allowed jobs to run.

That execution noise is consistent with an architecture of multiple ephemeral one-shots chained through pushes. It does not by itself establish that the final content remained unsynchronised.

## 6. Evidence of later correction

The red notices do not represent the latest documentary state.

Later commits with successful results exist:

- `ba0fcece6a5ca478e3d2240bb5805624075779db` · `docs: homogenize all READMEs with complete I-L manifesto network`;
- `0e8426fff85d90474c7c7f4a1340822b645e9436` · removal of completed homogenisation one-shots;
- `493452f913e6ba2cef0fd4a25121041b637e81a4` · integration of LI into canonical navigation and README files;
- `2e40e055df26bd965764f5fe97f52d484a42674b` · synchronisation of README files and links through LI;
- `b1f78a8821a919af83ec26b2fca92b590eccb1fe` · removal of LI synchronisation one-shots.

The current code search for `name: one-shot` returns no active workflows and the path `.github/workflows/one-shot-readmes-v4.yml` returns `404`, consistent with its later removal.

## 7. Finding

```text
FAILURE NOTIFICATIONS
→ genuinely failed historical runs

HOMOGENISATION SCRIPT IN RUN 31258964815
→ successful

POSTCHECK IN THE SAME RUN
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

The content should not be repaired again merely because Gmail preserves red notices from earlier runs.

## 8. Rule for future one-shots

Future one-shots should satisfy at least:

1. **trigger limited to the workflow's own file**, not global `on: [push]`;
2. **idempotence**: running twice should produce the same state;
3. a **concurrency group** to prevent two simultaneous writers in the same family;
4. **branch update before publishing**;
5. a **guarded commit**;
6. one active implementation per task, avoiding concurrent `v2`, `v3`, `v4` versions;
7. cleanup only after a correct postcheck and confirmed push;
8. validation of final state rather than interpretation of the colour of one isolated run;
9. where the GitHub connector can directly perform the modification with sufficient traceability, prefer direct writing and reserve Actions for transformations that are genuinely massive or reproducible.

Recommended minimum pattern:

```bash
git add -A
if ! git diff --cached --quiet; then
  git commit -m "..."
  git pull --rebase origin main
  git push origin main
fi
```

And at workflow level:

```yaml
concurrency:
  group: one-shot-<operation>
  cancel-in-progress: false
```

## 9. Recommended pattern

```text
CREATE ONE UNIQUE ONE-SHOT
→ TRIGGER ONLY ON ITS OWN PATH
→ CHECKOUT
→ IDEMPOTENT TRANSFORMATION
→ VALIDATION
→ COMMIT ONLY IF A DELTA EXISTS
→ PULL --REBASE
→ PUSH
→ POSTCHECK
→ REMOVE THE ONE-SHOT
→ NO NEW CASCADING RUNS
```

## 10. Relation to Perpetual Joint Audit™

This incident is a useful example of the difference between:

```text
ERROR SIGNAL
≠
ERRONEOUS FINAL STATE
```

The system must preserve the historical error because it provides information about process fragility, while distinguishing it from the validated final state so as not to enter infinite repair cycles.

---

**Pedro Martínez Alhambra · Innova_N**

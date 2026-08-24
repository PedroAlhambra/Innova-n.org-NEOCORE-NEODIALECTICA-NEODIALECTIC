# MAXPROC público · Run 14 · integración del gate de navegación lingüística
# Public MAXPROC · Run 14 · language-navigation gate integration

**Fecha / Date:** 2026-08-24 14:54 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Objetivo / Target:** cerrar la brecha entre `CONTENT_SYMMETRY` y `LANGUAGE_NAVIGATION` sin inferir PASS por ausencia de status. / close the gap between `CONTENT_SYMMETRY` and `LANGUAGE_NAVIGATION` without inferring PASS from missing status.  
**Commits materiales / Material commits:** `05c58e5f409a905771202094312cc282497ee6ac` · `3ff4abcc54522fb9178e4491bf85970d3eebaee8`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies obligatorias del corpus público y la nota MAXPROC anterior. `README.md` mantiene `7.3-CANDIDATE` como frontera pública activa y no canónica; `manifiestos/README.md` conserva I–LXXXI + ∞; `neoaxiomas/README.md` conserva NAX-01–14 y C-NAX-15–26; `propuestas/sintesis-abierta/README.md` mantiene la separación `CANDIDATE ≠ CANON`; `web4/README.md` sigue declarando WEB4 como especificación documental pública y no implementación final.

La auditoría estructural ES/EN versionada heredada de Run 13 está en `PASS 0/0/0/0`, pero Run 13 dejó correctamente `LANGUAGE_SELECTOR_GATE = NOT_VERIFIED` porque el gate de selector existía como workflow separado y su resultado no quedaba materializado en una auditoría versionada recuperable.

## Problema elegido

El defecto era de arquitectura de control, no de contenido: el workflow global de simetría que sí genera y versiona auditorías no ejecutaba el gate de navegación lingüística. Además, el auditor de selectores aceptaba cualquier destino que comenzara por `#es` o `#en`; por tanto podía no detectar un selector cuyo enlace apuntase a un anchor inexistente o incorrecto.

Esto permitía dos falsos positivos potenciales:

```text
CONTENT_SYMMETRY = PASS
LANGUAGE_NAVIGATION = NO OBSERVABLE
→ ESTADO GLOBAL INCOMPLETO

SELECTOR VISIBLE
+ DESTINO #es-incorrecto / #en-incorrecto
→ ANTIGUO AUDITOR PODÍA ACEPTARLO
```

## Acción

Se reforzó `.github/scripts/audit_language_selectors.py` para:

- exigir selector visible antes del cuerpo ES;
- derivar el anchor esperado desde los encabezados reales ES/EN;
- comparar el destino del selector con el anchor esperado;
- clasificar discrepancias como `LANGUAGE_ANCHOR_FAILURE`;
- generar una auditoría pública versionable en `auditorias/publicas/2026-08-24_auditoria_global_selectores_idioma_ES_EN.md`;
- mantener `LANGUAGE_SELECTOR_GATE = FAIL` con salida no cero cuando exista cualquier defecto.

Después se integró ese auditor en `.github/workflows/audit-global-bilingual-symmetry.yml`. El workflow global ahora ejecuta, en secuencia bloqueante:

```text
CONTENT_SYMMETRY
→ LANGUAGE_NAVIGATION
→ COMMIT DE AUDITORÍAS VERSIONADAS
```

y añade la auditoría de selectores al mismo commit automático que conserva la simetría global y el gate neoaxiomático.

## Pruebas y resultado

La lectura posterior del script y del workflow confirma que la integración y la validación estricta de anchors están fijadas en `main`.

El commit combinado observado antes de este delta no expone statuses tradicionales, por lo que ausencia de status sigue sin interpretarse como PASS. En el momento de esta nota aún no existe una copia recuperable de la nueva auditoría versionada de selectores; por ello el estado global del selector se mantiene prudentemente como `NOT_VERIFIED` hasta que el workflow produzca esa evidencia.

**Resultado del objetivo local:** `PASS` — la brecha de arquitectura entre el gate global y el gate de navegación queda corregida y trazada.

**Resultado global de navegación:** `NOT_VERIFIED` — pendiente de evidencia versionada generada por el workflow actualizado.

## Estado de gates

- `CONTENT_SYMMETRY = PASS` heredado y versionado en Run 13.
- `LANGUAGE_NAVIGATION = NOT_VERIFIED` hasta auditoría versionada posterior al nuevo workflow.
- `LINK_INTEGRITY = sin nueva regresión demostrada en esta iteración / no new regression demonstrated in this iteration`.
- `RELATIONAL_NAVIGATION = sin nueva regresión demostrada en esta iteración / no new regression demonstrated in this iteration`.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Paso siguiente

Verificar la primera auditoría versionada producida por el workflow global actualizado; si devuelve cero fallos, fijar `LANGUAGE_NAVIGATION = PASS`, y si devuelve fallos, reparar exclusivamente el primer `LANGUAGE_NAVIGATION_FAILURE` o `LANGUAGE_ANCHOR_FAILURE` listado sin rebajar el gate.

---

# EN · English

## Observed state

The required public corpus surfaces and the previous MAXPROC note were reread. `README.md` retains `7.3-CANDIDATE` as the active public, non-canonical frontier; `manifiestos/README.md` retains I–LXXXI + ∞; `neoaxiomas/README.md` retains NAX-01–14 and C-NAX-15–26; `propuestas/sintesis-abierta/README.md` preserves `CANDIDATE ≠ CANON`; `web4/README.md` still defines WEB4 as a public documentary specification rather than a final implementation.

The versioned structural ES/EN audit inherited from Run 13 is `PASS 0/0/0/0`, but Run 13 correctly left `LANGUAGE_SELECTOR_GATE = NOT_VERIFIED` because the selector gate existed as a separate workflow and its result was not materialised in a recoverable versioned audit.

## Selected problem

The defect was in control architecture rather than content: the global symmetry workflow that generates and versions audits did not execute the language-navigation gate. In addition, the selector auditor accepted any target beginning with `#es` or `#en`; it could therefore miss a selector whose link pointed to a nonexistent or incorrect anchor.

This allowed two potential false positives:

```text
CONTENT_SYMMETRY = PASS
LANGUAGE_NAVIGATION = NOT OBSERVABLE
→ INCOMPLETE GLOBAL STATE

VISIBLE SELECTOR
+ TARGET #es-wrong / #en-wrong
→ OLD AUDITOR COULD ACCEPT IT
```

## Action

`.github/scripts/audit_language_selectors.py` was strengthened to:

- require a visible selector before the ES body;
- derive the expected anchor from the real ES/EN headings;
- compare selector targets with those expected anchors;
- classify mismatches as `LANGUAGE_ANCHOR_FAILURE`;
- generate a versionable public audit at `auditorias/publicas/2026-08-24_auditoria_global_selectores_idioma_ES_EN.md`;
- retain `LANGUAGE_SELECTOR_GATE = FAIL` with non-zero exit whenever any defect exists.

The auditor was then integrated into `.github/workflows/audit-global-bilingual-symmetry.yml`. The global workflow now runs the following blocking sequence:

```text
CONTENT_SYMMETRY
→ LANGUAGE_NAVIGATION
→ COMMIT VERSIONED AUDITS
```

and adds the selector audit to the same automatic commit that preserves global symmetry and the Neoaxiomatic gate.

## Tests and result

Post-change inspection of the script and workflow confirms that strict anchor validation and global integration are fixed on `main`.

The combined commit observed before this delta exposes no traditional statuses, so missing status is still not interpreted as PASS. At the time of this note there is not yet a recoverable copy of the new versioned selector audit; global selector state therefore remains prudently `NOT_VERIFIED` until the updated workflow produces that evidence.

**Local target result:** `PASS` — the architectural gap between the global gate and language navigation has been corrected and traced.

**Global navigation result:** `NOT_VERIFIED` — pending versioned evidence generated by the updated workflow.

## Gate state

- `CONTENT_SYMMETRY = PASS` inherited and versioned in Run 13.
- `LANGUAGE_NAVIGATION = NOT_VERIFIED` until a versioned audit exists after the updated workflow.
- `LINK_INTEGRITY = no new regression demonstrated in this iteration`.
- `RELATIONAL_NAVIGATION = no new regression demonstrated in this iteration`.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Next step

Verify the first versioned audit produced by the updated global workflow; if it returns zero failures, fix `LANGUAGE_NAVIGATION = PASS`, and if it returns failures, repair only the first listed `LANGUAGE_NAVIGATION_FAILURE` or `LANGUAGE_ANCHOR_FAILURE` without weakening the gate.

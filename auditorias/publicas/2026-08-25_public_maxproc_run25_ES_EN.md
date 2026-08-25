# MAXPROC público · Run 25 · frescura de enlaces y auditoría relacional
# Public MAXPROC · Run 25 · link freshness and relational audit

**Fecha / Date:** 2026-08-25  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** corrección de la fecha hardcodeada del generador de auditoría relacional / correction of the hardcoded date in the relational-audit generator  
**Commit material / Material commit:** `b1edf719b772ba15eb873e1df4af78a58065dd83`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releyeron las superficies públicas de entrada y continuidad: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `web4/README.md`, las auditorías públicas vigentes y Run 24. La frontera continúa siendo **NEOCore™ 7.3-CANDIDATE**, activa, abierta a síntesis y no canónica. La Issue #161 continúa abierta como `CANDIDATE · OPEN SYNTHESIS` y conserva condiciones explícitas de promoción que no se consideran satisfechas por esta iteración.

## Problema elegido

Run 24 dejó `LINK_INTEGRITY` y `RELATIONAL_NAVIGATION` pendientes de reverificación fresca. La auditoría de rutas se regeneró sobre `main` actual y quedó limpia. Después se regeneró la auditoría relacional; sus métricas también quedaron limpias, pero reveló un defecto real del propio generador: el informe seguía escribiendo `Fecha / Date: 2026-08-12` aunque acababa de ejecutarse el 25 de agosto, porque la fecha estaba fijada literalmente en `.github/scripts/audit_relations_neocore.py`.

Ese defecto de procedencia impedía usar la fecha del informe como evidencia fiable de frescura aunque sus métricas hubieran sido recalculadas.

## Acción

Se modificó exclusivamente el generador relacional para calcular la fecha de ejecución en UTC mediante `datetime.now(timezone.utc).date().isoformat()` y usarla al renderizar `Fecha / Date`. No se modificaron manifiestos, neoaxiomas, relaciones curadas, Issues, cuerpos de Síntesis Abierta ni estados CANON/CANDIDATE.

Se regeneró después la auditoría relacional. El workflow temporal usado para ejecutar el delta fue eliminado por la propia ejecución.

## Pruebas y resultado

La auditoría fresca de rutas registra:

- Markdown activos revisados: **426**;
- rutas internas comprobadas: **10.778**;
- enlaces internos rotos: **0**;
- fallos canónicos críticos: **0**.

Su alcance no incluye disponibilidad remota de URLs externas ni validación semántica general de los **763** enlaces sólo a ancla; por tanto, ese límite se conserva explícito y no se transforma en un PASS más amplio de lo demostrado.

La auditoría relacional regenerada registra:

- fecha correcta: **2026-08-25**;
- cobertura del mapa curado: **81/81**;
- ausentes del mapa curado: **0**;
- neoaxiomas sin Síntesis específica: **0**;
- enlaces locales no resueltos: **0**;
- manifiestos sin relación entrante desde publicaciones/documentos aplicados: **0**.

**Resultado del defecto elegido:** `PASS`.

## Estado de gates

- `CONTENT_SYMMETRY = PASS` según el último gate global vigente, pendiente sólo de postcheck de esta nueva nota antes del cierre de Run 25.
- `LANGUAGE_NAVIGATION = PASS` según el último gate global vigente, pendiente sólo de postcheck de esta nueva nota antes del cierre de Run 25.
- `LINK_INTEGRITY = PASS_PATHS` · 0/10.778 rutas internas rotas; disponibilidad externa y semántica general de anchors quedan fuera de ese PASS.
- `RELATIONAL_NAVIGATION = PASS_DOCUMENTARY` · 81/81, sin huecos estructurales detectados por el auditor relacional; relación semántica/causal sigue requiriendo SAN/revisión humana.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residuos

No queda residuo del defecto corregido. El límite verificable más inmediato es que la auditoría de enlaces inventaría **763 enlaces sólo a ancla** pero no comprueba de forma general que cada destino corresponda a un anchor Markdown renderizado existente.

## PASO_SIGUIENTE / NEXT_STEP

Construir o ejecutar un gate público específico de integridad de anchors Markdown internos sobre las superficies activas y, si detecta algún destino inexistente, reparar exclusivamente el primer anchor roto demostrado.

---

# EN · English

## Observed state

The public entry and continuity surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `web4/README.md`, the current public audits and Run 24. The frontier remains **NEOCore™ 7.3-CANDIDATE**, active, open to synthesis and non-canonical. Issue #161 remains open as `CANDIDATE · OPEN SYNTHESIS` and retains explicit promotion conditions that are not considered satisfied by this iteration.

## Selected problem

Run 24 left `LINK_INTEGRITY` and `RELATIONAL_NAVIGATION` pending fresh reverification. The route audit was regenerated against current `main` and remained clean. The relational audit was then regenerated; its metrics also remained clean, but it exposed a real defect in the generator itself: the report still wrote `Fecha / Date: 2026-08-12` even though it had just run on 25 August, because the date was literally hardcoded in `.github/scripts/audit_relations_neocore.py`.

That provenance defect made the report date unreliable as freshness evidence even though its metrics had actually been recalculated.

## Action

Only the relational generator was changed so that it calculates the execution date in UTC through `datetime.now(timezone.utc).date().isoformat()` and uses it when rendering `Fecha / Date`. No manifesto, Neoaxiom, curated relation, Issue, Open Synthesis body or CANON/CANDIDATE state was changed.

The relational audit was then regenerated. The temporary workflow used to execute the delta was removed by the execution itself.

## Tests and result

The fresh route audit reports:

- active Markdown reviewed: **426**;
- internal routes checked: **10,778**;
- broken internal links: **0**;
- critical canonical failures: **0**.

Its scope does not include remote availability of external URLs or general semantic validation of the **763** anchor-only links; that limitation is therefore preserved explicitly and is not converted into a broader PASS than the evidence supports.

The regenerated relational audit reports:

- correct date: **2026-08-25**;
- curated-map coverage: **81/81**;
- missing from curated map: **0**;
- Neoaxioms without dedicated Synthesis: **0**;
- unresolved local links: **0**;
- manifestos without inbound relation from applied publications/documents: **0**.

**Selected-defect result:** `PASS`.

## Gate state

- `CONTENT_SYMMETRY = PASS` according to the latest current global gate, pending only the postcheck of this new note before Run 25 closes.
- `LANGUAGE_NAVIGATION = PASS` according to the latest current global gate, pending only the postcheck of this new note before Run 25 closes.
- `LINK_INTEGRITY = PASS_PATHS` · 0/10,778 broken internal routes; external availability and general anchor semantics remain outside that PASS.
- `RELATIONAL_NAVIGATION = PASS_DOCUMENTARY` · 81/81, with no structural gaps detected by the relational auditor; semantic/causal relations still require SAN/human review.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residues

No residue remains from the corrected defect. The nearest verifiable boundary is that the link audit inventories **763 anchor-only links** but does not generally verify that every target corresponds to an existing rendered Markdown anchor.

## PASO_SIGUIENTE / NEXT_STEP

Build or execute a dedicated public internal-Markdown-anchor integrity gate over active surfaces and, if it detects a missing destination, repair exclusively the first demonstrated broken anchor.

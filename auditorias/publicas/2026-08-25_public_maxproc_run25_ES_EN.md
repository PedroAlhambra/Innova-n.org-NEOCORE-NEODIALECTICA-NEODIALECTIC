# MAXPROC público · Run 25 · frescura de enlaces y auditoría relacional
# Public MAXPROC · Run 25 · link freshness and relational audit

**Fecha / Date:** 2026-08-25  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** corrección de la fecha hardcodeada del generador de auditoría relacional / correction of the hardcoded date in the relational-audit generator  
**Commit material / Material commit:** `b1edf719b772ba15eb873e1df4af78a58065dd83`  
**Resultado global / Global result:** `FAIL · LANGUAGE_NAVIGATION_FAILURE = 1`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releyeron `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `web4/README.md`, las auditorías públicas vigentes y Run 24. La frontera continúa siendo **NEOCore™ 7.3-CANDIDATE**, activa, abierta a síntesis y no canónica. La Issue #161 continúa abierta como `CANDIDATE · OPEN SYNTHESIS`; esta iteración no satisface ni altera su gate de promoción.

## Problema elegido

Run 24 dejó `LINK_INTEGRITY` y `RELATIONAL_NAVIGATION` pendientes de reverificación fresca. La auditoría de rutas se regeneró sobre `main` actual y quedó limpia. Al regenerar después la auditoría relacional, las métricas también quedaron limpias, pero apareció un defecto real de procedencia: el informe seguía escribiendo `Fecha / Date: 2026-08-12` porque esa fecha estaba fijada literalmente en `.github/scripts/audit_relations_neocore.py`.

## Acción

Se corrigió exclusivamente esa causa raíz: el generador relacional calcula ahora la fecha de ejecución UTC mediante `datetime.now(timezone.utc).date().isoformat()` y la usa al renderizar el informe. No se modificaron manifiestos, neoaxiomas, relaciones curadas, Issues, cuerpos de Síntesis Abierta ni estados CANON/CANDIDATE. La auditoría relacional se regeneró y el mecanismo temporal de esa reparación fue eliminado.

## Pruebas y resultado

La auditoría fresca de rutas registra **426 Markdown activos**, **10.778 rutas internas comprobadas**, **0 enlaces internos rotos** y **0 fallos canónicos críticos**. Su alcance no comprueba disponibilidad remota de URLs externas ni la semántica general de todos los enlaces sólo a ancla.

La auditoría relacional regenerada registra fecha correcta **2026-08-25**, cobertura **81/81**, **0** ausentes del mapa curado, **0** neoaxiomas sin Síntesis específica, **0** enlaces locales no resueltos y **0** manifiestos sin relación entrante desde publicaciones/documentos aplicados.

**Resultado del defecto elegido:** `PASS`.

El postcheck bloqueante posterior comprobó primero `CONTENT_SYMMETRY` y obtuvo **0 fallos**. A continuación `audit_language_selectors.py` auditó **356** superficies ES/EN y detectó **1** `LANGUAGE_NAVIGATION_FAILURE`: `auditorias/publicas/2026-08-09_postcheck_LVI_no_control_readmes_enlaces_ES_EN.md` carece de selector ES y EN. El fallo procede del generador `.github/scripts/audit_markdown_links_readmes.py`, que regenera una superficie bilingüe con gates `## ES · Resultado` y `## EN · Result` sin insertar selector visible en cabecera.

Conforme a la regla de una sola reparación material por iteración, este segundo defecto demostrado **no se repara en Run 25**. El workflow temporal de postcheck que quedó tras el fallo fue retirado sin alterar el corpus sustantivo.

## Estado de gates al cierre

- `CONTENT_SYMMETRY = PASS` · postcheck: 0 fallos.
- `LANGUAGE_NAVIGATION = FAIL` · **1/356** superficies falla.
- `LINK_INTEGRITY = PASS_PATHS` · **0/10.778** rutas internas rotas; no se amplía el PASS fuera del alcance del auditor.
- `RELATIONAL_NAVIGATION = PASS_DOCUMENTARY` · **81/81**, sin huecos estructurales documentales detectados.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.
- `GLOBAL_CORPUS_PASS = NO`.

## Residuo único

El generador `.github/scripts/audit_markdown_links_readmes.py` crea su propio informe ES/EN sin selector visible de idioma, por lo que cada regeneración puede reintroducir `LANGUAGE_NAVIGATION_FAILURE`.

## PASO_SIGUIENTE / NEXT_STEP

Corregir exclusivamente `.github/scripts/audit_markdown_links_readmes.py` para que su informe incluya un selector visible con anchors reales `#es--resultado` y `#en--result`, regenerar el informe y volver a ejecutar `audit_language_selectors.py` hasta demostrar `1 → 0`, sin abordar ningún segundo delta en esa iteración.

---

# EN · English

## Observed state

`README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `web4/README.md`, the current public audits and Run 24 were reread. The frontier remains **NEOCore™ 7.3-CANDIDATE**, active, open to synthesis and non-canonical. Issue #161 remains open as `CANDIDATE · OPEN SYNTHESIS`; this iteration neither satisfies nor changes its promotion gate.

## Selected problem

Run 24 left `LINK_INTEGRITY` and `RELATIONAL_NAVIGATION` pending fresh reverification. The route audit was regenerated against current `main` and remained clean. When the relational audit was then regenerated, its metrics also remained clean, but a real provenance defect appeared: the report still wrote `Fecha / Date: 2026-08-12` because that date was literally hardcoded in `.github/scripts/audit_relations_neocore.py`.

## Action

Only that root cause was corrected: the relational generator now calculates the UTC execution date through `datetime.now(timezone.utc).date().isoformat()` and uses it when rendering the report. No manifesto, Neoaxiom, curated relation, Issue, Open Synthesis body or CANON/CANDIDATE state was changed. The relational audit was regenerated and the temporary repair mechanism was removed.

## Tests and result

The fresh route audit reports **426 active Markdown files**, **10,778 internal routes checked**, **0 broken internal links** and **0 critical canonical failures**. Its scope does not check remote availability of external URLs or the general semantics of every anchor-only link.

The regenerated relational audit reports the correct date **2026-08-25**, coverage **81/81**, **0** missing from the curated map, **0** Neoaxioms without dedicated Synthesis, **0** unresolved local links and **0** manifestos without inbound relation from applied publications/documents.

**Selected-defect result:** `PASS`.

The subsequent blocking postcheck first checked `CONTENT_SYMMETRY` and obtained **0 failures**. `audit_language_selectors.py` then audited **356** ES/EN surfaces and detected **1** `LANGUAGE_NAVIGATION_FAILURE`: `auditorias/publicas/2026-08-09_postcheck_LVI_no_control_readmes_enlaces_ES_EN.md` lacks both ES and EN selectors. The failure originates in `.github/scripts/audit_markdown_links_readmes.py`, which regenerates a bilingual surface with `## ES · Resultado` and `## EN · Result` gates without inserting a visible header selector.

Under the one-material-repair-per-iteration rule, this second demonstrated defect **is not repaired in Run 25**. The temporary postcheck workflow left by the failure was removed without changing the substantive corpus.

## Gate state at close

- `CONTENT_SYMMETRY = PASS` · postcheck: 0 failures.
- `LANGUAGE_NAVIGATION = FAIL` · **1/356** surfaces fails.
- `LINK_INTEGRITY = PASS_PATHS` · **0/10,778** broken internal routes; the PASS is not broadened beyond the auditor's scope.
- `RELATIONAL_NAVIGATION = PASS_DOCUMENTARY` · **81/81**, with no documentary structural gaps detected.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.
- `GLOBAL_CORPUS_PASS = NO`.

## Single residue

The `.github/scripts/audit_markdown_links_readmes.py` generator creates its own ES/EN report without a visible language selector, so every regeneration can reintroduce `LANGUAGE_NAVIGATION_FAILURE`.

## PASO_SIGUIENTE / NEXT_STEP

Correct only `.github/scripts/audit_markdown_links_readmes.py` so that its report includes a visible selector targeting the real `#es--resultado` and `#en--result` anchors, regenerate the report and rerun `audit_language_selectors.py` until `1 → 0` is demonstrated, without addressing any second delta in that iteration.

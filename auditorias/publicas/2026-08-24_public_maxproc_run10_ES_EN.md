# MAXPROC público · Run 10 · reparación de navegación lingüística LXXIX
# Public MAXPROC · Run 10 · LXXIX language-navigation repair

**Fecha / Date:** 2026-08-24 10:35 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración del selector ES/EN en LXXIX, ruta viva + espejo canónico / restoration of the ES/EN selector in LXXIX, live route + canonical mirror  
**Commits del delta / Delta commits:** `443669331ca67aa7f121de159b147b02b7a7cf8e` · `9a0d806eb208bab6adf6b5e3c54ef4afda21c5bd` · corrección conservativa inmediata / immediate conservative correction `1a408329f64580c57b95644a2be034dd79c0293c`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies públicas obligatorias: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, la auditoría global ES/EN vigente y la nota MAXPROC anterior.

La frontera pública continúa siendo `7.3-CANDIDATE`, abierta y no canónica. El índice de manifiestos mantiene **I–LXXXI + ∞**. La capa neoaxiomática mantiene **NAX-01–NAX-14** como canon y **C-NAX-15–C-NAX-26** como candidatos abiertos a SAN™.

La auditoría global ES/EN versionada observada antes del delta informa **321 Markdown activos**, **255 documentos ES/EN divididos**, **1 fallo estructural**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**. El fallo estructural restante es `auditorias/publicas/2026-08-24_public_maxproc_run06_ES_EN.md`; por tanto no existe PASS global de contenido demostrable.

Las PR públicas abiertas siguen siendo #165 y #167, ambas antiguas ramas de mantenimiento PRE-7.3, no fusionadas y no utilizadas en esta iteración. La Issue #172 continúa abierta como lote 04 de autosíntesis `7.3-CANDIDATE`; #161 y #169 mantienen explícitamente que la candidata no equivale a canon.

## Problema elegido

Run 09 dejó como siguiente paso único **LXXIX**, que conservaba contenido ES/EN materialmente completo pero carecía del selector inicial visible en la ruta viva y en el espejo canónico.

El defecto era de capacidad de lectura y navegación:

`CONTENIDO BILINGÜE PRESENTE + SELECTOR AUSENTE = LANGUAGE_NAVIGATION_FAILURE`.

## Acción

Se añadió exclusivamente el selector visible:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

a:

- `manifiestos/79_contra_alarmismo_sin_sintesis_responsabilidad_alternativa_ES_EN.md`;
- `manifiestos/canonicos/LXXIX_contra_alarmismo_sin_sintesis_responsabilidad_alternativa_ES_EN.md`.

El commit de la ruta viva muestra como cambio material únicamente la inserción del selector. Durante la reconstrucción conservativa del espejo canónico se introdujo accidentalmente una variante tipográfica `construction` en dos rutas internas LXXVI; se detectó en el diff y se corrigió inmediatamente en `1a408329...`, restaurando exactamente `construccion`. No se deja esa regresión abierta.

No se modificó contenido sustantivo del manifiesto, genealogía, estado, Síntesis, Neoaxiomas™, Issues ni reglas de canon.

## Pruebas y resultado

La lectura posterior confirma el selector antes de `# ES · Castellano` tanto en la ruta viva como en el espejo canónico, apuntando a los anchors reales `#es--castellano` y `#en--english`.

El diff de `443669331...` demuestra que la ruta viva sólo recibió el selector. El diff de corrección `1a408329...` demuestra la restauración de las dos rutas LXXVI del espejo canónico tras la detección inmediata del typo de reconstrucción.

**Resultado del objetivo LXXIX:** `PASS`.

No se declara `LANGUAGE_SELECTOR_GATE = PASS` global: LXXX y LXXXI siguen pendientes en ruta viva y espejo canónico, es decir, **4 superficies activas conocidas** después de esta reparación.

El commit final no expone statuses CI recuperables; ausencia de status **no equivale a PASS**.

## Residuos

- Simetría estructural global versionada: **1 fallo conocido**, Run 06.
- Navegación lingüística: **LXXX–LXXXI**, ruta viva + espejo canónico.
- `7.3-CANDIDATE`: `ACTIVE / NOT_CANON`.
- PR #165 y #167: `OPEN / NOT_MERGED`.

## Paso siguiente

Reparar **LXXX** añadiendo el selector visible ES/EN en su ruta viva y en su espejo canónico, preservando íntegramente contenido y rutas internas, y verificar ambos documentos después del cambio.

---

# EN · English

## Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, the current global ES/EN audit and the previous MAXPROC note.

The public frontier remains `7.3-CANDIDATE`, open and non-canonical. The manifesto index remains **I–LXXXI + ∞**. The Neoaxiomatic layer retains **NAX-01–NAX-14** as canon and **C-NAX-15–C-NAX-26** as candidates open to SAN™.

The versioned global ES/EN audit observed before the delta reports **321 active Markdown files**, **255 split ES/EN documents**, **1 structural failure**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**. The remaining structural failure is `auditorias/publicas/2026-08-24_public_maxproc_run06_ES_EN.md`; therefore no global content PASS is demonstrated.

The open public PRs remain #165 and #167, both older PRE-7.3 maintenance branches, unmerged and unused in this iteration. Issue #172 remains open as `7.3-CANDIDATE` self-synthesis batch 04; #161 and #169 explicitly preserve that the candidate does not equal canon.

## Selected problem

Run 09 left **LXXIX** as its single next step. It retained materially complete ES/EN content but lacked the visible initial language selector in both the live route and canonical mirror.

This was a reader-capability and navigation defect:

`BILINGUAL CONTENT PRESENT + SELECTOR ABSENT = LANGUAGE_NAVIGATION_FAILURE`.

## Action

Only the visible selector:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

was added to:

- `manifiestos/79_contra_alarmismo_sin_sintesis_responsabilidad_alternativa_ES_EN.md`;
- `manifiestos/canonicos/LXXIX_contra_alarmismo_sin_sintesis_responsabilidad_alternativa_ES_EN.md`.

The live-route commit shows the selector as the only material change. During conservative reconstruction of the canonical mirror, an accidental `construction` spelling variant was introduced in two internal LXXVI routes; the diff exposed it and it was immediately corrected in `1a408329...`, restoring the exact `construccion` paths. That regression is not left open.

No substantive manifesto content, genealogy, status, Synthesis, Neoaxioms™, Issues or canon rules were changed.

## Tests and result

A post-read confirms the selector before `# ES · Castellano` in both the live route and canonical mirror, targeting the actual `#es--castellano` and `#en--english` anchors.

The `443669331...` diff demonstrates that the live route received only the selector. The `1a408329...` correction diff demonstrates restoration of the two LXXVI canonical paths after immediate detection of the reconstruction typo.

**LXXIX target result:** `PASS`.

No global `LANGUAGE_SELECTOR_GATE = PASS` is declared: LXXX and LXXXI remain pending in both live and canonical routes, leaving **4 known active surfaces** after this repair.

The final commit exposes no recoverable CI statuses; absence of status **does not equal PASS**.

## Residues

- Versioned global structural symmetry: **1 known failure**, Run 06.
- Language navigation: **LXXX–LXXXI**, live route + canonical mirror.
- `7.3-CANDIDATE`: `ACTIVE / NOT_CANON`.
- PR #165 and #167: `OPEN / NOT_MERGED`.

## Next step

Repair **LXXX** by adding the visible ES/EN selector to its live route and canonical mirror, preserving all content and internal paths exactly, then verify both documents after the change.

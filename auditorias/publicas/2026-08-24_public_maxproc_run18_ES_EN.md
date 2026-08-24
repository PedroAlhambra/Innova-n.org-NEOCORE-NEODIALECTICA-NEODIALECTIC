# MAXPROC público · Run 18 · reparación de navegación lingüística Stanford/ACE
# Public MAXPROC · Run 18 · Stanford/ACE language-navigation repair

**Fecha / Date:** 2026-08-24 18:39 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración del selector ES/EN en `analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md` / restoration of the ES/EN selector in `analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md`  
**Commit material / Material commit:** `041986b0b2e52b650f30781b4add211b62c3cf33`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, la auditoría global de simetría ES/EN y la auditoría global de selectores vigente.

La frontera pública continúa siendo **NEOCore™ 7.3-CANDIDATE**, activa y no canónica. La colección de manifiestos permanece en **I–LXXXI + ∞** y la capa neoaxiomática mantiene **NAX-01–NAX-14** como canon y **C-NAX-15–C-NAX-26** como candidatos abiertos. WEB4™ continúa documentada como especificación pública; no se interpreta como implementación final ni se promueve 7.3-CANDIDATE.

La auditoría estructural vigente informa **330 Markdown activos**, **264 documentos ES/EN divididos**, **0 fallos estructurales**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**. Por tanto `CONTENT_SYMMETRY = PASS` para ese corte versionado.

La auditoría global de selectores inmediatamente anterior a este delta informa **348 páginas ES/EN explícitas auditadas** y **124 fallos**, por lo que `LANGUAGE_NAVIGATION = FAIL`. Su primer residuo era `analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md`.

## Problema elegido

El documento Stanford/ACE contenía capas completas `## ES` y `## EN`, pero no disponía de selector visible antes del cuerpo español.

`CONTENIDO BILINGÜE PRESENTE + SELECTOR AUSENTE = LANGUAGE_NAVIGATION_FAILURE`.

## Acción

Se añadió exclusivamente el selector compatible con los anchors reales de sus encabezados existentes:

`[ES](#es) · [EN](#en)`

antes del separador que precede a `## ES`.

No se modificaron tesis, cronología, capturas, enlaces de fuente, genealogía, relaciones con manifiestos, cautelas ni contenido ES/EN.

## Pruebas y resultado

La lectura posterior del archivo confirma:

1. selector visible antes del cuerpo ES;
2. destino ES `#es`, correspondiente al encabezado real `## ES`;
3. destino EN `#en`, correspondiente al encabezado real `## EN`;
4. preservación del contenido sustantivo y de las relaciones documentales.

**Resultado del objetivo local:** `PASS`.

No se declara PASS global de navegación lingüística hasta que el workflow regenere la auditoría global sobre el nuevo head. La ausencia de workflow run recuperable inmediatamente después del commit no se interpreta como éxito.

## Estado de gates

- `CONTENT_SYMMETRY = PASS` en la auditoría estructural versionada vigente.
- `LANGUAGE_NAVIGATION = FAIL` en la última auditoría global disponible, pendiente de regeneración posterior al delta.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residuos

La última auditoría global disponible conserva **124 fallos de navegación lingüística** antes de esta reparación. El archivo Stanford/ACE ya no presenta el defecto local, pero el contador global sólo se actualizará cuando el gate vuelva a ejecutarse y versione el informe.

## PASO_SIGUIENTE

Reparar exclusivamente `analisis/publicos/2026-04-15-linkedin-como-red-profesional-fragmentada.md`, siguiente `LANGUAGE_NAVIGATION_FAILURE` listado, añadiendo selector ES/EN con anchors reales sin alterar contenido sustantivo; después verificar la nueva auditoría global sin rebajar el gate.

---

# EN · English

## Observed state

`README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, the global ES/EN symmetry audit and the current global language-selector audit were reread.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, active and non-canonical. The manifesto collection remains **I–LXXXI + ∞**, while the Neoaxiomatic layer retains **NAX-01–NAX-14** as canon and **C-NAX-15–C-NAX-26** as open candidates. WEB4™ remains documented as a public specification; it is not treated as a final implementation and 7.3-CANDIDATE is not promoted.

The current structural audit reports **330 active Markdown files**, **264 split ES/EN documents**, **0 structural failures**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**. Therefore `CONTENT_SYMMETRY = PASS` for that versioned cut.

The global selector audit immediately preceding this delta reports **348 explicit ES/EN pages audited** and **124 failures**, so `LANGUAGE_NAVIGATION = FAIL`. Its first residue was `analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md`.

## Selected problem

The Stanford/ACE document contained complete `## ES` and `## EN` layers but lacked a visible selector before the Spanish body.

`BILINGUAL CONTENT PRESENT + SELECTOR ABSENT = LANGUAGE_NAVIGATION_FAILURE`.

## Action

Only the selector matching the real anchors of the existing headings was added:

`[ES](#es) · [EN](#en)`

before the separator preceding `## ES`.

No thesis, chronology, capture, source link, genealogy, manifesto relation, safeguard or ES/EN substantive content was changed.

## Tests and result

Post-change inspection confirms:

1. a visible selector before the ES body;
2. ES target `#es`, matching the real `## ES` heading;
3. EN target `#en`, matching the real `## EN` heading;
4. preservation of substantive content and documentary relations.

**Local target result:** `PASS`.

No global language-navigation PASS is declared until the workflow regenerates the global audit on the new head. The absence of an immediately recoverable workflow run after the commit is not treated as success.

## Gate state

- `CONTENT_SYMMETRY = PASS` in the current versioned structural audit.
- `LANGUAGE_NAVIGATION = FAIL` in the latest available global audit, pending post-delta regeneration.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residues

The latest available global audit retains **124 language-navigation failures** before this repair. The Stanford/ACE file no longer has the local defect, but the global counter will only update after the gate runs again and versions its report.

## NEXT_STEP

Repair only `analisis/publicos/2026-04-15-linkedin-como-red-profesional-fragmentada.md`, the next listed `LANGUAGE_NAVIGATION_FAILURE`, by adding an ES/EN selector with real anchors without altering substantive content; then verify the regenerated global audit without weakening the gate.

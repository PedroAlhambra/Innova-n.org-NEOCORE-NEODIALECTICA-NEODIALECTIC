# MAXPROC público · Run 17 · reparación del primer fallo global de navegación lingüística
# Public MAXPROC · Run 17 · repair of the first global language-navigation failure

**Fecha / Date:** 2026-08-24 17:42 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración del selector ES/EN en `analisis/2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md` / restoration of the ES/EN selector in `analisis/2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md`  
**Commit material / Material commit:** `ab11d0807d17e7ebb0df53e35a6376e6da91c66b`  
**Commit automático de auditoría / Automated audit commit:** `dd00b68359386e0e80ed234ea163ee03e33cb870`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `web4/README.md`, la auditoría global ES/EN vigente, la auditoría global de selectores y la nota pública MAXPROC anterior.

La frontera pública continúa como **NEOCore™ 7.3-CANDIDATE**, activa y no canónica. La colección mantiene **I–LXXXI + ∞**; la capa neoaxiomática conserva **NAX-01–NAX-14** como canon y **C-NAX-15–C-NAX-26** como candidatos abiertos; WEB4™ continúa siendo especificación documental pública y no implementación final.

La auditoría estructural ES/EN versionada informa **329 Markdown activos**, **263 documentos ES/EN divididos**, **0 fallos estructurales**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**. Por tanto `CONTENT_SYMMETRY = PASS` para ese corte documentado.

La auditoría global de navegación lingüística previa a la reparación informaba **347 páginas ES/EN explícitas auditadas** y **125 fallos**, con `LANGUAGE_SELECTOR_GATE = FAIL`. El primer fallo listado era `analisis/2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md`, sin selector ES ni EN.

Las PR públicas #165 y #167 permanecen `OPEN / NOT_MERGED / NOT_MERGEABLE` y no se han utilizado en esta iteración.

## Problema elegido

El documento DistroKid–Spotify contenía ambas capas completas y ordenadas:

`# ES · Castellano` → `# EN · English`

pero carecía de selector visible antes del cuerpo principal. Conforme al gate vigente:

`CONTENIDO BILINGÜE PRESENTE + SELECTOR AUSENTE = LANGUAGE_NAVIGATION_FAILURE`.

## Acción

Se añadió exclusivamente, después de los metadatos y antes del cuerpo ES:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

No se modificaron hechos, cifras, cautelas, nombres de proyectos, identificadores, relaciones con manifiestos, genealogía ni contenido sustantivo.

## Pruebas y resultado

La lectura posterior de la superficie confirma:

1. selector visible antes de `# ES · Castellano`;
2. destino ES `#es--castellano`;
3. destino EN `#en--english`;
4. presencia real de ambos encabezados de idioma;
5. conservación del resto del documento.

Después de la reparación, el workflow global regeneró la auditoría en `dd00b68359386e0e80ed234ea163ee03e33cb870`. La nueva auditoría demuestra **347 páginas auditadas**, **124 fallos** y `LANGUAGE_SELECTOR_GATE = FAIL`: el contador baja exactamente en una unidad y el documento reparado desaparece de la lista.

**Resultado del objetivo local:** `PASS`.

**Resultado global de navegación:** `FAIL · 124/347`.

## Estado de gates

- `CONTENT_SYMMETRY = PASS` en la auditoría estructural versionada vigente.
- `LANGUAGE_NAVIGATION = FAIL` en la auditoría global regenerada: **124/347**.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`; no se declara PASS fresco.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`; no se declara PASS fresco.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residuos

El primer fallo anterior ha quedado cerrado y eliminado del inventario vivo. El nuevo primer fallo listado es `analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md`, también por ausencia de selector ES/EN. Permanecen otros **123** fallos adicionales de navegación lingüística distribuidos por análisis, auditorías, anuncios, manifiestos y otras superficies activas.

## PASO_SIGUIENTE

Reparar **exclusivamente** `analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md`, añadiendo un selector ES/EN con anchors reales antes del cuerpo español, sin alterar contenido sustantivo, y después volver a ejecutar/verificar la auditoría global sin rebajar el gate.

---

# EN · English

## Observed state

`README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `web4/README.md`, the current global ES/EN audit, the global language-selector audit and the previous public MAXPROC note were reread.

The public frontier remains **NEOCore™ 7.3-CANDIDATE**, active and non-canonical. The collection remains **I–LXXXI + ∞**; the Neoaxiomatic layer retains **NAX-01–NAX-14** as canon and **C-NAX-15–C-NAX-26** as open candidates; WEB4™ remains a public documentary specification rather than a final implementation.

The versioned structural ES/EN audit reports **329 active Markdown files**, **263 split ES/EN documents**, **0 structural failures**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**. Therefore `CONTENT_SYMMETRY = PASS` for that documented cut.

The global language-navigation audit before the repair reported **347 explicit ES/EN pages audited** and **125 failures**, with `LANGUAGE_SELECTOR_GATE = FAIL`. The first listed failure was `analisis/2026-08-04_Actualizacion_Auditoria-DistroKid-Spotify.md`, missing both ES and EN selector links.

Public PRs #165 and #167 remain `OPEN / NOT_MERGED / NOT_MERGEABLE` and were not used in this iteration.

## Selected problem

The DistroKid–Spotify document contained both complete and ordered language layers:

`# ES · Castellano` → `# EN · English`

but lacked a visible selector before the main body. Under the current gate:

`BILINGUAL CONTENT PRESENT + SELECTOR ABSENT = LANGUAGE_NAVIGATION_FAILURE`.

## Action

Only the following selector was inserted after metadata and before the ES body:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

No facts, figures, safeguards, project names, identifiers, manifesto relations, genealogy or substantive content were changed.

## Tests and result

Post-change inspection confirms:

1. a visible selector before `# ES · Castellano`;
2. ES target `#es--castellano`;
3. EN target `#en--english`;
4. actual presence of both language headings;
5. preservation of the rest of the document.

After the repair, the global workflow regenerated the audit in `dd00b68359386e0e80ed234ea163ee03e33cb870`. The new audit demonstrates **347 pages audited**, **124 failures** and `LANGUAGE_SELECTOR_GATE = FAIL`: the counter drops by exactly one and the repaired document disappears from the list.

**Local target result:** `PASS`.

**Global navigation result:** `FAIL · 124/347`.

## Gate state

- `CONTENT_SYMMETRY = PASS` in the current versioned structural audit.
- `LANGUAGE_NAVIGATION = FAIL` in the regenerated global audit: **124/347**.
- `LINK_INTEGRITY = NOT_REVERIFIED_IN_THIS_DELTA`; no fresh PASS is declared.
- `RELATIONAL_NAVIGATION = NOT_REVERIFIED_IN_THIS_DELTA`; no fresh PASS is declared.
- `CANONICAL_STATE = 7.3-CANDIDATE / NOT_CANON`.

## Residues

The previous first failure has been closed and removed from the live inventory. The new first listed failure is `analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md`, also due to missing ES/EN selector links. Another **123** language-navigation failures remain across analyses, audits, announcements, manifestos and other active surfaces.

## NEXT_STEP

Repair **only** `analisis/publicos/2026-04-01_stanford-ace-y-marco-previo-neodialectico.md` by adding an ES/EN selector with real anchors before the Spanish body, without altering substantive content, then rerun/verify the global audit without weakening the gate.

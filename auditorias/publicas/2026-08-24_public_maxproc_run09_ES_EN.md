# MAXPROC público · Run 09 · reparación de navegación lingüística LXXVIII
# Public MAXPROC · Run 09 · LXXVIII language-navigation repair

**Fecha / Date:** 2026-08-24 10:09 CEST  
**Estado observado / Observed state:** `7.3-CANDIDATE = ACTIVE_PUBLIC_FRONTIER / NOT_CANON`  
**Delta material / Material delta:** restauración del selector ES/EN en LXXVIII, ruta viva + espejo canónico / restoration of the ES/EN selector in LXXVIII, live route + canonical mirror  
**Commits del delta / Delta commits:** `dcd2bb7918480379e7ddc75d2a9a5a5bc3b5dc32` · `b6e4175fb3a1a6c301d0e88fd262549cc202f4ae`

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Estado observado

Se releen las superficies públicas obligatorias: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, la auditoría global ES/EN vigente y la nota pública MAXPROC anterior.

La frontera sigue siendo `7.3-CANDIDATE`, abierta y no canónica. El índice de manifiestos mantiene I–LXXXI + ∞ y `neoaxiomas/README.md` mantiene NAX-01–14 como canon y C-NAX-15–26 como candidatos abiertos a SAN™.

La auditoría global ES/EN versionada vigente informa **320 Markdown activos**, **254 documentos ES/EN divididos**, **1 fallo estructural**, **0 fallos de marcadores**, **0 superficies pareadas pendientes** y **0 plantillas Issue asimétricas**. El único fallo estructural listado es `2026-08-24_public_maxproc_run06_ES_EN.md`; por tanto no existe PASS global de contenido demostrable.

Las PR públicas #165 y #167 siguen abiertas y no fusionadas; ambas son mantenimiento antiguo de referencias PRE-7.3 y no forman parte de este delta. La Issue #172 mantiene abierto el lote 04 de autosíntesis 7.3-CANDIDATE, sin promoción canónica.

## Problema elegido

La nota Run 08 dejó como siguiente paso único la primera regresión confirmada de navegación lingüística: **LXXVIII contenía las dos capas `# ES` y `# EN`, pero carecía del selector inicial visible** tanto en su ruta viva como en su espejo canónico.

Esto es un fallo de capacidad de lectura y navegación, no un fallo de traducción. El lector podía llegar al documento bilingüe pero no saltar directamente a la capa lingüística deseada desde la cabecera.

## Acción

Se añadió exclusivamente el selector:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

antes del separador inicial en:

- `manifiestos/78_neorrenacimiento_incontrolabilidad_intrinseca_sistema_humano_ES_EN.md`;
- `manifiestos/canonicos/LXXVIII_neorrenacimiento_incontrolabilidad_intrinseca_sistema_humano_ES_EN.md`.

No se modificó contenido sustantivo, genealogía, estado, referencias cruzadas, Síntesis, Neoaxiomas™, Issues ni reglas de canon.

**Commits:** `dcd2bb7918480379e7ddc75d2a9a5a5bc3b5dc32` y `b6e4175fb3a1a6c301d0e88fd262549cc202f4ae`.

## Pruebas y resultado

La lectura posterior de ambas superficies confirma que el selector aparece antes de `# ES · Castellano` y apunta a los anchors `#es--castellano` y `#en--english` que corresponden a las dos cabeceras reales del documento.

**Resultado del objetivo LXXVIII:** `PASS`.

No se declara `LANGUAGE_SELECTOR_GATE = PASS` global: LXXIX, LXXX y LXXXI continúan materialmente verificados como superficies sin selector en ruta viva y espejo canónico, es decir, **al menos 6 superficies activas pendientes** después de esta reparación. Tampoco se observa un workflow run recuperable asociado al último commit, por lo que ausencia de CI no se interpreta como PASS.

## Residuos

- Simetría estructural global versionada: **1 fallo conocido**, Run 06.
- Navegación lingüística: LXXIX–LXXXI siguen pendientes en ruta viva y espejo canónico.
- `7.3-CANDIDATE` continúa `NOT_CANON`.
- PR #165 y #167 continúan abiertas y no fusionadas.

## Paso siguiente

Reparar **LXXIX** añadiendo el mismo selector visible ES/EN en su ruta viva y en su espejo canónico, sin modificar contenido sustantivo, y verificar ambos documentos después del cambio.

---

# EN · English

## Observed state

The required public surfaces were reread: `README.md`, `manifiestos/README.md`, `neoaxiomas/README.md`, `propuestas/sintesis-abierta/README.md`, `auditorias/publicas/README.md`, `web4/README.md`, the current global ES/EN audit and the previous public MAXPROC note.

The frontier remains `7.3-CANDIDATE`, open and non-canonical. The manifesto index remains I–LXXXI + ∞ and `neoaxiomas/README.md` retains NAX-01–14 as canon and C-NAX-15–26 as candidates open to SAN™.

The current versioned global ES/EN audit reports **320 active Markdown files**, **254 split ES/EN documents**, **1 structural failure**, **0 marker failures**, **0 paired surfaces pending review** and **0 asymmetric Issue templates**. The only listed structural failure is `2026-08-24_public_maxproc_run06_ES_EN.md`; therefore no global content PASS is demonstrated.

Public PRs #165 and #167 remain open and unmerged; both are older PRE-7.3 reference-maintenance work and are outside this delta. Issue #172 keeps batch 04 of 7.3-CANDIDATE self-synthesis open, without canonical promotion.

## Selected problem

Run 08 left as its single next step the first confirmed language-navigation regression: **LXXVIII contained both `# ES` and `# EN` layers but lacked the visible initial selector** in both its live route and canonical mirror.

This is a reader-capability and navigation failure rather than a translation failure. A reader could reach the bilingual document but could not jump directly from the header to the desired language layer.

## Action

Only the selector:

`[ES · Castellano](#es--castellano) · [EN · English](#en--english)`

was added before the initial separator in:

- `manifiestos/78_neorrenacimiento_incontrolabilidad_intrinseca_sistema_humano_ES_EN.md`;
- `manifiestos/canonicos/LXXVIII_neorrenacimiento_incontrolabilidad_intrinseca_sistema_humano_ES_EN.md`.

No substantive content, genealogy, status, cross-references, Synthesis, Neoaxioms™, Issues or canon rules were changed.

**Commits:** `dcd2bb7918480379e7ddc75d2a9a5a5bc3b5dc32` and `b6e4175fb3a1a6c301d0e88fd262549cc202f4ae`.

## Tests and result

A post-read of both surfaces confirms that the selector appears before `# ES · Castellano` and points to the `#es--castellano` and `#en--english` anchors corresponding to the document's two actual language headings.

**LXXVIII target result:** `PASS`.

No global `LANGUAGE_SELECTOR_GATE = PASS` is declared: LXXIX, LXXX and LXXXI remain materially verified as lacking the selector in both live route and canonical mirror, leaving **at least 6 active surfaces pending** after this repair. No recoverable workflow run is visible for the latest commit either, so absence of CI is not interpreted as PASS.

## Residues

- Versioned global structural symmetry: **1 known failure**, Run 06.
- Language navigation: LXXIX–LXXXI remain pending in live route and canonical mirror.
- `7.3-CANDIDATE` remains `NOT_CANON`.
- PR #165 and #167 remain open and unmerged.

## Next step

Repair **LXXIX** by adding the same visible ES/EN selector to its live route and canonical mirror without changing substantive content, then verify both documents after the change.

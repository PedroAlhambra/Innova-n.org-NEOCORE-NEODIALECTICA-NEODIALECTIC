# MAXPROC público · Run 33 · reparación de simetría del caso Gritax™
# Public MAXPROC · Run 33 · Gritax™ case symmetry repair

**Fecha / Date:** 2026-08-25  
**Estado / Status:** ITERACIÓN VERIFICADA CON GATES ABIERTOS / VERIFIED ITERATION WITH OPEN GATES  
**Frontera / Frontier:** `NEOCore™ 7.3-CANDIDATE · NOT_CANON`  
**Cambio material / Material change:** `61b7a77ceb507fe8365ec7627183e6e65f214926`

[ES · Castellano](#es--resultado) · [EN · English](#en--result)

---

## ES · Resultado

### 1. Estado vivo previo

La auditoría global de simetría ES/EN vigente identificaba **2 fallos estructurales**. El primero, y único seleccionado para esta iteración, era:

`propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md`

El defecto era estructural, no conceptual: la red documental estaba situada sólo después de la sección EN, por lo que el auditor la contabilizaba dentro de la capa inglesa. El resultado era `ES=135`, `EN=209`, ratio `1.55` y un esqueleto de encabezados no simétrico.

### 2. Corrección exclusiva

Se preservó íntegramente el cuerpo conceptual, la genealogía `XLV → LXI → LXXXII → CMN-0.1 → C-NAX-20 → NEOCore 7.3-CANDIDATE → SAN #174`, los enlaces y el estado candidato. La única reparación material fue proyectar la red documental de forma simétrica dentro de ambas capas:

- `### Red documental` dentro de ES;
- `### Documentary network` dentro de EN.

No se modificó `PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`, no se tocó la extensión C-NAX-20 y no se promovió 7.3-CANDIDATE.

### 3. Verificación

La auditoría regenerada sobre el estado posterior confirma ahora **352 Markdown activos**, **286 documentos ES/EN divididos**, **1 único fallo estructural**, **0 fallos de marcadores** y **0 superficies pareadas pendientes**. El caso Gritax™ ya figura fuera del inventario de fallos; sólo permanece `PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`.

```text
GLOBAL_BILINGUAL_SYMMETRY
split_fail = 1
marker_fail = 0
paired_review = 0
yaml_review = 0
```

El gate independiente `LANGUAGE_NAVIGATION` permanece en **FAIL**: se auditan **370 superficies ES/EN explícitas** y hay **3 fallos**, correspondientes al caso Gritax™, la extensión C-NAX-20 y CMN-0.1, todos por ausencia de selector visible ES/EN. Este estado no se rebaja ni se transforma en PASS.

El postcheck documental vigente mantiene además `LINK_INTEGRITY` abierto con **2 enlaces internos rotos**, ambos preexistentes en `auditorias/publicas/2026-08-25_public_maxproc_run32_ES_EN.md`, donde `../issues/174` se interpreta como ruta local inexistente. No se han corregido en esta iteración para respetar la regla de una sola reparación material.

Durante la primera regeneración hubo una carrera de escritura entre Actions y los postchecks concurrentes. Una ejecución posterior consiguió persistir los informes frescos; la auditoría de simetría vigente ya refleja el descenso de 2 a 1 fallo.

### 4. Estado de cierre

```text
GRITAX_CONTENT_SYMMETRY = REPAIRED
GLOBAL_CONTENT_SYMMETRY = FAIL_1_REMAINING
LANGUAGE_NAVIGATION = FAIL_3
LINK_INTEGRITY = FAIL_2
7.3-CANDIDATE = NOT_CANON
GLOBAL_PASS = NO
```

### 5. Único siguiente paso

Corregir **exclusivamente** el primer fallo de integridad documental vigente: sustituir en la traza pública del run32 las dos apariciones bilingües de `../issues/174` por la URL pública real de la Issue #174, sin tocar ninguna otra superficie ni contenido conceptual.

---

## EN · Result

### 1. Prior living state

The current global ES/EN symmetry audit identified **2 structural failures**. The first, and only one selected for this iteration, was:

`propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md`

The defect was structural rather than conceptual: the documentary network was placed only after the EN section, so the auditor counted it inside the English layer. The result was `ES=135`, `EN=209`, ratio `1.55`, with a non-symmetric heading skeleton.

### 2. Exclusive correction

The conceptual body, genealogy `XLV → LXI → LXXXII → CMN-0.1 → C-NAX-20 → NEOCore 7.3-CANDIDATE → SAN #174`, links and candidate status were fully preserved. The only material repair was to project the documentary network symmetrically inside both language layers:

- `### Red documental` inside ES;
- `### Documentary network` inside EN.

`PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md` was not modified, the C-NAX-20 extension was not touched, and 7.3-CANDIDATE was not promoted.

### 3. Verification

The regenerated audit over the resulting state now confirms **352 active Markdown files**, **286 split ES/EN documents**, **1 sole structural failure**, **0 marker failures** and **0 paired surfaces pending**. The Gritax™ case has left the failure inventory; only `PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md` remains.

```text
GLOBAL_BILINGUAL_SYMMETRY
split_fail = 1
marker_fail = 0
paired_review = 0
yaml_review = 0
```

The independent `LANGUAGE_NAVIGATION` gate remains **FAIL**: **370 explicit ES/EN surfaces** are audited and there are **3 failures**, corresponding to the Gritax™ case, the C-NAX-20 extension and CMN-0.1, all due to a missing visible ES/EN selector. This state is neither lowered nor converted into PASS.

The current documentary postcheck also keeps `LINK_INTEGRITY` open with **2 broken internal links**, both pre-existing in `auditorias/publicas/2026-08-25_public_maxproc_run32_ES_EN.md`, where `../issues/174` is interpreted as a missing local path. They were not repaired in this iteration in order to respect the single-material-fix rule.

During the first regeneration there was a concurrent-write race between Actions and parallel postchecks. A later execution successfully persisted the fresh reports; the current symmetry audit now records the reduction from 2 failures to 1.

### 4. Closing state

```text
GRITAX_CONTENT_SYMMETRY = REPAIRED
GLOBAL_CONTENT_SYMMETRY = FAIL_1_REMAINING
LANGUAGE_NAVIGATION = FAIL_3
LINK_INTEGRITY = FAIL_2
7.3-CANDIDATE = NOT_CANON
GLOBAL_PASS = NO
```

### 5. Single next step

Fix **only** the first current documentary-integrity failure: replace the two bilingual occurrences of `../issues/174` in the public run32 trace with the real public URL for Issue #174, without touching any other surface or conceptual content.

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

La ejecución `audit-global-bilingual-symmetry` sobre el commit material devolvió:

```text
GLOBAL_BILINGUAL_SYMMETRY
split_fail = 1
marker_fail = 0
paired_review = 0
yaml_review = 0
```

Por tanto, el caso Gritax™ salió del inventario de fallos estructurales y el único fallo estructural restante pertenece a `PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`.

La misma ejecución confirmó que el gate independiente `LANGUAGE_NAVIGATION` permanece en **FAIL** con **3 superficies** sin selector ES/EN visible: el caso Gritax™, la extensión C-NAX-20 y CMN-0.1. Este estado no se rebaja ni se transforma en PASS.

El intento automático de persistir los informes regenerados sufrió una carrera de escritura con los postchecks relacionales/documentales sobre `main`; la evidencia del runner se conserva. Los postchecks posteriores sí completaron sin introducir roturas documentales atribuibles a esta reparación.

### 4. Estado de cierre

```text
GRITAX_CONTENT_SYMMETRY = REPAIRED
GLOBAL_CONTENT_SYMMETRY = FAIL_1_REMAINING
LANGUAGE_NAVIGATION = FAIL_3
7.3-CANDIDATE = NOT_CANON
GLOBAL_PASS = NO
```

### 5. Único siguiente paso

Corregir **exclusivamente** el primer fallo vigente de `LANGUAGE_NAVIGATION`: añadir al caso Gritax™ el selector visible y correcto `ES · Castellano / EN · English`, sin tocar todavía las otras dos superficies ni el cuerpo conceptual.

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

The `audit-global-bilingual-symmetry` execution over the material commit returned:

```text
GLOBAL_BILINGUAL_SYMMETRY
split_fail = 1
marker_fail = 0
paired_review = 0
yaml_review = 0
```

Therefore, the Gritax™ case left the structural-failure inventory and the sole remaining structural failure belongs to `PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`.

The same execution confirmed that the independent `LANGUAGE_NAVIGATION` gate remains **FAIL** with **3 surfaces** lacking a visible ES/EN selector: the Gritax™ case, the C-NAX-20 extension and CMN-0.1. This state is neither lowered nor converted into PASS.

The automatic attempt to persist the regenerated reports encountered a concurrent-write race with relational/documentary postchecks on `main`; the runner evidence remains preserved. Later postchecks completed without introducing documentary breakage attributable to this repair.

### 4. Closing state

```text
GRITAX_CONTENT_SYMMETRY = REPAIRED
GLOBAL_CONTENT_SYMMETRY = FAIL_1_REMAINING
LANGUAGE_NAVIGATION = FAIL_3
7.3-CANDIDATE = NOT_CANON
GLOBAL_PASS = NO
```

### 5. Single next step

Fix **only** the first current `LANGUAGE_NAVIGATION` failure: add the visible and correct `ES · Castellano / EN · English` selector to the Gritax™ case, without yet touching the other two surfaces or the conceptual body.

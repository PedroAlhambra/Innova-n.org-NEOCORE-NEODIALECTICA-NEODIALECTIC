# MAXPROC público · Run32 · Reparación de enlace de Síntesis LXXXII / Public MAXPROC · Run32 · Repairing LXXXII Synthesis link

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Fecha / Date:** 2026-08-25  
**Estado / Status:** `FALLO SELECCIONADO CORREGIDO · VERIFICACIÓN GLOBAL ABIERTA / SELECTED DEFECT FIXED · GLOBAL VERIFICATION OPEN`  
**Frontera / Boundary:** `7.3-CANDIDATE / NOT_CANON`

---

# ES · Castellano

## 1. Estado vivo revisado

Antes de modificar se revisaron el head público, la auditoría global de simetría ES/EN, la auditoría de navegación lingüística y el postcheck dinámico de README, índices y enlaces.

El corte previo mostraba:

- `CONTENT_SYMMETRY = PASS`: **346** Markdown activos de alcance bilingüe, **280** documentos ES/EN divididos, **0** fallos estructurales y **0** fallos de marcadores;
- `LANGUAGE_NAVIGATION = PASS`: **364** superficies ES/EN explícitas auditadas y **0** fallos;
- postcheck documental: **439** Markdown activos, **10.822** rutas internas, **1** enlace interno roto y **0** fallos canónicos críticos;
- frontera canónica conservada: `7.3-CANDIDATE / NOT_CANON`.

## 2. Primer fallo real prioritario

El primer defecto real y verificable era el enlace de cabecera de `manifiestos/82_ciencia_multidimensional_neodialectica_ES_EN.md`:

```text
[#174](../issues/174)
```

El postcheck lo interpretaba como una ruta interna inexistente. La Issue **#174** sí existe y corresponde a la Síntesis Abierta de Ciencia Multidimensional Neodialéctica™ y «Cáncer de la Síntesis»; el mismo manifiesto ya contenía más abajo el enlace absoluto correcto.

## 3. Corrección aplicada

Se sustituyó exclusivamente el enlace roto de cabecera por la URL GitHub real de la Síntesis Abierta #174:

```text
https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/174
```

**Commit material:** `c7941b54e632a794a7ca32f9d6b68c4eac591956`.

No se reescribió el cuerpo del manifiesto, no se alteró su genealogía, no se modificaron Neoaxiomas ni la Síntesis y no se promovió `7.3-CANDIDATE` a canon.

## 4. Gates y genealogía preservados

La corrección conserva:

- simetría ES/EN del manifiesto;
- selector lingüístico existente;
- genealogía XLV → LXI → 7.3-CANDIDATE → LXXXII;
- relación con C-NAX-20, CMN-0.1 y Caso 001;
- `7.3-CANDIDATE = NOT_CANON`;
- Issue #174 como Síntesis Abierta, no como validación automática.

## 5. Verificación posterior

La reparación seleccionada queda verificada:

- la Issue #174 existe y está abierta;
- la ruta relativa defectuosa ya no existe en LXXXII;
- el postcheck regenerado vuelve a **0 enlaces internos rotos**;
- mantiene **0 fallos canónicos críticos**;
- comprueba **10.827** rutas internas sobre **439** Markdown activos.

Durante la misma verificación, una sincronización automática posterior regeneró la auditoría global ES/EN y dejó visibles **2 fallos estructurales nuevos** en superficies CMN:

1. `propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md`;
2. `propuestas/sintesis-abierta/PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`.

No se corrigen en esta iteración porque la regla MAXPROC exige corregir exclusivamente el primer fallo real prioritario seleccionado. Tampoco se rebaja el gate: `CONTENT_SYMMETRY` deja de poder declararse PASS mientras esos defectos permanezcan.

**Resultado de esta iteración:** el defecto seleccionado queda `FIXED_AND_LINK_GATE_VERIFIED`; el estado global permanece abierto por regresiones bilingües posteriores detectadas, no ocultadas.

## 6. Único siguiente paso

Corregir exclusivamente el primer fallo estructural ES/EN vigente: `propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md`, restaurando simetría real sin comprimir ninguna de las dos capas y volver a ejecutar la auditoría global.

---

# EN · English

## 1. Living state reviewed

Before modifying anything, the public head, global ES/EN symmetry audit, language-navigation audit and dynamic README/index/link postcheck were reviewed.

The previous cut showed:

- `CONTENT_SYMMETRY = PASS`: **346** active Markdown files in bilingual scope, **280** split ES/EN documents, **0** structural failures and **0** marker failures;
- `LANGUAGE_NAVIGATION = PASS`: **364** explicit ES/EN surfaces audited and **0** failures;
- documentary postcheck: **439** active Markdown files, **10,822** internal paths, **1** broken internal link and **0** critical canonical failures;
- preserved canonical boundary: `7.3-CANDIDATE / NOT_CANON`.

## 2. First real priority defect

The first real and verifiable defect was the header link in `manifiestos/82_ciencia_multidimensional_neodialectica_ES_EN.md`:

```text
[#174](../issues/174)
```

The postcheck interpreted it as a nonexistent internal path. Issue **#174** does exist and is the Open Synthesis for Neodialectical Multidimensional Science™ and the “Cancer of Synthesis”; the same manifesto already contained the correct absolute link further down.

## 3. Applied correction

Only the broken header link was replaced with the real GitHub URL for Open Synthesis #174:

```text
https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/174
```

**Material commit:** `c7941b54e632a794a7ca32f9d6b68c4eac591956`.

The manifesto body was not rewritten, its genealogy was not altered, no Neoaxioms or Synthesis content were modified, and `7.3-CANDIDATE` was not promoted to canon.

## 4. Preserved gates and genealogy

The correction preserves:

- manifesto ES/EN symmetry;
- the existing language selector;
- genealogy XLV → LXI → 7.3-CANDIDATE → LXXXII;
- relation to C-NAX-20, CMN-0.1 and Case 001;
- `7.3-CANDIDATE = NOT_CANON`;
- Issue #174 as Open Synthesis, not automatic validation.

## 5. Post-fix verification

The selected repair is verified:

- Issue #174 exists and is open;
- the defective relative path no longer exists in LXXXII;
- the regenerated postcheck returns to **0 broken internal links**;
- it retains **0 critical canonical failures**;
- it checks **10,827** internal paths across **439** active Markdown files.

During the same verification window, a later automatic synchronisation regenerated the global ES/EN audit and exposed **2 new structural failures** in CMN surfaces:

1. `propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md`;
2. `propuestas/sintesis-abierta/PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md`.

They are not fixed in this iteration because the MAXPROC rule requires correcting exclusively the first selected real priority defect. The gate is not lowered either: `CONTENT_SYMMETRY` can no longer be declared PASS while those defects remain.

**Iteration result:** the selected defect is `FIXED_AND_LINK_GATE_VERIFIED`; global state remains open because later bilingual regressions were detected and explicitly preserved rather than hidden.

## 6. Single next step

Fix exclusively the first current ES/EN structural failure: `propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md`, restoring real symmetry without compressing either language layer, then rerun the global audit.

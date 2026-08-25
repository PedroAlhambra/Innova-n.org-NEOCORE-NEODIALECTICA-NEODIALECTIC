# MAXPROC público · Run30 · Retirada de one-shot canónico obsoleto / Public MAXPROC · Run30 · Retiring stale canonical write one-shot

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

**Fecha / Date:** 2026-08-25  
**Estado / Status:** `CORRECCIÓN MATERIAL VERIFICADA / MATERIAL FIX VERIFIED`  
**Frontera / Boundary:** `7.3-CANDIDATE / NOT_CANON`

---

# ES · Castellano

## 1. Estado vivo revisado

Antes de modificar se revisaron los commits y auditorías vigentes. Los últimos gates públicos mantenían simetría ES/EN, navegación lingüística e integridad documental en estado limpio, y la frontera `7.3-CANDIDATE` seguía explícitamente no canónica.

## 2. Primer fallo real prioritario

Se localizó `.github/workflows/oneshot-register-lxvii-neotitanes.yml`, un workflow histórico con `contents: write` que seguía presente en `main` pese a estar diseñado como one-shot.

Ese workflow podía escribir directamente en:

- `manifiestos/README.md`;
- `manifiestos/CANONICAL_FILENAMES.json`;
- `propuestas/sintesis-abierta/README.md`;
- `propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md`;
- y ejecutar sincronizadores de navegación, canon y referencias.

Su lógica era anterior al gate explícito de estado canónico introducido en Run29 y, por tanto, constituía una ruta residual de escritura capaz de alterar superficies canónicas sin atravesar esa protección.

## 3. Corrección aplicada

Se retiró exclusivamente el workflow obsoleto:

` .github/workflows/oneshot-register-lxvii-neotitanes.yml `

Commit material:

`b7c648d9639aee53f1370c1a76719d843c32b4a7`

No se modificaron manifiestos, índices, genealogía, enlaces sustantivos, WEB4 ni contenido canónico.

## 4. Gates y restricciones

La corrección no rebaja ningún gate. Se conserva expresamente:

- `7.3-CANDIDATE = NOT_CANON`;
- sin promoción pública;
- sin reescritura de genealogía;
- sin cambio de contenido ES/EN;
- sin modificación de la frontera canónica.

## 5. Verificación

La verificación de esta iteración consiste en comprobar que la ruta residual de escritura ya no existe en `main` y que el cambio material se limita a retirar el one-shot histórico. La creación de esta traza Markdown activa además los gates públicos normales de simetría, navegación y enlaces; sus resultados posteriores deben interpretarse como evidencia independiente, no anticiparse como PASS antes de su ejecución.

## 6. Único siguiente paso

Auditar el siguiente workflow `oneshot-*` que todavía permanezca en `main` y pueda escribir superficies canónicas o de Síntesis; corregir únicamente el primero que resulte realmente ejecutable y no esté protegido por el gate vigente de `7.3-CANDIDATE`.

---

# EN · English

## 1. Living state reviewed

Before making changes, the current commits and active audits were reviewed. The latest public gates kept ES/EN symmetry, language navigation and documentary integrity clean, while the `7.3-CANDIDATE` boundary remained explicitly non-canonical.

## 2. First real priority defect

`.github/workflows/oneshot-register-lxvii-neotitanes.yml` was found still present in `main`: a historical workflow with `contents: write` even though it was designed as a one-shot.

That workflow could write directly to:

- `manifiestos/README.md`;
- `manifiestos/CANONICAL_FILENAMES.json`;
- `propuestas/sintesis-abierta/README.md`;
- `propuestas/sintesis-abierta/INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md`;
- and run navigation, canonical and cross-reference synchronisers.

Its logic predated the explicit canonical-state gate introduced in Run29 and therefore formed a residual write path capable of altering canonical surfaces without passing through that protection.

## 3. Applied correction

Only the obsolete workflow was removed:

` .github/workflows/oneshot-register-lxvii-neotitanes.yml `

Material commit:

`b7c648d9639aee53f1370c1a76719d843c32b4a7`

No manifestos, indexes, genealogy, substantive links, WEB4 or canonical content were modified.

## 4. Gates and restrictions

The correction lowers no gate. It explicitly preserves:

- `7.3-CANDIDATE = NOT_CANON`;
- no public promotion;
- no genealogy rewrite;
- no ES/EN content change;
- no canonical-frontier modification.

## 5. Verification

Verification for this iteration consists of confirming that the residual write path no longer exists in `main` and that the material change is limited to retiring the historical one-shot. Creating this Markdown trace also triggers the normal public symmetry, navigation and link gates; their later results must be treated as independent evidence rather than anticipated as PASS before execution.

## 6. Single next step

Audit the next `oneshot-*` workflow still present in `main` that can write canonical or Open Synthesis surfaces; correct only the first one that is actually executable and not protected by the current `7.3-CANDIDATE` gate.

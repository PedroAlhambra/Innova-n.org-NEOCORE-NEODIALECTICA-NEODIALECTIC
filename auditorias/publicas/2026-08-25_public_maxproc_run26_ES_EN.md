# MAXPROC público Run26 · diagnóstico de navegación lingüística del índice / Public MAXPROC Run26 · manifesto-index language-navigation diagnosis

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

# ES · Castellano

**Fecha:** 2026-08-25

## Estado observado

Antes de esta iteración, las auditorías vigentes demostraban `CONTENT_SYMMETRY = PASS`, `LANGUAGE_NAVIGATION = PASS`, `LINK_INTEGRITY = PASS` y `RELATIONAL_NAVIGATION = PASS_DOCUMENTARY`; `7.3-CANDIDATE` seguía abierta y no canónica.

## Problema elegido

`manifiestos/README.md` contiene un control visual presentado como selector `ES · Castellano / EN · English`, pero ambos enlaces apuntan al mismo destino: `#colección-canónica--canonical-collection`. La página es un índice bilingüe intercalado y no dispone de capas separadas ES/EN. Por tanto, el control no rompe rutas, pero representa falsamente una navegación lingüística que no existe.

## Acción

Se intentó aplicar una sustitución mínima y verificable mediante un workflow temporal. GitHub rechazó el workflow antes de ejecutar ningún job; no se modificó `manifiestos/README.md`, ningún contenido del corpus ni ningún estado canónico. El workflow temporal fue retirado y no queda residuo operativo activo.

## Pruebas

Se releyó `manifiestos/README.md` después del intento y conserva exactamente el contenido anterior. No se declara PASS del defecto porque la corrección no llegó a materializarse.

## Resultado

**NO_CHANGE** sobre el corpus material. El defecto queda demostrado y localizado sin rebajar gates ni inventar una reparación inexistente.

## PASO_SIGUIENTE

Corregir exclusivamente la cabecera de `manifiestos/README.md` con un mecanismo de escritura de contenido completo seguro, sustituyendo el pseudo-selector ES/EN por navegación bilingüe descriptiva real, y después volver a ejecutar los gates públicos.

# EN · English

**Date:** 2026-08-25

## Observed state

Before this iteration, current audits demonstrated `CONTENT_SYMMETRY = PASS`, `LANGUAGE_NAVIGATION = PASS`, `LINK_INTEGRITY = PASS` and `RELATIONAL_NAVIGATION = PASS_DOCUMENTARY`; `7.3-CANDIDATE` remained open and non-canonical.

## Chosen problem

`manifiestos/README.md` contains a visual control presented as an `ES · Castellano / EN · English` selector, but both links target the same destination: `#colección-canónica--canonical-collection`. The page is an interleaved bilingual index and does not expose separate ES/EN layers. The control therefore does not break routes, but it falsely represents language navigation that does not exist.

## Action

A minimal verifiable replacement was attempted through a temporary workflow. GitHub rejected the workflow before any job executed; `manifiestos/README.md`, corpus content and canonical state were not modified. The temporary workflow was removed and no active operational residue remains.

## Tests

`manifiestos/README.md` was reread after the attempt and retains its exact previous content. No PASS is claimed for the defect because the correction did not materialise.

## Result

**NO_CHANGE** on the material corpus. The defect is demonstrated and precisely located without lowering gates or inventing a nonexistent repair.

## NEXT_STEP

Correct only the header of `manifiestos/README.md` using a safe full-content write mechanism, replacing the ES/EN pseudo-selector with truthful descriptive bilingual navigation, then rerun the public gates.

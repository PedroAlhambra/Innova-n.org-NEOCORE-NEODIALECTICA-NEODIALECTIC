# Reconciliación global · simetría ES/EN, navegación y mapas vivos
# Global reconciliation · ES/EN symmetry, navigation and living maps

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

## ES · Castellano

**Fecha:** 2026-08-28  
**Naturaleza:** postcheck material y disparador de verificación fresca.  
**Regla:** este documento no declara PASS por sí mismo; el resultado operativo se toma de las auditorías y GitHub Actions ejecutadas sobre el estado posterior a estas reparaciones.

### Reparaciones incluidas

1. El auditor global ES/EN deja de contabilizar como párrafo inglés adicional el pie bilingüe compartido `Síntesis Abierta / Open Synthesis`.
2. Los fallos detectados por el auditor global pasan a bloquear realmente el job: un informe con `split_fail`, `marker_fail`, `paired_review` o `yaml_review` ya no puede producir un PASS operativo por ausencia de `exit != 0`.
3. El mapa vivo `manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md` se reconcilia de I–LXXXI a I–LXXXIV e incorpora LXXXII, LXXXIII y LXXXIV con rutas clicables hacia manifiestos, Síntesis Abierta y relaciones aplicadas.
4. El portal de Auditorías Públicas se reconcilia con la frontera LXXXIV y añade el seguimiento KDP del caso `51425302` al expediente vivo de IDEA.
5. Los workflows temporales usados exclusivamente para aplicar estas reparaciones se autoeliminan; no forman parte de la arquitectura operativa permanente.

### Criterio de cierre

El estado sólo puede considerarse limpio cuando exista evidencia fresca posterior a estas reparaciones para simetría ES/EN, selectores de idioma, navegación relacional, enlaces/README, integridad neoaxiomática y postcheck relacional. La evidencia histórica anterior conserva valor genealógico, pero no sustituye la verificación del head corregido.

---

## EN · English

**Date:** 2026-08-28  
**Nature:** material postcheck and fresh-verification trigger.  
**Rule:** this document does not declare PASS by itself; the operational result is taken from audits and GitHub Actions executed against the repository state after these repairs.

### Repairs included

1. The global ES/EN auditor no longer counts the shared bilingual `Síntesis Abierta / Open Synthesis` footer as an additional English paragraph.
2. Failures detected by the global auditor now genuinely block the job: a report containing `split_fail`, `marker_fail`, `paired_review` or `yaml_review` can no longer yield an operational PASS merely because a non-zero exit was missing.
3. The living map `manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md` is reconciled from I–LXXXI to I–LXXXIV and now includes LXXXII, LXXXIII and LXXXIV with clickable routes to manifestos, Open Synthesis and applied relations.
4. The Public Audits portal is reconciled with the LXXXIV frontier and adds KDP case `51425302` follow-up to IDEA's living case file.
5. Temporary workflows used solely to apply these repairs delete themselves and are not part of the permanent operational architecture.

### Closure criterion

The state may be considered clean only when fresh evidence after these repairs exists for ES/EN symmetry, language selectors, relational navigation, links/README integrity, neoaxiomatic integrity and the relational postcheck. Earlier historical evidence retains genealogical value but does not replace verification of the corrected head.

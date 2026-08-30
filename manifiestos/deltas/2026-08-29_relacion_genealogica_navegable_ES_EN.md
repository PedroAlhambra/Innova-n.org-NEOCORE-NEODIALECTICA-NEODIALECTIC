# Delta · Relación Genealógica Navegable™
# Delta · Navigable Genealogical Relation™

**Fecha / Date:** 2026-08-29  
**Estado / Status:** regla pública activa de integridad relacional / active public relational-integrity rule  
**Ámbito / Scope:** todos los manifiestos finitos vigentes + Manifiesto ∞ / all current finite manifestos + Manifesto ∞

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

## ES · Castellano

La cabecera **`Relación genealógica / Genealogical relation`** no es prosa decorativa. Declara relaciones internas del corpus y, por tanto, constituye una **superficie de navegación**.

Desde esta fijación:

1. todo concepto, manifiesto, Neoaxioma™, Síntesis Abierta™ u otra pieza canónica mencionada en una relación genealógica debe aparecer como hipervínculo Markdown real a su destino canónico;
2. no es suficiente que el mismo destino aparezca enlazado más abajo en `Referencias cruzadas canónicas / Canonical cross-references`: la relación original debe ser navegable en el lugar donde se declara;
3. el destino debe resolverse mediante el corpus real y, cuando aplique, `CANONICAL_FILENAMES.json`; nunca se inventará una ruta por semejanza nominal;
4. si no existe una correspondencia canónica única verificable, el caso se registra como `UNRESOLVED_GENEALOGICAL_TARGET` hasta su resolución, sin fabricar genealogía ni enlace;
5. una relación canónica presentada en texto plano constituye `GENEALOGICAL_NAVIGATION_FAILURE` y bloquea cualquier PASS global de navegabilidad;
6. los auditores, generadores, plantillas y sincronizadores deben preservar este invariante para impedir regresión posterior.

El manifiesto XLVII ha servido como caso de detección: su cabecera declaraba múltiples relaciones genealógicas canónicas en texto plano aun existiendo una norma general de navegabilidad. El fallo demuestra que la regla previa era conceptualmente correcta pero su control automático era incompleto.

```text
RELACION_DECLARADA
→ DESTINO_CANONICO_VERIFICADO
→ HIPERVINCULO_REAL
→ RETORNO_A_FUENTE
→ TRAZABILIDAD

RELACION_DECLARADA + TEXTO_PLANO_CANONICO
→ GENEALOGICAL_NAVIGATION_FAILURE
```

La reparación debe abarcar el corpus completo y la causa sistémica, no limitarse al archivo donde se detectó el fallo.

## EN · English

The **`Relación genealógica / Genealogical relation`** header is not decorative prose. It declares internal corpus relations and is therefore a **navigation surface**.

From this record onward:

1. every concept, manifesto, Neoaxiom™, Open Synthesis™ or other canonical item named in a genealogical relation must be a real Markdown hyperlink to its canonical destination;
2. it is not sufficient for the same destination to be linked later in `Canonical cross-references`: the original relation must be navigable where it is declared;
3. destinations must be resolved from the real corpus and, where applicable, `CANONICAL_FILENAMES.json`; paths must never be invented from naming similarity;
4. where no unique verifiable canonical target exists, record `UNRESOLVED_GENEALOGICAL_TARGET` until resolved rather than fabricating genealogy or a link;
5. a canonical relation rendered as plain text is a `GENEALOGICAL_NAVIGATION_FAILURE` and blocks any global navigability PASS;
6. auditors, generators, templates and synchronisers must preserve this invariant to prevent regression.

Manifesto XLVII is the detection case: its header declared several canonical genealogical relations as plain text even though a general navigability rule already existed. The failure shows that the prior principle was conceptually correct but its automated enforcement was incomplete.

```text
DECLARED_RELATION
→ VERIFIED_CANONICAL_TARGET
→ REAL_HYPERLINK
→ SOURCE_RETURN
→ TRACEABILITY

DECLARED_RELATION + CANONICAL_PLAIN_TEXT
→ GENEALOGICAL_NAVIGATION_FAILURE
```

Repair must cover the whole corpus and the systemic cause, not only the file where the failure was detected.

## Relaciones / Relations

- [Manifiestos / Manifestos](../README.md)
- [Memoria, Genealogía y Trazabilidad / Memory, Genealogy and Traceability](../06_memoria_genealogia_trazabilidad_ES_EN.md)
- [XLVII · Sombra, sino, vínculo y doble cara / Shadow, fate, bond and two faces](../47_odio_neo0_sino_goat_sombra_vinculo_doble_cara_ES_EN.md)
- [Auditor de relaciones clicables / Clickable-relations auditor](../../.github/scripts/audit_manifesto_clickable_relations.py)

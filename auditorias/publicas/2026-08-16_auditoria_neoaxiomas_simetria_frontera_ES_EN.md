# Auditoría de integridad neoaxiomática ES/EN y frontera C-NAX
# Neoaxiomatic ES/EN integrity and C-NAX frontier audit

**Fecha / Date:** 2026-08-16  
**Estado / Status:** **OK**  
**Frontera dinámica / Dynamic frontier:** **C-NAX-15–C-NAX-26**  
**Objeto / Scope:** NAX-01–NAX-14, registro C-NAX, formulaciones ES/EN, documentos dedicados e índice vivo de Síntesis. / NAX-01–NAX-14, C-NAX registry, ES/EN formulations, dedicated documents and the live Synthesis index.

## Resultado / Result

- NAX canónicos ES / canonical ES NAX: **14** · `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`.
- NAX canónicos EN / canonical EN NAX: **14** · `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`.
- C-NAX registrados / registered C-NAX: **12** · `[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]`.
- C-NAX con bloque desarrollado / C-NAX with developed block: **12** · `[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]`.
- Documentos C-NAX dedicados detectados / dedicated C-NAX documents detected: `[23, 24, 25, 26]`.

## Regla endurecida / Hardened rule

- **Una fila C-NAX sin formulación desarrollada ES/EN es fallo de integridad. / A C-NAX row without a developed ES/EN formulation is an integrity failure.**
- **Un documento C-NAX dedicado ausente del registro central es fallo de frontera. / A dedicated C-NAX document missing from the central registry is an integrity failure.**
- **La frontera C-NAX se deriva dinámicamente del registro; ningún máximo queda codificado a mano. / The C-NAX frontier is derived dynamically from the registry; no maximum is hard-coded.**
- **NAX/C-NAX quedan fuera de cualquier excepción genérica de encabezados: esta auditoría los comprueba por identificador. / NAX/C-NAX are outside any generic heading exception: this audit checks them by identifier.**

## Incidencias / Findings

- Ninguna / None.

## Genealogía de la reparación / Repair genealogy

- La auditoría global anterior podía omitir el bloque C-NAX porque se encontraba antes del split principal `# ES / # EN` y porque el chequeo genérico toleraba encabezados `NAX-`/`C-NAX-`. / The previous global audit could miss the C-NAX block because it sat before the main `# ES / # EN` split and because the generic checker tolerated `NAX-`/`C-NAX-` headings.
- C-NAX-15–18 quedaron desarrollados y reconciliados conservando su genealogía. / C-NAX-15–18 were developed and reconciled while preserving their genealogy.
- C-NAX-23 y C-NAX-24 se incorporaron mediante documentos dedicados y registro central. / C-NAX-23 and C-NAX-24 were incorporated through dedicated documents and the central registry.
- C-NAX-25 y C-NAX-26 amplían la frontera mediante documentos bilingües dedicados y Síntesis #155/#156; la auditoría deja de fijar un máximo manual para que futuras ampliaciones no queden silenciosamente fuera. / C-NAX-25 and C-NAX-26 extend the frontier through dedicated bilingual documents and Syntheses #155/#156; the audit no longer hard-codes a maximum so future extensions cannot silently fall outside it.

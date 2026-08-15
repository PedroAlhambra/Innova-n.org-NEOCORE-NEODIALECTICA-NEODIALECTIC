# Auditoría de integridad neoaxiomática ES/EN y frontera C-NAX
# Neoaxiomatic ES/EN integrity and C-NAX frontier audit

**Fecha / Date:** 2026-08-16  
**Estado / Status:** **OK**  
**Objeto / Scope:** NAX-01–NAX-14, registro C-NAX, formulaciones ES/EN, documentos dedicados e índice vivo de Síntesis. / NAX-01–NAX-14, C-NAX registry, ES/EN formulations, dedicated documents and the live Synthesis index.

## Resultado / Result

- NAX canónicos ES / canonical ES NAX: **14** · `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`.
- NAX canónicos EN / canonical EN NAX: **14** · `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`.
- C-NAX registrados / registered C-NAX: **10** · `[15, 16, 17, 18, 19, 20, 21, 22, 23, 24]`.
- C-NAX con bloque desarrollado / C-NAX with developed block: **10** · `[15, 16, 17, 18, 19, 20, 21, 22, 23, 24]`.
- Documentos C-NAX dedicados detectados / dedicated C-NAX documents detected: `[23, 24]`.

## Regla endurecida / Hardened rule

- **Una fila C-NAX sin formulación desarrollada ES/EN es fallo de integridad. / A C-NAX row without a developed ES/EN formulation is an integrity failure.**
- **Un documento C-NAX dedicado ausente del registro central es fallo de frontera. / A dedicated C-NAX document missing from the central registry is a frontier failure.**
- **NAX/C-NAX quedan fuera de cualquier excepción genérica de encabezados: esta auditoría los comprueba por identificador. / NAX/C-NAX are outside any generic heading exception: this audit checks them by identifier.**

## Incidencias / Findings

- Ninguna / None.

## Genealogía de la reparación / Repair genealogy

- La auditoría global anterior podía omitir el bloque C-NAX porque se encontraba antes del split principal `# ES / # EN` y porque el chequeo genérico toleraba encabezados `NAX-`/`C-NAX-`. / The previous global audit could miss the C-NAX block because it sat before the main `# ES / # EN` split and because the generic checker tolerated `NAX-`/`C-NAX-` headings.
- C-NAX-15 y C-NAX-16 recuperan formulaciones ya explícitas en sus fuentes públicas. / C-NAX-15 and C-NAX-16 recover formulations already explicit in their public sources.
- C-NAX-17 y C-NAX-18 reciben formulación autónoma consolidada fielmente desde los principios publicados en LXVII y LXVI+LXVII, conservando la genealogía. / C-NAX-17 and C-NAX-18 receive standalone formulations faithfully consolidated from the principles published in LXVII and LXVI+LXVII, preserving genealogy.
- C-NAX-23 y C-NAX-24 se incorporan al registro central sin cambiar su condición de candidatos. / C-NAX-23 and C-NAX-24 are incorporated into the central registry without changing their candidate status.

# Auditoría global de selectores de idioma ES/EN
# Global ES/EN language-selector audit

**Generada / Generated:** 2026-08-28 11:33 UTC  
**Páginas ES/EN explícitas auditadas / Explicit ES/EN split pages audited:** **379**  
**Fallos / Failures:** **5**  
**LANGUAGE_SELECTOR_GATE:** **FAIL**

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Regla

Toda superficie Markdown pública y activa que exponga capas explícitas `ES` y `EN` debe incluir, antes del cuerpo español, un selector visible que permita saltar directamente a ambas capas. Los destinos deben coincidir con los anchors reales derivados de los encabezados.

`CONTENT_SYMMETRY_PASS ≠ LANGUAGE_NAVIGATION_PASS`. Un selector ausente o un anchor incorrecto bloquea el PASS global.

## Resultado

- Páginas auditadas: **379**.
- Fallos: **5**.
- Estado: **FAIL**.

## Detalle de fallos

- `auditorias/publicas/2026-08-26_addendum_kdp_vinculacion_cruzada_es_en_formatos_51071689_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/2026-08-27_C_NAX_27_SOBERANIA_DIFERENCIADA_SISTEMA_SINTESIS_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/INTERACCION_NEGOCIACION_TECNOLOGICA_DEPENDENCIA_REVERSIBILIDAD_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector

---

# EN · English

## Rule

Every active public Markdown surface exposing explicit `ES` and `EN` layers must include, before the Spanish body, a visible selector linking directly to both language layers. Link targets must match the real anchors derived from those headings.

`CONTENT_SYMMETRY_PASS ≠ LANGUAGE_NAVIGATION_PASS`. A missing selector or incorrect anchor blocks the global PASS.

## Result

- Pages audited: **379**.
- Failures: **5**.
- Status: **FAIL**.

## Failure detail

- `auditorias/publicas/2026-08-26_addendum_kdp_vinculacion_cruzada_es_en_formatos_51071689_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/2026-08-27_C_NAX_27_SOBERANIA_DIFERENCIADA_SISTEMA_SINTESIS_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/INTERACCION_NEGOCIACION_TECNOLOGICA_DEPENDENCIA_REVERSIBILIDAD_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector

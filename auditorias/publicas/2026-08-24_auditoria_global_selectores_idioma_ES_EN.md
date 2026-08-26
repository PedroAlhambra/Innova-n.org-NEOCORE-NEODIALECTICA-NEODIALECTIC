# Auditoría global de selectores de idioma ES/EN
# Global ES/EN language-selector audit

**Generada / Generated:** 2026-08-26 16:57 UTC  
**Páginas ES/EN explícitas auditadas / Explicit ES/EN split pages audited:** **374**  
**Fallos / Failures:** **4**  
**LANGUAGE_SELECTOR_GATE:** **FAIL**

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Regla

Toda superficie Markdown pública y activa que exponga capas explícitas `ES` y `EN` debe incluir, antes del cuerpo español, un selector visible que permita saltar directamente a ambas capas. Los destinos deben coincidir con los anchors reales derivados de los encabezados.

`CONTENT_SYMMETRY_PASS ≠ LANGUAGE_NAVIGATION_PASS`. Un selector ausente o un anchor incorrecto bloquea el PASS global.

## Resultado

- Páginas auditadas: **374**.
- Fallos: **4**.
- Estado: **FAIL**.

## Detalle de fallos

- `auditorias/publicas/2026-08-26_addendum_kdp_vinculacion_cruzada_es_en_formatos_51071689_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/2026-08-25_EXTENSION_C_NAX_20_UNIDAD_DIFERENCIADA_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector

---

# EN · English

## Rule

Every active public Markdown surface exposing explicit `ES` and `EN` layers must include, before the Spanish body, a visible selector linking directly to both language layers. Link targets must match the real anchors derived from those headings.

`CONTENT_SYMMETRY_PASS ≠ LANGUAGE_NAVIGATION_PASS`. A missing selector or incorrect anchor blocks the global PASS.

## Result

- Pages audited: **374**.
- Failures: **4**.
- Status: **FAIL**.

## Failure detail

- `auditorias/publicas/2026-08-26_addendum_kdp_vinculacion_cruzada_es_en_formatos_51071689_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/2026-08-25_CIENCIA_MULTIDIMENSIONAL_CANCER_SINTESIS_GRITAX_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/2026-08-25_EXTENSION_C_NAX_20_UNIDAD_DIFERENCIADA_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector
- `propuestas/sintesis-abierta/PROTOCOLO_CMN_0_1_CIENCIA_MULTIDIMENSIONAL_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector

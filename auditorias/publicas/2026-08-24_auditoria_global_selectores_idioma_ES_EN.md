# Auditoría global de selectores de idioma ES/EN
# Global ES/EN language-selector audit

**Generada / Generated:** 2026-08-31 16:41 UTC
**Páginas ES/EN explícitas auditadas / Explicit ES/EN split pages audited:** **434**
**Fallos / Failures:** **1**
**LANGUAGE_SELECTOR_GATE:** **FAIL**

[ES · Castellano](#es--castellano) · [EN · English](#en--english)

---

# ES · Castellano

## Regla

Toda superficie Markdown pública y activa que exponga capas explícitas `ES` y `EN` debe incluir, antes del cuerpo español, un selector visible que permita saltar directamente a ambas capas. Los destinos deben coincidir con los anchors reales derivados de los encabezados.

`CONTENT_SYMMETRY_PASS ≠ LANGUAGE_NAVIGATION_PASS`. Un selector ausente o un anchor incorrecto bloquea el PASS global.

## Resultado

- Páginas auditadas: **434**.
- Fallos: **1**.
- Estado: **FAIL**.

## Detalle de fallos

- `actualizaciones/2026-08-31_NEO0_COMPOSITOR_ASCENSO_CAPA_README_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector

---

# EN · English

## Rule

Every active public Markdown surface exposing explicit `ES` and `EN` layers must include, before the Spanish body, a visible selector linking directly to both language layers. Link targets must match the real anchors derived from those headings.

`CONTENT_SYMMETRY_PASS ≠ LANGUAGE_NAVIGATION_PASS`. A missing selector or incorrect anchor blocks the global PASS.

## Result

- Pages audited: **434**.
- Failures: **1**.
- Status: **FAIL**.

## Failure detail

- `actualizaciones/2026-08-31_NEO0_COMPOSITOR_ASCENSO_CAPA_README_ES_EN.md` · `LANGUAGE_NAVIGATION_FAILURE` · ES selector, EN selector

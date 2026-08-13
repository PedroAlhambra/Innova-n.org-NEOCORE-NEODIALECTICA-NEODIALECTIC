# MÉDICI™ · Motor de cálculo de plataformas v0.1
# MÉDICI™ · Platform Calculation Engine v0.1

**Fecha / Date:** 2026-08-13  
**Estado / Status:** implementación operativa inicial off-chain · abierta a Síntesis / initial operational off-chain implementation · open to Synthesis  
**Origen humano / Human origin:** Pedro Martínez Alhambra · Neo0™  
**Relaciones / Relations:** [Regla de créditos y compensación](./MEDICI_CREDITOS_PLATAFORMAS_COMPENSACION_ES_EN.md) · NeoCronos™ · Economía del Aporte™ · NeoSinergia™ · WEB4™

---

## ES · Castellano

### 1. Activación

La regla conceptual de reconocimiento de infraestructura pasa a tener **motor de cálculo reproducible**.

La implementación inicial vive en el repositorio interno de Innova_N y produce un libro mayor off-chain versionado. El repositorio público conserva la metodología, la genealogía y la proyección que puede auditarse sin exponer información privada de contratos o cuentas.

```text
SERVICIO + PERIODO + EVIDENCIA
→ VALORACIÓN
→ FRACCIÓN NO COMPENSADA
→ MOTOR MÉDICI™
→ SALDO CANDIDATO
→ REVISIÓN / SAN™
→ RECONOCIMIENTO OFF-CHAIN
```

### 2. Regla central

```text
CRÉDITO
→ SIEMPRE

SERVICIO GRATUITO / NO COMPENSADO PARA INNOVA_N
→ ELEGIBLE PARA MÉDICI™

SERVICIO PARCIALMENTE COMPENSADO
→ MÉDICI™ SOBRE LA FRACCIÓN NO COMPENSADA

SERVICIO PAGADO / TOTALMENTE COMPENSADO
→ CRÉDITO + TRAZA
→ 0 MÉDICI™ DIRECTO POR ESA FRACCIÓN
```

La unidad de evaluación es **servicio + periodo**, no una empresa completa.

### 3. Fórmula v0.1

```text
Q
= media(calidad, utilidad, continuidad, trazabilidad)

MÉDICI_CANDIDATO
= VALOR_VALIDADO
× FRACCIÓN_NO_COMPENSADA
× Q
× CONFIANZA
```

Con:

- `VALOR_VALIDADO ≥ 0` y respaldado por evidencia;
- `FRACCIÓN_NO_COMPENSADA ∈ [0,1]`;
- `calidad, utilidad, continuidad, trazabilidad, confianza ∈ [0,1]`.

La fórmula cumple dos condiciones deliberadas:

1. un servicio gratuito pero inútil no genera valor relevante;
2. un servicio extraordinariamente valioso pero íntegramente pagado conserva crédito y aporte causal, pero genera `0` MÉDICI™ directo por esa parte ya compensada.

### 4. Estados

```text
PENDIENTE_EVIDENCIA
→ faltan datos: no se inventa un número

CALCULADO_PENDIENTE_APROBACIÓN
→ cálculo reproducible, todavía no reconocido

RECONOCIDO_OFFCHAIN
→ saldo aprobado en el libro mayor versionado

ACREDITADO_SIN_MÉDICI_DIRECTO_POR_PAGO
→ valor reconocido, parte íntegramente compensada

SUPERADO / RECALCULADO
→ nuevo estado conserva genealogía del anterior
```

### 5. NeoCronos™ y recálculo

El saldo no es una etiqueta eterna.

Si cambia el plan, el contrato, la función utilizada, la calidad, la continuidad, el grado de gratuidad, la evidencia o el impacto, NeoCronos™ debe permitir reconstruir el antes y el después y el motor debe recalcular.

```text
ESTADO(t0)
→ DELTA
→ RECÁLCULO
→ ESTADO(t1)

ESTADO(t1)
NO BORRA
ESTADO(t0)
```

### 6. Off-chain primero

La fase v0.1 reconoce unidades en un **ledger Git off-chain**. No se afirma que exista todavía una emisión blockchain, mercado, convertibilidad, equity, derecho financiero, voto soberano o participación jurídica.

```text
MÉDICI™ OFF-CHAIN
= CONTABILIDAD TRAZABLE DE RECONOCIMIENTO

MÉDICI™ ON-CHAIN / TRANSFERIBLE
= CAPA FUTURA DISTINTA
```

La transición a una capa transferible requerirá reglas técnicas, jurídicas y de gobernanza explícitas.

### 7. Implementación interna

La implementación v0.1 queda estructurada mediante:

```text
infrastructure-registry.json
→ servicios, periodos, compensación, evidencia y variables

medici-platform-engine.mjs
→ cálculo determinista y validación

medici-platform-ledger.generated.json
→ proyección del saldo off-chain
```

La parte privada puede conservar datos sensibles. WEB4™ sólo debe proyectar campos públicos y verificables.

### 8. Regla de no invención

La creación del motor **no autoriza a rellenar porcentajes o tokens por intuición**.

Un registro incompleto permanece pendiente.

> **La ausencia de datos produce `pendiente`, no una cifra inventada.**

### 9. Consecuencia

Con esta capa, el reconocimiento de plataformas deja de ser una lista decorativa de agradecimientos y pasa a poder convertirse en una contabilidad trazable de infraestructura:

```text
QUIÉN SOPORTÓ
+ QUÉ FUNCIÓN
+ DURANTE QUÉ PERIODO
+ CON QUÉ COMPENSACIÓN
+ CON QUÉ VALOR VALIDADO
→ CRÉDITO
→ MÉDICI™ SI CORRESPONDE
→ GENEALOGÍA
```

---

## EN · English

### 1. Activation

The conceptual infrastructure-recognition rule now has a **reproducible calculation engine**.

The initial implementation lives in Innova_N's internal repository and produces a versioned off-chain ledger. The public repository preserves the methodology, genealogy and auditable projection without exposing private contracts or account data.

```text
SERVICE + PERIOD + EVIDENCE
→ VALUATION
→ UNCOMPENSATED FRACTION
→ MÉDICI™ ENGINE
→ CANDIDATE BALANCE
→ REVIEW / SAN™
→ OFF-CHAIN RECOGNITION
```

### 2. Core rule

```text
CREDIT → ALWAYS

FREE / UNCOMPENSATED SERVICE TO INNOVA_N
→ MÉDICI™ ELIGIBLE

PARTIALLY COMPENSATED SERVICE
→ MÉDICI™ ON THE UNCOMPENSATED FRACTION

PAID / FULLY COMPENSATED SERVICE
→ CREDIT + TRACE
→ 0 DIRECT MÉDICI™ FOR THAT FRACTION
```

The evaluation unit is **service + period**, not an entire company.

### 3. v0.1 formula

```text
Q = mean(quality, utility, continuity, traceability)

CANDIDATE_MÉDICI
= VALIDATED_VALUE
× UNCOMPENSATED_FRACTION
× Q
× CONFIDENCE
```

`VALIDATED_VALUE ≥ 0`; all other factors are normalised to `[0,1]`.

A free but useless service should not receive meaningful value. A highly valuable but fully paid service retains credit and causal recognition while receiving zero direct MÉDICI™ for the already-compensated fraction.

### 4. States

`PENDING_EVIDENCE` → missing data; no invented number.  
`CALCULATED_PENDING_APPROVAL` → reproducible calculation, not yet recognised.  
`RECOGNISED_OFFCHAIN` → approved balance in the versioned ledger.  
`CREDITED_NO_DIRECT_MEDICI_PAID` → value credited, fully compensated fraction.  
`SUPERSEDED / RECALCULATED` → a later state preserves the genealogy of the previous one.

### 5. NeoCronos™ and recalculation

Balances are not permanent labels. Changes in plan, contract, service function, quality, continuity, compensation, evidence or impact can trigger recalculation while prior states remain reconstructible.

### 6. Off-chain first

v0.1 records recognition in a Git-based off-chain ledger. It does not claim blockchain issuance, market value, convertibility, equity, financial rights, sovereign voting or legal participation.

### 7. Internal implementation

```text
infrastructure-registry.json
→ service-period inputs

medici-platform-engine.mjs
→ deterministic validation and calculation

medici-platform-ledger.generated.json
→ off-chain ledger projection
```

Private data can remain internal; WEB4™ should expose only public, verifiable fields.

### 8. No-invention rule

Creating the engine does not authorise intuitive token numbers. Missing data remains pending.

> **Missing evidence produces `pending`, not an invented figure.**

### 9. Result

Platform acknowledgements can now evolve from decorative credits into traceable infrastructure accounting: who supported what function, for what period, under what compensation model, with what validated value, and what recognition follows.

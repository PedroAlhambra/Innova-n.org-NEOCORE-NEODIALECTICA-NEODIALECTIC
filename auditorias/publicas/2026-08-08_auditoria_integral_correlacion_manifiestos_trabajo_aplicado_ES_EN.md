# Auditoría integral · Manifiestos ↔ trabajo aplicado
# Integral audit · Manifestos ↔ applied work

**Fecha / Date:** 2026-08-08  
**Marco / Framework:** Innova_N · Neodialéctica™ · NEOCore™ · WEB4™ · Síntesis Abierta™  
**Estado / Status:** público · postcheck relacional · revisable / public · relational postcheck · revisable

---

# ES · Castellano

## 1. Objeto

Revisar la capa pública del repositorio como un sistema relacionado y corregir un problema acumulado: los manifiestos habían crecido más deprisa que los enlaces explícitos entre **principios**, **análisis**, **auditorías**, **casos**, **obras**, **protocolos**, **evidencias** y **Síntesis Abiertas**.

La finalidad no es convertir cada manifiesto en un índice gigante, sino construir una navegación bidimensional:

```text
LECTURA LONGITUDINAL
I → II → III → ... → XLVII

LECTURA TRANSVERSAL
MANIFIESTO
↔ CASOS
↔ ANÁLISIS
↔ AUDITORÍAS
↔ EVIDENCIA
↔ OBRAS
↔ PROTOCOLOS
↔ SÍNTESIS ABIERTA
```

## 2. Capa revisada

La lectura integral de la capa pública se apoyó especialmente en:

- los manifiestos I–XLVII;
- el índice canónico de manifiestos;
- el índice y protocolo de Síntesis Abierta;
- `analisis/INDEX.md` y `analisis/publicos/README.md`;
- auditorías públicas;
- la serie España–Marruecos;
- los expedientes KDP/Author Central/IDEA y DistroKid–Spotify;
- los análisis sobre economía de la atención, IA institucional, Stanford/ACE, LinkedIn, religión/identidad y protección de la infancia;
- `obras/idea/README.md`;
- el Oráculo/índice de fragmentos;
- el Protocolo de Proyección Distribuida Neodialéctica™;
- y `wiki-source/Manifiestos.md`.

No se afirma que cada archivo histórico del repositorio haya sido reescrito o releído línea por línea en esta pasada. La revisión se concentra en los nodos canónicos y en las familias de trabajo que materialmente ponen a prueba los principios.

## 3. Hallazgo estructural principal

El repositorio contenía una **desincronización canónica**:

- existían ya manifiestos hasta **XLVII**;
- el índice de manifiestos todavía declaraba **I–XLV** y una taxonomía incompleta de oleadas;
- el índice de Síntesis Abierta todavía declaraba una cobertura inferior;
- otros READMEs periféricos conservan referencias históricas o contadores anteriores.

En esta pasada se corrigieron los dos índices canónicos de navegación:

1. `manifiestos/README.md` → **47 manifiestos · I–XLVII · 14 oleadas**;
2. `propuestas/sintesis-abierta/README.md` → **47 manifiestos · I–XLVII** y sus Issues actuales.

La sincronización de contadores en todos los READMEs periféricos queda separada de esta operación para no sustituir archivos grandes sin una pasada específica de comparación y postcheck.

## 4. Nueva capa relacional

Se crea:

- [`manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md`](../../manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md)

La matriz cubre **I–XLVII** y clasifica cada relación como:

- **A · aplicación o auditoría directa**;
- **B · análisis estructural**;
- **C · relación documental, genealógica o simbólica**.

La matriz permite que un lector que llegue desde un manifiesto encuentre trabajo que lo desarrolla o lo pone a prueba sin depender de conocer previamente la estructura de carpetas.

## 5. Núcleo de extracción y parasitismo

La correlación más fuerte aparece entre:

- **VI · Parasitismo Sistémico**;
- **VII · Economía del Aporte**;
- **IX · Memoria, Genealogía y Trazabilidad**;
- **XXI · Reconocimiento Neodialéctico**;
- **XXII · Contra la Reducción y la Captura Intelectual**;
- **XXVIII · Los Tesla**;
- **XXIX · Contra la Idolatría del Dinero**;
- **XXXIV · Utilidad Operativa y Auditoría Conjunta Perpetua**.

Y las familias aplicadas:

- economía de la atención → economía del aporte;
- DistroKid–Spotify;
- KDP–Author Central–IDEA;
- precedencia y convergencia en IA/Stanford;
- contratación, tutela y dependencia institucional en Canarias.

Los manifiestos materialmente acoplados a estos casos incorporan ahora bloques `Trabajo aplicado y casos relacionados` con enlaces internos relativos.

## 6. Disciplina de evidencia

La capa relacional incorpora límites explícitos para impedir que el enlace produzca una acusación más fuerte que la fuente:

```text
CORRELACIÓN
≠ CAUSALIDAD

PRECEDENCIA
≠ COPIA PROBADA

INVESTIGACIÓN
≠ CULPABILIDAD

PATRÓN FUNCIONAL
≠ IDENTIDAD MORAL DE UNA PERSONA O GRUPO

EXPEDIENTE ABIERTO
≠ CONCLUSIÓN PENAL O INTENCIONAL
```

Aplicaciones concretas:

- el expediente DistroKid–Spotify se mantiene abierto y no se presenta como prueba automática de desvío deliberado de regalías;
- Stanford/ACE y la convergencia institucional de IA preservan precedencia y similitudes, no prueban copia directa;
- el análisis de Canarias estudia contratación, tutela, concentración y control, sin etiquetar a personas o entidades como «parásitos»;
- el Punto de No Retorno Infantil™ permanece como hipótesis de umbral medible, no como estado ya probado;
- los expedientes España–Marruecos preservan la separación entre hechos, hipótesis y conexiones políticas no demostradas.

## 7. Manifiestos con enlace aplicado directo en esta pasada

Se añadieron bloques compactos sin alterar la numeración interna ni insertar material dentro del cuerpo doctrinal de:

- VI · Parasitismo Sistémico;
- VII · Economía del Aporte;
- IX · Memoria, Genealogía y Trazabilidad;
- XXI · Reconocimiento Neodialéctico;
- XXII · Contra la Reducción y la Captura Intelectual;
- XXVIII · Los Tesla;
- XXIX · Contra la Idolatría del Dinero;
- XXXI · Contra el Neuromarketing Antihumanista;
- XXXIV · Utilidad Operativa y Auditoría Conjunta Perpetua;
- XXXVIII · Protección Integral de la Infancia.

Para el resto, la relación queda disponible desde la matriz transversal. Esta decisión evita replicar decenas de enlaces en cada archivo y conserva el cuerpo de los manifiestos como documento legible.

## 8. Arquitectura resultante

```text
MANIFIESTO
├─ navegación longitudinal
├─ Síntesis Abierta
├─ trabajo aplicado directo cuando la relación es material
└─ mapa transversal I–XLVII
       ├─ análisis
       ├─ auditorías
       ├─ expedientes
       ├─ evidencias
       ├─ obras
       ├─ protocolos
       └─ capas simbólicas
```

La Wiki continúa cumpliendo sólo una función de orientación. `wiki-source/Manifiestos.md` apunta al índice y al mapa transversal, sin copiar las matrices.

## 9. Regla de mantenimiento propuesta y aplicada

A partir de esta pasada:

1. un nuevo manifiesto debe declarar una relación real con trabajo existente o indicar que todavía carece de caso aplicado;
2. un nuevo caso material debe incorporarse al mapa y enlazarse directamente desde los manifiestos cuya función pone realmente a prueba;
3. un caso no se enlaza sólo porque comparta vocabulario;
4. cada relación conserva el nivel probatorio del expediente;
5. la Wiki no duplica la matriz;
6. los commits conservan precedencia técnica y la fijación canónica permanece humana.

## 10. Pendientes detectados

La lectura integral detecta un pendiente independiente de la correlación: algunos **READMEs y portadas periféricas** todavía muestran contadores o rangos anteriores a XLVII. No se han sustituido masivamente en esta pasada para evitar romper archivos extensos sin comparación completa.

El índice canónico de manifiestos y el índice de Síntesis Abierta ya quedan normalizados a I–XLVII. Una pasada posterior de sincronización de superficies debe limitarse a contadores, accesos y navegación, sin reescribir contenido histórico.

---

# EN · English

## 1. Purpose

Review the repository's public layer as a related system and correct an accumulated problem: manifestos had grown faster than the explicit links connecting **principles**, **analyses**, **audits**, **cases**, **works**, **protocols**, **evidence** and **Open Syntheses**.

The goal is not to turn every manifesto into a giant index, but to build two-dimensional navigation:

```text
LONGITUDINAL READING
I → II → III → ... → XLVII

TRANSVERSAL READING
MANIFESTO
↔ CASES
↔ ANALYSES
↔ AUDITS
↔ EVIDENCE
↔ WORKS
↔ PROTOCOLS
↔ OPEN SYNTHESIS
```

## 2. Reviewed layer

The integral reading of the public layer focused on Manifestos I–XLVII; the canonical manifesto index; Open Synthesis index and protocol; public-analysis and audit indexes; the Spain–Morocco series; KDP/Author Central/IDEA and DistroKid–Spotify cases; analyses on the attention economy, institutional AI, Stanford/ACE, LinkedIn, religion/identity and child protection; IDEA's canonical documentary node; the Oracle/fragments index; the Distributed Neodialectical Projection Protocol™; and the versioned Wiki source.

This pass does not claim that every historical file in the repository was rewritten or reread line by line. It focuses on canonical nodes and work families that materially test the principles.

## 3. Main structural finding

A **canonical synchronisation drift** was present: Manifestos already existed through **XLVII**, while the manifesto and Open Synthesis indexes still exposed older ranges and incomplete wave taxonomy.

This pass normalised:

1. `manifiestos/README.md` → **47 manifestos · I–XLVII · 14 waves**;
2. `propuestas/sintesis-abierta/README.md` → **47 manifestos · I–XLVII** and current Issues.

Mass replacement of every peripheral README counter is intentionally separated from this operation so large files are not replaced without a dedicated comparison and postcheck.

## 4. New relational layer

The new [`manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md`](../../manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md) covers I–XLVII and classifies links as direct application/audit, structural analysis, or documentary/genealogical/symbolic relation.

## 5. Extraction and parasitism core

The strongest correlation connects Systemic Parasitism, Contribution Economy, Memory-Genealogy-Traceability, Neodialectical Recognition, Against Intellectual Reduction and Capture, The Teslas, Against the Idolatry of Money and Operational Utility/Perpetual Joint Audit with the attention economy, DistroKid–Spotify, KDP–Author Central–IDEA, AI/Stanford precedence and convergence, and Canary Islands guardianship/procurement/dependency analysis.

## 6. Evidence discipline

The relational layer explicitly preserves:

```text
CORRELATION ≠ CAUSATION
PRECEDENCE ≠ PROVEN COPYING
INVESTIGATION ≠ GUILT
FUNCTIONAL PATTERN ≠ MORAL IDENTITY
OPEN CASE ≠ PENAL OR INTENTIONAL CONCLUSION
```

## 7. Direct manifesto links added in this pass

Compact `Applied work and related cases` blocks were added without changing internal numbering or inserting material inside the doctrinal body of VI, VII, IX, XXI, XXII, XXVIII, XXIX, XXXI, XXXIV and XXXVIII.

The remaining manifestos are connected through the transversal map, avoiding repetitive link blocks that would damage readability.

## 8. Resulting architecture

```text
MANIFESTO
├─ longitudinal navigation
├─ Open Synthesis
├─ direct applied work where materially coupled
└─ transversal I–XLVII map
       ├─ analyses
       ├─ audits
       ├─ case files
       ├─ evidence
       ├─ works
       ├─ protocols
       └─ symbolic layers
```

The Wiki remains an orientation layer and does not duplicate the matrix.

## 9. Maintenance rule

New manifestos should declare a real relation to existing work or explicitly state that no applied case exists yet. New material cases should enter the map and be linked directly from manifestos they genuinely test. Links must preserve the evidence level of the underlying case.

## 10. Detected pending work

Some **peripheral READMEs and cover surfaces** still expose counters or ranges preceding XLVII. They were not mass-replaced in this pass in order to avoid breaking large files without a full comparison.

The canonical manifesto and Open Synthesis indexes are already normalised to I–XLVII. A later surface-synchronisation pass should be restricted to counters, access links and navigation, without rewriting historical content.

---

**© 2026 Pedro Martínez Alhambra · Fundación Innova_N / Innova_N Foundation**

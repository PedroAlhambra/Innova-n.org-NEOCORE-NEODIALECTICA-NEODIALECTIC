from pathlib import Path

p=Path('neoaxiomas/NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md')
text=p.read_text(encoding='utf-8')
marker='# EN · English'
start=text.index(marker)
new_en=r'''# EN · English

## 1. Detected absence

The current formulation of NAX-10 clearly developed the **grammar of custodial figures** —Eagle, Crown, Earth/World, Tower/Castle, Stone and Lion— but left insufficiently explicit an earlier historical layer of the project itself: **WaterFire™** and the elemental grammar that this symbol already contained in compressed form.

The absence is genealogical, not merely aesthetic.

Fragment III states:

> “WaterFire™ is not a concept or an element.”
>
> “It is the paradox that sustains the origin of the system: a fire that orders without destroying and a water that guides without dispersing.”
>
> “NEOCore™ is born from this.”

WaterFire™ must therefore be recognised as a **historical root and synthetic operator** of the elemental dimension of the framework.

## 2. WaterFire™ is not a list

WaterFire™ does not simply mean adding two elements.

It represents a relation:

```text
FIRE
→ transformation · energy · impulse · creation · possible destruction

WATER
→ continuity · adaptation · memory · regulation · possible dispersion

WATERFIRE™
→ regulated tension
→ transformation without devastation
→ fluidity without loss of direction
→ contradiction preserved until a higher synthesis
```

This formulation anticipates a central property of Neodialectics: **opposites need not be eliminated in order to produce order; they may be preserved in relation and generate a new structure**.

## 3. Explicit elemental layer

The symbolic grammar of the framework must make visible, at minimum, the five elements already recovered in its iconography:

- **Water™** → continuity, memory, adaptation, life, circulation and the capacity to receive form without losing material identity;
- **Fire™** → energy, transformation, will, light, creation and the risk of destruction when left without regulation;
- **Earth™** → matter, limit, biosphere, support, territory, shared reality and material condition;
- **Wood™** → growth, living structure, branching, regeneration, learning and organic continuity;
- **Metal™** → technique, tools, precision, resistance, conduction, industry and the capacity for material transformation.

These five symbols do not constitute an exhaustive inventory of the universe.

## 4. Neoaxiom of Elemental Totality™

> **No symbolic enumeration of elements shall be confused with the totality it seeks to represent. The framework preserves explicit elements to make its grammar legible, while remaining open to all materials, states, forces, relations, forms of life, knowledge and realities known or yet to be known that are relevant to understanding the Whole.**

The rule may be expressed as follows:

```text
EXPLICIT ELEMENTS
≠
TOTALITY

WATER + FIRE + EARTH + WOOD + METAL
→ READING GATEWAY
→ NOT AN ONTOLOGICAL LIMIT

ELEMENTAL TOTALITY™
=
ALL THAT IS KNOWN
+ ALL THAT CAN BE RELATED
+ OPENNESS TO WHAT IS STILL UNKNOWN
+ TRACEABILITY
+ SYNTHESIS
```

## 5. Relation to the Neodialectical shield and flag

The shield should not represent only institutions, persons or abstract virtues. Within its own frame it must contain a reference to the **materiality of the world** and to the forces through which humanity understands and transforms reality.

Water, Fire, Earth, Wood and Metal should therefore remain explicitly integrated into its visual grammar.

The flag and shield, however, do not mean “five elements and nothing more”. Their symbolic scope is broader:

> **to represent all persons and, jointly, the totality of concentrated human knowledge existing in spacetime, including the material, living, technical, cultural, symbolic and cognitive reality that this knowledge seeks to understand.**

The representation is necessarily compressed. It cannot literally draw everything that exists. Its function is to declare that **no part of reality is excluded in principle from the field of Synthesis**.

## 6. Two layers of NAX-10

NAX-10 should henceforth be read as a structure of two complementary layers:

### A · Custodial figures

Eagle · Crown · Earth/World · Tower/Castle · Stone · Lion · open historical constellation.

These figures express functions of vision, responsibility, limit, protection, foundation, strength and memory.

### B · Elements of reality

Water · Fire · Earth · Wood · Metal · openness to material and relational totality.

These elements express the world upon which custody operates and of which custody itself forms a part.

```text
CUSTODY WITHOUT A WORLD
=
EMPTY ABSTRACTION

WORLD WITHOUT CUSTODY
=
POWER WITHOUT DIRECTION

CUSTODIAL FIGURES
+
ELEMENTAL TOTALITY
+
WATERFIRE™
=
EXPANDED NEODIALECTICAL ARCHETYPAL GRAMMAR
```

## 7. Why WaterFire™ is historically central

This relation explains why WaterFire™ appears in an early layer of the project.

Before the current architecture formalised SAN™, NEOREALs™, multihead layers, the double pyramid, memory of absence or the Neoaxiomatic layer, a structural intuition was already present:

**order without destroying; guide without dispersing; preserve creative contradiction.**

This makes WaterFire™ a first-order genealogical piece. It does not retrospectively prove that the entire system had already been formulated at that time, but it does document real conceptual continuity between its symbolic root and later mechanisms.

## 8. Safeguard against simplification

The framework does not adopt a classical five-element theory as scientific dogma.

The elements operate simultaneously as:

- cultural memory;
- archetypal language;
- pedagogical compression;
- representation of material functions;
- a gateway to interdisciplinary relations.

Where physics, chemistry, biology, cosmology or other sciences describe reality with more precise categories, those categories retain priority in their empirical domains. Elemental grammar does not replace them: **it connects them symbolically without erasing their specificity**.

## 9. Synthesis formula

> **WaterFire™ is the historical memory of a creative contradiction. The elements make the materiality of that contradiction visible. Elemental Totality™ prevents the symbol from closing around its own list. And NAX-10 reunites custody and world: that which must be cared for and that of which custody itself forms a part.**

**Status:** RESTORED AS A GENEALOGICAL ROOT OF NAX-10 · OPEN TO SAN™.
'''
text=text[:start]+new_en
p.write_text(text,encoding='utf-8')
print('NAX10_ELEMENTAL_SYMMETRY=1')

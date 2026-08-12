from pathlib import Path
import re

ROOT=Path('.').resolve()
p=ROOT/'neoaxiomas/README.md'
text=p.read_text(encoding='utf-8')
old=text

old0='''The Neoaxiomatic layer distinguishes inherited axioms, activated neoaxioms, candidate neoaxioms, revised neoaxioms and suspended neoaxioms. Revision never erases genealogy.'''
new0='''The Neoaxiomatic layer distinguishes:

- **inherited axiom:** a principle already present and consolidated in the framework;
- **activated neoaxiom:** a principle that begins to operate explicitly in the current architecture;
- **candidate neoaxiom:** a formulation still undergoing scrutiny;
- **revised neoaxiom:** an improved formulation that does not erase its genealogy;
- **suspended neoaxiom:** a principle whose application is halted because of a contradiction, evidence or pending risk.

The non-deletion rule remains in force: a revision does not erase the path that led to the previous formulation.'''
if text.count(old0)!=1:
    raise SystemExit(f'Neoaxioms §0 compression target count={text.count(old0)}')
text=text.replace(old0,new0,1)

start=text.index('# EN · English')
end=text.index('## Trazabilidad / Traceability', start)
en=text[start:end]
# Mirror the separators used by the Spanish canonical body.
en=re.sub(r'(?<!---\n\n)\n## NAX-', '\n---\n\n## NAX-', en)

old_open='''## Open Synthesis

Useful contributions include counterexamples, conflicts between Neoaxioms, multihead failure modes, alternative topologies, energy measurements, life-cycle analysis, NEOREAL traceability proposals, symbolic criticism and reproducible implementations.

**[Contribute to SAN™ →](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)**

---

'''
new_open='''---

## 1. Relationship among the current Neoaxioms

```text
NAX-01 · UNITY OF MEANING / DISTRIBUTED POWER
        │
        ├── NAX-02 · FIRST FRACTAL MULTIHEAD LAYER
        │      ├── NAX-03 · NO PRIOR HOMOGENISATION
        │      ├── NAX-05 · DIFFERENTIAL + RETURN TO SOURCE
        │      └── NAX-06 · MEMORY OF ABSENCE
        │
        ├── NAX-04 · FRACTAL DOUBLE PYRAMID
        ├── NAX-07 · OPERATIONAL NEOREAL NETWORK
        ├── NAX-08 · COOPERATIVE EXCELLENCE
        ├── NAX-09 · VERIFIED DISTRIBUTED COMPUTING
        ├── NAX-10 · EAGLE · CROWN · EARTH · TOWER · STONE · LION
        ├── NAX-12 · TRACEABILITY REPLACES REDUNDANT BUREAUCRACY
        │      └── NAX-13 · RELEASED TIME → CREATION AND CONTRIBUTION
        └── NAX-14 · SYMBIOTIC ACCESS WITHOUT CIVILISATIONAL FRACTURE
               ↖ transversal relation with NAX-08 · cooperation without exclusion

NAX-11 · HUMAN FIXATION + REVISABLE SAN
        └── governs the transition from proposal to fixed state
```

### Open Synthesis index by Neoaxiom

| Neoaxiom | Synthesis |
|---|---|
| **NAX-01 · Unity of Meaning and Distribution of Power™** | [#84](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/84) |
| **NAX-02 · First Fractal Multihead Layer™** | [#85](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/85) |
| **NAX-03 · No Prior Homogenisation™** | [#86](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/86) |
| **NAX-04 · Fractal Double Pyramid™** | [#87](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/87) |
| **NAX-05 · Monadic Differential and Return to Source™** | [#88](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/88) |
| **NAX-06 · Memory of Absence™** | [#89](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/89) |
| **NAX-07 · Mandatory NEOREAL™ Network for Operational Actors** | [#90](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/90) |
| **NAX-08 · Cooperative Excellence against Predatory Competition™** | [#91](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/91) |
| **NAX-09 · Distributed Local Computing with Ecological Verification™** | [#92](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/92) |
| **NAX-10 · Archetypal Grammar of Custodianship™ — Eagle, Crown, Earth, Tower, Stone and Lion** | [#93](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/93) |
| **NAX-11 · Human Fixation Authority and Revisable Synthesis™** | [#94](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/94) |
| **NAX-12 · Traceability Substitution for Redundant Bureaucracy™** | [#95](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/95) |
| **NAX-13 · Releasing Control Time into Creation and Contribution™** | [#96](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/96) |
| **NAX-14 · Prevention of Symbiotic Bifurcation™** | [#97](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/97) |

**General matrix:** [Issue #80](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/80).

---

## 2. How to participate in Neoaxiom Open Synthesis

Especially useful contributions include:

- counterexamples;
- contradictions among Neoaxioms;
- risks of centralisation or fragmentation;
- limits of the multihead architecture;
- weighting criteria among heads;
- alternative models to the double pyramid;
- comparative energy measurements for local / datacentre computing;
- hardware life-cycle analyses;
- NEOREAL™ traceability proposals;
- criticism of the archetypal grammar;
- proposals for more universal wording;
- reproducible technical implementations.

**[Contribute to SAN™ →](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)**

---

'''
if en.count(old_open)!=1:
    raise SystemExit(f'Neoaxioms Open Synthesis compression target count={en.count(old_open)}')
en=en.replace(old_open,new_open,1)
text=text[:start]+en+text[end:]

if text==old:
    raise SystemExit('No Neoaxiom symmetry changes produced')
p.write_text(text,encoding='utf-8')
print('NEOAXIOM_STRICT_BILINGUAL_SYMMETRY changed=1')

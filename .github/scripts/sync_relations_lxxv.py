from pathlib import Path
import re

ROOT=Path('.').resolve()
REL=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
START='<!-- NEO_RELATIONS_LXXV_START -->'
END='<!-- NEO_RELATIONS_LXXV_END -->'

block=f'''{START}

## LXXV · Las Hojas Carcomidas™ · Memoria Natural, Viración Arquetípica y Fraternidad de la Coexistencia™ / The Gnawed Leaves™ · Natural Memory, Archetypal Drift and Fraternity of Coexistence™

- **Manifiesto / Manifesto:** [LXXV · Las Hojas Carcomidas™ · Memoria Natural, Viración Arquetípica y Fraternidad de la Coexistencia™ / The Gnawed Leaves™ · Natural Memory, Archetypal Drift and Fraternity of Coexistence™](./75_las_hojas_carcomidas_memoria_natural_viracion_arquetipica_ES_EN.md).
- **Relación / Relation:** B–C · memoria material-relacional, degradación de relaciones, reciprocidad ecológica, viración arquetípica y custodia de sistemas vivos / material-relational memory, degradation of relations, ecological reciprocity, archetypal drift and custodianship of living systems.
- **Síntesis Abierta / Open Synthesis:** [#134](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/134).
- **Candidato neoaxiomático / Neoaxiomatic candidate:** [C-NAX-22 · Memoria Material-Relacional™ / Material-Relational Memory™ · #135](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/135) · [capa neoaxiomática / Neoaxiomatic layer](../neoaxiomas/README.md).
- **Interconexiones / Interconnections:** [VI · Manifiesto sobre el Parasitismo Sistémico / Manifesto on Systemic Parasitism](./09_parasitismo_sistemico_ES_EN.md) · [XVI · Manifiesto de la Refragmentación Arquetípica™ / Manifesto of Archetypal Refragmentation™](./16_refragmentacion_arquetipica_ES_EN.md) · [XVII · Manifiesto del Respeto a Todos los Seres Vivos™ / Manifesto of Respect for All Living Beings™](./17_respeto_todos_seres_vivos_ES_EN.md) · [XL · Respeto Neodialéctico, Neoego y Honor Relacional™ / Neodialectical Respect, Neoego and Relational Honour™](./40_respeto_neoego_honor_relacional_ES_EN.md) · [LXXIV · Asimetría de la Destrucción™ · Del Trol Humano al Bot / Asymmetry of Destruction™ · From the Human Troll to the Bot](./74_asimetria_destruccion_trol_humano_bot_ES_EN.md).

**Regla probatoria / Evidentiary rule:** Memoria Material-Relacional™ no equivale a consciencia, intención ni almacenamiento deliberado; las categorías empíricas de biología, ecología, geología, genética, climatología, química o física conservan prioridad dentro de sus dominios. / Material-Relational Memory™ is not equivalent to consciousness, intention or deliberate storage; empirical categories from biology, ecology, geology, genetics, climatology, chemistry or physics retain priority within their domains.

{END}'''

text=REL.read_text(encoding='utf-8')
old=text
text=re.sub(r'^\*\*Cobertura / Coverage:\*\*.*$',
            '**Cobertura / Coverage:** I–LXXV · 75 manifiestos finitos + ∞ como continuidad abierta / 75 finite manifestos I–LXXV + ∞ as open continuity  ',
            text,count=1,flags=re.M)
if START in text and END in text:
    text=re.sub(re.escape(START)+r'.*?'+re.escape(END),block,text,count=1,flags=re.S)
else:
    marker='## Regla de mantenimiento / Maintenance rule'
    if marker in text:
        text=text.replace(marker,block+'\n\n---\n\n'+marker,1)
    else:
        text=text.rstrip()+'\n\n'+block+'\n'
if text!=old:
    REL.write_text(text,encoding='utf-8')
    print('RELATIONS_LXXV_SYNC changed=1')
else:
    print('RELATIONS_LXXV_SYNC changed=0')

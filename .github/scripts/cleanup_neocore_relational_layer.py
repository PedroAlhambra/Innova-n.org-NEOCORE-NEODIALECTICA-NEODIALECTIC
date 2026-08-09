from pathlib import Path
import re,sys
neo=Path('neoaxiomas/README.md');t=neo.read_text(encoding='utf-8')
old='''        ├── NAX-08 · COOPERACIÓN DE EXCELENCIA
        │      └── NAX-14 · PREVENCIÓN DE BIFURCACIÓN SIMBIÓTICA
        ├── NAX-09 · COMPUTACIÓN DISTRIBUIDA VERIFICADA
        ├── NAX-10 · ÁGUILA · CORONA · TIERRA · TORRE · PIEDRA
        ├── NAX-12 · TRAZABILIDAD SUSTITUYE BUROCRACIA REDUNDANTE
        │      └── NAX-13 · TIEMPO LIBERADO → CREACIÓN Y APORTE
        └── NAX-14 · ACCESO SIMBIÓTICO SIN FRACTURA CIVILIZATORIA'''
new='''        ├── NAX-08 · COOPERACIÓN DE EXCELENCIA
        ├── NAX-09 · COMPUTACIÓN DISTRIBUIDA VERIFICADA
        ├── NAX-10 · ÁGUILA · CORONA · TIERRA · TORRE · PIEDRA
        ├── NAX-12 · TRAZABILIDAD SUSTITUYE BUROCRACIA REDUNDANTE
        │      └── NAX-13 · TIEMPO LIBERADO → CREACIÓN Y APORTE
        └── NAX-14 · ACCESO SIMBIÓTICO SIN FRACTURA CIVILIZATORIA
               ↖ relación transversal con NAX-08 · cooperación sin exclusión'''
if old in t:t=t.replace(old,new,1)
# Formatting only: collapse accidental runs of 4+ newlines around separators.
t=re.sub(r'\n{4,}(---\n)',r'\n\n\1',t)
neo.write_text(t,encoding='utf-8')

root=Path('README.md');r=root.read_text(encoding='utf-8')
es='| **Manifiestos** | **[I–LIX · 59 manifiestos bilingües](./manifiestos/README.md)** |'
en='| **Manifestos** | **[I–LIX · 59 bilingual manifestos](./manifiestos/README.md)** |'
esadd=es+'\n| **Neoaxiomas™** | [Capa Axiomática Abierta](./neoaxiomas/README.md) · [Síntesis específicas](./propuestas/sintesis-abierta/README.md#neoaxiomas--síntesis-abierta-específica--neoaxioms--dedicated-open-synthesis) |\n| **Mapa relacional vivo** | [Manifiestos ↔ trabajo aplicado](./manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md) · [Auditoría MAXPROC](./auditorias/publicas/2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones_ES_EN.md) |'
enadd=en+'\n| **Neoaxioms™** | [Open Axiomatic Layer](./neoaxiomas/README.md) · [Dedicated syntheses](./propuestas/sintesis-abierta/README.md#neoaxiomas--síntesis-abierta-específica--neoaxioms--dedicated-open-synthesis) |\n| **Living relational map** | [Manifestos ↔ applied work](./manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md) · [MAXPROC audit](./auditorias/publicas/2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones_ES_EN.md) |'
if es in r and '| **Neoaxiomas™** | [Capa Axiomática Abierta]' not in r:r=r.replace(es,esadd,1)
if en in r and '| **Neoaxioms™** | [Open Axiomatic Layer]' not in r:r.replace(en,enadd,1)
# Correct a typo-safe fallback if English row exists and replacement was not assigned.
if en in r and '| **Neoaxioms™** | [Open Axiomatic Layer]' not in r:r=r.replace(en,enadd,1)
root.write_text(r,encoding='utf-8')

nt=neo.read_text(encoding='utf-8')
block=re.search(r'## 1\. Relación entre los Neoaxiomas vigentes\n\n```text\n(.*?)```',nt,re.S)
if not block:raise SystemExit('Neoaxiom relation tree missing')
if block.group(1).count('NAX-14')!=1:raise SystemExit('NAX-14 duplicated in relation tree')
if '| **Neoaxiomas™** | [Capa Axiomática Abierta]' not in root.read_text(encoding='utf-8'):raise SystemExit('root ES Neoaxioms access row missing')
print('POSTCHECK OK: Neoaxiom relation tree deduplicated; root access tables expose Neoaxioms and relational map')

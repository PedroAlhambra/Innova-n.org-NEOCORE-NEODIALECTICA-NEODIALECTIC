from pathlib import Path
import runpy

p = Path('manifiestos/40_respeto_neoego_honor_relacional_ES_EN.md')
text = p.read_text(encoding='utf-8')

es_protocol = '* [Protocolo operativo de Síntesis Abierta](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)'
es_issue = '* [Síntesis Abierta XL · Issue #48](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/48)'
if es_issue not in text:
    text = text.replace(es_protocol, es_issue + '\n' + es_protocol, 1)

en_protocol = '* [Open Synthesis operational protocol](../propuestas/sintesis-abierta/APORTAR_A_LA_SINTESIS_ES_EN.md)'
en_issue = '* [Open Synthesis XL · Issue #48](https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/48)'
if en_issue not in text:
    text = text.replace(en_protocol, en_issue + '\n' + en_protocol, 1)

p.write_text(text, encoding='utf-8')

runpy.run_path('.github/scripts/one_shot_sync_xliii.py', run_name='__main__')

Path('.github/scripts/one_shot_repair_xl_run_xliii.py').unlink(missing_ok=True)
Path('.github/workflows/one-shot-repair-xl-run-xliii.yml').unlink(missing_ok=True)

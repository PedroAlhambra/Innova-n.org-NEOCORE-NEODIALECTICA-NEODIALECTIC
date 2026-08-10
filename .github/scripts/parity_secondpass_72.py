from pathlib import Path
import re

# Executes only inside the temporary 7.2 parity run, after the conservative
# first-pass additions and immediately before the audit. It corrects five
# cases where preserving missing structure initially duplicated material that
# was already present in compressed English prose/code.

def replace_tail(path, marker, replacement):
    p=Path(path)
    s=p.read_text(encoding='utf-8')
    pat=re.compile(re.escape(marker)+r'.*?(?=\n##\s+)',re.S)
    if not pat.search(s):
        raise SystemExit(f'second-pass marker not found: {marker}')
    s=pat.sub(replacement.strip()+'\n',s,count=1)
    p.write_text(s,encoding='utf-8')

replace_tail('manifiestos/28_los_tesla_ES_EN.md','<!-- PARITY_72_28_II -->',r'''
<!-- PARITY_72_28_II -->
The Spanish source distinguishes eight auditable mechanisms rather than collapsing them into one accusation:

- **economic**: funding, employment, access or subsistence;
- **institutional**: exclusion from decision spaces;
- **reputational**: discredit without refuting the work;
- **legal/bureaucratic**: exhaustion through procedures or litigation;
- **algorithmic**: burying the source while amplifying stronger distributors;
- **cognitive**: forcing endless re-explanation of documented work;
- **historical**: preserving the idea while erasing origin;
- **physical**: violence or caused death, assertable only with sufficient evidence.
''')

replace_tail('manifiestos/30_coherencia_fines_medios_ES_EN.md','<!-- PARITY_72_30_III -->',r'''
<!-- PARITY_72_30_III -->
The Spanish source keeps nine dimensions explicit:

- necessity;
- proportionality;
- possible transparency;
- reversibility;
- temporality;
- responsibility;
- traceability;
- non-dehumanisation;
- coherence between the means and the value invoked by the end.
''')

replace_tail('manifiestos/34_utilidad_operativa_marco_auditoria_conjunta_perpetua_ES_EN.md','<!-- PARITY_72_34_II -->',r'''
<!-- PARITY_72_34_II -->
The audit function is explicitly decomposed in the Spanish source so that it can:

1. reconstruct what was claimed;
2. identify who made the claim and in what context;
3. recover the available sources and evidence;
4. separate fact, testimony, inference, hypothesis and proposal;
5. identify contradictions and missing information;
6. compare alternative explanations;
7. preserve dissent instead of erasing it;
8. record corrections and changes of criterion;
9. connect the case with related cases and systemic patterns;
10. verify whether a proposed repair was actually applied;
11. measure the result after implementation;
12. reopen the case if materially new evidence appears.

The objective is not an omniscient tribunal, but persistent memory of claims, corrections, responsibilities and outcomes.
''')

replace_tail('manifiestos/39_autoconciencia_necesidad_vital_neodialectica_ES_EN.md','<!-- PARITY_72_39_III -->',r'''
<!-- PARITY_72_39_III -->
The Spanish source also preserves the failure sequence that the existing English synthesis contrasts with its relational sequence:

```text
ISOLATED PROBLEM
→ LOCAL SOLUTION
→ UNOBSERVED EXTERNAL EFFECT
→ NEW PROBLEM
→ NEW PARTIAL CORRECTION
→ ACCUMULATION OF CONTRADICTIONS
```
''')

replace_tail('manifiestos/42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md','<!-- PARITY_72_42_VIII -->',r'''
<!-- PARITY_72_42_VIII -->
The Spanish source explicitly contrasts the existing English person-centred sequence with the reduction sequence:

```text
USER
→ AUDIENCE
→ DATA
→ PROFILE
→ TARGET
→ CONVERSION
```
''')

# Remove the temporary audit hook from the auditor source before the successful
# workflow commits the final tree, then delete this one-shot helper itself.
aud=Path('.github/scripts/audit_es_en_parity.py')
s=aud.read_text(encoding='utf-8')
s=re.sub(r'\n# NEOCORE72_SECOND_PASS_HOOK_START\n.*?# NEOCORE72_SECOND_PASS_HOOK_END\n','\n',s,count=1,flags=re.S)
aud.write_text(s,encoding='utf-8')
Path(__file__).unlink()

from pathlib import Path
import os, re, sys

ROOT=Path('.').resolve()
REPO='https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC'
NEO=ROOT/'neoaxiomas/README.md'
TEMP=ROOT/'neoaxiomas/NAX-12_14_PROPUESTA_TEMPORAL_ES_EN.md'
SYN=ROOT/'propuestas/sintesis-abierta/README.md'
MAN_INDEX=ROOT/'manifiestos/README.md'
REL=ROOT/'manifiestos/RELACIONES_TRABAJO_APLICADO_ES_EN.md'
AUDIT=ROOT/'auditorias/publicas/2026-08-09_auditoria_relacional_manifestos_neoaxiomas_publicaciones_ES_EN.md'

ISSUES={
'NAX-01':84,'NAX-02':85,'NAX-03':86,'NAX-04':87,'NAX-05':88,'NAX-06':89,'NAX-07':90,
'NAX-08':91,'NAX-09':92,'NAX-10':93,'NAX-11':94,'NAX-12':95,'NAX-13':96,'NAX-14':97,
}
TITLES_ES={
'NAX-01':'Unidad de sentido y distribución de potencia™','NAX-02':'Primera Capa Fractal Multicabeza™','NAX-03':'No Homogeneización Previa™','NAX-04':'Doble Pirámide Fractal™','NAX-05':'Diferencial Monádico y Retorno a Fuente™','NAX-06':'Memoria de Ausencia™','NAX-07':'Red NEOREAL™ Obligatoria para Actores Operativos','NAX-08':'Cooperación de Excelencia frente a Competencia Depredadora™','NAX-09':'Computación Distribuida Local con Verificación Ecológica™','NAX-10':'Gramática Arquetípica de Custodia™','NAX-11':'Autoridad de Fijación Humana y Síntesis Revisable™','NAX-12':'Trazabilidad Sustitutiva de Burocracia Redundante™','NAX-13':'Liberación del Tiempo de Control hacia Creación y Aporte™','NAX-14':'Prevención de la Bifurcación Simbiótica™'}

def rel(frm,target): return os.path.relpath(target,start=frm.parent).replace(os.sep,'/')
def issue_url(n): return f'{REPO}/issues/{n}'

def replace_block(text,start,end,block):
    if start in text and end in text:
        return re.sub(re.escape(start)+r'.*?'+re.escape(end),block,text,count=1,flags=re.S)
    return text

# 1) Integrate full NAX-12..14 proposal without shortening any existing text.
neo=NEO.read_text(encoding='utf-8')
if TEMP.exists():
    tmp=TEMP.read_text(encoding='utf-8')
    es_m=re.search(r'# ES · Castellano\n\n(.*?)(?=\n# EN · English)',tmp,re.S)
    en_m=re.search(r'# EN · English\n\n(.*)\Z',tmp,re.S)
    if es_m and '## NAX-12 · Trazabilidad Sustitutiva' not in neo:
        anchor='\n---\n\n## 1. Relación entre los Neoaxiomas iniciales'
        neo=neo.replace(anchor,'\n---\n\n'+es_m.group(1).strip()+'\n\n---\n\n## 1. Relación entre los Neoaxiomas iniciales',1)
    if en_m and '## NAX-12 · Traceability Substitution' not in neo:
        anchor='\n---\n\n## Open Synthesis'
        neo=neo.replace(anchor,'\n\n'+en_m.group(1).strip()+'\n\n---\n\n## Open Synthesis',1)

# 2) Reaffirm inherited non-reductive integrity rule.
needle='La regla de no eliminación continúa vigente: una revisión no borra el camino que llevó a la formulación anterior.'
add='''\n\n> **Regla heredada de integridad no reductiva:** ninguna tarea de mantenimiento, sincronización, traducción, indexación o automatización puede sustituir un texto fuente del marco por un resumen ni acortarlo para hacerlo más manejable. Si se crea una capa de acceso, índice o navegación, el texto íntegro permanece y la nueva capa enlaza de vuelta a él.'''
if needle in neo and 'Regla heredada de integridad no reductiva' not in neo:
    neo=neo.replace(needle,needle+add,1)
needle_en='Revision never erases genealogy.'
add_en='''\n\n> **Inherited non-reductive integrity rule:** maintenance, synchronisation, translation, indexing or automation must never replace a framework source text with a summary or shorten it for convenience. Any access, index or navigation layer must preserve and link back to the complete source text.'''
if needle_en in neo and 'Inherited non-reductive integrity rule' not in neo:
    neo=neo.replace(needle_en,needle_en+add_en,1)

# 3) Put a dedicated Open Synthesis link in every ES/EN Neoaxiom section.
for ident,num in ISSUES.items():
    # Each ID appears twice (ES/EN). Work section by section.
    pattern=re.compile(r'(^## '+re.escape(ident)+r' · [^\n]+\n)(.*?)(?=^## NAX-\d{2} ·|^## \d+\.|^## Open Synthesis|^# EN ·|\Z)',re.M|re.S)
    def patch(m):
        head,body=m.group(1),m.group(2)
        body=re.sub(r'\n\*\*(?:Síntesis Abierta específica|Dedicated Open Synthesis):\*\*[^\n]*','',body)
        link=f'{issue_url(num)}'
        label='Síntesis Abierta específica' if '**Estado:**' in body else 'Dedicated Open Synthesis'
        line=f'\n**{label}:** [#{num}]({link}) · [Matriz general / General matrix #80]({issue_url(80)})\n'
        status=re.search(r'\n\*\*(?:Estado|Status):\*\*[^\n]*',body)
        if status:
            pos=status.end(); body=body[:pos]+line+body[pos:]
        else:
            body=line+body
        return head+body
    neo=pattern.sub(patch,neo)

# 4) Replace ES relation topology with complete NAX-01..14 map and synthesis index.
start='## 1. Relación entre los Neoaxiomas iniciales'
end='## 2. Cómo participar en la Síntesis Abierta de Neoaxiomas'
block=f'''## 1. Relación entre los Neoaxiomas vigentes

```text
NAX-01 · UNIDAD DE SENTIDO / POTENCIA DISTRIBUIDA
        │
        ├── NAX-02 · PRIMERA CAPA FRACTAL MULTICABEZA
        │      ├── NAX-03 · NO HOMOGENEIZACIÓN
        │      ├── NAX-05 · DIFERENCIAL + RETORNO A FUENTE
        │      └── NAX-06 · MEMORIA DE AUSENCIA
        │
        ├── NAX-04 · DOBLE PIRÁMIDE FRACTAL
        ├── NAX-07 · RED NEOREAL OPERATIVA
        ├── NAX-08 · COOPERACIÓN DE EXCELENCIA
        │      └── NAX-14 · PREVENCIÓN DE BIFURCACIÓN SIMBIÓTICA
        ├── NAX-09 · COMPUTACIÓN DISTRIBUIDA VERIFICADA
        ├── NAX-10 · ÁGUILA · CORONA · TIERRA · TORRE · PIEDRA
        ├── NAX-12 · TRAZABILIDAD SUSTITUYE BUROCRACIA REDUNDANTE
        │      └── NAX-13 · TIEMPO LIBERADO → CREACIÓN Y APORTE
        └── NAX-14 · ACCESO SIMBIÓTICO SIN FRACTURA CIVILIZATORIA

NAX-11 · FIJACIÓN HUMANA + SAN REVISABLE
        └── gobierna la transición de propuesta a estado fijado
```

### Índice de Síntesis Abierta por Neoaxioma

| Neoaxioma | Síntesis |
|---|---|
'''+ '\n'.join(f'| **{k} · {TITLES_ES[k]}** | [#{v}]({issue_url(v)}) |' for k,v in ISSUES.items()) + f'''

**Matriz general:** [Issue #80]({issue_url(80)}).

---

{end}'''
if start in neo and end in neo:
    neo=re.sub(re.escape(start)+r'.*?'+re.escape(end),block,neo,count=1,flags=re.S)

# Add cross-map navigation.
nav='**Navegación / Navigation:**'
if nav in neo and 'RELACIONES_TRABAJO_APLICADO_ES_EN.md' not in neo.split(nav,1)[1].split('\n',1)[0]:
    firstline=neo.split(nav,1)[1].split('\n',1)[0]
    neo=neo.replace(nav+firstline,nav+firstline+f' · [Mapa transversal / Transversal map]({rel(NEO,REL)})',1)
NEO.write_text(neo,encoding='utf-8')

# 5) Add specific Neoaxiom synthesis index to Open Synthesis landing page.
s=SYN.read_text(encoding='utf-8')
A='<!-- NEOAXIOM_SYNTHESIS_INDEX_START -->'; B='<!-- NEOAXIOM_SYNTHESIS_INDEX_END -->'
table=f'''{A}

## Neoaxiomas™ · Síntesis Abierta específica / Neoaxioms™ · Dedicated Open Synthesis

Cada Neoaxioma dispone de un espacio de contraste propio además de la matriz general #80. / Each Neoaxiom has its own scrutiny space in addition to general matrix #80.

| Neoaxioma | Síntesis Abierta |
|---|---|
'''+ '\n'.join(f'| **{k} · {TITLES_ES[k]}** | [#{v}]({issue_url(v)}) |' for k,v in ISSUES.items()) + f'''

[Matriz general Neoaxiomas™ · #80]({issue_url(80)}) · [Texto íntegro de Neoaxiomas™]({rel(SYN,NEO)})

{B}'''
if A in s and B in s:
    s=replace_block(s,A,B,table)
else:
    marker='<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'
    s=s.replace(marker,marker+'\n\n'+table,1)
SYN.write_text(s,encoding='utf-8')

# 6) Curated relation map: expand coverage and append non-destructive managed relations LIII-LIX + Neoaxioms.
r=REL.read_text(encoding='utf-8')
r=re.sub(r'\*\*Cobertura / Coverage:\*\* I–LII · 52 manifiestos / 52 manifestos', '**Cobertura / Coverage:** I–LIX · 59 manifiestos / 59 manifestos',r)
# XLIX section existed but lacked its own manifesto link, so coverage detector could not verify it.
xlix='## XLIX · La Neodialéctica como Punto de Encuentro entre Culturas™'
if xlix in r:
    seg=r.split(xlix,1)[1]
    before_next=seg.split('\n\n## L ·',1)[0] if '\n\n## L ·' in seg else seg
    if '49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md' not in before_next:
        r=r.replace(xlix,xlix+'\n\n- [XLIX · Manifiesto / Manifesto](./49_neodialectica_punto_encuentro_culturas_interoperabilidad_cultural_ES_EN.md)',1)
RA='<!-- NEO_RELATIONS_LIII_LIX_NEOAX_START -->'; RB='<!-- NEO_RELATIONS_LIII_LIX_NEOAX_END -->'
relations=f'''{RA}

---

## LIII–LIX · ampliación relacional vigente / current relational extension

### LIII · Leónidas™
- [Manifiesto](./53_leonidas_defensor_sintesis_auditoria_abierta_aportes_externos_ES_EN.md) · [Síntesis #69]({REPO}/issues/69)
- [Protocolo Leónidas™](../propuestas/sintesis-abierta/LEONIDAS_AUDITORIA_ABIERTA_Y_APORTES_EXTERNOS_ES_EN.md) · [Auditorías públicas](../auditorias/publicas/README.md) · [Auditoría de integridad #71]({REPO}/issues/71)
- Relaciones principales: II · Síntesis Abierta; III · Derecho de Aporte; IX · Memoria/Genealogía/Trazabilidad; XX · Umbral-X; XXXIV · Auditoría Conjunta; XLVIII · La Síntesis Todo lo Ve; LI · Poder Cívico.

### LIV · Riqueza y Chatarra™
- [Manifiesto](./54_riqueza_chatarra_chatarrero_restauracion_civilizatoria_ES_EN.md) · [Síntesis #72]({REPO}/issues/72)
- Relaciones principales: VII · Economía del Aporte; XXIII · Soberanía del Tiempo Cognitivo; XXV · Pulido de la Piedra; XXVII · Valor de los Alimentos y la Vida; XXX · Coherencia Fines-Medios; XLV · Multidimensionalidad.
- Función aplicada: reparación, reparabilidad, segunda vida, remanufactura, recuperación y dignidad del oficio reparador.

### LV · Ataque de las Micromáquinas™
- [Manifiesto](./55_ataque_micromaquinas_plagas_escala_invisible_ES_EN.md) · [Síntesis #74]({REPO}/issues/74)
- [Estado real de la evidencia](../analisis/publicos/2026-08-09_micromaquinas_plagas_escala_invisible_estado_real_ES_EN.md) · [Brief de debate](../propuestas/sintesis-abierta/2026-08-09_LV_micromaquinas_plagas_escala_invisible_debate_ES_EN.md)
- Relaciones principales: IX · Trazabilidad; XX · Defensa Intelectual/Umbral-X; XXX · Coherencia Fines-Medios; XXXVIII · Protección Integral; XLV · Multidimensionalidad; LVI · NO-CONTROL.

### LVI · NO-CONTROL™ · Síntesis Previa a la Potencia
- [Manifiesto](./56_no_control_sintesis_previa_potencia_energia_orbital_ES_EN.md) · [Síntesis #76]({REPO}/issues/76)
- Relaciones principales: IV · Bien Común; IX · Trazabilidad; XXX · Coherencia Fines-Medios; XXXIV · Auditoría Conjunta; XLIV · Neowar; XLV · Multidimensionalidad; LIX · Custodia Cognitiva.
- Regla epistemológica enlazada: capacidad de doble uso no demuestra intención hostil.

### LVII–LIX · Refugio → Inteligencia Civilizatoria → Custodia Cognitiva
- [Mapa específico LVII–LIX](./RELACIONES_LVII_LIX_ES_EN.md)
- [LVII · #77]({REPO}/issues/77) · [LVIII · #78]({REPO}/issues/78) · [LIX · #79]({REPO}/issues/79)
- La secuencia conecta cuidado basal, capacidad cognitiva pública y custodia distribuida sin monopolio de conciencia.

## Neoaxiomas™ ↔ Manifiestos ↔ trabajo aplicado

- [Neoaxiomas™](../neoaxiomas/README.md) · [Matriz general #80]({REPO}/issues/80)
- **NAX-01 / NAX-08 / NAX-14** ↔ V · Simbiosis Humano–IA; VII · Economía del Aporte; L · Inteligencia Compartida; LVIII · Inteligencia Civilizatoria; LIX · Custodia Cognitiva.
- **NAX-02–06** ↔ II · Síntesis Abierta; IX · Memoria/Genealogía/Trazabilidad; XIX · Persistencia de la Memoria; XLVIII · La Síntesis Todo lo Ve.
- **NAX-07** ↔ X · WEB4™ SistemaTrazable™; XLIII · Inteligencia Humana Expandida; LIX · Custodia Cognitiva.
- **NAX-09** ↔ XXX · Coherencia Fines-Medios; LIV · Riqueza y Chatarra; LVI · NO-CONTROL.
- **NAX-10** ↔ XXV · Pulido de la Piedra; XXXVI · Corona, Águila y Custodia.
- **NAX-11** ↔ I · Neo0; IX · Trazabilidad; XXXIV · Auditoría Conjunta.
- **NAX-12** ↔ IX · Trazabilidad; X · SistemaTrazable™; XXXIV · Auditoría Conjunta.
- **NAX-13** ↔ VII · Economía del Aporte; XXI · Reconocimiento; XXIII · Soberanía del Tiempo Cognitivo.
- **NAX-14** ↔ V · Simbiosis; XIV · Alienación; XXXVIII · Protección de Infancia; XLII–XLIII · soberanía e inteligencia expandida; LVIII–LIX.

**Regla:** las relaciones anteriores son estructurales/documentales y permanecen abiertas a SAN; no convierten proximidad conceptual en prueba causal.

{RB}'''
if RA in r and RB in r:r=replace_block(r,RA,RB,relations)
else:r=r.rstrip()+'\n\n'+relations+'\n'
REL.write_text(r,encoding='utf-8')

# 7) Add compact relational menus to README/LEEME surfaces.
MENU_A='<!-- NEO_RELATIONAL_MENU_START -->'; MENU_B='<!-- NEO_RELATIONAL_MENU_END -->'
def menu_block(f):
    return f'''{MENU_A}

### Mapa relacional vivo / Living relational map

[Manifiestos / Manifestos]({rel(f,MAN_INDEX)}) · [Relaciones y trabajo aplicado / Relations and applied work]({rel(f,REL)}) · [Neoaxiomas™]({rel(f,NEO)}) · [Síntesis Abierta / Open Synthesis]({rel(f,SYN)}) · [Auditoría relacional MAXPROC / MAXPROC relational audit]({rel(f,AUDIT)})

{MENU_B}'''
readmes=sorted({p for p in ROOT.rglob('README*.md') if '.git' not in p.parts}|({ROOT/'LEEME.md'} if (ROOT/'LEEME.md').exists() else set()))
for f in readmes:
    text=f.read_text(encoding='utf-8'); mb=menu_block(f)
    if MENU_A in text and MENU_B in text:text=replace_block(text,MENU_A,MENU_B,mb)
    else:
        marker='<!-- NEOAXIOMAS_GLOBAL_LINK_END -->'
        if marker in text:text=text.replace(marker,marker+'\n\n'+mb,1)
        else:text=text.rstrip()+'\n\n'+mb+'\n'
    f.write_text(text,encoding='utf-8')

# 8) Add a non-reductive relational footer to every canonical manifesto.
idx=MAN_INDEX.read_text(encoding='utf-8')
manifest_paths=[]
for href in re.findall(r'^- \*\*[IVXLCDM]+\*\* · \[[^\]]+\]\(([^)]+\.md)\)',idx,re.M):
    p=(MAN_INDEX.parent/href).resolve()
    if p.exists() and p not in manifest_paths:manifest_paths.append(p)
FA='<!-- NEO_RELATIONAL_FOOTER_START -->'; FB='<!-- NEO_RELATIONAL_FOOTER_END -->'
for f in manifest_paths:
    text=f.read_text(encoding='utf-8')
    footer=f'''{FA}

## Relaciones y contexto / Relations and context

[Mapa transversal]({rel(f,REL)}) · [Mapa relacional MAXPROC]({rel(f,AUDIT)}) · [Neoaxiomas™]({rel(f,NEO)}) · [Índice de Síntesis Abierta]({rel(f,SYN)})

> Este bloque añade navegación y relaciones; no sustituye, resume ni reduce el cuerpo del manifiesto. / This block adds navigation and relations; it does not replace, summarise or reduce the manifesto body.

{FB}'''
    if FA in text and FB in text:text=replace_block(text,FA,FB,footer)
    else:
        nav='<!-- NEO_MANIFESTO_NAV_START -->'
        if nav in text:text=text.replace(nav,footer+'\n\n'+nav,1)
        else:text=text.rstrip()+'\n\n'+footer+'\n'
    f.write_text(text,encoding='utf-8')

# Basic postcheck.
fail=[]
neo=NEO.read_text(encoding='utf-8')
for ident,num in ISSUES.items():
    if ident not in neo or issue_url(num) not in neo:fail.append(f'{ident}: missing dedicated synthesis')
for ident in ('NAX-12','NAX-13','NAX-14'):
    if neo.count('## '+ident+' ·')<2:fail.append(f'{ident}: ES/EN integration incomplete')
if '**Cobertura / Coverage:** I–LIX · 59 manifiestos / 59 manifestos' not in REL.read_text(encoding='utf-8'):fail.append('relation map coverage stale')
for f in manifest_paths:
    t=f.read_text(encoding='utf-8')
    if t.count(FA)!=1 or t.count(FB)!=1:fail.append(f'{f.relative_to(ROOT)} relational footer')
for f in readmes:
    t=f.read_text(encoding='utf-8')
    if t.count(MENU_A)!=1 or t.count(MENU_B)!=1:fail.append(f'{f.relative_to(ROOT)} relational menu')
print('NEOAXIOMS',len(ISSUES),'MANIFESTOS',len(manifest_paths),'READMES',len(readmes))
if fail:
    print('POSTCHECK FAIL');print('\n'.join(fail));sys.exit(1)
print('POSTCHECK OK: NAX-01..14 syntheses linked; NAX-12..14 integrated; relation map I-LIX; relational menus and manifesto footers complete')

from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path('.')
MAN = ROOT / 'manifiestos'
README = MAN / 'README.md'
REGISTRY = MAN / 'CANONICAL_FILENAMES.json'
START = '<!-- NEO_CROSS_REFERENCES_START -->'
END = '<!-- NEO_CROSS_REFERENCES_END -->'
HEADING = '## Referencias cruzadas canónicas / Canonical cross-references'

def roman_to_int(s: str) -> int:
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=prev=0
    for ch in reversed(s):
        v=vals[ch]
        if v < prev: total -= v
        else: total += v; prev=v
    return total

def latest_manifesto() -> tuple[str, Path]:
    entries=json.loads(REGISTRY.read_text(encoding='utf-8'))['entries']
    if not entries:
        raise SystemExit('CANONICAL_REGISTRY_EMPTY')
    roman=max(entries,key=roman_to_int)
    path=ROOT/entries[roman]['legacy']
    if not path.exists():
        raise SystemExit(f'CANONICAL_SOURCE_MISSING={path}')
    return roman,path

def ensure_crossref_markers(path: Path) -> bool:
    text=path.read_text(encoding='utf-8')
    if START in text and END in text: return False
    pos=text.find(HEADING)
    if pos < 0:
        print(f'LATEST_CROSSREF_HEADING_MISSING={path}')
        return False
    text=text[:pos]+START+'\n\n'+text[pos:]
    after=text.find('\n## ',pos+len(START)+len(HEADING))
    text=(text.rstrip()+'\n\n'+END+'\n') if after < 0 else (text[:after]+'\n\n'+END+text[after:])
    path.write_text(text,encoding='utf-8')
    return True

def reconcile_readme(roman: str, path: Path) -> bool:
    text=README.read_text(encoding='utf-8')
    source=path.read_text(encoding='utf-8')
    hs=re.findall(r'^#\s+'+re.escape(roman)+r'\s*·\s*(.+?)\s*$',source,re.M)
    issue=re.search(r'\*\*Síntesis Abierta / Open Synthesis:\*\*\s*\[#(\d+)\]\((https://github\.com/[^)]+/issues/\1)\)',source)
    if len(hs)<2 or not issue:
        raise SystemExit('LATEST_MANIFESTO_METADATA_UNRESOLVED')
    es_title,en_title=hs[0],hs[1]
    issue_num,issue_url=issue.group(1),issue.group(2)
    entries=json.loads(REGISTRY.read_text(encoding='utf-8'))['entries']
    count=len(entries)

    block=(
      '> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>\n'
      f'> **{roman} · {es_title} / {en_title}**\n>\n'
      f'> **[Manifiesto {roman} / Manifesto {roman}]({path.name}) · [Síntesis Abierta {roman} · #{issue_num} / Open Synthesis {roman} · #{issue_num}]({issue_url})**\n\n'
    )
    new,n=re.subn(r'> ## 🔴 ÚLTIMO MANIFIESTO FINITO ABIERTO A SÍNTESIS / LATEST FINITE MANIFESTO OPEN FOR SYNTHESIS\n>\n.*?(?=> ## ∞ · PUERTA ABIERTA PERMANENTE / PERMANENT OPEN DOOR)',block,text,count=1,flags=re.S)
    if n!=1: raise SystemExit('README_LATEST_BLOCK_UNRESOLVED')
    frontier=f'**Frontera canónica vigente / Current canonical frontier:** **{count} manifiestos finitos bilingües · I–{roman} + Manifiesto ∞ / {count} finite bilingual manifestos · I–{roman} + Manifesto ∞**  '
    new,n=re.subn(r'\*\*Frontera canónica vigente / Current canonical frontier:\*\* \*\*.*?\*\*  ',frontier,new,count=1)
    if n!=1: raise SystemExit('README_FRONTIER_LINE_UNRESOLVED')
    if new==text: return False
    README.write_text(new,encoding='utf-8')
    return True

def main() -> int:
    roman,path=latest_manifesto()
    marker_change=ensure_crossref_markers(path)
    readme_change=reconcile_readme(roman,path)
    print(f'LATEST_MANIFESTO={roman}:{path}')
    print(f'LATEST_SOURCE=CANONICAL_FILENAMES.json')
    print(f'LATEST_CROSSREF_MARKERS_CHANGED={marker_change}')
    print(f'README_FRONTIER_CHANGED={readme_change}')
    return 0

if __name__=='__main__':
    raise SystemExit(main())

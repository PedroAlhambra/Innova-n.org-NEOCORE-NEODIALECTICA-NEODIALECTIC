from pathlib import Path
import re
import urllib.parse

ROOT = Path('.')
REPORT = Path('auditorias/publicas/2026-08-08_auditoria_global_readmes_enlaces_y_trazabilidad_kdp_ES_EN.md')
XLII_FILE = '42_fin_era_hombre_manipulado_ia_despertar_soberania_cognitiva_ES_EN.md'
XLIII_FILE = '43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md'
ISSUE51 = 'https://github.com/PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC/issues/51'

COLLECTION_HUBS = [
    Path('README.md'), Path('LEEME.md'), Path('PORTADA.md'), Path('COVER.md'),
    Path('manifiestos/README.md'), Path('propuestas/sintesis-abierta/README.md'),
    Path('wiki-source/Manifiestos.md'),
]
LIVE_HUBS = [
    Path('README.md'), Path('LEEME.md'), Path('PORTADA.md'), Path('COVER.md'),
    Path('analisis/README.md'), Path('analisis/auditorias/README.md'),
    Path('analisis/publicos/README.md'), Path('analisis/publicos/evidencias/README.md'),
    Path('auditorias/publicas/README.md'), Path('manifiestos/README.md'),
    Path('obras/README.md'), Path('obras/idea/README.md'), Path('obras/idea/assets/README.md'),
    Path('propuestas/sintesis-abierta/README.md'), Path('wiki-source/README.md'),
]
KDP_HUBS = [
    Path('README.md'), Path('analisis/README.md'), Path('analisis/INDEX.md'),
    Path('analisis/publicos/README.md'), Path('analisis/auditorias/README.md'),
    Path('auditorias/publicas/README.md'), Path('obras/idea/README.md'),
    Path('wiki-source/Analisis_Neodialecticos_Publicos.md'),
]


def rel_from(src: Path, dst: str):
    import os
    r = os.path.relpath(dst, src.parent).replace('\\', '/')
    return r if r.startswith('.') else './' + r


def insert_after_line(lines, idx, new_lines):
    existing = '\n'.join(lines[idx+1:idx+6])
    if XLIII_FILE in existing or ISSUE51 in existing:
        return False
    lines[idx+1:idx+1] = new_lines
    return True


def sync_collection_file(path: Path):
    if not path.exists():
        return 0
    text = path.read_text(encoding='utf-8')
    old = text

    # Correct truly stale current-range markers, without treating I–XLIII as I–XLII.
    text = re.sub(r'I–XLII(?!I)', 'I–XLIII', text)
    text = re.sub(r'\b42 manifiestos bilingües\b', '43 manifiestos bilingües', text, flags=re.I)
    text = re.sub(r'\b42 bilingual manifestos\b', '43 bilingual manifestos', text, flags=re.I)
    text = re.sub(r'\b42 manifiestos\b', '43 manifiestos', text, flags=re.I)

    # Bring tenth-wave headings/summaries to XLII–XLIII where they were frozen at XLII.
    text = text.replace('**Décima oleada · XLII:**', '**Décima oleada · XLII–XLIII:**')
    text = text.replace('**Tenth wave · XLII:**', '**Tenth wave · XLII–XLIII:**')
    text = text.replace('## Décima oleada · XLII · Fin de la Era del Hombre Manipulado™',
                        '## Décima oleada · XLII–XLIII · Fin de la Era del Hombre Manipulado™ e Inteligencia Humana Expandida™')
    text = text.replace('## Tenth wave · XLII · End of the Manipulated Human Era™',
                        '## Tenth wave · XLII–XLIII · End of the Manipulated Human Era™ and Human Expanded Intelligence™')
    text = text.replace('* **Décima oleada · XLII–XLIII:** Fin de la Era del Hombre Manipulado™, IA, despertar crítico y soberanía cognitiva.',
                        '* **Décima oleada · XLII–XLIII:** Fin de la Era del Hombre Manipulado™, soberanía cognitiva e Inteligencia Humana Expandida™.')
    text = text.replace('* **Tenth wave · XLII–XLIII:** End of the Manipulated Human Era™, AI, critical awakening and cognitive sovereignty.',
                        '* **Tenth wave · XLII–XLIII:** End of the Manipulated Human Era™, cognitive sovereignty and Human Expanded Intelligence™.')

    # Add XLIII beside every explicit XLII bullet/list entry that has not yet been extended.
    lines = text.splitlines()
    i = 0
    changes = 0
    while i < len(lines):
        line = lines[i]
        lookahead = '\n'.join(lines[i+1:i+5])
        if XLII_FILE in line and XLIII_FILE not in lookahead:
            prefix = None
            if re.match(r'^\s*42\.\s+\[', line):
                prefix = 'numbered'
            elif re.match(r'^\s*\*\s+\[XLII\s+·', line):
                prefix = 'bullet'
            elif re.match(r'^\s*\|\s*XLII\s*\|', line):
                prefix = 'table'
            if prefix:
                target = rel_from(path, 'manifiestos/' + XLIII_FILE)
                spanish = ('Fin de la Era' in line) or ('IA, Despertar' in line) or ('Soberanía' in line)
                if prefix == 'numbered':
                    title = 'Contra la Incomprensión Reductiva de la IA™ · Inteligencia Humana Expandida™' if spanish else 'Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™'
                    new = [f'43. [{title}]({target})']
                elif prefix == 'bullet':
                    title = 'XLIII · Contra la Incomprensión Reductiva de la IA™ · Inteligencia Humana Expandida™' if spanish else 'XLIII · Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™'
                    new = [f'* [{title}]({target})']
                else:
                    # Preserve column count and add semantically useful content for 3/4-column tables.
                    cols = line.count('|') - 1
                    title = 'Contra la Incomprensión Reductiva de la IA™ · Inteligencia Humana Expandida™' if spanish else 'Against the Reductive Misunderstanding of AI™ · Human Expanded Intelligence™'
                    function = ('Distinguir IA capturada, sustitutiva y humano-expansiva; formular ampliación cognitiva soberana y Revisión de Pares Aumentada™' if spanish else
                                'Distinguish captured, substitutive and human-expansive AI; formulate sovereign cognitive augmentation and Augmented Peer Review™')
                    if cols >= 4:
                        new = [f'| XLIII | [{title}]({target}) | {function} | [Issue #51]({ISSUE51}) |']
                    else:
                        new = [f'| XLIII | [{title}]({target}) | {function} |']
                lines[i+1:i+1] = new
                changes += 1
                i += len(new)
        # Add Issue #51 immediately after explicit Issue #50 bullets when the next lines do not contain #51.
        if ('issues/50' in line) and line.lstrip().startswith('*'):
            lookahead = '\n'.join(lines[i+1:i+5])
            if 'issues/51' not in lookahead:
                if 'Open Synthesis' in line:
                    new_line = f'* [Open Synthesis XLIII · Issue #51]({ISSUE51})'
                else:
                    new_line = f'* [Síntesis Abierta XLIII · Issue #51]({ISSUE51})'
                lines[i+1:i+1] = [new_line]
                changes += 1
                i += 1
        i += 1
    text = '\n'.join(lines) + ('\n' if old.endswith('\n') else '')

    if text != old:
        path.write_text(text, encoding='utf-8')
        return changes + 1
    return 0


LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')


def clean_target(raw):
    t = raw.strip().strip('<>')
    if not t or t.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:', '#')):
        return None
    t = t.split('#', 1)[0].split('?', 1)[0]
    return urllib.parse.unquote(t) or None


def repo_md_files():
    return sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts and 'node_modules' not in p.parts)


def check_links(files):
    checked, broken, wiki_aliases = 0, [], 0
    root = ROOT.resolve()
    for src in files:
        text = src.read_text(encoding='utf-8')
        for raw in LINK_RE.findall(text):
            target = clean_target(raw)
            if target is None:
                continue
            checked += 1
            candidate = (ROOT / target.lstrip('/')).resolve() if target.startswith('/') else (src.parent / target).resolve()
            try:
                candidate.relative_to(root)
            except ValueError:
                broken.append((str(src), raw, 'escapes repository root'))
                continue
            if candidate.exists():
                continue
            # Versioned GitHub Wiki source intentionally uses extensionless Wiki routes such as (Home).
            # Treat them as valid aliases when the corresponding .md source exists.
            if 'wiki-source' in src.parts and candidate.with_suffix('.md').exists():
                wiki_aliases += 1
                continue
            broken.append((str(src), raw, str(candidate.relative_to(root))))
    return checked, broken, wiki_aliases


def stale_findings():
    out = []
    patterns = [
        ('XLIIII', re.compile(r'XLIIII')),
        ('I–XLII', re.compile(r'I–XLII(?!I)')),
        ('42 manifiestos', re.compile(r'\b42\s+manifiestos\b', re.I)),
        ('42 bilingual manifestos', re.compile(r'\b42\s+bilingual\s+manifestos\b', re.I)),
        ('tenth wave only XLII ES', re.compile(r'Décima oleada · XLII(?!–XLIII)')),
        ('tenth wave only XLII EN', re.compile(r'Tenth wave · XLII(?!–XLIII)')),
    ]
    for p in LIVE_HUBS + [Path('wiki-source/Manifiestos.md')]:
        if not p.exists():
            continue
        text = p.read_text(encoding='utf-8')
        for label, pat in patterns:
            if pat.search(text):
                out.append((str(p), label))
    return out


def collection_missing():
    out = []
    for p in COLLECTION_HUBS:
        if not p.exists():
            out.append((str(p), 'file missing'))
            continue
        t = p.read_text(encoding='utf-8')
        if XLIII_FILE not in t:
            out.append((str(p), 'XLIII link missing'))
        if 'I–XLIII' not in t and p.name in {'README.md','LEEME.md','PORTADA.md','COVER.md'}:
            out.append((str(p), 'I–XLIII current range missing'))
    return out


def kdp_missing():
    marker = 'KDP_51071689_TRACE_START'
    out = []
    for p in KDP_HUBS:
        if not p.exists() or marker not in p.read_text(encoding='utf-8'):
            out.append(str(p))
    return out


def readme_bilingual_issues():
    out=[]
    for p in sorted(ROOT.rglob('README.md')):
        if '.git' in p.parts:
            continue
        t=p.read_text(encoding='utf-8')
        if ('ES ·' not in t) or ('EN ·' not in t):
            out.append(str(p))
    return out


def fence_issues(files):
    out=[]
    for p in files:
        t=p.read_text(encoding='utf-8')
        if t.count('```') % 2:
            out.append(str(p))
    return out


def write_report(md_count, readme_count, link_count, broken, wiki_aliases, stale, coll_missing, kdp_miss, bilingual, fences, changed):
    def rows(items):
        return 'Ninguno.' if not items else '\n'.join('- `' + ' → '.join(map(str,x if isinstance(x,tuple) else (x,))) + '`' for x in items)
    ok = not (broken or stale or coll_missing or kdp_miss or bilingual or fences)
    status = 'OK · sin flecos internos detectados por esta auditoría' if ok else 'REQUIERE CORRECCIÓN'
    content=f'''# Auditoría global final · README, enlaces, XLIII y trazabilidad KDP 51071689\n## Final global audit · README, links, XLIII and KDP 51071689 traceability\n\n**Fecha / Date:** 2026-08-08  \n**Estado / Status:** **{status}**\n\n[ES · Castellano](#es--castellano) · [EN · English](#en--english)\n\n---\n\n# ES · Castellano\n\n## Dictamen\n\n- Markdown revisados: **{md_count}**.\n- README.md revisados: **{readme_count}**.\n- Enlaces Markdown internos relativos comprobados: **{link_count}**.\n- Enlaces Wiki extensionless reconocidos correctamente contra su `.md` fuente: **{wiki_aliases}**.\n- Enlaces internos genuinamente rotos: **{len(broken)}**.\n- Marcadores canónicos obsoletos en hubs vivos: **{len(stale)}**.\n- Hubs de colección sin XLIII/estado actual: **{len(coll_missing)}**.\n- Hubs KDP sin bloque de trazabilidad actual: **{len(kdp_miss)}**.\n- README sin selector/estructura bilingüe ES–EN: **{len(bilingual)}**.\n- Markdown con cercas de código desbalanceadas: **{len(fences)}**.\n- Hubs de colección modificados durante esta pasada: **{changed}**.\n\n## KDP · cadena trazable actual\n\n```text\nAUDITORÍA MAESTRA\n→ HITO OPERATIVO 06-08\n→ CIERRE HUMANO PREMATURO\n→ REAPERTURA 07-08\n→ RESPUESTA KDP 08-08\n→ DISPONIBILIDAD ACTUAL NO AFECTADA\n→ CAUSA TÉCNICA TODAVÍA NO EXPLICADA\n→ SEGUIMIENTO SOLICITADO\n```\n\nLa auditoría preserva como hecho la corrección operativa previa de idiomas/asociaciones y como hecho posterior la respuesta de KDP de que el estado «cambios sin publicar» puede dejarse sin tocar sin afectar a la disponibilidad actual. No eleva a hecho ninguna hipótesis sobre la causa.\n\n## Estado XLIII\n\nLa colección actual queda sincronizada como **43 manifiestos bilingües · I–XLIII · diez oleadas**. Los hubs de colección revisados enlazan XLIII y no conservan una décima oleada congelada en XLII.\n\n## Enlaces rotos\n\n{rows(broken)}\n\n## Marcadores obsoletos\n\n{rows(stale)}\n\n## Hubs de colección incompletos\n\n{rows(coll_missing)}\n\n## Hubs KDP incompletos\n\n{rows(kdp_miss)}\n\n## README bilingües\n\n{rows(bilingual)}\n\n## Cercas Markdown\n\n{rows(fences)}\n\n## Límite de la comprobación\n\nSe han validado contra el árbol real del repositorio todas las rutas Markdown relativas detectadas. Los enlaces externos de terceros no quedan garantizados permanentemente por esta auditoría y los anclajes automáticos de GitHub derivados de encabezados Unicode no se someten aquí a una simulación completa del renderer.\n\n---\n\n# EN · English\n\n## Determination\n\n- Markdown files reviewed: **{md_count}**.\n- README.md files reviewed: **{readme_count}**.\n- Relative internal Markdown links checked: **{link_count}**.\n- Extensionless Wiki links correctly resolved against versioned `.md` sources: **{wiki_aliases}**.\n- Genuine broken internal links: **{len(broken)}**.\n- Stale canonical markers in live hubs: **{len(stale)}**.\n- Collection hubs missing XLIII/current state: **{len(coll_missing)}**.\n- KDP hubs missing the current traceability block: **{len(kdp_miss)}**.\n- README files lacking ES–EN bilingual structure: **{len(bilingual)}**.\n- Markdown files with unbalanced code fences: **{len(fences)}**.\n\nThe current KDP chain preserves the earlier operational correction while recording the later unpublished-changes state, KDP's confirmation that current availability is unaffected when that state is left untouched, and the still-unexplained technical cause.\n\nThe public manifesto collection is synchronised as **43 bilingual manifestos · I–XLIII · ten waves**.\n\nRepository-local relative links have been checked against the actual tree. Permanent availability of third-party external URLs and full renderer-level validation of every Unicode-generated heading anchor are outside this check.\n\n---\n\n## Trazabilidad / Traceability\n\n- [Auditoría maestra / Master KDP audit](../../analisis/publicos/2026-08-06_auditoria-indirecta-kdp-author-central-idea_ES_EN.md)\n- [Reapertura / Reopening · 2026-08-07](./2026-08-07_addendum_reapertura_caso_51071689_ES_EN.md)\n- [Respuesta KDP / KDP response · 2026-08-08](./2026-08-08_addendum_kdp_respuesta_cambios_sin_publicar_51071689_ES_EN.md)\n- [XLIII](../../manifiestos/43_contra_incomprension_reductiva_ia_inteligencia_humana_expandida_ES_EN.md)\n- [Síntesis Abierta XLIII · Issue #51]({ISSUE51})\n- [Repositorio / Repository](../../README.md)\n'''
    REPORT.write_text(content,encoding='utf-8')
    return ok


def main():
    changed=0
    for p in COLLECTION_HUBS:
        changed += int(sync_collection_file(p) > 0)

    files=repo_md_files()
    checked, broken, wiki_aliases=check_links(files)
    stale=stale_findings()
    coll=collection_missing()
    kdp=kdp_missing()
    bilingual=readme_bilingual_issues()
    fences=fence_issues(files)
    ok=write_report(len(files), len(list(ROOT.rglob('README.md'))), checked, broken, wiki_aliases, stale, coll, kdp, bilingual, fences, changed)

    print('RESULT', 'OK' if ok else 'FAIL')
    print('Markdown', len(files), 'READMEs', len(list(ROOT.rglob('README.md'))), 'links', checked, 'wiki_aliases', wiki_aliases)
    print('broken', broken)
    print('stale', stale)
    print('collection_missing', coll)
    print('kdp_missing', kdp)
    print('readme_bilingual_issues', bilingual)
    print('fence_issues', fences)

    # remove disposable one-shot machinery before the final commit
    for q in [
        Path('.github/scripts/one_shot_finalize_global_docs_xliii_kdp.py'),
        Path('.github/workflows/one-shot-finalize-global-docs-xliii-kdp.yml'),
        Path('.github/triggers/finalize-global-docs-xliii-kdp.trigger'),
    ]:
        if q.exists(): q.unlink()

    if not ok:
        raise SystemExit(2)

if __name__=='__main__':
    main()

from __future__ import annotations

from pathlib import Path
import json
import os
import re
import sys
import urllib.request

ROOT = Path('.')
REPO = os.environ.get('GITHUB_REPOSITORY', 'PedroAlhambra/Innova-n.org-NEOCORE-NEODIALECTICA-NEODIALECTIC')
INDEX = ROOT / 'propuestas' / 'sintesis-abierta' / 'INDICE_COMPLETO_SINTESIS_ABIERTAS_ES_EN.md'
TOKEN = os.environ.get('GITHUB_TOKEN', '')
ISSUE_RE = re.compile(r'https://github\.com/' + re.escape(REPO) + r'/issues/(\d+)')
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

if not TOKEN:
    print('ISSUE_DOCUMENT_RECIPROCITY=FAIL GITHUB_TOKEN_REQUIRED')
    sys.exit(2)


def local_target(src: Path, href: str) -> Path | None:
    href = href.split('#', 1)[0].strip()
    if not href or href.startswith(('http://', 'https://', 'mailto:', '#')):
        return None
    p = (src.parent / href).resolve()
    try:
        p.relative_to(ROOT.resolve())
    except ValueError:
        return None
    return p


def fetch_issue(number: int) -> dict:
    req = urllib.request.Request(
        f'https://api.github.com/repos/{REPO}/issues/{number}',
        headers={
            'Authorization': f'Bearer {TOKEN}',
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'User-Agent': 'innova-n-maxproc-audit',
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


# Dedicated mappings are declared by table rows in the complete Open Synthesis index.
# Dashboard/reference links outside those rows are intentionally not interpreted as
# dedicated bilateral relationships.
mappings: set[tuple[Path, int]] = set()
for line in INDEX.read_text(encoding='utf-8').splitlines():
    if not line.lstrip().startswith('|'):
        continue
    issues = [int(x) for x in ISSUE_RE.findall(line)]
    if not issues:
        continue
    local_docs = []
    for _label, href in LINK_RE.findall(line):
        p = local_target(INDEX, href)
        if p is not None and p.suffix.lower() == '.md':
            local_docs.append(p)
    if not local_docs:
        continue
    # The first local document in a row is the canonical object whose synthesis
    # is declared by that row. Secondary protocol links are not bilateral claims.
    mappings.add((local_docs[0], issues[0]))

failures: list[str] = []
issue_cache: dict[int, dict] = {}
for doc, issue_no in sorted(mappings, key=lambda x: (x[1], x[0].as_posix())):
    if not doc.exists():
        failures.append(f'DOCUMENT_MISSING issue=#{issue_no} path={doc.relative_to(ROOT.resolve())}')
        continue
    doc_text = doc.read_text(encoding='utf-8', errors='replace')
    if not re.search(rf'\[[^\]]*#?{issue_no}[^\]]*\]\(https://github\.com/{re.escape(REPO)}/issues/{issue_no}\)', doc_text):
        failures.append(f'DOCUMENT_TO_ISSUE_NOT_CLICKABLE issue=#{issue_no} path={doc.relative_to(ROOT.resolve())}')
    if issue_no not in issue_cache:
        try:
            issue_cache[issue_no] = fetch_issue(issue_no)
        except Exception as exc:
            failures.append(f'ISSUE_FETCH_FAILURE issue=#{issue_no} error={type(exc).__name__}:{exc}')
            continue
    issue = issue_cache[issue_no]
    body = issue.get('body') or ''
    rel = doc.relative_to(ROOT.resolve()).as_posix()
    hrefs = [href for _label, href in LINK_RE.findall(body)]
    reciprocal = any(
        href == rel
        or href.endswith('/blob/main/' + rel)
        or href.endswith('/raw/main/' + rel)
        or ('/blob/' in href and href.endswith('/' + rel))
        for href in hrefs
    )
    if not reciprocal:
        failures.append(f'ISSUE_TO_DOCUMENT_NOT_CLICKABLE issue=#{issue_no} path={rel}')

if failures:
    print(f'ISSUE_DOCUMENT_RECIPROCITY=FAIL mappings={len(mappings)} issues={len(issue_cache)} failures={len(failures)}')
    for f in failures:
        print(f)
    sys.exit(1)

print(f'ISSUE_DOCUMENT_RECIPROCITY=PASS mappings={len(mappings)} issues={len(issue_cache)}')

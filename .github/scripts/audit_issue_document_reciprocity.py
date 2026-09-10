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


def github_headers() -> dict[str, str]:
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'innova-n-maxproc-audit',
    }
    if TOKEN:
        headers['Authorization'] = f'Bearer {TOKEN}'
    return headers


def fetch_issue_batch(required: set[int]) -> dict[int, dict]:
    """Fetch public issue metadata in collection pages to avoid one API call per mapping.

    GITHUB_TOKEN is optional for public repositories; CI can still provide it for a
    higher rate limit. Pull requests are ignored even though GitHub's issues
    collection contains them.
    """
    out: dict[int, dict] = {}
    page = 1
    while required - set(out):
        url = f'https://api.github.com/repos/{REPO}/issues?state=all&per_page=100&page={page}'
        req = urllib.request.Request(url, headers=github_headers())
        with urllib.request.urlopen(req, timeout=30) as r:
            items = json.load(r)
        if not items:
            break
        for item in items:
            if 'pull_request' in item:
                continue
            number = item.get('number')
            if number in required:
                out[number] = item
        if len(items) < 100:
            break
        page += 1
    return out


def fetch_repo_comments(required: set[int]) -> dict[int, list[dict]]:
    """Fetch recent repository issue comments in pages, newest first.

    This keeps the reciprocity gate bounded: one collection request usually covers
    all reconciliation comments instead of one request per issue.
    """
    out: dict[int, list[dict]] = {n: [] for n in required}
    page = 1
    while page <= 10:
        url = (
            f'https://api.github.com/repos/{REPO}/issues/comments'
            f'?sort=created&direction=desc&per_page=100&page={page}'
        )
        req = urllib.request.Request(url, headers=github_headers())
        with urllib.request.urlopen(req, timeout=30) as r:
            items = json.load(r)
        if not items:
            break
        for comment in items:
            issue_url = comment.get('issue_url') or ''
            match = re.search(r'/issues/(\d+)$', issue_url)
            if match:
                number = int(match.group(1))
                if number in out:
                    out[number].append(comment)
        # Reconciliation comments are recent; stop once all required issues have
        # at least one comment in the fetched window. Older body links remain
        # handled by the issue collection itself.
        if all(out[n] for n in required):
            break
        if len(items) < 100:
            break
        page += 1
    return out

def body_has_path(text: str, rel: str) -> bool:
    hrefs = [href for _label, href in LINK_RE.findall(text or '')]
    return any(
        href == rel
        or href.endswith('/blob/main/' + rel)
        or href.endswith('/raw/main/' + rel)
        or ('/blob/' in href and href.endswith('/' + rel))
        for href in hrefs
    )


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
required_issues = {issue_no for _doc, issue_no in mappings}
try:
    issue_cache = fetch_issue_batch(required_issues)
except Exception as exc:
    print(f'ISSUE_DOCUMENT_RECIPROCITY=FAIL ISSUE_BATCH_FETCH_FAILURE {type(exc).__name__}:{exc}')
    sys.exit(2)

missing_body_issues: set[int] = set()
for doc, issue_no in mappings:
    issue = issue_cache.get(issue_no)
    if issue is None:
        continue
    rel = doc.relative_to(ROOT.resolve()).as_posix()
    if not body_has_path(issue.get('body') or '', rel):
        missing_body_issues.add(issue_no)
try:
    comment_cache = fetch_repo_comments(missing_body_issues) if missing_body_issues else {}
except Exception as exc:
    # External rate limits are operationally distinct from reciprocity failures.
    print(f'ISSUE_DOCUMENT_RECIPROCITY=EXTERNAL_RATE_LIMIT_OR_FETCH_BLOCK {type(exc).__name__}:{exc}')
    sys.exit(2)

for doc, issue_no in sorted(mappings, key=lambda x: (x[1], x[0].as_posix())):
    if not doc.exists():
        failures.append(f'DOCUMENT_MISSING issue=#{issue_no} path={doc.relative_to(ROOT.resolve())}')
        continue
    doc_text = doc.read_text(encoding='utf-8', errors='replace')
    if not re.search(rf'\[[^\]]*#?{issue_no}[^\]]*\]\(https://github\.com/{re.escape(REPO)}/issues/{issue_no}\)', doc_text):
        failures.append(f'DOCUMENT_TO_ISSUE_NOT_CLICKABLE issue=#{issue_no} path={doc.relative_to(ROOT.resolve())}')
    if issue_no not in issue_cache:
        failures.append(f'ISSUE_FETCH_FAILURE issue=#{issue_no} error=NOT_FOUND_IN_PUBLIC_ISSUE_COLLECTION')
        continue
    issue = issue_cache[issue_no]
    body = issue.get('body') or ''
    rel = doc.relative_to(ROOT.resolve()).as_posix()
    reciprocal = body_has_path(body, rel)
    if not reciprocal:
        comments = comment_cache.get(issue_no, [])
        reciprocal = any(body_has_path(comment.get('body') or '', rel) for comment in comments)
    if not reciprocal:
        failures.append(f'ISSUE_TO_DOCUMENT_NOT_CLICKABLE issue=#{issue_no} path={rel}')

if failures:
    print(f'ISSUE_DOCUMENT_RECIPROCITY=FAIL mappings={len(mappings)} issues={len(issue_cache)} failures={len(failures)}')
    for f in failures:
        print(f)
    sys.exit(1)

print(f'ISSUE_DOCUMENT_RECIPROCITY=PASS mappings={len(mappings)} issues={len(issue_cache)}')

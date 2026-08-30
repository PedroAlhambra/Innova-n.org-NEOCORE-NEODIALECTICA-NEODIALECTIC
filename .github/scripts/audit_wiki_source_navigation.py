from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path('.')
WIKI = ROOT / 'wiki-source'
EXCLUDED = {'README.md', 'DEPLOY_MINIMO.md'}
PAGES = sorted(p for p in WIKI.glob('*.md') if p.name not in EXCLUDED)
PAGE_NAMES = {p.name for p in PAGES}
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
failures: list[str] = []

if 'Home.md' not in PAGE_NAMES or '_Sidebar.md' not in PAGE_NAMES:
    failures.append('WIKI_REQUIRED_ENTRYPOINT_MISSING')

# Wiki-local links such as (Neoaxiomas) resolve to Neoaxiomas.md. Repository links
# and external links are checked by their own corpus gates.
for p in PAGES:
    text = p.read_text(encoding='utf-8', errors='replace')
    if re.search(r'NEOCore™?\s+(?:v)?\d+\.\d+', text, flags=re.I):
        failures.append(f'{p}: WIKI_HARDCODED_CURRENT_VERSION')
    for label, href in LINK_RE.findall(text):
        h = href.split('#', 1)[0].strip()
        if not h or h.startswith(('http://', 'https://', 'mailto:', '/')):
            continue
        # GitHub Wiki uses extensionless page slugs; normal .md links are also accepted.
        candidate = h if h.endswith('.md') else h + '.md'
        candidate = candidate.replace('%20', '_').replace(' ', '_')
        if '/' not in candidate and candidate not in PAGE_NAMES:
            failures.append(f'{p}: WIKI_LOCAL_TARGET_MISSING [{label}]({href}) -> {candidate}')

# Every projected content page must be reachable from the stable navigation graph.
adj: dict[str, set[str]] = {p.name: set() for p in PAGES}
for p in PAGES:
    for _label, href in LINK_RE.findall(p.read_text(encoding='utf-8', errors='replace')):
        h = href.split('#', 1)[0].strip()
        if not h or h.startswith(('http://', 'https://', 'mailto:', '/')) or '/' in h:
            continue
        candidate = h if h.endswith('.md') else h + '.md'
        candidate = candidate.replace('%20', '_').replace(' ', '_')
        if candidate in PAGE_NAMES:
            adj[p.name].add(candidate)

roots = {'Home.md', '_Sidebar.md'} & PAGE_NAMES
seen = set(roots)
stack = list(roots)
while stack:
    cur = stack.pop()
    for nxt in adj.get(cur, ()):
        if nxt not in seen:
            seen.add(nxt)
            stack.append(nxt)
orphans = sorted(PAGE_NAMES - seen)
if orphans:
    failures.append(f'WIKI_ORPHAN_PAGES={orphans}')

if failures:
    print(f'WIKI_SOURCE_NAVIGATION=FAIL pages={len(PAGES)} failures={len(failures)}')
    for item in failures:
        print(item)
    sys.exit(1)

print(f'WIKI_SOURCE_NAVIGATION=PASS pages={len(PAGES)} reachable={len(seen)}')

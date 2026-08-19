from pathlib import Path
import re
import subprocess

# One-shot/idempotent migration for actual NEOCore version identifiers only.
# Date/range strings such as IDEA_1997_2002 must never be rewritten.

DIRECT = {
    'NEOCore™ 7.2 CANON · 7.3-CANDIDATE EN DESARROLLO / IN DEVELOPMENT':
        'NEOCore™ 7.3-CANDIDATE · EN DESARROLLO / IN DEVELOPMENT',
    'NEOCore™ 7.2 CANON': 'NEOCore™ PRE-7.3',
    'NEOCore™ 7.2': 'NEOCore™ PRE-7.3',
    'NEOCore 7.2': 'NEOCore PRE-7.3',
    'NEOCORE 7.2': 'NEOCORE PRE-7.3',
    'NEOCore™ 7_2': 'NEOCore™ PRE-7.3',
    'NEOCore 7_2': 'NEOCore PRE-7.3',
    'NEOCORE_7_2': 'NEOCORE_PRE_7_3',
    'neocore_7_2': 'neocore_PRE_7_3',
    'NEOCORE_72': 'NEOCORE_PRE_73',
    'neocore-72': 'neocore-pre-73',
    'web4_neocore_72': 'web4_neocore_pre73',
}

PATH_VERSION_RE = re.compile(r'(?i)(?:neocore[^/]*7_2|web4[^/]*7_2)')
LINE_CONTEXT_RE = re.compile(
    r'(?i)(neocore|neo core|fijaci[oó]n\s+7\.2|fixation\s+7\.2|'
    r'delta\s+7\.2|versi[oó]n\s+7\.2|version\s+7\.2|7\.2\s+canon)'
)


def tracked_files():
    raw = subprocess.check_output(['git', 'ls-files', '-z'])
    return [Path(p.decode('utf-8')) for p in raw.split(b'\0') if p]


def is_text(path: Path):
    try:
        path.read_text(encoding='utf-8')
        return True
    except Exception:
        return False


def rename_versioned_paths(files):
    renames = {}
    for path in files:
        s = str(path)
        if '7_2' not in s or not PATH_VERSION_RE.search(s):
            continue
        new = s.replace('7_2', 'PRE_7_3')
        Path(new).parent.mkdir(parents=True, exist_ok=True)
        subprocess.check_call(['git', 'mv', s, new])
        renames[s] = new
    return renames


def migrate_text(path: Path, renames):
    if not path.exists() or not is_text(path):
        return False
    text = path.read_text(encoding='utf-8')
    old = text
    for src, dst in renames.items():
        text = text.replace(src, dst)
    for src, dst in DIRECT.items():
        text = text.replace(src, dst)
    out = []
    for line in text.splitlines(keepends=True):
        if '7.2' in line and LINE_CONTEXT_RE.search(line):
            line = re.sub(r'(?i)(fijaci[oó]n|fixation|delta|versi[oó]n|version)\s+7\.2',
                          lambda m: m.group(1) + ' PRE-7.3', line)
            line = re.sub(r'(?i)7\.2\s+CANON', 'PRE-7.3', line)
            line = re.sub(r'(?i)(NEOCore™?|NEOCORE)\s+(?:v)?7\.2', r'\1 PRE-7.3', line)
        out.append(line)
    text = ''.join(out)
    if text != old:
        path.write_text(text, encoding='utf-8')
        return True
    return False


files = tracked_files()
renames = rename_versioned_paths(files)
files = tracked_files()
changed = []
for p in files:
    if migrate_text(p, renames):
        changed.append(str(p))
print(f'NEOCORE_PRE73_RENAMES={len(renames)}')
print(f'NEOCORE_PRE73_TEXT_FILES_CHANGED={len(changed)}')
for src, dst in sorted(renames.items()): print(f'RENAME {src} -> {dst}')
for p in sorted(changed): print(f'EDIT {p}')

from pathlib import Path
import subprocess

# One-shot/idempotent migration: remove living references to the superseded 7.2 label
# while preserving genealogy as PRE-7.3 instead of rewriting unrelated numeric values.

VERSION_MARKERS = (
    'neocore', 'neo core', 'versión', 'version', 'canon', 'fijación', 'fixation',
    'delta', 'review brief', 'postcheck', 'web4', 'candidate', 'candidata'
)

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
    'neocore-72': 'neocore-73-candidate',
}


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
        if '7_2' not in s:
            continue
        new = s.replace('7_2', 'PRE_7_3')
        if new == s:
            continue
        Path(new).parent.mkdir(parents=True, exist_ok=True)
        subprocess.check_call(['git', 'mv', s, new])
        renames[s] = new
    return renames


def migrate_text(path: Path, renames):
    if not path.exists() or not is_text(path):
        return False
    text = path.read_text(encoding='utf-8')
    old = text

    # First update renamed paths everywhere.
    for src, dst in renames.items():
        text = text.replace(src, dst)
        text = text.replace('./' + src, './' + dst)

    # Then update explicit NEOCore/version tokens.
    for src, dst in DIRECT.items():
        text = text.replace(src, dst)

    # Contextual replacement only: avoid touching unrelated decimal values such as measurements.
    out = []
    for line in text.splitlines(keepends=True):
        low = line.lower()
        if '7.2' in line and any(marker in low for marker in VERSION_MARKERS):
            line = line.replace('7.2', 'PRE-7.3')
        if '7_2' in line and any(marker in low for marker in VERSION_MARKERS):
            line = line.replace('7_2', 'PRE_7_3')
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
for src, dst in sorted(renames.items()):
    print(f'RENAME {src} -> {dst}')
for p in sorted(changed):
    print(f'EDIT {p}')

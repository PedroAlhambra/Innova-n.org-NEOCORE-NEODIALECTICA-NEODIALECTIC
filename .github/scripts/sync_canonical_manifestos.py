from pathlib import Path, PurePosixPath
from urllib.parse import unquote
import json
import os
import re

ROOT = Path('.').resolve()
REGISTRY = ROOT / 'manifiestos' / 'CANONICAL_FILENAMES.json'

LINK_RE = re.compile(r'(?P<prefix>!?(?:\[[^\]]*\]))\((?P<target>[^)]+)\)')
TITLE_RE = re.compile(r'^(?P<url>\S+?)(?P<title>\s+["\'][^"\']*["\']\s*)$')


def posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def split_suffix(target: str):
    """Return path part plus untouched ?query/#fragment suffix."""
    cut = len(target)
    for marker in ('?', '#'):
        i = target.find(marker)
        if i != -1:
            cut = min(cut, i)
    return target[:cut], target[cut:]


def relative_href(origin_file: Path, destination: Path) -> str:
    rel = os.path.relpath(destination, origin_file.parent)
    return PurePosixPath(rel).as_posix()


def rewrite_markdown(text: str, source: Path, canonical: Path, legacy_to_canonical: dict[Path, Path]) -> str:
    def repl(match: re.Match) -> str:
        prefix = match.group('prefix')
        raw = match.group('target').strip()
        if not raw:
            return match.group(0)

        angle = raw.startswith('<') and raw.endswith('>')
        core = raw[1:-1].strip() if angle else raw
        title = ''
        tm = TITLE_RE.match(core)
        if tm:
            core = tm.group('url')
            title = tm.group('title')

        low = core.lower()
        if low.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:')) or core.startswith('#'):
            return match.group(0)

        path_part, suffix = split_suffix(core)
        decoded = unquote(path_part)
        if not decoded:
            return match.group(0)

        if decoded.startswith('/'):
            destination = (ROOT / decoded.lstrip('/')).resolve()
        else:
            destination = (source.parent / decoded).resolve()

        try:
            destination.relative_to(ROOT)
        except ValueError:
            return match.group(0)

        destination = legacy_to_canonical.get(destination, destination)
        rewritten = relative_href(canonical, destination) + suffix
        if angle:
            rewritten = f'<{rewritten}>'
        return f'{prefix}({rewritten}{title})'

    return LINK_RE.sub(repl, text)


def main():
    data = json.loads(REGISTRY.read_text(encoding='utf-8'))
    entries = data['entries']

    legacy_to_canonical = {}
    for roman, entry in entries.items():
        legacy = (ROOT / entry['legacy']).resolve()
        canonical = (ROOT / entry['canonical']).resolve()
        legacy_to_canonical[legacy] = canonical

    changed = 0
    generated = 0
    missing = []

    for roman, entry in entries.items():
        legacy = (ROOT / entry['legacy']).resolve()
        canonical = (ROOT / entry['canonical']).resolve()
        if not legacy.exists():
            missing.append((roman, posix(legacy)))
            continue

        source_text = legacy.read_text(encoding='utf-8')
        rendered = rewrite_markdown(source_text, legacy, canonical, legacy_to_canonical)
        canonical.parent.mkdir(parents=True, exist_ok=True)
        generated += 1
        old = canonical.read_text(encoding='utf-8') if canonical.exists() else None
        if old != rendered:
            canonical.write_text(rendered, encoding='utf-8')
            changed += 1

    print(f'CANONICAL_REGISTERED={len(entries)}')
    print(f'CANONICAL_GENERATED={generated}')
    print(f'CANONICAL_CHANGED={changed}')
    print(f'CANONICAL_MISSING_LEGACY={len(missing)}')
    for roman, path in missing:
        print(f'MISSING {roman}: {path}')

    if missing:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
VERSION_README = ROOT / "versiones" / "README.md"

TEXT_SUFFIXES = {".md", ".txt", ".json", ".yml", ".yaml", ".js", ".mjs", ".html", ".css", ".py"}
SKIP_DIRS = {".git", "node_modules", "vendor"}

# Explicit markers that mean the version is material provenance/compatibility,
# not a duplicated CURRENT_VERSION statement.
PROVENANCE_MARKERS = (
    "VERSION_OF_ORIGIN",
    "introduced_in",
    "introduced in",
    "introducido en",
    "compatibility",
    "compatibilidad",
    "snapshot",
    "historical",
    "histórico",
    "history",
    "genealogy",
    "genealogía",
    "base version",
    "versión base",
)


def current_version() -> str:
    text = VERSION_README.read_text(encoding="utf-8")
    m = re.search(r"Current version:\*\*\s*\*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", text)
    if not m:
        m = re.search(r"Versión vigente[^\n]*\*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", text)
    if not m:
        raise SystemExit("Cannot resolve CURRENT_VERSION from versiones/README.md")
    return m.group(1)


def allowed_path(rel: pathlib.Path) -> bool:
    p = rel.as_posix()
    if rel.name.lower() == "readme.md":
        return True
    if p.startswith("versiones/"):
        return True
    return False


def main() -> int:
    version = current_version()
    offenders: list[str] = []

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if allowed_path(rel):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if version not in text:
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            if version not in line:
                continue
            low = line.lower()
            if any(marker.lower() in low for marker in PROVENANCE_MARKERS):
                continue
            offenders.append(f"{rel}:{lineno}: {line.strip()[:220]}")

    print(f"CURRENT_VERSION={version}")
    if offenders:
        print("CURRENT_VERSION_REFERENCE_POLICY = FAIL")
        print("Current version number leaked into intermediate surfaces without provenance/compatibility marker:")
        for item in offenders:
            print(f"- {item}")
        return 1

    print("CURRENT_VERSION_REFERENCE_POLICY = PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

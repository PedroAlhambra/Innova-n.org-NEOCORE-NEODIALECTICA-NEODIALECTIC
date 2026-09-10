#!/usr/bin/env python3
"""Validate live Neoaxiom reading routes without hard-coded frontiers."""
from __future__ import annotations

import re
from pathlib import Path

neo = Path("neoaxiomas")
readme_path = neo / "README.md"
readme = readme_path.read_text(encoding="utf-8")
assert "README = ÍNDICE" in readme
assert "README = INDEX" in readme

canonical = {}
for path in sorted(neo.glob("NAX-*_ES_EN.md")):
    if path.name == "NAX-10_FUEGO_DE_AGUA_TOTALIDAD_ELEMENTAL_ES_EN.md":
        continue
    match = re.match(r"NAX-(\d+)_", path.name)
    if match:
        canonical.setdefault(int(match.group(1)), []).append(path)

ids = sorted(canonical)
expected = list(range(1, max(ids) + 1)) if ids else []
assert ids == expected, f"non-contiguous canonical NAX frontier: {ids}"
for number, paths in canonical.items():
    assert len(paths) == 1, f"NAX-{number}: expected one primary document, found {paths}"
    assert f"(./{paths[0].name})" in readme, f"NAX-{number}: README route missing"

active = []
historical = []
for path in sorted(neo.glob("C-NAX-*_ES_EN.md")):
    match = re.match(r"C-NAX-(\d+)_", path.name)
    if not match:
        continue
    number = int(match.group(1))
    text = path.read_text(encoding="utf-8", errors="replace")
    status = next((line for line in text.splitlines() if line.startswith("**Estado / Status:**")), "")
    is_historical = "HISTÓRICO" in status and f"FIJADO COMO NAX-{number}" in status
    if is_historical:
        historical.append(number)
        targets = canonical.get(number, [])
        assert len(targets) == 1, f"C-NAX-{number}: historical snapshot lacks unique NAX-{number}"
        assert f"./{targets[0].name}" in text, f"C-NAX-{number}: genealogy route to NAX-{number} missing"
    else:
        active.append(number)
        assert f"(./{path.name})" in readme, f"C-NAX-{number}: active README route missing"

print(
    f"NEOAXIOM_READING_ROUTES=PASS canonical={len(ids)} "
    f"historical_candidates={historical} active_candidates={active}"
)

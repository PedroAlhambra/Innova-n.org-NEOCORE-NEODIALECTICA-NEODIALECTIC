#!/usr/bin/env python3
"""Check added lines for accidental trailing whitespace.

Markdown hard breaks (exactly two ASCII spaces at EOL on a non-blank
line) are valid. Other trailing spaces/tabs remain failures.
"""
from __future__ import annotations

import re
import subprocess
import sys

base = sys.argv[1] if len(sys.argv) > 1 else "HEAD^"
proc = subprocess.run(
    ["git", "diff", "--unified=0", "--no-color", base, "HEAD"],
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
if proc.returncode:
    sys.stderr.write(proc.stderr)
    raise SystemExit(proc.returncode)

current = None
bad = []
for raw in proc.stdout.splitlines():
    if raw.startswith("+++ b/"):
        current = raw[6:]
        continue
    if not current or not raw.startswith("+") or raw.startswith("+++"):
        continue
    line = raw[1:]
    match = re.search(r"[ \t]+$", line)
    if not match:
        continue
    whitespace = match.group(0)
    markdown_hardbreak = (
        current.lower().endswith((".md", ".markdown"))
        and whitespace == "  "
        and bool(line[:-2].strip())
    )
    if not markdown_hardbreak:
        bad.append((current, repr(whitespace)))

if bad:
    print("DIFF_INTEGRITY_FAILURE: accidental trailing whitespace", file=sys.stderr)
    for path, whitespace in bad[:100]:
        print(f"- {path}: trailing={whitespace}", file=sys.stderr)
    raise SystemExit(1)

print("DIFF_INTEGRITY_MARKDOWN=PASS")
"""Fail-closed compatibility gate for the document-based Neoaxiom corpus.

The historical implementation rewrote neoaxiomas/README.md as a monolith. The
README is now only the navigation index, so automated symmetry work must happen
inside each NAX/C-NAX document and may never reconstruct formulations in README.
"""

from pathlib import Path
import subprocess
import sys


root = Path('.').resolve()
readme = (root / 'neoaxiomas/README.md').read_text(encoding='utf-8')
if 'README = ÍNDICE' not in readme or 'README = INDEX' not in readme:
    raise SystemExit('NEOAXIOM_MONOLITH_FAILURE: document-based index contract missing; refusing rewrite')

subprocess.run(
    [sys.executable, str(root / '.github/scripts/audit_neoaxiom_registry_integrity.py')],
    check=True,
)
print('NEOAXIOM_STRICT_BILINGUAL_SYMMETRY document_mode=verified changed=0')

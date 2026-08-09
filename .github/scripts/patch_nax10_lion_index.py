from pathlib import Path
import re,sys
p=Path('neoaxiomas/README.md')
t=p.read_text(encoding='utf-8')
old=t
t=t.replace('├── NAX-10 · ÁGUILA · CORONA · TIERRA · TORRE · PIEDRA','├── NAX-10 · ÁGUILA · CORONA · TIERRA · TORRE · PIEDRA · LEÓN')
t=t.replace('| **NAX-10 · Gramática Arquetípica de Custodia™** | [#93]', '| **NAX-10 · Gramática Arquetípica de Custodia™ — Águila, Corona, Tierra, Torre, Piedra y León** | [#93]')
if t==old: raise SystemExit('no NAX-10 index changes applied')
if 'PIEDRA · LEÓN' not in t or 'Piedra y León** | [#93]' not in t: raise SystemExit('NAX-10 lion index validation failed')
p.write_text(t,encoding='utf-8')
print('NAX-10 INDEX OK: Lion included in topology and synthesis index')

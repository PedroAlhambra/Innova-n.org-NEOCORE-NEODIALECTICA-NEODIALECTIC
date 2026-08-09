from pathlib import Path
p=Path('analisis/publicos/2026-08-09_delta_manifestacion_sistemica_necesidad_neo0_idea_custodia_cognitiva_ES_EN.md')
s=p.read_text(encoding='utf-8')
old='33_idea_piedra_angular_rosetta_civilizatoria_reset_reemplazo_ES_EN.md'
new='33_idea_piedra_angular_roseta_civilizatoria_reset_reemplazo_ES_EN.md'
if old in s:
    p.write_text(s.replace(old,new),encoding='utf-8')
    print('REPAIRED')
else:
    print('NO_CHANGE')

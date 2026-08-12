from pathlib import Path

p=Path('.github/scripts/audit_global_bilingual_symmetry.py')
text=p.read_text(encoding='utf-8')
old=text

text=text.replace("""ES_PATTERNS = [
    r'^#\\s+ES\\s+·\\s+(?:Castellano|Español)\\s*$',
    r'^##\\s+ES\\s+·\\s+(?:Castellano|Español)\\s*$',
]
EN_PATTERNS = [
    r'^#\\s+EN\\s+·\\s+English\\s*$',
    r'^##\\s+EN\\s+·\\s+English\\s*$',
]
""","""# Recognise every explicit language gate, not only one house spelling.
# Examples: ES · Castellano, ES · Versión española, EN · English version,
# EN · Short assessment. A gate must begin with ES/EN; bilingual headings are not gates.
ES_PATTERNS = [r'^#{1,4}\\s+ES\\s+·\\s+[^\\n]+$']
EN_PATTERNS = [r'^#{1,4}\\s+EN\\s+·\\s+[^\\n]+$']
""")

# Make strict list/quote/table/code parity non-negotiable and paragraph parity exact.
text=text.replace("""            # Paragraph segmentation may vary by one for language grammar; larger differences
            # are treated as compression until manually reviewed.
            if abs(ash['paragraphs']-bsh['paragraphs']) > 1:
                problems.append(f'{ident}: párrafos ES={ash[\"paragraphs\"]} EN={bsh[\"paragraphs\"]}')
""","""            # Strict editorial symmetry: paragraph/block count is also part of the representation.
            # Translation may change word count, never the documentary granularity without review.
            if ash['paragraphs'] != bsh['paragraphs']:
                problems.append(f'{ident}: párrafos ES={ash[\"paragraphs\"]} EN={bsh[\"paragraphs\"]}')
""")

# Expand Issue-form visible-string audit beyond name/description/label.
text=text.replace("""    for m in re.finditer(r'^\\s*(name|description|label):\\s*[\"\\']?(.+?)[\"\\']?\\s*$',text,re.M):
        val=m.group(2).strip()
        if len(val)<3 or val.startswith('http'): continue
        if ' / ' not in val and not ('ES' in val and 'EN' in val):
            misses.append(f'{m.group(1)}={val[:90]}')
""","""    # Every visible scalar in a GitHub form must be bilingual. Technical IDs, URLs and
    # validation booleans are not user-visible copy.
    for m in re.finditer(r'^\\s*(name|description|label|placeholder|title):\\s*[\"\\']?(.+?)[\"\\']?\\s*$',text,re.M):
        key,val=m.group(1),m.group(2).strip()
        if len(val)<3 or val.startswith('http') or val in ('[]','{}'): continue
        if ' / ' not in val and ' · ' not in val and not ('ES' in val and 'EN' in val):
            misses.append(f'{key}={val[:90]}')
    # Dropdown and checkbox option labels are visible too. Require an explicit bilingual separator.
    for m in re.finditer(r'^\\s*-\\s+(?:label:\\s*)?[\"\\']?([^\\n\"\\']+?)[\"\\']?\\s*$',text,re.M):
        val=m.group(1).strip()
        if not val or val in ('type: markdown','type: input','type: textarea','type: dropdown','type: checkboxes'): continue
        if val.startswith('type:') or val.startswith('id:') or val.startswith('required:'): continue
        if ' / ' not in val and ' · ' not in val:
            misses.append(f'option={val[:90]}')
""")

if text==old:
    raise SystemExit('No auditor hardening changes found; inspect source drift.')
p.write_text(text,encoding='utf-8')
print('GLOBAL_SYMMETRY_AUDITOR_HARDENED=1')

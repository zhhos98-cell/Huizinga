from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "Malinowski could revisit living relations; Huizinga moved through notes, memory, cards, reproductions and surviving texts."
new = "Malinowski’s published ethnography rested on observation of living relations; Huizinga moved through notes, memory, cards, reproductions and surviving texts."
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

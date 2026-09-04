from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "Malinowski’s ethnography supplied relations; Huizinga tested their historical reach.[^17]"
new = "Malinowski’s ethnography did not supply the relational vocabulary from scratch. It bound older historical objects—generosity, friendship and the efficacy of words—to observed circuits of reciprocity, obligation, trust and exchange; Huizinga tested that denser configuration’s historical reach.[^17]"
if text.count(old) != 1:
    raise SystemExit(f'expected exactly one anchor, found {text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

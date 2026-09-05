from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "At Harvard his route crossed Malinowski’s: Malinowski was himself in the United States on a Rockefeller-supported visit, and his report places Huizinga in a seminar on ‘the functional view of Anthropology’.[^2]"
new = "At Harvard his route crossed Malinowski’s: Malinowski was himself in the United States on a Rockefeller-supported visit, and his report places Huizinga in a Harvard seminar where discussions similar to Malinowski’s theoretical programme were repeated.[^2]"
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

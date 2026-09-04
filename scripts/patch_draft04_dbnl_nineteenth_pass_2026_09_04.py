from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "On 7 April 1926, only days before his transatlantic crossing—and six days before a surviving letter places him aboard the *Berengaria*—[^25] he attacked *evolutie*"
new = "On 7 April 1926, only days before his transatlantic crossing—and six days before a surviving letter places him aboard the *Berengaria*[^25]—he attacked *evolutie*"
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

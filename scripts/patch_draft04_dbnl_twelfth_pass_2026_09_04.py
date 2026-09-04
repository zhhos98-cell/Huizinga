from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "On 7 April 1926, roughly a week before his 13/14 April departure for America, he attacked *evolutie* as a general historical principle, defined cultural history as social morphology concerned with what connects people to one another rather than with what holds them together internally, and placed ethnology among the special cultural sciences already practising such morphology (Huizinga, 1927: 5–7)."
new = "On 7 April 1926, only days before his transatlantic crossing—and six days before a surviving letter places him aboard the *Berengaria*—he attacked *evolutie* as a general historical principle, defined cultural history as social morphology concerned with what connects people to one another rather than with what holds them together internally, and placed ethnology among the special cultural sciences already practising such morphology (Huizinga, 1927: 5–7)."
if text.count(old) != 1:
    raise SystemExit(f'expected exactly one anchor, found {text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

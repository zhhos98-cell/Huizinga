from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "The 1927 imprint in a December 1926 letter is unresolved; the physical presentation copy would be needed to decide how the book circulated before its title-page year."
new = "A production-history control sharpens the anomaly: on 19 February 1926 Malinowski told the Frazers that *Sex & Repression* ‘will be published soon’ (Trinity College Cambridge, Frazer Papers, FRAZ/2/139), while the standard edition’s preface is dated February 1927. Huizinga’s December object may therefore have been a pre-final state; only the physical copy or publisher records can decide its exact state."
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

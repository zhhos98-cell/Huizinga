from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "On 7 April 1926, only days before his transatlantic crossing—and six days before a surviving letter places him aboard the *Berengaria*—he attacked *evolutie* as a general historical principle,"
new = "On 7 April 1926, only days before his transatlantic crossing—and six days before a surviving letter places him aboard the *Berengaria*—[^25] he attacked *evolutie* as a general historical principle,"
if text.count(old) != 1:
    raise SystemExit(f'body anchor count={text.count(old)}')
text = text.replace(old, new, 1)

anchor = "[^24]: Johan Huizinga, *Herfsttij der Middeleeuwen* (Haarlem: H.D. Tjeenk Willink & Zoon, 1919)."
pos = text.find(anchor)
if pos == -1:
    raise SystemExit('note 24 anchor not found')
# Insert note 25 after the full note-24 paragraph.
end = text.find('\n\n', pos)
if end == -1:
    raise SystemExit('note 24 paragraph end not found')
note = "\n\n[^25]: Johan Huizinga (aboard R.M.S. *Berengaria*) to his son Jakob Huizinga, 13 April 1926, *Briefwisseling* II, letter [633]. Huizinga says that since the previous day the ship had been meeting a head-on storm. This establishes that he was already on the transatlantic passage by 13 April; it is not used to infer an exact European embarkation date."
text = text[:end] + note + text[end:]
path.write_text(text, encoding='utf-8')

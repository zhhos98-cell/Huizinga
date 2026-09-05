#!/usr/bin/env python3
from pathlib import Path

P = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
s = P.read_text(encoding='utf-8')

old = "The distinction is revealing. ‘Origins of culture’ retained an older promise attached to *primitive*: living difference could offer access to beginnings. ‘Historical use’ valued Malinowski after that shortcut had been loosened. Relations observed in the Trobriands could become useful to history without requiring the Trobrianders to stand simply as Europe’s past. In the same letter Huizinga resisted one Freudian argument by invoking ‘the immense complexity of the smallest social phenomenon’."
new = "The distinction is revealing. ‘Origins of culture’ retained an older promise attached to *primitive*: living difference could offer access to beginnings. ‘Historical use’ valued Malinowski after that shortcut had been loosened. Relations observed in the Trobriands could become useful to history without requiring the Trobrianders to stand simply as Europe’s past. The same year, the third edition of *Mensch en menigte in Amerika* described modern urban revivalism as `het voortleven van een primitieve geesteshouding in een economisch hoog ontwikkeld milieu` and compared its credulity and excitability with the medieval popular mind.[^23] Here *primitive* marked persistence inside modernity rather than the first position in a sequence. In the same letter Huizinga resisted one Freudian argument by invoking ‘the immense complexity of the smallest social phenomenon’."
if s.count(old) != 1:
    raise SystemExit(f'expected one March 1928 anchor, found {s.count(old)}')
s = s.replace(old, new, 1)

if '[^23]:' in s:
    raise SystemExit('note [^23] already exists')
ref_anchor = '\n## References\n'
note = "\n[^23]: Johan Huizinga, *Mensch en menigte in Amerika. Vier essays over moderne beschavingsgeschiedenis*, 3rd ed. (Haarlem: H.D. Tjeenk Willink & Zoon, 1928), *Verzamelde Werken* V, DBNL TEI `sources/dbnl/verzamelde_werken/huiz003verz06_01.xml`, pp. 387–389. The DBNL text preserves Huizinga’s January 1928 preface, which states that the book was written in 1918, revised in 1920, and revised again for the third edition. In `Tam en wild Amerika`, after discussing contemporary revivalism, he writes: `Het is het voortleven van een primitieve geesteshouding in een economisch hoog ontwikkeld milieu`, immediately comparing traits of contemporary America with the medieval popular mind.\n"
if s.count(ref_anchor) != 1:
    raise SystemExit(f'expected one References anchor, found {s.count(ref_anchor)}')
s = s.replace(ref_anchor, note + ref_anchor, 1)

P.write_text(s, encoding='utf-8')
print('patched Draft 04: 1928 primitive-within-modernity counterevidence + note 23')

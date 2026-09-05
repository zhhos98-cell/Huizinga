#!/usr/bin/env python3
from pathlib import Path

P = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
s = P.read_text(encoding='utf-8')

old_sentence = "Malinowski’s functional language entered precisely where the temporal label ceased to be sufficient: between locating a form and explaining the relations through which it worked."
new_sentence = "The functional language Huizinga encountered in America, Malinowski’s included, entered precisely where the temporal label ceased to be sufficient: between locating a form and explaining the relations through which it worked."
if s.count(old_sentence) != 1:
    raise SystemExit(f'expected exactly one functional-language sentence, found {s.count(old_sentence)}')
s = s.replace(old_sentence, new_sentence, 1)

anchor = "The remark fixes a personal and comparative judgment before the surviving exchange of books: Huizinga had heard Malinowski in an American setting, continued to think about him after leaving Harvard, and was already placing resemblance beside difference.\n\nHistories of interwar anthropology place such encounters inside foundation patronage, where anthropologists had to articulate the distinctiveness of their objects and methods (Biehn, 2009). Five years later Malinowski would ask what could make Leiden’s resources anthropology."
insert = "The remark fixes a personal and comparative judgment before the surviving exchange of books: Huizinga had heard Malinowski in an American setting, continued to think about him after leaving Harvard, and was already placing resemblance beside difference.\n\nHuizinga’s own American notes place the functional vocabulary in a wider setting. In *Amerika levend en denkend*, internally dated October 1926 and published the following year, he described American social science as pluralist and hostile to a single explanatory ground. Summarizing Dewey, he wrote that all action was *interactie, wederzijdsche handeling* and that morality, economic life and scientific thought were *sociale functies*; at the same time he resisted making history mere *hand- en spandiensten* for sociology.[^22] By December, *functional* already belonged to a broader American repertoire; the pair exchange attached it to particular ethnological books and to Huizinga’s historical problems.\n\nHistories of interwar anthropology place such encounters inside foundation patronage, where anthropologists had to articulate the distinctiveness of their objects and methods (Biehn, 2009). Five years later Malinowski would ask what could make Leiden’s resources anthropology."
if s.count(anchor) != 1:
    raise SystemExit(f'expected exactly one America insertion anchor, found {s.count(anchor)}')
s = s.replace(anchor, insert, 1)

ref_anchor = "\n## References\n"
note = "\n[^22]: Johan Huizinga, *Amerika levend en denkend. Losse opmerkingen*, internally dated `19261000` in DBNL and published by H.D. Tjeenk Willink & Zoon, Haarlem, 1927; *Verzamelde Werken* V, DBNL TEI `sources/dbnl/verzamelde_werken/huiz003verz06_01.xml`, especially pp. 445, 448–451. In ‘Geestelijke wachtwoorden’ Huizinga says the purpose of his American journey brought him into close contact with economics, political science, sociology, cultural anthropology and psychology. In ‘De wetenschap der samenleving’ he describes American social science as pluralist, rejects `één enkelen verklaringsgrond`, summarizes Dewey’s `interactie, wederzijdsche handeling`, calls morality, economic life and scientific thought `sociale functies`, and resists making history `hand- en spandiensten` for sociology.\n"
if '[^22]:' in s:
    raise SystemExit('note [^22] already exists')
if s.count(ref_anchor) != 1:
    raise SystemExit(f'expected exactly one References anchor, found {s.count(ref_anchor)}')
s = s.replace(ref_anchor, note + ref_anchor, 1)

P.write_text(s, encoding='utf-8')
print('patched Draft 04: wider American functional repertoire + note 22')

#!/usr/bin/env python3
from pathlib import Path

PATH = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = PATH.read_text(encoding='utf-8')

old_leiden = """The memorandum did not begin its life when Huizinga sent it abroad. On 17 July Van Vollenhoven told him that the paper had already been shown locally, including to Van Eerde, and revised; Snouck Hurgronje was proposed as another reader.[^12] The object that reached Malinowski was therefore already a Leiden composite, altered by local circulation before it entered the Huizinga–Malinowski correspondence. That chronology matters because the classificatory language in the packet was not merely an eccentric private vocabulary. It belonged to a practical attempt to gather existing museums, institutes, languages and colonial expertises into an institution.
"""
new_leiden = old_leiden + """
Huizinga had already put part of that institutional map into print. In June 1929, discussing university ‘role division’, he reproduced the claim that Leiden’s chairs in Indonesian languages and in *land- en volkenkunde van Nederlandsch Indië* were ‘een privilege der Leidsche Universiteit’, explicitly linked to the university’s collections and chairs in colonial law.[^20]
"""

old_coda = """Later that year, in his rectoral address *Over de grenzen van spel en ernst in de cultuur*, Huizinga moved from the Trobriand Kula exchange—circulation, prestige, trust, generosity—to Mauss’s potlatch and then to Philip the Good’s 1454 Burgundian *Vœu du Faisan*, ‘not so very far’ from a potlatch. Semitic and Sanskrit play vocabulary returned; Genoa and Antwerp brought wagering and calculation (Huizinga, 1933). The comparison remained heterogeneous: Kula remained Kula, Burgundy remained Burgundy, and the old philologist remained inside the historian.
"""
new_coda = """Later that year, in his rectoral address *Over de grenzen van spel en ernst in de cultuur*, Huizinga moved from the Trobriand Kula exchange to Mauss’s potlatch and then to Philip the Good’s 1454 Burgundian *Vœu du Faisan*. The published text makes the bridge narrower than a stack of parallels. Huizinga said he was adding the Burgundian case not for its ‘play-character in general’ but as a specific example of *wedijverend, wederkeerig weeldevertoon en spilziek onthaal*: a sequence of court banquets in which hosts took turns, passed a wreath, escalated splendour, and were finally outdone by Philip. Only after specifying that sequence did he call the case ‘not so very far’ from a potlatch.[^21] Semitic and Sanskrit play vocabulary then returned; Genoa and Antwerp brought wagering and calculation. The comparison remained heterogeneous: Kula remained Kula, Burgundy remained Burgundy, and the old philologist remained inside the historian.
"""

if text.count(old_leiden) != 1:
    raise SystemExit(f'Leiden anchor count={text.count(old_leiden)}; refusing patch')
if text.count(old_coda) != 1:
    raise SystemExit(f'Coda anchor count={text.count(old_coda)}; refusing patch')
if '[^20]:' in text or '[^21]:' in text:
    raise SystemExit('Footnotes 20/21 already exist; refusing duplicate patch')

text = text.replace(old_leiden, new_leiden, 1)
text = text.replace(old_coda, new_coda, 1)

notes = """
[^20]: Johan Huizinga, ‘Het sprookje van de rolverdeeling’, *De Gids* 93, no. 6 (June 1929), reprinted in *Verzamelde Werken* VII, p. 404; DBNL TEI `sources/dbnl/verzamelde_werken/huiz003verz08_01.xml`. Huizinga reproduces the 1924 role-division formulation that the Leiden chairs in Indonesian languages and in `land- en volkenkunde van Nederlandsch Indië` were ‘een privilege der Leidsche Universiteit’, linked to Leiden’s collections and chairs in colonial law.

[^21]: Johan Huizinga, *Over de grenzen van spel en ernst in de cultuur* (1933), reprinted in *Verzamelde Werken* V, pp. 18–20; DBNL TEI `sources/dbnl/verzamelde_werken/huiz003verz06_01.xml`, checked against `corrections/chunk_067_manual_round2b.json`. Before comparing the *Vœu du Faisan* to potlatch, Huizinga says he introduces it ‘Niet om zijn spelkarakter in het algemeen, maar als specifiek voorbeeld van wedijverend, wederkeerig weeldevertoon en spilziek onthaal’ and then reconstructs the sequence of Burgundian banquets.

"""
marker = '\n## References\n'
if text.count(marker) != 1:
    raise SystemExit(f'References marker count={text.count(marker)}; refusing patch')
text = text.replace(marker, '\n' + notes + '## References\n', 1)

PATH.write_text(text, encoding='utf-8')
print('patched Draft 04: Leiden 1929 prehistory + 1933 mechanism-first comparison + notes 20/21')

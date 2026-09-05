#!/usr/bin/env python3
from pathlib import Path

P = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
s = P.read_text(encoding='utf-8')

old = "In 1921, reviewing Wells’s attempt to extend world history from planetary and biological development into human history, Huizinga objected that geological or biological *ontwikkeling* had little to do with ‘de functie van het historisch begrijpen’; a wider chronology did not by itself yield historical understanding (Huizinga, 1921). On 7 April 1926, roughly a week before his 13/14 April departure for America, he attacked *evolutie* as a general historical principle, defined cultural history as social morphology concerned with what connects people to one another rather than with what holds them together internally, and placed ethnology among the special cultural sciences already practising such morphology (Huizinga, 1927: 5–7). His Indian papers also used *primitief* for earlier intellectual or medical layers.[^3]"
new = "In 1921, reviewing Wells’s attempt to extend world history from planetary and biological development into human history, Huizinga objected that geological or biological *ontwikkeling* had little to do with ‘de functie van het historisch begrijpen’; a wider chronology did not by itself yield historical understanding (Huizinga, 1921). On 7 April 1926, roughly a week before his 13/14 April departure for America, he attacked *evolutie* as a general historical principle, defined cultural history as social morphology concerned with what connects people to one another rather than with what holds them together internally, and placed ethnology among the special cultural sciences already practising such morphology (Huizinga, 1927: 5–7). More directly, the 1919 first edition of *Herfsttij* had called symbolic thought, from an ethnological standpoint, `een zeer primitieve geestesfunctie` and linked *het primitieve denken* to medieval symbolism.[^24] His Indian papers also used *primitief* for earlier intellectual or medical layers.[^3]"
if s.count(old) != 1:
    raise SystemExit(f'expected exactly one America baseline sequence, found {s.count(old)}')
s = s.replace(old, new, 1)

if '[^24]:' in s:
    raise SystemExit('note [^24] already exists')
ref_anchor = '\n## References\n'
note = "\n[^24]: Johan Huizinga, *Herfsttij der Middeleeuwen* (Haarlem: H.D. Tjeenk Willink & Zoon, 1919), chapter on symbolism. The wording `van ethnologisch gezichtspunt ... een zeer primitieve geestesfunctie` and the following account of `het primitieve denken` are present in the 1919 first-edition scan (verified against Dutch Wikisource, scan p. 182) as well as the later collected-works text, DBNL TEI `sources/dbnl/verzamelde_werken/huiz003verz04_01.xml`, p. 247. This occurrence is used only as a pre-contact history of the category, not as an analogy between late-medieval civilization and the later history of *primitive*.\n"
if s.count(ref_anchor) != 1:
    raise SystemExit(f'expected one References anchor, found {s.count(ref_anchor)}')
s = s.replace(ref_anchor, note + ref_anchor, 1)

P.write_text(s, encoding='utf-8')
print('patched Draft 04: added first-edition Herfsttij primitive baseline + note 24')

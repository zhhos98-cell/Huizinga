#!/usr/bin/env python3
from pathlib import Path

P = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
s = P.read_text(encoding='utf-8')

old = "In contemporary texts, he had already distinguished geological or biological *ontwikkeling* from ‘de functie van het historisch begrijpen’ in 1921, testing historical schemes by what they allowed one to understand rather than by chronology alone (Huizinga, 1921)."
new = "In 1921, reviewing Wells’s attempt to extend world history from planetary and biological development into human history, Huizinga objected that geological or biological *ontwikkeling* had little to do with ‘de functie van het historisch begrijpen’; a wider chronology did not by itself yield historical understanding (Huizinga, 1921)."

if s.count(old) != 1:
    raise SystemExit(f'expected exactly one 1921 Wells sentence, found {s.count(old)}')
s = s.replace(old, new, 1)
P.write_text(s, encoding='utf-8')
print('patched Draft 04: calibrated 1921 Wells/world-history sentence')

#!/usr/bin/env python3
from pathlib import Path

P = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
s = P.read_text(encoding='utf-8')

old = "In the same essay he divided the labour more exactly: ethnology and related sciences could define recurrent forms, while cultural history followed their changing operation in historical events; the boundary was crossed from both sides and retained its significance. Cultural history could learn from ‘de praktische sociologie der Amerikanen’ and from Mauss without becoming subordinate labour for sociology (Huizinga, 1929)."
new = "In the same essay he made the division concrete: religious studies and ethnology could define forms such as myth, consecration, sacred action, contest-play and secret association, while cultural history followed their *werking* in historical events. Service, honour, loyalty and obedience might each be objects of sociology, but their systematic treatment remained insufficient unless cultural history showed their changing operation and form across centuries and countries. Cultural history could learn from ‘de praktische sociologie der Amerikanen’ and from Mauss without becoming subordinate labour for sociology (Huizinga, 1929)."
if s.count(old) != 1:
    raise SystemExit(f'expected exactly one 1929 method sentence cluster, found {s.count(old)}')
s = s.replace(old, new, 1)
P.write_text(s, encoding='utf-8')
print('patched Draft 04: calibrated 1929 relation-functions method sequence')

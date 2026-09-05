#!/usr/bin/env python3
from pathlib import Path

P = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
s = P.read_text(encoding='utf-8')

old = "Late 1933 adds another route, this time returning explicitly to *primitive*. On 27 October Huizinga wrote Malinowski that he had come across a review of Sjoerd Hofstra’s *Differenzierungserscheinungen in einigen afrikanischen Gruppen: Ein Beitrag zur Frage der primitiven Individualität*; Malinowski replied three days later.[^19] On 6 November Huizinga cited Hofstra’s book in an Amsterdam lecture on Renaissance and ‘new time’. The passage concerned W. C. Willoughby’s account of a prophet among *natuurvolken* calling people to return to old loyalties because the ideal age lay in the past (Huizinga, 1934). Here an ethnographic example entered an argument about historical return. The people described as primitive did not have to stand simply as Europe’s past; the example supplied a relation to the past."
new = "Late 1933 adds another route, this time returning explicitly to *primitive*. On 27 October Huizinga wrote Malinowski that he had come across a review of Sjoerd Hofstra’s *Differenzierungserscheinungen in einigen afrikanischen Gruppen: Ein Beitrag zur Frage der primitiven Individualität*; Malinowski replied three days later.[^19] On 6 November, in an Amsterdam lecture on Renaissance and ‘new time’, Huizinga wrote that when humanity means the future it often cries ‘back’, then footnoted Hofstra’s citation of W. C. Willoughby’s prophet among *natuurvolken* calling people to return to old loyalties because the ideal age lay in the past (Huizinga, 1934). The ethnographic example supplied a relation—return to an idealized past—to a general historical claim. The people described as primitive did not have to stand simply as Europe’s past."
if s.count(old) != 1:
    raise SystemExit(f'expected exactly one Hofstra paragraph, found {s.count(old)}')
s = s.replace(old, new, 1)
P.write_text(s, encoding='utf-8')
print('patched Draft 04: calibrated Hofstra footnote relation-first structure')

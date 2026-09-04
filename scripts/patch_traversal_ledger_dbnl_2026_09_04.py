#!/usr/bin/env python3
from pathlib import Path

P = Path('research/article_full_corpus_traversal_2026-09-04.md')
text = P.read_text(encoding='utf-8')

repls = [
("- `IMAGE_SOURCE_REGISTERED` — scan/PDF original confirmed and available for page-level verification.\n- `PENDING` — not yet read in this pass.\n",
 "- `IMAGE_SOURCE_REGISTERED` — scan/PDF original confirmed and available for page-level verification.\n- `MACHINE_TRAVERSED` — every XML element/text block was deterministically parsed and inspected by the traversal script; this is complete machine coverage, not a claim of human line-by-line semantic reading.\n- `PENDING` — not yet read in this pass.\n"),
("This is a candidate for later surgical revision of Draft 04 after corpus traversal, not for immediate free-standing expansion.\n",
 "This mechanism-first sequence was surgically integrated into Draft 04 during the DBNL collected-works pass; the revision replaces the earlier stack-of-parallels compression with the source's narrower relation-first sequence.\n"),
("Required next action: continue metadata traversal and try broader primary-text variants/known bibliographic markers to isolate the actual *Verzamelde Werken* / complete-works files, then traverse those volumes systematically.\n",
 "Update: this Library-specific hunt is no longer required for article access to the collected works. The nine DBNL TEI volumes are now mirrored directly in GitHub and machine-traversed below. Library isolation remains relevant only if a separate copy/provenance question arises.\n"),
]
for old,new in repls:
    if text.count(old) != 1:
        raise SystemExit(f'anchor count {text.count(old)} for: {old[:80]!r}')
    text = text.replace(old,new,1)

anchor = "## Article argument-function audit\n"
if text.count(anchor) != 1:
    raise SystemExit(f'article audit anchor count={text.count(anchor)}')
section = """## Corpus F — DBNL *Verzamelde Werken* TEI mirror

The published collected-works layer is now directly controlled in this repository rather than inferred from Library search.

- nine DBNL TEI XML files under `sources/dbnl/verzamelde_werken/`: `MACHINE_TRAVERSED`;
- XML elements visited: **79,038**;
- normalized text blocks inspected: **23,422**;
- normalized block characters inspected: **12,066,667**;
- high-recall article candidates retained for human review: **8,720**.

Deterministic outputs:

- `analysis/dbnl_vw_article_candidates_2026-09-04.tsv`;
- `research/article_dbnl_verzamelde_werken_integration_2026-09-04.md`;
- `research/article_dbnl_vw_integration_decisions_2026-09-04.md`.

Two findings passed the article-function test and have already been integrated surgically into Draft 04:

1. **1929 Leiden institutional prehistory — CHRONOLOGICAL / INSTITUTIONAL CONSEQUENCE.** In `Het sprookje van de rolverdeeling`, Huizinga reproduced the claim that Leiden's chairs in Indonesian languages and in `land- en volkenkunde van Nederlandsch Indië` were `een privilege der Leidsche Universiteit`, explicitly tied to the university's collections and chairs in colonial law. This now precedes the 1931 Centre proposal in the Leiden scene.
2. **1933 Kula -> potlatch -> Burgundy — MECHANISM.** The published address specifies reciprocal display and a concrete Burgundian banquet sequence before allowing the analogy to potlatch. Draft 04 now follows that mechanism-first order rather than presenting the three cases as adjacent parallels.

Material held out of the body after review includes the 1933 Warburg `cultuurwetenschappelijk laboratorium` passage (parallel without a demonstrated pair/Leiden mechanism) and later *Homo ludens* primitive/ethnology formulations beyond the article's 1933 stopping rule.

Canonical Draft 04 after this integration: blob `4eac472ffb04b3362ff56a765989d8e0a8d66999`.

"""
text = text.replace(anchor, section + anchor, 1)
P.write_text(text, encoding='utf-8')
print('updated traversal ledger with DBNL collected-works status')

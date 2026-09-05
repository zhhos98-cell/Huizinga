# Generated DBNL analysis

This directory contains deterministic machine outputs from the mirrored nine-volume DBNL *Verzamelde Werken* TEI corpus. These files are **generated navigation/review aids, not human article decisions**.

Current outputs:

- `dbnl_vw_article_candidates_2026-09-04.tsv` — high-recall scored candidate blocks from all nine XML volumes;
- `article_dbnl_verzamelde_werken_integration_2026-09-04.md` — machine traversal report and ranked candidate excerpts;
- `article_dbnl_vw_units_1921_1933_review_2026-09-04.md` — all 124 units admitted by the bounded 1921–1933 year/title rule, with no rank truncation.

The source XML remains under `../../../sources/dbnl/verzamelde_werken/`. `../../../scripts/scan_dbnl_vw_article.py` and `../../../scripts/review_dbnl_vw_units_1921_1933.py` regenerate this layer.

Human adjudication belongs in `../../../research/`, especially:

- `article_dbnl_vw_integration_decisions_2026-09-04.md`;
- `article_dbnl_vw_postintegration_recheck_2026-09-05.md`;
- `article_dbnl_vw_truncated_tail_closure_2026-09-05.md`.

A keyword score or candidate row does not constitute article evidence. Prefer an existing human control before opening these generated files. Re-run the machine layer only when source XML or the bounded scan logic actually changes, not to rediscover a closed article point.

# chunk_028 visual review

Status: **COMPLETE — retrieval-grade visual audit, 244/244 pages.**

This directory contains the separate visual correction/triage layer for `chunk_028`. The raw PaddleOCR v3 source is preserved unchanged.

Files:

- `full_visual_audit_manifest_v1.tsv` — page-level canonical classification.
- `empty_ocr_visual_review_v1.tsv` — visual resolution of all 53 baseline-empty pages.
- `composite_page_structure_v1.tsv` — documentary/layout segmentation and reading-order warnings.
- `core_theme_hits_v1.md` — research-facing conceptual/institutional hits and negative controls.
- `review_summary_v1.md` — narrative audit summary.
- `status.txt` — compact status record.

The chunk moves from late-medieval England/Burgundy/Low Countries source work into a very large mounted religion/Renaissance/humanist working complex, then into dated nineteenth-century political-history notes around 1830/1848. The mounted portions are highly reading-order-sensitive and contain many severe OCR hallucinations. Exact quotation from `high-noise` pages requires scan-level verification.

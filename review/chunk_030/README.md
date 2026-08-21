# chunk_030 visual review

Status: **COMPLETE — retrieval-grade visual audit, 237/237 pages.**

This directory contains the separate visual correction/triage layer for `chunk_030`. The raw PaddleOCR v3 source is preserved unchanged.

Files:

- `full_visual_audit_manifest_v1.tsv` — page-level canonical classification.
- `empty_ocr_visual_review_v1.tsv` — visual resolution of all 44 baseline-empty pages.
- `composite_page_structure_v1.tsv` — documentary/layout segmentation and reading-order warnings.
- `core_theme_hits_v1.md` — research-facing conceptual/institutional hits and negative controls.
- `review_summary_v1.md` — narrative audit summary.
- `status.txt` — compact status record.

The chunk moves through a large mounted intellectual/political-history complex into Burke and British radical/reform politics, an explicitly organized Revolution packet, a long 1819-1820 Parliamentary Debates sequence, and finally medieval Zeeland/Flanders ecclesiastical-geographical source notes. Mounted sections are highly reading-order-sensitive and contain many severe OCR hallucinations. Exact quotation from `high-noise` pages requires scan-level verification.

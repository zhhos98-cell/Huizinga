# chunk_031 review

This directory contains the retrieval-grade visual/OCR review layer for `chunk_031:p0001-p0247`.

Raw PaddleOCR v3 text is preserved unchanged. The files here classify every scan page, resolve all baseline-empty OCR pages against the scans, map documentary packets/layout hazards, and surface research-facing hits and negative controls.

Canonical files:

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review_v1.tsv`
- `composite_page_structure_v1.tsv`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`

The review is designed for retrieval and triage, not diplomatic transcription. Exact quotation from `high-noise` or `false-empty-recovery` pages still requires close reading of the scan.

# chunk_029 retrieval-grade review

Scope: `chunk_029:p0001-p0240`.

This directory contains the visual/OCR audit layer for chunk 029. The source PaddleOCR v3 text is preserved unchanged. Review files classify retrieval quality, resolve empty-OCR pages through direct visual inspection, map composite/mounted-page structure, and promote research-facing hits with explicit negative controls.

## Files

- `full_visual_audit_manifest_v1.tsv` — page-by-page canonical review classification.
- `empty_ocr_visual_review_v1.tsv` — visual resolution of every baseline-empty OCR page.
- `composite_page_structure_v1.tsv` — documentary segmentation and layout/reading-order notes.
- `core_theme_hits_v1.md` — first-order thematic/documentary hits and false-positive controls.
- `review_summary_v1.md` — human-readable audit report.
- `status.txt` — compact status snapshot.

## Review policy

Mounted-slip boards are classified conservatively because OCR reading order does not preserve physical layout. Exact quotation from `high-noise` or `false-empty-recovery` pages requires direct scan verification. Modern semantic intrusions, generated tables/test phrases, and plausible-looking OCR text are treated as machine pathology when unsupported by the scan.

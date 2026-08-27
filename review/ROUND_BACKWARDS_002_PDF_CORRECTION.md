# Huizinga PDF-to-JSON correction round, backwards batch 002

Original PDFs checked, newest span first:

- `chunk_069__p0201-0214.pdf`
- `chunk_069__p0161-0200.pdf`
- `chunk_069__p0121-0160.pdf`
- `chunk_069__p0081-0120.pdf`
- `chunk_069__p0041-0080.pdf`

Pages compared with the original scans: **174**.

The raw JSON is preserved. Thirteen PDF-verified actions were applied to a new corrected copy. The principal interventions remove four pathological blocks dominated by repeated digits or words, remove an unrelated Korean UI-like insertion, recover four OCR-empty envelope labels or shelfmarks, and replace four misread headings. Dense mounted-slip pages retain all unaffected OCR blocks.

Files:

- `chunk_069.pdf_by_PaddleOCR-VL-1.6.corrected.json`
- `corrections/chunk_069_manual.json`
- `review/chunk_069/applied_patch_audit_v1.tsv`
- `review/chunk_069/pdf_verification_log_v1.tsv`

Supply note: `chunk_069:p0001-p0040` belongs to the following backwards batch and is not included here.

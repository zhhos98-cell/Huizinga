# Huizinga Leiden visual review progress

Updated: 2026-08-20

## Chunk 001

- Source span: `chunk_001:p0001`–`chunk_001:p0179` (179 scan pages).
- Review PDFs received in five blocks: 1–40, 41–80, 81–120, 121–160, 161–179.
- **Full-page visual audit: 179/179 complete.** Every scan page has been visually checked for text presence, layout, OCR failure, and retrieval usability.
- Review level: **retrieval-grade visual correction layer**. Raw PaddleOCR is preserved unchanged; this is not presented as a diplomatic or word-perfect transcription.
- Page classes: **38 usable; 70 usable-with-noise; 32 high-noise requiring close transcription before exact quotation; 10 false-empty OCR pages manually recovered; 4 short-text pages manually verified; 25 genuinely blank.** Total: 179.
- Complete page-level status is in `review/chunk_001/full_visual_audit_manifest_v1.tsv`.
- `empty_ocr` audit: **35/35 visually checked**; **25 genuinely blank**, **10 false-empty with substantive text** — `p0018`, `p0020`, `p0068`, `p0098`, `p0100`, `p0108`, `p0109`, `p0149`, `p0150`, `p0162`.
- Conservative recoveries for those ten pages are in `review/chunk_001/empty_ocr_visual_review.jsonl`.
- Repeated Rockefeller stationery verified on five chunk-001 pages: `p0101`, `p0109`, `p0145`, `p0151`, `p0169`. `p0109` was a complete OCR false negative.
- The exact-quotation queue is explicit rather than hidden: 32 high-noise already-nonempty pages plus 7 fragmentary/faint false-empty recoveries need another close palaeographic read before verbatim use. Their page-level content has already been visually audited.
- Detailed summary and queue: `review/chunk_001/review_summary_v1.md`.

### Status

**Chunk 001 retrieval-grade visual audit: COMPLETE.**

## Chunk 003

- Source span: `chunk_003:p0001`–`chunk_003:p0090` (90 pages).
- Some split uploads failed, but the complete 90-page source PDF `chunk_003(1).pdf` was available, so coverage is complete.
- **Full-page visual audit: 90/90 complete.**
- Page classes: **29 usable; 39 usable-with-noise; 11 high-noise; 3 false-empty OCR pages recovered; 1 verified short printed-text page; 7 genuinely blank.**
- Baseline empty OCR pages: 10. Visual result: **7 blank, 3 false-empty** (`p0038`, `p0079`, `p0080`).
- `chunk_003:p0082` visually verifies the printed letterhead **“The Laura Spelman Rockefeller Memorial / 61 Broadway / New York.”** The baseline OCR captured this occurrence.
- Files: `review/chunk_003/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`.

### Status

**Chunk 003 retrieval-grade visual audit: COMPLETE.**

## Chunk 004

- Baseline span: `chunk_004:p0001`–`chunk_004:p0236` (236 pages).
- Visual scan coverage currently available: `p0001–p0080` and `p0161–p0236`.
- **Visually audited: 156/236.** Missing scan block: **`p0081–p0160` (80 pages)**.
- Reviewed-page classes: **57 usable; 76 usable-with-noise; 19 high-noise; 1 false-empty OCR recovery; 3 genuinely blank.**
- Baseline empty OCR pages: `p0045`, `p0101`, `p0114`, `p0176`, `p0210`, `p0236`. Current visual result: `p0045`, `p0176`, `p0236` blank; `p0210` is a substantive false-empty handwritten page; `p0101` and `p0114` fall inside the missing scan block and remain priority checks.
- `p0210` anchor-level recovery includes papal/Italian material: **paus; Italië; Langob.; Ravenna en Pentapolis; keizer Leo III (717–741); paus Greg. II; Liutprand; Rome; 715–731; 731–741**.
- Files: `review/chunk_004/visual_audit_manifest_p0001-0080_v1.tsv`, `visual_audit_manifest_p0161-0236_v1.tsv`, `missing_scan_block_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`.

### Status

**Chunk 004 retrieval-grade visual audit: PARTIAL — 156/236 complete; missing `p0081–p0160`.**

## Cross-chunk institutional hits

- Verified Rockefeller stationery now totals **six pages** across reviewed chunks: `chunk_001:p0101`, `p0109`, `p0145`, `p0151`, `p0169`, and `chunk_003:p0082`.
- Cross-chunk index: `review/rockefeller_stationery_index.md`.
- Treat stationery hits as documentary occurrences, not automatically as substantive correspondence or proof of funding/agency; sender, recipient, body text, date, and archival sequence require separate confirmation.

### Review policy

Preserve raw OCR as source data. Visual review is written as a separate correction/transcription layer. Do not infer illegible text. Use `[unclear]` for uncertain readings and `[...]` where the physical scan cuts off text. Retrieval-grade quality classes are triage labels, not claims of diplomatic transcription.

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
- Split scan set now verified complete and contiguous: 1–40, 41–80, 81–90; page-count check `40 + 40 + 10 = 90`.
- **Full-page visual audit: 90/90 complete.**
- Page classes: **29 usable; 39 usable-with-noise; 11 high-noise; 3 false-empty OCR pages recovered; 1 verified short printed-text page; 7 genuinely blank.**
- Baseline empty OCR pages: 10. Visual result: **7 blank, 3 false-empty** (`p0038`, `p0079`, `p0080`).
- `chunk_003:p0082` visually verifies the printed letterhead **“The Laura Spelman Rockefeller Memorial / 61 Broadway / New York.”** The baseline OCR captured this occurrence.
- Files: `review/chunk_003/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`.

### Status

**Chunk 003 retrieval-grade visual audit: COMPLETE (90/90).**

## Chunk 004

- Baseline span: `chunk_004:p0001`–`chunk_004:p0236` (236 pages).
- Split scan set now verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–236; page-count check `40 + 40 + 40 + 40 + 40 + 36 = 236`.
- **Full-page visual audit: 236/236 complete.** The former `p0081–p0160` gap has been reviewed and `missing_scan_block_v1.tsv` is now marked resolved.
- Full-page classes: **86 usable; 105 usable-with-noise; 39 high-noise; 1 false-empty OCR recovery; 5 genuinely blank.**
- Baseline empty OCR pages: `p0045`, `p0101`, `p0114`, `p0176`, `p0210`, `p0236`. Final visual result: **five blank** (`p0045`, `p0101`, `p0114`, `p0176`, `p0236`) and **one false-empty** (`p0210`).
- `p0101` and `p0114`, previously unresolved because their scan block was missing, have now been inspected at full-page/higher resolution and confirmed blank.
- `p0210` anchor-level recovery includes papal/Italian material: **paus; Italië; Langob.; Ravenna en Pentapolis; keizer Leo III (717–741); paus Greg. II; Liutprand; Rome; 715–731; 731–741**.
- New middle-block high-noise queue includes severe under-capture (`p0082`, `p0084`, `p0110`, `p0117`), hallucinated/mixed-script OCR (`p0091–p0094`, `p0120`, `p0122`, `p0123`, `p0138`, `p0139`, `p0144`, `p0160`), pathological year/repetition output (`p0145`, `p0159`), and low-coverage/multi-slip layouts (`p0151`, `p0155`, `p0156`).
- Files: `review/chunk_004/visual_audit_manifest_p0001-0080_v1.tsv`, `visual_audit_manifest_p0081-0160_v1.tsv`, `visual_audit_manifest_p0161-0236_v1.tsv`, `missing_scan_block_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`.

### Status

**Chunk 004 retrieval-grade visual audit: COMPLETE (236/236).**

## Chunk 006

- Source span: `chunk_006:p0001`–`chunk_006:p0180` (180 pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–180; page-count check `40 + 40 + 40 + 40 + 20 = 180`.
- **Full-page visual audit: 180/180 complete.**
- Page classes: **47 usable; 66 usable-with-noise; 37 high-noise; 3 false-empty OCR pages recovered; 3 verified short-text pages; 2 minimal/non-substantive mark pages; 22 genuinely blank.**
- Baseline empty OCR pages: 26. Visual result: **22 blank/no substantive text, 3 substantive false-empty pages (`p0092`, `p0176`, `p0180`), 1 minimal mark-only page (`p0093`).**
- `p0176` anchor-level recovery: **H. Joly; Sainte Thérèse; Les Saints; Paris; Lecoffre**.
- `p0180` contains multiple handwritten slips/card; visible anchor: **“De la méthode dans les sciences. Histoire ...”**.
- Major OCR pathology includes `p0008` over-expansion, `p0095`/`p0164`/`p0168` repetition cleanup, and severe mounted-slip under-capture in the exact-quotation queue.
- Files: `review/chunk_006/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`.

### Status

**Chunk 006 retrieval-grade visual audit: COMPLETE (180/180).**

## Chunk 007

- Source span: `chunk_007:p0001`–`chunk_007:p0147` (147 pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–147; page-count check `40 + 40 + 40 + 27 = 147`.
- **Full-page visual audit: 147/147 complete.** All pages were visually checked against the clean PaddleOCR v3 baseline; obvious mismatch and empty-OCR cases were rechecked at higher resolution.
- Page classes: **15 usable; 87 usable-with-noise; 37 high-noise requiring close transcription before exact quotation; 2 false-empty OCR pages recovered; 6 genuinely blank/no-substantive-text pages.**
- Baseline empty OCR pages: 8. Visual result: **6 blank** (`p0103`, `p0111`, `p0112`, `p0127`, `p0133`, `p0140`) and **2 false-empty** (`p0115`, `p0120`).
- `p0115` is a complete OCR false negative: two mounting boards carry many handwritten slips and require close transcription.
- `p0120` is a complete OCR false negative for the printed letterhead **“The Laura Spelman Rockefeller Memorial / 61 Broadway / New York.”** No substantive body text is visible on that scan; the occurrence is added to the stationery index.
- Major pathology includes severe under-capture (`p0045`, `p0080`, `p0105`, `p0122`, `p0128`, `p0132`, `p0142`), mixed-script/multilingual hallucination (`p0093`, `p0104`, `p0107`, `p0109`, much of the mounted-slip sequence), and reading-order collapse on multi-slip boards from `p0113` onward.
- Files: `review/chunk_007/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`.

### Status

**Chunk 007 retrieval-grade visual audit: COMPLETE (147/147).**

## Cross-chunk institutional hits

- Verified Rockefeller stationery now totals **seven pages** across reviewed chunks: `chunk_001:p0101`, `p0109`, `p0145`, `p0151`, `p0169`, `chunk_003:p0082`, and `chunk_007:p0120`.
- Cross-chunk index: `review/rockefeller_stationery_index.md`.
- Treat stationery hits as documentary occurrences, not automatically as substantive correspondence or proof of funding/agency; sender, recipient, body text, date, and archival sequence require separate confirmation.

### Review policy

Preserve raw OCR as source data. Visual review is written as a separate correction/transcription layer. Do not infer illegible text. Use `[unclear]` for uncertain readings and `[...]` where the physical scan cuts off text. Retrieval-grade quality classes are triage labels, not claims of diplomatic transcription.

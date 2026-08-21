# Huizinga Leiden visual review progress

Updated: 2026-08-21

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

## Chunk 005

- Source span: `chunk_005:p0001`–`chunk_005:p0173` (173 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–173; page-count check `40 + 40 + 40 + 40 + 13 = 173`.
- **Full-page visual audit: 173/173 complete.** Every page was checked against the clean PaddleOCR v3 baseline, with empty-OCR and severe mismatch cases rechecked at higher resolution.
- Baseline empty OCR pages: 15. Visual result: **3 false-empty recoveries** (`p0044`, `p0063`, `p0149`), **10 genuinely blank/no-substantive-text pages** (`p0008`, `p0012`, `p0014`, `p0024`, `p0042`, `p0045`, `p0050`, `p0056`, `p0151`, `p0173`), **1 minimal/non-substantive page** (`p0036`), and **1 verified short printed-text page** (`p0158`, `BRIEFKAART`).
- `p0044` is a complete OCR false negative for a mounted sheet containing a handwritten classification/table plus several attached slips.
- `p0063` is a complete OCR false negative for the printed letterhead **“The Laura Spelman Rockefeller Memorial / 61 Broadway / New York.”**
- `p0149` is a complete OCR false negative for dense handwritten historical notes; visible anchors include `Philips II` and dates in the 1517–1521 range, but exact quotation still requires close reading.
- Main high-noise queue includes severe multi-slip under-capture (`p0016`, `p0018`, `p0019`, `p0020`, `p0021`, `p0023`, `p0026`, `p0027`, `p0030`, `p0049`, `p0062`), pathological repetition/mixed-script output (`p0046`, `p0074`), plus the false-empty manuscript pages where close transcription remains necessary.
- Files: `review/chunk_005/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`, `status.txt`.

### Status

**Chunk 005 retrieval-grade visual audit: COMPLETE (173/173).**

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

## Chunk 008

- Source span: `chunk_008:p0001`–`chunk_008:p0111` (111 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–111; page-count check `40 + 40 + 31 = 111`.
- **Full-page visual audit: 111/111 complete.** Empty-OCR and severe under/over-capture cases were rechecked at higher resolution.
- Baseline empty OCR pages: 18. Visual result: **7 false-empty recoveries** (`p0001`, `p0028`, `p0035`, `p0052`, `p0056`, `p0057`, `p0070`) and **11 genuinely blank/no-substantive-text pages** (`p0006`, `p0010`, `p0014`, `p0017`, `p0023`, `p0029`, `p0033`, `p0036`, `p0044`, `p0089`, `p0096`).
- `p0001` is a complete OCR false negative for **“The Laura Spelman Rockefeller Memorial / 61 Broadway / New York.”**
- `p0028` contains faint handwritten material with the visible date range **1795–1856**.
- `p0035` contains multiple handwritten mounted slips, many rotated, despite an empty baseline.
- `p0052` contains a dense series of handwritten index slips; clearly readable anchors include **“d.13. keuze of interpretatie”**, **“d.12. zuiverheid spiritualiteit”**, and **“17. vormleer”**.
- `p0056`, `p0057`, and `p0070` are additional mounted-slip false negatives with text present but insufficient for exact quotation without close reading.
- Main high-noise queue is concentrated in mounted-slip layouts with extreme under-capture (`p0005`, `p0047`, `p0053`–`p0055`, `p0061`, `p0064`–`p0066`, `p0068`, `p0071`–`p0078`, `p0084`) and pathological over-expansion/repetition (`p0019`, `p0025`, `p0059`).
- Pages `p0085`–`p0111` are predominantly printed book/newspaper material and are substantially more regular for retrieval than the mounted-slip sequence.
- Files: `review/chunk_008/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`, `status.txt`.

### Status

**Chunk 008 retrieval-grade visual audit: COMPLETE (111/111).**

## Chunk 009

- Source span: `chunk_009:p0001`–`chunk_009:p0102` (102 scan pages).
- Split scan set is complete and contiguous: 1–40, 41–80, 81–102; page-count check `40 + 40 + 22 = 102`.
- All 102 pages were visually checked against the clean PaddleOCR v3 baseline.
- Page classes: **12 usable; 84 usable-with-noise; 5 high-noise; 0 false-empty OCR recoveries; 1 genuinely blank/no substantive text.**
- High-noise queue: `p0045`, `p0080`, `p0090`, `p0093`, `p0102`.
- Files: `review/chunk_009/full_visual_audit_manifest_v1.tsv`, `review_summary_v1.md`, `status.txt`, `README.md`.

### Status

**Chunk 009 retrieval-grade visual audit: COMPLETE (102/102).**

## Chunk 010

- Source span: `chunk_010:p0001`–`chunk_010:p0153` (153 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–153; page-count check `40 + 40 + 40 + 33 = 153`.
- **Full-page visual audit: 153/153 complete.** The regular notebook sequence was checked at page-layout level; anomalies and empty-OCR cases were rechecked at higher resolution.
- Page classes: **143 usable-with-noise; 6 high-noise; 1 false-empty OCR recovery; 1 verified short-text page; 2 genuinely blank/no-substantive-text pages.**
- Baseline empty OCR pages: `p0150`, `p0151`, `p0152`. Visual result: **two blank** (`p0150`, `p0151`) and **one false-empty** (`p0152`).
- `p0152` contains an envelope marked **“Fred. Hendrik”** plus two handwritten slips; conservative visible anchors include **1633–1637** and **1905**.
- High-noise queue: `p0006`, `p0007`, `p0060`, `p0102`, `p0128`, `p0153`.
- `p0153` is a clear baseline hallucination: OCR **“2020 THETROO DAOMO ROBLOX UK”** versus the visible mounted-slip text **“de naamverwisseling.”**
- Files: `review/chunk_010/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`, `status.txt`, `README.md`.

### Status

**Chunk 010 retrieval-grade visual audit: COMPLETE (153/153).**

## Chunk 011

- Source span: `chunk_011:p0001`–`chunk_011:p0200` (200 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200; page-count check `40 + 40 + 40 + 40 + 40 = 200`.
- **Full-page visual audit: 200/200 complete.** All pages were checked against the clean PaddleOCR v3 baseline; empty-OCR, unusual-layout, and mixed-script cases were rechecked at higher resolution.
- Page classes: **192 usable-with-noise; 3 high-noise; 3 verified short-text pages; 2 genuinely blank/no-substantive-text pages; 0 false-empty recoveries.**
- Baseline empty OCR pages: `p0150`, `p0200`; both are visually blank/no substantive text.
- High-noise queue: `p0061`, `p0147`, `p0166`. `p0061` is a severe mounted-slip under-capture; `p0147` and `p0166` contain repeated mixed-script hallucinations on dense handwritten pages.
- Distinctive printed insertions: `p0074` is the illustrated title page of James I's *Workes*; `p0075` is a printed bookseller/catalogue page headed **“ENGLAND TO THE DEATH OF ELIZABETH”** paired with handwritten notes.
- Verified short-text pages: `p0001`, `p0157` (**BRIEFKAART**), `p0162` (**“Eng. beschaving XVIII. 1925/26”**).
- Files: `review/chunk_011/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`, `status.txt`, `README.md`.

### Status

**Chunk 011 retrieval-grade visual audit: COMPLETE (200/200).**

## Chunk 012

- Source span: `chunk_012:p0001`–`chunk_012:p0161` (161 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161; page-count check `40 + 40 + 40 + 40 + 1 = 161`.
- **Full-page visual audit: 161/161 complete.** All pages were checked against the clean PaddleOCR v3 baseline; empty-OCR, mounted-slip, photographic-table, and short-text anomalies were rechecked at higher resolution.
- Page classes: **8 usable; 115 usable-with-noise; 12 high-noise; 8 false-empty OCR recoveries; 3 verified short-text pages; 15 genuinely blank/no-substantive-text pages.**
- Baseline empty OCR pages: 23. Visual result: **15 blank** (`p0093`, `p0096`, `p0099`, `p0103`, `p0107`, `p0110`, `p0114`, `p0117`, `p0121`, `p0124`, `p0128`, `p0136`, `p0137`, `p0151`, `p0152`) and **8 false-empty** (`p0122`, `p0123`, `p0125`, `p0131`, `p0153`, `p0154`, `p0156`, `p0158`).
- High-noise queue: `p0098`, `p0101`, `p0105`, `p0106`, `p0109`, `p0112`, `p0119`, `p0127`, `p0140`, `p0155`, `p0157`, `p0161`; the dominant failures are mounted-board under-capture and near-total failure on dense photographic tables.
- Documentary transitions worth retaining for later analysis: `p0138` is headed **“OUD ARCHIEF IN ZEELAND”** and includes **“MIDDELBURG, 20 Juni 1923”**; `p0142–p0150` contain Huizinga's printed Sir Philip Sidney commemorative address; `p0159` gives the heading **“Veelvuldigste namen uit het zijlschotregister van Winsummer- & Schaphalster Zijlvest 1553.”**
- Files: `review/chunk_012/full_visual_audit_manifest_v1.tsv`, `empty_ocr_visual_review.jsonl`, `review_summary_v1.md`, `status.txt`, `README.md`.

### Status

**Chunk 012 retrieval-grade visual audit: COMPLETE (161/161).**

## Cross-chunk institutional hits

- Verified Rockefeller stationery now includes occurrences in reviewed chunks 001, 003, 005, 007, and 008. Newly verified complete OCR false negatives are `chunk_005:p0063` and `chunk_008:p0001`; `chunk_005:p0059` also visibly carries the same letterhead and was captured by baseline OCR.
- Cross-chunk index: `review/rockefeller_stationery_index.md`.
- Treat stationery hits as documentary occurrences, not automatically as substantive correspondence or proof of funding/agency; sender, recipient, body text, date, and archival sequence require separate confirmation.

### Review policy

Preserve raw OCR as source data. Visual review is written as a separate correction/transcription layer. Do not infer illegible text. Use `[unclear]` for uncertain readings and `[...]` where the physical scan cuts off text. Retrieval-grade quality classes are triage labels, not claims of diplomatic transcription.

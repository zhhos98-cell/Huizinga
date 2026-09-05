# Huizinga visual calibration — five-PDF round 002

Date: 2026-08-26

Operational unit: five supplied scan PDFs. Raw PaddleOCR JSON files are preserved unchanged; calibration is written only to `review/`.

## Inputs completed

1. `chunk_002_1-61.pdf` — 61 pages
2. `chunk_002_62-122.pdf` — 61 pages
3. `chunk_002_123-183.pdf` — 61 pages
4. `chunk_034__p0041-0080.pdf` — 40 pages
5. `chunk_034__p0121-0160.pdf` — 40 pages

Total scan pages reviewed: **263**.

## `chunk_002` — three PDFs / 183 pages

The three contiguous 61-page PDFs were reviewed page by page across `p0001-p0183`. The scan set is dominated by dark-background archival/microfilm-style images carrying pale slips, cards, forms, typewritten sheets, manuscript leaves, signatures, stamps, and rotated or paired source objects.

Round 002 upgrades the former macro-only state to a true **183/183 page-level visual manifest** and an exhaustive baseline OCR empty/nonempty-signal audit. The raw split OCR is empty on ten pages:

`p0001;p0005;p0015;p0016;p0048;p0053;p0096;p0137;p0174;p0175`

Nine are visually true blank/no-substantive pages. `p0016` is the single false-empty recovery: the OCR signal is empty while faint substantive text is visible in the scan.

Two nonempty machine-pathology controls remain especially strong: `p0089`, where normal continuous French handwriting becomes catastrophic repeated-number/table-like OCR output, and `p0143`, where a backside/blank-slip montage produces unsupported modern `2024`/numeric material.

Visual/layout manifest counts are: `usable-with-noise=138`, `high-noise=32`, `blank-no-substantive=9`, `short-text=3`, `false-empty-recovery=1`.

This is page-level visual and false-empty closure, not line-by-line semantic proofreading of every nonempty OCR string. Exact quotation remains scan-first.

## `chunk_034__p0041-0080.pdf` — 40 pages

All 40 pages were visually swept. The segment continues the dark-background archival-card sequence, with small typed/handwritten record content, signatures, stamps, numbers, and index-card layouts. Local p33 (absolute `chunk_034:p0073`) was re-rendered at higher resolution and confirmed as a genuine blank source card on a dark background, not a rendering failure. No gross page-order or rendering break was observed.

Result: macro visual calibration PASS for `p0041-p0080`; `p0073` is added as a high-confidence blank/no-substantive negative control.

## `chunk_034__p0121-0160.pdf` — 40 pages

All 40 pages were visually swept. The same archival-card structure continues; denser writing is visible in parts of the later local sequence, while several pages are sparse or blank-card records. Local p5 (absolute `chunk_034:p0125`) was checked at higher resolution and confirmed as a genuine blank source card on a dark background. No gross rendering catastrophe was observed.

Result: macro visual calibration PASS for `p0121-p0160`; `p0125` is added as a high-confidence blank/no-substantive negative control.

## Round result

- **5 PDFs / 263 pages** completed.
- `chunk_002:p0001-p0183`: page-level visual coverage **183/183 COMPLETE**; baseline empty/false-empty audit **183/183 COMPLETE**; one false-empty recovery at `p0016`.
- `chunk_034`: **80 newly reviewed pages**, bringing macro-reviewed coverage to `p0001-p0080` and `p0121-p0160`; new true-blank controls at `p0073` and `p0125`.
- A photographed blank card/sheet must not be treated as a missing rendered page. Blank-source controls remain important OCR negative controls.
- Dominant OCR hazards are dark-background/source-object segmentation, tiny typewriting, handwriting/signatures/stamps, rotation, multi-object pages, nonlinear reading order, and semantic over-generation on sparse/composite archival layouts.

## Calibration policy

Raw PaddleOCR JSON remains unchanged. `chunk_002` has genuine page-level visual and baseline false-empty closure, but not full semantic proofreading of every nonempty OCR string. The newly reviewed `chunk_034` spans remain macro calibration with direct control pages rather than diplomatic transcription or a complete page-level OCR usability manifest. Exact quotation from manuscript/composite pages remains scan-first.

# Huizinga visual calibration — five-PDF round 008

Date: 2026-08-26

Operational unit: five supplied scan PDFs. This round closes chunk_037 and opens chunk_038 at `p0121-p0160`. Raw PaddleOCR JSON files are not rewritten by this pass.

## Inputs completed

1. `chunk_037__p0121-0160.pdf` — 40 pages
2. `chunk_037__p0161-0200.pdf` — 40 pages
3. `chunk_037__p0201-0240.pdf` — 40 pages
4. `chunk_037__p0241-0243.pdf` — 3 pages
5. `chunk_038__p0121-0160.pdf` — 40 pages

Total scan pages visually reviewed: **163**.

## Round 008 visual class counts

Across all five PDFs:

- high-noise-layout-risk: **118**
- blank-no-substantive-visual: **35**
- short-text-or-nontext: **2**
- usable-with-noise-visual: **8**

Segment breakdown:

- `chunk_037:p0121-p0160`: 31 high-noise, 9 blank/no-substantive
- `chunk_037:p0161-p0200`: 30 high-noise, 10 blank/no-substantive
- `chunk_037:p0201-p0240`: 28 high-noise, 11 blank/no-substantive, 1 short/nontext
- `chunk_037:p0241-p0243`: 3 high-noise
- `chunk_038:p0121-p0160`: 26 high-noise, 5 blank/no-substantive, 1 short/nontext, 8 usable-with-noise

## chunk_037 closure

The remaining `p0121-p0243` span is now visually classified, bringing chunk_037 to **243/243 page-level visual closure**.

Round 008 contributes 92 high-noise, 30 blank/no-substantive and 1 short/nontext page over the final 123 pages. Combined with Round 007, the whole-chunk aggregate is:

- high-noise-layout-risk: **174**
- blank-no-substantive-visual: **61**
- short-text-or-nontext: **1**
- usable-with-noise-visual: **7**

The previously identified retrieval-stronger packet at `p0058` and `p0112-p0117` remains the main large-sheet/linear-manuscript exception to the otherwise dominant mounted-slip morphology. Selective higher-resolution inspection in the closing span classifies `p0218` as short/nontext: a sparse envelope/file-object page with only a small amount of substantive text.

## chunk_038 opening

Round 008 reviews `p0121-p0160`, bringing chunk_038 to **40/226 page-level visual coverage**.

The first fifteen pages show a conspicuous morphology break from the usual dark mounting-board / small-slip regime. `p0121-p0122` are large typed/linear sheets; `p0125-p0126` are page-scale handwritten manuscript sheets; `p0130-p0131` are relatively linear name/list cards; and `p0132-p0133` are single-column clippings. These eight pages are retrieval-usable with noise. In contrast, `p0123-p0124` and `p0134-p0135` are newspaper or stitched multi-column layouts and remain high-noise/reading-order-risk pages. `p0127` is a small envelope/file-cover object and is short/nontext.

From `p0137` onward, the familiar mounted-slip morphology again predominates, with periodic genuinely blank/no-substantive source cards.

No indexed raw OCR file for chunk_037 or chunk_038 was found in the current repository search, so the work recorded here is visual/layout calibration only and does not claim OCR-string correction.

## Round result

- **5 PDFs / 163 pages** completed.
- chunk_037: **243/243 visual closure COMPLETE**.
- chunk_038: **40/226 visual coverage** at `p0121-p0160`.
- Raw OCR files were not rewritten; OCR strings were not exhaustively proofread page by page.

## Calibration policy

The current work is page-level visual/layout calibration. Exact quotation from handwriting-heavy, mounted-board, clipped-newspaper or composite pages remains scan-first. Pages marked usable-with-noise are retrieval-usable but still require direct scan verification for quotation.

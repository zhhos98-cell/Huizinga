# Huizinga visual calibration — five-PDF round 007

Date: 2026-08-26

Operational unit: five supplied scan PDFs. This round closes chunk_036 and opens chunk_037 through `p0120`. Raw PaddleOCR JSON files are not rewritten by this pass.

## Inputs completed

1. `chunk_036__p0161-0200.pdf` — 40 pages
2. `chunk_036__p0201-0240.pdf` — 40 pages
3. `chunk_037__p0001-0040.pdf` — 40 pages
4. `chunk_037__p0041-0080.pdf` — 40 pages
5. `chunk_037__p0081-0120.pdf` — 40 pages

Total scan pages visually reviewed: **200**.

## Round 007 visual class counts

Across all five PDFs:

- high-noise-layout-risk: **140**
- blank-no-substantive-visual: **51**
- short-text-or-nontext: **2**
- usable-with-noise-visual: **7**

Segment breakdown:

- `chunk_036:p0161-p0200`: 29 high-noise, 9 blank/no-substantive, 2 short/nontext
- `chunk_036:p0201-p0240`: 29 high-noise, 11 blank/no-substantive
- `chunk_037:p0001-p0040`: 29 high-noise, 11 blank/no-substantive
- `chunk_037:p0041-p0080`: 29 high-noise, 10 blank/no-substantive, 1 usable-with-noise
- `chunk_037:p0081-p0120`: 24 high-noise, 10 blank/no-substantive, 6 usable-with-noise

## chunk_036 closure

The remaining `p0161-p0240` span is now visually classified, bringing chunk_036 to **240/240 page-level visual closure**.

Whole-chunk aggregate:

- high-noise-layout-risk: **171**
- blank-no-substantive-visual: **59**
- short-text-or-nontext: **6**
- usable-with-noise-visual: **4**

The dominant regime remains dark archival mounting board with multiple source slips/cards and non-linear reading order. `p0170-p0171` are sparse envelope/folder-object pages with little or no substantive source body and are retained as short/nontext controls.

## chunk_037 opening

Round 007 reviews `p0001-p0120`, bringing chunk_037 to **120/243 page-level visual coverage**. The remaining supplied span is `p0121-p0243`.

The first three segments are again dominated by mounted slips and blank source cards. A distinct morphology shift occurs at `p0058` and especially `p0112-p0117`, where large page-scale handwritten/linear sheets replace the usual small-slip composite regime. These pages are materially more retrieval-usable, while still carrying handwriting, rotation and scan-noise risk.

No indexed `chunk_037` raw OCR file was found in the current repository search, so the chunk_037 work in this round is visual/layout calibration only and does not claim OCR-string correction.

## Round result

- **5 PDFs / 200 pages** completed.
- chunk_036: **240/240 visual closure COMPLETE**.
- chunk_037: **120/243 visual coverage**; `p0121-p0243` remains.
- Raw OCR files were not rewritten; OCR strings were not exhaustively proofread page by page.

## Calibration policy

The current work is page-level visual/layout calibration. Exact quotation from handwriting-heavy, mounted-board or composite pages remains scan-first. Large linear manuscript sheets marked usable-with-noise are retrieval-usable but still require direct scan verification for quotation.

# Huizinga visual calibration — five-PDF round 011

Date: 2026-08-26

Operational unit: five supplied scan PDFs. This round closes chunk_039 and opens chunk_040 through `p0160`. Raw PaddleOCR JSON files are not rewritten by this pass.

## Inputs completed

1. `chunk_039__p0201-0236.pdf` — 36 pages
2. `chunk_040__p0001-0040.pdf` — 40 pages
3. `chunk_040__p0041-0080.pdf` — 40 pages
4. `chunk_040__p0081-0120.pdf` — 40 pages
5. `chunk_040__p0121-0160.pdf` — 40 pages

Total scan pages visually reviewed: **196**.

## Round 011 visual class counts

Across all five PDFs:

- high-noise-layout-risk: **147**
- blank-no-substantive-visual: **46**
- short-text-or-nontext: **1**
- usable-with-noise-visual: **2**

Segment breakdown:

- `chunk_039:p0201-p0236`: 28 high-noise, 6 blank/no-substantive, 1 short/nontext, 1 usable-with-noise
- `chunk_040:p0001-p0040`: 27 high-noise, 12 blank/no-substantive, 1 usable-with-noise
- `chunk_040:p0041-p0080`: 31 high-noise, 9 blank/no-substantive
- `chunk_040:p0081-p0120`: 30 high-noise, 10 blank/no-substantive
- `chunk_040:p0121-p0160`: 31 high-noise, 9 blank/no-substantive

## chunk_039 closure

The final `p0201-p0236` segment brings chunk_039 to **236/236 page-level visual closure COMPLETE**.

Whole-chunk aggregate:

- high-noise-layout-risk: **173**
- blank-no-substantive-visual: **56**
- short-text-or-nontext: **1**
- usable-with-noise-visual: **6**

The tail continues the dominant dark-board / mounted-slip morphology. `p0209` is the one retrieval-stronger tail exception: two relatively large, internally linear manuscript/list sheets give a clearer reading sequence than surrounding composite boards. `p0224` is a sparse envelope/file-object page with only minimal label text and is classified short/nontext. The earlier Round 010 retrieval controls remain `p0026`, `p0066`, `p0111`, `p0126`, and `p0169`.

## chunk_040 opening

The first four supplied segments bring chunk_040 to **160/243 page-level visual coverage**.

Current aggregate over `p0001-p0160`:

- high-noise-layout-risk: **119**
- blank-no-substantive-visual: **40**
- short-text-or-nontext: **0**
- usable-with-noise-visual: **1**

The morphology is unusually stable: dark archival mounting boards with many small slips dominate nearly every nonblank page, with frequent blank source cards interspersed. `p0010` is the clearest exception in this 160-page opening span, containing two large internally linear handwritten sheets beside an envelope/source card and is retrieval-usable with noise. No short/nontext control was identified in the opening 160 pages.

## OCR boundary

No indexed raw OCR file for chunk_039 or chunk_040 was found in the current repository search. This round therefore records visual/layout calibration only and does not claim OCR-string correction or exhaustive semantic proofreading.

## Round result

- **5 PDFs / 196 pages** completed.
- chunk_039: **236/236 visual closure COMPLETE**.
- chunk_040: **160/243 visual coverage** at `p0001-p0160`.
- Raw OCR files were not rewritten; OCR strings were not exhaustively proofread page by page.

## Calibration policy

The current work is page-level visual/layout calibration. Exact quotation from handwriting-heavy, mounted-board, clipped or composite pages remains scan-first. Pages marked usable-with-noise are retrieval-usable but still require direct scan verification for quotation.

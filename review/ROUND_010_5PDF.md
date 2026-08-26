# Huizinga visual calibration — five-PDF round 010

Date: 2026-08-26

Operational unit: five supplied scan PDFs. This round opens chunk_039 and reviews its first 200 pages (`p0001-p0200`). Raw PaddleOCR JSON files are not rewritten by this pass.

## Inputs completed

1. `chunk_039__p0001-0040.pdf` — 40 pages
2. `chunk_039__p0041-0080.pdf` — 40 pages
3. `chunk_039__p0081-0120.pdf` — 40 pages
4. `chunk_039__p0121-0160.pdf` — 40 pages
5. `chunk_039__p0161-0200.pdf` — 40 pages

Total scan pages visually reviewed: **200**.

## Round 010 visual class counts

Across all five PDFs:

- high-noise-layout-risk: **145**
- blank-no-substantive-visual: **50**
- short-text-or-nontext: **0**
- usable-with-noise-visual: **5**

Segment breakdown:

- `chunk_039:p0001-p0040`: 28 high-noise, 11 blank/no-substantive, 1 usable-with-noise
- `chunk_039:p0041-p0080`: 29 high-noise, 10 blank/no-substantive, 1 usable-with-noise
- `chunk_039:p0081-p0120`: 28 high-noise, 11 blank/no-substantive, 1 usable-with-noise
- `chunk_039:p0121-p0160`: 30 high-noise, 9 blank/no-substantive, 1 usable-with-noise
- `chunk_039:p0161-p0200`: 30 high-noise, 9 blank/no-substantive, 1 usable-with-noise

## chunk_039 opening

The first 200 pages retain the corpus's dominant dark mounting-board / multi-slip morphology. Most nonblank pages contain several independently oriented manuscript or catalogue fragments, so they remain high-noise/layout-risk even where individual slips are legible.

Five pages are stronger retrieval exceptions after selective higher-resolution inspection:

- `p0026`: two large handwritten linear sheets beside an envelope; internal order is substantially clearer than the surrounding slip boards.
- `p0066`: two large handwritten linear slips with a simple top-to-bottom sequence.
- `p0111`: a single large ledger/form card; rotation remains a nuisance, but the object itself has a clear internal order.
- `p0126`: one large handwritten linear sheet paired with a blank source card.
- `p0169`: a large university-library request card beside an envelope; the document is internally linear and visually distinct from the usual mounted-slip composites.

`p0092` was checked at higher resolution and is an empty lined source strip, so it is blank/no-substantive rather than short text. No short/nontext control was identified in the reviewed 200-page span.

## Remaining chunk_039 coverage

The supplied but not yet reviewed tail is:

- `p0201-p0236` — 36 pages

Chunk_039 therefore stands at **200/236 page-level visual coverage**.

The next exact five-PDF round can combine this 36-page tail with `chunk_040:p0001-p0040`, `p0041-p0080`, `p0081-p0120`, and `p0121-p0160` for **196 pages**, closing chunk_039 and opening chunk_040 through `p0160`.

## OCR boundary

No indexed raw OCR file for chunk_039 was found in the current repository search, so this is visual/layout calibration only and does not claim OCR-string correction or exhaustive semantic proofreading.

## Round result

- **5 PDFs / 200 pages** completed.
- chunk_039: **200/236 visual coverage** at `p0001-p0200`.
- Current chunk_039 aggregate: **145 high-noise / 50 blank / 0 short / 5 usable**.
- Raw OCR files were not rewritten; OCR strings were not exhaustively proofread page by page.

## Calibration policy

The current work is page-level visual/layout calibration. Exact quotation from handwriting-heavy, mounted-board, clipped or composite pages remains scan-first. Pages marked usable-with-noise are retrieval-usable but still require direct scan verification for quotation.

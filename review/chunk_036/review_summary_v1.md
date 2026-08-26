# chunk_036 page-level visual pass v1

Round 006 opens chunk_036 with four contiguous 40-page scan PDFs and establishes page-level visual calibration through `p0160`. Raw PaddleOCR JSON remains unchanged.

## Scope

Reviewed: **p0001-p0160 (160 pages across four PDFs)**.

Remaining visual span: **p0161-p0240 (80 pages across two supplied PDFs)**.

## Visual class counts

Across p0001-p0160:

- high-noise-layout-risk: **113**
- blank-no-substantive-visual: **39**
- short-text-or-nontext: **4**
- usable-with-noise-visual: **4**

Segment breakdown:

- `p0001-p0040`: 30 high-noise, 10 blank/no-substantive
- `p0041-p0080`: 23 high-noise, 9 blank/no-substantive, 4 short/nontext, 4 usable-with-noise
- `p0081-p0120`: 29 high-noise, 11 blank/no-substantive
- `p0121-p0160`: 31 high-noise, 9 blank/no-substantive

The dominant morphology is dark archival mounting board with many small handwritten/typed slips and spatial/non-linear reading order. Selective higher-resolution inspection of `p0041-p0048` identifies physical book/spine objects at `p0041-p0042` and `p0047-p0048`, while `p0043-p0046` are large handwritten/linear manuscript sheets. The latter four are classified usable-with-noise because their source body is large and linear even where scan noise or rotation remains.

## OCR provenance and limit

`chunk_036.pdf_by_PaddleOCR.json` is present in the repository and remains unchanged by this pass. The current work is **scan morphology / page-level visual calibration**; it does not claim OCR-string correction or exhaustive semantic proofreading of every nonblank source region.

## Current result

`chunk_036`: **160/240 page-level visual coverage**. The remaining supplied spans `p0161-p0200` and `p0201-p0240` are the next closure target.

Exact quotation from mounted-slip, composite, handwriting-heavy or otherwise high-noise pages remains scan-first.

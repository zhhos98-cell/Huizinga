# Huizinga visual calibration — five-PDF round 006

Date: 2026-08-26

Operational unit: five supplied scan PDFs. This round closes the sole remaining chunk_034 visual gap and opens chunk_036 through `p0160`. Raw PaddleOCR JSON files are not rewritten by this pass.

## Inputs completed

1. `chunk_034__p0081-0120.pdf` — 40 pages
2. `chunk_036__p0001-0040.pdf` — 40 pages
3. `chunk_036__p0041-0080.pdf` — 40 pages
4. `chunk_036__p0081-0120.pdf` — 40 pages
5. `chunk_036__p0121-0160.pdf` — 40 pages

Total scan pages visually reviewed: **200**.

## Round 006 visual class counts

Across all five PDFs:

- high-noise-layout-risk: **143**
- blank-no-substantive-visual: **48**
- short-text-or-nontext: **5**
- usable-with-noise-visual: **4**

Segment breakdown:

- `chunk_034:p0081-p0120`: 30 high-noise, 9 blank/no-substantive, 1 short/nontext
- `chunk_036:p0001-p0040`: 30 high-noise, 10 blank/no-substantive
- `chunk_036:p0041-p0080`: 23 high-noise, 9 blank/no-substantive, 4 short/nontext, 4 usable-with-noise
- `chunk_036:p0081-p0120`: 29 high-noise, 11 blank/no-substantive
- `chunk_036:p0121-p0160`: 31 high-noise, 9 blank/no-substantive

## chunk_034 closure

The former gap `p0081-p0120` is now visually classified. Together with earlier rounds, chunk_034 reaches **246/246 page-level visual closure**.

The gap is dominated by dark archival mounting boards carrying multiple slips/cards and non-linear reading order. Selective higher-resolution checks classify `p0111` as short/minimal and confirm `p0112` as genuinely blank/no-substantive.

Reconciled whole-chunk aggregate after gap closure (using higher-resolution control `p0073=blank/no-substantive` as authoritative over its older row-manifest label):

- high-noise-layout-risk: **174**
- blank-no-substantive-visual: **55**
- short-text-or-nontext: **13**
- usable-with-noise-visual: **4**

## chunk_036 opening

Round 006 reviews `p0001-p0160`, bringing chunk_036 to **160/240 page-level visual coverage**. The remaining visual span is `p0161-p0240`.

Most reviewed pages retain the familiar mounting-board / multi-slip morphology and therefore carry segmentation and reading-order risk. A short morphology break occurs at `p0041-p0048`: higher-resolution inspection identifies physical book/spine objects at `p0041-p0042` and `p0047-p0048`, while `p0043-p0046` are large handwritten/linear manuscript sheets that are materially more retrieval-usable despite scan noise and rotation.

## Round result

- **5 PDFs / 200 pages** completed.
- chunk_034: **246/246 visual closure COMPLETE**.
- chunk_036: **160/240 visual coverage**; `p0161-p0240` remains.
- Raw OCR files remain unchanged; this is page-level visual/layout calibration, not exhaustive OCR-string semantic proofreading.

## Calibration policy

The current work is page-level visual/layout calibration. Except for explicit selective higher-resolution controls, OCR strings were not exhaustively proofread page by page. Exact quotation from handwriting-heavy, mounted-board or composite pages remains scan-first.

# Huizinga visual calibration — five-PDF round 009

Date: 2026-08-26

Operational unit: five supplied scan PDFs. This round reviews every remaining supplied span of chunk_038 and closes the chunk at 226/226 page-level visual coverage. Raw PaddleOCR JSON files are not rewritten by this pass.

## Inputs completed

1. `chunk_038__p0001-0040.pdf` — 40 pages
2. `chunk_038__p0041-0080.pdf` — 40 pages
3. `chunk_038__p0081-0120.pdf` — 40 pages
4. `chunk_038__p0161-0200.pdf` — 40 pages
5. `chunk_038__p0201-0226.pdf` — 26 pages

Total scan pages visually reviewed: **186**.

## Round 009 visual class counts

Across all five PDFs:

- high-noise-layout-risk: **124**
- blank-no-substantive-visual: **37**
- short-text-or-nontext: **1**
- usable-with-noise-visual: **24**

Segment breakdown:

- `chunk_038:p0001-p0040`: 30 high-noise, 9 blank/no-substantive, 1 short/nontext
- `chunk_038:p0041-p0080`: 32 high-noise, 7 blank/no-substantive, 1 usable-with-noise
- `chunk_038:p0081-p0120`: 17 high-noise, 2 blank/no-substantive, 21 usable-with-noise
- `chunk_038:p0161-p0200`: 26 high-noise, 12 blank/no-substantive, 2 usable-with-noise
- `chunk_038:p0201-p0226`: 19 high-noise, 7 blank/no-substantive

## chunk_038 closure

Adding Round 009 to the Round 008 `p0121-p0160` pass brings chunk_038 to **226/226 page-level visual closure**.

Whole-chunk aggregate:

- high-noise-layout-risk: **150**
- blank-no-substantive-visual: **42**
- short-text-or-nontext: **2**
- usable-with-noise-visual: **32**

The dominant morphology remains dark archival mounting board with many small slips, fragments and blank source cards. The main exception is a sustained retrieval-stronger packet at `p0100-p0120`: `p0100-p0118` are large, internally linear printed catalogue/clipping pages and `p0119-p0120` are page-scale typed sheets. These twenty-one pages have substantially clearer reading order than the mounted-slip regime and are classified usable-with-noise.

Additional retrieval-stronger exceptions are `p0055`, a pair of large handwritten linear sheets, and `p0191` plus `p0196`, where large handwritten sheets retain a clear top-to-bottom order despite envelopes, rotation and scan noise. A new short/nontext control is `p0013`, an envelope/file-object page with only minimal label text. Higher-resolution review also confirms `p0179-p0180` as blank/no-substantive rather than short-text pages.

The Round 008 morphology break remains part of the whole-chunk usable packet at `p0121-p0122`, `p0125-p0126`, and `p0130-p0133`; `p0127` remains the earlier short/nontext control.

No indexed raw OCR file for chunk_038 was found in the current repository search, so this closure is visual/layout calibration only and does not claim OCR-string correction.

## Round result

- **5 PDFs / 186 pages** completed.
- chunk_038: **226/226 visual closure COMPLETE**.
- Whole-chunk visual aggregate: **150 high-noise / 42 blank / 2 short / 32 usable**.
- Raw OCR files were not rewritten; OCR strings were not exhaustively proofread page by page.

## Calibration policy

The current work is page-level visual/layout calibration. Exact quotation from handwriting-heavy, mounted-board, clipped-newspaper or composite pages remains scan-first. Pages marked usable-with-noise are retrieval-usable but still require direct scan verification for quotation.

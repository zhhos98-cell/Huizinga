# Huizinga visual calibration — five-PDF round 005

Date: 2026-08-26

Operational unit: five supplied scan PDFs. This round completes the five remaining chunk_035 segments. Raw PaddleOCR JSON files are not rewritten by this pass.

## Inputs completed

1. `chunk_035__p0041-0080.pdf` — 40 pages
2. `chunk_035__p0081-0120.pdf` — 40 pages
3. `chunk_035__p0121-0160.pdf` — 40 pages
4. `chunk_035__p0161-0200.pdf` — 40 pages
5. `chunk_035__p0201-0231.pdf` — 31 pages

Total scan pages visually reviewed: **191**.

## chunk_035 closure

Round 005 class counts:

- high-noise-layout-risk: **109**
- blank-no-substantive-visual: **58**
- short-text-or-nontext: **13**
- usable-with-noise-visual: **11**

Together with the 40 pages completed in round 004, chunk_035 reaches **231/231 page-level visual closure**.

Whole-chunk aggregate:

- high-noise-layout-risk: **137**
- blank-no-substantive-visual: **69**
- short-text-or-nontext: **14**
- usable-with-noise-visual: **11**

The dominant regime remains dark archival mounting board with many small source slips and non-linear reading order. A notable morphology change occurs around `p0121-p0127`, where large printed newspaper/periodical sources become directly readable at page scale. `p0129` is image-dominant. High-resolution blank checks were added at `p0128` and `p0209`.

## Round result

- **5 PDFs / 191 pages** completed.
- chunk_035: **231/231 visual closure COMPLETE**.
- New high-resolution blank controls: `p0128`, `p0209`.
- No indexed chunk_035 raw OCR file was found; this remains a visual/layout calibration closure, not OCR-string correction.

## Calibration policy

The current work is page-level visual/layout calibration. Except for explicit high-resolution controls, OCR strings were not exhaustively proofread page by page. Exact quotation from handwriting-heavy, mounted-board or composite pages remains scan-first.

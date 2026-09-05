# Huizinga visual calibration — five-PDF round 004

Date: 2026-08-26

Operational unit: five supplied scan PDFs. This round continues page-level visual/layout calibration. Raw PaddleOCR JSON files are not rewritten by this pass.

## Inputs completed

1. `chunk_033__p0001-0040.pdf` — 40 pages
2. `chunk_033__p0161-0200.pdf` — 40 pages
3. `chunk_034__p0161-0200.pdf` — 40 pages
4. `chunk_034__p0241-0246.pdf` — 6 pages
5. `chunk_035__p0001-0040.pdf` — 40 pages

Total scan pages visually reviewed: **166**.

## chunk_033 — closure of both former scan gaps

The two previously missing 40-page spans were visually classified page by page. Added class counts across the 80 pages:

- high-noise-layout-risk: **54**
- blank-no-substantive-visual: **18**
- usable-with-noise-visual: **3**
- short-text-or-nontext: **5**

High-resolution checks confirm `p0001` and `p0161` as genuine blank pale cards/sheets on the dark archival mounting background.

Together with the 156 pages reviewed in round 003, chunk_033 now has **236/236 page-level visual coverage**. Whole-chunk visual closure is therefore complete at the repository's retrieval-grade calibration standard. This does not convert the work into diplomatic transcription or exhaustive semantic proofreading of every nonblank OCR string.

## chunk_034 — p0161-p0200 plus final six-page tail

`p0161-p0200` adds 40 reviewed pages:

- high-noise-layout-risk: **26**
- blank-no-substantive-visual: **8**
- usable-with-noise-visual: **2**
- short-text-or-nontext: **4**

`p0241-p0246` adds 6 reviewed pages:

- high-noise-layout-risk: **5**
- blank-no-substantive-visual: **1**

High-resolution blank controls were added at `p0198` and `p0242`. The final tail is now closed. Chunk_034 page-level visual coverage advances from 160/246 to **206/246**. The only remaining visual gap is `p0081-p0120`.

## chunk_035 — first 40 pages

The first scan segment has now been visually classified:

- high-noise-layout-risk: **28**
- blank-no-substantive-visual: **11**
- short-text-or-nontext: **1**

The dominant regime is again dark archival mounting board with multiple small handwritten or typed slips and non-linear reading order. `p0001` was checked at full extracted-image resolution and is a genuine blank pale card. `p0029` is a sparse modern catalogue/cover sheet with only minimal metadata.

The repository currently has no indexed `chunk_035` raw OCR file, so this review layer records scan morphology and confidence limits only. The full local scan set visible to this session is 231 pages in six segments; after this round, page-level visual coverage is **40/231**.

## Round result

- **5 PDFs / 166 pages** completed.
- chunk_033: **236/236 visual closure COMPLETE**.
- chunk_034: **206/246 page-level visual**, only `p0081-p0120` remains.
- chunk_035: **40/231 page-level visual** started.
- New high-resolution blank controls: chunk_033 `p0001`, `p0161`; chunk_034 `p0198`, `p0242`; chunk_035 `p0001`.

## Calibration policy

The current work is page-level visual/layout calibration. Except for explicit high-resolution controls, OCR strings were not exhaustively proofread page by page. Exact quotation from handwritten, mounted-board, composite or otherwise high-noise pages remains scan-first.

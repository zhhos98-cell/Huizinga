# chunk_033 page-level visual pass v3 — whole-chunk closure

Round 004 supplied the two scan spans that had remained absent from the earlier review layer: `p0001-p0040` and `p0161-p0200`. Both spans were visually classified page by page while preserving `chunk_033.pdf_by_PaddleOCR-VL-1.6.json` unchanged.

## New scope

Reviewed in this pass:

- `chunk_033__p0001-0040.pdf` — 40 pages
- `chunk_033__p0161-0200.pdf` — 40 pages

Added page-level coverage: **80 pages**.

The compact run manifest is `page_visual_run_manifest_round004_missing_spans_v1.tsv`.

## New visual class counts

Across the two newly reviewed spans:

- high-noise-layout-risk: **54**
- blank-no-substantive-visual: **18**
- usable-with-noise-visual: **3**
- short-text-or-nontext: **5**

The same dark-board / mounted-slip regime dominates. A small minority of single printed clippings is comparatively OCR-friendly; envelopes and isolated cards are retained as short/minimal rather than inflated into long machine text.

High-resolution checks confirm `p0001` and `p0161` as genuine blank pale source cards/sheets.

## Whole-chunk result

The previous review covered 156 pages. Adding these 80 pages gives **236/236 page-level visual coverage** for chunk_033.

Aggregate visual classes across all 236 pages are:

- high-noise-layout-risk: **152**
- blank-no-substantive-visual: **45**
- usable-with-noise-visual: **23**
- short-text-or-nontext: **16**

The whole chunk is therefore visually closed at retrieval-grade calibration level.

## Hard limit

Whole-chunk visual closure does not mean word-perfect transcription. Raw OCR remains preserved, and nonblank OCR strings were not exhaustively semantically proofread. The direct `p0041` machine-pathology control remains especially important: mounted, spatial manuscript evidence must outrank invented mixed-script/table continuations in rough OCR.

# Huizinga visual calibration — five-PDF round 003

Date: 2026-08-26

Operational unit: five supplied scan PDFs. Raw PaddleOCR JSON files remain unchanged; calibration is written only to `review/`.

## Inputs completed

1. `chunk_033__p0041-0080.pdf` — 40 pages
2. `chunk_033__p0081-0120.pdf` — 40 pages
3. `chunk_033__p0121-0160.pdf` — 40 pages
4. `chunk_033__p0201-0236.pdf` — 36 pages
5. `chunk_034__p0201-0240.pdf` — 40 pages

Total scan pages visually reviewed: **196**.

## chunk_033 — four PDFs / 156 pages

All currently available chunk_033 scan pages were rendered and visually classified page by page. The four spans now have **156/156 available-page visual coverage**, represented compactly in `review/chunk_033/page_visual_run_manifest_available_spans_v1.tsv`.

Visual class counts across the 156 pages:

- high-noise-layout-risk: 98
- blank-no-substantive-visual: 27
- usable-with-noise-visual: 20
- short-text-or-nontext: 11

The dominant regime is the dark archival mounting board with multiple small source objects and nonlinear reading order. Printed clippings and full-sheet manuscript/notebook pages form the more OCR-friendly minority.

High-resolution checks establish new genuine blank controls at `p0094`, `p0123`, and `p0204`. `p0205` is a sparse but nonblank counter-control with a small visible note/envelope source region. The earlier `p0041` mixed-script / invented-table OCR pathology control remains in force.

The chunk is still not closed because scans `p0001-p0040` and `p0161-p0200` are absent. The new visual classification also does not claim exhaustive semantic proofreading of every raw OCR string.

## chunk_034 — p0201-p0240 / 40 pages

All 40 pages were rendered and visually classified. The span contains 29 high-noise layout pages, 9 genuine blank/no-substantive pages and 2 short/minimal-text pages.

Blank pages in this span are:

`p0201;p0205;p0208;p0214;p0222;p0225;p0228;p0233;p0238`.

`p0201` was re-rendered at high resolution and confirmed as a genuine blank pale card on the dark archival background. `p0217` was also re-rendered at high resolution and is a sparse but nonblank source: a small grey envelope/card carrying a short handwritten note.

This brings chunk_034 page-level visual coverage to **160/246 pages**: `p0001-p0080`, `p0121-p0160`, and `p0201-p0240`. The scan gaps `p0081-p0120` and `p0161-p0200` remain. The final locally available six-page tail `p0241-p0246` was deliberately left for the next five-PDF batch.

## Round result

- **5 PDFs / 196 pages** completed.
- chunk_033: all **156 currently available scan pages** now have page-level visual classification; whole-chunk closure still blocked by two missing 40-page spans.
- chunk_034: page-level visual coverage advanced from 120/246 to **160/246**; `p0241-p0246` remains queued.
- New high-resolution blank controls: chunk_033 `p0094`, `p0123`, `p0204`; chunk_034 `p0201`.
- New high-resolution sparse/nonblank control: chunk_034 `p0217`.

## Calibration policy

Raw PaddleOCR JSON remains unchanged. The current work is page-level visual/layout calibration. Except for established or high-resolution controls, OCR strings were not exhaustively proofread page by page. Exact quotation from handwritten, mounted-board, composite or otherwise high-noise pages remains scan-first.

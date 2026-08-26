# chunk_033 page-level visual pass v2

This pass upgrades all currently available chunk_033 scan spans from macro-only review to explicit page-level visual classification while preserving `chunk_033.pdf_by_PaddleOCR-VL-1.6.json` unchanged.

## Scope

Reviewed scan PDFs:

- `chunk_033__p0041-0080.pdf` — 40 pages
- `chunk_033__p0081-0120.pdf` — 40 pages
- `chunk_033__p0121-0160.pdf` — 40 pages
- `chunk_033__p0201-0236.pdf` — 36 pages

Total page-level visual coverage: **156 pages**. Missing scan spans remain `p0001-p0040` and `p0161-p0200`, so chunk-level closure is still impossible.

`page_visual_run_manifest_available_spans_v1.tsv` records the page-level classifications in contiguous runs. The run encoding is compact, but every page in the four available spans was rendered and visually checked before classification.

## Visual class counts

Across the 156 reviewed pages:

- high-noise-layout-risk: **98**
- blank-no-substantive-visual: **27**
- usable-with-noise-visual: **20**
- short-text-or-nontext: **11**

The dominant hazard remains the dark archival mounting board with multiple small handwritten or typed slips, envelopes, clipped fragments and nonlinear reading order. Full-sheet notebook/manuscript leaves and printed clippings form a smaller, more OCR-friendly regime.

## Controls

Prior controls remain valid: `p0041` is the direct mixed-script / invented-table semantic pathology control; `p0046`, `p0052`, `p0056`, `p0060`, and `p0071` are established blank controls; `p0049` and `p0068` are minimal-text controls.

This pass adds high-resolution blank controls at `p0094`, `p0123`, and `p0204`. Each is a genuinely blank pale source sheet/card on the dark archival background rather than a failed render. Representative sparse but nonblank material includes `p0205`, where a small note/envelope source region is visible.

The full visual blank/no-substantive set in the reviewed spans is:

`p0046;p0052;p0056;p0060;p0071;p0094;p0099;p0106;p0110;p0115;p0119;p0123;p0126;p0130;p0133;p0136;p0139;p0145;p0151;p0156;p0204;p0208;p0213;p0216;p0222;p0230;p0233`.

## Hard limit

This round does **not** claim line-by-line semantic proofreading of the raw OCR for every nonblank page. `ocr_signal=not_crosschecked_in_this_round` in the run manifest is deliberate. Existing exact OCR-pathology controls are retained, but the new work is page-level visual/layout calibration, not a full OCR-string closure.

Retrieval-grade whole-chunk completion therefore still requires both missing scan spans and, if desired, exhaustive page-by-page OCR usability calibration against those scans.

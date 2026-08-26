# chunk_033 review layer

This directory calibrates `chunk_033.pdf_by_PaddleOCR-VL-1.6.json` against the scan segments currently available to the review layer while preserving the raw PaddleOCR JSON unchanged.

## Current calibration level

All four currently available scan segments now have explicit page-level visual classification:

- `p0041-p0080` — 40/40 pages
- `p0081-p0120` — 40/40 pages
- `p0121-p0160` — 40/40 pages
- `p0201-p0236` — 36/36 pages

That gives **156/156 available scan pages visually classified**. The two missing spans `p0001-p0040` and `p0161-p0200` still prevent whole-chunk closure.

The compact `page_visual_run_manifest_available_spans_v1.tsv` encodes contiguous page runs with the same class/flags. It is a lossless compression of the page-level visual classification rather than a macro/contact-sheet-only label.

This work is still not diplomatic transcription and does not claim exhaustive OCR-string proofreading for every nonblank page. Newly classified pages carry `ocr_signal=not_crosschecked_in_this_round` unless an earlier exact control or a new high-resolution control exists.

## Main visual result

The dominant regime is the dark archival mounting board: multiple small handwritten or typed slips, envelopes, clipped fragments and nonlinear reading order. Smaller groups of full-sheet manuscript/notebook leaves and printed clippings are materially more OCR-friendly.

`p0041` remains the principal direct pathology control: the scan is a dense handwritten composite board while the rough OCR contains mixed-script substitutions and invented table-like semantics.

The expanded visual pass establishes 27 blank/no-substantive pages across the available spans. High-resolution controls at `p0094`, `p0123`, and `p0204` confirm that recurring pale source sheets/cards can be genuinely blank rather than rendering failures. `p0205` is a useful opposite sparse control: a small note/envelope source region is visibly present, so the page is minimal but not blank.

## Files

- `status.txt` — compact machine-readable state.
- `scan_availability_v1.tsv` — supplied/missing scan spans and page-level review status.
- `page_visual_run_manifest_available_spans_v1.tsv` — compact page-level visual classification for all 156 available scan pages.
- `calibration_controls_v1.tsv` — exact pathology/blank/minimal controls.
- `review_summary_v2.md` — strict scope, counts and limits of the page-level pass.
- `review_summary_v1.md` — earlier macro-level calibration narrative.

Whole-chunk completion is not claimed until `p0001-p0040` and `p0161-p0200` are supplied/reviewed. Full OCR-usability closure would additionally require page-by-page semantic checking of the raw OCR layer.

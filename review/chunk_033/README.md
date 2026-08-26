# chunk_033 review layer

This directory calibrates `chunk_033.pdf_by_PaddleOCR-VL-1.6.json` against the scan segments currently available to the review layer while preserving the raw PaddleOCR JSON unchanged.

## Current calibration level

A macro visual audit is complete for 156 scan pages in four supplied segments: `p0041-p0080`, `p0081-p0120`, `p0121-p0160`, and `p0201-p0236`.

The two missing spans `p0001-p0040` and `p0161-p0200` prevent chunk-level closure. The present layer is therefore scan-calibrated but partial. It is designed for retrieval and triage, not diplomatic transcription, and does not claim a full page-by-page OCR usability manifest.

## Main visual result

The reviewed material is strongly layout-dependent. Much of `p0041-p0160` consists of dark mounting boards carrying multiple slips, cards, letters, forms and clippings, often with handwriting, skew, rotated fragments and two-up/composite layouts. `p0201-p0236` continues with correspondence, manuscript material, cards and printed clippings/brochure-like pieces.

A direct pathology control is visible at `p0041`: the scan is a composite board of handwritten slips, while the corresponding rough OCR around the visible `[25]g` archival header contains mixed-script substitutions and invented table semantics. Exact quotation from such mounted-board pages must remain scan-first.

Confirmed visual blank/minimal controls within the first supplied segment include `p0046`, `p0052`, `p0056`, `p0060`, `p0068`, and `p0071`; `p0049` is an envelope/backside with only faint marks. See `calibration_controls_v1.tsv`.

## Files

- `status.txt` — compact machine-readable state.
- `scan_availability_v1.tsv` — supplied and missing scan spans.
- `calibration_controls_v1.tsv` — exact scan-level pathology/blank/minimal controls established in this pass.
- `review_summary_v1.md` — narrative account of the current partial visual calibration.

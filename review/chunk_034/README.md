# chunk_034 review layer

This directory calibrates `chunk_034.pdf_by_PaddleOCR-VL-1.6.json` against scan segments supplied to the review layer while preserving the raw PaddleOCR JSON unchanged.

## Current calibration level

The reviewed spans now have explicit page-level visual classification:

- `p0001-p0080` — 80 pages
- `p0121-p0160` — 40 pages
- `p0201-p0240` — 40 pages

That gives **160/246 pages visually classified**. The current scan gaps are `p0081-p0120` and `p0161-p0200`. The final six-page segment `p0241-p0246` is locally available but remains for the next batch.

The first two reviewed spans retain row-by-row manifests. The new `p0201-p0240` span is represented by `page_visual_run_manifest_p0201-p0240_v1.tsv`, which compactly encodes contiguous page runs with identical class/flags after every page was rendered and visually checked.

The OCR string layer is not closed. These visual manifests do not claim line-by-line semantic proofreading of every raw OCR string.

## Main visual result

The dominant documentary form is a dark archival mounting background carrying narrow handwritten/typed slips, envelopes, cards and other small source regions. Repeated pale blank cards are genuine source backsides/blank pieces rather than evidence of missing scans.

`p0001` remains the true-empty control matching empty raw OCR. `p0002` remains the catastrophic repeated-character over-generation control.

The new `p0201-p0240` pass contains 29 high-noise layout pages, 9 visually blank/no-substantive pages and 2 short/minimal-text pages. The blank set is `p0201;p0205;p0208;p0214;p0222;p0225;p0228;p0233;p0238`. High-resolution checking confirms `p0201` is genuinely blank. `p0217` is a sparse but nonblank counter-control containing a short handwritten note on a small grey envelope/card.

## Files

- `status.txt` — compact machine-readable state.
- `scan_availability_v1.tsv` — supplied/reviewed scan coverage and explicit gaps.
- `page_visual_manifest_p0001-p0080_v1.tsv` — row-level visual/layout audit for 80 pages.
- `page_visual_manifest_p0121-p0160_v1.tsv` — row-level visual/layout audit for 40 pages.
- `page_visual_run_manifest_p0201-p0240_v1.tsv` — compact page-level visual classification for the newly reviewed 40-page span.
- `review_summary_v2.md` — current scope, counts and limits.
- `calibration_controls_v1.tsv` — exact blank/pathology/minimal controls.
- `review_summary_v1.md` — earlier macro-level calibration narrative.

Whole-chunk visual completion is not claimed until the two missing 40-page spans and the final `p0241-p0246` tail are reviewed. Full OCR-usability closure would additionally require page-by-page OCR-string calibration.

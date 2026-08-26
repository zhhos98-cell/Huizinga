# chunk_034 review layer

This directory calibrates `chunk_034.pdf_by_PaddleOCR-VL-1.6.json` against scan segments supplied to the review layer while preserving the raw PaddleOCR JSON unchanged.

## Current calibration level

The first 40 scan pages, `p0001-p0040`, have been rendered and inspected at macro visual level in the current five-PDF review round. A later supplied segment `p0121-p0160` is available but deliberately remains for a later round; intervening pages were not supplied here.

The current state is therefore partial scan calibration, not chunk-level closure and not a diplomatic transcription.

## Main visual result

`p0001-p0040` is dominated by dark archival mounting boards carrying many small handwritten slips, often interleaved with envelope/card backs. The repeated blank-card/backside pattern is documentary structure, not evidence of dropped pages.

`p0001` is a genuine blank/no-substantive card and the baseline raw OCR is empty, making it a useful true-empty control. `p0002` is the opposite control: a dense composite board whose raw OCR contains some plausible fragments but also catastrophic repeated-character over-generation. The repeated Chinese `选` sequence is machine output and has no visual support on the scan.

Verified blank/no-substantive controls in this 40-page segment are `p0001`, `p0005`, `p0009`, `p0014`, `p0017`, `p0021`, `p0024`, `p0028`, `p0032`, and `p0039`.

## Files

- `status.txt` — compact machine-readable state.
- `scan_availability_v1.tsv` — current supplied/reviewed scan coverage.
- `calibration_controls_v1.tsv` — exact blank/pathology controls from `p0001-p0040`.
- `review_summary_v1.md` — narrative account of this partial scan calibration.

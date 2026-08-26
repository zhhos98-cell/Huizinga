# chunk_034 review layer

This directory calibrates `chunk_034.pdf_by_PaddleOCR-VL-1.6.json` against scan segments supplied to the review layer while preserving the raw PaddleOCR JSON unchanged.

## Current calibration level

Macro visual calibration is now complete for `p0001-p0080` and `p0121-p0160`, for a total of 120 reviewed scan pages. `p0001-p0040` was reviewed in five-PDF round 001; `p0041-p0080` and `p0121-p0160` were reviewed in five-PDF round 002.

The current state remains partial scan calibration, not chunk-level closure and not a diplomatic transcription. `p0081-p0120` and `p0161-p0200` are not present in the current local scan set. Later scan PDFs `p0201-p0240` and `p0241-p0246` are locally available but have not yet been included in a completed five-PDF review round.

## Main visual result

The reviewed spans are dominated by dark archival mounting backgrounds carrying handwritten/typed slips, cards, forms, envelope/card backs, signatures, stamps, and other small source objects. Repeated blank-card/backside patterns are documentary structure, not evidence of dropped pages.

In `p0001-p0040`, `p0001` is a genuine blank/no-substantive card and the baseline raw OCR is empty, making it a useful true-empty control. `p0002` is the opposite control: a dense composite board whose raw OCR contains some plausible fragments but also catastrophic repeated-character over-generation. The repeated Chinese `选` sequence is machine output and has no visual support on the scan.

Verified blank/no-substantive controls in the first segment are `p0001`, `p0005`, `p0009`, `p0014`, `p0017`, `p0021`, `p0024`, `p0028`, `p0032`, and `p0039`.

Round 002 adds two high-resolution negative controls: `p0073` and `p0125` are genuine blank source cards on dark backgrounds, not rendering failures. Any substantive OCR prose on these pages should therefore be treated as unsupported unless rechecked directly against the scan.

## Files

- `status.txt` — compact machine-readable state.
- `scan_availability_v1.tsv` — current supplied/reviewed scan coverage.
- `calibration_controls_v1.tsv` — exact blank/pathology controls from reviewed spans.
- `review_summary_v1.md` — narrative account of this partial scan calibration.

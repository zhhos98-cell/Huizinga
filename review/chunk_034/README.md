# chunk_034 review layer

This directory calibrates `chunk_034.pdf_by_PaddleOCR-VL-1.6.json` against scan segments supplied to the review layer while preserving the raw PaddleOCR JSON unchanged.

## Current calibration level

The reviewed spans now have genuine page-by-page visual manifests, not merely macro/contact-sheet labels:

- `p0001-p0080`: 80/80 page-level visual rows in `page_visual_manifest_p0001-p0080_v1.tsv`
- `p0121-p0160`: 40/40 page-level visual rows in `page_visual_manifest_p0121-p0160_v1.tsv`

That gives **120 page-level visually reviewed pages out of a 246-page chunk**. The chunk is therefore still partial, not closed and not a diplomatic transcription.

`p0081-p0120` and `p0161-p0200` are not present in the current supplied scan set. Later scan PDFs `p0201-p0240` and `p0241-p0246` are locally available but were not counted as reviewed in this completed five-PDF round.

The OCR string layer is also not closed: unlike `chunk_002`, these spans do not currently have per-page split OCR review artifacts suitable for an exhaustive empty/nonempty and semantic string audit. The manifests record visual/layout retrieval status without pretending to have proofread every OCR string.

## Main visual result

The reviewed spans are dominated by dark archival mounting backgrounds carrying handwritten/typed slips, cards, forms, envelope/card backs, signatures, stamps, and other small source objects. Repeated blank-card/backside patterns are documentary structure, not evidence of dropped pages.

In `p0001-p0040`, `p0001` is a genuine blank/no-substantive card and the baseline raw OCR is empty, making it a useful true-empty control. `p0002` is the opposite control: a dense composite board whose raw OCR contains some plausible fragments but also catastrophic repeated-character over-generation. The repeated Chinese `选` sequence is machine output and has no visual support on the scan.

Verified blank/no-substantive controls in the first segment are `p0001`, `p0005`, `p0009`, `p0014`, `p0017`, `p0021`, `p0024`, `p0028`, `p0032`, and `p0039`. `p0073` and `p0125` remain high-resolution negative controls for genuine blank source cards.

The `p0041-p0080` page-level pass confirms the same mounted-slip / envelope rhythm through most of the span. `p0070-p0071` form a distinct layout regime of full document sheets. `p0121-p0160` returns to mounted slip boards interleaved with genuine blank cards/backsides.

## Files

- `status.txt` — compact machine-readable state.
- `scan_availability_v1.tsv` — current supplied/reviewed scan coverage and explicit gaps.
- `page_visual_manifest_p0001-p0080_v1.tsv` — 80-row page-level visual/layout audit.
- `page_visual_manifest_p0121-p0160_v1.tsv` — 40-row page-level visual/layout audit.
- `review_summary_v2.md` — exact scope and limits of the current page-level state.
- `calibration_controls_v1.tsv` — exact blank/pathology controls from reviewed spans.
- `review_summary_v1.md` — earlier macro-level calibration narrative.

Chunk-level completion is not claimed until the missing scan spans are supplied/reviewed and the OCR string layer receives corresponding page-level calibration.

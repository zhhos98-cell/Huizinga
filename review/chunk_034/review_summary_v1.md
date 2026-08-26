# chunk_034 review summary

This review layer now visually calibrates `chunk_034:p0001-p0080` and `p0121-p0160` against the rough PaddleOCR layer while preserving `chunk_034.pdf_by_PaddleOCR-VL-1.6.json` unchanged. `p0001-p0040` was reviewed in five-PDF round 001; `p0041-p0080` and `p0121-p0160` were added in round 002.

## Result

- 120 scan pages have been rendered and visually inspected at macro level: `p0001-p0080` and `p0121-p0160`.
- The reviewed material is a coherent archival-card/mounting-board sequence with recurrent blank cards, backsides, typed and handwritten slips, forms, signatures, stamps, and small source regions.
- No gross page-order break, whole-page duplicate sequence, or rendering catastrophe was visible in the newly reviewed round-002 spans.
- OCR risk is dominated by composite/sparse layout, handwriting, tiny typewriting, rotations, card/background segmentation, and semantic over-generation rather than ordinary clean-print character error.
- This pass does not claim a full chunk-level page usability manifest or diplomatic transcription.

## Documentary/layout structure

In `p0001-p0040`, dark mounting boards carrying small handwritten slips alternate with envelope/card backs. The blank-card rhythm is visibly structural: `p0001`, `p0005`, `p0009`, `p0014`, `p0017`, `p0021`, `p0024`, `p0028`, `p0032`, and `p0039` are blank/no-substantive at scan level.

The same archival logic continues through `p0041-p0080` and `p0121-p0160`. Many pages contain one pale card or sheet against a dark background; others carry small typed/manuscript records, signatures, stamps, or form-like layouts. Sparse or blank photographed source objects must not be conflated with failed PDF rendering or dropped content.

## Direct calibration controls

`p0001` remains a clean true-empty control: the scan shows a blank card and the first raw OCR record is empty.

`p0002` remains a strong machine-pathology control. The scan is a dense mounted composite with handwritten slips and an envelope/backside. The corresponding raw OCR captures some plausible fragments but also produces an extremely long repeated Chinese `选` sequence with no visual support.

Round 002 adds two further high-confidence blank-source controls. `p0073` (local p33 of `chunk_034__p0041-0080.pdf`) was re-rendered at higher resolution and is a genuinely blank pale card on a dark background. `p0125` (local p5 of `chunk_034__p0121-0160.pdf`) was likewise checked at higher resolution and is a genuine blank source card. These controls distinguish source-level blankness from rendering failure and from any unsupported substantive OCR text.

## Coverage and hard limits

Reviewed: `p0001-p0080`, `p0121-p0160`.

Not locally supplied in the current scan set: `p0081-p0120`, `p0161-p0200`.

Locally available but not yet reviewed in a completed five-PDF round: `p0201-p0240`, `p0241-p0246`.

Full chunk closure therefore remains pending. Exact quotation from handwritten, rotated, or composite archival pages must remain scan-first, and a page-by-page OCR usability/false-empty manifest is still a separate closure pass.

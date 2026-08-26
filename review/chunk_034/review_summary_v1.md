# chunk_034 review summary

This pass visually calibrates `chunk_034:p0001-p0040` against the rough PaddleOCR layer while preserving `chunk_034.pdf_by_PaddleOCR-VL-1.6.json` unchanged. The later supplied segment `p0121-p0160` was not included because the current operational unit is five PDFs.

## Result

- 40/40 pages in the supplied `p0001-p0040` segment were rendered and visually inspected at macro level.
- The segment is a coherent archival mounting-board sequence with recurrent blank card/backside separators; no gross page-order break or duplicate-page sequence was visible.
- OCR risk is dominated by composite layout, handwriting, small slips and semantic over-generation rather than ordinary clean-print character error.
- This pass does not claim a full chunk-level page usability manifest.

## Documentary/layout structure

Most substantive pages are dark mounting boards carrying one or two columns of small handwritten slips. Envelope or card backs recur between these boards. The blank-card rhythm is visibly structural: `p0001`, `p0005`, `p0009`, `p0014`, `p0017`, `p0021`, `p0024`, `p0028`, `p0032`, and `p0039` are blank/no-substantive at scan level.

`p0033-p0035` contain envelope/backside material with short handwritten labels and, at `p0035`, a return to a mounted slip board. `p0036-p0038` are again dense mounted-board pages. `p0040` combines an envelope/backside with another mounted board.

## Direct calibration controls

`p0001` is a clean true-empty control: the scan shows a blank card and the first raw OCR record is empty.

`p0002` is a strong machine-pathology control. The scan is a dense mounted composite with handwritten slips and an envelope/backside. The corresponding raw OCR identifies the visible archival header approximately and captures fragments, but then produces an extremely long repeated Chinese `选` sequence inside a text block. Nothing in the scan supports that output. The page must therefore be classified `high-noise`, with exact reading deferred to the scan.

This pair is useful for later page-level calibration: raw emptiness can be correct on genuine blank cards, while a non-empty structured OCR response can still be catastrophically wrong on visually dense composite manuscript boards.

## Hard limits

No claim is made here for `p0041-p0120` or pages after `p0160`, because those spans are not part of this review input. `p0121-p0160` is locally available but deliberately deferred to a later five-PDF round.

Full chunk closure requires the remaining scan sequence plus a page-by-page OCR usability/false-empty pass. Exact quotation from the mounted handwritten boards must remain scan-first.

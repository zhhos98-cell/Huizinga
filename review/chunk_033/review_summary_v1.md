# chunk_033 review summary

This pass visually calibrates the currently supplied scan spans against the rough PaddleOCR layer while preserving `chunk_033.pdf_by_PaddleOCR-VL-1.6.json` unchanged. It covers 156 scan pages: `p0041-p0160` and `p0201-p0236`. The missing spans `p0001-p0040` and `p0161-p0200` prevent full chunk closure.

## Result

- 156 supplied scan pages rendered and visually inspected at macro level.
- No gross page-order break or duplicate-page sequence was visible within the four supplied segments.
- The dominant OCR risk is not ordinary character error but layout failure on mounted composite boards, handwriting, small source regions, skew/rotation and semantic over-generation.
- A full page-by-page OCR usability/false-empty manifest is not claimed in this pass.

## Reviewed documentary/layout sequence

`p0041-p0080` begins with dark archival mounting boards carrying multiple handwritten slips, frequently two boards/pages within one scan. Several blank or near-blank card/backside pages interrupt the mounted sequence. Around `p0065-p0072` the physical form shifts toward manuscript/notebook leaves and small mounted items; `p0073-p0076` contains a printed *Astronomische Chronologie* brochure/booklet, followed by newspaper clippings through `p0080`.

`p0081-p0120` remains materially heterogeneous: letters, cards, forms, printed clippings, handwritten notes and occasional diagram/image-like components. Many pages are tilted or composite, so linear OCR reading order is unreliable even when individual snippets are partly legible.

`p0121-p0160` continues with correspondence, cards, clippings and mixed typed/printed/handwritten material. Sparse backsides and small-card pages coexist with dense source pages. The scan sequence itself appears coherent, but retrieval must remain page-image aware.

`p0201-p0236` moves through dark-mounted letters/cards, handwritten correspondence or notebook-like material, small cards and then printed/clipping/brochure-like pieces. Several pages contain a small source region inside a large dark frame, increasing both false-empty and hallucination risk.

## Direct calibration controls

`p0041` is a strong negative control for trusting the raw semantic layer. Visually it is a dense composite board of handwritten slips. The rough OCR around the same visible `[25]g` archival header contains mixed-script substitutions and invented table-like semantics. This is the same failure family already documented in earlier Huizinga chunks: plausible-looking machine prose or structured output can be less reliable than a visibly difficult manuscript page warrants.

Verified blank/no-substantive pages in the directly checked opening segment are `p0046`, `p0052`, `p0056`, `p0060`, and `p0071`. `p0049` is an envelope/backside with only faint marks; `p0068` is an almost blank ruled spread with a tiny annotation. These are useful controls when evaluating raw empty versus non-empty OCR behavior.

## Hard limits

The review does not infer content for `p0001-p0040` or `p0161-p0200`, because those scans were not supplied. It also does not promote OCR-only lexical hits into research evidence without a page-image match. Exact quotation from mounted boards or handwriting requires direct high-resolution scan checking.

Full chunk closure requires the two missing scan spans and a page-level OCR usability/false-empty manifest across the complete sequence.

# chunk_056 visual calibration span p0121-p0160

Date: 2026-08-27

Input: `chunk_056__p0121-0160.pdf` (40 pages).

Raw PaddleOCR JSON is preserved unchanged. This is retrieval-grade visual/OCR usability calibration, not exhaustive semantic proofreading of every OCR string.

## Visual class counts

- high-noise-layout-risk: 9
- blank-no-substantive-visual: 3
- short-text-or-nontext: 21
- usable-with-noise-visual: 7

## Morphology

- `p0121-p0127`: strongest retrieval-oriented packet in this span; narrow but internally linear handwritten leaves/slips paired with blank supports, with clear local reading order.
- `p0128-p0135`: transition through blank controls, sparse covers/cards, and one composite mounted packet at `p0130`.
- `p0136-p0139`: multi-piece mounted handwritten composites; reading-order risk returns.
- `p0140-p0156`: dominated by sparse card/index-card material and briefkaart-like controls; largely short/minimal rather than retrieval-strong prose.
- `p0157-p0160`: dense mounted-slip boards resume and are classified high-noise-layout-risk.

Page-level decisions are recorded in `review/chunk_056/page_visual_run_manifest_p0121-p0160_v1.tsv`.

This span was processed independently; chunk-level status/roll-up consolidation is intentionally left to the thread closing the surrounding chunk spans.
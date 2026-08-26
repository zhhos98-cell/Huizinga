# chunk_034 page-level visual pass v2

The reviewed scan spans now have explicit page-level visual classification rather than macro-only labels. The raw PaddleOCR JSON remains unchanged.

## Current result

Page-level visual coverage now includes:

- `p0001-p0080` — 80 pages
- `p0121-p0160` — 40 pages
- `p0201-p0240` — 40 pages

Total: **160/246 pages visually classified**. The current scan gaps remain `p0081-p0120` and `p0161-p0200`. `p0241-p0246` is locally available but was not part of this completed five-PDF round.

The older row manifests remain authoritative for `p0001-p0080` and `p0121-p0160`. The new `page_visual_run_manifest_p0201-p0240_v1.tsv` compactly encodes contiguous page runs with the same visual class/flags; every page in the 40-page span was rendered and visually checked before classification.

## Visual result for p0201-p0240

The new span is dominated by dark mounting boards carrying narrow handwritten/typed slips and envelopes, with repeated blank source cards interleaved at regular intervals.

Visual class counts for `p0201-p0240`:

- high-noise-layout-risk: **29**
- blank-no-substantive-visual: **9**
- short-text-or-nontext: **2**

The confirmed blank/no-substantive pages in this span are:

`p0201;p0205;p0208;p0214;p0222;p0225;p0228;p0233;p0238`.

`p0201` was re-rendered at high resolution and is a genuine blank pale source card on the dark archival background. `p0217` is the opposite sparse control: a small grey envelope/card carries a short handwritten note, so it is minimal but not blank.

## Existing controls retained

`p0001` remains the true-empty control matching empty raw OCR. `p0002` remains the catastrophic repeated-character over-generation control. Earlier blank controls are unchanged, including the high-resolution blank controls `p0073` and `p0125`.

## What is not claimed complete

The OCR strings for the reviewed chunk_034 spans are not split into per-page review artifacts comparable to `_tmp_chunk002_pages`. These manifests therefore record page-level visual/layout status, not semantic proofreading of every OCR string. No full OCR-usability closure is claimed.

Whole-chunk visual closure still requires the two missing 40-page spans plus the final six-page `p0241-p0246` segment. Full OCR closure would additionally require page-by-page OCR-string calibration.

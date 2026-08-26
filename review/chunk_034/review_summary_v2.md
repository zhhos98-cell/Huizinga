# chunk_034 page-level visual pass v2

The reviewed scan spans now have true page-by-page visual manifests rather than macro-only labels. `p0001-p0080` is represented in `page_visual_manifest_p0001-p0080_v1.tsv`; `p0121-p0160` is represented in `page_visual_manifest_p0121-p0160_v1.tsv`. The raw PaddleOCR JSON remains unchanged.

## Current result

- page-level visual coverage: **120 pages total** = `p0001-p0080` + `p0121-p0160`
- whole-chunk page-level visual coverage: **120/246**, therefore **NOT COMPLETE**
- current scan gaps: `p0081-p0120` and `p0161-p0200`
- available but not reviewed in this completed five-PDF round: `p0201-p0240` and `p0241-p0246`

`p0001-p0040` retains the earlier exact controls: `p0001` is the true-empty control; `p0002` is the catastrophic repeated-character over-generation control; prior blank/no-substantive controls are `p0001;p0005;p0009;p0014;p0017;p0021;p0024;p0028;p0032;p0039`.

The new page-level `p0041-p0080` pass confirms the same mounted-slip / envelope rhythm through most of the span, with full document sheets at `p0070-p0071` forming a distinct layout regime. The page-level `p0121-p0160` pass is again dominated by mounted slip boards interleaved with genuine blank cards/backsides; `p0125` remains a high-resolution blank control.

## What is not claimed complete

The OCR strings for the chunk_034 reviewed spans are not split into per-page review artifacts comparable to `_tmp_chunk002_pages`. These manifests therefore record page-level visual/layout status, not page-level semantic proofreading of every OCR string. No full OCR-usability closure is claimed.

## Visual class counts

For `p0001-p0080`:

- high-noise-layout-risk: 54
- blank-no-substantive-visual: 17
- short-text-or-nontext: 7
- usable-with-noise-visual: 2

For `p0121-p0160`:

- high-noise-layout-risk: 30
- blank-no-substantive-visual: 10

The dominant structural hazard is the mounted archival board: multiple small source objects, nonlinear reading order, frequent envelope/backside partners, and text regions too small for safe OCR-first interpretation.

# chunk_002 review layer

This directory calibrates `chunk_002.pdf_by_PaddleOCR-VL-1.6.json` against the archival scan set while preserving the raw PaddleOCR JSON unchanged.

## Current calibration level

All three contiguous 61-page PDF segments are available and form `p0001-p0183`. The former scan/page-alignment blocker is resolved.

The current review now has a genuine page-by-page visual pass for **183/183 pages**, recorded in `full_page_visual_empty_signal_manifest_v1.tsv`. The same pass exhaustively cross-checks the split-OCR baseline empty/nonempty signal for all 183 pages and therefore closes the baseline-empty/false-empty question.

This is stronger than the former macro-only state, but it is still important not to overstate the result: every page has been visually classified, while every nonempty OCR string has **not** been semantically proofread line by line. Thus page-level visual retrieval is complete; full semantic OCR-usability closure remains incomplete.

## Scan set

- `p0001-p0061`: `/Huizinga/chunk_002_1-61.pdf`
- `p0062-p0122`: `/Huizinga/chunk_002_62-122.pdf`
- `p0123-p0183`: `/Huizinga/chunk_002_123-183.pdf`

## Exhaustive empty / false-empty result

The raw split OCR is empty on exactly ten pages:

`p0001;p0005;p0015;p0016;p0048;p0053;p0096;p0137;p0174;p0175`

Nine are visually true blank/no-substantive pages. `p0016` is the single false-empty recovery: its split OCR is empty, but faint substantive text is visible in the scan.

Two nonempty machine-pathology controls remain especially useful:

- `p0089`: normal continuous French handwriting becomes catastrophic repeated-number/table-like output.
- `p0143`: a backside/blank-slip montage produces unsupported modern `2024`/numeric material.

## Visually secured retrieval complexes

1. Zeeland / Middelburg opening boards: p0001-p0008; the literal envelope label `Zelandensia` is visible at p0006.
2. Salimbene / medieval Italy: p0011 is the title card `Salimbene 1914/15`; notes continue at p0012.
3. Florence communal / factional / art-historical material: visually established in the dense notebook sequence around p0029-p0048.
4. `Trois esprits prégothiques < Paris 1930 >`: title card at p0049, followed by the long French twelfth-century packet.

## Highest-value corrected anchors

- p0086 (manuscript p.31): `Cet élément ludique` plus competition/disputation is visible in the scan.
- p0087 (ms p.32): `primitive` is visible in the continuation of the same medieval intellectual-history argument.
- p0090 (ms p.35): Abélard is positioned not simply as a precursor of the Renaissance but `au contraire comme un prégothique`; nearby language retains the primitive/apparatus argument.

## Files

- `status.txt` — compact machine-readable state.
- `full_page_visual_empty_signal_manifest_v1.tsv` — 183/183 page-level visual classifications plus exhaustive baseline empty/nonempty signal and false-empty audit.
- `review_summary_v2.md` — exact scope and limits of the page-level closure pass.
- `review_summary_v1.md` — earlier scan-calibrated substantive review.
- `core_theme_hits_v1.md` — research-relevant OCR hits and negative controls.
- `composite_page_structure_v1.tsv` — scan-aligned packet structure.
- `ocr_anchor_index_v1.tsv` — OCR/source anchors with absolute pages and visual status.
- `scan_availability_v1.tsv` — complete contiguous scan coverage.
- `visual_anchor_alignment_v2.tsv` — direct raw-batch-to-scan alignment and priority corrections.
- `alignment_blocker_v1.md` — historical blocker note, now marked RESOLVED.

For exact quotation, continue to read the scan directly. `usable-with-noise` in the page manifest is a visual/layout retrieval class, not a diplomatic-transcription guarantee.

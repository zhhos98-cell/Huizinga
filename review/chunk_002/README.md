# chunk_002 review layer

This directory calibrates `chunk_002.pdf_by_PaddleOCR-VL-1.6.json` against the archival scan set while preserving the raw PaddleOCR JSON unchanged.

## Current calibration level

The former scan/page-alignment blocker is resolved. All three contiguous 61-page PDF segments are available and form `p0001-p0183`. All 183 pages have been rendered and inspected at macro visual level; priority OCR anchors were re-rendered at higher resolution and compared directly with the manuscript scans.

Absolute `pXXXX` citation is therefore restored for the verified raw anchors. This does not make the rough JSON a diplomatic transcription: composite mounted boards, dense handwriting and severe machine over-generation still require scan-first reading for exact quotation.

## Scan set

- `p0001-p0061`: `/Huizinga/chunk_002_1-61.pdf`
- `p0062-p0122`: `/Huizinga/chunk_002_62-122.pdf`
- `p0123-p0183`: `/Huizinga/chunk_002_123-183.pdf`

The previously missing middle segment is now present. See `scan_availability_v1.tsv`.

## Visually secured retrieval complexes

1. Zeeland / Middelburg opening boards: p0001-p0008; the literal envelope label `Zelandensia` is visible at p0006.
2. Salimbene / medieval Italy: p0011 is the title card `Salimbene 1914/15`; notes continue at p0012.
3. Florence communal / factional / art-historical material: visually established in the dense notebook sequence around p0029-p0048.
4. `Trois esprits prégothiques < Paris 1930 >`: title card at p0049, followed by the long French twelfth-century packet.

## Highest-value corrected anchors

- p0086 (manuscript p.31): `Cet élément ludique` plus competition/disputation is visible in the scan.
- p0087 (ms p.32): `primitive` is visible in the continuation of the same medieval intellectual-history argument.
- p0090 (ms p.35): Abélard is positioned not simply as a precursor of the Renaissance but `au contraire comme un prégothique`; nearby language retains the primitive/apparatus argument.

These findings promote the play / competition / primitive / Renaissance complex from OCR-only lead to scan-verified evidence. `visual_anchor_alignment_v2.tsv` records raw UUID-to-page alignment and the correction of the earlier loose `Zelandensia` UUID association.

## OCR pathology policy

The rough JSON contains catastrophic over-generation as well as ordinary handwriting errors. p0089 is a direct control: a normal continuous French manuscript leaf becomes a huge repeated-number/table continuation in OCR. Generated modern-English `play`, long numerical strings, mixed scripts and contemporary/biomedical intrusions remain excluded from historical evidence unless the scan supports them.

Raw-OCR negative controls for `Malinowski`, `anthropolog*` and `ethnolog*` remain in force. The verified p0087 `primitive` passage stays in its immediate medieval intellectual-history context.

## Files

- `status.txt` — current machine-readable state.
- `review_summary_v1.md` — scan-calibrated substantive review.
- `core_theme_hits_v1.md` — research-relevant OCR hits and negative controls.
- `composite_page_structure_v1.tsv` — scan-aligned packet structure.
- `ocr_anchor_index_v1.tsv` — OCR/source anchors with absolute pages and visual status.
- `scan_availability_v1.tsv` — complete contiguous scan coverage.
- `visual_anchor_alignment_v2.tsv` — direct raw-batch-to-scan alignment and priority corrections.
- `alignment_blocker_v1.md` — historical blocker note, now marked RESOLVED.

A full page-by-page OCR usability/false-empty manifest remains a separate closure pass if chunk 002 is to be promoted to the exact same manifest standard as chunks 003-031.

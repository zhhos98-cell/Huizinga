# Huizinga visual calibration — five-PDF round 002

Date: 2026-08-26

Operational unit: five supplied scan PDFs. Raw PaddleOCR JSON files are preserved unchanged; calibration is written only to `review/`.

## Inputs completed

1. `chunk_002_1-61.pdf` — 61 pages
2. `chunk_002_62-122.pdf` — 61 pages
3. `chunk_002_123-183.pdf` — 61 pages
4. `chunk_034__p0041-0080.pdf` — 40 pages
5. `chunk_034__p0121-0160.pdf` — 40 pages

Total scan pages visually swept: **263**.

## Per-PDF calibration result

### `chunk_002_1-61.pdf`

The 61 pages are dark-background archival/microfilm-style scans, commonly carrying one or two pale paper slips, cards, forms, or manuscript leaves. Small typewriting, handwriting, signatures/stamps, source-object borders, rotations, and paired objects are the principal OCR hazards. Some photographed cards are genuinely blank or nearly blank; local p20 is a direct visual control showing blank source objects rather than missing rendering. No gross renderer failure, whole-page duplication, or sequence-level visual break was observed.

This is a revalidation of the already calibrated `chunk_002` scan set, not a replacement calibration. No new macro-level finding requires overriding the existing corrected/review layer.

### `chunk_002_62-122.pdf`

All 61 pages were visually swept. The same dark-mount archival structure continues: typed and manuscript sheets, cards/forms, occasional headings/logos, and recurrent blank or near-blank source objects. OCR risk remains concentrated in small source regions, handwriting, rotations, card/background segmentation, and multi-object reading order. No gross rendering catastrophe or sequence-level duplication was observed.

Result: existing `chunk_002` calibration is revalidated at macro level.

### `chunk_002_123-183.pdf`

All 61 pages were visually swept. The sequence again consists of archival boards or dark backgrounds carrying pale source objects, with mixed manuscript, typewritten, form, and card material. Later pages include several sparse or nearly blank photographed source sheets/cards. These are documentary objects, not evidence of dropped PDF rendering. No gross rendering failure or whole-page duplication was observed.

Result: existing `chunk_002` calibration is revalidated at macro level.

### `chunk_034__p0041-0080.pdf`

All 40 pages were visually swept. The segment continues the dark-background archival-card sequence, with small typed/handwritten record content, signatures, stamps, numbers, and index-card layouts. Local p33 (absolute `chunk_034:p0073`) was re-rendered at higher resolution and confirmed as a genuine blank source card on a dark background, not a rendering failure. No gross page-order or rendering break was observed.

Result: macro visual calibration PASS for `p0041-p0080`; `p0073` is added as a high-confidence blank/no-substantive negative control.

### `chunk_034__p0121-0160.pdf`

All 40 pages were visually swept. The same archival-card structure continues; denser writing is visible in parts of the later local sequence, while several pages are sparse or blank-card records. Local p5 (absolute `chunk_034:p0125`) was checked at higher resolution and confirmed as a genuine blank source card on a dark background. No gross rendering catastrophe was observed.

Result: macro visual calibration PASS for `p0121-p0160`; `p0125` is added as a high-confidence blank/no-substantive negative control.

## Round result

- **5 PDFs / 263 pages** completed.
- `chunk_002:p0001-p0183` received a complete second macro visual revalidation across all three 61-page source PDFs.
- `chunk_034` gained **80 newly reviewed pages**, bringing macro-reviewed coverage to `p0001-p0080` and `p0121-p0160`.
- A photographed blank card/sheet must not be treated as a missing rendered page. Blank-source controls remain important OCR negative controls.
- Dominant OCR hazards in this round are dark-background/source-object segmentation, tiny typewriting, handwriting/signatures/stamps, rotation, multi-object pages, and semantic over-generation on sparse/composite archival layouts.

## Calibration policy

This round is a macro visual calibration/revalidation pass with direct control pages. It does not claim diplomatic transcription or a complete page-level OCR usability/false-empty manifest. Exact quotation from manuscript/composite pages remains scan-first. Raw PaddleOCR JSON files remain unchanged.

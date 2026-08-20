# Chunk 006 visual review summary

Updated: 2026-08-20

## Scope and review level

- Source span: `chunk_006:p0001`–`chunk_006:p0180` (180 scan pages).
- Split scan set is complete and contiguous:
  - `chunk_006__p0001-0040.pdf`
  - `chunk_006__p0041-0080.pdf`
  - `chunk_006__p0081-0120.pdf`
  - `chunk_006__p0121-0160.pdf`
  - `chunk_006__p0161-0180.pdf`
- Page-count check: `40 + 40 + 40 + 40 + 20 = 180`; no scan-page gap remains.
- All 180 pages were visually checked against the clean PaddleOCR v3 baseline.
- Review level: **retrieval-grade visual correction layer**, not diplomatic or word-perfect transcription. Raw PaddleOCR is preserved unchanged.

## Page-level result

| class | pages |
|---|---:|
| usable | 47 |
| usable with noise | 66 |
| high-noise, close transcription required before exact quotation | 37 |
| false-empty OCR visually recovered | 3 |
| verified short-text pages | 3 |
| minimal/non-substantive visual marks | 2 |
| genuinely blank | 22 |
| **total** | **180** |

The full page-level audit is in `full_visual_audit_manifest_v1.tsv`.

## Layout and OCR behaviour

Chunk 006 changes documentary form part-way through. The opening section is dominated by full handwritten note pages; from roughly the mid-50s onward, many scans are mounting boards carrying multiple narrow handwritten or printed slips. The latter are much more vulnerable to reading-order errors, under-capture, and mixed-script hallucination, so the audit treats them conservatively as `usable_with_noise` unless the mismatch is severe.

The exact-quotation high-noise queue is:

`p0008`, `p0057`, `p0060`, `p0066`, `p0069`, `p0070`, `p0072`, `p0073`, `p0074`, `p0081`, `p0085`, `p0089`, `p0095`, `p0096`, `p0100`, `p0104`, `p0105`, `p0106`, `p0110`, `p0111`, `p0120`, `p0126`, `p0138`, `p0140`, `p0141`, `p0147`, `p0154`, `p0158`, `p0159`, `p0160`, `p0161`, `p0164`, `p0165`, `p0166`, `p0168`, `p0169`, `p0173`

Especially clear pathology includes:
- `p0008`: OCR expands to 6,276 characters although the scan contains only a small mounted note/card arrangement.
- `p0095`: v3 cleanup reduces a pathological OCR run from 10,767 to 1,016 characters.
- `p0164`: repetition cleanup reduces 7,426 characters to 132.
- `p0168`: repetition cleanup reduces 6,244 characters to 439.
- `p0081`, `p0085`, `p0096`, `p0104`, `p0110`, `p0126`, `p0158`, `p0161`, `p0165`, and `p0169`: substantial visible mounted notes are represented by very short or otherwise grossly inadequate OCR.
- `p0138`, `p0141`, `p0166`, and `p0173`: severe hallucination/mixed-script or digit-run behaviour makes verbatim use unsafe.

## Empty-OCR audit

Baseline OCR marks 26 pages empty:

`p0026, p0040, p0054, p0055, p0058, p0061, p0075, p0076, p0084, p0090, p0092, p0093, p0097, p0101, p0107, p0112, p0118, p0121, p0127, p0139, p0142, p0146, p0174, p0176, p0177, p0180`.

Final visual result:
- **22 genuinely blank / no substantive text**: `p0026`, `p0040`, `p0054`, `p0055`, `p0058`, `p0061`, `p0075`, `p0076`, `p0084`, `p0090`, `p0097`, `p0101`, `p0107`, `p0112`, `p0118`, `p0121`, `p0127`, `p0139`, `p0142`, `p0146`, `p0174`, `p0177`
- **3 substantive false-empty OCR pages**: `p0092`, `p0176`, `p0180`
- **1 non-substantive minimal mark**: `p0093` (a tiny index/marginal mark only)

The three substantive recoveries are intentionally anchor-level rather than guessed transcriptions:
- `p0092`: multiple mounted handwritten slips containing substantial text; baseline OCR is completely empty.
- `p0176`: one mounted handwritten bibliographic slip; visible anchors include **H. Joly**, **Sainte Thérèse**, **Les Saints**, **Paris**, **Lecoffre**.
- `p0180`: multiple handwritten slips plus a larger handwritten card; one clearly visible anchor reads **“De la méthode dans les sciences. Histoire ...”** with the remainder requiring close reading.

Details for all 26 baseline-empty pages are in `empty_ocr_visual_review.jsonl`.

## Short/minimal pages

`p0027`, `p0083`, and `p0175` are short-text pages where the visual content is genuinely brief rather than evidence of a full-page OCR collapse. `p0093` and `p0155` contain only minimal/non-substantive marks; `p0155` is notable because Paddle turned a small handwritten squiggle into an Arabic token, so the baseline text should not be treated as documentary content.

## Status

**Chunk 006 retrieval-grade visual audit: COMPLETE (180/180).**

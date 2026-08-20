# Chunk 007 visual review summary

Updated: 2026-08-20

## Scope and review level

- Source span: `chunk_007:p0001`–`chunk_007:p0147` (147 scan pages).
- Split scan set is complete and contiguous:
  - `chunk_007__p0001-0040.pdf`
  - `chunk_007__p0041-0080.pdf`
  - `chunk_007__p0081-0120.pdf`
  - `chunk_007__p0121-0147.pdf`
- Page-count check: `40 + 40 + 40 + 27 = 147`; no scan-page gap remains.
- All 147 pages were visually checked against the clean PaddleOCR v3 baseline. Obvious mismatch/empty-OCR cases were rechecked at higher resolution.
- Review level: **retrieval-grade visual correction layer**, not diplomatic or word-perfect transcription. Raw PaddleOCR remains unchanged.

## Page-level result

| class | pages |
|---|---:|
| usable | 15 |
| usable with noise | 87 |
| high-noise, close transcription required before exact quotation | 37 |
| false-empty OCR visually recovered | 2 |
| genuinely blank / no substantive text | 6 |
| **total** | **147** |

The full page-level audit is in `full_visual_audit_manifest_v1.tsv`.

## Layout and OCR behaviour

Chunk 007 has two main documentary regimes. `p0001`–roughly `p0112` are predominantly full handwritten note leaves, often photographed as paired pages. From `p0113` onward the scans shift heavily toward dark mounting boards carrying multiple narrow handwritten slips, cards, envelopes, and occasional printed clippings. The mounted-slip sequence produces the same retrieval problems seen elsewhere in the corpus: reading-order collapse, severe under-capture, mixed-language/script hallucination, and isolated over-expansion.

The exact-quotation high-noise queue is:

`p0045`, `p0080`, `p0090`, `p0093`, `p0104`, `p0105`, `p0107`, `p0109`, `p0113`, `p0114`, `p0116`, `p0117`, `p0118`, `p0119`, `p0121`, `p0122`, `p0123`, `p0124`, `p0125`, `p0126`, `p0128`, `p0129`, `p0130`, `p0131`, `p0132`, `p0134`, `p0135`, `p0136`, `p0137`, `p0138`, `p0141`, `p0142`, `p0143`, `p0144`, `p0145`, `p0146`, `p0147`

Especially clear pathology includes:
- `p0045`: two densely written facing pages are represented by only **452 baseline characters**.
- `p0080`: a substantial two-page handwritten scan is represented by only **161 characters**, with mixed-script/repetition output.
- `p0090`: nonempty OCR contains pathological numeric/repetition cleanup markers; visual content is substantially richer than the baseline suggests.
- `p0093`: OCR contains repeated implausible numeric strings and mixed-script hallucination despite a relatively small handwritten source.
- `p0104`, `p0105`, `p0107`, `p0109`: short/small manuscript pages are rendered as unstable multilingual or mixed-script OCR; `p0105` is also grossly under-captured.
- `p0115`: two full mounting boards with many handwritten slips are a **complete OCR false negative**.
- `p0121`–`p0138`: mounted-slip pages are particularly unstable. `p0122` has only 174 characters for two full boards; `p0128` has only 14 characters; `p0132` has 335 characters for a full board. Several pages hallucinate repeated `CV.` labels, non-Latin scripts, or unrelated English/German/French strings.
- `p0141`–`p0147`: multi-slip boards remain under-captured and/or hallucinated; `p0142` has only 17 baseline characters for a two-board scan.

## Empty-OCR audit

Baseline OCR marks eight pages empty:

`p0103`, `p0111`, `p0112`, `p0115`, `p0120`, `p0127`, `p0133`, `p0140`.

Final visual result:
- **6 genuinely blank / no substantive text**: `p0103`, `p0111`, `p0112`, `p0127`, `p0133`, `p0140`
- **2 substantive/documentary false-empty pages**: `p0115`, `p0120`

The two recoveries are conservative:
- `p0115`: two mounted boards carry many handwritten slips. Baseline OCR is completely empty; close transcription is still required.
- `p0120`: printed letterhead reads **“The Laura Spelman Rockefeller Memorial / 61 Broadway / New York.”** The scan shows the letterhead without substantive body text. This occurrence is added to the cross-chunk stationery index.

Details for all eight baseline-empty pages are in `empty_ocr_visual_review.jsonl`.

## Status

**Chunk 007 retrieval-grade visual audit: COMPLETE (147/147).**

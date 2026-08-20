# Chunk 004 visual review summary

Updated: 2026-08-20

## Scope and coverage

- Baseline source span: `chunk_004:p0001`–`chunk_004:p0236` (236 scan pages).
- The split scan set is now complete and contiguous:
  - `chunk_004__p0001-0040.pdf`
  - `chunk_004__p0041-0080.pdf`
  - `chunk_004__p0081-0120.pdf`
  - `chunk_004__p0121-0160.pdf`
  - `chunk_004__p0161-0200.pdf`
  - `chunk_004__p0201-0236.pdf`
- Page-count check: `40 + 40 + 40 + 40 + 40 + 36 = 236`; no scan-page gap remains.
- **Full-page visual audit: 236/236 complete.** The previously missing `p0081–p0160` block has now received the same retrieval-grade visual pass as the rest of the chunk.
- Review level remains a **retrieval-grade visual correction layer**, not a diplomatic or word-perfect transcription. Raw PaddleOCR is preserved unchanged.

## Full chunk result

| class | pages |
|---|---:|
| usable | 86 |
| usable with noise | 105 |
| high-noise, close transcription required before exact quotation | 39 |
| false-empty OCR visually recovered | 1 |
| genuinely blank | 5 |
| **total** | **236** |

Page-level manifests are retained by scan span:
- `visual_audit_manifest_p0001-0080_v1.tsv`
- `visual_audit_manifest_p0081-0160_v1.tsv`
- `visual_audit_manifest_p0161-0236_v1.tsv`

The former gap record `missing_scan_block_v1.tsv` is retained as provenance and now marked `resolved`.

## Newly reviewed middle block: p0081–p0160

The 80-page middle block yielded **29 usable, 29 usable-with-noise, 20 high-noise, and 2 genuinely blank pages**. The high-noise designation is deliberately conservative: it marks pages where the scan contains substantive handwriting but the baseline OCR shows severe under-capture, script hallucination, repetition/pathology, or layout failure sufficient to make verbatim quotation unsafe.

New high-noise pages in this span:

`p0082, p0084, p0091, p0092, p0093, p0094, p0110, p0117, p0120, p0122, p0123, p0138, p0139, p0144, p0145, p0151, p0155, p0156, p0159, p0160`

Notable failure modes include: `p0082`, `p0084`, `p0110`, and `p0117`, where substantial visible notes are represented by only a few dozen or roughly a hundred OCR characters; `p0145`, where the OCR invents a long sequential year run; and `p0159`, where a large OCR repetition run had to be machine-cleaned in the baseline. These pages remain useful as scan references but require direct visual reading for exact wording.

## Empty-OCR audit

Baseline OCR marks six chunk-004 pages empty: `p0045`, `p0101`, `p0114`, `p0176`, `p0210`, `p0236`.

Final visual result:
- **Confirmed genuinely blank**: `p0045`, `p0101`, `p0114`, `p0176`, `p0236`.
- **False-empty OCR page recovered**: `p0210`.

The newly available scans settle the two previously unresolved cases. `p0101` shows no substantive text, only paper/staining/very faint show-through; `p0114` is likewise visually blank. Both are therefore confirmed blanks rather than OCR failures.

`p0210` remains the sole complete false-empty OCR page in chunk 004. It is a dense handwritten page. High-confidence visible anchors include **paus**, **Italië**, **Langob.**, **Ravenna en Pentapolis**, **keizer Leo III (717–741)**, **paus Greg. II**, **Liutprand**, **Rome**, **715–731**, and **731–741**. This remains an anchor-level recovery, not a diplomatic transcription.

Details are in `empty_ocr_visual_review.jsonl`.

## Exact-quotation queue

Already-nonempty pages conservatively flagged high-noise across the full chunk:

`p0016, p0050, p0080, p0082, p0084, p0091, p0092, p0093, p0094, p0110, p0117, p0120, p0122, p0123, p0138, p0139, p0144, p0145, p0151, p0155, p0156, p0159, p0160, p0164, p0177, p0179, p0186, p0190, p0191, p0192, p0193, p0197, p0202, p0207, p0211, p0213, p0222, p0227, p0228`

Add `p0210` to the close-reading queue whenever verbatim quotation is required because its baseline OCR is completely empty.

## Status

**Chunk 004 retrieval-grade visual audit: COMPLETE (236/236).**

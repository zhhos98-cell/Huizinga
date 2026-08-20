# Chunk 004 visual review summary

Updated: 2026-08-20

## Scope and current coverage

- Baseline source span: `chunk_004:p0001`–`chunk_004:p0236` (236 scan pages).
- Scan images currently available for visual review:
  - `p0001–p0040`
  - `p0041–p0080`
  - `p0161–p0236` (from `chunk_004_161-236.pdf`)
- **Missing visual block: `p0081–p0160` (80 pages).**
- Therefore **156/236 pages have been visually audited** and **80/236 remain visual-pending solely because the scan block is not available in this workspace**.
- Raw PaddleOCR for all 236 pages is preserved and remains searchable; the 80 missing-scan pages are explicitly recorded as visual-pending rather than silently treated as reviewed.

## Reviewed-page result (156 pages)

| class | pages |
|---|---:|
| usable | 57 |
| usable with noise | 76 |
| high-noise, close transcription required before exact quotation | 19 |
| false-empty OCR visually recovered | 1 |
| genuinely blank | 3 |
| **visually reviewed subtotal** | **156** |
| visual pending: missing scan block | **80** |
| **baseline total** | **236** |

Page-level reviewed manifests are split to match the available scan blocks: `visual_audit_manifest_p0001-0080_v1.tsv` and `visual_audit_manifest_p0161-0236_v1.tsv`. The absent middle block is recorded in `missing_scan_block_v1.tsv`.

## Empty-OCR audit

Baseline OCR marks six chunk-004 pages empty: `p0045`, `p0101`, `p0114`, `p0176`, `p0210`, `p0236`.

Current visual result:
- **Confirmed blank**: `p0045`, `p0176`, `p0236`.
- **False-empty OCR page recovered**: `p0210`.
- **Cannot yet inspect because the scan is missing**: `p0101`, `p0114`.

`p0210` is a dense handwritten page. High-confidence visible anchors include **paus**, **Italië**, **Langob.**, **Ravenna en Pentapolis**, **keizer Leo III (717–741)**, **paus Greg. II**, **Liutprand**, **Rome**, **715–731**, and **731–741**. This is recorded as an anchor-level recovery, not a diplomatic transcription.

Details are in `empty_ocr_visual_review.jsonl`.

## Exact-quotation queue in the reviewed span

Already-nonempty reviewed pages conservatively flagged high-noise:

`p0016, p0050, p0080, p0164, p0177, p0179, p0186, p0190, p0191, p0192, p0193, p0197, p0202, p0207, p0211, p0213, p0222, p0227, p0228`

`p0210` should also be close-read before verbatim quotation.

## Missing-scan priority

When the missing `p0081–p0160` block is re-uploaded, the first pages to inspect should be `p0101` and `p0114`, because the baseline OCR is entirely empty there. The rest of the 80-page block still needs the same full-page visual pass.

## Status

**Chunk 004 retrieval-grade visual audit: PARTIAL — 156/236 complete; 80 pages (`p0081–p0160`) awaiting scan images.**

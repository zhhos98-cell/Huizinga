# Chunk 010 visual review summary

Updated: 2026-08-21

## Scope and review level

- Source span: `chunk_010:p0001`–`chunk_010:p0153` (153 scan pages).
- Split scan set verified complete and contiguous:
  - `chunk_010__p0001-0040.pdf`
  - `chunk_010__p0041-0080.pdf`
  - `chunk_010__p0081-0120.pdf`
  - `chunk_010__p0121-0153.pdf`
- Page-count check: `40 + 40 + 40 + 33 = 153`; no scan-page gap remains.
- All 153 pages were visually checked against the clean PaddleOCR v3 baseline. The full set was reviewed at page-layout level; anomaly and empty-OCR cases were rechecked at higher resolution.
- Review level: **retrieval-grade visual correction layer**, not diplomatic or word-perfect transcription. Raw PaddleOCR remains unchanged.

## Page-level result

| class | pages |
|---|---:|
| usable with noise | 143 |
| high-noise, close transcription required before exact quotation | 6 |
| false-empty OCR visually recovered | 1 |
| verified short-text page | 1 |
| genuinely blank / no substantive text | 2 |
| **total** | **153** |

No page in this handwritten run is promoted to a word-clean `usable` class: even the regular notebook pages retain enough character-level noise that exact quotation should return to the scan.

## Layout and OCR behaviour

Chunk 010 is unusually regular for this archive. Most of `p0001`–`p0149` consists of a blank verso or backing leaf paired with one dense handwritten note page. This makes text-presence detection reliable and reading order comparatively stable. The baseline usually captures enough names, dates, places, and bibliographical anchors for retrieval, while character accuracy remains uneven.

The main failures are not page omission but local hallucination inside otherwise substantial OCR: modern-English filler, mixed scripts, and language switching appear on some manuscript pages even when the visible page is ordinary Dutch/French/German historical notes.

High-noise queue:

`p0006`, `p0007`, `p0060`, `p0102`, `p0128`, `p0153`

- `p0006`, `p0007`, `p0060`, `p0102`, `p0128`: conspicuous mixed-script or generative-looking OCR that diverges from the visible manuscript. These remain useful only as loose retrieval surfaces.
- `p0153`: baseline OCR reads **“2020 THETROO DAOMO ROBLOX UK”**, while the visible mounted slip reads **“de naamverwisseling.”** The second strip on the board is blank.

Several short or special-layout pages are not OCR failures:
- `p0059` is a short mounted label/card; the brief baseline is proportionate to the visible text.
- `p0100`, `p0124`, and `p0149` contain less text than the surrounding notebook sequence, matching their visibly shorter sheets/notes.

## Empty-OCR audit

Baseline empty OCR pages: `p0150`, `p0151`, `p0152`.

Visual result:
- `p0150`: blank/no substantive text.
- `p0151`: blank/no substantive text.
- `p0152`: **false-empty OCR**. The scan contains an envelope marked **“Fred. Hendrik”** and two handwritten slips. Conservative visible anchors include **1633–1637** and **1905**; exact slip transcription still requires close reading.

The conservative recovery is stored separately in `empty_ocr_visual_review.jsonl`.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 010 retrieval-grade visual audit: COMPLETE (153/153).**

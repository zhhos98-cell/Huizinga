# Chunk 011 visual review summary

Updated: 2026-08-21

## Scope and review level

- Source span: `chunk_011:p0001`–`chunk_011:p0200` (200 scan pages).
- Split scan set verified complete and contiguous:
  - `chunk_011__p0001-0040.pdf`
  - `chunk_011__p0041-0080.pdf`
  - `chunk_011__p0081-0120.pdf`
  - `chunk_011__p0121-0160.pdf`
  - `chunk_011__p0161-0200.pdf`
- Page-count check: `40 + 40 + 40 + 40 + 40 = 200`; no scan-page gap remains.
- **Full-page visual audit: 200/200 complete.** All pages were checked against the clean PaddleOCR v3 baseline, with empty-OCR, unusual-layout, and mixed-script cases rechecked at higher resolution.
- Review level: **retrieval-grade visual correction layer**, not diplomatic or word-perfect transcription. Raw PaddleOCR remains unchanged.

## Page-level result

| class | pages |
|---|---:|
| usable with noise | 192 |
| high-noise, close transcription required before exact quotation | 3 |
| verified short-text pages | 3 |
| genuinely blank / no substantive text | 2 |
| false-empty OCR recoveries | 0 |
| **total** | **200** |

## Layout and OCR behaviour

Chunk 011 is unusually regular for this archive. Most of `p0002–p0149` consists of single notebook leaves or paired leaves photographed against the dark background, with dense handwriting concentrated on the right-hand leaf. The baseline usually captures enough names, dates, and topical anchors for retrieval, while spelling, segmentation, and reading order remain too unstable for exact quotation.

The layout changes around `p0151`: a run of loose cards and narrow leaves replaces the regular notebook format. OCR remains usable for retrieval on most of these pages, but line order becomes less reliable. `p0162` is a short title card, after which a further notebook/loose-leaf sequence continues through `p0199`.

Two visually distinctive printed insertions occur at `p0074–p0075`. `p0074` reproduces the illustrated title page of James I's *Workes*; the OCR catches the title anchors but with errors. `p0075` combines a printed bookseller/catalogue page headed **“ENGLAND TO THE DEATH OF ELIZABETH”** with a handwritten note leaf; the baseline is text-rich but should still be treated as retrieval-grade rather than quotation-safe.

## Empty-OCR audit

Baseline empty OCR pages: `p0150`, `p0200`.

Visual result:
- `p0150`: genuinely blank / no substantive text.
- `p0200`: genuinely blank / no substantive text.

No substantive false-empty OCR page was found in chunk 011.

## High-noise queue

`p0061`, `p0147`, `p0166`

- `p0061`: two mounted handwritten slips are clearly visible, but the baseline is only 374 characters and contains obvious hallucinated/nonsensical material. Severe under-capture; close transcription required.
- `p0147`: dense handwritten notebook page. The baseline contains multiple non-Latin hallucinations inconsistent with the visible Dutch/English manuscript. Retrieval anchors survive, but exact quotation is unsafe.
- `p0166`: dense handwritten notebook/loose-leaf page. The baseline again introduces repeated mixed-script hallucinations; exact transcription requires visual rereading.

## Verified short-text pages

- `p0001`: short cover/title card. The baseline reads `Engeland.1803-1649. 1923/24 1936/37 Eng.Staatsstorm.1928/29`; retain baseline wording unless closely transcribed from the scan.
- `p0157`: printed **BRIEFKAART** form.
- `p0162`: title card **“Eng. beschaving XVIII. 1925/26”**.

## Status

**Chunk 011 retrieval-grade visual audit: COMPLETE (200/200).**

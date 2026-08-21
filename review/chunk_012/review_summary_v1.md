# Chunk 012 visual review summary

Updated: 2026-08-21

## Scope and review level

- Source span: `chunk_012:p0001`–`chunk_012:p0161` (161 scan pages).
- Split scan set verified complete and contiguous:
  - `chunk_012__p0001-0040.pdf`
  - `chunk_012__p0041-0080.pdf`
  - `chunk_012__p0081-0120.pdf`
  - `chunk_012__p0121-0160.pdf`
  - `chunk_012__p0161-0161.pdf`
- Page-count check: `40 + 40 + 40 + 40 + 1 = 161`; no scan-page gap remains.
- All 161 pages were visually checked against the clean PaddleOCR v3 baseline.
- Review level: **retrieval-grade visual correction layer**, not diplomatic or word-perfect transcription. Raw PaddleOCR is preserved unchanged.

## Page-level result

| class | pages |
|---|---:|
| usable | 8 |
| usable with noise | 115 |
| high-noise, close transcription required before exact quotation | 12 |
| false-empty OCR visually recovered | 8 |
| verified short-text | 3 |
| genuinely blank / no substantive text | 15 |
| **total** | **161** |

## Layout and sequence

Chunk 012 changes documentary form several times. `p0001` is a course-title card (**Eng. Staatsvorm / 1928/29**). `p0002–p0092` are predominantly dense handwritten course notes on loose/notebook leaves. `p0094–p0095` are narrow printed/newspaper clippings. From `p0097` the material shifts into mounted index-slip boards, with intermittent blank leaves, and this is where OCR reading order and coverage deteriorate sharply. `p0138` is a letter headed **“OUD ARCHIEF IN ZEELAND”**; the baseline captures **“MIDDELBURG, 20 Juni 1923”** among its anchors. `p0142–p0150` contain the printed address **“REDE BIJ DE ONTHULLING VAN EEN GEDENKTEEKEN VOOR SIR PHILIP SIDNEY TE ZUTPHEN OP 2 JULI 1913 UITGESPROKEN DOOR J. HUIZINGA”** and its following pages. `p0153–p0161` are photographic/transparency/table images; `p0159` gives a readable heading for the name-frequency table sequence: **“Veelvuldigste namen uit het zijlschotregister van Winsummer- & Schaphalster Zijlvest 1553.”**

## Empty-OCR audit

Baseline empty OCR pages: **23**.

- **15 genuinely blank / no substantive text:** `p0093`, `p0096`, `p0099`, `p0103`, `p0107`, `p0110`, `p0114`, `p0117`, `p0121`, `p0124`, `p0128`, `p0136`, `p0137`, `p0151`, `p0152`.
- **8 substantive false-empty recoveries:** `p0122`, `p0123`, `p0125`, `p0131`, `p0153`, `p0154`, `p0156`, `p0158`.

Notable false-empty cases:
- `p0122`: mounted board with six handwritten strips plus an envelope. Conservative visible anchors include **“Poland”** and **“Poland, The Eve of Peace, 1920.”**
- `p0123`, `p0125`, `p0131`: mounted boards with multiple handwritten/index strips; baseline is completely empty despite substantive text.
- `p0153`, `p0154`, `p0156`, `p0158`: photographic/transparency frames containing dense tabular lists; each is a complete OCR false negative.

## High-noise queue

`p0098`, `p0101`, `p0105`, `p0106`, `p0109`, `p0112`, `p0119`, `p0127`, `p0140`, `p0155`, `p0157`, `p0161`.

The main failure mode is severe under-capture on mounted boards and photographic tables rather than ordinary handwriting noise. `p0101` combines low coverage with pathological repetition cleanup. `p0127` collapses into repeated English filler unrelated to the visible mounted strips. `p0140` is a mounted board with several tabular/index strips but the baseline contains only **“a”**. The table photographs `p0155`, `p0157`, and `p0161` are similarly extreme: the visible frames contain dense tabular text while the baseline contains only **“1.00”**, **“A:11”**, and **“AB”**, respectively.

## Short-text pages

- `p0001`: course-title card, visually **“Eng. Staatsvorm / 1928/29”**; baseline captures only the year.
- `p0141`: small handwritten note; text presence verified, exact wording remains close-reading work.
- `p0142`: printed Sir Philip Sidney address title page, baseline and image agree on the main title.

## Status

**Chunk 012 retrieval-grade visual audit: COMPLETE (161/161).**

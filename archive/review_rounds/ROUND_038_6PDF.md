# Huizinga visual calibration — six-PDF round 038

Date: 2026-08-27

Operational unit: six supplied scan PDFs, closing chunk_062 and advancing chunk_063 through `p0160`. From this round onward the normal batch size is **six PDFs** unless a supplied terminal tail requires a smaller closure batch. Raw PaddleOCR JSON is preserved unchanged.

## Inputs completed

1. `chunk_062__p0161-0200.pdf` — 40 pages
2. `chunk_062__p0201-0235.pdf` — 35 pages
3. `chunk_063__p0001-0040.pdf` — 40 pages
4. `chunk_063__p0041-0080.pdf` — 40 pages
5. `chunk_063__p0081-0120.pdf` — 40 pages
6. `chunk_063__p0121-0160.pdf` — 40 pages

Total scan pages visually reviewed: **235**.

## Round 038 visual class counts

- high-noise-layout-risk: **159**
- blank-no-substantive-visual: **45**
- short-text-or-nontext: **0**
- usable-with-noise-visual: **31**

## Round result

- **6 PDFs / 235 pages** completed.
- chunk_062 closes at **235/235** page-level visual coverage. Whole-chunk aggregate: **175 high-noise / 47 blank / 9 short / 4 usable**.
- chunk_063 advances through `p0160` at **160/233** page-level visual coverage. Current aggregate: **106 high-noise / 25 blank / 0 short / 29 usable**.
- chunk_062 terminal morphology remains predominantly mounted-slip/composite, with stronger exceptions at `p0209` and `p0235`.
- chunk_063 contains two conspicuous retrieval-oriented breaks: the printed booklet packet `p0042-p0050`, and the larger manuscript/ledger packet `p0121-p0128`; additional strong exceptions occur at `p0065-p0068`, `p0097`, `p0133-p0134`, and `p0156-p0157`.
- The supplied chunk_063 remainder `p0161-p0233` is left for the next six-PDF operational unit.

Raw OCR is preserved; OCR strings were not exhaustively proofread page by page.

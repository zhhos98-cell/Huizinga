# Huizinga visual calibration - six-PDF round 040

Date: 2026-08-27

Operational unit: six supplied scan PDFs, closing chunk_064 and advancing chunk_065 through `p0200`. The six-PDF batch convention is retained. Raw PaddleOCR JSON is preserved unchanged.

## Inputs completed

1. `chunk_064__p0161-0200.pdf` - 40 pages
2. `chunk_064__p0201-0229.pdf` - 29 pages
3. `chunk_065__p0041-0080.pdf` - 40 pages
4. `chunk_065__p0081-0120.pdf` - 40 pages
5. `chunk_065__p0121-0160.pdf` - 40 pages
6. `chunk_065__p0161-0200.pdf` - 40 pages

Total scan pages visually reviewed: **229**.

## Round 040 visual class counts

- high-noise-layout-risk: **168**
- blank-no-substantive-visual: **38**
- short-text-or-nontext: **21**
- usable-with-noise-visual: **2**

## Round result

- **6 PDFs / 229 pages** completed.
- chunk_064 closes at **229/229** page-level visual coverage. Final aggregate: **178 high-noise / 41 blank / 5 short / 5 usable**.
- chunk_065 advances across `p0041-p0200` at **160/228** page-level visual coverage. Current aggregate for the reviewed span: **111 high-noise / 28 blank / 19 short / 2 usable**.
- The chunk_064 tail remains mounted-slip/composite material and introduces no new retrieval packet on the scale of the earlier `p0035`, `p0104-p0106`, or `p0147` exceptions.
- chunk_065 contains a visibly larger proportion of envelope, owner/address-card, and postal controls. Stronger retrieval-oriented exceptions are `p0056` and `p0079`; photo/contact-strip material appears at `p0062-p0064`.
- `chunk_065__p0001-0040.pdf` is not supplied in the current queue. This leading gap remains explicit and is not counted as reviewed.
- The next six-PDF unit can begin with `chunk_065__p0201-0228.pdf`, then continue through chunk_066 `p0001-p0200`.

Raw OCR is preserved; OCR strings were not exhaustively proofread page by page.

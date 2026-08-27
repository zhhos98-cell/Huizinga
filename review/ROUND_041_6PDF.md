# Huizinga visual calibration - six-PDF round 041

Date: 2026-08-27

Operational unit: six supplied scan PDFs, backfilling and closing chunk_065, then advancing chunk_066 through `p0160`. The six-PDF batch convention is retained. Raw PaddleOCR JSON is preserved unchanged.

## Inputs completed

1. `chunk_065__p0001-0040.pdf` - 40 pages
2. `chunk_065__p0201-0228.pdf` - 28 pages
3. `chunk_066__p0001-0040.pdf` - 40 pages
4. `chunk_066__p0041-0080.pdf` - 40 pages
5. `chunk_066__p0081-0120.pdf` - 40 pages
6. `chunk_066__p0121-0160.pdf` - 40 pages

Total scan pages visually reviewed: **228**.

## Round 041 visual class counts

- high-noise-layout-risk: **178**
- blank-no-substantive-visual: **35**
- short-text-or-nontext: **9**
- usable-with-noise-visual: **6**

## Round result

- **6 PDFs / 228 pages** completed.
- chunk_065 is now closed at **228/228** page-level visual coverage. Final aggregate: **165 high-noise / 39 blank / 22 short / 2 usable**.
- The newly supplied `p0001-p0040` span repairs the explicit leading gap from Round 040; `p0201-p0228` closes the terminal tail. Neither span adds a retrieval packet stronger than the already identified `p0056` and `p0079` exceptions.
- chunk_066 advances through `p0160` at **160/226** page-level visual coverage. Current aggregate: **124 high-noise / 24 blank / 6 short / 6 usable**.
- chunk_066 remains dominated by mounted-slip/composite boards. The clearest early retrieval-oriented break is `p0061-p0062`, where larger printed regions become visually dominant, followed by a much stronger internally linear packet at `p0129-p0132`: manuscript and full-page printed leaves largely escape the narrow-slip morphology.
- The supplied chunk_066 remainder `p0161-p0226` is left for the next six-PDF operational unit, which can then continue into chunk_067 through `p0160`.

Raw OCR is preserved; OCR strings were not exhaustively proofread page by page.

# Huizinga visual calibration — five-PDF round 012

Date: 2026-08-26

Operational unit: five supplied scan PDFs. The concurrently active Round 011 (`chunk_039:p0201-p0236` plus `chunk_040:p0001-p0160`) is intentionally excluded. This round reviews the remaining tail of chunk_040 and opens chunk_041 through `p0080`. Raw PaddleOCR JSON is preserved unchanged.

## Inputs completed

1. `chunk_040__p0161-0200.pdf` — 40 pages
2. `chunk_040__p0201-0240.pdf` — 40 pages
3. `chunk_040__p0241-0243.pdf` — 3 pages
4. `chunk_041__p0001-0040.pdf` — 40 pages
5. `chunk_041__p0041-0080.pdf` — 40 pages

Total scan pages visually reviewed: **163**.

## Round 012 visual class counts

- high-noise-layout-risk: **103**
- blank-no-substantive-visual: **43**
- short-text-or-nontext: **5**
- usable-with-noise-visual: **12**

Segment breakdown:

- `chunk_040:p0161-p0243`: 51 high-noise, 22 blank/no-substantive, 3 short/nontext, 7 usable-with-noise
- `chunk_041:p0001-p0080`: 52 high-noise, 21 blank/no-substantive, 2 short/nontext, 5 usable-with-noise

## Morphology and controls

Both spans are dominated by dark mounting boards carrying multiple small manuscript or catalogue slips. The main retrieval-stronger exceptions are `chunk_040:p0200-p0201`, `p0207-p0209`, `p0211-p0212`, and `chunk_041:p0031-p0032`, `p0056`, `p0061-p0062`, where one or more large internally linear sheets provide clearer reading order. Sparse controls are `chunk_040:p0197`, `p0213-p0214` and `chunk_041:p0022-p0023`.

## OCR boundary

Unlike the older status note, indexed raw OCR JSON is present for chunk_040 and chunk_041. It was used as an auxiliary signal, but the classifications above are scan-first. Raw OCR strings were not rewritten or exhaustively proofread.

## Round result

- **5 PDFs / 163 pages** completed.
- chunk_040 tail `p0161-p0243`: visually closed for the supplied tail; whole-chunk closure depends on the separately running Round 011 writeback.
- chunk_041: **80/236** visual coverage.

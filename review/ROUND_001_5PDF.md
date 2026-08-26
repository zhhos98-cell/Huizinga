# Huizinga visual calibration — five-PDF round 001

Date: 2026-08-26

Operational unit: five supplied scan PDFs. Raw PaddleOCR JSON files are preserved unchanged; calibration is written only to `review/`.

## Inputs completed

1. `chunk_033__p0041-0080.pdf` — 40 pages
2. `chunk_033__p0081-0120.pdf` — 40 pages
3. `chunk_033__p0121-0160.pdf` — 40 pages
4. `chunk_033__p0201-0236.pdf` — 36 pages
5. `chunk_034__p0001-0040.pdf` — 40 pages

Total scan pages visually swept: **196**.

## Output

- `review/chunk_033/`: partial scan-calibrated review layer covering 156 pages (`p0041-p0160`, `p0201-p0236`). Missing `p0001-p0040` and `p0161-p0200` remain explicit blockers to chunk closure.
- `review/chunk_034/`: partial scan-calibrated review layer for `p0001-p0040`.
- Exact calibration controls record confirmed blank/minimal pages and two direct OCR pathology checks: `chunk_033:p0041` and `chunk_034:p0002`.

## Calibration policy

This round is a macro visual calibration pass with exact control pages, not a complete page-by-page diplomatic transcription or full OCR usability manifest. Composite mounted boards, handwriting, skew and small source regions remain scan-first for exact quotation. No unsupplied page range is inferred or reconstructed.

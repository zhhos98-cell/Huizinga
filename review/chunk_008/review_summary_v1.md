# Chunk 008 visual review summary

Updated: 2026-08-21

## Scope and review level

- Source span: `chunk_008:p0001`–`chunk_008:p0111` (111 scan pages).
- Split scan set verified complete and contiguous: `1–40`, `41–80`, `81–111`.
- Page-count check: `40 + 40 + 31 = 111`; no scan-page gap remains.
- All 111 pages were visually checked against the clean PaddleOCR v3 baseline. Empty-OCR and severe mismatch cases were rechecked at higher resolution.
- Review level: **retrieval-grade visual correction layer**, not diplomatic or word-perfect transcription. Raw PaddleOCR remains unchanged.

## Page-level result

| class | pages |
|---|---:|
| usable | 27 |
| usable with noise | 45 |
| high-noise, close transcription required before exact quotation | 21 |
| false-empty OCR visually recovered | 7 |
| genuinely blank / no substantive text | 11 |
| **total** | **111** |

## Empty-OCR audit

Baseline empty OCR pages: 18.

- False-empty recoveries: `p0001`, `p0028`, `p0035`, `p0052`, `p0056`, `p0057`, `p0070`.
- Blank/no substantive text: `p0006`, `p0010`, `p0014`, `p0017`, `p0023`, `p0029`, `p0033`, `p0036`, `p0044`, `p0089`, `p0096`.

Notable recoveries:

- `p0001`: printed **“The Laura Spelman Rockefeller Memorial / 61 Broadway / New York.”**
- `p0028`: faint handwritten material; visible date range **1795–1856**.
- `p0035`: multiple handwritten mounted slips, many rotated.
- `p0052`: dense mounted index slips; readable anchors include **“d.13. keuze of interpretatie”**, **“d.12. zuiverheid spiritualiteit”**, and **“17. vormleer”**.
- `p0056`, `p0057`, `p0070`: further mounted-slip OCR false negatives; exact wording requires close transcription.

## OCR pathology and quotation queue

Main high-noise queue:

`p0005`, `p0019`, `p0025`, `p0047`, `p0053`, `p0054`, `p0055`, `p0059`, `p0061`, `p0064`, `p0065`, `p0066`, `p0068`, `p0071`, `p0072`, `p0074`, `p0075`, `p0076`, `p0077`, `p0078`, `p0084`.

The dominant failure mode is mounted-slip under-capture and reading-order collapse. `p0019` and `p0025` are conspicuous over-expansion/hallucination cases; `p0059` required v3 repetition cleanup. From `p0085` onward the material shifts strongly toward printed book/newspaper pages and OCR becomes substantially more regular for retrieval.

## Status

**Chunk 008 retrieval-grade visual audit: COMPLETE (111/111).**

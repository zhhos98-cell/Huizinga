# Huizinga Leiden visual review progress

Updated: 2026-08-20

## Chunk 001

- Source span: `chunk_001:p0001`–`chunk_001:p0179` (179 scan pages).
- Review PDFs received in five blocks: 1–40, 41–80, 81–120, 121–160, 161–179.
- `empty_ocr` audit: **35/35 pages visually checked**.
- Confirmed genuinely blank: **25**.
- False-empty OCR pages with substantive text: **10** — p0018, p0020, p0068, p0098, p0100, p0108, p0109, p0149, p0150, p0162.
- Transcriptions/cautious partial transcriptions for those false-empty pages are in `review/chunk_001/empty_ocr_visual_review.jsonl`.
- Important recovered false negative: `chunk_001:p0109` reads **“The Laura Spelman Rockefeller Memorial / 61 Broadway / New York.”**
- Close visual correction of the already-nonempty OCR pages remains in progress; raw OCR files are preserved unchanged.

### Review policy

Preserve raw OCR as source data. Visual review is written as a separate correction/transcription layer. Do not infer illegible text. Use `[unclear]` for uncertain readings and `[...]` where the physical scan cuts off text.

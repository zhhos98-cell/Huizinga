# Huizinga Leiden archive proofreading layer

This directory records image-first proofreading of the 71 Leiden archive PDF chunks against the frozen consolidated PaddleOCR text layer.

## Governing principle

The PDF image is authoritative. Existing OCR is a draft/search aid only.

The original consolidated OCR (`huizinga_leiden_paddleocr_clean_001-071_complete_v3.json`) remains immutable. Proofreading creates a separate correction/description layer; it does not silently overwrite the raw OCR.

## Page states

Each physical PDF page advances through explicit states:

- `unseen` — not yet reviewed against the image.
- `image_checked` — image inspected; page type, archival marks, orientation, and obvious blank/backing status recorded.
- `text_checked` — OCR/text content checked against the image; substantive OCR errors and uncertain readings recorded.
- `final_checked` — page has reached the archival-use standard for this project. Blank/backing/cover pages can reach this state without a transcription when their material function has been recorded.

A chunk is `complete` only when every page has a terminal `final_checked` status.

## Transcription rules

- Preserve historical spelling, punctuation, abbreviations, language switching, capitalization, and visible deletions where practicable.
- Do not modernize, translate, or silently normalize wording.
- Do not infer missing words from context.
- Use `[unclear]` for a visible but unresolved reading and `[illegible]` where the image does not support a defensible reading.
- Distinguish printed matter, Huizinga manuscript, later archival labels, envelopes/covers, and mounted slips where visually separable.
- Record archive/inventory identifiers exactly as seen; uncertain characters remain marked uncertain.
- Multi-slip mounting sheets are treated as one physical PDF page but retain internal block order/layout notes.
- OCR-empty pages are never assumed blank until image-checked.

## Progress/checkpoints

Work proceeds chunk by chunk in physical PDF order. During a chunk, checkpoints are normally written every 20–30 pages so progress survives conversation/session loss.

The project-wide tracker is `PROGRESS.md`. Each chunk receives its own page ledger and checkpoint notes under `proofreading/chunk_NNN/`.

## File-integrity rule

Do not trust chat/UI preview page counts as the archival page count. Record PDF metadata (`pdfinfo` or equivalent) and cross-check it against the consolidated JSON page sequence before proofreading. Large files may have preview/render caps even when the underlying PDF is complete.

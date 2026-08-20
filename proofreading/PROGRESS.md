# Proofreading progress

Last updated: 20 August 2026

## Corpus control

- frozen OCR corpus: `huizinga_leiden_paddleocr_clean_001-071_complete_v3.json`
- total frozen corpus pages: 15,139
- chunks: 001–071 complete
- proofreading mode: image-first, chunk-by-chunk
- active branch: `corpus-scan-2026-08-20`

## Current chunk

### chunk_002

- status: **in progress**
- PDF metadata: **183 pages**, approximately **182 MB**
- consolidated JSON pages for chunk 002: **183**
- crosswalk: PDF page count == JSON chunk page count; initial pages visually align (`PDF p2` corresponds to `chunk_002:p0002`)
- UI/file-preview warning: the conversation preview exposed only the first 150 rendered pages, despite the underlying PDF containing 183 pages. Use PDF metadata/local rendering for completeness control.
- structural/image pass: **25 / 183** pages reviewed
- pages at `final_checked`: **6 / 183**
- pages at `text_checked`: **11 / 183**
- pages at `image_checked` awaiting text pass: **8 / 183**
- unseen pages: **158 / 183**
- next text-pass page: **17**
- next unseen physical page: **26**
- latest structural checkpoint: `proofreading/chunk_002/CHECKPOINT_001_p001-025.md`
- text passes:
  - `proofreading/chunk_002/TEXT_PASS_001_p002-010.md`
  - `proofreading/chunk_002/TEXT_PASS_002_p012-014.md`

## Chunk register

- chunk_001 — not yet proofread in this archival pass
- chunk_002 — **IN PROGRESS**
- chunks_003–071 — not yet proofread in this archival pass

## Checkpoint rule

During an active chunk, update this file every ~20–30 physical pages, and immediately when a high-value archival discovery or crosswalk problem appears.

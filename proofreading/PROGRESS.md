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
- baseline crosswalk: PDF page count == JSON chunk page count, but page-level OCR merge exceptions are now being logged separately
- UI/file-preview warning: the conversation preview exposed only the first 150 rendered pages, despite the underlying PDF containing 183 pages. Use PDF metadata/local rendering for completeness control.
- structural/image pass: **50 / 183** pages reviewed
- pages at `final_checked`: **8 / 183**
- pages at `text_checked`: **26 / 183**
- pages at `image_checked` awaiting text pass: **16 / 183**
- unseen pages: **133 / 183**
- next text-pass page: **33**
- next unseen physical page: **51**
- latest structural checkpoint: `proofreading/chunk_002/CHECKPOINT_002_p026-050.md`
- crosswalk control: `proofreading/chunk_002/CROSSWALK_NOTES.md`
- text passes:
  - `proofreading/chunk_002/TEXT_PASS_001_p002-010.md`
  - `proofreading/chunk_002/TEXT_PASS_002_p012-014.md`
  - `proofreading/chunk_002/TEXT_PASS_003_p017-023.md`
  - `proofreading/chunk_002/TEXT_PASS_004_p025.md`
  - `proofreading/chunk_002/TEXT_PASS_005_p026-032.md`

## Current archival findings

- Salimbene packet p12–23 is now structurally controlled: bibliography/life → sources and chronological page map → autograph/manuscript transmission → source genealogy/glossary → synthetic historiographical notes.
- Florence dossier begins at p24/p25 and runs through p48. Its opening formulation is analytically important: Huizinga calls Florence's development to the rise of the Medici `een bloedige gesch.` and sets `partijstrijd en hebzucht` beside the city's `prachtige bloei`.
- Florence p26–32 is now text-controlled as one analytical module: urban autonomy and Guelf/Ghibelline conflict → guild/popolo constitution → finance/florin/banking and Dante's wealth vocabulary → Bianchi/Neri exile crisis → comparison with Italian signorie/condottieri → Ciompi/Albizzi/Medici → monumental building and architectural form.
- **Crosswalk exception confirmed:** frozen OCR `chunk_002:p0030` merges physical PDF p30 and p31; OCR p31 is nearly empty. Physical PDF p31 is the substantial Florence architecture page. See `CROSSWALK_NOTES.md`.
- p49 starts a separate archival unit: `Trois esprits prégothiques <Paris 1930>`; do not merge it into the Florence sequence.

## Chunk register

- chunk_001 — not yet proofread in this archival pass
- chunk_002 — **IN PROGRESS**
- chunks_003–071 — not yet proofread in this archival pass

## Checkpoint rule

During an active chunk, update this file every ~20–30 physical pages, and immediately when a high-value archival discovery or crosswalk problem appears.

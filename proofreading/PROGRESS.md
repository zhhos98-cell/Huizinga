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

- status: **structural pass complete; text proofreading in progress**
- PDF metadata: **183 pages**, approximately **182 MB**
- consolidated JSON pages for chunk 002: **183**
- baseline crosswalk: PDF page count == JSON chunk page count, with page-level OCR merge exceptions logged separately
- UI/file-preview warning: conversation/file preview exposes only the first 150 rendered pages despite the underlying PDF containing 183 pages. Use physical PDF metadata/local rendering for completeness control.
- structural/image pass: **183 / 183 pages reviewed — COMPLETE**
- pages at `final_checked`: **13 / 183**
- pages at `text_checked`: **49 / 183**
- pages at `image_checked` awaiting text/diplomatic pass: **121 / 183**
- unseen pages: **0 / 183**
- next structural page: **none — physical pass complete**
- next text-control priorities: `p33`, `p36`, `p37` diplomatic Latin inserts; then Paris 1930 lecture and p176–183 mounted-card packet
- latest structural checkpoints:
  - `proofreading/chunk_002/CHECKPOINT_006_p126-150.md`
  - `proofreading/chunk_002/CHECKPOINT_007_p151-183.md`
- crosswalk control: `proofreading/chunk_002/CROSSWALK_NOTES.md`
- text passes:
  - `proofreading/chunk_002/TEXT_PASS_001_p002-010.md`
  - `proofreading/chunk_002/TEXT_PASS_002_p012-014.md`
  - `proofreading/chunk_002/TEXT_PASS_003_p017-023.md`
  - `proofreading/chunk_002/TEXT_PASS_004_p025.md`
  - `proofreading/chunk_002/TEXT_PASS_005_p026-032.md`
  - `proofreading/chunk_002/TEXT_PASS_006_p033-047.md`
  - `proofreading/chunk_002/TEXT_PASS_007_p126-136.md`

## Current archival findings

- Salimbene packet p12–23 is structurally controlled: bibliography/life → sources and chronological page map → autograph/manuscript transmission → source genealogy/glossary → synthetic historiographical notes.
- Florence dossier p24/25–48 is analytically controlled. It begins from `een bloedige gesch.` / `partijstrijd en hebzucht` and integrates constitutional conflict, guild/popolo institutions, finance, architecture, Dante, Giotto, Pisano/Petrarch/classical reception, Medici household/Platonic culture, Quattrocento visual culture and Savonarola.
- Florence p34–35 and p38–47 have been text-checked. Three mixed-source pages (`p33`, `p36`, `p37`) remain at `image_checked` because their Latin documentary transcriptions require a dedicated diplomatic pass.
- **Crosswalk exception confirmed:** frozen OCR `chunk_002:p0030` merges physical PDF p30 and p31; OCR p31 is nearly empty. Physical p31 is the substantial Florence architecture page. See `CROSSWALK_NOTES.md`.
- p49 opens `Trois esprits prégothiques <Paris 1930>`. p50–51 are an opening/proem draft; p52 a bibliographical insert; p53 blank; p54 onward a fuller French lecture draft.
- Paris 1930 p54–69 frames the twelfth century as `formation/fermentation`, explicitly engages Haskins's `Renaissance of the Twelfth Century`, and gives strong causal weight to Church/monastic reform, chivalry, crusade, towns, schools and corporate forms rather than classical revival alone.
- First `esprit`, **Abélard**, is bounded at p70–95. Huizinga builds an ecology of book scarcity, oral teaching, schools, mobile masters, competitive dialectic and `jeu/disputa`; Abélard is treated as `prégothique` / `primitif`, not simply as a Renaissance precursor.
- p96 is blank. p97 begins `deuxième` and introduces **Jean de Salisbury**. The Jean section ends at p136; p126–136 is now text-controlled through `Policraticus`, social/group observation, prince/law/public utility/tyranny, and `nugae curialium` as a rival courtly form of life.
- p137 is blank. p138–143 form a source-control/bibliographical interlude, including Leiden library request slips for Alain de Lille material.
- p144 explicitly begins the third `esprit`, **Alain de Lille**. Huizinga assigns him the aesthetic/imaginative side of the twelfth century: poverty of visible images, richness of colour, verbal `pictura`, symbolic classification, Realism/Platonism and the transition from `prégothique` openness toward Gothic system/order.
- Alain section ends at p173. p174–175 are blank separators.
- p176 begins a new archival unit: mounted working cards on **Abélard / Bernard / Berengar of Poitiers**, with Latin quotations and edition/page controls. It is not part of the Paris 1930 continuous lecture.
- `chunk_002:p0098` remains a severe OCR failure despite a readable physical manuscript page, reinforcing image-first control.

## Chunk register

- chunk_001 — not yet proofread in this archival pass; split PDFs are now available for a controlled pass after chunk_002 text work
- chunk_002 — **STRUCTURAL PASS COMPLETE / TEXT PASS IN PROGRESS**
- chunks_003–071 — not yet proofread in this archival pass

## Checkpoint rule

During an active chunk, update this file every ~20–30 physical pages, and immediately when a high-value archival discovery, boundary, or crosswalk problem appears. A chunk is not marked complete until all substantive pages have reached the required text/diplomatic state; a completed structural pass alone is not completion.

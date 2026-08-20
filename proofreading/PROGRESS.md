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
- baseline crosswalk: PDF page count == JSON chunk page count, with page-level OCR merge exceptions logged separately
- UI/file-preview warning: conversation/file preview exposes only the first 150 rendered pages despite the underlying PDF containing 183 pages. Use physical PDF metadata/local rendering for completeness control.
- structural/image pass: **125 / 183** pages reviewed
- pages at `final_checked`: **10 / 183**
- pages at `text_checked`: **38 / 183**
- pages at `image_checked` awaiting text pass: **77 / 183**
- unseen pages: **58 / 183**
- next unseen physical page: **126**
- latest structural checkpoint: `proofreading/chunk_002/CHECKPOINT_005_p101-125.md`
- crosswalk control: `proofreading/chunk_002/CROSSWALK_NOTES.md`
- text passes:
  - `proofreading/chunk_002/TEXT_PASS_001_p002-010.md`
  - `proofreading/chunk_002/TEXT_PASS_002_p012-014.md`
  - `proofreading/chunk_002/TEXT_PASS_003_p017-023.md`
  - `proofreading/chunk_002/TEXT_PASS_004_p025.md`
  - `proofreading/chunk_002/TEXT_PASS_005_p026-032.md`
  - `proofreading/chunk_002/TEXT_PASS_006_p033-047.md`

## Current archival findings

- Salimbene packet p12–23 is structurally controlled: bibliography/life → sources and chronological page map → autograph/manuscript transmission → source genealogy/glossary → synthetic historiographical notes.
- Florence dossier p24/25–48 is analytically controlled. It begins from `een bloedige gesch.` / `partijstrijd en hebzucht` and integrates constitutional conflict, guild/popolo institutions, finance, architecture, Dante, Giotto, Pisano/Petrarch/classical reception, Medici household/Platonic culture, Quattrocento visual culture and Savonarola.
- Florence p34–35 and p38–47 have been text-checked. Three mixed-source pages (`p33`, `p36`, `p37`) remain at `image_checked` because their Latin documentary transcriptions require a dedicated diplomatic pass.
- **Crosswalk exception confirmed:** frozen OCR `chunk_002:p0030` merges physical PDF p30 and p31; OCR p31 is nearly empty. Physical p31 is the substantial Florence architecture page. See `CROSSWALK_NOTES.md`.
- p49 opens `Trois esprits prégothiques <Paris 1930>`. p50–51 are an opening/proem draft; p52 a bibliographical insert; p53 blank; p54 onward a fuller French lecture draft.
- Paris 1930 p54–69 frames the twelfth century as `formation/fermentation`, explicitly engages Haskins's `Renaissance of the Twelfth Century`, and gives strong causal weight to Church/monastic reform, chivalry, crusade, towns, schools and corporate forms rather than classical revival alone.
- First `esprit`, **Abélard**, is bounded at p70–95. p76–95 build an ecology of book scarcity, oral teaching, schools, mobile masters, competitive dialectic and `jeu/disputa`; Huizinga treats Abélard as `prégothique` / `primitif`, not a Renaissance precursor, and sets him against Saint Bernard as an opposite pole of the same century.
- p96 is blank. p97 begins `deuxième` and introduces **Jean de Salisbury** as the second `esprit`.
- Jean section continues through at least p125. Huizinga constructs a `clerc non-clérical` / `clerc-gentilhomme` type through overlap of clerical, courtly and chivalric forms; fortitude/good humour; probabilistic intellectual judgement; classical `humanités`; ancient/modern inheritance (`dwarfs on giants`); Peter the Venerable's Islamic translation/knowledge project; and John's concise, humorous style.
- p125 opens an internal subsection on Jean's political/social thought. The **third `esprit` has not yet appeared**.
- `chunk_002:p0098` is a severe OCR failure despite a readable physical manuscript page, reinforcing image-first control.

## Chunk register

- chunk_001 — not yet proofread in this archival pass
- chunk_002 — **IN PROGRESS**
- chunks_003–071 — not yet proofread in this archival pass

## Checkpoint rule

During an active chunk, update this file every ~20–30 physical pages, and immediately when a high-value archival discovery or crosswalk problem appears.

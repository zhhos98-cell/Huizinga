# Proofreading progress

Last updated: 20 August 2026

## Corpus control

- frozen OCR corpus: `huizinga_leiden_paddleocr_clean_001-071_complete_v3.json`
- total frozen corpus pages: 15,139
- chunks: 001–071 complete
- proofreading mode: image-first, chunk-by-chunk
- active branch: `corpus-scan-2026-08-20`
- frozen OCR is an immutable search/draft layer; proofreading corrections and page/capture controls live separately.

## Completed chunk

### chunk_002 — **COMPLETE**

- physical PDF captures: **183**
- consolidated JSON pages for chunk 002: **183**
- structural/image pass: **183 / 183 — COMPLETE**
- `final_checked`: **13 / 183**
- `text_checked`: **170 / 183**
- `image_checked` remaining: **0 / 183**
- unseen remaining: **0 / 183**
- resolved captures: **183 / 183**
- completion record: `proofreading/chunk_002/COMPLETE_2026-08-20.md`
- complete page ledger: `proofreading/chunk_002/PAGE_LEDGER_COMPLETE.csv`
- crosswalk/capture exceptions: `proofreading/chunk_002/CROSSWALK_NOTES.md`

### Completion standard

`chunk_002` is complete under the current archival proofreading standard: every substantive physical capture has reached `text_checked`, and blank/backing/title/cover captures have reached `final_checked`. This does **not** mean that every clipped abbreviation, faint proper name, or copied Latin line has been normalised into a publication-ready critical edition. Uncertain micro-readings remain unresolved/marked and should be returned to the image or cited edition before exact publication quotation.

The conversation/file preview exposes only the first 150 rendered pages of the PDF, but local physical-file control confirmed 183 captures; all 183 are represented in the page ledger.

## chunk_002 control files

### Structural checkpoints

- `proofreading/chunk_002/CHECKPOINT_001_p001-025.md`
- `proofreading/chunk_002/CHECKPOINT_002_p026-050.md`
- `proofreading/chunk_002/CHECKPOINT_003_p051-075.md`
- `proofreading/chunk_002/CHECKPOINT_004_p076-100.md`
- `proofreading/chunk_002/CHECKPOINT_005_p101-125.md`
- `proofreading/chunk_002/CHECKPOINT_006_p126-150.md`
- `proofreading/chunk_002/CHECKPOINT_007_p151-183.md`

### Text/control passes

- `proofreading/chunk_002/TEXT_PASS_001_p002-010.md`
- `proofreading/chunk_002/TEXT_PASS_002_p012-014.md`
- `proofreading/chunk_002/TEXT_PASS_003_p017-023.md`
- `proofreading/chunk_002/TEXT_PASS_004_p025.md`
- `proofreading/chunk_002/TEXT_PASS_005_p026-032.md`
- `proofreading/chunk_002/TEXT_PASS_006_p033-047.md`
- `proofreading/chunk_002/TEXT_PASS_007_p126-136.md`
- `proofreading/chunk_002/TEXT_PASS_008_p033_p036-037_LATIN.md`
- `proofreading/chunk_002/TEXT_PASS_009_p050-069_PARIS_FRAMING.md`
- `proofreading/chunk_002/TEXT_PASS_010_p070-095_ABELARD.md`
- `proofreading/chunk_002/TEXT_PASS_011_p097-125_JEAN_DE_SALISBURY.md`
- `proofreading/chunk_002/TEXT_PASS_012_p138-143_ALAIN_APPARATUS.md`
- `proofreading/chunk_002/TEXT_PASS_013_p144-173_ALAIN_DE_LILLE.md`
- `proofreading/chunk_002/TEXT_PASS_014_p176-183_ABELARD_BERNARD_CARDS.md`

## chunk_002 archival sequence

1. p1–10 — Zelandensia / Zeeland mounted slips.
2. p11–23 — Salimbene packet: bibliography/life → sources/page map → autograph/transmission → glossary/allusion apparatus → synthetic notes.
3. p24–48 — Florence XIII–XV: political/factional conflict, guild/popolo constitution, finance, architecture, Dante/Giotto/Pisano/Petrarch, Medici/Platonism, Quattrocento visual culture and Savonarola.
4. p49–175 — `Trois esprits prégothiques <Paris 1930>`:
   - p50–69 — civilisational framing / Haskins / `formation`–`fermentation`;
   - p70–95 — Abélard;
   - p97–136 — Jean de Salisbury;
   - p138–143 — Alain source/library apparatus;
   - p144–173 — Alain de Lille;
   - p174–175 — blank close.
5. p176–183 — separate Abélard / Bernard / Berengar of Poitiers mounted-card packet.

## High-value findings from chunk_002

- Florence p25 frames development to the Medici as `een bloedige gesch.` and sets `partijstrijd en hebzucht` beside cultural `prachtige bloei`.
- Paris 1930 defines the twelfth century through `formation` / `fermentation` and explicitly engages C. H. Haskins's *The Renaissance of the Twelfth Century*.
- Huizinga's causal field gives major weight to Church/monastic reform, chivalry, crusade, towns, schools and corporate forms; the key formulation is `naissance, non pas renaissance`.
- In the Abélard section `primitive` is relational/pre-systematic rather than merely backward: intellectual power and competitive `jeu/disputa` precede mature disciplinary restraints.
- Jean de Salisbury is built as a `clerc-gentilhomme` / humane-critical type; Peter the Venerable's Islam/Qur'an translation project appears as organised knowledge acquisition.
- Alain de Lille carries the lecture from verbal image/colour and `pictura` to `esprit gothique` as pressure toward category, system, order, harmony and style.
- Salimbene, Alain request forms and the final mounted-card packet preserve Huizinga's research workflow materially: source acquisition, bibliography, manuscript transmission, concordance, quotation harvesting and synthesis.

## Permanent chunk_002 technical exceptions

- frozen OCR `chunk_002:p0030` merges physical p30 and p31; OCR p31 is nearly empty; physical p31 contains the substantial Florence architecture page.
- physical PDF pp.32–33 are overlapping photographic captures that repeat the same left-hand Latin leaf while the right-hand page changes.
- physical PDF pp.36–37 likewise repeat the same left-hand Latin leaf (`Van Mieris, Groot Charterboek I 176`) while the right-hand page changes.
- `chunk_002:p0098` is a severe OCR failure despite a readable physical French manuscript page.

These establish that PDF capture, OCR page and manuscript leaf are distinct identifiers. See `CROSSWALK_NOTES.md`.

## Chunk register

- chunk_001 — being handled in a separate conversation/workstream; no work on it is claimed here.
- chunk_002 — **COMPLETE (archival proofreading pass, 20 Aug 2026)**
- chunks_003–071 — not yet proofread in this archival pass in this conversation.

## Checkpoint rule

For future chunks, update this file every ~20–30 physical captures and immediately when a high-value discovery, archival boundary or crosswalk problem appears. A chunk is complete only when no substantive capture remains at `image_checked` or `unseen` under the current archival standard.

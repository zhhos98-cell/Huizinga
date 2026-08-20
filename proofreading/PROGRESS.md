# Proofreading progress

Last updated: 20 August 2026

## Corpus control

- frozen OCR corpus: `huizinga_leiden_paddleocr_clean_001-071_complete_v3.json`
- total frozen corpus pages: **15,139**
- chunks: **001–071 complete in frozen OCR layer**
- proofreading mode: **image-first, chunk-by-chunk**
- active branch: `corpus-scan-2026-08-20`
- frozen OCR is immutable; proofreading, document-class and capture/leaf corrections live separately.

## Completed in this workstream

### chunk_002 — **COMPLETE**

- physical captures: **183 / 183 resolved**
- `final_checked`: **13**
- `text_checked`: **170**
- `image_checked`: **0**
- `unseen`: **0**
- completion record: `proofreading/chunk_002/COMPLETE_2026-08-20.md`
- ledger: `proofreading/chunk_002/PAGE_LEDGER_COMPLETE.csv`
- crosswalk: `proofreading/chunk_002/CROSSWALK_NOTES.md`

Future work on chunk_002 should be targeted publication-level authority/diplomatic checking, not restart of basic proofreading.

### chunk_005 — **TEXT/IMAGE RESOLUTION COMPLETE; FINAL HOUSEKEEPING PENDING**

- physical captures: **173 / 173 resolved**
- structural/image pass: **173 / 173 — COMPLETE**
- `final_checked`: **14 / 173**
- `text_checked`: **159 / 173**
- `image_checked`: **0 / 173**
- `unseen`: **0 / 173**
- structural checkpoints: `CHECKPOINT_001`–`CHECKPOINT_005`
- text-control passes: `TEXT_PASS_001`–`TEXT_PASS_019`
- crosswalk/material notes: `proofreading/chunk_005/CROSSWALK_NOTES.md`
- remaining repo housekeeping only: create `PAGE_LEDGER_COMPLETE.csv` and `COMPLETE_2026-08-20.md`.

Important chunk_005 corrections:

- p59 and p63 are two physically distinct blank Laura Spelman Rockefeller Memorial letterheads; neither is Rockefeller correspondence.
- p149 is false-empty OCR: the physical capture is a dense manuscript page.
- p151 is genuinely blank; p158 is unused printed `BRIEFKAART`; p173 is the blank physical close.
- no PDF/OCR page merge or repeated-leaf capture anomaly was confirmed.

## Active / prepared in this workstream

### chunk_008 — **OCR PREPASS READY / IMAGE PASS NOT STARTED**

- frozen OCR pages: **111** (`p0001`–`p0111`)
- non-empty OCR pages: **93**
- empty OCR pages: **18**
- physical PDF/review slices currently unavailable in the conversation/File Library/repo at the time of prepass.
- therefore: `image_checked = 0`, `text_checked = 0`, `final_checked = 0`; no physical blank is accepted from OCR alone.
- OCR prepass: `proofreading/chunk_008/OCR_PREPASS_2026-08-20.md`
- preferred image-review split: p1–40 / p41–80 / p81–111.

Provisional OCR-derived structure to verify from images:

1. p001–020 — handwritten / mounted research and teaching notes.
2. p021–022 — German printed `FORSCHUNGEN UND FORTSCHRITTE` material; p023 OCR-empty.
3. p024–032 — mixed notes/apparatus; p028–029 OCR-empty.
4. p033–043 — cultural-historical/historiographical notes; p033, p035–036 OCR-empty.
5. p044–077 — bibliography/historiography/social-studies cards and printed notices; several OCR-empty candidates.
6. p078–084 — possible Huizinga programme/lecture + manuscript material.
7. p085–088 — Dutch `Staatsblad` archival legislation (`N.378`).
8. p090–092 — second `Staatsblad` archival packet (`N.552`, 2 Sept. 1919 in OCR).
9. p093–095 — Leiden/Troeltsch/Historisch Genootschap newspaper-clipping cluster.
10. p097–104 — dense German printed scholarly/scientific articles.
11. p105–111 — Dutch printed reviews/news/scientific discussion.

## Parallel workstreams

- chunk_001 — being proofread in another conversation/workstream; no current page count is claimed here.
- chunk_003 — being proofread in another conversation/workstream; no current page count is claimed here.
- chunk_004 — being proofread in another conversation/workstream; no current page count is claimed here.
- chunk_005 — page-level proofreading resolved here; final ledger/completion-file housekeeping remains.
- chunk_008 — active here at OCR-prepass stage, awaiting physical image slices.
- other chunks — no proofreading completion is claimed in this workstream.

## Completion rule

A chunk is complete only when no substantive physical capture remains at `image_checked` or `unseen` under the current archival standard. Blank/backing/title/material-only captures may be `final_checked`; substantive handwritten/typed/printed research material must reach `text_checked` before chunk closure. OCR keyword hits and OCR-empty pages must be reclassified from the physical image.

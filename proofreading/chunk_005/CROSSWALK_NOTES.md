# chunk_005 PDF/OCR/material crosswalk notes

Date opened: 20 August 2026

## Control principle

Physical PDF capture is authoritative for document class and material relation. Frozen OCR remains an immutable search/draft layer. A machine keyword hit can derive from preprinted stationery, reused paper, a reverse side, or a mounted fragment and must not automatically be interpreted as correspondence content.

## Material correction 001 — p59 Rockefeller hit is blank stationery

Physical `chunk_005` p59 is a single clean sheet carrying only the printed heading:

`The Laura Spelman Rockefeller Memorial / 61 Broadway / New York`

No substantive handwritten or typed text appears on the sheet.

### Consequence

- retain the OCR keyword `Rockefeller` in the frozen layer;
- classify the physical capture as `blank_letterhead / material_artifact`;
- do **not** count it as Rockefeller correspondence, dossier prose, or evidence for the 1931 Leiden anthropology proposal.

## Material correction 002 — p63 is a second distinct blank Rockefeller sheet

Physical p63 carries the same preprinted Laura Spelman Rockefeller Memorial heading and is otherwise blank.

Direct visual comparison with p59 shows different stain/mark patterns. p63 is therefore a **different physical sheet**, not a duplicate photographic capture of p59.

### Consequence

The archive contains at least two separate surviving blank sheets of this Rockefeller Memorial stationery in this local sequence. This is material evidence for the presence/reuse/preservation of Rockefeller stationery in Huizinga's papers, but not evidence for the content of a Rockefeller exchange.

## OCR correction 003 — p149 is false-empty

Frozen OCR `chunk_005:p0149` is empty. The physical PDF capture is **not blank**: it contains a dense handwritten manuscript page on the right side, with substantial continuous text.

### Consequence

- classify p149 as `substantive_manuscript` / `image_checked`;
- add `ocr_false_empty = true` in any future corrected ledger;
- never infer physical blankness from `empty_ocr` alone.

This is the strongest false-empty example so far in chunk_005 and is structurally comparable to the severe OCR failure already recorded for chunk_002:p0098.

## Material correction 004 — p151 is genuinely blank

Physical p151 is a blank folded/leaf capture. Unlike p149, the OCR-empty condition here corresponds to the physical object. `final_checked`.

## Material correction 005 — p158 is an unused printed postcard

Physical p158 is an unused `BRIEFKAART` card (`Klein Toornvliet`, Helpman bij Groningen). It contains printed stationery text but no substantive manuscript entry. It is a material/backing artifact and is `final_checked`.

Adjacent pp.155–157 use similar postcard stock beside substantive narrow handwritten teaching strips. The postcard and the manuscript strip must therefore be represented as separate material components even when photographed in one capture.

## Material correction 006 — p173 is the blank physical close

Physical p173 is genuinely blank and marks the end of chunk_005. `final_checked`.

## Downstream marker rule

For global discovery/index work, p59 and p63 should carry fields equivalent to:

- `entity_exact = Rockefeller`
- `document_class = blank_letterhead`
- `material_evidence = true`
- `correspondence_content = false`
- `anthropology_dossier_evidence = false`
- `image_checked = true`

For p149:

- `document_class = substantive_manuscript`
- `ocr_false_empty = true`
- `image_checked = true`

This prevents future full-corpus retrieval from silently converting stationery hits into substantive documentary hits or empty OCR into blank physical pages.

## Page/capture anomalies

No OCR/PDF **page-number merge** or repeated-leaf photographic overlap has been confirmed in physical pp.1–173. The major chunk_005 crosswalk problems are instead **document-class and OCR-presence errors**: blank stationery retrieved as substantive keyword evidence, and a substantive manuscript capture retrieved as empty OCR.

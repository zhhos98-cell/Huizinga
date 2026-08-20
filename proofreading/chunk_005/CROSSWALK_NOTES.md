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

## Downstream marker rule

For global discovery/index work, p59 and p63 should carry fields equivalent to:

- `entity_exact = Rockefeller`
- `document_class = blank_letterhead`
- `material_evidence = true`
- `correspondence_content = false`
- `anthropology_dossier_evidence = false`
- `image_checked = true`

This prevents future full-corpus keyword retrieval from silently converting a stationery hit into a substantive documentary hit.

## Page/capture anomalies

No OCR/PDF page-number merge or repeated-leaf capture anomaly has yet been confirmed in physical pp.1–80. Continue checking pp.81–173.

# Chunk 014 visual review summary

## Scope

- Source span: `chunk_014:p0001`–`chunk_014:p0251` (251 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–240, 241–251.
- Page-count check: `40 + 40 + 40 + 40 + 40 + 40 + 11 = 251`.
- Review level: retrieval-grade visual correction layer against the clean PaddleOCR v3 baseline. Raw OCR remains unchanged.

## Result

- **Full-page visual audit: 251/251 complete.**
- Page classes:
  - 6 usable
  - 140 usable-with-noise
  - 48 high-noise
  - 8 false-empty OCR recoveries
  - 7 short-text pages
  - 42 genuinely blank/no-substantive-text pages
- Baseline empty OCR pages: 50.
- Visual result: 42 genuinely blank and 8 false-empty recoveries.

### False-empty recoveries

`p0020`, `p0024`, `p0087`, `p0137`, `p0160`, `p0169`, `p0246`, `p0249`.

The substantive false-empty failures are mounted-slip boards (`p0020`, `p0087`, `p0137`, `p0246`) and recurring **Laura Spelman Rockefeller Memorial, 61 Broadway, New York** letterhead (`p0024`, `p0160`, `p0169`, `p0249`). These would disappear entirely from text-only retrieval.

### High-noise queue

`p0004`, `p0011`, `p0012`, `p0022`, `p0023`, `p0026`, `p0029`, `p0034`, `p0060`, `p0062`, `p0069`, `p0070`, `p0078`, `p0079`, `p0098`, `p0100`, `p0101`, `p0106`, `p0107`, `p0109`, `p0110`, `p0112`, `p0115`, `p0125`, `p0127`, `p0135`, `p0140`, `p0141`, `p0149`, `p0156`, `p0172`, `p0174`, `p0175`, `p0189`, `p0201`, `p0209`, `p0212`, `p0226`, `p0227`, `p0231`, `p0232`, `p0234`, `p0235`, `p0241`, `p0243`, `p0244`, `p0248`, `p0251`.

The dominant failure modes are (1) mounted-slip reading-order collapse and severe under-capture, (2) dense handwritten/postcard pages reduced to a few tokens, and (3) pathological OCR expansion/repetition. `p0098` and especially `p0125` over-expand relative to the visible material; `p0100`, `p0115`, `p0209`, `p0212`, and `p0241` carry repeat-cleanup/residual repetition signals. `p0244` is near-total under-capture; `p0251` repeats a short phrase instead of representing the full mounted board.

## Core-theme hits

### 1. Publisher descriptions of visual/print production (`p0007–p0009`)

The Paul Hazard sequence is unusually explicit about the material construction of a historical book. `p0008` specifies `papier pur alfa`, new type, ornamental elements and **`planches hors texte en héliogravure`**; `p0009` again specifies plates made **`d'après des documents de l'époque`** and preserves a Firmin-Didot printer line. The printed prospectus/catalogue sits directly beside Huizinga's mounted slips.

This is first-order evidence that the archive's “visual” materials arrive already embedded in publisher decisions about paper, typography, reproduction technique, selection and publicity.

### 2. Review-copy circulation as documentary infrastructure (`p0229–p0237`)

The Gardner/Godfrey cluster exposes a concrete circulation mechanism rather than an abstract readership:

- Basil Blackwell submits Gardner's *English Gothic Foliage Sculpture* for review and requests the review when published (`p0229`).
- Cambridge University Press separately sends the same title for review on 24 June 1927 (`p0230`).
- B. T. Batsford sends Godfrey's *The Story of Architecture in England* for review (`p0236`).
- A 19 September 1928 Batsford letter explicitly links the Godfrey book to popular interest in architecture and possible school use (`p0237`).

For the project, this gives a material route from publisher/bookseller to editor/reviewer and onward to periodical and educational publics.

### 3. Publisher-supplied provenance (`p0248`)

The printed phrase **`ÜBERREICHT VOM VERLEGER`** on a mounted-slip board is a direct provenance cue: an item in the working archive was marked as supplied by the publisher. The surrounding handwritten material needs close transcription.

### 4. Symbol / architecture / worldview queue (`p0035–p0057`)

Several long handwritten pages connect architectural form, `symbolisme`, `verbeelding` and `wereldbeschouwing`. Because the OCR is unstable, this cluster is flagged for later close transcription rather than used for exact quotation now.

### 5. Negative control

No secure Malinowski/anthropology/ethnology dossier was found in chunk 014. `primitief` occurs in medieval/Christian cultural-development notes and should not be remapped into anthropology.

## Short-text pages

- `p0010`, `p0013`, `p0017`, `p0021`, `p0027`, `p0245`: short Laura Spelman Rockefeller Memorial letterhead pages.
- `p0071`: postcard/form page with the short printed anchor **BRIEFKAART**.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 014 retrieval-grade visual audit: COMPLETE (251/251).**

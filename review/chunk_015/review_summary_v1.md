# Chunk 015 visual review summary

## Scope

- Source span: `chunk_015:p0001`–`chunk_015:p0090` (90 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–90.
- Page-count check: `40 + 40 + 10 = 90`.
- Review level: retrieval-grade visual correction layer against the clean PaddleOCR v3 baseline. Raw OCR remains unchanged.

## Result

- **Full-page visual audit: 90/90 complete.**
- Page classes:
  - 15 usable
  - 43 usable-with-noise
  - 18 high-noise
  - 5 false-empty OCR recoveries
  - 5 short-text pages
  - 4 genuinely blank/no-substantive-text pages
- Baseline empty OCR pages: 9.
- Visual result: 4 genuinely blank and 5 false-empty recoveries.

### False-empty recoveries

`p0004`, `p0005`, `p0021`, `p0043`, `p0061`.

- `p0004`: mounted board with several substantive handwritten slips.
- `p0005`, `p0021`: **Laura Spelman Rockefeller Memorial, 61 Broadway, New York** letterhead.
- `p0043`: mounted board with substantive handwritten slips.
- `p0061`: faint tabular/handwritten sheet beneath a blank strip.

### Genuine blank/no-substantive pages

`p0038`, `p0051`, `p0084`, `p0090`.

### High-noise queue

`p0003`, `p0011`, `p0016`, `p0017`, `p0023`, `p0035`, `p0036`, `p0041`, `p0042`, `p0044`, `p0046`, `p0048`, `p0054`, `p0059`, `p0065`, `p0069`, `p0083`, `p0086`.

The dominant failure mode remains mounted-slip under-capture and reading-order collapse. Several boards with many visible slips are reduced to only a few OCR tokens (`p0042`, `p0054`, `p0069`). `p0083` is a separate pathological-repetition case: v3 removed a repeated run reported as `x678`; the surviving OCR remains unsuitable for exact quotation. `p0086` is a full handwritten page whose OCR captures only a small fraction.

## Core-theme hits

### 1. `p0070`: material damage becomes an observational test

The clipped *Courrier des Arts* article **“Crépuscule de Viollet-le-Duc”** uses wartime damage to Gothic vaults as a material anomaly against the inherited Viollet-le-Duc structural model, then follows the problem into engineering/statics and Pol Abraham's architectural work. This is external printed material, not Huizinga's prose, but it is a strong archival witness to a methodological ecology in which damaged objects, technical expertise and visual/structural interpretation can revise an established historical theory.

### 2. `p0075–p0082`: a complete scholarly-print circulation ecology

This run materially joins:

`review/article → publisher prospectus → table of contents → bookseller solicitation → subscription pricing → targeted order form → university-press advertisement → archival-source claim → collotype/half-tone reproduction → catalogue → extracted reviews → typographic/binding praise`.

Particularly strong controls:

- `p0077`: Svets & Zeitlinger actively markets **Medium Ævum** and takes subscriptions for the learned-society periodical.
- `p0078`: Editions Béatrice targets professors, librarians and directors of study circles with a discount and future-subscription mechanism.
- `p0079`: OUP advertises Bémont's *Simon de Montfort* as rebuilt from record sources/local and family archives and physically equipped with **8 half-tone plates** plus **a collotype facsimile**.
- `p0081–p0082`: Oxford catalogue entries quantify plates/illustrations/photogravure, while Editions Béatrice recirculates reviews praising typography, binding and printing.

This substantially strengthens the working proposition from chunks 013–014: **Huizinga's working archive is also an archive of the production, marketing, routing and reception of scholarly objects.** The safe formulation remains archival/material: these documents entered or were retained in his working papers; individual reading/use still has to be demonstrated case by case.

### 3. `p0052`: cultural-history boundary work

A handwritten methodological page explicitly raises the boundary between church/religious history, political theory/sociology and **algemene cultuurgeschiedenis**. The OCR is too noisy for diplomatic quotation, but the conceptual structure is clear enough to justify close transcription. This could become important for defining what Huizinga thought cultural history was allowed to absorb institutionally and socially.

### 4. Museum/object and conceptual queues retained from the earlier pass

- `p0041–p0042`: a dense mounted reference cluster with OCR anchors including `CP. Museum 44.2.x1.36.37`, `AKG`, and `F. Stenitz, Gesca.d.Naturwiss.`. Exact object/repository identities remain unresolved.
- `p0045`: church/world, schematisation and dogma/formula language; close transcription required.
- `p0087–p0089`: terminal Leiden/Burgundy/Fruin/siege-inundation historical-note sequence; retained as a historical-memory queue rather than forced into the visual-production argument.

### 5. Rockefeller Memorial stationery

`p0001`, `p0005`, `p0008`, `p0012`, `p0021` repeat **The Laura Spelman Rockefeller Memorial, 61 Broadway, New York**. Two are OCR false-empty. At present this is an institutional-provenance cue only; no specific Rockefeller transaction should be inferred from blank/letterhead pages.

### 6. Negative control

No secure Malinowski/anthropology/ethnology dossier appears in chunk 015. False lexical lookalikes were checked and rejected.

## Short-text pages

- `p0001`, `p0008`, `p0012`: Rockefeller Memorial letterhead captured by OCR.
- `p0088`, `p0089`: short torn manuscript/bibliographical notes whose limited visible text is substantially represented by the baseline.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 015 retrieval-grade visual audit: COMPLETE (90/90).**

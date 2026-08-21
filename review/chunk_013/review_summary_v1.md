# Chunk 013 visual review summary

## Scope

- Source span: `chunk_013:p0001`–`chunk_013:p0215` (215 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–215.
- Page-count check: `40 + 40 + 40 + 40 + 40 + 15 = 215`.
- Review level: retrieval-grade visual correction layer against the clean PaddleOCR v3 baseline. Raw OCR remains unchanged.

## Result

- **Full-page visual audit: 215/215 complete.**
- Page classes:
  - 4 usable
  - 162 usable-with-noise
  - 22 high-noise
  - 9 false-empty OCR recoveries
  - 2 verified short-text pages
  - 1 minimal/non-substantive page
  - 15 genuinely blank/no-substantive-text pages
- Baseline empty OCR pages: 24.
- Visual result: 15 genuinely blank and 9 false-empty recoveries.

### False-empty recoveries

`p0067`, `p0074`, `p0078`, `p0079`, `p0082`, `p0141`, `p0142`, `p0166`, `p0214`.

The strongest false-empty failures are mounted-slip boards (`p0078`, `p0079`, `p0082`, `p0141`, `p0142`) and the full faded manuscript page `p0166`. `p0142` visibly includes the anchor **“Ridderspelen als beleving der Feodaltijd.”** `p0214` is a short note with conservative visible anchors **kunstenaars; Würzburg; Neumann; Goldoni; Molière**.

### High-noise queue

`p0001`, `p0004`, `p0006`, `p0010`, `p0024`, `p0063`, `p0066`, `p0068`, `p0069`, `p0070`, `p0084`, `p0086`, `p0088`, `p0097`, `p0118`, `p0119`, `p0122`, `p0126`, `p0127`, `p0131`, `p0134`, `p0139`.

The dominant failure modes are (1) severe under-capture of large genealogical/tabular sheets at the beginning of the chunk, (2) mounted-board reading-order collapse, (3) mixed-script hallucination on short/list material, and (4) pathological table/repetition expansion (`p0024`; `p0134` was partially cleaned by v3 but remains unreliable).

## Core-theme hits

This chunk contains unusually strong material for the visual/material-culture line and should not be treated merely as an OCR-cleaning block.

### 1. Reformation/Luther: handwritten slips -> publisher prospectus -> portrait -> image bibliography (`p0141–p0148`)

The sequence moves directly from mounted handwritten slips into publisher-produced visual and bibliographical material:

- `p0141–p0142`: mounted Reformation/Luther notes; `p0142` includes **“Ridderspelen als beleving der Feodaltijd.”**
- `p0143`: printed advertisement for **Museum der Weltgeschichte**, explicitly promising **Textabbildungen** and black/colour plates.
- `p0144`: a printed **Martin Luther** portrait, identified as after a **1521 engraving by Lucas Cranach the Elder**, physically paired with a handwritten slip.
- `p0145`: publisher advertisement for Hartmann Grisar, *Martin Luthers Leben und sein Werk*, advertised with **13 Tafeln**.
- `p0146`: *Luther-Studien / Luthers Kampfbilder*, explicitly organized around image conflict: **Abbildungen**, **Bilder im Text**, **Tafeln**, and pamphlet/image warfare.
- `p0147–p0148`: Karl Schottenloher's bibliographical prospectus, including the projected historical map and the material publication plan in fascicles.

For the visual-material argument, the important point is the documentary ecology: Huizinga's working sequence incorporates commercial/publisher ephemera, reproductions, portraiture, bibliographical infrastructure, and handwritten note slips in one archival run. The image is therefore already mediated and produced elsewhere before entering his notes.

### 2. Eighteenth-century lecture notes: institutions, reproduction, publicity, diffusion (`p0167–p0211`)

`p0211` identifies the run as **“XVIII e eeuw (ter uitwerken)”**. Within it:

- `p0167` lists **bibliotheken, kabinetten, galerij, magazijn, museum, kunsthandel** among cultural institutions/formations.
- `p0169` moves through dress/representation, **Swift–Hogarth**, encyclopedism and cultural action.
- `p0174` includes engraving/illustration in the English furniture/park/Chardin cluster.
- `p0200` explicitly describes a **panorama of nature and society**, a historical **wereldbeeld**, and images/representations interweaving.
- `p0207` is the strongest single page: galleries/magazines; **“Prentkunst”** as illustrating, decorating and reproducing; art academies; theatre; opera/concert; **publiciteit**; and instruments/material means.
- `p0209` explicitly shifts attention from **product** to **diffusie**, while noting that visual art had not yet been incorporated into a comparable “cultus” and invoking the **République des lettres**.

These pages give first-order vocabulary for a circulation/institution/visual-production argument rather than requiring that one reconstruct it only from scattered objects.

### 3. Negative control

No direct Malinowski/anthropology/ethnology hit was found in chunk 013. The occurrence of **primitief** at `p0199` belongs to a discussion of chemistry/anthropomorphic conceptions of substances, not to anthropology.

## Short/minimal pages

- `p0111`: **Naam en Adres des Afzenders**
- `p0211`: **XVIII e eeuw (ter uitwerken)**
- `p0163`: backs/blank sides of mounted slips with only a minimal archival numeral (`52`)

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 013 retrieval-grade visual audit: COMPLETE (215/215).**

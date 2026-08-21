# Chunk 017 visual review summary

## Scope

- Source span: `chunk_017:p0001`–`chunk_017:p0228` (228 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–228.
- Page-count check: `40 + 40 + 40 + 40 + 40 + 28 = 228`.
- Review level: retrieval-grade full-page visual correction layer against the clean PaddleOCR v3 baseline. Raw OCR remains unchanged.
- The chunk begins mainly as continuous handwritten / mounted-note medieval-history material and shifts, especially after `p0180`, into a dense Philippe le Bon character-and-portrait dossier containing mounted slips, correspondence, invoices, payment receipts and printed offprints.

## Result

- **Full-page visual audit: 228/228 complete.**
- Page classes:
  - 11 usable
  - 167 usable-with-noise
  - 26 high-noise
  - 9 false-empty OCR recoveries
  - 3 short-text pages
  - 12 genuinely blank/no-substantive-text pages
- Baseline empty OCR pages: 21.
- Visual result: 12 genuinely blank/no-substantive and 9 false-empty recoveries.

### False-empty recoveries

`p0006`, `p0012`, `p0069`, `p0165`, `p0181`, `p0184`, `p0200`, `p0202`, `p0212`.

The most consequential failures are in the late mounted dossier: `p0181`, `p0184`, `p0200`, `p0202` and `p0212` contain substantive mounted notes that would disappear entirely from text-only retrieval. Earlier `p0069` and `p0165` are full manuscript-sheet failures.

### Genuine blank/no-substantive pages

`p0116`, `p0117`, `p0118`, `p0140`, `p0178`, `p0179`, `p0185`, `p0197`, `p0201`, `p0209`, `p0213`, `p0226`.

### High-noise queue

`p0011`, `p0047`, `p0049`, `p0101`, `p0180`, `p0182`, `p0183`, `p0186`, `p0187`, `p0188`, `p0189`, `p0190`, `p0191`, `p0192`, `p0193`, `p0194`, `p0195`, `p0196`, `p0198`, `p0199`, `p0203`, `p0204`, `p0207`, `p0210`, `p0211`, `p0217`.

Dominant failure modes:

1. **mounted-board reading-order collapse and under-capture**, especially in the `het beeld van Phil. den Goed` dossier (`p0180–p0204`);
2. **diagrammatic visual under-capture** (`p0047`);
3. **pathological OCR expansion/repetition** (`p0049`, `p0204`, `p0207`, `p0210`);
4. **multilingual/model drift on small handwriting** (`p0101`);
5. **near-total text loss on dense boards** (`p0187` = 12 OCR chars; `p0211` = 38; `p0217` = 36).

## Core-theme results

### 1. `p0143–p0147`: first-order statement of visual historical method

This is the strongest conceptual result in the chunk. Huizinga begins from the portrait of Philippe le Bon and compares multiple surviving copies, explicitly asks an audience to inspect photographs of them, and then rejects naive physiognomic reading. He calls the portraits `sources iconographiques` and places them beside a written tradition concerning person, character and physique.

Most importantly, `p0146` treats both the **iconographic** and **written** traditions as defective and fortuitous because historical knowledge depends on what happens to have survived. `p0147` then asks whether the pictorial and written domains can be combined into a more convincing historical image.

This supports a strong but bounded proposition: Huizinga explicitly conceptualized visual evidence as a historical tradition with preservation bias, to be triangulated with written evidence rather than read transparently as character.

### 2. `p0203–p0208`: the photographic-reproduction chain becomes directly documentary

The dossier preserves several layers of image acquisition:

- research notes locating/comparing portraits, including a Gotha no. 78 reference (`p0203–p0204`);
- a Huizinga draft asking the director of the museum in Gotha for a good photograph, about **20 × 26 cm**, of a Philip the Good portrait (`p0208`);
- a **27 November 1929** invoice from the Gotha photographic firm **Selma Jandt, vormals M. Jink & Sohn** to Huizinga (`p0205`);
- a **5 December 1929** invoice from **M. Escoute, Lille**, explicitly advertising `PHOTOGRAPHIE INDUSTRIELLE ET DOCUMENTAIRE` and `REPRODUCTIONS D'ART`, with line items for a `cliché 20 × 26`, an `épreuve 20 × 26`, displacement time and two museum-deposit proofs (`p0206`);
- Dutch foreign postal money-order receipts mounted with the dossier (`p0207`).

The safe operational reconstruction is:

`identify portrait/location → contact institution → order photographic reproduction → specialist photographic/art-reproduction supplier → negative/cliché and proof/print → payment and museum routing → research photograph`

The Gotha request and Gotha photographic invoice are securely connected to a Philip the Good image. The Lille invoice is securely a Huizinga art-reproduction transaction, but the surviving page alone does not prove it concerns the identical Gotha portrait.

### 3. `p0218–p0221`: new autograph evidence corrects the historical character image

The printed `Quatre lettres autographes de Philippe le Bon` reports four autograph notes discovered in the Düsseldorf State Archives, `Kleve-Mark`. The accompanying handwritten note says the item is intended to correct an earlier claim in an article on Philip's character that his letters no longer survived.

The article itself says the notes matter less for unknown factual content than for the light their wording throws on the writer's character and personality. The dossier therefore preserves a feedback mechanism:

`archival discovery → corrective communication → autograph evidence → revision of a published historical characterization`

### 4. `p0180–p0204`: the archive physically constructs a `beeld`

`p0180` begins `het beeld van Phil. den Goed`; the following boards aggregate character adjectives, extracts, bibliography, portrait references and institutional/object locations. Their textual details require close transcription, but their material organization is already clear: the historical `beeld` is assembled through juxtaposition of heterogeneous documentary fragments.

### 5. `p0224–p0225`: copies remain evidence through genealogy

The German art-historical extract treats non-original portraits as still valuable for iconography, provided their relation to earlier exemplars is reconstructed. It even proposes that a miniature and an older painting may derive independently from a lost third original. This makes copying, anachronism, lost originals and image genealogy explicit methodological problems inside the same dossier.

### 6. `p0047`: diagrammatic organization

A hand-drawn boxed/figural diagram is almost entirely missed by OCR. Exact interpretation remains open, but the page confirms that the working archive contains internally produced visual/diagrammatic structures as well as received images and photographic reproductions.

### 7. Negative control

No secure Malinowski / anthropology / ethnology dossier appears in chunk 017. Apparent lexical lookalikes were checked against context and rejected. No Rockefeller provenance cluster appears.

## Short-text pages

`p0094`, `p0177`, `p0228`.

These are genuinely brief notes rather than OCR failures.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 017 retrieval-grade visual audit: COMPLETE (228/228).**

# Chunk 018 visual review summary

## Scope

- Source span: `chunk_018:p0001`–`chunk_018:p0247` (247 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–240, 241–247.
- Page-count check: `40 + 40 + 40 + 40 + 40 + 40 + 7 = 247`.
- Review level: retrieval-grade full-page visual correction layer against the clean PaddleOCR v3 baseline. Raw OCR remains unchanged.
- Material profile: the first ~160 pages are predominantly continuous handwritten American-history/culture notes; the middle includes clippings, a drawing notebook, postcards and small fragments; `p0198–p0216` becomes a dense mounted-card dossier, followed by sustained draft prose and a final short mounted-slip run.

## Result

- **Full-page visual audit: 247/247 complete.**
- Page classes:
  - 1 usable
  - 189 usable-with-noise
  - 48 high-noise
  - 1 false-empty OCR recovery
  - 1 short-text page
  - 7 genuinely blank/no-substantive-text pages
- Baseline empty OCR pages: 8.
- Visual result: 7 genuinely blank/no-substantive and 1 false-empty recovery.

### False-empty recovery

- `p0176`: a printed postcard headed **BRIEFKAART**, with address lines and printed address block, is clearly visible although baseline OCR is empty.

### Genuine blank/no-substantive pages

`p0164`, `p0166`, `p0179`, `p0220`, `p0239`, `p0242`, `p0245`.

`p0164` and `p0166` are book/cover views without substantive text; the others are blank sheets/cards/strips.

### High-noise queue

`p0007`, `p0093`, `p0094`, `p0137`, `p0148`, `p0149`, `p0150`, `p0160`, `p0161`, `p0165`, `p0167–p0175`, `p0177–p0178`, `p0197–p0216`, `p0229`, `p0240–p0241`, `p0243–p0244`, `p0246–p0247`.

Dominant failure modes:

1. **pathological repetition / hallucination**: `p0007` (v3 removed x2024 inline repeats), `p0137` (x574), and `p0229` (a repeated paragraph block removed x90) remain unsafe for quotation;
2. **compound and rotated layouts**: `p0148–p0150`, `p0160–p0161`, and the postcard/small-card run `p0167–p0178` lose ordering and often one entire component;
3. **non-text visual content**: `p0165` contains two profile drawings that OCR cannot represent;
4. **mounted-slip flattening**: `p0198–p0216` and `p0240–p0247` are spatially organized card boards whose meaning depends on adjacency/order that OCR destroys;
5. **near-total under-capture**: `p0197` visually contains a sender envelope plus handwritten slip, while OCR returns only `Afzender`.

## Core-theme results

### 1. William James and explicit analogical reasoning (`p0147–p0150`)

The clean printed page `p0147`, headed **`UIT DE PHILOSOPHIE VAN WILLIAM JAMES`**, includes the formulation **`Het onbekende verklarende naar analogie van het bekende`**. The next page continues the printed discussion of subliminal consciousness and is physically paired with handwritten notes; further handwritten material follows.

This is a high-value analogy-family hit, with a strict attribution control: the explicit formulation belongs to the retained printed James discussion, not automatically to Huizinga's own prose.

### 2. Drawing as working material (`p0165`)

A notebook contains two profile-head sketches and a Leiden bookseller label from **L. F. Servaas & Zonen**. The page extends the visual-method sequence from maps/diagrams/photographs to drawing inside a retained notebook. The identity of the hand and purpose of the sketches remain unresolved.

### 3. Mounted-card method generalizes beyond the Philippe dossier (`p0198–p0216`)

The dark boards carry many small cards on Indigenous/frontier history. Secure source anchors include Turner/trading-frontier material, Helen Hunt Jackson, Friederici and Mooney. The material form closely resembles the montage structure found in chunk 017, but on a different historical problem.

This strengthens a general working-method proposition: Huizinga's archive can preserve **argument-preparatory card montage**, where quotations, statistics, bibliography and source excerpts are arranged spatially before synthesis.

### 4. From card montage to synthetic American-history draft (`p0217–p0238`)

The mounted-card run is followed immediately by sustained comparative prose on American/European history, individualism and economic/political development. `p0217` and `p0219` contain especially clear English framing statements about European history, American history and general contrasts.

The archive therefore supports a concrete operational hypothesis:

`source/bibliographical slips → mounted topical ordering → synthetic draft`

The sequence is materially strong, while one-to-one causal use of individual slips still requires textual matching.

### 5. American visual-culture queue (`p0143–p0146`)

The notes include Whistler, Morris Hunt, Mary Cassatt, George Inness and references to architecture/sculpture. OCR remains too unstable for exact quotation; retain as a close-transcription queue.

### 6. Negative control

No secure Malinowski/anthropology/ethnology dossier was found. `primitive` usages are contextualized within frontier/social development, religion or individualism. Rockefeller references are business-history material rather than Rockefeller Memorial institutional provenance.

## Short-text page

- `p0183`: genuinely brief handwritten note; its limited visible text is broadly commensurate with OCR.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 018 retrieval-grade visual audit: COMPLETE (247/247).**

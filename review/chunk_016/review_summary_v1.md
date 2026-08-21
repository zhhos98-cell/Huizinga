# Chunk 016 visual review summary

## Scope

- Source span: `chunk_016:p0001`–`chunk_016:p0276` (276 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–240, 241–276.
- Page-count check: `40 + 40 + 40 + 40 + 40 + 40 + 36 = 276`.
- Review level: retrieval-grade full-page visual correction layer against the clean PaddleOCR v3 baseline. Raw OCR remains unchanged.
- The scan set is visually dominated by continuous handwritten medieval-history notes, usually photographed as one written sheet beside a blank verso/sheet. A few mounted-board/map pages interrupt that pattern.

## Result

- **Full-page visual audit: 276/276 complete.**
- Page classes:
  - 46 usable
  - 206 usable-with-noise
  - 15 high-noise
  - 1 false-empty OCR recovery
  - 7 short-text pages
  - 1 genuinely blank/no-substantive-text page
- Baseline empty OCR pages: 2.
- Visual result: 1 genuine blank (`p0276`) and 1 false-empty recovery (`p0113`).

### False-empty recovery

`p0113` is a full substantive handwritten manuscript page on the right-hand sheet. The baseline is entirely empty, so the page would disappear from text-only retrieval.

### High-noise queue

`p0018`, `p0021`, `p0030`, `p0034`, `p0035`, `p0036`, `p0065`, `p0077`, `p0098`, `p0127`, `p0158`, `p0159`, `p0214`, `p0253`, `p0275`.

The dominant failure modes differ from chunks 013–015. Here they are mainly:

1. **under-capture of dense handwriting** (`p0018`, `p0021`, `p0034–p0036`, `p0065`, `p0077`, `p0127`);
2. **model hallucination / multilingual drift** (`p0030`, `p0035–p0036`);
3. **compound or mounted layouts** (`p0098`, `p0158–p0159`, `p0214`, `p0275`);
4. **pathological repetition** (`p0030`; `p0253`, where v3 removed an inline run reported as x2001).

`p0120` and `p0126` also carry repetition-cleanup flags but retain enough useful text to remain in the usable-with-noise class.

## Core-theme hits

### 1. Visual method changes form in chunk 016: the map (`p0158–p0159`)

The standout visual object is a mounted hand-drawn regional map with black/red boundary lines and place/region labels, physically paired with a separate note slip. The OCR nearly misses it altogether. This is important because the visual archive is no longer only externally produced plates, portraits, catalogues or publisher ephemera: the working dossier itself contains diagrammatic/cartographic organization.

### 2. Symbolic images as argumentative history (`p0014–p0015`, `p0087`)

The notes follow the two-swords and two-luminaries figures from biblical comparison into mystical/political symbols and later into Dante's criticism of scholastic proofs of papal supremacy. In this sequence, images and symbols function as historical arguments with trajectories, not as decoration.

### 3. Material antiquity and political imagination (`p0124–p0128`)

The Cola di Rienzo sequence joins old monuments, an image/statue on the Capitol, inscriptions/classical names and a political vision centered on Rome. Exact transcription of `p0126` requires care, but the material/monumental cluster is secure.

### 4. From bibliography to reconstruction to `beeld` (`p0200`, `p0217–p0218`)

`p0200` explicitly identifies and criticizes a historical reconstruction associated with Thorold Rogers and notes its later circulation into William Morris. `p0217` gathers a bibliography of English constitutional/economic history; `p0218` then opens a synthetic comparison of the Schism era as a `beeld` of instability, division and change. This is unusually useful evidence for how source apparatus can be transformed into an epochal synthesis.

### 5. Periodization/reflexivity queue (`p0029–p0030`)

`p0029` appears to contrast XIII-century harmony/form with XIV-century conflict/change and to question the subjectivity of that appreciation. `p0030` is too corrupted for quotation, so the pair remains a priority close-transcription target.

### 6. Negative control

No secure Malinowski/anthropology/ethnology/primitive-language dossier appears in chunk 016.

## Short-text pages

`p0028`, `p0058`, `p0079`, `p0114`, `p0144`, `p0216`, `p0274`.

These are visually sparse pages or small mounted notes whose limited substantive text is broadly commensurate with the baseline; they should not be confused with false-empty failures.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 016 retrieval-grade visual audit: COMPLETE (276/276).**

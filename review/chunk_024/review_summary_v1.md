# Chunk 024 OCR/page review summary

## Scope

- Source span: `chunk_024:p0001`–`chunk_024:p0085` (85 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–85; page-count check `40 + 40 + 5 = 85`.
- Review level: full retrieval-grade visual/OCR audit against clean PaddleOCR v3.
- Raw OCR is preserved unchanged; scan-grounded corrections and failure diagnoses are recorded separately.

## Result

- **Full-page audit: 85/85 complete.**
- Final retrieval classes:
  - **30 usable**
  - **31 usable-with-noise**
  - **18 high-noise**
  - **1 false-empty OCR recovery**
  - **1 short-text/title page**
  - **4 blank/no-substantive pages**
- Canonical page-level manifest: `full_visual_audit_manifest_v2.tsv`.
- `full_visual_audit_manifest_v1.tsv` is retained as an audit trail but is superseded for the packet assignment of `p0035–p0048`; the second visual pass showed that several scans combine two documentary streams on the same photographed frame.

### Empty-OCR control

Baseline-empty pages are `p0001`, `p0003`, `p0034`, `p0054`, `p0056`.

- `p0001` is a complete OCR false negative. The narrow handwritten label reads **`Excerpts Kern`**.
- `p0003`, `p0034`, `p0054`, and `p0056` are genuine blank/no-substantive pages.

## Documentary architecture

### 1. Kern extract and cross-chunk overlap (`p0001–p0034`)

`p0001` is the `Excerpts Kern` label. `p0002` is the handwritten cover/title for **Mannen en Vrouwen van Beteekenis in onze Dagen: Hendrik Kern, door J. Huizinga**, Haarlem, H. D. Tjeenk Willink & Zoon, 1899; `p0003` is blank.

`p0004–p0033` are printed pages of the 1899 Kern publication. `p0004–p0012` duplicate the same printed sequence already scanned at `chunk_023:p0179–p0187`; `p0013–p0033` continue the publication beyond chunk 023. `p0033` closes with a numbered publication/review list; `p0034` is blank.

This corrects the earlier boundary assumption that `chunk_023:p0187` was the final surviving page of the printed item.

### 2. Composite Kern + Indian-medicine frames (`p0035–p0048`)

The second visual pass materially changes the first structural description. `p0035` is already an Indian-medicine page: it opens with **`Review of the history of medicine, by Thomas A. Wise, London 1867`** and contains Dhanvantari/Ayurveda and medicinal-plant material.

From `p0036` through `p0047`, many scan frames photograph **two different manuscript sheets side by side**. One sheet belongs to a Kern/Indology/philology/bibliographical strand and is frequently inverted; the other belongs to an Indian-medicine/Ayurveda strand and is usually upright. The baseline OCR therefore often merges two documentary streams into one reading order. Examples include:

- `p0036`: inverted Kern/bibliographical material paired with a medical page listing branches of Ayurveda and physician qualifications;
- `p0037`: Kern biographical/philological notes paired with Indian medical/cosmological notes;
- `p0038–p0042`: inverted Kern bibliography/reference sheets paired with medicine/pharmacy/cosmology notes;
- `p0043–p0047`: the same composite pattern continues, with Indology/inscription/Buddhism material sharing frames with medical/terminological notes.

`p0048` returns to a single dense Kern/Indology/Buddhism note with secure Oldenberg/Kern/Buddhism anchors.

This composite-page structure is a major OCR-quality issue in its own right: some apparent semantic incoherence is produced by scan layout rather than by Huizinga's note-taking.

### 3. Anatomy / medicine (`p0049–p0053`)

A compact run of anatomical notes follows: `Anatomie des Menschen`, circulation, joints, vertebrae, articulations and related terminology. OCR is noisy but generally retrieval-usable. `p0054` is blank.

### 4. Isolated legend/folklore note (`p0055–p0056`)

`p0055` is a separate legend/folklore note. The baseline is badly distorted and belongs in the close-transcription queue. `p0056` is blank.

### 5. Methodological Indian-medicine introduction (`p0057–p0062`)

These pages discuss Indian culture, persistence of conceptual strata, categories of disease/death and the relation between earlier and later forms of thought. `p0061–p0062` are particularly low-contrast and badly under-captured. The occurrence of language about `primitieve` thought here belongs to the methodological framing of Indian medicine; it does not establish a separate anthropology/Malinowski dossier.

### 6. Suśruta / Ayurveda working notes (`p0063–p0085`)

`p0063` visibly begins **`Inhoud van den Susruta`**. The subsequent run covers the branches of medicine, surgery, instruments, cautery, leeches, blood, materia medica, dhātu/doṣa material, water/food, disease classification, physiology, dreams, symptoms and chapter lists, with dense Sanskrit/romanized excerpts.

The baseline remains useful for topic retrieval on much of this run, but exact Sanskrit spelling/diacritics should always be checked against the scan. No silent Sanskrit normalization is applied in the correction layer.

## High-noise queue

`p0036`, `p0038`, `p0041`, `p0042`, `p0044`, `p0046`, `p0055`, `p0059`, `p0061`, `p0062`, `p0065`, `p0066`, `p0070`, `p0074`, `p0075`, `p0076`, `p0082`, `p0084`.

Dominant failure modes:

1. **Composite-frame reading-order collapse** in `p0036–p0047`, where Kern/Indology and Indian-medicine sheets share one scan frame.
2. **Low-contrast under-capture** on `p0061–p0062`.
3. **Mixed-script hallucination** in Sanskrit/romanized material, especially `p0065–p0066`, `p0070`, `p0074`, `p0076`, and `p0084`.
4. **Pathological over-expansion**: `p0075` contains a generated `S1 ...` style formula/sequence absent from the scan; `p0082` contains a long generated `7:1, 7:2, ...` sequence absent from the scan.

## Verified correction anchors

- `p0001`: **`Excerpts Kern`**.
- `p0002`: **Mannen en Vrouwen van Beteekenis in onze Dagen / Hendrik Kern / door J. Huizinga / Haarlem, H. D. Tjeenk Willink & Zoon / 1899**.
- `p0035`: **`Review of the history of medicine, by Thomas A. Wise, London 1867`**; Dhanvantari/Ayurveda anchors visible.
- `p0063`: scan heading **`Inhoud van den Susruta`**; baseline `Susuria` is incorrect.
- `p0075`: the baseline's long generated `S1...` mathematical/formula sequence is not present on the manuscript page.
- `p0076`: the baseline Cyrillic block is hallucinated; the scan is Roman-script/Sanskrit transliteration plus Dutch notes.
- `p0082`: the baseline's `7:1`, `7:2`, ... numeric run is hallucinated; the scan contains ordinary manuscript prose/lists.
- `p0084`: the Vietnamese-like baseline phrase is hallucinated; the scan remains Dutch/Sanskrit/romanized material.

## Retrieval guidance

The printed Kern run `p0004–p0033` is the strongest text-search layer in the chunk. The handwritten material is useful for thematic and name-level retrieval but should not be treated as verbatim transcription. Searches across `p0036–p0047` require particular caution because a single OCR page may contain terms from two physically separate manuscript sheets.

## Status

**Chunk 024 retrieval-grade visual/OCR audit: COMPLETE (85/85). Close transcription remains optional refinement for the 18-page high-noise queue.**

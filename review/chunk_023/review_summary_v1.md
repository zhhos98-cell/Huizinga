# Chunk 023 OCR/page review summary

## Scope

- Source span: `chunk_023:p0001`–`chunk_023:p0187` (187 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–187.
- Page-count check: `40 + 40 + 40 + 40 + 27 = 187`.
- Review level: full retrieval-grade page audit against clean PaddleOCR v3.
- Page-image inspection is used only for OCR quality control, layout recovery, documentary-boundary verification and false-empty recovery.
- Raw OCR is preserved unchanged; corrections are recorded in the review layer.

## Result

- **Full-page audit: 187/187 complete.**
- Page classes:
  - **113 usable-with-noise**
  - **60 high-noise**
  - **4 false-empty OCR recoveries**
  - **2 short-text/title/label pages**
  - **8 blank/no-substantive pages**
- Baseline empty OCR pages: **11**.
- Scan review of baseline empties: **4 false-empty recoveries** and **7 genuine blank/no-substantive pages**.
- One additional nonempty baseline page (`p0063`) is actually blank; its OCR `f4` is spurious.

### False-empty recoveries

`p0017`, `p0096`, `p0110`, `p0174`.

- `p0017`: faint handwritten continuation notes are visible.
- `p0096`: scan reads **`Aanteekeningen Vidūṣaka`**.
- `p0110`: scan recovers **`Sāhityadarpaṇa etc.`** and **`Notities Vidūṣaka`**.
- `p0174`: substantive handwritten Kern-related bibliographical/biographical note is visible on the right-hand card.

### Genuine blank/no-substantive pages

`p0001`, `p0041`, `p0063`, `p0105`, `p0106`, `p0109`, `p0175`, `p0177`.

- `p0041` is the blank reverse of the p0040 contents/folder label.
- `p0063` is a blank ruled card; baseline `f4` is OCR noise.
- `p0177` is a blank inside cover/endpaper in the printed Kern booklet.

### Short-text/title/label pages

`p0040`, `p0176`.

- `p0040`: scan-verified folder/contents label: **`Licht & geluid` / `Kern` / `Betekenisleer` / `Vidūṣaka`**.
- `p0176`: printed 1899 title/cover for Huizinga's **`Hendrik Kern`**.

### High-noise queue

`p0002–p0016`, `p0018–p0021`, `p0027–p0028`, `p0034–p0039`, `p0062`, `p0067`, `p0111–p0131`, `p0149`, `p0165–p0173`.

Dominant failure modes:

1. **small/mounted/compound pages and unstable reading order**, especially in the continuation of the Europe-around-1700 dossier and the Vidūṣaka/Kern supplementary slips;
2. **severe handwriting under-capture**, including `p0014`, where substantial two-sheet content collapses to baseline `100.`;
3. **recycled-paper OCR pollution** in `p0111–p0131`: the model repeatedly captures the same printed exhibition advertisement on the backs/paired sides of research slips instead of the handwritten Sanskrit/Vidūṣaka notes;
4. **repetition artefacts / under-capture** on dense pages such as `p0039`, `p0116`, `p0149`, `p0169`.

## Documentary architecture

### 1. Continuation of chunk 022's `Europ. pol. gesch. rondom 1700` packet (`p0002–p0039`)

The first substantive run continues the separately titled chunk 022 dossier:

`Europ. pol. gesch. rondom 1700. (met materiaal ter voortzetting) 1926/27 1934/35`

The material includes chronology/bibliography sheets, notes on Russia/Peter and the eastern/northern European political system, and printed German source material on Karl Stählin (`p0028–p0030`).

This corrects a purely scan-based boundary in the chunk 022 review: the documentary packet continues across the digital chunk division and reaches at least `chunk_023:p0039`.

### 2. Contents/folder label (`p0040–p0041`)

`p0040` is one of the most structurally useful pages in the chunk. The scan reads:

`Licht & geluid`
`Kern`
`Betekenisleer`
`Vidūṣaka`

`p0041` is its blank reverse.

The subsequent packets match these labels closely, giving source-internal support for the reconstructed architecture.

### 3. `Licht & geluid / Betekenisleer` manuscript (`p0042–p0062`)

`p0042` begins **`Inleiding, pag. 1-19`** and discusses the relation among expressions for perceptions of the different senses, explicitly referring to Jacob Grimm. The run develops comparative linguistic/semantic material around light, sound, movement, intensity and cross-sensory association.

`p0062` is a short quotation/reference insert associated with Jacob Grimm. `p0063` is a blank divider/card.

### 4. Vidūṣaka / Sanskrit-drama dossier (`p0064–p0131`)

`p0064` marks the substantive shift into Sanskrit drama: rasa, laughter/comedy, dramatic characters, Sanskrit terminology and play-specific notes.

Two labels are scan-recovered despite empty OCR:

- `p0096`: **`Aanteekeningen Vidūṣaka`**
- `p0110`: **`Sāhityadarpaṇa etc.` / `Notities Vidūṣaka`**

`p0111–p0131` are mounted supplementary notes. The repeated exhibition advertisement in baseline OCR is a support-material artefact from recycled printed clipping paper, not repeated Huizinga research prose. These pages require slip-level transcription if used substantively.

### 5. Paginated Kern working manuscript (`p0132–p0164`)

`p0132` is red-numbered page `1` and provides an outline/reference map with biographical and Indological names/topics. `p0133` continues with red page numbers `2–3`; the sequence runs continuously to `p0164`, red-numbered `64`.

The safest archival description is a **64-page paginated Kern working manuscript / preparatory text**. It is tightly associated in contents and sequence with the Kern project, while exact textual dependence on the 1899 published version remains a collation question.

### 6. Supplementary Kern notes (`p0165–p0174`)

A set of small biographical/bibliographical notes follows the paginated manuscript. OCR is partial and unstable. `p0174` is a false-empty recovery; `p0175` is a genuine blank divider/card.

### 7. Printed `Hendrik Kern` publication (`p0176–p0187`)

`p0176` identifies the printed layer as:

**Mannen en Vrouwen van Beteekenis in onze Dagen: Hendrik Kern, door J. Huizinga**, Haarlem, H. D. Tjeenk Willink & Zoon, **1899**.

`p0177` is blank. `p0178–p0187` preserve the printed text. This published item is kept distinct from the preceding manuscript and supplementary-note layers.

## Priority close-transcription / collation queue

1. `p0040` — diplomatic transcription of the contents/folder label.
2. `p0017` — recover the faint false-empty continuation note.
3. `p0096` and `p0110` — preserve packet labels in any page-level corpus.
4. `p0042–p0062` — stabilize the `Licht & geluid / Betekenisleer` manuscript, especially terminology and cited comparative forms.
5. `p0064–p0104` — close transcription of the main Vidūṣaka/Sanskrit-drama note sequence.
6. `p0111–p0131` — slip-by-slip recovery separating handwritten research text from recycled exhibition-clipping versos.
7. `p0132` — diplomatic transcription of the Kern manuscript outline/reference map.
8. `p0132–p0164` — collate the 64-page working manuscript against the printed 1899 `Hendrik Kern`.
9. `p0165–p0174` — recover the supplementary Kern notes, including false-empty `p0174`.
10. Cross-chunk collation: link `chunk_022:p0166–p0249` with `chunk_023:p0002–p0039` to establish the full extent of the `Europ. pol. gesch. rondom 1700` packet.

## Negative control

No secure Malinowski / anthropology / Volkenkunde / Rockefeller dossier is established in chunk 023. `Ethnologie` in the `Betekenisleer` argument is a philological/methodological reference within that manuscript and should not be promoted into a separate anthropology dossier.

## Status

**Chunk 023 retrieval-grade OCR/page audit and correction layer: COMPLETE (187/187).**

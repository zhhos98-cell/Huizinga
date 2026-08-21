# Chunk 023 OCR/page review summary

## Scope

- Source span: `chunk_023:p0001`–`chunk_023:p0187` (187 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–187.
- Page-count check: `40 + 40 + 40 + 40 + 27 = 187`.
- Review level: full retrieval-grade page audit against clean PaddleOCR v3.
- Page-image inspection is used only for OCR quality control, layout recovery, documentary-boundary verification, manuscript-pagination verification and false-empty recovery.
- Raw OCR is preserved unchanged; corrections are recorded in the review layer.

## Result

- **Full-page audit: 187/187 complete.**
- Page classes after the close recheck of `p0052`:
  - **112 usable-with-noise**
  - **61 high-noise**
  - **4 false-empty OCR recoveries**
  - **2 short-text/title/label pages**
  - **8 blank/no-substantive pages**
- Baseline empty OCR pages: **11**.
- Scan review of baseline empties: **4 false-empty recoveries** and **7 genuine blank/no-substantive pages**.
- One additional nonempty baseline page (`p0063`) is actually blank; its OCR `f4` is spurious.
- `p0052` is now high-noise rather than usable-with-noise: it is a dense manuscript page marked `20`, while the baseline contains only 526 characters and captures only a small fraction of the visible text.

### False-empty recoveries

`p0017`, `p0096`, `p0110`, `p0174`.

- `p0017`: faint handwritten continuation notes are visible on a card marked `8`.
- `p0096`: rotated scan reads **`Aanteekeningen Vidūsaka`**.
- `p0110`: scan recovers **`Sâhityadarpana etc.`** and **`Notities Vidūsaka`**.
- `p0174`: dense handwritten bibliography page marked `10`. Secure visible anchors include **`Lex Salica` / `Sprache der salischen Franken`**, **`onderwijs der Ned. taal`**, **`Oude Ned. Spraakkunst`**, and **`Middelnederlandsch Woordenboek`**.

The spellings and diacritics above are transcribed as visible on the scans rather than Sanskrit-normalized.

### Genuine blank/no-substantive pages

`p0001`, `p0041`, `p0063`, `p0105`, `p0106`, `p0109`, `p0175`, `p0177`.

- `p0041` is the blank reverse of the `p0040` contents/folder label.
- `p0063` is a blank ruled card; baseline `f4` is OCR noise.
- `p0177` is a blank inside cover/endpaper in the printed Kern booklet.

### Short-text/title/label pages

`p0040`, `p0176`.

- `p0040`: scan-verified folder/contents label: **`Licht & geluid` / `Kern` / `Beteekenisleer` / `Vidūsaka`**.
- `p0176`: printed 1899 title/cover for Huizinga's **`Hendrik Kern`**; baseline `BETE.EKENIS` is corrected to **`BETEEKENIS`**.

### High-noise queue

`p0002–p0016`, `p0018–p0021`, `p0027–p0028`, `p0034–p0039`, `p0052`, `p0062`, `p0067`, `p0111–p0131`, `p0149`, `p0165–p0173`.

Dominant failure modes:

1. **small/mounted/compound pages and unstable reading order**, especially in the continuation of the Europe-around-1700 dossier and the Vidūsaka/Kern supplementary slips;
2. **severe handwriting under-capture**, including `p0014` (substantial two-sheet content collapses to baseline `100.`) and `p0052` (dense full manuscript page collapses to 526 characters);
3. **recycled-paper OCR pollution** in `p0111–p0131`: the model repeatedly captures printed exhibition material on reused support paper rather than the handwritten Sanskrit/Vidūsaka research text;
4. **repetition artefacts / under-capture** on dense pages such as `p0039`, `p0116`, `p0149`, `p0169`.

## Documentary architecture

### 1. Continuation of chunk 022's `Europ. pol. gesch. rondom 1700` packet (`p0002–p0039`)

The first substantive run continues the separately titled chunk 022 dossier:

`Europ. pol. gesch. rondom 1700. (met materiaal ter voortzetting) 1926/27 1934/35`

The material includes chronology/bibliography sheets, notes on Russia/Peter and the eastern/northern European political system, and printed German source material on Karl Stählin (`p0028–p0030`).

This is a documentary-boundary correction: the archival packet crosses the digital chunk division and reaches at least `chunk_023:p0039`.

### 2. Contents/folder label (`p0040–p0041`)

`p0040` is one of the most structurally useful pages in the chunk. The scan reads:

`Licht & geluid`
`Kern`
`Beteekenisleer`
`Vidūsaka`

`p0041` is its blank reverse.

The subsequent packets match these labels closely, giving source-internal support for the reconstructed architecture. The older spelling **`Beteekenisleer`** and source form **`Vidūsaka`** are retained.

### 3. `Licht & geluid / Beteekenisleer` manuscript (`p0042–p0062`)

`p0042` begins the scan-verified heading **`Inleiding. pag. 1–19.`** and discusses the relation among expressions for perceptions of the different senses, explicitly referring to Jacob Grimm. The run develops comparative linguistic/semantic material around light, sound, movement, intensity, association and metaphor.

`p0052`, manuscript page `20`, is a newly tightened OCR warning: the scan shows a dense continuation page, while PaddleOCR retrieves only 526 characters. It therefore belongs in the exact-transcription queue.

`p0062` is a short quotation/reference insert associated with Jacob Grimm. `p0063` is a blank divider/card.

### 4. Vidūsaka / Sanskrit-drama dossier (`p0064–p0131`)

`p0064` marks the substantive shift into Sanskrit drama: rasa, laughter/comedy, dramatic characters, Sanskrit terminology and play-specific notes.

Two labels are recovered despite empty OCR:

- `p0096`: **`Aanteekeningen Vidūsaka`**
- `p0110`: **`Sâhityadarpana etc.` / `Notities Vidūsaka`**

`p0111–p0131` are mounted supplementary notes. The repeated exhibition advertisement in baseline OCR is a support-material artefact from recycled printed paper, not repeated Huizinga research prose. These pages require slip-level transcription if used substantively.

### 5. Paginated Kern working manuscript (`p0132–p0164`)

`p0132` is red-numbered page `1` and provides an outline/reference map with biographical and Indological names/topics. `p0133` continues with red page numbers `2–3`; the sequence runs continuously to `p0164`, red-numbered `64`.

The safest archival description is a **64-page paginated Kern working manuscript / preparatory dossier**. Its connection with the printed 1899 biography is stronger than adjacency alone:

- manuscript `p0137` contains **`International Sanskrit Insurance Company`** and **`Mutual Praise Society`**, phrases that recur in printed `p0187`;
- manuscript `p0155` contains M. de Vries / `Çakuntala` material developed in printed `p0185`;
- manuscript `p0164` records the 1862 `Çakuntala` translation material, also treated in printed `p0185`.

These correspondences establish a demonstrable genetic relationship between the working manuscript/dossier and the publication. They still do not by themselves show that `p0132–p0164` is a line-for-line final printer's copy; full collation remains necessary.

### 6. Supplementary Kern notes (`p0165–p0174`)

A set of smaller biographical/bibliographical notes follows the paginated manuscript. OCR is partial and unstable. `p0174` is a complete OCR false negative, and the scan now identifies it more specifically as a bibliography page with Lex Salica, Dutch-language teaching/grammar, and Middelnederlandsch Woordenboek anchors. `p0175` is a genuine blank divider/card.

### 7. Printed `Hendrik Kern` publication (`p0176–p0187`)

`p0176` identifies the printed layer as:

**Mannen en Vrouwen van Beteekenis in onze Dagen: Hendrik Kern, door J. Huizinga**, Haarlem, H. D. Tjeenk Willink & Zoon, **1899**.

`p0177` is blank. `p0178–p0187` preserve the printed text. This published item is kept distinct from the preceding manuscript and supplementary-note layers while serving as the main collation target for the Kern dossier.

## Priority close-transcription / collation queue

1. `p0017` — recover the faint false-empty continuation note.
2. `p0042–p0062` — stabilize the `Licht & geluid / Beteekenisleer` manuscript; prioritize newly high-noise `p0052`.
3. `p0064–p0104` — close transcription of the main Vidūsaka/Sanskrit-drama sequence.
4. `p0096` and `p0110` — preserve source-spelling packet labels exactly in any page-level corpus.
5. `p0111–p0131` — slip-by-slip recovery separating handwritten research text from recycled exhibition-clipping support material.
6. `p0132` — diplomatic transcription of the Kern manuscript outline/reference map.
7. `p0132–p0164` — full collation against printed `p0178–p0187`, starting with the already matched `p0137↔p0187`, `p0155↔p0185`, and `p0164↔p0185` anchors.
8. `p0165–p0174` — recover the supplementary Kern bibliography/notes, including false-empty `p0174`.
9. Cross-chunk collation: link `chunk_022:p0166–p0249` with `chunk_023:p0002–p0039` to establish the full extent of the `Europ. pol. gesch. rondom 1700` packet.

## Negative control

No secure Malinowski / anthropology / Volkenkunde / Rockefeller dossier is established in chunk 023. `Ethnologie` in the `Beteekenisleer` argument is a philological/methodological reference within that manuscript and should not be promoted into a separate anthropology dossier.

## Status

**Chunk 023 retrieval-grade OCR/page audit and correction layer: COMPLETE (187/187).**

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
- Close-reading corrections now include severe under-capture/recovery work on `p0052`, `p0062`, `p0067`, `p0130–p0132`, `p0165`, and `p0172–p0174`; these are recorded as a review layer rather than silently substituted into raw OCR.

### False-empty recoveries

`p0017`, `p0096`, `p0110`, `p0174`.

- `p0017`: faint handwritten continuation notes are visible on a card marked `8`; exact reading remains unresolved.
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
2. **severe handwriting under-capture**, including `p0014` (substantial two-sheet content collapses to baseline `100.`) and `p0052` (a dense manuscript page is reduced to fragmentary marginal/lower-page OCR);
3. **recycled-paper OCR pollution** in `p0111–p0131`: the model repeatedly captures printed exhibition material or card-stock printing rather than the handwritten research text;
4. **repetition artefacts / under-capture** on dense pages such as `p0039`, `p0116`, `p0149`, `p0169`.

Several high-noise pages now have secure-anchor recovery without being promoted to full diplomatic transcription: `p0052`, `p0067`, `p0130`, `p0131`, `p0165`, `p0172`, and `p0173`.

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

`p0052`, manuscript page `20`, is a severe OCR under-capture. Close reading recovers two methodologically important sentences with high confidence: Huizinga says that individual words have not always been examined with exact philological precision but that recurrent correspondences of development and usage should provide warrant for the general standpoint; he then states that the aim is, **`door in uitgebreiden zin ideeën-associatie aan te nemen`**, to make the understanding of a word easier in many cases. The complete page still belongs in the diplomatic-transcription queue.

`p0062` is a mounted closing quotation/reference insert associated with Jacob Grimm. Scan checking corrects several consequential OCR errors, including **`geheime bezüge`** (not `betrüge`), **`jenen brauch`** (not `jemen`), and **`Jakob Grimm, die V Sinne`**. `p0063` is a blank divider/card.

### 4. Vidūsaka / Sanskrit-drama dossier (`p0064–p0131`)

`p0064` marks the substantive shift into Sanskrit drama: rasa, laughter/comedy, dramatic characters, Sanskrit terminology and play-specific notes.

`p0067` is a small mounted Indological note that baseline OCR badly garbles. The prose can now be read securely as asking whether the Indians only after Alexander called the Greeks **Yavana**, or whether the name must rest on a much older acquaintance; two short ethnonym/comparandum readings remain `[unclear]` and are deliberately left unresolved.

Two labels are recovered despite empty OCR:

- `p0096`: **`Aanteekeningen Vidūsaka`**
- `p0110`: **`Sâhityadarpana etc.` / `Notities Vidūsaka`**

`p0111–p0131` are mounted supplementary notes. The repeated exhibition advertisement in baseline OCR is a support-material artefact from recycled printed paper, not repeated Huizinga research prose. Slip-level recovery has now been started at the end of this run: `p0130–p0131` preserve a continuous German excerpt on laughter, seriousness, congruence/incongruence, and the relation between Begriff and Anschauung. The scan cleanly separates this handwriting from the printed exhibition/card-stock support material. No author attribution is assigned in the correction layer because it is not securely visible on these scans.

### 5. Paginated Kern working manuscript (`p0132–p0164`)

`p0132` is red-numbered page `1` and provides an outline/reference map with biographical and Indological names/topics. A close-reading pass now recovers secure anchors including `het fort v. Makassar`, `Grimm (Scherer)`, `Weber`, `het Skr. woordenb.`, `Kon. Athenaeum`, `Indian Office. Enc.`, `Goldstücker Enc.`, `Bühler's hypothese`, `Ralph Griffith. Enc.`, `de Brahmanen`, `upanayana, huwelijk`, `Brug over Ganges`, `Râmâyana`, `het Georgisch`, `de Ural.-Alt. talen`, `de Ind. ethiek`, and `Prabodhacandrodaya`; unresolved/crossed-out entries remain deliberately unexpanded. `p0133` continues with red page numbers `2–3`; the sequence runs continuously to `p0164`, red-numbered `64`.

The safest archival description is a **64-page paginated Kern working manuscript / preparatory dossier**. Its connection with the printed 1899 biography is stronger than adjacency alone:

- manuscript `p0137` contains **`International Sanskrit Insurance Company`** and **`Mutual Praise Society`**, phrases that recur in printed `p0187`;
- manuscript `p0155` contains M. de Vries / `Çakuntala` material developed in printed `p0185`;
- manuscript `p0164` records the 1862 `Çakuntala` translation material, also treated in printed `p0185`.

These correspondences establish a demonstrable genetic relationship between the working manuscript/dossier and the publication. They still do not by themselves show that `p0132–p0164` is a line-for-line final printer's copy; full collation remains necessary.

### 6. Supplementary Kern notes (`p0165–p0174`)

A set of smaller biographical/bibliographical notes follows the paginated manuscript. OCR is partial and unstable, but several pages now have scan-grounded recovery. `p0165` securely restores **`1868. Over het woord Zarathustra en den mythischen persoon van dien naam.`**; `p0172` yields bibliographical anchors including Kuno Meyer, Bohnenberger, Hugo Schuchardt and *Lives of Saints from the Book of Lismore*; `p0173` restores a Philippines/colonial bibliography note centred on Montero y Vidal and **`El Archipiélago filipino y las islas Marianas, Carolinas y Palaos`**. `p0174` is a complete OCR false negative and is identified as a bibliography page with Lex Salica, Dutch-language teaching/grammar, and Middelnederlandsch Woordenboek anchors. `p0175` is a genuine blank divider/card.

### 7. Printed `Hendrik Kern` publication (`p0176–p0187`)

`p0176` identifies the printed layer as:

**Mannen en Vrouwen van Beteekenis in onze Dagen: Hendrik Kern, door J. Huizinga**, Haarlem, H. D. Tjeenk Willink & Zoon, **1899**.

`p0177` is blank. `p0178–p0187` preserve the printed text. This published item is kept distinct from the preceding manuscript and supplementary-note layers while serving as the main collation target for the Kern dossier.

## Priority close-transcription / collation queue

1. `p0017` — recover the faint false-empty continuation note; current scan is too faint for a responsible exact reading.
2. `p0042–p0062` — continue stabilizing the `Licht & geluid / Beteekenisleer` manuscript. `p0052` and `p0062` now have secure-anchor corrections, but `p0052` still needs full diplomatic transcription.
3. `p0064–p0104` — close transcription of the main Vidūsaka/Sanskrit-drama sequence; `p0067` now has a partial secure reading with two `[unclear]` terms.
4. `p0111–p0131` — slip-by-slip recovery separating handwritten research text from recycled exhibition/card-stock support material. `p0130–p0131` are now partially recovered as a continuous German laughter/seriousness excerpt.
5. `p0132` — complete diplomatic transcription of the Kern manuscript outline/reference map; a substantial set of secure anchors is already recorded.
6. `p0132–p0164` — full collation against printed `p0178–p0187`, starting with the already matched `p0137↔p0187`, `p0155↔p0185`, and `p0164↔p0185` anchors.
7. `p0165–p0174` — continue recovering the supplementary Kern bibliography/notes. `p0165`, `p0172`, `p0173`, and false-empty `p0174` now have secure-anchor records.
8. `p0096` and `p0110` — preserve source-spelling packet labels exactly in any page-level corpus.
9. Cross-chunk collation: link `chunk_022:p0166–p0249` with `chunk_023:p0002–p0039` to establish the full extent of the `Europ. pol. gesch. rondom 1700` packet.

## Negative control

No secure Malinowski / anthropology / Volkenkunde / Rockefeller dossier is established in chunk 023. `Ethnologie` in the `Beteekenisleer` argument is a philological/methodological reference within that manuscript and should not be promoted into a separate anthropology dossier.

## Status

**Chunk 023 retrieval-grade OCR/page audit and correction layer: COMPLETE (187/187); close-transcription/collation refinement remains active.**

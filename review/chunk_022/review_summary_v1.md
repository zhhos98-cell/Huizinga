# Chunk 022 OCR/page review summary

## Scope

- Source span: `chunk_022:p0001`–`chunk_022:p0250` (250 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–240, 241–250.
- Page-count check: `40 + 40 + 40 + 40 + 40 + 40 + 10 = 250`.
- Review level: full retrieval-grade page audit against the clean PaddleOCR v3 baseline.
- Page-image inspection is used only for OCR quality control, page/layout recovery, and verification of titles/dates.

## Result

- **Full-page audit: 250/250 complete.**
- Page classes:
  - **206 usable-with-noise**
  - **30 high-noise**
  - **3 false-empty OCR recoveries**
  - **1 short-text page**
  - **10 blank/no-substantive-text pages**
- Baseline empty OCR pages: 12.
- Scan review result for baseline empties: 3 false-empty recoveries and 9 genuine blank/no-substantive pages.
- One additional nonempty OCR page (`p0150`) contains only an unfilled printed sender-address form and is therefore classified no-substantive.

### False-empty recoveries

`p0014`, `p0019`, `p0166`.

- `p0014`: mounted board with multiple handwritten slips; baseline OCR is empty.
- `p0019`: mounted board with multiple handwritten slips; baseline OCR is empty.
- `p0166`: packet title recovered from the scan:
  - `Europ. pol. gesch. rondom 1700.`
  - `(met materiaal ter voortzetting)`
  - `1926/27`
  - `1934/35`

`p0166` is a major dossier boundary and reuse marker, not a blank page.

### Genuine blank/no-substantive pages

`p0008`, `p0015`, `p0138`, `p0150`, `p0151`, `p0154`, `p0159`, `p0160`, `p0244`, `p0250`.

- `p0150`: only an unfilled printed sender-address form.
- `p0159`: only an unfilled printed `BRIEFKAART` form plus a blank card.
- `p0160`: envelope/cover with printed sender/return label only.
- The others are blank cards/dividers or have no substantive retrievable text.

### Short-text page and critical title correction

`p0038` is a short packet title. The baseline reads:

`Duitsche Rijk 1688. 1924/25. 1934/35`

The scan instead reads:

`Duitsche Rijk 1648–1688. 1924/25. 1934/35 ten deele`

This correction is structurally important: the packet covers **1648–1688**, and its use in **1934/35 is explicitly marked as partial (`ten deele`)**.

### High-noise queue

`p0004–p0007`, `p0009–p0013`, `p0016–p0018`, `p0020–p0022`, `p0039`, `p0152–p0153`, `p0155–p0158`, `p0161–p0165`, `p0200`, `p0215`, `p0249`.

Dominant failure modes:

1. **mounted/compound-page under-capture and unstable reading order** (`p0009–p0022`, `p0152–p0165`);
2. **name-heavy / roster-like lists with unreliable proper-name recognition** (`p0004–p0007`, `p0249`);
3. **dense handwriting/model drift** (`p0039`, `p0200`, `p0215`);
4. **gross over-expansion/repetition on compound material**, especially `p0162`.

## Documentary architecture of the chunk

### 1. Dated 1937–1938 Restoration teaching sequence (`p0001–p0022`)

`p0001–p0003` preserve a compressed dated teaching/course sequence beginning `20.X.37` and continuing into May 1938. Topics include Bourbon Restoration, the Charter, Vienna, Holy Alliance/intervention, Metternich, de Maistre, liberalism, nationalism, German Confederation, France, July Revolution, Belgium, Poland and Switzerland.

The exact institutional course identity is not yet verified. `p0004–p0007` are name/roster-like sheets whose function should remain open, and `p0009–p0022` contain mounted supplementary slips/bibliographical notes with unstable OCR.

Cross-chunk significance: chunk 021 already preserved Restoration material marked `1907/8`, `1920/21`, and dated 1927–1928 course cards. Chunk 022 adds a 1937–1938 dated teaching sequence. This securely establishes repeated teaching/reworking of the same broad historical field across several documentary moments; direct stemmatic copying among the layers still requires collation.

### 2. Inserted Historical Association pamphlet (`p0023–p0037`)

`p0023` begins the printed Historical Association pamphlet **The Congress of Vienna 1814–15 / The Conference of Paris 1919**, including C. K. Webster's comparison of their organisation/results, H. W. V. Temperley's contribution on international government, a Corfu Incident note, and a bibliography; it records papers read at the Fifth International Congress of Historical Sciences, Brussels, 1923.

This is an inserted printed source, **not Huizinga-authored manuscript text**. It should be indexed separately from his handwritten lecture/research notes.

### 3. `Duitsche Rijk 1648–1688` packet (`p0038–p0165`)

The scan-verified title on `p0038` is:

`Duitsche Rijk 1648–1688. 1924/25. 1934/35 ten deele`

The packet therefore preserves a German-Empire/imperial-politics dossier used in 1924/25 and only **partly** reused in 1934/35.

- `p0039–p0137`: dense main working/teaching notes on the post-Westphalian Empire, estates, Reichstag/institutions, imperial politics and connected European diplomacy.
- `p0139–p0149`: a dated 1924/25 teaching-note sequence. OCR securely recovers `5.XI.24`, then additional November/December 1924 and January–May 1925 dates, though several numerals require diplomatic transcription.
- `p0155–p0165`: a mounted supplementary packet explicitly labelled **`Varia bij Duitsche Rijk 1648–1688`**. These pages consist largely of small bibliographical/reference slips and are high-noise because reading order is not linear.

### 4. `Europ. pol. gesch. rondom 1700` packet (`p0166–p0249`)

False-empty `p0166` gives the packet title:

`Europ. pol. gesch. rondom 1700. (met materiaal ter voortzetting) 1926/27 1934/35`

This establishes a **separate but overlapping dossier**, broader than the `Duitsche Rijk` packet.

- `p0167–p0243`: dense manuscript notes on European political history around 1700, including France/Louis XIV, Spanish succession, Sweden/Denmark, Brandenburg/Prussia, Dutch Republic, Poland-Lithuania, Muscovy/Russia/Peter I, Ottoman/Hungarian dimensions, and wider alliance/state-system questions.
- `p0245–p0248`: a numbered, dated 1934–1935 teaching sequence of **25 meetings**, from `1. 10.X.34` through `25. 29.V.35`.
- `p0249`: name/roster-like list; exact function and proper names are not safe to infer from the current OCR.

A scan check corrects meeting 16 on `p0247` from baseline `6.II.35` to **`6.III.'35`**, which restores the chronological weekly sequence between `27.II.35` and `13.III.35`.

### 5. The two early-modern packets should not be collapsed into one course

The strongest structural correction in this audit is that chunk 022 contains at least two separately labelled early-modern packets:

1. `Duitsche Rijk 1648–1688` — `1924/25`, `1934/35 ten deele`;
2. `Europ. pol. gesch. rondom 1700` — `1926/27`, `1934/35`.

Because the first explicitly says `1934/35 ten deele`, the safest inference is that some `Duitsche Rijk` material was partially reused or folded into/alongside the broader 1934–1935 teaching. A direct stemmatic relationship still needs page-by-page collation; the archive does not justify treating `p0038–p0249` as one stable master course.

## High-value conceptual pages

### `p0168`: comparative synthesis of the European state world

`p0168` moves above event chronology and synthetically classifies European states around consolidation, power and changing position. France and England appear as strong/active centres; Prussia and Russia as rising; Italy and the German Empire as fragmented/weak structures; Poland, Turkey and Spain as weakening/declining; Austria and the Dutch Republic are treated as more complex cases.

This is best described as a **synthetic comparative classification of the European state system**, not as Huizinga's own term `state-space`.

### `p0243`: political-military autonomy compared with 1914 and 1935

The scan verifies the line:

`het maximum van monarchale militair-diplomatieke autonomie! - heel anders dan 1914, en 1935?`

The surrounding note links political and military technique to increased means and greater mobility of power/government. A margin phrase reads:

`de krijg als vak en techniek`

This corrects an earlier overstatement: the page does **not** securely say that “war becomes a science.” The source-grounded formulation is that Huizinga treats warfare as a **field/profession and technique** and explicitly compares the conditions of monarchical military-diplomatic autonomy with **1914 and 1935**.

## Priority close-transcription / collation queue

1. `p0038` — diplomatic transcription of the packet title/reuse marker.
2. `p0166` — diplomatic transcription of the false-empty Europe-around-1700 title.
3. `p0001–p0003` — reconstruct the full 1937–1938 Restoration teaching sequence.
4. `p0139–p0149` — stabilize all 1924/25 lecture dates and meeting boundaries.
5. `p0245–p0248` — diplomatic transcription of all 25 meetings in 1934/35; meeting 16 already scan-corrected to `6.III.'35`.
6. `p0168` — close transcription of the state-system synthesis.
7. `p0243` — close transcription of the 1914/1935 comparison and surrounding conceptual language.
8. `p0014`, `p0019`, `p0152–p0165` — slip-by-slip recovery of false-empty and Varia mounted material.
9. `p0004–p0007`, `p0249` — proper-name transcription only if the function/identities become research-relevant.
10. Collate `Duitsche Rijk 1648–1688` against the 1934/35 `Europ. pol. gesch. rondom 1700` course to determine which material was reused `ten deele`.

## Negative control

No secure Malinowski / anthropology / ethnology / Volkenkunde / Rockefeller dossier is established in chunk 022. Apparent OCR proximity should not be promoted into a thematic connection.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `verified_corrections_v1.tsv`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 022 retrieval-grade OCR/page audit and correction layer: COMPLETE (250/250).**

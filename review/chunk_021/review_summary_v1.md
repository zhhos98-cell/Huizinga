# Chunk 021 OCR/page review summary

## Scope

- Source span: `chunk_021:p0001`–`chunk_021:p0235` (235 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–235.
- Page-count check: `40 + 40 + 40 + 40 + 40 + 35 = 235`.
- Review level: retrieval-grade page audit against the clean PaddleOCR v3 baseline.
- Page-image inspection is used only as an OCR-quality-control and false-empty recovery layer.

## Result

- **Full-page audit: 235/235 complete.**
- Page classes:
  - 201 usable-with-noise
  - 26 high-noise
  - 2 false-empty OCR recoveries
  - 3 short-text pages
  - 3 blank/no-substantive-text pages
- Baseline empty OCR pages: 5.
- Page-image result: 2 false-empty recoveries and 3 genuine blank/no-substantive pages.

### False-empty recoveries

`p0001`, `p0196`.

- `p0001`: handwritten title `1850-1900`.
- `p0196`: short handwritten conceptual note within the conservatism sequence; exact opening/name requires close transcription.

### Genuine blank/no-substantive pages

`p0158`, `p0221`, `p0235`.

`p0235` contains only an unfilled printed `BRIEFKAART` postcard form.

### Short-text pages

`p0054`, `p0211`, `p0233`.

- `p0054`: `1815-1848 | 1907/8 | 1920/21`.
- `p0211`: short conceptual/bibliographic note.
- `p0233`: brief dated course card on postcard stock (`9.V.28`).

### High-noise queue

`p0013, p0020, p0028, p0029, p0032, p0033, p0041, p0048, p0061, p0062, p0085, p0090, p0106, p0113, p0127, p0143, p0172, p0173, p0183, p0184, p0188, p0202, p0206, p0212, p0218, p0219`.

Dominant failure modes:

1. **mounted/compound-page under-capture or unstable reading order** (`p0013`, `p0020`, `p0032–p0033`, `p0048`, `p0061–p0062`, `p0127`, `p0172`);
2. **handwriting-model drift / multilingual or generic-text hallucination** (`p0028–p0029`, `p0085`, `p0090`, `p0106`, `p0113`, `p0143`, `p0173`, `p0183–p0184`, `p0188`, `p0202`, `p0206`, `p0212`, `p0218–p0219`);
3. **gross OCR repetition / over-expansion** (`p0041`).

## Documentary structure of the chunk

### 1. `1850-1900` modern-history dossier (`p0001–p0053`)

The title is recovered visually from false-empty `p0001`. The run is a broad working/teaching dossier covering later-nineteenth-century European and global history rather than one continuous narrative. It moves among national unifications and state formation, international politics, the United States, imperial/world questions, religion, science and cultural production.

### 2. `1815-1848` Restoration dossier with reuse marker (`p0054–p0157`)

`p0054` reads `1815-1848 | 1907/8 | 1920/21`. The following notes form a large Restoration-era dossier: post-Napoleonic settlement, Vienna, France, Britain, German and Italian states, nationalism, reaction, romanticism, liberalism and conservatism.

The dates on `p0054` are strong internal evidence of reuse/reworking at more than one teaching moment, but the exact institutional course identity remains unverified.

The later part of this run (`p0139–p0145`) becomes explicitly conceptual, treating reaction, romanticism and conservative/liberal positions as broader political/social attitudes rather than merely party labels.

### 3. Meta-historical periodization and Restoration synthesis (`p0159–p0220`)

`p0159` begins `Reductio / Receptio / Risorgimento / Tijdperde der Restauratie, 1814-1840` and asks what the period-name means and where it applies. It compares `Restauratie` with `Renaissance`, `Reformatie` and `Revolution`, notes the evaluative/aspirational load of epoch terms, and turns to identifying multiple historical `strekkingen`.

`p0160` lists legitimacy, nationalism, constitutionalism, economic expansion/imperialism, conservatism, liberalism, socialism, ultramontanism, positivism and historicism before entering a detailed Restoration/Congress of Vienna/Holy Alliance sequence.

`p0196` is a false-empty recovery inside the conservatism discussion.

`p0207–p0208` are especially important for concepts of historical time: recurrence/restoration, `vooruitgang`, `ontwikkeling`, Enlightenment rationalism and liberalism, with references including Turgot, Condorcet, Guido de Ruggiero and R. G. Collingwood.

`p0218–p0220` attempt a synthetic classification of political values/attitudes, but OCR quality falls sharply and close transcription is required.

### 4. Dated 1927–1928 lecture/course cards (`p0222–p0234`)

The final substantive sequence is explicitly dated from `5.X.'27` to `30.V.'28`. It revisits Restoration, Reaction and Romanticism, Louis XVIII/Charter, Vienna, Holy Alliance and intervention, Metternich, de Maistre, Chateaubriand, Adam Müller/Haller, liberalism and revolution.

This gives unusually strong internal evidence for reconstructing a teaching sequence across the 1927–1928 academic year.

### 5. Reuse across documentary layers

Taken together, `p0054`, `p0159–p0220`, and `p0222–p0234` strongly suggest repeated teaching/reworking of the same Restoration and political-concept material across several documentary moments: `1907/8`, `1920/21`, and `1927/28`. This is an archival inference from internal dating and thematic recurrence, not yet a stemmatic proof of direct copying or a verified course catalogue identification.

## Priority close-transcription / collation queue

1. `p0001` for title recovery in any page-level corpus.
2. `p0054` and adjacent pages to establish the `1907/8` / `1920/21` reuse context.
3. `p0139–p0145` for the reaction/romanticism/conservatism conceptual sequence.
4. `p0159–p0160` for a diplomatic transcription of the periodization argument and list of `strekkingen`.
5. `p0196` to recover the exact subject/name and wording of the conservative-system note.
6. `p0207–p0208` for the progress/development/liberalism sequence.
7. `p0218–p0220` because OCR model drift currently obscures a potentially important synthetic classification.
8. `p0222–p0234` for a dated reconstruction of the 1927–1928 lecture/course sequence and comparison with the earlier Restoration dossier.

## Negative control

No secure Malinowski / anthropology / ethnology / ethnography / Volkenkunde dossier appears in chunk 021. No Rockefeller transaction or dossier is securely established.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 021 retrieval-grade OCR/page audit: COMPLETE (235/235).**

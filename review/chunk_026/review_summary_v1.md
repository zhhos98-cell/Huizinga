# chunk_026 review summary

`chunk_026:p0001-p0254` contains 254 scan pages. A full-page visual audit against the conservative PaddleOCR v3 baseline is complete. Raw OCR is preserved unchanged; this review is a separate retrieval-grade correction/triage layer, not a diplomatic transcription.

## Result

- 254/254 scan pages visually checked.
- 18 pages: `usable`.
- 125 pages: `usable-with-noise`.
- 75 pages: `high-noise`.
- 13 pages: `short-text`.
- 5 pages: substantive `false-empty-recovery`.
- 18 pages: `blank/no-substantive`.
- Baseline empty OCR pages: 28 total. Visual review resolves them as 5 substantive false negatives, 5 short-text pages, and 18 genuine blanks/no-substantive pages.

The five complete substantive false negatives are: `p0013`, `p0053`, `p0055`, `p0057`, `p0237`. Baseline-empty pages with only short archival/printed text are `p0001`, `p0047`, `p0058`, `p0122`, `p0133`. The 18 genuine blank/no-substantive pages are: `p0039`, `p0040`, `p0051`, `p0144`, `p0166`, `p0167`, `p0171`, `p0175`, `p0178`, `p0183`, `p0186`, `p0193`, `p0199`, `p0202`, `p0216`, `p0220`, `p0231`, `p0252`.

`p0013` is particularly important as an OCR miss: the scan contains a full handwritten Indian-medicine page headed **“Mala 1.”**. `p0053`, `p0055`, and `p0057` are handwritten postcard backs in the political-pamphlet catalogue sequence; `p0057` visibly includes **“Sources de France”**, **“Vauban”**, **“Projet de paix”**, and **“1706”**. `p0237` is a dense mounted-slip board with substantive handwritten material throughout.

## Documentary structure

`p0001-p0037` continues the Indian-medicine/Ayurveda/physiology complex. `p0001` is a folder/cover with the faint label **“physiologie”** and Roman numeral II. The loose notes that follow contain headings and concepts including `Dosa`, `Dhātu`, `Mala`, humoral/constitutional schemes and discussion of Indian medicine. OCR quality is unstable here: the visible manuscript is predominantly Latin-script handwriting, while the baseline sometimes substitutes or inserts Chinese, Korean, Tibetan-like and other unrelated scripts.

`p0038-p0044` is a transition into European political-pamphlet material. `p0038` is a manuscript overview around pamphlets of 1700-1713; `p0041-p0044` are mounted bibliographical slips. From `p0045-p0156` the physical format becomes a long postcard catalogue sequence: scans repeatedly show `BRIEFKAART` fronts paired with handwritten backs containing titles, references and notes on European politics, dynastic succession and the War of the Spanish Succession. `p0157-p0165` then shifts to dense continuous manuscript synthesis on the same pamphlet/succession complex.

`p0168-p0223` forms a large metrology/numismatics/monetary-history working complex. Most pages are mounted-slip boards, often two boards per scan, dealing with weights, measures, coinage, medieval and early-modern monetary institutions, and related historical references. This is the most reading-order-sensitive portion of the chunk and the main concentration of high-noise pages. `p0224-p0232` continues the same subject on looser sheets and tables.

`p0233-p0236` inserts regular printed numismatic/bibliographical material, including **Wörterbuch der Münzkunde**, catalogues of ancient coin publications, and **Museumskunde**. `p0238` is a short label reading **GROTIVS** and `p0239` an envelope/archival label. `p0240-p0254` then moves decisively into the learned-letters/Grotius documentary complex: `p0240` is a 1908 Maatschappij der Nederlandsche Letterkunde circular describing P. C. Molhuysen's catalogue of printed scholarly letters; `p0241-p0251` is an alphabetical bibliography; `p0253-p0254` prints the **Statuten van de “Vereeniging voor de uitgave van Grotius.”**

## OCR pathologies

The dominant failure modes are unrelated-script substitution in the Ayurveda notes, severe under-capture on sparse/multi-item frames, generated table structure, reading-order collapse on mounted boards, and large hallucinated repetition/number sequences. Clear machine failures include: `p0026` hallucinated repetition; `p0029` and `p0148` long character-run cleanup; `p0032` and `p0168` massive repeat-run removal; `p0065` and `p0140` generated duplicate-table rows; `p0100` Tibetan-like script hallucination; `p0191` and `p0197` generated number-sequence overexpansion; `p0195` Cyrillic-like substitution; `p0203` semantic intrusion including “cybersecurity”; `p0205` repeat-run cleanup; `p0210` duplicate-table generation; `p0211` character-run plus semantic hallucination; `p0212` severe under-capture; `p0215` Arabic-like script substitution; `p0222` a repeated paragraph-block cycle; and `p0228` near-total under-capture plus a character run.

The high-noise queue is explicit in `full_visual_audit_manifest_v1.tsv` and `status.txt`. These pages remain useful for coarse keyword retrieval where recognizable anchors survive, but scan-level checking is required before quotation and mounted-slip order must not be inferred from OCR order.

## Research-facing notes

Three clusters are worth retaining for later analysis. First, `p0029-p0033` repeatedly uses **primitief/primitieve** while characterising Indian medicine and its conceptual strata. In this chunk that language belongs to a history-of-medicine/intellectual classification context, so it should not be promoted by itself into a claim about Huizinga's anthropology or later cultural theory.

Second, `p0131-p0132` contains an unusually direct play/game item: **“Vorstelijk Kaartspel”** / **“Vorstelyk Kaartspel tusschen een Spanjaard, Hollander, Fransman, Engelsman en Hoogduitser”**. The notes treat card play as a vehicle for political and economic positions among European powers. This is a genuine first-order play/game hit and is stronger for the play-history branch than generic occurrences of `spel` elsewhere in the chunk.

Third, the final Grotius block is institutionally substantial. `p0253-p0254` defines the purpose and governance of the **Vereeniging voor de uitgave van Grotius**; the dated statute at `p0254` (2 January 1917) lists **J. Huizinga** among the signatories together with C. van Vollenhoven, P. C. Molhuysen, A. Eekhof, G. Vissering, D. F. Scheurleer and G. J. Fabius. This is direct documentary evidence of Huizinga's participation in the Grotius editorial/institutional project.

## Files

- `full_visual_audit_manifest_v1.tsv` - canonical 254-page retrieval classification.
- `empty_ocr_visual_review_v1.tsv` - all 28 baseline-empty pages, visually resolved.
- `composite_page_structure_v1.tsv` - physical layout and documentary-sequence warnings.
- `core_theme_hits_v1.md` - research-facing conceptual/institutional hits.
- `status.txt` - compact machine-readable status.

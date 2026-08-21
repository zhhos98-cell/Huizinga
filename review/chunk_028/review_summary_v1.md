# chunk_028 review summary

`chunk_028:p0001-p0244` contains 244 scan pages. A full-page visual audit against the conservative PaddleOCR v3 baseline is complete. Raw OCR is preserved unchanged; this review is a separate retrieval-grade correction/triage layer, not a diplomatic transcription.

## Result

- 244/244 scan pages visually checked.
- 0 pages: `usable`.
- 49 pages: `usable-with-noise`.
- 134 pages: `high-noise`.
- 15 pages: `short-text`.
- 11 pages: substantive `false-empty-recovery`.
- 35 pages: `blank/no-substantive`.
- Baseline empty OCR pages: 53 total. Visual review resolves them as 11 substantive false negatives, 7 short-text pages, and 35 genuine blanks/no-substantive pages.

The eleven substantive false negatives are `p0055`, `p0060`, `p0076`, `p0087`, `p0114`, `p0134`, `p0137`, `p0140`, `p0141`, `p0177`, `p0230`. All are visibly populated mounted boards despite empty baseline OCR. The seven baseline-empty short-text pages are `p0081`, `p0169`, `p0173`, `p0174`, `p0182`, `p0197`, `p0213`. `p0081` reads **“Godsdienst verslag”**; `p0169`, `p0174`, and `p0182` are exact Laura Spelman Rockefeller Memorial letterheads; `p0197` contains only **“1463.”**

The 35 genuine blank/no-substantive pages are `p0001`, `p0027`, `p0037`, `p0046`, `p0054`, `p0057`, `p0064`, `p0067`, `p0070`, `p0074`, `p0077`, `p0088`, `p0091`, `p0095`, `p0098`, `p0101`, `p0105`, `p0109`, `p0113`, `p0116`, `p0120`, `p0123`, `p0129`, `p0133`, `p0136`, `p0139`, `p0142`, `p0147`, `p0151`, `p0214`, `p0224`, `p0225`, `p0228`, `p0231`, `p0234`.

## Documentary structure

`p0001-p0053` continues the late-medieval English/Burgundian/Low Countries source-work complex from chunk 027. Most early pages are paired handwritten extracts and archival references around England, Holland, Zeeland and Burgundy; multi-slip boards recur at `p0011-p0012`, `p0025-p0026`, `p0035-p0036`, and from `p0044` onward. Some pages also bring in Geert Groote, Erasmus and related humanist/religious material. `p0001`, `p0027`, `p0037`, and `p0046` function as blank green cover/separator pages.

`p0055-p0080` becomes a dense mounted intellectual-history sequence. References to Renaissance/humanist material, Erasmus, *civilitas* and moral/religious vocabulary recur, but the OCR is often badly corrupted. `p0081` then supplies a useful physical label: **“Godsdienst verslag.”** From `p0083-p0153` the archive remains dominated by mounted boards of religious, classical, humanist and moral-culture notes. `p0154-p0197` continues the same broad working complex but is punctuated by a concentrated run of Laura Spelman Rockefeller Memorial stationery and increasingly sparse boards. `p0183` is particularly valuable: an envelope marked **“Renaissance”** accompanies slips including **“Met dien primitief begrip der Renaissance…”** and **“Contrast Erasmus & Machiavelli.”**

`p0198-p0212` shifts sharply into loose dated political-history notes and postcard backs. The sequence concerns 1830/1848, revolution, constitutional change, national movements, Cavaignac, Marx and related nineteenth-century political chronology. `p0208`, dated 24 September and 1 October 1930, includes the OCR/visual anchor **“1848 als klassenstrijd.”** After a short separator at `p0213-p0214`, `p0215-p0244` returns to mounted boards and dense bibliographical/political notes on the same nineteenth-century complex, especially German, Italian and French developments around 1848.

## OCR pathologies

The dominant failure mode is the same one seen in neighboring chunks: mounted-board reading-order collapse plus severe under-capture. Chunk 028 also contains an unusually high concentration of semantic hallucination. Clear examples include `p0079` (modern **“2024 World Economic Forum”** intrusion), `p0086` (character-run removal plus duplicated/generated **KONINKLIJKE AKADEMIE** text), `p0102` (the test phrase **“The quick brown fox jumps over the lazy dog”**), `p0135` and `p0145` (modern semantic intrusions), `p0166` (generated modern/geographical material), `p0171` (invented conversational/economic prose), `p0216` (large over-generated text on a mounted board), `p0218` (invented **Bureau of Ethnology** citation), `p0232` (long **Quizlet** hallucination), `p0237` (massive repeated paragraph block removed by v3 cleanup), and `p0239-p0240` (modern semantic intrusions and suspicious over-generation). `p0128`, `p0216`, `p0240`, `p0242`, and `p0243` are also suspiciously long relative to their physical mounted-board layouts.

The high-noise queue is explicit in `full_visual_audit_manifest_v1.tsv` and `status.txt`. Mounted-slip OCR must never be treated as preserving the physical order of the slips, and exact quotation from high-noise pages requires direct scan verification.

## Research-facing notes

Three points should be retained. First, `p0183` gives unusually direct first-order evidence about the conceptual category **Renaissance**, including a visible phrase beginning **“Met dien primitief begrip der Renaissance…”** and a separate **“Contrast Erasmus & Machiavelli”** slip. This is stronger than generic OCR hits because both the packet label and conceptual juxtaposition are visible on the scan.

Second, `p0198-p0212` is a coherent teaching/working sequence for nineteenth-century political history. The dated cards make the sequence analytically useful for reconstructing how categories such as revolution, class conflict, nationalism and constitutionalism were organized in Huizinga's notes.

Third, chunk 028 adds nine visually verified Rockefeller stationery occurrences, three of them baseline-empty OCR misses. These have been added to the cross-chunk stationery index, but remain documentary occurrences only.

The apparent ethnology reference at `p0218` is a machine hallucination, and no secure direct Malinowski/anthropology/ethnology hit was found in this chunk.

## Files

- `full_visual_audit_manifest_v1.tsv` - canonical 244-page retrieval classification.
- `empty_ocr_visual_review_v1.tsv` - all 53 baseline-empty pages, visually resolved.
- `composite_page_structure_v1.tsv` - documentary/layout segmentation and reading-order warnings.
- `core_theme_hits_v1.md` - research-facing conceptual/institutional hits and negative controls.
- `status.txt` - compact machine-readable status.

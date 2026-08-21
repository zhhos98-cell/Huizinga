# chunk_030 review summary

`chunk_030:p0001-p0237` contains 237 scan pages. A full-page visual audit against the conservative PaddleOCR v3 baseline is complete. Raw OCR is preserved unchanged; this review is a separate retrieval-grade correction/triage layer, not a diplomatic transcription.

## Result

- 237/237 scan pages visually checked.
- 0 pages: `usable`.
- 56 pages: `usable-with-noise`.
- 135 pages: `high-noise`.
- 5 pages: `short-text`.
- 10 pages: substantive `false-empty-recovery`.
- 31 pages: `blank/no-substantive`.
- Baseline empty OCR pages: 44 total. Visual review resolves them as 10 substantive false negatives, 3 short-text pages, and 31 genuine blanks/no-substantive pages.

The ten substantive false negatives are `p0017`, `p0035`, `p0038`, `p0043`, `p0044`, `p0100`, `p0163`, `p0167`, `p0182`, `p0184`. All are visibly populated mounted boards despite empty baseline OCR. The three baseline-empty short-text pages are `p0091`, `p0096`, `p0183`: `p0091` contains one short handwritten slip; `p0096` and `p0183` are exact Laura Spelman Rockefeller Memorial letterheads.

The 31 genuine blank/no-substantive pages are `p0001`, `p0004`, `p0007`, `p0010`, `p0013`, `p0018`, `p0022`, `p0023`, `p0024`, `p0029`, `p0040`, `p0058`, `p0062`, `p0066`, `p0067`, `p0073`, `p0074`, `p0077`, `p0080`, `p0084`, `p0089`, `p0134`, `p0135`, `p0147`, `p0148`, `p0158`, `p0164`, `p0168`, `p0173`, `p0179`, `p0237`.

## Documentary structure

`p0002-p0057` is dominated by mounted intellectual- and political-history boards. The material ranges across eighteenth-century political thought, Leslie Stephen, Romanticism/Renaissance vocabulary and related bibliography. Reading order is physical-layout dependent, and the baseline frequently substitutes fluent modern prose or mixed scripts for the handwritten slips.

`p0059-p0065` forms a short bibliographical transition, including orange printed cards visually associated with Friedrich Meinecke and a `Staatsräson` reference. `p0068-p0122` then settles into a large Burke/British political-thought complex. Visible/OCR anchors include *Speech on American Taxation*, *A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful*, *Appeal from the New to the Old Whigs*, and *Letters on a Regicide Peace*. `p0120` closes the sequence with a composite board plus dense manuscript page and an OCR-supported scholasticism/Renaissance transition.

`p0123-p0133` shifts into loose working notes on British radicalism and reform around 1790-1820, including Burdett, Cobbett, Cochrane, Major Cartwright, Manchester/Peterloo-era agitation and the 1819-1820 crisis. After two blank separators, `p0136-p0146` becomes an explicitly organized **Revolution** packet, first on mounted boards and then on longer conceptual-history cards. `p0140-p0142` also preserve Sociëteit Minerva / Quaestuur printed stationery.

`p0149-p0195` returns to mounted revolution/social-thought and political-biographical boards. Proudhon appears at `p0180`. Four exact Laura Spelman Rockefeller Memorial letterheads occur in the chunk: `p0092`, `p0096`, `p0183`, `p0186`; the middle two are baseline-empty OCR misses.

`p0196-p0223` is a coherent full-sheet Parliamentary Debates / English-radicalism sequence, with 1819-1820 parliamentary chronology, reform, post-Napoleonic unrest and the suspension of Habeas Corpus. `p0215-p0221` are visually regular manuscript/typescript pages but the OCR suffers severe character-order collapse and semantic over-generation. `p0224-p0236` then breaks sharply back to medieval Zeeland/Flanders source work on Middelburg, parishes, wateringen and ecclesiastical/toponymic evidence, continuing directly into chunk 031. `p0237` is blank.

## OCR pathologies

The dominant failure mode in the mounted sections is reading-order collapse plus lexical/semantic hallucination. Particularly clear examples include `p0019` (modern 2020/URL intrusion), `p0037` and `p0055` (mixed-script hallucination), `p0046` (generated modern prose), `p0079` (repetitive Spanish prose), `p0093-p0094` (Beijing/conversational intrusions), `p0108` (massive asterisk-run over-generation), `p0112` (character-run cleanup plus generic geographic prose), `p0127` (generated repeated place list), `p0137` (test-like English sentence plus Thai), `p0138` (modern URL and repeat cleanup), `p0153-p0155` (repeat/mixed-script semantic over-generation), `p0161` (modern web/conversational intrusion), `p0185` (numeric enumeration explosion), `p0187` (2020/Macau intrusion), `p0189-p0192` (mixed-script, 2022 and conversational intrusions), and `p0215-p0221` (large-scale character-order corruption/over-generation). `p0223` is severely under-captured and contains a removed token-repetition run.

Mounted-slip OCR must never be treated as preserving the physical order of the slips, and exact quotation from `high-noise` or `false-empty-recovery` pages requires direct scan verification.

## Research-facing notes

Three clusters are especially strong. First, `p0041` and `p0136-p0146` preserve explicit first-order conceptual work on **Renaissance** and **Revolution**. Second, `p0068-p0133` and `p0196-p0223` form a very large political-thought/radical-politics working complex, particularly around Burke and British reform politics. Third, `p0224-p0236` shows a clean documentary shift into medieval Zeeland/Flanders ecclesiastical-geographical research, useful for distinguishing thematic packets and for linking chunk 030 to chunk 031.

The OCR-only `primitieit/primitief`-like form on `p0236` belongs to this medieval Zeeland/Flanders context and is not evidence for anthropology. No secure direct Malinowski/anthropology/ethnology hit was found.

## Files

- `full_visual_audit_manifest_v1.tsv` — canonical 237-page retrieval classification.
- `empty_ocr_visual_review_v1.tsv` — all 44 baseline-empty pages, visually resolved.
- `composite_page_structure_v1.tsv` — documentary/layout segmentation and reading-order warnings.
- `core_theme_hits_v1.md` — research-facing conceptual/institutional hits and negative controls.
- `status.txt` — compact machine-readable status.

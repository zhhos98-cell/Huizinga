# chunk_029 review summary

`chunk_029:p0001-p0240` contains 240 scan pages. A full-page visual audit against the conservative PaddleOCR v3 baseline is complete. Raw OCR remains unchanged; this review is a separate retrieval-grade correction and triage layer, not a diplomatic transcription.

## Result

- 240/240 scan pages visually checked.
- 1 page: `usable-with-noise`.
- 168 pages: `high-noise`.
- 2 pages: `short-text`.
- 17 pages: substantive `false-empty-recovery`.
- 52 pages: `blank/no-substantive`.
- Baseline empty OCR pages: 70 total. Visual review resolves them as 17 substantive false negatives, 1 short-text page, and 52 genuine blank/no-substantive pages.

The seventeen substantive false negatives are `p0003`, `p0018`, `p0019`, `p0032`, `p0040`, `p0045`, `p0050`, `p0063`, `p0064`, `p0084`, `p0172`, `p0182`, `p0200`, `p0203`, `p0220`, `p0227`, `p0232`. All are visibly populated mounted boards despite empty baseline OCR. `p0148` is the single baseline-empty short-text page: one short mounted slip is visible. `p0147` is another genuinely short single-slip page but was not baseline-empty.

The 52 visually verified blank/no-substantive pages are `p0001`, `p0021`, `p0028`, `p0031`, `p0034`, `p0037`, `p0041`, `p0046`, `p0049`, `p0053`, `p0056`, `p0059`, `p0062`, `p0065`, `p0069`, `p0075`, `p0082`, `p0086`, `p0091`, `p0096`, `p0102`, `p0111`, `p0114`, `p0117`, `p0120`, `p0123`, `p0128`, `p0133`, `p0142`, `p0146`, `p0149`, `p0152`, `p0159`, `p0162`, `p0165`, `p0169`, `p0173`, `p0183`, `p0190`, `p0193`, `p0201`, `p0204`, `p0207`, `p0213`, `p0214`, `p0217`, `p0221`, `p0225`, `p0228`, `p0231`, `p0234`, `p0237`.

## Documentary structure

`p0001-p0041` continues the nineteenth-century political-history sequence already visible at the end of chunk 028. The material is organized on mounted boards around 1830/1848/1852, France and Italy, with recurrent references to Cavaignac, Tocqueville, Marx, Louis-Napoleon, constitutional change and national movements. `p0042` then gives a strong physical anchor: the accompanying envelope is visibly labelled **“Mazzini.”** `p0042-p0061` continues as an Italian/national-movement working packet.

From roughly `p0062-p0160` the center of gravity changes to English constitutional and institutional history: monarchy, Parliament, cabinet/government, Privy Council, standing army, courts, legal forms, fiscal structures, universities and related institutional vocabulary. These are overwhelmingly mounted multi-slip boards, so OCR order must never be treated as the physical order of Huizinga's notes.

`p0161-p0207` moves into eighteenth-century English political, literary, religious and cultural material. The most important documentary shift comes at `p0208-p0212`, a Horace Walpole source-acquisition packet. `p0208` contains an envelope headed **“Horace Walpole”** and three Koninklijke Bibliotheek request cards in Huizinga's name dated 12 November 1925; `p0210` contains two more. Visible titles include *Memoirs*, *Fugitive Pieces* and *Historic Doubts*. `p0211` is a Leiden University Library request for *The Castle of Otranto*, dated 13 November 1925, and `p0212` requests *Works. ed. Berry. 5 vol. 1790*, also dated 13 November; that sheet bears a 23 November 1925 stamp. In this local sequence the archive preserves not just reading notes but the practical infrastructure of requesting books, receiving them, excerpting them and filing the results.

After short separators at `p0213-p0217`, `p0218` begins a packet whose envelope reads **“Methodisme.”** Its slips concern Wesley and enthusiasm, including a visible heading **“Wesley's Journal.”** `p0222` is another deliberately assembled conceptual packet around **sentimentalism**, with repeated explicit sentimentalism vocabulary and eighteenth-century literary references. These two pages are strong first-order evidence for Huizinga's category-building around religion, emotion, moral psychology and eighteenth-century culture.

## OCR pathologies

Chunk 029 is one of the clearest demonstrations that semantic plausibility cannot be used as an OCR quality criterion. Representative failures include repeated/generated Marx strings (`p0006-p0007`), modern Brooklyn/2021 material (`p0008`), modern scientific/technical intrusions (`p0010-p0012`), massive over-generation (`p0015`), a fabricated 1978 Paris “International Conference on Art and Art Techniques” (`p0033`), modern dates and software/computing language on historical boards (`p0044`, `p0067`, `p0072-p0073`, `p0079-p0080`, `p0097`, `p0104`, `p0112`, `p0121`, `p0127`, `p0140`, `p0155`, `p0166-p0167`, `p0178-p0179`), a generated table at `p0189`, and the exact test phrase **“The quick brown fox jumps over the lazy dog”** at `p0205`. `p0216` required v3 removal of 1,356 copies of an inline repeat run.

Two lexical traps matter for research retrieval. `p0187` produces “Renaissance” in OCR, but direct visual inspection shows an eighteenth-century British political board, including Pitt references; the lexical hit is false. `p0178` contains anthropology-like OCR amid obvious modern/gibberish generation, while the scan provides no secure anthropology/ethnology evidence. No direct Malinowski/anthropology/ethnology hit was verified, and no Laura Spelman Rockefeller Memorial stationery was found in this chunk.

## Research-facing result

Four clusters deserve promotion beyond page-level audit: the continuation of the 1848 political sequence with the `p0042` **Mazzini** packet; the `p0208-p0212` Horace Walpole library-request/source-acquisition packet; the `p0218` **Methodisme / Wesley / enthusiasm** packet; and the `p0222` **sentimentalism** packet. Together they show the archive switching from political category-building to a materially documented eighteenth-century research workflow and then to deliberately filed conceptual complexes around religion and sentiment.

## Files

- `full_visual_audit_manifest_v1.tsv` — canonical 240-page retrieval classification.
- `empty_ocr_visual_review_v1.tsv` — all 70 baseline-empty pages, visually resolved.
- `composite_page_structure_v1.tsv` — documentary/layout segmentation and reading-order warnings.
- `core_theme_hits_v1.md` — research-facing conceptual/institutional hits and negative controls.
- `status.txt` — compact machine-readable status.

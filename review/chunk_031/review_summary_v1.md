# chunk_031 review summary

`chunk_031:p0001-p0247` contains 247 scan pages. A full-page visual audit against the conservative PaddleOCR v3 baseline is complete. Raw OCR is preserved unchanged; this review is a separate retrieval-grade correction/triage layer, not a diplomatic transcription.

## Result

- 247/247 scan pages visually checked.
- 19 pages: `usable`.
- 15 pages: `usable-with-noise`.
- 154 pages: `high-noise`.
- 29 pages: `short-text`.
- 15 pages: substantive `false-empty-recovery`.
- 15 pages: `blank/no-substantive`.
- Baseline empty OCR pages: 41 total. Visual review resolves them as 15 substantive false negatives, 11 short-text/minimal pages, and 15 genuine blanks/no-substantive pages.

The fifteen substantive false negatives are `p0008`, `p0009`, `p0028`, `p0053`, `p0058`, `p0068`, `p0083`, `p0089`, `p0106`, `p0181`, `p0225`, `p0239`, `p0240`, `p0242`, `p0246`. They include populated mounted boards and full manuscript sheets despite empty baseline OCR.

The eleven baseline-empty short-text/minimal pages are `p0046`, `p0055`, `p0059`, `p0082`, `p0088`, `p0099`, `p0113`, `p0127`, `p0132`, `p0171`, `p0216`. The first nine are exact Laura Spelman Rockefeller Memorial letterheads; `p0171` and `p0216` carry only very sparse pencil/handwritten annotations.

The fifteen verified blank/no-substantive pages are `p0025`, `p0026`, `p0029`, `p0032`, `p0044`, `p0045`, `p0152`, `p0170`, `p0173`, `p0230`, `p0231`, `p0234`, `p0238`, `p0241`, `p0244`.

## Documentary structure

`p0001-p0150` is dominated by the medieval Zeeland/Walcheren **Burg/Kerspel** research dossier that begins at the end of chunk 030. The opening loose sheets include the visible heading **“De naam Zeeland”**; the sequence then expands into mounted boards, maps, excerpts and place-name/parish material around Middelburg, Souburg, Domburg, Walcheren and related Low Countries historical geography. The mounted pages are strongly layout-dependent and the OCR often invents modern prose or mixes scripts.

Within that long complex, `p0042-p0043` preserve Dutch/French Belgian Royal Library request forms; `p0042` visibly carries Huizinga’s name. From `p0046` through `p0145`, Rockefeller Memorial letterhead sheets recur densely between mounted boards. Twenty-one exact visual letterheads occur in the chunk, nine of them complete baseline OCR misses. Their recurrence is documentary context only and should not be promoted into a funding/sender claim.

`p0156-p0169` changes form sharply into printed scholarly polemic on the authenticity of the Middelburg city right of 1254. The first printed item closes with H. Obreen; the reply closes with O. Oppermann. `p0174-p0176` then contains Otto Piper / *Burgenkunde* publisher material, followed by `p0177-p0180` printed review/reception material. `p0177` explicitly discusses J. Huizinga’s *Burg en Kerspel in Walcheren* under “L’organisation primitive de l’île de Walcheren.”

`p0181-p0207` returns to loose manuscript working sheets. Physical order is straightforward, but OCR quality collapses badly: many pages are visually ordinary handwritten notes while the model produces modern websites, stock phrases, equations and unrelated English. `p0201-p0202` introduce “Stempel” working notes and a Koninklijke Nederlandsche Akademie van Wetenschappen memorandum.

`p0208-p0229` is a coherent **Ancien Régime / French Revolution** working sequence. `p0208` opens with cultural/artistic notes on the Ancien Régime; `p0217` is visibly headed “Max. Robespierre”; subsequent pages continue revolutionary chronology, institutions and actors. `p0230-p0247` returns to mounted/composite working boards with blank separators and severe OCR instability.

## OCR pathologies

The mounted sections reproduce the now-familiar failure mode: reading-order collapse, severe under-capture, semantic hallucination and mixed-script substitution. Clear machine intrusions include `p0010` (2024 World Economic Forum material), `p0012` (massive repetition cleanup), `p0027` (Arabic/Tamil mixed-script output), `p0030` (BING/“Vegetarian” modern intrusion), `p0064` (enumeration over-generation), `p0072-p0073` (2020/modern media material), `p0100` and `p0108` (modern 2020/2024 intrusions), `p0134` (“The answer is correct…” stock sentence), `p0148` (modern nicotine/Hong Kong prose), `p0154-p0155` (reversed/URL and Spanish generated text), and especially `p0182-p0207`, where ordinary manuscript sheets produce 2024, URLs, “The quick brown fox…”, formulae, modern legal/workplace prose and other semantic hallucinations. `p0224` also shows heavy repetition/over-generation.

Exact quotation from `high-noise` and `false-empty-recovery` pages requires direct scan verification. The printed runs at `p0156-p0161`, `p0163-p0169`, and `p0174-p0179` are the main retrieval-grade exceptions.

## Research-facing notes

The strongest research-facing result is packet-level rather than a single lexical hit: chunk 031 reconstructs a large **Burg/Kerspel/Walcheren research apparatus**, including source slips, maps, library-request forms, comparative burg bibliography, scholarly polemic and printed reception. It therefore supplies unusually clear evidence for Huizinga’s research workflow from source acquisition through excerpting and reorganization to debate/reception.

A second strong result is the `p0208-p0229` French-Revolution packet, anchored visually by “Max. Robespierre.” A third is the unusually dense Rockefeller stationery run, which should remain a documentary-context signal until sequence/body-text evidence establishes agency.

No secure direct Malinowski/anthropology/ethnology hit and no secure first-order play/game-theory hit was established. The `primitive` wording at `p0177` belongs explicitly to medieval Walcheren, while the `war = play` phrase at `p0200` is machine intrusion.

## Files

- `full_visual_audit_manifest_v1.tsv` — canonical 247-page retrieval classification.
- `empty_ocr_visual_review_v1.tsv` — all 41 baseline-empty pages, visually resolved.
- `composite_page_structure_v1.tsv` — documentary/layout segmentation and reading-order warnings.
- `core_theme_hits_v1.md` — research-facing hits and negative controls.
- `status.txt` — compact machine-readable status.

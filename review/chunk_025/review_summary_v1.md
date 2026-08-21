# chunk_025 review summary

`chunk_025:p0001-p0246` contains 246 scan pages. A full-page visual audit against the conservative PaddleOCR v3 baseline is complete. Raw OCR is preserved unchanged; this review is a separate retrieval-grade correction/triage layer, not a diplomatic transcription.

## Result

- 246/246 scan pages visually checked.
- 107 pages: `usable-with-noise`.
- 75 pages: `high-noise`.
- 36 pages: `short-text`.
- 21 pages: substantive `false-empty-recovery`.
- 7 pages: `blank/no-substantive`.
- Baseline empty OCR pages: 28 total. Visual review resolves them as 21 false negatives and 7 genuine blanks.

The 21 complete false negatives are: `p0028`, `p0033`, `p0049`, `p0050`, `p0057`, `p0093`, `p0096`, `p0100`, `p0115`, `p0123`, `p0127`, `p0151`, `p0152`, `p0179`, `p0188`, `p0196`, `p0198`, `p0205`, `p0228`, `p0235`, `p0236`. The seven genuine blank/no-substantive pages are `p0055`, `p0187`, `p0192`, `p0201`, `p0214`, `p0242`, `p0246`.

## Documentary structure

The chunk continues the Indian-medicine/Ayurveda/Suśruta working-note sequence from chunk 024. `p0001` is already in that stream. A major physical-layout issue appears at `p0002-p0027`: two distinct sheets are repeatedly photographed in the same scan frame. One carries Dutch biographical/educational prose; the other carries Indian-medicine/Sanskrit material. Some sheets are rotated. The baseline OCR often interleaves those physically separate streams, so apparent semantic jumps are frequently layout failures rather than authorial transitions.

From roughly `p0028-p0175`, the dominant sequence is loose working notes on Ayurveda/Indian medicine: constitution and humoral theory, disease classification, therapeutics, pregnancy/reproduction, diagnosis, hygiene, materia medica, macrocosm/microcosm, rasāyana/vājīkaraṇa, and Sanskrit/romanized excerpts. Useful scan-visible headings/anchors include `Diagnosis`, `Hydrotherapy`, `Macrocosmos-Microcosmos`, `Primitivisme`, `Rasayama Vajikara`, and numerous disease/therapy headings. `p0176-p0186` shifts into a schematic/index-like outline of the material, including system headings and alphabetical/topical lists.

From `p0188` onward, physical format becomes much less regular. Mounted-slip boards alternate with loose sheets, envelopes and larger notes. The first mounted run (`p0188-p0213`) mixes biographical/bibliographical material with continued Indian-medicine notes; `p0205-p0213` is especially dense and reading-order-sensitive. `p0215-p0231` returns mainly to loose notes. `p0232-p0245` is another extended mounted-slip-board run. `p0242` is a blank envelope, and `p0246` contains mounted blank sheets/cards.

## OCR pathologies

The main failure modes are severe under-capture, page-level mixing of two physical sheets, reading-order collapse on mounted boards, and hallucinated scripts. Particularly clear machine failures include the massive repeat run on `p0082`, extreme overexpansion on `p0083`, Arabic-script replacement on `p0158`, generated duplicate-table structure on `p0183`, a repeated block on `p0190`, Greek repetition on `p0208`, a long repeat run on `p0239`, and a large Cyrillic/Mongolian-like replacement block on `p0245`. These forms are not treated as source text.

The high-noise queue is explicit in `full_visual_audit_manifest_v1.tsv` and `status.txt`. Those pages are still useful for coarse retrieval when recognizable anchors survive, but they require scan-level checking before any verbatim quotation.

## Research-facing note

Two headings are potentially worth remembering for later conceptual work: `p0095` explicitly uses **Macrocosmos-Microcosmos**, and `p0125` has **Primitivisme**. In this chunk they occur inside the Indian-medicine working-note complex; they should not by themselves be promoted into claims about Huizinga's later anthropology, cultural theory, or Malinowski without further contextual evidence.

## Files

- `full_visual_audit_manifest_v1.tsv` - canonical 246-page retrieval classification.
- `empty_ocr_visual_review_v1.tsv` - all 28 baseline-empty pages, visually resolved.
- `composite_page_structure_v1.tsv` - physical multi-stream/mounted-board layout warnings.
- `status.txt` - compact machine-readable status.

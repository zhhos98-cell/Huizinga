# chunk_002 review layer

This directory fills the historical review gap for `chunk_002.pdf_by_PaddleOCR-VL-1.6.json` without overstating the state of the evidence.

## Current calibration level

The raw PaddleOCR JSON is preserved unchanged. A substantive second-pass OCR review has been completed at packet/theme level: coherent historical complexes, major OCR pathologies, high-value conceptual anchors, and negative controls have been identified. This is sufficient for corpus retrieval, thematic triage, and prioritizing later scan work.

It is **not** a retrieval-grade visual completion. Absolute `pXXXX` alignment of the raw OCR anchors has not yet been recovered reliably, so no page-class totals or page-level visual manifest are invented here.

## Scan situation

A scan source for `p0123-p0183` is confirmed in the File Library as `/Huizinga/chunk_002_123-183.pdf`. In the current review environment the PDF could not be read or materialized, so those 61 pages are **not claimed as visually audited**. Scan coverage outside that segment has not been confirmed in this pass.

## Substantive structure established from raw OCR

The raw OCR supports at least four major retrieval complexes:

1. Middelburg / Zeeland medieval, urban, legal and jurisdictional material, including `Zelandensia`-type anchors.
2. Medieval Italian material around Salimbene and Ezzelino da Romano.
3. A Florence communal/political/art-historical complex: popolo, guilds, Guelf/Ghibelline conflict, Ciompi, Albizzi/Medici and related civic/artistic material.
4. The analytically strongest complex: Abélard/Héloïse and twelfth-century intellectual history. This packet explicitly links disputation to combat/tournament imagery, preserves `élément ludique` / competition language, applies `primitive` to a twelfth-century intellectual or mental attitude, discusses the modern label `Renaissance` for the twelfth century, and contains the judgment that Abélard should not simply be treated as a precursor of the Renaissance but as `prégothique`.

The fourth complex is a first-order research lead because play/competition, periodization, and `primitive` occur inside one coherent medieval intellectual-history argument rather than as detached lexical coincidences.

## OCR pathology policy

The raw file also contains severe semantic hallucination and over-generation: repeated numerical strings, modern/synthetic English, mixed-script substitution, biomedical or contemporary vocabulary inside historical material, and reading-order collapse on composite pages. Generated English occurrences of `play` are excluded from the research hit set.

No raw-OCR match was established for `Malinowski`, `anthropolog*`, or `ethnolog*`. No raw-OCR Rockefeller Memorial hit was established either; because the scans are not visually available, this last point is only an OCR negative control and not a visual exclusion.

## Files

- `status.txt` — conservative machine-readable state.
- `review_summary_v1.md` — substantive review and adequacy assessment.
- `core_theme_hits_v1.md` — research-relevant hits and negative controls.
- `composite_page_structure_v1.tsv` — provisional packet map without invented page IDs.
- `ocr_anchor_index_v1.tsv` — raw-OCR anchor index using textual/source anchors rather than fabricated `pXXXX` assignments.
- `scan_availability_v1.tsv` — confirmed scan coverage/access state.

A page-level visual manifest and empty-OCR resolution table should be created only after reliable page alignment and scan access are restored.

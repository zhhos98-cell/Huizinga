# chunk_032 review

Current state: **existing OCR layer calibrated; visual audit pending scan availability**.

This directory deliberately separates the immutable raw PaddleOCR JSON from a conservative correction/retrieval layer. The chunk contains 235 OCR records. The present review does not claim diplomatic transcription or retrieval-grade visual completion because the scan PDF is not currently available.

## Files

- `page_class_index_v1.md` — canonical 235-page OCR-only class index and refined packet map.
- `empty_ocr_unresolved_v1.tsv` — 66 baseline-empty pages kept unresolved until scans arrive.
- `composite_page_structure_v1.tsv` — seven provisional documentary packets, refined after a second raw-OCR pass.
- `ocr_anchor_index_v1.tsv` — conservative high-value OCR anchors and rejected false hits.
- `core_theme_hits_v1.md` — research-facing results and negative controls.
- `review_summary_v1.md` — full narrative calibration summary.
- `status.txt` — compact machine-readable state.

## Strongest current results

1. `p0108-p0159`: a coherent French-Revolution research complex showing multi-source biographical/reference lookup, Robespierre/Lafayette/Dumouriez interpretation, and Stanhope/Pitt parliamentary cross-checking.
2. `p0219-p0235`, especially `p0233`: academic-relief material for prisoner/interned students; OCR explicitly names `J. HUIZINGA, Voorzitter, Leiden` and describes provision of study/scientific-work support.
3. `p0175`: earlier administrative/institutional occurrence of `J. HUIZINGA, Voorzitter, Leiden. L. VAN ITALLIE, Leiden.` Its relationship to the late relief packet remains unresolved pending scans.

## Hard limits

- 66 baseline-empty pages cannot be classified as blank versus false-negative without page images.
- 89 pages are OCR-pathological and require visual control before substantive use.
- No secure Malinowski, primitive/primitief, Rockefeller Memorial or play/game hit is established in the current OCR layer.

When scans arrive, the first visual priorities are the 66 empty pages, the A4 French-Revolution source-triangulation sequence, and the exact identity/document form of the A7 academic-relief committee.
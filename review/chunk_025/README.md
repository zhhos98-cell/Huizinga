# review/chunk_025

Review layer for `chunk_025:p0001-p0246` (246 scan pages). Raw PaddleOCR v3 remains unchanged.

**Full retrieval-grade visual/OCR audit: COMPLETE (246/246).**

Chunk 025 is dominated by Huizinga's Indian-medicine/Ayurveda/Suśruta working notes, but its physical scan structure matters. `p0002-p0027` repeatedly photographs two distinct manuscript sheets in the same frame, one Dutch biographical/educational and one Indian-medicine/Sanskrit. Later, especially from `p0188`, mounted-slip boards recur and make OCR reading order unstable.

Final page classes: **107 usable-with-noise; 75 high-noise; 36 short-text; 21 false-empty recoveries; 7 blank/no-substantive.**

Baseline empty OCR pages: 28. Visual result: **21 substantive false negatives** and **7 genuine blanks**. See `empty_ocr_visual_review_v1.tsv`.

Files:
- `full_visual_audit_manifest_v1.tsv` - canonical page-level retrieval classification
- `empty_ocr_visual_review_v1.tsv` - empty-OCR visual controls
- `composite_page_structure_v1.tsv` - scan-frame/mounted-slip structure and reading-order cautions
- `review_summary_v1.md` - documentary architecture, OCR pathology and research-facing notes
- `status.txt` - compact completion state

High-value conceptual anchors retained for later contextual checking include `p0095` (**Macrocosmos-Microcosmos**) and `p0125` (**Primitivisme**). They belong here to the Indian-medicine note complex and are not, on their own, evidence for later anthropological or cultural-theoretical positions.

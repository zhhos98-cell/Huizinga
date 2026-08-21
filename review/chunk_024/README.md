# review/chunk_024

Review layer for `chunk_024:p0001`–`p0085` (85 scan pages). Raw PaddleOCR v3 remains unchanged.

**Retrieval-grade visual/OCR audit: COMPLETE (85/85).** Final classes: **30 usable; 31 usable-with-noise; 18 high-noise; 1 false-empty OCR recovery; 1 short-text/title page; 4 blank/no-substantive pages.** The canonical page-level file is `full_visual_audit_manifest_v2.tsv`; detailed findings and the close-transcription queue are in `review_summary_v1.md`.

Current scan-grounded architecture:

- `p0001`: narrow handwritten label **`Excerpts Kern`**; complete OCR false negative.
- `p0002`: handwritten cover/title for **Mannen en Vrouwen van Beteekenis in onze Dagen: Hendrik Kern, door J. Huizinga**, Haarlem, H. D. Tjeenk Willink & Zoon, 1899; `p0003` is blank.
- `p0004–p0033`: printed `Hendrik Kern` extract/booklet. `p0004–p0012` duplicate `chunk_023:p0179–p0187`; `p0013–p0033` continue the publication beyond chunk 023. `p0034` is blank.
- `p0035`: early Indian-medicine note, opening with **`Review of the history of medicine, by Thomas A. Wise, London 1867`** and Dhanvantari/Ayurveda material.
- `p0036–p0047`: **composite scan frames**. Many frames photograph two physically distinct manuscript sheets side by side: a Kern/Indology/philology/bibliographical sheet, often inverted, and an Indian-medicine/Ayurveda/cosmology sheet, usually upright. Baseline OCR frequently merges the two documentary streams and collapses reading order. This second visual pass supersedes the first-pass description of this whole run as a single Kern bibliographical packet.
- `p0048`: single dense Kern/Indology/Buddhism note.
- `p0049–p0053`: anatomical/medical notes (`Anatomie des Menschen`, circulation, joints, vertebrae, articulation); `p0054` is blank.
- `p0055`: isolated legend/folklore note; `p0056` is blank.
- `p0057–p0062`: methodological Indian-medicine notes; `p0061–p0062` are low-contrast and severely under-captured.
- `p0063–p0085`: Suśruta/Ayurveda working notes. `p0063` visibly begins **`Inhoud van den Susruta`**; the run covers branches of medicine, surgery, instruments, materia medica, dhātu/doṣa, disease classification and dense Sanskrit/romanized material.

Baseline-empty pages are `p0001`, `p0003`, `p0034`, `p0054`, `p0056`. Visual review gives **1 false-empty** (`p0001`) and **4 genuine blanks** (`p0003`, `p0034`, `p0054`, `p0056`).

High-noise queue: `p0036`, `p0038`, `p0041`, `p0042`, `p0044`, `p0046`, `p0055`, `p0059`, `p0061`, `p0062`, `p0065`, `p0066`, `p0070`, `p0074`, `p0075`, `p0076`, `p0082`, `p0084`.

Machine-pathology controls verified against scans include: the generated `S1...` sequence on `p0075`, the Cyrillic block on `p0076`, the `7:1, 7:2, ...` numeric run on `p0082`, and the Vietnamese-like phrase on `p0084`; none is present in the manuscript scans.

Files:
- `full_visual_audit_manifest_v2.tsv` — canonical 85-page retrieval-grade classification and packet assignment
- `review_summary_v1.md` — detailed architecture, OCR pathology and high-noise queue
- `verified_corrections_v1.tsv` — scan-grounded corrections and false-machine-text controls
- `composite_page_structure_v1.tsv` — corrected structure for `p0035–p0048`
- `cross_chunk_overlap_v1.tsv` — duplicate printed-page mapping between chunks 023 and 024
- `status.txt` — closed review state
- `structural_scan_manifest_v1.tsv` and `full_visual_audit_manifest_v1.tsv` — retained as first-pass audit trail; their `p0035–p0048` packet assignment is superseded by the second visual pass

This chunk also corrects the previous boundary description of the printed Kern item: `chunk_023:p0187` is not the final surviving printed page; chunk 024 contains an overlapping rescan followed by a substantial continuation.

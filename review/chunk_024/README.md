# review/chunk_024

Review layer for `chunk_024:p0001`–`p0085` (85 scan pages). Raw PaddleOCR v3 remains unchanged.

Initial structural scan of all 85 pages is complete; retrieval-grade page-by-page OCR classification/close correction remains in progress.

Current scan-grounded architecture:

- `p0001`: narrow handwritten label, scan reads `Excerpts Kern`; baseline OCR is empty, so this is a false-empty recovery.
- `p0002`: handwritten cover/title for **Mannen en Vrouwen van Beteekenis in onze Dagen: Hendrik Kern, door J. Huizinga**, Haarlem, H. D. Tjeenk Willink & Zoon, 1899.
- `p0003`: blank inside cover/endpaper.
- `p0004–p0033`: printed `Hendrik Kern` extract/booklet. The first part is a cross-chunk overlap: `chunk_024:p0004–p0012` duplicates the same printed sequence already scanned at `chunk_023:p0179–p0187`; `chunk_024:p0013–p0033` continues the publication beyond chunk 023. `p0033` closes with a numbered list of Kern publications/reviews; `p0034` is a blank endpaper/cover.
- `p0035–p0048`: handwritten bibliographical/philological notes with strong Kern-related content, including publication/reference lists and notes on languages, inscriptions, the Indian Archipelago and related scholarship. Exact packet boundaries inside this run remain under close review.
- `p0049–p0053`: anatomical/medical notes (`Anatomie des Menschen`, circulation, joints, vertebrae, articulation); `p0054` is blank.
- `p0055`: isolated handwritten legend/folklore note; `p0056` is blank.
- `p0057–p0085`: Indian medicine / Ayurveda / Suśruta-oriented working notes. `p0063` explicitly begins `Inhoud van den Susruta`; subsequent pages contain surgical instruments, materia medica, humoral/dhātu material, disease classification and dense Sanskrit/romanized excerpts through `p0085`.

Baseline-empty pages are `p0001`, `p0003`, `p0034`, `p0054`, `p0056`. Visual review gives **1 false-empty** (`p0001`) and **4 genuine blank/no-substantive pages** (`p0003`, `p0034`, `p0054`, `p0056`).

Files:
- `verified_corrections_v1.tsv` — scan-grounded corrections/recoveries begun with labels, title material and empty-page controls
- `cross_chunk_overlap_v1.tsv` — duplicate printed-page mapping between chunks 023 and 024
- `status.txt` — current review state

This chunk materially revises the previous boundary description of the printed Kern item: `chunk_023:p0187` is not the final surviving printed page; chunk 024 contains an overlapping rescan followed by a substantial continuation.

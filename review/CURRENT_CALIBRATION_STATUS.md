# Current Huizinga calibration status

Updated: 2026-08-26

This file is a current roll-up. `review/PROGRESS.md` is a historical detailed log and is not assumed to reflect later chunks unless explicitly updated there.

## Corpus-level status

- `chunk_001`: **retrieval-grade visual audit COMPLETE**.
- `chunk_002`: **OCR calibration + absolute scan alignment restored; macro visual sweep COMPLETE; full page-level OCR usability manifest still pending**. All three contiguous scan segments `p0001-p0183` are now available and were rendered/inspected. Priority conceptual anchors are scan-verified at p0086 (`élément ludique` / competition-disputation), p0087 (`primitive` in the same medieval intellectual-history argument), and p0090 (Abélard not simply a Renaissance precursor but `prégothique`). See `review/chunk_002/status.txt`, `visual_anchor_alignment_v2.tsv`, and the resolved `alignment_blocker_v1.md`.
- `chunk_003`–`chunk_031`: **retrieval-grade visual review COMPLETE** at the repository's established calibration standard. `COMPLETE` here means retrieval-grade visual/OCR correction and triage, not diplomatic or word-perfect transcription; high-noise pages still require direct scan checking before exact quotation.
- `chunk_032`: **OCR-layer second-pass CALIBRATED; visual audit NOT COMPLETE** because the scan set is unavailable to the review layer. See `review/chunk_032/status.txt`.

## Current continuity statement

`001 ✅ visual | 002 🟢 scan-aligned / macro visual + priority anchors verified / page-grade manifest pending | 003–031 ✅ visual | 032 🟡 OCR-calibrated / visual pending`

The previous chunk-002 blocker was specifically scan access and absolute `pXXXX` alignment. That blocker is now resolved. The remaining 002 work is narrower: page-by-page OCR usability / false-empty grading and a few exact-leaf pinpointing tasks, not recovery of the scan sequence.

## chunk_002 corrected research priority

The strongest packet begins with the title card `Trois esprits prégothiques < Paris 1930 >` at p0049. Within it:

- p0086 (manuscript p.31) visibly begins `Cet élément ludique` and links the ludic element to competition/disputation;
- p0087 (ms p.32) visibly contains `primitive` in the continuation of that medieval intellectual-history argument;
- p0090 (ms p.35) visibly places Abélard not simply as a precursor of the Renaissance but `au contraire comme un prégothique`, with nearby language retaining the primitive/apparatus contrast.

This is now scan-verified evidence rather than an OCR-only lead. The immediate context remains medieval intellectual history and periodization; raw negative controls still show no secure `Malinowski`, `anthropolog*`, or `ethnolog*` context.

A direct pathology control is also secured: p0089 contains ordinary continuous French handwriting, while the rough OCR generated a catastrophic repeated-number/table-like continuation. Raw machine continuations therefore remain subordinate to scan evidence.

## Next closure priorities

1. Pinpoint the exact pXXXX leaves for the Haskins / *The Renaissance of the Twelfth Century* line and nearby Gilson line within the p0049-p0136 packet.
2. If exact parity with chunks 003-031 is required, build the full p0001-p0183 page-level OCR usability / false-empty manifest.
3. Close chunk 032 visually when its scans become available.

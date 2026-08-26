# Current Huizinga calibration status

Updated: 2026-08-26

This file is a current roll-up. `review/PROGRESS.md` is a historical detailed log and is not assumed to reflect later chunks unless explicitly updated there.

## Corpus-level status

- `chunk_001`: **retrieval-grade visual audit COMPLETE**.
- `chunk_002`: **substantive OCR-layer calibration COMPLETE; visual audit NOT COMPLETE**. The former missing-review gap is now filled with a conservative review layer under `review/chunk_002/`. Absolute `pXXXX` alignment is still pending. Known scan segments: `p0001-p0061` and `p0123-p0183`; current scan-pixel access is blocked in the review environment. See `review/chunk_002/status.txt` and `alignment_blocker_v1.md`.
- `chunk_003`–`chunk_031`: **retrieval-grade visual review COMPLETE** at the repository's established calibration standard. `COMPLETE` here means retrieval-grade visual/OCR correction and triage, not diplomatic or word-perfect transcription; high-noise pages still require direct scan checking before exact quotation.
- `chunk_032`: **OCR-layer second-pass CALIBRATED; visual audit NOT COMPLETE** because the scan set is unavailable to the review layer. See `review/chunk_032/status.txt`.

## Current continuity statement

`001 ✅ visual | 002 🟡 OCR-calibrated / visual pending | 003–031 ✅ visual | 032 🟡 OCR-calibrated / visual pending`

The previous statement that `chunk_002` was an unreviewed hole is no longer accurate. The remaining 002 gap is specifically **visual/page-alignment completion**, not absence of substantive review.

## chunk_002 research priority

The highest-value OCR-layer packet is the Abélard/Héloïse / twelfth-century intellectual-history complex. It brings together `élément ludique`, social competition, tournament/disputation imagery, `primitive` as an intellectual-historical descriptor, and explicit work on the period label `Renaissance`, including the characterization of Abélard as `prégothique` rather than simply a Renaissance precursor. Negative controls found no secure raw-OCR `Malinowski`, `anthropolog*`, or `ethnolog*` context. See `review/chunk_002/core_theme_hits_v1.md`.

## Next closure priorities

1. Restore ordered raw-record → absolute `pXXXX` alignment for chunk 002 without inferring page numbers from wrapped connector output.
2. Restore visual access to the known 002 scan segments and visually verify the high-priority conceptual anchors.
3. Locate the unconfirmed 002 scan ranges (`p0062-p0122` and material after `p0183`).
4. Resolve chunk 002 blank/false-empty and page-class status only from scans.
5. Close chunk 032 visually when its scans become available.

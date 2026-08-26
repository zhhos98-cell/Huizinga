# chunk_002 absolute page-alignment blocker — RESOLVED 2026-08-26

## Historical purpose

This note originally recorded why the substantive OCR anchors in `chunk_002` were indexed by raw-source UUIDs rather than by guessed `pXXXX` page IDs. That caution was correct while scan pixels and the middle scan segment were unavailable.

## Resolution

On 2026-08-26 all three contiguous 61-page scan segments became available in the review runtime:

- `chunk_002_1-61.pdf` -> `p0001-p0061`
- `chunk_002_62-122.pdf` -> `p0062-p0122`
- `chunk_002_123-183.pdf` -> `p0123-p0183`

All 183 pages were rendered for a macro visual sweep. Priority pages were re-rendered at higher resolution and directly compared with the rough PaddleOCR output. The raw OCR is organized in sequential four-image batches; the scan sequence supplies the missing absolute reference. Multiple independent visual/textual anchors confirm the alignment rather than relying on connector wrapper order alone.

## Independent alignment checks

- Raw batch `72bbc5ae-...` aligns to `p0001-p0004`; `p0002` is visibly a mounted Zeeland legal/bibliographical board.
- Raw batch `7d56ec88-...` aligns to `p0005-p0008`; `p0006` visibly carries the envelope label `Zelandensia`.
- Raw batch `eda81e7f-...` aligns to `p0009-p0012`; `p0011` is the title card `Salimbene 1914/15`.
- Raw batch `1ef7154e-...` aligns to `p0029-p0032`; `p0029` visibly treats Florence communal/factional history.
- Raw batch `9bcf2bc7-...` aligns to `p0049-p0052`; `p0049` is the title card `Trois esprits prégothiques < Paris 1930 >`.
- Raw batch `dce87a52-...` aligns to `p0085-p0088`; `p0086` (manuscript p.31) visibly begins `Cet élément ludique`, and `p0087` (ms p.32) contains `primitive` in the same intellectual-history argument.
- Raw batch `f1e3ac39-...` aligns to `p0089-p0092`; `p0090` (ms p.35) visibly contains the Abélard / Renaissance / `prégothique` boundary argument.

See `visual_anchor_alignment_v2.tsv` for the compact audit table.

## Remaining caution

Absolute page alignment is now restored for the scan set and the priority raw anchors. This does **not** make the rough OCR diplomatic transcription. Composite mounted boards, dense handwriting, and several machine-overgeneration records still require page-by-page correction before exact quotation. In particular, `p0089` demonstrates the failure mode clearly: the underlying manuscript is normal continuous French prose while the raw OCR produced a catastrophic repeated-number/table-like continuation.

## Current rule

Use canonical `pXXXX` for scan citation and retain raw UUIDs as secondary machine anchors. Do not overwrite the original OCR JSON. Corrections belong in the review layer, with direct scan verification for exact quotation or fine reading-order claims.

# Strict PDF re-proofreading v2

Started: 2026-08-27

## Evidence standard

A page counts as `STRICT_VERIFIED` only when all of the following have happened:

1. The original scan page has actually been opened and visually inspected.
2. The corresponding PaddleOCR-VL JSON page has been read and compared against the scan.
3. Substantive transcription/OCR errors found in that comparison have been recorded in the manual correction ledger and applied to the `.corrected.json` output.
4. The page receives an explicit v2 audit row recording the source PDF, result, and any action taken.
5. `no_change` is a substantive result: it may be recorded only after the same scan-versus-JSON comparison, never inferred from absence of a correction.

A chunk counts as `STRICT_COMPLETE` only when every page in its defined scope has an explicit v2 audit row and there are no gaps.

## Legacy material

The following do **not** constitute strict verification by themselves:

- `review/chunk_*/pdf_verification_log_v1.tsv` rows;
- a page range passed to `scripts/build_pdf_verification_log.py`;
- existence of `corrections/chunk_*_manual.json`;
- existence of `.corrected.json`;
- retrieval-grade visual/OCR review manifests;
- historical `COMPLETE` / visual-closure markers.

`build_pdf_verification_log.py` historically generated one row for every page in a supplied span without opening the PDF. Its v1 output is therefore retained only as a legacy span/audit manifest, not as proof of visual comparison.

## Re-proofreading rule

The v2 pass begins from zero. Earlier corrections remain useful hypotheses and audit history, but every page and every inherited correction must be re-checked against the original scan before receiving v2 credit.

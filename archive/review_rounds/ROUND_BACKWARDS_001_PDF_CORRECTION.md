# Huizinga PDF-to-JSON correction round, backwards batch 001

Direction: newest supplied PDF backwards.

Original PDFs checked:

- `chunk_071__p0001-0040.pdf`
- `chunk_070__p0161-0186.pdf`
- `chunk_070__p0081-0120.pdf`
- `chunk_070__p0041-0080.pdf`
- `chunk_070__p0001-0040.pdf`

Pages compared with the original scans: **186** (`chunk_071`: 40; `chunk_070`: 146).

This is a transcription-correction round, not a visual-classification-only pass. The raw OCR JSON remains immutable. PDF-verified edits are applied to new `.corrected.json` copies and recorded in machine-readable ledgers plus before/after audit TSVs.

Applied actions:

- `chunk_070`: 16 actions on 12 pages: 4 replacements, 1 dropped hallucinated block, 4 page clears followed where appropriate by 7 manual recoveries.
- `chunk_071`: 3 high-confidence title-page replacements (`Huizinga`, `W. L. v. HELTEN / 1893. Januar.`, `Etymologie.`).

Principal corrections include removal of a repeated-zero hallucination on `chunk_070:p0010`, removal of a spurious mathematical formula from the envelope at `p0032`, several recovered archival shelfmarks and envelope labels, and correction of the title-page names and heading in `chunk_071:p0002`.

Coverage logs:

- `review/chunk_070/pdf_verification_log_v1.tsv`
- `review/chunk_071/pdf_verification_log_v1.tsv`

Patch ledgers and before/after audits:

- `corrections/chunk_070_manual.json`
- `corrections/chunk_071_manual.json`
- `review/chunk_070/applied_patch_audit_v1.tsv`
- `review/chunk_071/applied_patch_audit_v1.tsv`

Known supply gap: `chunk_070:p0121-p0160` was not among the supplied PDFs and is not claimed as reviewed here.

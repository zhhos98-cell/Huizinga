# Backwards PDF correction batch 003

- Direction: newest supplied spans toward older spans.
- PDFs checked: 5.
- Pages checked against original PDFs: 183.
- Covered spans: `chunk_069:p0001-p0040`, `chunk_068:p0121-p0200`, `chunk_067:p0161-p0223`.
- Method: every page visually inspected from rendered original PDF; OCR anomaly candidates rechecked at higher resolution; only high/medium-confidence changes applied to JSON.
- Machine-readable page logs: `review/chunk_067/pdf_verification_log_v1.tsv`, `review/chunk_068/pdf_verification_log_v1.tsv`, and `review/chunk_069/pdf_verification_log_v1.tsv`.
- Correction ledgers: `corrections/chunk_067_manual.json`, `corrections/chunk_068_manual.json`, and `corrections/chunk_069_manual.json`.
- Applied-patch audits: `review/chunk_067/applied_patch_audit_v1.tsv`, `review/chunk_068/applied_patch_audit_v1.tsv`, and `review/chunk_069/applied_patch_audit_v1.tsv`.
- Substantive corrections in this batch: 16 actions across 12 pages, including deletion of fabricated HTML tables, repeated-zero/repeated-letter runs, unrelated Chinese/English headings, and replacement/recovery of legible envelope labels and shelfmarks.
- Validation: for every affected chunk, the page set changed between raw and corrected JSON exactly equals the page set in its complete correction ledger.

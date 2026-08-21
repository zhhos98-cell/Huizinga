# review/chunk_022

Retrieval-grade OCR/page audit and correction layer for `chunk_022:p0001`–`p0250`.

Source scans were checked in seven contiguous blocks: 1–40, 41–80, 81–120, 121–160, 161–200, 201–240, 241–250.

Page-image inspection is used only for **OCR quality control, layout recovery, title/date verification, and false-empty recovery**. It is not treated as a separate image-history or visual-culture research strand. Raw PaddleOCR text is preserved unchanged; verified corrections are recorded in the review layer rather than silently rewriting the baseline.

The chunk contains several distinct documentary packets rather than one continuous course manuscript: a dated 1937–1938 Restoration teaching sequence; an inserted Historical Association pamphlet comparing Vienna 1814–15 and Paris 1919; a `Duitsche Rijk 1648–1688` packet used in 1924/25 and `1934/35 ten deele`; and a separate `Europ. pol. gesch. rondom 1700` packet marked `1926/27` and `1934/35`, ending with a 25-meeting 1934–1935 teaching sequence.

Files:
- `full_visual_audit_manifest_v1.tsv` — page-level status against clean PaddleOCR v3
- `empty_ocr_visual_review.jsonl` — checks of all baseline-empty pages
- `verified_corrections_v1.tsv` — scan-verified corrections to high-value OCR readings
- `core_theme_hits_v1.md` — high-priority documentary/research hits surfaced during review
- `review_summary_v1.md` — audit summary and close-transcription/collation queue
- `status.txt` — completion marker

Raw OCR is preserved unchanged. The review layer records retrieval/quality judgments and source-grounded corrections.

# PaddleOCR corpus

Canonical location for the Leiden / Huizinga PaddleOCR-VL corpus after the 2026-09-05 repository reorganization.

## Layers

- `raw/` — original `chunk_*.pdf_by_PaddleOCR-VL-1.6.json` outputs. Treat as immutable source evidence.
- `corrected/` — corrected derivatives. A corrected file is authoritative only for corrections recorded in `../../../corrections/`; it does not erase the raw source.
- `aggregates/` — merged historical convenience JSONs (`001-059`, `001-071`, etc.). Use for broad navigation only. For citation, correction, or disputed wording, return to the relevant chunk and its review/correction trail.

The canonical processing relation is:

`raw chunk -> corrections ledger -> corrected derivative -> review/audit`

`../../../scripts/apply_pdf_corrections.py` reads from `raw/` and writes to `corrected/`. Chunk-specific audits remain under `../../../review/chunk_*/`.

## Split chunks

Historical split source files such as `chunk_004_1-160`, `chunk_004_161-236`, `chunk_016_1-150`, and `chunk_016_151-276` remain in `raw/` under their original filenames. Their existence is provenance, not an instruction to regenerate a unified file.

## Search discipline

For article work, prefer a bounded `research/article_*` control when one exists. Open this corpus directly only when a source passage, OCR state, or page-level locator needs checking. Do not use the aggregate files as a reason to rerun full-corpus thematic sweeps.

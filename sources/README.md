# Sources

This directory is the canonical entry point for source corpora. Source files are organized by provenance and processing layer so article work can open the relevant corpus directly instead of scanning the repository root.

## Canonical source families

### `ocr/paddle/`

Leiden / Huizinga OCR corpus produced by PaddleOCR-VL. See `ocr/paddle/README.md` before using it.

- `ocr/paddle/raw/` — immutable raw OCR outputs. Original blob contents are preserved from the former repository-root layout.
- `ocr/paddle/corrected/` — authorized corrected OCR derivatives produced from correction ledgers.
- `ocr/paddle/aggregates/` — historical merged / convenience corpora. These are derived navigation objects, not a higher evidentiary level than the underlying chunks.

Correction provenance remains in `../corrections/`; page-level review and current calibration remain in `../review/`.

### `dbnl/`

Mirrored DBNL material, including the nine-volume *Verzamelde Werken* TEI XML corpus under `dbnl/verzamelde_werken/`. Article-facing traversal reports and integration decisions live in `../research/`, not beside the source XML.

## Retrieval rule

Start from the smallest controlled layer that can answer the question:

1. article/control note in `research/` when the issue has already been adjudicated;
2. chunk-level review material in `review/chunk_*` when a specific manuscript/OCR span is needed;
3. corrected OCR when an authorized correction exists;
4. raw OCR or DBNL XML only when the source itself must be rechecked.

Do not rescan all source families merely to rediscover a point already closed in an article-facing control note. Raw source movement in the 2026-09-05 repository reorganization changed paths only; source blob contents were not regenerated.

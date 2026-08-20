# Huizinga

Canonical Leiden corpus and discovery layer for the Huizinga–Malinowski project.

## Current corpus

- `huizinga_leiden_paddleocr_clean_001-071_complete_v3.json`
- chunks 001–071 complete
- **15,139 pages** total
- **12,654 non-empty OCR pages**
- **2,485 empty OCR pages**

## Current scan checkpoint — 20 August 2026

A full sequential pass of the consolidated Leiden OCR has been completed **without early exit**.

Current review queue after false-positive cleaning:

- **A: 8 pages** — immediate image/material review
- **B: 15 pages** — strong contextual or archival-unit review
- **C: 318 pages** — machine recall/context layer
- **341 sparse marked pages** total

The scan keeps exact identities separate from fuzzy OCR candidates and explicitly flags possible stationery reuse, verso material, or OCR-layer mixing.

### Entry points

- [`FULL_CORPUS_SCAN_CHECKPOINT_2026-08-20.md`](analysis/full_corpus_scan_2026-08-20/FULL_CORPUS_SCAN_CHECKPOINT_2026-08-20.md) — governing scan state and research consequences
- [`priority_review_v1.md`](analysis/full_corpus_scan_2026-08-20/priority_review_v1.md) — A/B human-review queue
- [`chunk_scan_summary_v1.csv`](analysis/full_corpus_scan_2026-08-20/chunk_scan_summary_v1.csv) — full 001–071 coverage summary
- `page_markers_v1_001-035.csv`, `page_markers_v1_036-055.csv`, `page_markers_v1_056-071.csv` — sparse page-marker index, 341 rows total
- [`scan_manifest_v1.json`](analysis/full_corpus_scan_2026-08-20/scan_manifest_v1.json) — reproducibility metadata and input SHA-256
- [`scan_full_corpus_markers.py`](analysis/full_corpus_scan_2026-08-20/scan_full_corpus_markers.py) — reproducible scanner

## Current high-value findings

The scan does **not** yet text-layer-confirm the 17 July 1931 Huizinga memorandum + Nieuwenhuis annex, nor the missing 1932 Outhwaite/Leiden Survey reports. Their absence from OCR retrieval must not be treated as archival absence because 2,485 pages have empty OCR and some material is visually complex.

High-priority image-review targets include:

- `chunk_027:p0046` — Rockefeller Memorial/trustee text plus **23 Juni 1931**, but mixed with unrelated note material;
- `chunk_037:p0157` — `FOR THE SOCIAL SCIENCES IN HOLLAND`;
- `chunk_067:p0140` — `FOR THE SOCIAL SCIENCES IN HOLLAND — DR. J. HUIZINGA`;
- `HUI-071-2-31-000` (`chunk_068:p0052–0064`) — a substantive working dossier around *Klank die wegsterft*, including Hornbostel, Van Erp, Westenenk, the Koloniaal Instituut, and an institutional/publicity chain tied to Huizinga's *De Gids* article.

Rockefeller stationery is present on many OCR pages. It is **not automatically evidence of the 1931 Leiden dossier**; possible stationery reuse / verso / OCR-layer mixing is marked explicitly.

## Project topology

This repository is the canonical primary-corpus and discovery layer.

The current article-control, argument, and pre-existing source-control layer remains in:

`zhhos98-cell/Edward_Griffith/research_notes/huizinga_malinowski/`

until that material is migrated or cross-referenced here. New corpus findings should not alter the V6 body unless they pass the existing body-entry threshold recorded in the scan checkpoint.

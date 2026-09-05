# Huizinga

The repository now separates **active article work**, **canonical source layers**, **current review authority**, and **frozen workflow provenance**.

Two project states remain distinct:

- **corpus retrieval / calibration: CLOSED — 2026-08-30**;
- **article writing: ACTIVE — current 1926–1933 Huizinga–Malinowski draft**.

## Read first

1. `CURRENT_HANDOFF.md`
2. `writing/README.md`
3. `writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`
4. `research/README.md`
5. `sources/README.md` only when source-level rechecking is needed

## Current article

Canonical working draft:

`writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`

The current four-part architecture is exchange/Kula → travel/comparative method → institutions/human sciences → 1933 hinge. `Primitive` remains an analytic pressure test, not the topic of every section. See `research/article_structure_recomposition_exchange_travel_institution_1933_2026-09-05.md` and the reusable Kula chain in `research/article_kula_longitudinal_control_2026-09-05.md`.

Drafts 01–03 and superseded scene / temporal-gate files are writing history. See `writing/README.md`.

## Repository map

### Active / article-facing

- `writing/` — canonical prose and live architecture notes.
- `research/` — bounded article controls and closed provenance branches. Use its README before opening new research.

### Sources

- `sources/dbnl/` — DBNL mirrors, including *Verzamelde Werken* TEI XML.
- `sources/ocr/paddle/raw/` — immutable PaddleOCR chunk outputs formerly stored at repository root.
- `sources/ocr/paddle/corrected/` — authorized corrected OCR derivatives.
- `sources/ocr/paddle/aggregates/` — historical merged convenience corpora.
- `corrections/` — manual correction ledgers and correction provenance.

See `sources/README.md` and `sources/ocr/paddle/README.md`.

### Current review authority

For the closed corpus state use:

- `FINAL_CLOSURE_2026-08-30.md`
- `CLOSURE_STATE_2026-08-30.json`
- `review/CURRENT_CALIBRATION_STATUS.md`
- `review/CORE_THEME_HITS.md`

Specific page/chunk evidence remains under `review/chunk_*/`.

### Frozen provenance

- `archive/review_rounds/` — old sequential `ROUND_*` and `PROGRESS.md` logs. They document how review proceeded but do not define current status.
- `archive/` — other retired workflow documentation, superseded writing, and noncanonical probes.

Do not restart from a frozen round note because it contains an old local TODO.

## Retrieval discipline

Use the smallest layer that already controls the question:

`article/control note -> chunk review -> corrected source -> raw source`.

A full-corpus scan is a last resort, not the normal way to find an article fact. The 2026-09-05 reorganization moved raw OCR and frozen review files by preserving their Git blob contents; it did not regenerate the evidence.

The three-Malinowski-book physical-copy provenance hunt remains dormant. Reopen only for direct copy-level Huizinga evidence.

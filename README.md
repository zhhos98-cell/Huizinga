# Huizinga

The repository now has two separate states:

- **corpus retrieval / calibration: CLOSED — 2026-08-30**;
- **article writing: ACTIVE — current 1921–1933 Huizinga–Malinowski draft**.

## Read first

1. `CURRENT_HANDOFF.md`
2. `writing/README.md`
3. `writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`
4. `research/README.md`

For the closed corpus state, use:

- `FINAL_CLOSURE_2026-08-30.md`
- `CLOSURE_STATE_2026-08-30.json`
- `review/CURRENT_CALIBRATION_STATUS.md`
- `review/CORE_THEME_HITS.md`

Older round notes, chunk-local priority fields and pre-closure status language are research provenance. They do not reopen the retrieval programme.

## Current article

Canonical working draft:

`writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`

Current focus: Huizinga and Malinowski on the *primitive*, 1921–1933. The article starts from their direct exchange and uses earlier material only when the exchange requires it. Huizinga’s and Malinowski’s own wording should carry the prose whenever possible.

Drafts 01–03 and the old scene / temporal-gate files are superseded writing history. See `writing/README.md`.

## Research directory

`research/` contains bounded writing deltas and closed provenance branches. See `research/README.md` before opening a new search.

The three-Malinowski-book provenance hunt is dormant. Reopen it only for direct copy-level Huizinga evidence.

## Frozen data layout

The chunk corpus remains deliberately flat because correction and audit tooling records those paths directly. Do not reorganize the chunk JSONs for directory aesthetics.

- `chunk_*.pdf_by_PaddleOCR-VL-1.6.json` — raw OCR source layer; immutable evidence output.
- `*.corrected.json` — authorized corrected derivatives.
- `corrections/` — manual correction ledgers and patch provenance.
- `review/` — page-level review signals, applied-patch audits and PDF-verification logs.
- `scripts/` — frozen reproducibility / audit utilities.
- `archive/` — retired workflow documentation and noncanonical probes.

Interpret the corpus as `raw -> correction ledger -> corrected derivative -> review/audit`. The closure files control whether further retrieval or correction work is warranted.
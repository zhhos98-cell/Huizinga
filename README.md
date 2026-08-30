# Huizinga

Current repository state: **CLOSED AT RETRIEVAL / RESEARCH-CALIBRATION GRADE — 2026-08-30**.

Canonical state files:

- `FINAL_CLOSURE_2026-08-30.md`
- `CLOSURE_STATE_2026-08-30.json`
- `CURRENT_HANDOFF.md`

The remaining unavailable source-image spans and Strict Reproofread V2 are bounded dormant verification/editorial debt, not an active research queue. Do not restart from older `PROGRESS`, round, or chunk-local `priority` language when it conflicts with the canonical closure files.

## Frozen data layout

The chunk corpus remains deliberately flat because correction and audit tooling records those paths directly. Do not reorganize the chunk JSONs merely for directory aesthetics.

- `chunk_*.pdf_by_PaddleOCR-VL-1.6.json` — raw OCR source layer; treat as immutable evidence output.
- `*.corrected.json` — corrected derivatives where PDF/source verification produced an authorized correction layer. These do not replace or mutate the raw files.
- `corrections/` — manual correction ledgers and patch provenance.
- `review/` — page-level review signals, applied-patch audits and PDF-verification logs.
- `scripts/` — retained reproducibility/audit utilities. They are frozen tooling, not a live research queue.
- `archive/` — noncanonical probes and retired workflow documentation, including the preserved Strict V2 source-probe material.

Interpret the repository as `raw -> correction ledger -> corrected derivative -> review/audit`, with the closure files controlling whether further work is warranted.

The frozen `main` branch no longer carries active write-capable correction workflows. The retired backwards-PDF correction workflow is documented under `archive/workflows/README.md`; its generated corrected JSON, correction ledgers and verification logs remain preserved in their canonical locations.

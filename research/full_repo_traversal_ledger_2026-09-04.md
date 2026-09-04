# Full repository traversal ledger — 2026-09-04

Purpose: verify the current article against the whole controlled Huizinga repository rather than against thematic hits or prior evidence maps alone. This ledger distinguishes inventory from actual reading and records technical limits explicitly.

## Status vocabulary

- `READ_FULL` — the complete UTF-8 file content has been retrieved and read in this traversal.
- `PARSED_FULL` — the complete structured/text derivative has been retrieved and its entries inspected in this traversal.
- `OVERSIZE_BLOB_REGISTERED` — exact repo path, SHA and size are registered, but the connector cannot return the complete blob because of size; this does **not** count as full reading.
- `BINARY_REGISTERED` — binary object is present and inventoried; textual/visual derivatives must be used for content control.
- `DERIVATIVE_PENDING` — raw/binary source is registered but its available review/correction derivatives have not all yet been reread.
- `DERIVATIVE_READ` — the source itself is not directly readable here, but its controlled derivative file(s) have been fully read.
- `NOT_YET_READ` — file is inventoried but has not yet been read in this traversal.

## Corpus divisions

1. Root archival OCR corpus: `chunk_001`–`chunk_071` raw/corrected PaddleOCR JSON plus merged clean corpora.
2. `corrections/`: manual/PDF-verified correction files.
3. `review/`: page-level visual-audit, manifest, summary, correction and status files for chunks 001–071, plus round-level and stationery controls.
4. `research/`: article controls, historiography, provenance and other bounded research deltas.
5. `writing/`: canonical Draft 04, reading companion, architecture/evidence-map files.
6. `archive/`: prior writing/calibration and source-probe material.
7. `scripts/`: correction/log generation scripts.
8. Huizinga published/collected works: exact local carrier still to be verified. Targeted DBNL/*Verzamelde Werken* references do not count as a corpus sweep.

## Root inventory status

The root tree has been recursively inventoried. It contains raw OCR JSON for chunks 001–071, corrected JSON for selected chunks, three merged OCR corpora, and the directories `archive/`, `corrections/`, `research/`, `review/`, `scripts/`, and `writing/`.

### Raw archival OCR

- `chunk_001`–`chunk_071`: `OVERSIZE_BLOB_REGISTERED / DERIVATIVE_PENDING` as a corpus. Exact individual paths, SHAs and sizes are present in the root Git tree. Individual blobs range from roughly 0.6MB to 2.8MB and are not reliably returned in full by the connector.
- Split roots include chunk 004 and chunk 016.
- Corrected root JSONs exist for chunk 002 and chunks 067–071.
- `huizinga_leiden_paddleocr_clean_001-059_skip016.json`: `OVERSIZE_BLOB_REGISTERED` (~17.7MB).
- `huizinga_leiden_paddleocr_clean_001-071_complete_v3.json`: `OVERSIZE_BLOB_REGISTERED` (~19.25MB).
- `huizinga_leiden_paddleocr_clean_001-071_missing060.json`: `OVERSIZE_BLOB_REGISTERED` (~20.4MB).

Technical rule: no claim that the raw OCR corpus has been fully read will be made unless a complete textual carrier is actually traversed. The present route is therefore raw-blob registration plus exhaustive rereading of every available controlled review/correction derivative.

## Directory-tree inventory

- `archive/`: complete recursive tree inventoried. File contents not all reread yet.
- `corrections/`: 8 files inventoried; **8/8 read in full**.
- `research/`: complete recursive tree inventoried; `research/README.md` and this ledger read; remaining files pending.
- `review/`: complete recursive tree inventoried, including chunk directories 001–071 and all round/protocol files. Individual-file reread pending except where later recorded.
- `scripts/`: 2 files inventoried; **2/2 read in full**.
- `writing/`: 7 files inventoried; pending full reread as a set.

## Files fully read so far in this traversal

### `corrections/` — COMPLETE 8/8

- `corrections/chunk_002_manual.json` — `READ_FULL`.
- `corrections/chunk_067_manual.json` — `READ_FULL`.
- `corrections/chunk_067_manual_round2a.json` — `READ_FULL`.
- `corrections/chunk_067_manual_round2b.json` — `READ_FULL`.
- `corrections/chunk_068_manual.json` — `READ_FULL`.
- `corrections/chunk_069_manual.json` — `READ_FULL`.
- `corrections/chunk_070_manual.json` — `READ_FULL`.
- `corrections/chunk_071_manual.json` — `READ_FULL`.

### `scripts/` — COMPLETE 2/2

- `scripts/apply_pdf_corrections.py` — `READ_FULL`. It applies page/block correction ledgers, rewrites corrected JSON, and emits an auditable patch table.
- `scripts/build_pdf_verification_log.py` — `READ_FULL`. Critical limitation: its `pdf_verification_log_v1.tsv` is explicitly a **legacy span manifest, not visual verification**. Strict re-proofreading is tracked separately in `review/STRICT_REPROOFREAD_V2_STATUS.tsv` and requires page-by-page visual inspection.

### Other

- `research/README.md` — `READ_FULL`.
- `research/full_repo_traversal_ledger_2026-09-04.md` — working traversal record.

## Already visible article-relevant implications from the correction layer

These are observations to test against the full corpus, not yet instructions to patch Draft 04:

- Chunk 067 corrections preserve the exact 1933 sequence in which Malinowski’s Kula supplies an ethnological example, Mauss’s potlatch is explicitly called play, and the text moves onward to economic history. This supports a concept-history reconstruction only if `primitive` remains the object whose explanatory work is being redistributed; it does not warrant a parallel autonomous `play` thesis.
- Chunk 067 contains `primitieve roulette`, confirming that the lexical family still survives inside the 1933 address. This is counterevidence against any narrative of lexical disappearance.
- Chunk 067 round2b restores Huizinga’s full *Vœu du Faisan* comparison: a chain of Burgundian court banquets passed the turn by a wreath, rose from lower to higher rank, and culminated in Philip the Good surpassing the others in competitive, reciprocal display. This can do more argumentative work than the present one-line “not so very far from a potlatch” summary because it shows exactly which relation Huizinga carried across the comparison.
- Chunk 002 corrected French material emphasizes transformation/adaptation/reuse of classical tradition and social forms. Its article function, if any, must be demonstrated rather than appended as a thematic parallel.
- Chunks 068–071 corrections are chiefly OCR/source-control repairs. Chunks 069–070 recover labels such as `Max Weber`, `Menhirs / Grottes / Mégalithes`, `Angst en literatuur`, and `Sociologische Ver...`; these are currently directory/context signals only, not article evidence.

## Article-function audit to be performed after traversal

Every current factual block in Draft 04 will be assigned one of these functions:

- `CORE_PRIMITIVE_ARGUMENT` — changes what `primitive` can classify, imply, or authorize.
- `PAIR_CAUSAL_JUNCTION` — documents a transfer by which a `primitive` problem moves between the two men/textual systems.
- `HUZINGA_INTERNAL_CONTROL` — shows Huizinga’s independent conceptual/source practice necessary to interpret that transfer.
- `MALINOWSKI_INTERNAL_CONTROL` — shows what Malinowski’s anthropological usage actually does.
- `HISTORIOGRAPHICAL_INTERVENTION` — changes an existing scholarly proposition.
- `COUNTEREVIDENCE` — prevents teleology or overclaim.
- `CONTEXT_ONLY` — needed for chronology/background but does not itself advance the argument.
- `PARALLEL_ONLY` — interesting material currently sitting beside the argument without doing work; candidate for deletion, relocation, or reconnection.

No Draft 04 patch should be made from this audit until the relevant source files have been actually traversed and the function is explicit.

## Next traversal batch

1. Traverse every file under `review/chunk_001` onward, recording exact completion by chunk; do not substitute `CORE_THEME_HITS.md` or `PROGRESS.md` for the underlying derivative files.
2. Read review-level protocol/status files, especially strict-v2 controls, separately from legacy manifests.
3. Traverse every `research/`, `writing/`, and `archive/` text file.
4. Resolve the carrier and extent of Huizinga’s collected works; if the repository only stores locators rather than the full corpus, record that and begin a separate volume-by-volume published-work traversal.

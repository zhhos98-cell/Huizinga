# Article full-corpus traversal ledger — 2026-09-04

Purpose: audit the current Huizinga–Malinowski article against the actual corpus, not against keyword hits or existing evidence summaries. This is a bounded article-QA exception to the otherwise closed generic retrieval programme.

## Status vocabulary

- `ENUMERATED` — path, type, size/SHA or Library file id confirmed.
- `READ_FULL` — complete text actually returned and inspected.
- `READ_PARTIAL` — file opened but connector response was truncated; must not be treated as fully read.
- `DERIVATIVE_COVERAGE` — raw oversized file cannot be returned directly; its page-level review/correction derivatives must be traversed instead.
- `IMAGE_SOURCE_REGISTERED` — scan/PDF original confirmed and available for page-level verification.
- `PENDING` — not yet read in this pass.

## Corpus A — GitHub raw Huizinga Leiden OCR

Root tree enumerated on 2026-09-04.

- `chunk_001...chunk_071` raw PaddleOCR JSON files: `ENUMERATED`.
- Split raw files such as chunk 004 and chunk 016: `ENUMERATED`.
- Corrected root JSON variants for chunks 002 and 067–071: `ENUMERATED`.
- `huizinga_leiden_paddleocr_clean_001-071_complete_v3.json` (19.2 MB): `ENUMERATED / DERIVATIVE_COVERAGE`; connector cannot return this oversized blob directly.
- Earlier merged clean variants: `ENUMERATED / DERIVATIVE_COVERAGE`.

Rule: no claim of “raw corpus fully read” will be made merely from metadata. Coverage must be established through the complete page-level review/correction layer and, where argumentatively important, checked against Library scan PDFs.

## Corpus B — GitHub corrections

Directory contains eight manual-correction JSON files.

- `corrections/chunk_002_manual.json`: `READ_FULL`.
- `corrections/chunk_067_manual.json`: `READ_PARTIAL` (connector output truncated; contains high-value 1933 Kula/potlatch/play corrections but still requires continuation/derivative control).
- `corrections/chunk_067_manual_round2a.json`: `READ_FULL`.
- `corrections/chunk_067_manual_round2b.json`: `PENDING`.
- `corrections/chunk_068_manual.json`: `PENDING`.
- `corrections/chunk_069_manual.json`: `PENDING`.
- `corrections/chunk_070_manual.json`: `PENDING`.
- `corrections/chunk_071_manual.json`: `PENDING`.

Early article-relevant recovery from the correction layer: Huizinga's corrected 1933 text explicitly routes Kula through `mildheid, vriendschap, vertrouwen, eer, hoogmoed en avontuur`, credit, gift, prestige and trust before moving to potlatch/Mauss and modern economic history. This material must be assessed for argumentative function, not merely appended as another comparison.

## Corpus C — GitHub review layer

`review/` tree enumerated recursively.

- `review/chunk_001` through `review/chunk_071`: all directories confirmed present.
- Round summaries, backward-correction logs, protocol/status files, `CORE_THEME_HITS.md`, `PROGRESS.md`, calibration/status files: enumerated.
- `review/PROGRESS.md`: `READ_PARTIAL` in this pass; it confirms the audit architecture is page-complete/retrieval-grade for the chunks it describes, but it does not substitute for re-reading each derivative file for article QA.
- Example `review/chunk_001` tree confirmed: `empty_ocr_visual_review.jsonl`, `full_visual_audit_manifest_v1.tsv`, `review_summary_v1.md`.

Required next action: traverse every file in every `review/chunk_###` directory, not only `CORE_THEME_HITS.md` or summaries.

## Corpus D — GitHub research / writing / archive / scripts

Trees recursively enumerated.

- `research/`: enumerated; article controls and provenance deltas present.
- `writing/`: seven files enumerated. Canonical draft remains `writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`.
- `archive/`: recursively enumerated; includes four source-probe JPGs plus archived Draft 01–03 and calibration/temporal-gate files.
- `scripts/`: two scripts enumerated.

Canonical Draft 04 current blob at start of this traversal: `176cc10280b0b906a2d2062fafd0bc460dd04876`. Current draft opened in this pass; response was truncated, so paragraph-function audit is in progress rather than complete.

## Corpus E — ChatGPT Library `/Huizinga`

Important correction to earlier scope: the user’s “Huizinga corpus in the library” is not reducible to the GitHub repo.

- Library folder `/Huizinga` confirmed.
- It contains original chunk scan PDFs in page blocks (e.g. chunk 048–053 listings directly confirmed): `IMAGE_SOURCE_REGISTERED`.
- The folder is large and paginated; collected/complete-work volumes have not yet been cleanly isolated from the archival chunk PDFs in this pass.
- Library content searches for `Verzamelde Werken` initially produced unrelated or secondary Huizinga material; no file will be identified as a collected-works volume by filename guess alone.

Required next action: finish Library metadata traversal, isolate the actual *Verzamelde Werken* / complete-works files, then traverse those volumes systematically.

## Article argument-function audit

Every retained evidence unit in Draft 04 will be assigned one function:

- `PREMISE`
- `MECHANISM`
- `COUNTEREVIDENCE`
- `CAUSAL / CHRONOLOGICAL CONSEQUENCE`
- `JURISDICTIONAL CONSEQUENCE`
- `SECOND-ORDER CONTROL`
- `MERELY PARALLEL`

`MERELY PARALLEL` material is not automatically deleted. It must either be connected to a premise/mechanism/consequence by source-supported historical action, moved to a note, or removed if it does no work.

Core QA question: not “is this material interesting?” but “what inference in the article fails if this material is removed?”

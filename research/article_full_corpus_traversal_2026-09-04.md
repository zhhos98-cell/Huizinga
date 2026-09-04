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

Directory contains eight manual-correction JSON files. This layer is now closed for the present pass.

- `corrections/chunk_002_manual.json`: `READ_FULL`.
- `corrections/chunk_067_manual.json`: `READ_FULL` (read in three explicit line ranges after the initial connector truncation).
- `corrections/chunk_067_manual_round2a.json`: `READ_FULL`.
- `corrections/chunk_067_manual_round2b.json`: `READ_FULL`.
- `corrections/chunk_068_manual.json`: `READ_FULL`.
- `corrections/chunk_069_manual.json`: `READ_FULL`.
- `corrections/chunk_070_manual.json`: `READ_FULL`.
- `corrections/chunk_071_manual.json`: `READ_FULL`.

### Argument-changing result from chunk 067

The corrected 1933 text does more than place Kula, potlatch, Burgundy and economic history side by side.

1. Huizinga specifies Kula through `mildheid, vriendschap, vertrouwen, eer, hoogmoed en avontuur`, and calls it a `spel van mildheid, vertrouwen en gemeenschap`; he also describes it as a credit system despite its apparently anti-economic character.
2. Potlatch is then specified through ceremonial giving, honour/status, delayed reciprocal obligation, generosity and trust.
3. Most importantly, Huizinga explicitly anticipates that adding the 1454 *Vœu du Faisan* may look forced. He says he adds it **not for its general play-character**, but as a specific case of `wedijverend, wederkeerig weeldevertoon en spilziek onthaal`.
4. He then reconstructs the Burgundian historical sequence: a series of court banquets -> turn-taking -> passing a wreath -> movement from lower to higher -> escalating splendour -> Philip the Good finally outdoing the others.
5. Only after specifying that mechanism does he say the case is “not so very far from a potlatch.”

Article consequence: the present coda risks presenting `Kula -> potlatch -> Burgundy` as a stack of parallels. The source itself instead supplies a narrower historical operation:

`relation isolated in ethnography -> same relation specified in a historical sequence -> analogy narrowed by mechanism`.

This is a candidate for later surgical revision of Draft 04 after corpus traversal, not for immediate free-standing expansion.

The remaining 068–071 corrections mainly remove OCR hallucinations and restore labels/shelfmarks. They did not produce another article-level mechanism in this pass.

## Corpus C — GitHub review layer

`review/` tree enumerated recursively.

- `review/chunk_001` through `review/chunk_071`: all directories confirmed present.
- Round summaries, backward-correction logs, protocol/status files, `CORE_THEME_HITS.md`, `PROGRESS.md`, calibration/status files: enumerated.
- `review/PROGRESS.md`: `READ_PARTIAL` in this pass; it confirms the audit architecture is page-complete/retrieval-grade for the chunks it describes, but it does not substitute for re-reading each derivative file for article QA.

### Chunk-by-chunk re-traversal

#### `review/chunk_001` — CLOSED

Directory contains three files; all three have now been read completely in this pass.

- `empty_ocr_visual_review.jsonl`: `READ_FULL` in two explicit line ranges.
- `full_visual_audit_manifest_v1.tsv`: `READ_FULL` in two explicit line ranges; all 179 page rows inspected.
- `review_summary_v1.md`: `READ_FULL`.

Audit state confirmed: 179/179 pages visually audited; 25 genuinely blank, 10 false-empty OCR recoveries, 32 high-noise pages requiring scan check before exact quotation.

Article-relevant result: the Laura Spelman Rockefeller Memorial letterhead is not a single isolated page. It forms a five-page documentary cluster (`p0101`, `p0109`, `p0145`, `p0151`, `p0169`); `p0109` had been a total OCR false negative. This strengthens provenance/network context but, absent letter content establishing an action, the stationery cluster does **not** by itself prove foundation causality and should not be asked to do so.

Other recovered false-empty material is primarily agrarian history, Zeeland/legal reference slips, or fragmentary notes and does not currently alter the article argument.

Required next action: continue with every file in `review/chunk_002`, then sequentially through `review/chunk_071`.

## Corpus D — GitHub research / writing / archive / scripts

Trees recursively enumerated.

- `research/`: enumerated; article controls and provenance deltas present.
- `writing/`: seven files enumerated. Canonical draft remains `writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`.
- `archive/`: recursively enumerated; includes four source-probe JPGs plus archived Draft 01–03 and calibration/temporal-gate files.
- `scripts/`: two scripts enumerated.

Canonical Draft 04 current blob at start of this traversal: `176cc10280b0b906a2d2062fafd0bc460dd04876`. The prose was subsequently read in explicit ranges covering the introduction through the 1933 coda. A paragraph-function audit is in progress.

### First paragraph-function audit: recurrent parallelism

At least five existing passages currently contain evidence or scholarship that is only partly functional:

1. Intro final historiography paragraph: Rydin -> Wickberg -> Morgan currently behaves largely as a literature shelf; the final inference about retention/reassignment does more work than the citations leading to it.
2. End of America section: Biehn + “five years later” is a floating bridge rather than a demonstrated 1926-to-1931 causal relation.
3. 1926 Malinowski published-self-description paragraph: Frazer conversion, Central European formation, *Crime and Custom*, primitive mentality and Chimisso accumulate side by side; the strongest functional core is the shift of explanatory burden inside *Crime and Custom*.
4. 1930 lexical paragraph: multiple senses of `primitive/primitief` risk becoming a word-example display unless changing inferential licence is demonstrated.
5. Travel historiography paragraph: Small/van der Lem and Arnade/Vale form two scholarship clusters that need to alter particular evidentiary claims rather than remain adjacent literature.

These are not yet prose-edit instructions. Full corpus traversal may supply missing historical connections or show that some material belongs in notes rather than body.

## Corpus E — ChatGPT Library `/Huizinga`

Important correction to earlier scope: the user’s “Huizinga corpus in the library” is not reducible to the GitHub repo.

- Library folder `/Huizinga` confirmed.
- It contains original chunk scan PDFs in page blocks (multiple blocks from chunks 002 and 032 onward directly listed; chunks 048–056 specifically confirmed during this pass): `IMAGE_SOURCE_REGISTERED`.
- A top-level JSON-only listing under `/Huizinga` returned six non-chunk OCR files; none is obviously a Huizinga collected-works volume.
- The folder is large and paginated; collected/complete-work volumes have not yet been cleanly isolated from the archival chunk PDFs in this pass.
- Library content searches for `Verzamelde Werken` initially produced unrelated or secondary Huizinga material, including `/huaxi/3.json`; that file is a secondary Huizinga/Warburg study, not volume III of the collected works.
- Distinctive phrase searches (`kiemen van mijn wetenschappelijk denken`, `te veel van de schaduw des doods`, `de praktische sociologie der Amerikanen`, `Met dien primitief begrip der Renaissance`) did not return a confirmable collected-works primary file; they mainly returned an old article draft or unrelated OCR. This is a retrieval/indexing failure, **not** evidence that the collected works are absent.
- A surfaced `8.json` was inspected by snippet and belongs to unrelated West China Union University material; numbered JSON filenames cannot be treated as collected-work volume numbers.
- No file will be identified as a collected-works volume by number or filename guess alone.

Required next action: continue metadata traversal and try broader primary-text variants/known bibliographic markers to isolate the actual *Verzamelde Werken* / complete-works files, then traverse those volumes systematically.

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

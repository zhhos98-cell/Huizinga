# Current handoff — Huizinga

## Two separate states

### Corpus / retrieval

**CLOSED — 2026-08-30.**

Canonical closure files:

1. `FINAL_CLOSURE_2026-08-30.md`
2. `CLOSURE_STATE_2026-08-30.json`
3. `review/CURRENT_CALIBRATION_STATUS.md`
4. `review/CORE_THEME_HITS.md`

Sequential review-round logs no longer sit in the active `review/` surface. `PROGRESS.md`, `ROUND_001...042`, the tail round and backwards PDF-correction rounds are frozen under `archive/review_rounds/`. They are workflow provenance, not current authority and not a restart queue.

### Canonical source layout — reorganized 2026-09-05

Raw source corpora are now categorized under `sources/` so article work does not need to rescan the repository root.

- `sources/dbnl/` — DBNL mirrors; *Verzamelde Werken* TEI XML is under `sources/dbnl/verzamelde_werken/`.
- `sources/ocr/paddle/raw/` — immutable raw PaddleOCR chunk JSONs formerly stored at root.
- `sources/ocr/paddle/corrected/` — authorized corrected OCR derivatives.
- `sources/ocr/paddle/aggregates/` — historical merged convenience corpora.
- `corrections/` — correction ledgers / correction provenance.
- `review/chunk_*/` — page/chunk review, source checks and applied-patch audits.

Read `sources/README.md` and `sources/ocr/paddle/README.md` only when source-level rechecking is needed. The 2026-09-05 move preserved original Git blobs; source contents were not regenerated. `scripts/apply_pdf_corrections.py` has been updated to the new paths.

Retrieval order for article questions:

`research article/control note -> review/chunk_* -> corrected source -> raw source`.

Do not run a full corpus search when a bounded control already closes the point.

### Article writing

**ACTIVE.**

Read first:

1. `writing/README.md`
2. `writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`
3. `research/article_structure_recomposition_exchange_travel_institution_1933_2026-09-05.md`
4. `research/README.md`

Draft 04 is the canonical working article. Drafts 01–03 are superseded.

Current title:

**Only a Benevolent Outsider: Johan Huizinga, Bronisław Malinowski, and the Waning of the Primitive, 1926–1933**

Current writing rule: start from the direct Huizinga–Malinowski exchange, then call in earlier Huizinga material only where the exchange requires it. Prefer source wording over project-made terminology. Keep QA, evidence-ranking and repository shorthand out of article prose. `Primitive` remains the analytic pressure test but should not become the topic announced by every section.

## User-directed structural recomposition — 2026-09-05

The previous five-section `primitive`-led order is superseded by four parts:

1. `Exchange, Kula, and Mutual Calibration, 1926–1929`
2. `Travel and Comparative Method, 1929–1931`
3. `Institutions: Leiden, Anthropology, and the Human Sciences, 1931`
4. `1933 as a Hinge: Solutions, Limits, and Divergence`

Structural logic:

- **exchange first:** America is the encounter scene; Trekvaart, the three-book dispatch including *Argonauts*, reciprocal reading, Trobriands, and Kula carry the pair argument;
- **travel second:** compare knowledge practices rather than itineraries. Controlled evidence supports Malinowski's Trobriand fieldwork versus Huizinga's Java–Bali–Hong Kong travel / memory / card / source-verification regime. No controlled evidence supports a shared Bali destination;
- **institutions third:** Leiden carries the wider institutional history of anthropology / human sciences, including museums, philanthropy, disciplinary organization, `primitive or semi-cultured races`, Malinowski's audit and Huizinga's outsiderhood;
- **1933 as hinge:** compare incomplete responses rather than a completed solution. Kula → potlatch → Burgundy demonstrates comparison through specified relations; Academy `refrained`, Hofstra, and surviving developmental language prevent a conversion/disappearance story.

The 2026-09-05 Draft 04 recomposition removed the body paragraph whose main job was lexical polysemy (`Trois esprits prégothiques` + Renaissance `primitief`) and compressed the Philip-the-Good portrait dossier into a source-practice contrast. The old `[^9]` note remains an editorial-hygiene item, not a research gap.

## Kula longitudinal control — closed 2026-09-05

Use `research/article_kula_longitudinal_control_2026-09-05.md` rather than rerunning a broad Kula search.

Controlled chain:

`1926 three-book transaction / Argonauts received`
→ `1928 origins of culture vs historical use`
→ `1929 quite at home in the Trobriands + stage of savage life`
→ `1933 explicit Kula description`
→ `Malinowski's Kula illuminating related phenomena`
→ `potlatch relations`
→ `Burgundian reciprocal competitive display`.

This supports Kula as a longitudinal object of mutual calibration, not a simple influence chain. Reopen only for:

1. direct Huizinga annotation/excerpt/citation of *Argonauts* before 1933;
2. correspondence explicitly discussing Kula before 1933;
3. Malinowski responding to Huizinga's Kula/Burgundy comparison.

## Article-facing research

Active only when a specific sentence or note requires it. Current index: `research/README.md`.

High-value article support includes:

- 1921 Wells / Spengler;
- 1925 Bloch review;
- 7 April 1926 cultural-history theses;
- 1926–29 direct correspondence;
- Kula / *Argonauts* longitudinal chain;
- 1929 *De taak der cultuurgeschiedenis*;
- 1929 Philip the Good dossier;
- 1930 Dutch-culture lectures;
- 1931 Leiden Centre correspondence and institutional genealogy;
- 1933 Academy candidature, rectoral address and Hofstra exchange.

Nieuwenhuis / Leiden institutional genealogy: a same-titled 1913 Centre/museum-reorganization antecedent and the 1913 object-to-capacity programme are secure; direct 1913 → 1931 textual reuse remains NOTE / PARTIAL until BPL 2591 F9N and the Yale 1931 annex are directly compared. Use `research/article_nieuwenhuis_annex_1913_1931_genealogy_control_2026-09-05.md`.

### Current bounded next questions

Do not reopen generic `primitive` retrieval.

1. **post-1933 divergence:** only if the final section requires a symmetric later comparison; do not launch generic late-career sweeps;
2. **travel comparison:** seek a common-place control such as Bali only if direct evidence makes it plausible; otherwise retain Trobriands versus Java–Bali;
3. **chunk_018 America manuscript:** possible body addition only after key English wording and object/state are controlled.

### DBNL collected-works status — corrected 2026-09-05

The nine mirrored DBNL TEI XML files were fully machine-traversed: 79,038 XML elements, 23,422 normalized text blocks and 12,066,667 normalized characters, yielding 8,720 high-recall article candidates. A later audit found that the bounded 1921–1933 unit-review report—not the XML traversal—had been truncated by `ranked[:70]`: 124 units were surfaced but only 70 emitted. The cap is removed and the regenerated report emits 124/124 bounded units.

The restored 54-unit tail has been article-facing reviewed under `AGENTS.md`; its strongest items are reserves and none warrants a Draft 04 addition. See `research/article_dbnl_vw_truncated_tail_closure_2026-09-05.md`.

124/124 means every unit admitted by the bounded year/title rule, not individual manual annotation of all 8,720 candidate blocks. Do not restart generic thematic sweeps.

## Dormant provenance branch

The search for Huizinga’s three physical Malinowski books is closed unless direct copy-level evidence appears. A copy without a Huizinga ownership mark, Malinowski presentation inscription or documented Huizinga provenance should be dropped.

## Bounded dormant source-image debt

These source-image gaps remain factual boundaries rather than an active queue:

- `chunk_032:p0001-p0235` — OCR-calibrated only; source scans unavailable;
- `chunk_055:p0121-p0160` — unsupplied;
- `chunk_068:p0001-p0120` — unsupplied;
- `chunk_070:p0121-p0160` — unsupplied;
- `chunk_071:p0041-p0186` — unsupplied.

The early `chunk_008 s5105/s5106` external-source benchmark remains `IDENTITY_MISMATCH_PARTIAL / EXTERNAL_SOURCE_MATRIX_INCOMPLETE`; it is non-blocking.

## Restart rule

Reopen only a specific branch when the current article exposes a load-bearing factual gap, when a listed missing source span becomes available, or when a separate publication-grade reproofreading project is explicitly started. Do not restore old round queues, generic semantic sweeps or completionism.

# Final closure — Huizinga

Date: 2026-08-30  
Status: **CLOSED AT RETRIEVAL / RESEARCH-CALIBRATION GRADE WITH BOUNDED SOURCE-IMAGE DEBT**

This is the authoritative current-state document for `zhhos98-cell/Huizinga`. It supersedes older queue language in `review/PROGRESS.md`, the 2026-08-27 roll-up in `review/CURRENT_CALIBRATION_STATUS.md`, individual round notes, and stale `priority` / `next round` instructions whenever they conflict with this file.

## 1. Closure judgment

The present Huizinga corpus programme is closed.

`RESEARCH / THEMATIC DISCOVERY`
→ **CLOSED**

`RETRIEVAL-GRADE OCR / VISUAL CALIBRATION PROGRAMME`
→ **CLOSED AT AVAILABLE-SOURCE BOUNDARY**

`RAW OCR`
→ **PRESERVED**

`CORRECTED DERIVATIVES / MANUAL PATCH LEDGERS`
→ **PRESERVED**

`STRICT DIPLOMATIC RE-PROOFREAD V2`
→ **NOT RUN; FROZEN AS A SEPARATE PUBLICATION-GRADE EDITORIAL SCOPE**

`ACTIVE BLOCKING USER ACTIONS`
→ **NONE**

`GENERIC EXPANSION`
→ **STOP**

The remaining unavailable source-image spans are explicit verification debt, not an active research queue. Their absence does not license promotion of OCR-only readings to scan-verified facts, but it also does not keep the repository operationally open.

## 2. What is actually complete

The repository contains the 71 chunk JSON corpus, raw OCR preservation, page-level review/calibration material, a mature core-theme hit tracker, manual correction ledgers, and a long sequence of source-PDF review rounds.

The calibration programme established the distinction between:

`raw OCR presence`
≠ `retrieval usability`
≠ `source-image verification`
≠ `semantic/diplomatic transcription`.

That distinction remains mandatory after closure.

### 2.1 Broad visual/retrieval coverage

The 2026-08-27 roll-up already records retrieval-grade visual completion for chunks 001 and 003–031, page-level/false-empty closure for chunk 002, and full or supplied-set visual closure across most of chunks 033–059. Later status files and rounds extend the programme through the 060s.

Key later closures include:

- `chunk_060`: 250/250 source pages reviewed; no remaining visual span in its current local scan set;
- `chunk_061`: 234/234;
- `chunk_062`: 235/235;
- `chunk_063`: 233/233;
- `chunk_064`: 229/229;
- `chunk_065`: 228/228, including the Round-041 backfill of the earlier leading gap;
- `chunk_066`: 226/226;
- `chunk_067`: forward visual classification through p0160 plus direct original-PDF comparison of p0161–p0223 in Backwards Batch 003; the complete chunk has therefore been source-inspected, although the tail does not have the same page-classification manifest structure as the forward span;
- `chunk_069`: p0041–p0214 checked in Backwards Batch 002 and p0001–p0040 checked in Backwards Batch 003, giving complete source-PDF comparison of the 214-page chunk.

The backward correction rounds did more than lexical cleanup: they compared supplied original PDFs page by page against the OCR/JSON layer, removed pathological synthetic blocks, recovered legible labels/shelfmarks, and preserved all unaffected raw OCR.

### 2.2 Core-theme indexing

`review/CORE_THEME_HITS.md` is frozen as the current thematic/research index. It already separates first-order material from contextual vocabulary, bibliographical occurrences, stationery evidence, and OCR hallucinations.

The controlled thematic packets include, among others:

- visual/material production and circulation;
- play, games, chivalry and historical experience;
- Renaissance and Revolution conceptual vocabulary;
- eighteenth-century `wereldbeeld` / science-as-culture material;
- scholarly periodicals, correspondence and editorial infrastructure;
- Grotius editorial work;
- source-acquisition workflow;
- nationalism/patria, Methodism/enthusiasm and sentimentalism;
- Rockefeller stationery as documentary context only.

Negative-control rules remain binding: a lexical hit such as `primitief`, `anthropology`, `Rockefeller`, `play`, or an institutional letterhead is not by itself evidence for a substantive Huizinga claim, intellectual influence, sender identity, funding relation or agency.

No further generic semantic sweep is justified by the present project scope.

## 3. Bounded source-image verification debt

The following items remain explicitly unresolved at the source-image layer.

### A. `chunk_032` — OCR-calibrated, scan unavailable

Scope: p0001–p0235.

- 235/235 pages represented in the OCR page-class index;
- OCR-layer second pass calibrated;
- source-image visual audit unavailable;
- 66 baseline-empty OCR pages remain unresolved until a scan is available;
- high-value OCR packets, including the French-Revolution source-triangulation sequence and the late relief/committee material, remain **OCR-only** unless independently source-verified.

Classification:

`CHUNK_032 = OCR_CALIBRATED / VISUAL_SOURCE_UNAVAILABLE / NONBLOCKING_DEBT`.

### B. `chunk_055` — one interior source gap

Total source pages: 217.

Reviewed: p0001–p0120 and p0161–p0217 = 177/217.

Missing span:

`p0121–p0160`.

Classification:

`CHUNK_055_P0121_P0160 = UNSUPPLIED_SOURCE_IMAGE_DEBT`.

### C. `chunk_068` — leading source gap

Backwards Batch 003 directly checked p0121–p0200.

No equivalent supplied-PDF comparison is controlled here for:

`p0001–p0120`.

Classification:

`CHUNK_068_P0001_P0120 = UNSUPPLIED_SOURCE_IMAGE_DEBT`.

### D. `chunk_070` — middle source gap

Backwards Batch 001 directly checked p0001–p0120 and p0161–p0186.

Known missing span:

`p0121–p0160`.

Classification:

`CHUNK_070_P0121_P0160 = UNSUPPLIED_SOURCE_IMAGE_DEBT`.

### E. `chunk_071` — source comparison only for opening forty pages

Backwards Batch 001 directly checked p0001–p0040.

No supplied-PDF comparison is controlled here for:

`p0041–p0186`.

Classification:

`CHUNK_071_P0041_P0186 = UNSUPPLIED_SOURCE_IMAGE_DEBT`.

These five bounded debt items are dormant. If the source scans later appear in a backend resource, they may be used for a targeted upgrade, but the repo does not return to an open generic queue merely because the files exist.

## 4. Calibration benchmark boundary

The early benchmark programme contains a useful unresolved external-source identity case around `chunk_008` (`s5105/s5106`), tentatively associated with *The Rotarian* May 1936 / February 1937 material.

The repository-level source pages and externally recovered candidate covers were not sufficient to establish full identity. Keep the benchmark at:

`IDENTITY_MISMATCH_PARTIAL / EXTERNAL_SOURCE_MATRIX_INCOMPLETE`.

This is a calibration-boundary issue, not a load-bearing Huizinga historical claim. It is frozen unless the exact external source object becomes necessary for a reproducibility or publication claim.

## 5. Strict Reproofread V2 is deliberately not a closure criterion

`review/STRICT_REPROOFREAD_V2_PROTOCOL.md` correctly reset strict credit to zero and requires actual source scan + OCR comparison + correction decision + explicit audit row before a page can be called `STRICT_VERIFIED`.

Current strict-credit truth remains:

- chunk_067: 0/223 strict-verified;
- chunk_068: 0/200;
- chunk_069: 0/214;
- chunk_070: 0/186;
- chunk_071: 0/186.

Those zeros must **not** be rewritten as completed proofreading.

But V2 is now classified as a different deliverable: exhaustive publication-grade/diplomatic re-proofreading of every page. It is not required for the present retrieval/research-calibration project to close.

Therefore:

`STRICT_V2_ZERO_CREDIT ≠ ACTIVE RESEARCH BLOCKER`.

If a future edition, transcript or publication requires page-perfect text, V2 can be deliberately reopened as a separately scoped editorial project.

## 6. Corrections and raw-data guardrail

Raw PaddleOCR JSON remains immutable evidence.

Manual corrections are carried in corrected derivatives and explicit ledgers under `corrections/` and corresponding audit files under `review/chunk_*`.

Do not silently overwrite raw OCR to make it look cleaner.

Do not infer that a page was semantically proofread merely because it was visually classified.

Do not infer that a complete PDF-verification log equals diplomatic transcription unless it satisfies the strict V2 protocol page by page.

## 7. Reopening criteria

Reopen only a bounded branch if one of the following occurs:

1. one of the exact missing source-image spans listed above becomes available **and** source-level verification is useful;
2. a load-bearing historical claim requires exact scan control rather than OCR/retrieval control;
3. a publication requires diplomatic or near-diplomatic transcription, in which case Strict Reproofread V2 becomes a separately scoped editorial project;
4. a new primary source materially contradicts a retained first-order interpretation;
5. a new Huizinga dossier is deliberately scoped as a separate project.

Do **not** reopen for:

- generic keyword expansion;
- another undirected semantic sweep;
- completionism for its own sake;
- stale `priority` / `next round` wording in old status files;
- the existence of zero strict-V2 credit by itself;
- OCR hallucinations or weak lexical coincidences without a defined source test.

## FINAL STATUS

**HUZINGA RESEARCH / CALIBRATION PROGRAMME: CLOSED.**  
**RETRIEVAL-GRADE CORPUS: CLOSED AT AVAILABLE-SOURCE BOUNDARY.**  
**CORE-THEME INDEX: FROZEN.**  
**STRICT REPROOFREAD V2: NOT RUN / SEPARATE FUTURE EDITORIAL SCOPE.**  
**SOURCE-IMAGE RESIDUALS: FIVE BOUNDED DORMANT DEBT ITEMS.**  
**ACTIVE BLOCKING USER ACTIONS: NONE.**  
**GENERIC EXPANSION: STOP.**

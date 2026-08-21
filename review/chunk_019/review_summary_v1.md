# Chunk 019 OCR/page review summary

## Scope

- Source span: `chunk_019:p0001`–`chunk_019:p0167` (167 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–167.
- Page-count check: `40 + 40 + 40 + 40 + 7 = 167`.
- Review level: retrieval-grade page audit against the clean PaddleOCR v3 baseline.
- Page-image inspection is used only as an OCR-quality-control layer. It is not a separate image/visual research programme.

## Result

- **Full-page audit: 167/167 complete.**
- Page classes:
  - 18 usable
  - 100 usable-with-noise
  - 23 high-noise
  - 5 false-empty OCR recoveries
  - 11 short-text pages
  - 10 blank/no-substantive-text pages
- Baseline empty OCR pages: 15.
- Page-image result: 10 genuine blank/no-substantive pages and 5 false-empty recoveries.

### False-empty recoveries

`p0018`, `p0021`, `p0034`, `p0064`, `p0121`.

These pages contain mounted notes or handwritten material that would disappear from text-only retrieval.

### Genuine blank/no-substantive pages

`p0001`, `p0006`, `p0010`, `p0014`, `p0017`, `p0032`, `p0049`, `p0050`, `p0062`, `p0072`.

`p0072` contains a small scribble/archive mark but no substantive retrievable text for the present corpus.

### High-noise queue

`p0002, p0005, p0009, p0013, p0016, p0024, p0033, p0057, p0061, p0065, p0067, p0068, p0070, p0071, p0075, p0081, p0110, p0129, p0137, p0143, p0154, p0155, p0157`.

Dominant failure modes:

1. **mounted-slip under-capture / unstable reading order** (`p0002`, `p0005`, `p0016`, `p0057`, `p0061`, `p0075`, `p0154–p0155`);
2. **handwriting-model drift / multilingual hallucination** (`p0024`, `p0067–p0071`, `p0143`);
3. **gross OCR over-expansion** (`p0013`, `p0065`, `p0129`, `p0157`);
4. **near-total loss on small mounted notes** (`p0033`, `p0137`).

## Documentary structure of the chunk

The chunk has several distinct textual clusters.

### 1. American-history and U.S. network material (`p0002–p0054`)

Early notes concern American history and political/institutional subjects. The strongest single document is `p0031`, a typed memorandum arranging Huizinga’s appointments and travel through Philadelphia, Baltimore, Washington and Chapel Hill. It names the University of Pennsylvania, Johns Hopkins, the Cosmos Club, the Robert Brookings School and the University of North Carolina, along with individual hosts/organizers and detailed transport instructions.

`p0035–p0054` then forms a printed American-Revolution/constitutional source packet: John Adams debate material, the Articles of Confederation, representation/slavery questions, the Journals of the Continental Congress, James Truslow Adams and S. E. Morison.

### 2. Transitional notes and provenance (`p0055–p0080`)

This run mixes mounted working notes, bibliography and some highly unstable OCR. `p0063` preserves Laura Spelman Rockefeller Memorial letterhead. It should currently be treated only as a provenance cue.

### 3. French Revolution historiography and research infrastructure (`p0081–p0110`)

The notes survey major interpretations of the Revolution and repeatedly cite Burke, Thiers, Tocqueville, Quinet, Taine, Aulard, Jaurès, Caron and Tournaux. `p0096` is especially useful for the institutional history of Revolution scholarship; `p0103–p0106` explicitly inventory bibliographies, archival/publication projects, assembly records and newspapers.

### 4. Ancien Régime / revolutionary institutions (`p0117–p0150`)

The notes move into seigneurial rights, taxation, provincial estates, representative bodies, revolutionary committees and the Declaration of Rights. The handwriting OCR is generally retrieval-useful but unsuitable for long verbatim quotation without checking.

### 5. Dated Revolution working cards (`p0161–p0166`)

The final run is explicitly dated 1922–1923 and compresses interpretations and chronology from the intellectual framing of the Revolution through 1789, the Bastille, August decrees, rights, constitutional changes, 1791 and Convention/Jacobin material.

## Priority close-transcription queue

1. `p0031` only if a diplomatic transcription of the itinerary is needed; baseline is otherwise strong.
2. `p0087–p0106` for a precise reconstruction of Huizinga’s historiographical/source-method notes on the French Revolution.
3. `p0117–p0150` where specific institutional/economic claims are to be quoted.
4. `p0161–p0166` to reconstruct the dated working/teaching sequence.
5. False-empty pages `p0018`, `p0021`, `p0034`, `p0064`, `p0121` if their individual slips become relevant.

## Negative control

No secure Malinowski / anthropology / ethnology dossier appears in chunk 019. Apparent lexical matches occur within unrelated French-Revolution notes and were rejected.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 019 retrieval-grade OCR/page audit: COMPLETE (167/167).**

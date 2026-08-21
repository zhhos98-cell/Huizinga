# Chunk 020 OCR/page review summary

## Scope

- Source span: `chunk_020:p0001`–`chunk_020:p0206` (206 scan pages).
- Split scan set verified complete and contiguous: 1–40, 41–80, 81–120, 121–160, 161–200, 201–206.
- Page-count check: `40 + 40 + 40 + 40 + 40 + 6 = 206`.
- Review level: retrieval-grade page audit against the clean PaddleOCR v3 baseline.
- Page-image inspection is used only as an OCR-quality-control layer. It is not a separate image/visual research programme.

## Result

- **Full-page audit: 206/206 complete.**
- Page classes:
  - 164 usable-with-noise
  - 27 high-noise
  - 4 false-empty OCR recoveries
  - 3 short-text pages
  - 8 blank/no-substantive-text pages
- Baseline empty OCR pages: 12.
- Page-image result: 8 genuine blank/no-substantive pages and 4 false-empty recoveries.

### False-empty recoveries

`p0001`, `p0010`, `p0176`, `p0177`.

- `p0001` is the title `Aperçu de la civilisation hollandaise du XVIIe siècle`.
- `p0010` is a dense handwritten continuation page.
- `p0176–p0177` are mounted boards with substantive handwritten slips.

### Genuine blank/no-substantive pages

`p0116`, `p0162`, `p0164`, `p0167`, `p0174`, `p0175`, `p0183`, `p0189`.

`p0189` contains mounted blank slips but no substantive retrievable writing.

### High-noise queue

`p0004, p0035, p0041, p0063, p0084, p0120, p0122, p0137, p0178, p0179, p0180, p0181, p0182, p0184, p0185, p0186, p0187, p0188, p0194, p0199, p0200, p0201, p0202, p0203, p0204, p0205, p0206`.

Dominant failure modes:

1. **dense handwriting under-capture** (`p0035`, `p0041`, `p0063`);
2. **OCR over-expansion/repetition or model drift** (`p0004`, `p0084`, `p0120`, `p0122`, `p0137`, `p0194`, `p0200`);
3. **mounted-slip under-capture / unstable reading order** (`p0178–p0182`, `p0184–p0188`, `p0199–p0206`);
4. **cross-panel concatenation of distinct topics** (`p0203–p0204`).

## Documentary structure of the chunk

### 1. French seventeenth-century Dutch-civilization lecture (`p0001–p0115`)

The title page identifies the dossier as `Aperçu de la civilisation hollandaise du XVIIe siècle`. The manuscript builds a cultural-historical account through geography, economy, political institutions, urban/social structure, religion, learned institutions and major intellectual/literary figures before moving through painting, architecture and foreign influence.

The strongest methodological pages are `p0011–p0012`, where Huizinga resists treating `baroque` as a sufficient period label and explicitly discusses social, economic, political and ethnographic conditions as useful but incomplete explanations of a civilization.

### 2. Heidelberg German version (`p0117–p0160`)

`p0117` names the University of Heidelberg and gives the theme `Die sozialen Grundlagen der holländischen Kultur des 17. Jahrh.` The German text closely parallels the French argument. `p0121–p0124` repeat the problem of period labels and the move toward social/economic/political/ethnographic conditions.

This is a strong multilingual-version cluster; exact translation/revision relationships remain a collation task.

### 3. Dutch outline and ceremonial note (`p0161–p0173`)

`p0161`, `p0165–p0173` return in Dutch to the foundations of seventeenth-century Dutch culture. `p0163` separately discusses receipt of a university `Doktorwürde`; the institution on that page is not yet securely read.

### 4. Mounted medieval/legal and historiographical cards (`p0176–p0206`)

This is a heterogeneous card-index zone. It includes:

- Brabant/Leuven and medieval municipal/charter material (`p0176–p0181`);
- Augustine / medieval political-theory and related bibliography (`p0184–p0188`, later cards);
- Eduard Meyer's theory/method of history (`p0186`);
- explicit notes on the definition and scientific status of history (`p0201–p0204`);
- political-thought bibliography and natural-law/state material (`p0199–p0205`).

The scan-page unit is often not the intellectual unit here: several pages contain two boards or multiple independent slips.

## Priority close-transcription queue

1. `p0001`, `p0010` to restore the two false-empty pages inside the French lecture.
2. `p0011–p0012` for the methodological passage on `baroque` and explanatory conditions.
3. `p0117`, `p0121–p0124` to establish the Heidelberg version and collate it against the French manuscript.
4. `p0163` to identify the university / honorary-degree context precisely.
5. `p0176–p0181` if the municipal/charter notes become relevant.
6. `p0186` and especially `p0201–p0204` for Huizinga's explicit theory-of-history / history-as-science notes.
7. `p0203–p0205` at panel/slip level, because OCR currently concatenates distinct note sequences.

## Negative control

No secure Malinowski / anthropology / ethnology dossier appears in chunk 020. No Rockefeller transaction is securely established.

## Files

- `full_visual_audit_manifest_v1.tsv`
- `empty_ocr_visual_review.jsonl`
- `core_theme_hits_v1.md`
- `review_summary_v1.md`
- `status.txt`
- `README.md`

## Status

**Chunk 020 retrieval-grade OCR/page audit: COMPLETE (206/206).**

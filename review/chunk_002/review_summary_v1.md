# chunk_002 substantive OCR + scan calibration summary

## Review level

`chunk_002.pdf_by_PaddleOCR-VL-1.6.json` remains preserved unchanged. The review layer now combines the earlier OCR-layer calibration with direct access to the complete contiguous scan set `p0001-p0183`.

On 2026-08-26 the three 61-page PDF segments were materialized in the review runtime, rendered, and inspected. This resolves the former absolute-page blocker. A macro visual sweep now covers all 183 pages, and the highest-priority OCR anchors were checked at higher resolution against the scans.

This is still not diplomatic transcription. Dense handwriting, mounted composite boards and severe machine over-generation remain reasons to check the scan before exact quotation.

## 1. Absolute alignment restored

The raw PaddleOCR results occur in sequential four-image batches. Direct scan comparison supplies secure absolute anchors:

- `72bbc5ae-...` -> `p0001-p0004` (early Zeeland boards)
- `7d56ec88-...` -> `p0005-p0008` (`Zelandensia` visibly at p0006)
- `eda81e7f-...` -> `p0009-p0012` (`Salimbene 1914/15` at p0011)
- `1ef7154e-...` -> `p0029-p0032` (Florence communal/factional notes)
- `9bcf2bc7-...` -> `p0049-p0052` (`Trois esprits prégothiques < Paris 1930 >` at p0049)
- `dce87a52-...` -> `p0085-p0088`
- `f1e3ac39-...` -> `p0089-p0092`

The earlier OCR-layer association of the literal `Zelandensia` with `72bbc...` was too loose: the scan shows the envelope word itself on p0006, hence in the next raw batch, `7d56...`. Both batches nevertheless belong to the same Zeeland complex.

See `visual_anchor_alignment_v2.tsv`.

## 2. Zeeland / Middelburg packet

The opening pages are physically composite archival boards and envelopes with short mounted slips. p0002 visibly contains Zeeland legal/bibliographical material; p0006 carries an envelope marked `Zelandensia`. The raw OCR is useful for retrieval but often flattens separate slips into unstable reading order. Page-level quotation from this packet should therefore cite the scan and reconstruct each mounted item locally.

## 3. Salimbene / medieval Italy

p0011 is a clean title card reading `Salimbene 1914/15`, and p0012 begins the associated notes. This locks the Salimbene raw batch to p0009-p0012 and confirms that the medieval-Italy packet is a distinct physical sequence rather than an OCR-only semantic cluster.

## 4. Florence communal / political / art-historical complex

The dense notebook sequence around p0029-p0048 is visually real. p0029 visibly treats Florence communal and factional history, matching the raw OCR cluster containing Florence, Ciompi, Albizzi, Medici and related civic/artistic material. The packet is secure for retrieval; the rough OCR remains unsuitable as line-by-line transcription.

## 5. `Trois esprits prégothiques`: strongest conceptual complex

p0049 is the title card `Trois esprits prégothiques < Paris 1930 >`. The following long French manuscript packet supplies the strongest conceptual material in chunk 002.

Three priority findings are now scan-verified:

- p0086, manuscript p.31: the page visibly begins `Cet élément ludique` and develops competition/disputation. This confirms that the play vocabulary is conceptual and embedded in an argument about scholastic/dialectical competition.
- p0087, manuscript p.32: `primitive` is visibly present in the continuation of the same intellectual-history argument. The positive hit is therefore medieval/intellectual-historical, not an anthropology keyword coincidence.
- p0090, manuscript p.35: the page visibly states that Abélard should not be treated simply as a precursor of the Renaissance but `au contraire comme un prégothique`; the continuation characterizes the apparent modernity / underlying intellectual apparatus in terms including `primitive`.

These are now first-order scan anchors for the genealogy of Huizinga's play vocabulary, competitive forms, periodization and `primitive` terminology. Exact punctuation and full diplomatic transcription should still be taken from close scan reading, not copied from PaddleOCR.

## 6. OCR pathology directly demonstrated

p0089 is particularly useful as a control. The scan contains ordinary continuous French handwriting on manuscript p.34. The raw OCR for the same batch generated a catastrophic table-like structure with an enormous repeated numerical string. This shows that the most spectacular machine strings in chunk 002 can be pure model over-generation rather than difficult-but-real manuscript content.

The conservative policy remains: coherent scan-supported historical language outranks generated modern English, repeated-number continuations, mixed scripts, biomedical insertions and other semantic hallucinations.

## 7. Negative controls

The previous raw-OCR negative controls remain: no secure `Malinowski`, `anthropolog*`, or `ethnolog*` match was established. The now visually verified `primitive` passage strengthens the immediate medieval intellectual-history reading rather than an anthropological one.

A raw-OCR negative for Rockefeller remains only an OCR negative. The complete scans are now available, so a true stationery-level visual exclusion can be made in a dedicated page-by-page pass if needed.

## Adequacy assessment

The current layer is adequate for corpus retrieval, absolute pXXXX citation of the verified anchors, thematic analysis, and distinguishing genuine conceptual evidence from OCR hallucination. It is not yet a full diplomatic edition or a finished page-by-page OCR usability manifest.

## Next closure pass

1. Pinpoint the exact scan leaf for the Haskins / *The Renaissance of the Twelfth Century* line and the nearby Gilson line inside the p0049-p0136 packet.
2. Run page-by-page OCR usability / false-empty grading across p0001-p0183 if chunk 002 is to be promoted to the same retrieval-grade manifest format as chunks 003-031.
3. Use the scan rather than raw JSON for any exact quotation from p0086-p0090 or the mounted composite boards.

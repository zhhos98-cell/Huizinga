# chunk_032 OCR-layer calibration summary

`chunk_032:p0001-p0235` contains 235 OCR page records. This pass calibrates the **existing PaddleOCR layer only**. The raw file `chunk_032.pdf_by_PaddleOCR-VL-1.6.json` is preserved unchanged. No chunk-032 scan PDF is currently available in the review workspace, so this is not a visual audit and must not be labelled retrieval-grade visual completion.

## Calibration state

- 235/235 OCR records are represented in the existing page-class index.
- 66 pages are baseline-empty and remain `UNRESOLVED_SCAN_UNAVAILABLE`.
- 56 pages are `ocr-coherent-with-noise`.
- 17 pages are `ocr-high-noise`.
- 7 pages are `ocr-short-unverified`.
- 89 pages are `ocr-pathological`.
- Raw OCR remains immutable source data; corrections below are a separate interpretive/retrieval layer.

The present pass does **not** convert any baseline-empty page into blank or false-empty status. That distinction requires the scans.

## Main documentary result 1: French-Revolution source work is substantially more coherent than the first triage suggested

The strongest recoverable complex remains `p0108-p0159`, but a second pass through the raw OCR shows that it is not merely a topical run on the French Revolution. It preserves a repeated **source-triangulation workflow**.

One sequence tries to identify and reconstruct an Assemblée nationale deputy by consulting several different reference works: a general biographical dictionary, an `Almanach des députés à l'Assemblée nationale`, a modern biographical work, a historical/biographical dictionary of the Revolution and Empire, and revolutionary periodical/bibliographical material. The OCR is imperfect at names and dates, but the research operation is clear: a person or statement is pursued across multiple reference instruments rather than accepted from one source.

A second sequence is headed in OCR `Robespierre : Idées religieuses et fèles nationales` (the second word is almost certainly OCR-damaged and is not silently normalized here). It follows Robespierre's statements concerning Lafayette and Dumouriez, then asks what particular facts those accusations may have referred to. The Dutch working prose explicitly records failure to find a closer factual match at one point and then treats Robespierre as attempting to give an historical `beeld` of the politics of the persons concerned.

The dossier then follows Earl Stanhope and Pitt through biographical reference material and `Parliamentary History`, checking motions of January and April 1794, the institutional difference between Commons and Lords, and whether a parliamentary event really corresponds to Robespierre's wording. Several OCR dates are visibly corrupt in context (`994`, `1994` inside an otherwise 1794 sequence); these are machine errors, not source dates.

Other stable anchors in the same broad complex include the National Convention, `10 Frimaire II`, Barère, Le Chapelier and revolutionary press/bibliography. Some individual pages remain pathological, so the safe research unit is the packet and its source-checking procedure rather than a verbatim transcription.

**Research value:** the chunk preserves practical historical criticism in action: `problem/quotation -> identify actor -> consult multiple biographical/bibliographical tools -> check parliamentary/event chronology -> compare source wording -> formulate a cautious historical interpretation`.

## Main documentary result 2: academic-relief / prisoner-student committee material

The late packet `p0219-p0235` is also stronger than the first triage description `academic-relief fragments` suggested. OCR-supported text describes an organization operating on a principle rendered approximately as **strict reciprocity** and taking as its task assistance to **krijgsgevangen of geïnterneerde studenten**. The assistance includes books or comparable study materials and means for continuing scientific/scholarly work; another block refers to work at the expense of the committee, scientific activity, provision of information and consultation with academic teachers.

The material contains a disciplinary allocation including `Oudgerm.`, `Vergel. taalwetenschap`, `Sanskrit` and `Vad. of alg. geschiedenis`, and a roster headed by:

- `J. HUIZINGA, Voorzitter, Leiden.`
- `L. VAN ITALLIE, Leiden.`
- `J. H. KERN, Groningen.`
- `A. NOORDTZIJ, Utrecht.`
- `L. H. SCHOLTE, Amsterdam.`

`p0233` remains the clearest OCR-layer anchor for this relief/committee strand. The exact formal committee name and the precise wording of its rules require the scan before quotation.

The same `J. HUIZINGA, Voorzitter, Leiden / L. VAN ITALLIE, Leiden` wording also appears in the OCR around the earlier administrative transition (`p0175`). Without page images we should not decide whether this is a duplicate form, a related committee document or a separate institutional item.

## Documentary structure after the second OCR pass

- `A1 p0001-p0028`: heavily corrupted pre-Revolution / mixed historical notes. Fifteen baseline-empty pages. `p0022` has an `ethnologia` string embedded in generated sociological/English prose and remains a negative control, not an anthropology hit.
- `A2 p0029-p0043`: early Revolution / 1789 source-bibliography material, still too unstable for close argument reconstruction.
- `A3 p0044-p0107`: mixed political/social-historical notes with extensive semantic hallucination and reading-order failure.
- `A4 p0108-p0159`: strongest coherent complex; French-Revolution research with biographical dictionaries, deputy/reference tools, Robespierre, Convention/Frimaire, Stanhope/Pitt and parliamentary cross-checking.
- `A5 p0160-p0180`: Leiden administrative/stationery forms and institutional names. Relationship to the later relief committee is plausible at OCR level but unresolved.
- `A6 p0181-p0218`: mixed medieval/bibliographical working notes with many empty/pathological records.
- `A7 p0219-p0235`: coherent academic-relief / prisoner-and-interned-student committee material embedded among noisy pages; Huizinga is explicitly listed as `Voorzitter`.

## Machine-pathology controls

The raw OCR contains conspicuous non-source generation, including repeated modern year sequences extending far beyond the historical material, stock English prose, mixed-script substitutions and semantic over-generation. One Barère page, for example, appends repeated generic English (`He had been born in the world...`) after a plausible historical heading. A separate pathological result produces huge repeated year tables. Such generated text is excluded from research claims even when a genuine name survives at the beginning of the page.

The OCR-only `play` matches occur inside similarly broken English generation and are not evidence for a play/game dossier.

## Research-facing negative controls

- No secure `Malinowski` hit is present in the raw OCR.
- No secure `primitive` / `primitief` hit is present in this chunk's raw OCR.
- The `ethnologia` occurrence at `p0022` is embedded in severe semantic corruption and is not an anthropology/ethnology dossier.
- No secure first-order play/game hit is established.
- No Rockefeller Memorial occurrence is established in the raw OCR layer.

## Files

- `page_class_index_v1.md` — canonical OCR-only page classes.
- `empty_ocr_unresolved_v1.tsv` — all 66 baseline-empty pages, deliberately unresolved pending scans.
- `composite_page_structure_v1.tsv` — packet map, refined in this calibration pass.
- `ocr_anchor_index_v1.tsv` — conservative source/research anchors from the second OCR pass.
- `core_theme_hits_v1.md` — research-facing hits and negative controls.
- `status.txt` — compact status.

## Status

**Chunk 032 existing OCR layer: CALIBRATED FOR RETRIEVAL/TRIAGE.**

**Visual audit: BLOCKED / SCAN UNAVAILABLE.**

This chunk must remain open until the scan pages are supplied and the 66 baseline-empty pages plus the 89 pathological pages can be checked visually.
# chunk_002 PDF/OCR crosswalk notes

Date opened: 20 August 2026

## Control principle

For proofreading and archival citation, the physical PDF page/image is authoritative. The frozen OCR corpus remains immutable and is used as a search/draft layer only. Any page-number divergence, OCR page merge, or repeated photographic capture of the same manuscript leaf must be recorded here and propagated to later export/index work.

A further distinction is now explicit: a physical PDF `page` is a **photographic capture**, not necessarily a unique manuscript leaf. Adjacent captures can overlap and repeat one side of a notebook spread while changing the other side. Future page/index work therefore needs both a `capture_id` and, where possible, a `leaf_id` / `capture_overlap` relation.

## Exception 001 — physical pp.30–31 merged in frozen OCR p0030

Observed during image-first proofreading of the Florence dossier.

### Physical PDF p30

- mostly blank page;
- contains only the short continuation on the Ciompi → Albizzi → Medici transition;
- visually distinct physical page numbered `6` in Huizinga's notebook sequence.

### Physical PDF p31

- separate notebook page numbered `7`;
- contains the substantial transition into Florence's monumental building and architecture: communal building works, S. Maria del Fiore, Palazzo della Signoria, Romanesque/material notes, mosaic/inlay/coloured stone.

### Frozen OCR behaviour

- `chunk_002:p0030` contains the p30 Ciompi lines **followed by** the substantial architectural text from physical p31.
- `chunk_002:p0031` is nearly empty (`Ola A. Alonke Omeronov 24. 100 kWh in`), i.e. it does not represent the physical p31 text.
- `chunk_002:p0032` again corresponds to physical PDF p32 (Latin transcription on left + Baptistery/Gothic notes on right).

### Required downstream handling

1. Do not cite the architectural material as physical p30 merely because it appears in OCR `p0030`.
2. Human-facing citations/notes should use physical PDF p31 for the architecture block.
3. A future corrected/search layer should split OCR `p0030` into two page associations rather than rewriting the frozen corpus.
4. Any page-level corpus index should include a `crosswalk_exception` field for physical pp.30–31.

Status: **confirmed by direct image comparison**.

## Capture overlap 002 — physical pp.32–33 repeat the same left-hand Latin leaf

Direct image comparison shows that physical PDF p32 and p33 are overlapping photographs of a notebook/spread configuration.

- The **left-hand Latin documentary leaf is the same physical leaf** in both captures.
- The **right-hand Huizinga page changes** between p32 and p33.
- The repeated Latin text is a crusade/pilgrimage ecclesiastical transcription with secure anchors including `Dilectis in Christo amicis ...`, `peregrinationis`, `Damietam`, `Babyloniam`, and `Alexandriam`.
- The duplicate capture must not be counted as two independent documents or two independent Latin transcriptions.

### Required downstream handling

- mark physical pp.32–33 with the same `leaf_id` for the repeated left-hand leaf, or use an explicit `capture_overlap_A` relation;
- keep the two PDF capture locators because their right-hand content differs;
- do not deduplicate the whole PDF page/capture, only the repeated manuscript leaf within the capture.

Status: **confirmed by direct image comparison**. Text control is recorded in `TEXT_PASS_008_p033_p036-037_LATIN.md`.

## Capture overlap 003 — physical pp.36–37 repeat the same left-hand Latin leaf

Physical PDF p36 and p37 form a second overlapping-capture pair.

- The **left-hand Latin leaf is the same physical leaf** in both captures.
- The right-hand Florence/Giotto working page changes between the captures.
- Huizinga's source heading on the repeated Latin leaf is secure as `Van Mieris, Groot Charterboek I 176.`
- The copied document begins `A divina permissione dictus patriarcha Hierosolimitanus ...` and concerns crusaders/pilgrims, Jerusalem/Egypt and ecclesiastical support/authority.

### Required downstream handling

- record a shared `leaf_id` / `capture_overlap_B` for the repeated left-hand leaf;
- retain p36 and p37 as distinct photographic captures because their right-hand pages differ;
- never infer two independent documents merely from two PDF page numbers.

Status: **confirmed by direct image comparison**. Text control is recorded in `TEXT_PASS_008_p033_p036-037_LATIN.md`.

## Severe OCR failure control

`chunk_002:p0098` is a readable physical French manuscript page but the frozen OCR is essentially unusable. It remains a strong example of why OCR emptiness/nonsense cannot be treated as evidence that a page lacks text.

## Downstream schema recommendation

A corrected/searchable derivative should preserve at minimum:

- `pdf_capture_page`;
- `ocr_page_id`;
- `leaf_id` when identifiable;
- `capture_overlap` / repeated-leaf relation;
- `crosswalk_exception`;
- proofreading state;
- corrected/search text as a separate derivative layer.

The frozen OCR itself remains unchanged.

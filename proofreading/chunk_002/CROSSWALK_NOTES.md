# chunk_002 PDF/OCR crosswalk notes

Date opened: 20 August 2026

## Control principle

For proofreading and archival citation, the physical PDF page/image is authoritative. The frozen OCR corpus remains immutable and is used as a search/draft layer only. Any page-number divergence or OCR page merge must be recorded here and propagated to later export/index work.

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

# chunk_032 OCR page-class index

This is the canonical OCR-only triage index for `chunk_032:p0001-p0235`. A second pass through the raw PaddleOCR JSON has now refined the packet interpretation and research anchors, but **no chunk-032 scan PDF is currently available**, so every class below remains visually unverified. Raw PaddleOCR text is preserved unchanged.

Second-pass calibration status: **OCR layer calibrated for retrieval/triage; visual audit still blocked by scan unavailability.** No baseline-empty page has been reclassified without a scan.

## baseline-empty-unresolved — 66

p0001,p0002,p0006,p0007,p0008,p0009,p0012,p0013,p0019,p0020,p0023,p0024,p0026,p0027,p0028,p0031,p0033,p0037,p0042,p0045,p0047,p0048,p0049,p0050,p0053,p0054,p0057,p0058,p0060,p0064,p0065,p0071,p0073,p0076,p0080,p0081,p0085,p0086,p0090,p0093,p0094,p0095,p0096,p0103,p0113,p0139,p0160,p0164,p0167,p0173,p0174,p0177,p0178,p0181,p0184,p0185,p0191,p0198,p0202,p0207,p0210,p0215,p0216,p0217,p0218,p0230

## ocr-coherent-with-noise — 56

p0118,p0119,p0120,p0121,p0122,p0123,p0124,p0125,p0126,p0128,p0129,p0130,p0132,p0135,p0136,p0137,p0138,p0140,p0141,p0142,p0143,p0144,p0145,p0147,p0148,p0149,p0151,p0152,p0153,p0155,p0156,p0157,p0158,p0159,p0161,p0175,p0188,p0192,p0193,p0194,p0196,p0199,p0200,p0201,p0203,p0204,p0208,p0209,p0211,p0212,p0222,p0225,p0226,p0233,p0234,p0235

These pages contain relatively sustained historical/documentary text at the OCR layer. They are retrieval anchors only; exact quotation and documentary-form claims still require the scans.

## ocr-high-noise — 17

p0003,p0010,p0011,p0015,p0017,p0021,p0025,p0029,p0034,p0038,p0055,p0061,p0063,p0083,p0102,p0108,p0110

## ocr-short-unverified — 7

p0004,p0014,p0030,p0088,p0101,p0176,p0180

## ocr-pathological — 89

p0005,p0016,p0018,p0022,p0032,p0035,p0036,p0039,p0040,p0041,p0043,p0044,p0046,p0051,p0052,p0056,p0059,p0062,p0066,p0067,p0068,p0069,p0070,p0072,p0074,p0075,p0077,p0078,p0079,p0082,p0084,p0087,p0089,p0091,p0092,p0097,p0098,p0099,p0100,p0104,p0105,p0106,p0107,p0109,p0111,p0112,p0114,p0115,p0116,p0117,p0127,p0131,p0133,p0134,p0146,p0150,p0154,p0162,p0163,p0165,p0166,p0168,p0169,p0170,p0171,p0172,p0179,p0182,p0183,p0186,p0187,p0189,p0190,p0195,p0197,p0205,p0206,p0213,p0214,p0219,p0220,p0221,p0223,p0224,p0227,p0228,p0229,p0231,p0232

This class marks pages with strong evidence of semantic hallucination, mixed-script substitution, repetitive over-generation, modern stock prose/URLs, numerical runs, or severe corruption. It does not imply that the underlying scan lacks useful content.

## Refined provisional packet map

- `A1 p0001-p0028`: heavily corrupted pre-Revolution/mixed historical notes. `p0022` `ethnologia` is a machine-corruption negative control.
- `A2 p0029-p0043`: early Revolution/1789 source and bibliography anchors.
- `A3 p0044-p0107`: mixed political/social-history notes with severe semantic instability.
- `A4 p0108-p0159`: strongest OCR-coherent packet. Second pass establishes a source-triangulation sequence involving Assemblée nationale biographical/reference lookup, Robespierre/Lafayette/Dumouriez, Convention/Frimaire, Barère/Le Chapelier, and Stanhope/Pitt checked against `Parliamentary History`.
- `A5 p0160-p0180`: Leiden administrative/stationery/institutional transition; `p0175` has `J. HUIZINGA, Voorzitter, Leiden. L. VAN ITALLIE, Leiden.` Possible relation to A7 remains unresolved.
- `A6 p0181-p0218`: mixed medieval/bibliographical working notes; many pathological or empty records.
- `A7 p0219-p0235`: academic-relief / POW-and-interned-student committee material amid noisy pages. `p0233` is the clearest anchor; OCR describes aid for `krijgsgevangen of geinterneerde studenten` and names Huizinga as `Voorzitter`.

## Second-pass research controls

- Strongest methodological hit: A4 historical source triangulation and parliamentary cross-checking.
- Strongest institutional hit: A7 academic relief for prisoner/interned students, with Huizinga as chair.
- No secure `Malinowski`, `primitive/primitief`, Rockefeller Memorial or first-order play/game hit was established in the raw OCR.
- `ethnologia` at `p0022` and OCR `play` strings on pathological pages are explicitly rejected as research hits.

See `ocr_anchor_index_v1.tsv`, `core_theme_hits_v1.md` and `review_summary_v1.md` for the calibrated interpretation.
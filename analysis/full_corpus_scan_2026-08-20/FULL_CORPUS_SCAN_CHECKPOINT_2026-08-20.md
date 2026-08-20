# Full corpus scan checkpoint — 20 August 2026

## Scope

Input: `huizinga_leiden_paddleocr_clean_001-071_complete_v3.json`

Input SHA-256: `fae29b1cc98ef0142e0fcef66b2c1b275e6fbe2f5521fdb8582da346c9a7454e`

The scan covered the consolidated Leiden OCR **from page 1 through page 15,139 without early exit**.

- pages scanned: **15,139**
- non-empty OCR pages: **12,654**
- empty OCR pages: **2,485**
- review queue after false-positive cleaning: **A = 8**, **B = 15**, **C = 318**
- machine-readable sparse marker rows: **341**

This is a discovery/triage layer, not a new transcription. No OCR wording was silently corrected.

## Marker policy

Each page was checked for:

1. exact core entities: Huizinga, Malinowski, Rockefeller, Laura Spelman Rockefeller Memorial, Van Sickle, Kittredge, Outhwaite, Nieuwenhuis, Van Eerde, Van de Sande Bakhuyzen, de Josselin de Jong, Rassers, Van Vollenhoven, Hornbostel, Westenenk, Van Erp, and selected Rockefeller officers;
2. separate fuzzy-name candidates, using bounded edit distance; fuzzy hits are never promoted to confirmed identities by themselves;
3. project vocabulary: anthropology / ethnology / ethnography / volkenkunde; sociology / social science; centre / institute / museum; Rockefeller Foundation / Memorial; colonial / Netherlands Indies; musicology / phonogram; fieldwork; primitive;
4. dates in the 1920–1935 window;
5. documentary signals: archive headers, correspondence salutations/addresses, Rockefeller letterhead/trustee text, report/memorandum vocabulary;
6. OCR/material warnings, especially pages on which Rockefeller letterhead appears mixed with unrelated Huizinga notes.

The scanner records page IDs and preserves the physical sequence of the consolidated corpus. A/B priority pages were then inspected with neighboring pages so that obvious newspaper/bibliographic false positives could be demoted.

## What the full pass did and did not find

### 1. The 17 July 1931 Huizinga memorandum packet is **not text-layer confirmed**

The current project control expects:

- Huizinga, 17 July 1931, “Memorandum on the development of a Centre of Anthropological Research in connexion with the reorganization of the Ethnographical Museum at Leyden”;
- seven folio pages of typescript signed by Huizinga;
- two-page Nieuwenhuis addendum, “Ethnographical objects as data for psychological research about primitive or semi-cultured races”;
- surrounding 19 July / 30 July / 12 August Huizinga–Malinowski correspondence.

The full sequential OCR pass did not produce a credible match for the memorandum title, Nieuwenhuis title, `mixtum compositum`, `definite social science`, `benevolent outsider`, or the known 1931 correspondence wording.

This is **not evidence of archival absence**. There are 2,485 empty OCR pages, and a physical document may be present but unreadable at text layer.

### 2. The 1932 Outhwaite / Leiden Survey reports are **not text-layer confirmed**

No exact Outhwaite, Van Sickle, or Kittredge hit survives manual validation as the target Rockefeller/Leiden material. Fuzzy candidates were retained in the marker index but inspected conservatively; none currently justifies identification of the missing Survey reports.

### 3. Rockefeller material is physically present throughout the corpus

`Rockefeller` occurs on 73 OCR pages; Laura Spelman Rockefeller Memorial / Rockefeller Memorial stationery language occurs on dozens of pages.

The important control is that many of these pages appear to be **stationery reuse, verso material, or OCR layer mixing** rather than Rockefeller correspondence about the 1931 Leiden scheme. Therefore `Rockefeller` alone is not a dossier identifier.

Highest-value image-review page:

- **`chunk_027:p0046`** — reads `Rockefeller Memorial`, trustee names including John D. Rockefeller Jr., George Welwood Murray and Raymond B. Fosdick, plus the exact date **23 Juni 1931**. The same OCR page also contains `Sterrewacht` and unrelated reading-note matter. Treat as an A-level **material-image question**, not yet as a 1931 Rockefeller visit document.

Related:
- `chunk_027:p0048` — Rockefeller Memorial trustee/letterhead fragment, with `1928`.

### 4. Two exact “Social Sciences in Holland” labels surfaced

- **`chunk_037:p0157`** — `FOR THE SOCIAL SCIENCES IN HOLLAND`
- **`chunk_067:p0140`** — `FOR THE SOCIAL SCIENCES IN HOLLAND — DR. J. HUIZINGA`

Both are embedded among Huizinga note material. They are A-level image-review targets because the OCR cannot establish whether they are printed slips, dividers, versos, stationery, or another material layer.

### 5. `HUI-071-2-31-000` is a real article-working dossier with underused primary material

The corpus itself supplies the archive boundary:

- **`chunk_068:p0052`** — `Inventarisnummer: HUI-071-2-31-000`
- **`chunk_068:p0053`** — `Hui zi II (artikelen) 31 / Klank die wegsterft`

Within that unit:

- **`chunk_068:p0058`** — incoming letter to Huizinga; Walter Kaudern, Hornbostel, Stanford University, and tactical timing of Huizinga’s *De Gids* article;
- **`chunk_068:p0059`** — continuation/address material: Papaverhof 10 Den Haag and temporary c/o E. M. von Hornbostel, Berlin-Steglitz;
- **`chunk_068:p0060`** — concrete institutional action chain: Van Erp → Westenenk → Koloniaal Instituut → Minister van Koloniën → Governor-General / Raad van Indië, explicitly timed around Huizinga’s *De Gids* article;
- `chunk_068:p0061–0064` — adjacent working notes on music research, publication/open-letter strategy, phonograms, institutes, Stanford, and 1927-style date notations.

This cluster does **not** replace the 1931 anthropology dossier. It materially strengthens the article’s earlier institutional prehistory: dispersed expertise/materials were actively turned into an administrative and publicity sequence, not merely described retrospectively.

### 6. Three exact Malinowski hits are not missing correspondence

`chunk_067:p0070–0072` are *Homo ludens* / Kula discussion and bibliography. They are retained as C-level context and explicitly marked **not correspondence**.

## Repository topology after this checkpoint

The dedicated `Huizinga` repository should now be treated as the canonical corpus/discovery layer.

The older `Edward_Griffith/research_notes/huizinga_malinowski/` tree remains the current article-control and argument layer until its checkpoint/source-control files are migrated or cross-referenced.

Files produced by this scan:

- `analysis/full_corpus_scan_2026-08-20/page_markers_v1_001-035.csv`
- `analysis/full_corpus_scan_2026-08-20/page_markers_v1_036-055.csv`
- `analysis/full_corpus_scan_2026-08-20/page_markers_v1_056-071.csv`
  — three parts of the sparse page-level marker index (341 A/B/C rows total; every page was scanned, unmarked pages omitted from these sparse files);
- `analysis/full_corpus_scan_2026-08-20/chunk_scan_summary_v1.csv` — 001–071 coverage table;
- `analysis/full_corpus_scan_2026-08-20/priority_review_v1.md` — human-readable A/B queue;
- `analysis/full_corpus_scan_2026-08-20/scan_full_corpus_markers.py` — reproducible scanner;
- this checkpoint.

## Research consequence

The V6 body should **not** be changed merely because Rockefeller stationery or labels surfaced.

Current body-entry threshold remains in force. New Leiden material should enter the body only if it materially:

- establishes a direct 1931 Rockefeller decision/transmission mechanism;
- recovers the memorandum/addendum or a materially sharper version of its claims;
- recovers Outhwaite/Van Eerde/Bakhuyzen evaluation language that changes the present Rockefeller reading;
- or supplies another primary source that changes the mechanism rather than only upgrading citation/provenance.

The immediate archival task is now image-first review of A pages, followed by B pages, while preserving the full machine marker layer for later re-ranking.

# review/chunk_023

Full retrieval-grade OCR/page audit and correction layer for `chunk_023:p0001`–`p0187`.

Source scans were checked in five contiguous blocks: 1–40, 41–80, 81–120, 121–160, 161–187. Page-image inspection is used only for OCR quality control, false-empty recovery, layout/reading-order diagnosis, packet/title verification and manuscript-pagination verification. Raw PaddleOCR v3 text is preserved unchanged.

The scan-grounded architecture is: a continuation of chunk 022's `Europ. pol. gesch. rondom 1700` dossier through `p0039`; a contents/folder label at `p0040` reading `Licht & geluid`, `Kern`, `Beteekenisleer`, `Vidūsaka`; a `Licht & geluid / Beteekenisleer` manuscript beginning `Inleiding. pag. 1–19.`; separately labelled `Aanteekeningen Vidūsaka` and `Notities Vidūsaka / Sâhityadarpana etc.` research layers; compound mounted slips/clippings; a scan-verified **64-page paginated `Hendrik Kern` working manuscript/dossier** (`p0132` = manuscript p.1; `p0133` = pp.2–3; `p0164` = p.64); post-manuscript philological/Indological notes; and the printed **`Hendrik Kern, door J. Huizinga`** (Haarlem: H. D. Tjeenk Willink & Zoon, 1899) at `p0176–p0187`.

A major calibration result is that the relation between `p0132–p0164` and the printed biography is demonstrable from the archive, not merely inferred from adjacency. Manuscript `p0137` contains `International Sanskrit Insurance Company` and `Mutual Praise Society`, which recur in printed `p0187`; manuscript `p0155` carries M. de Vries / `Çakuntala` material developed in printed `p0185`; manuscript `p0164` records the 1862 `Çakuntala` translation material, also treated in `p0185`. The safest description remains **working manuscript/dossier**, rather than a line-for-line final printer's copy, until full collation is complete.

The mounted-slip run `p0111–p0129` has now received a dedicated page-by-page visual separation pass. On these scans the recurring `Tentoonstelling`/Bremmer exhibition print is reused support material, while the substantive Huizinga research notes are the handwritten slips mounted beside or over it. The pass records the layout and secure research anchors without pretending to a full diplomatic transcription. `p0123` is an especially strong OCR-displacement case: baseline text is overwhelmingly recycled exhibition print while the scan contains two substantive handwritten research slips. `p0129` closes the run with a conceptual note beginning `deze vaste vergelijkingen zijn door hun veelgebruiktheid tot symbolen geworden` and a slip headed `Spraakwoorden & vergelijkingen`.

Source spellings on packet labels are preserved rather than normalized: `Vidūsaka` and `Sâhityadarpana` are transcribed as visible on the scans.

Files:
- `full_visual_audit_manifest_v1.tsv` — page-level OCR/scan status
- `empty_ocr_visual_review.jsonl` — all baseline-empty pages checked
- `verified_corrections_v1.tsv` — high-confidence scan corrections and recovered labels
- `mounted_slip_scan_pass_p0111-0129_v1.tsv` — page-by-page separation of handwritten research slips from recycled printed support
- `core_theme_hits_v1.md` — documentary/research synthesis
- `review_summary_v1.md` — full audit summary and close-transcription/collation queue
- `status.txt` — completion marker

Raw OCR is preserved unchanged. Corrections live only in this review layer.

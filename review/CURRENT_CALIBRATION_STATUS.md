# Current Huizinga calibration status

Updated: 2026-08-26

This file is the current roll-up. `review/PROGRESS.md` is historical and may lag later calibration rounds.

## Corpus-level status

- `chunk_001`: **retrieval-grade visual audit COMPLETE**.
- `chunk_002`: **retrieval-grade visual / false-empty audit COMPLETE for p0001-p0183**. All three contiguous scan PDFs are aligned; page-level visual coverage and baseline empty/nonempty-signal audit are 183/183 complete. One false-empty recovery is `p0016`. Full line-by-line semantic proofreading of every nonempty OCR string is not claimed. See `review/chunk_002/status.txt`.
- `chunk_003`–`chunk_031`: **retrieval-grade visual review COMPLETE** at the repository's established calibration standard. `COMPLETE` means retrieval-grade visual/OCR correction and triage, not diplomatic transcription.
- `chunk_032`: **OCR-layer second-pass CALIBRATED; visual audit NOT COMPLETE** because the scan set is unavailable to the review layer.
- `chunk_033`: **page-level visual closure COMPLETE: 236/236 pages**. Round 004 supplied and reviewed the two former gaps `p0001-p0040` and `p0161-p0200`. Aggregate visual classes: 152 high-noise, 45 blank/no-substantive, 23 usable-with-noise, 16 short/minimal. New high-resolution blank controls: `p0001`, `p0161`. See `review/chunk_033/review_summary_v3.md`.
- `chunk_034`: **page-level visual closure COMPLETE: 246/246 pages**. Round 006 reviewed the former `p0081-p0120` gap. Reconciled whole-chunk aggregate: 174 high-noise, 55 blank/no-substantive, 13 short/nontext, 4 usable-with-noise. See `review/chunk_034/review_summary_v4.md`.
- `chunk_035`: **page-level visual closure COMPLETE: 231/231 pages**. Whole-chunk aggregate: 137 high-noise, 69 blank/no-substantive, 14 short/nontext, 11 usable-with-noise. See `review/chunk_035/review_summary_v2.md`.
- `chunk_036`: **page-level visual closure COMPLETE: 240/240 pages**. Whole-chunk aggregate: 171 high-noise, 59 blank/no-substantive, 6 short/nontext, 4 usable-with-noise. See `review/chunk_036/review_summary_v2.md`.
- `chunk_037`: **page-level visual closure COMPLETE: 243/243 pages**. Whole-chunk aggregate: 174 high-noise, 61 blank/no-substantive, 1 short/nontext, 7 usable-with-noise. See `review/chunk_037/review_summary_v2.md`.
- `chunk_038`: **page-level visual closure COMPLETE: 226/226 pages**. Whole-chunk aggregate: 150 high-noise, 42 blank/no-substantive, 2 short/nontext, 32 usable-with-noise. See `review/chunk_038/review_summary_v2.md`.
- `chunk_039`: **page-level visual closure COMPLETE: 236/236 pages**. Whole-chunk aggregate: 173 high-noise, 56 blank/no-substantive, 1 short/nontext, 6 usable-with-noise. See `review/chunk_039/review_summary_v2.md`.
- `chunk_040`: **page-level visual closure COMPLETE: 243/243 pages**. Round 011 reviewed `p0001-p0160`; Round 012 supplied and reviewed the tail `p0161-p0243`. Reconciled aggregate: **170 high-noise, 62 blank/no-substantive, 3 short/nontext, 8 usable-with-noise**. Retrieval-stronger exceptions include `p0010`, `p0200-p0201`, `p0207-p0209`, and `p0211-p0212`.
- `chunk_041`: **page-level visual closure COMPLETE: 236/236 pages**. Aggregate: **151 high-noise, 53 blank/no-substantive, 18 short/nontext, 14 usable-with-noise**. Retrieval-stronger packets include `p0133-p0135`, `p0161`, `p0173-p0174`, `p0214`, and `p0219-p0220`. See `review/chunk_041/status.txt`.
- `chunk_042`: **page-level visual closure COMPLETE: 222/222 pages**. Aggregate: **143 high-noise, 42 blank/no-substantive, 16 short/nontext, 21 usable-with-noise**. The strongest sustained retrieval packet is `p0175-p0183`. See `review/chunk_042/status.txt`.
- `chunk_043`: **page-level visual closure COMPLETE: 212/212 pages**. Aggregate: **139 high-noise, 46 blank/no-substantive, 15 short/nontext, 12 usable-with-noise**. The strongest early reading-order exception is `p0016-p0018`; the tail adds `p0202`. See `review/chunk_043/review_summary_v2.md`.
- `chunk_044`: **page-level visual closure COMPLETE: 200/200 pages for the supplied scan set**. Round 017 aggregate: **103 high-noise, 21 blank/no-substantive, 30 short/nontext, 46 usable-with-noise**. The morphology shifts sharply around `p0134-p0139` from dense mounted-slip boards to sparse controls and then larger letters/notebook leaves and internally linear correspondence. See `review/chunk_044/review_summary_v1.md`.

## Continuity statement

`001 ✅ visual | 002 ✅ page-level visual + false-empty closure / semantic OCR proofreading partial | 003–031 ✅ visual | 032 🟡 OCR-calibrated / visual pending | 033–044 ✅ page-level visual closure`

## Five-PDF rounds

- `ROUND_001_5PDF.md`: first scan-calibration batch across chunks 033/034.
- `ROUND_002_5PDF.md`: five PDFs / 263 pages; chunk_002 page-level visual + false-empty closure and additional chunk_034 review.
- `ROUND_003_5PDF.md`: five PDFs / 196 pages; all then-available chunk_033 scans promoted to page-level visual classification and chunk_034 advanced through `p0240`.
- `ROUND_004_5PDF.md`: five PDFs / 166 pages; chunk_033 closed at 236/236, chunk_034 advanced to 206/246 including the final tail, and chunk_035 opened at 40/231.
- `ROUND_005_5PDF.md`: five PDFs / 191 pages; chunk_035 closed at 231/231 page-level visual coverage.
- `ROUND_006_5PDF.md`: five PDFs / 200 pages; chunk_034 closed at 246/246 and chunk_036 advanced through `p0160`.
- `ROUND_007_5PDF.md`: five PDFs / 200 pages; chunk_036 closed at 240/240 and chunk_037 advanced through `p0120`.
- `ROUND_008_5PDF.md`: five PDFs / 163 pages; chunk_037 closed at 243/243 and chunk_038 opened at `p0121-p0160`.
- `ROUND_009_5PDF.md`: five PDFs / 186 pages; chunk_038 closed at 226/226 page-level visual coverage.
- `ROUND_010_5PDF.md`: five PDFs / 200 pages; chunk_039 advanced through `p0200` at 200/236 page-level visual coverage.
- `ROUND_011_5PDF.md`: five PDFs / 196 pages; chunk_039 closed at 236/236 and chunk_040 advanced through `p0160`.
- `ROUND_012_5PDF.md`: five PDFs / 163 pages; chunk_040 tail `p0161-p0243` reviewed and chunk_041 opened through `p0080`.
- `ROUND_013_5PDF.md`: five PDFs / 196 pages; chunk_041 closed at 236/236 and chunk_042 opened through `p0040`.
- `ROUND_014_5PDF.md`: five PDFs / 182 pages; chunk_042 closed at 222/222.
- `ROUND_015_5PDF.md`: five PDFs / 200 pages; chunk_043 advanced through `p0200`.
- `ROUND_016_TAIL.md`: exceptional supplied-tail closure, one PDF / 12 pages; chunk_043 closed at 212/212 without holding the tail for an artificial five-PDF bundle.
- `ROUND_017_5PDF.md`: five PDFs / 200 pages; chunk_044 closed at 200/200 for the supplied scan set.

The operational unit remains five supplied PDFs per completed round. A supplied terminal tail may be closed separately when waiting would create an artificial batch boundary. Raw PaddleOCR JSON files remain unchanged unless a separate correction workflow explicitly writes a corrected derivative.

## High-value chunk_002 anchors retained

The strongest packet begins with `Trois esprits prégothiques < Paris 1930 >` at p0049. Scan-verified anchors include p0086 (`Cet élément ludique` / competition-disputation), p0087 (`primitive` in the same medieval intellectual-history argument), p0089 as catastrophic repeated-number/table OCR pathology control, and p0090 placing Abélard not simply as a Renaissance precursor but `au contraire comme un prégothique`.

## Next closure priorities

1. Continue with the next five supplied PDFs, beginning `chunk_045:p0001-p0200`.
2. Close chunk_032 visually when scans become available.
3. Perform exhaustive nonempty OCR-string semantic proofreading only where full OCR-usability closure, rather than retrieval-grade visual calibration, is actually required.

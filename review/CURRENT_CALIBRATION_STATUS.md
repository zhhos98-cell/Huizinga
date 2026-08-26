# Current Huizinga calibration status

Updated: 2026-08-26

This file is the current roll-up. `review/PROGRESS.md` is historical and may lag later calibration rounds.

## Corpus-level status

- `chunk_001`: **retrieval-grade visual audit COMPLETE**.
- `chunk_002`: **retrieval-grade visual / false-empty audit COMPLETE for p0001-p0183**. All three contiguous scan PDFs are aligned; page-level visual coverage and baseline empty/nonempty-signal audit are 183/183 complete. One false-empty recovery is `p0016`. Full line-by-line semantic proofreading of every nonempty OCR string is not claimed. See `review/chunk_002/status.txt`.
- `chunk_003`–`chunk_031`: **retrieval-grade visual review COMPLETE** at the repository's established calibration standard. `COMPLETE` means retrieval-grade visual/OCR correction and triage, not diplomatic transcription.
- `chunk_032`: **OCR-layer second-pass CALIBRATED; visual audit NOT COMPLETE** because the scan set is unavailable to the review layer.
- `chunk_033`: **page-level visual closure COMPLETE: 236/236 pages**. Round 004 supplied and reviewed the two former gaps `p0001-p0040` and `p0161-p0200`. Aggregate visual classes: 152 high-noise, 45 blank/no-substantive, 23 usable-with-noise, 16 short/minimal. New high-resolution blank controls: `p0001`, `p0161`. See `review/chunk_033/review_summary_v3.md`.
- `chunk_034`: **page-level visual coverage 206/246** covering `p0001-p0080` and `p0121-p0246`. Round 004 reviewed `p0161-p0200` plus `p0241-p0246`. Only `p0081-p0120` remains unavailable/unreviewed. New high-resolution blank controls: `p0198`, `p0242`. See `review/chunk_034/review_summary_v3.md`.
- `chunk_035`: **page-level visual coverage 40/231** for `p0001-p0040`. The remaining five supplied scan PDFs are queued and can form the next complete five-PDF round. No indexed chunk_035 raw OCR file was found in the repository during this pass. See `review/chunk_035/review_summary_v1.md`.

## Continuity statement

`001 ✅ visual | 002 ✅ page-level visual + false-empty closure / semantic OCR proofreading partial | 003–031 ✅ visual | 032 🟡 OCR-calibrated / visual pending | 033 ✅ 236/236 visual closure | 034 🟢 206/246 visual / one 40-page gap | 035 🟢 40/231 visual`

## Five-PDF rounds

- `ROUND_001_5PDF.md`: first scan-calibration batch across chunks 033/034.
- `ROUND_002_5PDF.md`: five PDFs / 263 pages; chunk_002 page-level visual + false-empty closure and additional chunk_034 review.
- `ROUND_003_5PDF.md`: five PDFs / 196 pages; all then-available chunk_033 scans promoted to page-level visual classification and chunk_034 advanced through `p0240`.
- `ROUND_004_5PDF.md`: five PDFs / 166 pages; chunk_033 closed at 236/236, chunk_034 advanced to 206/246 including the final tail, and chunk_035 opened at 40/231.

The operational unit remains five supplied PDFs per completed round. A round may cross chunk boundaries. Raw PaddleOCR JSON files remain unchanged unless a separate correction workflow explicitly writes a corrected derivative.

## High-value chunk_002 anchors retained

The strongest packet begins with `Trois esprits prégothiques < Paris 1930 >` at p0049. Scan-verified anchors include p0086 (`Cet élément ludique` / competition-disputation), p0087 (`primitive` in the same medieval intellectual-history argument), p0089 as catastrophic repeated-number/table OCR pathology control, and p0090 placing Abélard not simply as a Renaissance precursor but `au contraire comme un prégothique`.

## Next closure priorities

1. Run the next five-PDF round on the five remaining supplied chunk_035 segments: `p0041-p0080`, `p0081-p0120`, `p0121-p0160`, `p0161-p0200`, `p0201-p0231`.
2. Obtain or supply `chunk_034:p0081-p0120` to close chunk_034 visually.
3. Close chunk_032 visually when scans become available.
4. Locate/add the chunk_035 raw OCR layer before any OCR-string correction pass.
5. Perform exhaustive nonempty OCR-string semantic proofreading only where full OCR-usability closure, rather than retrieval-grade visual calibration, is actually required.

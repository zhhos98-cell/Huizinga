# Current Huizinga calibration status

Updated: 2026-08-26

This file is the current roll-up. `review/PROGRESS.md` is historical and may lag later calibration rounds.

## Corpus-level status

- `chunk_001`: **retrieval-grade visual audit COMPLETE**.
- `chunk_002`: **retrieval-grade visual / false-empty audit COMPLETE for p0001-p0183**. All three contiguous scan PDFs are aligned; page-level visual coverage and baseline empty/nonempty-signal audit are 183/183 complete. One false-empty recovery is `p0016`. Full line-by-line semantic proofreading of every nonempty OCR string is not claimed. See `review/chunk_002/status.txt`.
- `chunk_003`–`chunk_031`: **retrieval-grade visual review COMPLETE** at the repository's established calibration standard. `COMPLETE` means retrieval-grade visual/OCR correction and triage, not diplomatic transcription.
- `chunk_032`: **OCR-layer second-pass CALIBRATED; visual audit NOT COMPLETE** because the scan set is unavailable to the review layer.
- `chunk_033`: **page-level visual closure COMPLETE: 236/236 pages**. Round 004 supplied and reviewed the two former gaps `p0001-p0040` and `p0161-p0200`. Aggregate visual classes: 152 high-noise, 45 blank/no-substantive, 23 usable-with-noise, 16 short/minimal. New high-resolution blank controls: `p0001`, `p0161`. See `review/chunk_033/review_summary_v3.md`.
- `chunk_034`: **page-level visual closure COMPLETE: 246/246 pages**. Round 006 reviewed the former `p0081-p0120` gap. Reconciled whole-chunk aggregate: 174 high-noise, 55 blank/no-substantive, 13 short/nontext, 4 usable-with-noise (the high-resolution `p0073` blank control supersedes its older row-manifest short-text label). New higher-resolution controls in the gap: `p0111` short/minimal and `p0112` blank/no-substantive. See `review/chunk_034/review_summary_v4.md`.
- `chunk_035`: **page-level visual closure COMPLETE: 231/231 pages**. Round 005 reviewed the remaining five supplied segments (`p0041-p0231`, 191 pages). Whole-chunk aggregate: 137 high-noise, 69 blank/no-substantive, 14 short/nontext, 11 usable-with-noise. New high-resolution blank controls: `p0128`, `p0209`. No indexed chunk_035 raw OCR file was found, so this is visual/layout closure rather than OCR-string correction. See `review/chunk_035/review_summary_v2.md`.
- `chunk_036`: **page-level visual closure COMPLETE: 240/240 pages**. Round 007 reviewed the remaining `p0161-p0240` segments (80 pages). Whole-chunk aggregate: 171 high-noise, 59 blank/no-substantive, 6 short/nontext, 4 usable-with-noise. See `review/chunk_036/review_summary_v2.md`.
- `chunk_037`: **page-level visual closure COMPLETE: 243/243 pages**. Round 008 reviewed the remaining `p0121-p0243` span. Whole-chunk aggregate: 174 high-noise, 61 blank/no-substantive, 1 short/nontext, 7 usable-with-noise. The retrieval-stronger packet remains `p0058` and `p0112-p0117`; a new higher-resolution short/nontext control is `p0218`. No indexed chunk_037 raw OCR file was found in the current repository search. See `review/chunk_037/review_summary_v2.md`.
- `chunk_038`: **page-level visual closure COMPLETE: 226/226 pages**. Round 009 reviewed the five remaining supplied segments (186 pages). Whole-chunk aggregate: 150 high-noise, 42 blank/no-substantive, 2 short/nontext, 32 usable-with-noise. The strongest sustained retrieval packet is `p0100-p0120`, with additional usable exceptions at `p0055`, the Round 008 packet `p0121-p0122`, `p0125-p0126`, `p0130-p0133`, and `p0191`, `p0196`. Short/nontext controls are `p0013` and `p0127`; higher-resolution blank controls include `p0179-p0180`. No indexed chunk_038 raw OCR file was found in the current repository search. See `review/chunk_038/review_summary_v2.md`.
- `chunk_039`: **page-level visual closure COMPLETE: 236/236 pages**. Round 011 reviewed the final `p0201-p0236` tail. Whole-chunk aggregate: 173 high-noise, 56 blank/no-substantive, 1 short/nontext, 6 usable-with-noise. Retrieval exceptions are `p0026`, `p0066`, `p0111`, `p0126`, `p0169`, and tail control `p0209`; `p0224` is the short/nontext envelope/file-object control and `p0092` remains a blank/no-substantive control. No indexed chunk_039 raw OCR file was found in the current repository search. See `review/chunk_039/review_summary_v2.md`.
- `chunk_040`: **page-level visual coverage 160/243** covering `p0001-p0160`. Round 011 opens the chunk with 119 high-noise, 40 blank/no-substantive, 0 short/nontext, and 1 usable-with-noise page. `p0010` is the clearest retrieval-stronger exception in the opening span. No indexed chunk_040 raw OCR file was found in the current repository search. Remaining supplied span: `p0161-p0243`. See `review/chunk_040/review_summary_v1.md`.

## Continuity statement

`001 ✅ visual | 002 ✅ page-level visual + false-empty closure / semantic OCR proofreading partial | 003–031 ✅ visual | 032 🟡 OCR-calibrated / visual pending | 033 ✅ 236/236 visual closure | 034 ✅ 246/246 visual closure | 035 ✅ 231/231 visual closure | 036 ✅ 240/240 visual closure | 037 ✅ 243/243 visual closure | 038 ✅ 226/226 visual closure | 039 ✅ 236/236 visual closure | 040 🟢 160/243 visual`

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

The operational unit remains five supplied PDFs per completed round. A round may cross chunk boundaries. Raw PaddleOCR JSON files remain unchanged unless a separate correction workflow explicitly writes a corrected derivative.

## High-value chunk_002 anchors retained

The strongest packet begins with `Trois esprits prégothiques < Paris 1930 >` at p0049. Scan-verified anchors include p0086 (`Cet élément ludique` / competition-disputation), p0087 (`primitive` in the same medieval intellectual-history argument), p0089 as catastrophic repeated-number/table OCR pathology control, and p0090 placing Abélard not simply as a Renaissance precursor but `au contraire comme un prégothique`.

## Next closure priorities

1. Finish the remaining supplied chunk_040 tail (`p0161-p0200`, `p0201-p0240`, `p0241-p0243`; 83 pages) in the next cross-chunk round once two further PDFs are supplied, preserving the five-PDF operational unit.
2. Continue into the next chunk as soon as those two companion PDFs are available.
3. Close chunk_032 visually when scans become available.
4. Locate/add the chunk_035 raw OCR layer only if OCR-string correction is required beyond retrieval-grade visual closure.
5. Perform exhaustive nonempty OCR-string semantic proofreading only where full OCR-usability closure, rather than retrieval-grade visual calibration, is actually required.

# Current Huizinga calibration status

Updated: 2026-08-26

This file is the current roll-up. `review/PROGRESS.md` is historical and may lag later calibration rounds.

## Corpus-level status

- `chunk_001`: **retrieval-grade visual audit COMPLETE**.
- `chunk_002`: **retrieval-grade visual / false-empty audit COMPLETE for p0001-p0183**. All three contiguous scan PDFs are aligned; page-level visual coverage and baseline empty/nonempty-signal audit are 183/183 complete. One false-empty recovery is `p0016`. Full line-by-line semantic proofreading of every nonempty OCR string is not claimed. See `review/chunk_002/status.txt`.
- `chunk_003`–`chunk_031`: **retrieval-grade visual review COMPLETE** at the repository's established calibration standard. `COMPLETE` means retrieval-grade visual/OCR correction and triage, not diplomatic transcription.
- `chunk_032`: **OCR-layer second-pass CALIBRATED; visual audit NOT COMPLETE** because the scan set is unavailable to the review layer.
- `chunk_033`: **page-level visual classification COMPLETE for all currently available scans: 156/156 available pages** covering `p0041-p0160` and `p0201-p0236`. Missing scans `p0001-p0040` and `p0161-p0200` still prevent whole-chunk closure. New high-resolution blank controls: `p0094`, `p0123`, `p0204`. See `review/chunk_033/page_visual_run_manifest_available_spans_v1.tsv` and `review_summary_v2.md`.
- `chunk_034`: **page-level visual coverage 160/246** covering `p0001-p0080`, `p0121-p0160`, and `p0201-p0240`. Missing scans remain `p0081-p0120` and `p0161-p0200`. The locally available six-page tail `p0241-p0246` is not yet reviewed. New high-resolution blank control: `p0201`; sparse nonblank control: `p0217`.

## Continuity statement

`001 ✅ visual | 002 ✅ page-level visual + false-empty closure / semantic OCR proofreading partial | 003–031 ✅ visual | 032 🟡 OCR-calibrated / visual pending | 033 🟢 156/156 available-page visual complete / two scan gaps | 034 🟢 160/246 page-level visual`

## Five-PDF rounds

- `ROUND_001_5PDF.md`: first scan-calibration batch across chunks 033/034.
- `ROUND_002_5PDF.md`: five PDFs / 263 pages; chunk_002 page-level visual + false-empty closure and additional chunk_034 review.
- `ROUND_003_5PDF.md`: five PDFs / 196 pages; all available chunk_033 scans promoted to page-level visual classification and chunk_034 advanced through `p0240`.

The operational unit remains five supplied PDFs per completed round. A round may cross chunk boundaries. Raw PaddleOCR JSON files remain unchanged; corrections, controls and confidence limits live in `review/`.

## High-value chunk_002 anchors retained

The strongest packet begins with `Trois esprits prégothiques < Paris 1930 >` at p0049. Scan-verified anchors include p0086 (`Cet élément ludique` / competition-disputation), p0087 (`primitive` in the same medieval intellectual-history argument), p0089 as catastrophic repeated-number/table OCR pathology control, and p0090 placing Abélard not simply as a Renaissance precursor but `au contraire comme un prégothique`.

## Next closure priorities

1. Continue the five-PDF workflow. The immediate locally available tail is `chunk_034__p0241-0246.pdf`; it can be grouped with the next four supplied PDFs.
2. Obtain or supply `chunk_033:p0001-p0040` and `p0161-p0200` to close chunk_033 visually.
3. Obtain or supply `chunk_034:p0081-p0120` and `p0161-p0200` to close the major chunk_034 scan gaps.
4. Close chunk_032 visually when scans become available.
5. Perform exhaustive nonempty OCR-string semantic proofreading only where full OCR-usability closure, rather than retrieval-grade visual calibration, is actually required.

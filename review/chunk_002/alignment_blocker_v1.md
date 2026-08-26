# chunk_002 absolute page-alignment blocker

## Purpose

This note records why the substantive OCR anchors in `chunk_002` are currently indexed by stable raw-source anchors rather than by guessed `pXXXX` page IDs.

## What is secure

- The repository contains the raw file `chunk_002.pdf_by_PaddleOCR-VL-1.6.json` (blob SHA `8f18ee80abe94170255c4f1955d833ce4db96b3d`).
- The raw OCR has been substantively reviewed and several coherent historical/conceptual packets have been identified.
- Stable raw-source anchors (including OCR result UUIDs) can be used to return to the relevant records.
- A scan segment named `/Huizinga/chunk_002_123-183.pdf` is confirmed in the File Library.

## Why `pXXXX` is not assigned yet

In the current connector environment the large raw JSON is exposed through wrapped/truncated response objects and semantic snippets rather than as a clean, locally parseable ordered JSON array. Repeated wrapper content means that counts of strings such as `inputImage` or suffixes such as `input_img_N.jpg` are **not a safe substitute for array index or archival page number**.

An earlier provisional count derived from connector `inputImage` matches was therefore rejected and is not used anywhere in the review layer.

The confirmed PDF segment could not be read/materialized in the current environment, so it cannot yet be used to align the OCR records visually.

## Interim indexing rule

Until ordered-array access or scan matching is available:

1. Use the source anchors in `ocr_anchor_index_v1.tsv` for retrieval.
2. Do not fabricate absolute `pXXXX` values from search-result order, wrapper order, UUID order, or `input_img_N` suffixes.
3. Do not create page-class totals, empty/false-empty resolutions, or a full visual manifest.
4. Exact quotation, authorship assignment, and documentary-form claims remain scan-dependent.

## Acceptable resolution paths

Absolute page alignment can be closed by either of the following:

- obtain the raw JSON as a directly materializable/local ordered file and enumerate its top-level OCR records; or
- obtain working visual access to the scans and match stable OCR/source anchors to physical page sequence.

Once alignment is recovered, convert the source-anchor index to canonical `pXXXX`, then perform the normal page-level visual audit used for completed Huizinga chunks.

## Priority anchors after alignment

The first pages to map and visually verify should be the Abélard/Héloïse/twelfth-century complex containing `élément ludique`, tournament/disputation imagery, `primitive`, the twelfth-century `Renaissance` discussion, and the `prégothique` characterization. After that, map the Zeeland/Middelburg, Salimbene/Ezzelino, and Florence complexes.

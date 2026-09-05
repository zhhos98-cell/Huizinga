# Session handoff — 2026-09-05 13:35 +08:00

Purpose: compact restart point for the next Huizinga session. Do not reopen searches already bounded below.

## What changed this session

1. **1933 KNAW scene sharpened in Draft 04.** Huizinga's 23 May 1933 line, `Being no anthropologist I refrained from taking a leading part in your candidature`, is now controlled against his institutional office: he had been president/chair of the KNAW Afdeeling Letterkunde since **11 November 1929**. Article-facing implication: the self-limitation is disciplinary despite senior Academy office, not institutional marginality. Do not infer that the presidency proves he formally led, nominated, or controlled Malinowski's candidature.

2. **KNAW archive route moved from repository-level to item/index-level.** Relevant old archive: **Noord-Hollands Archief, toegang 64**, KNAW Amsterdam ((1838) 1851–1940 (1954)). Current OpenData control: public/CC0 EAD, 852 placement-list numbers; permanent page displays last modified **14 July 2024**. Earlier 2026-07-06 parse was corrected and must not be reused.

3. **First direct membership locator:** toegang 64, **inv. 569, `Benoemingen van leden van de afdeling letterkunde 1855–1940`**. Status PRIORITY/PARTIAL: title/date range are secure; dossier has not been inspected, so foreign-member/Malinowski coverage remains unproved.

4. **Legacy index route recovered from the later KNAW archive:** **inv. 1462–1466** indexes minute books back to 1925 and records Roman minute-book volume + Arabic page; **inv. 1464 = J–O**, therefore the first box to inspect for a `Malinowski` card. **inv. 1468–1471** indexes old archive dossiers back to 1925; **inv. 1470 = M–R**, therefore first dossier-index box for Malinowski/membership/candidature. These are index locators only; card contents remain uninspected.

5. Preferred KNAW archive-pull order is now: (a) toegang 64 inv. 569; (b) later archive inv. 1464 under Malinowski/relevant membership headings; (c) inv. 1470; (d) exact old minute book/dossier exposed by those indexes. **Do not return to broad `Malinowski + KNAW` web searching.**

6. **Ahlbrinck control remains unchanged:** 15 Sep 1931 dispatch = *Encyclopaedie der Karaïben* is HIGHLY PROBABLE / NOTE-PARTIAL, not certain. Secure downstream evidence is Malinowski's 4 Oct thanks for the *Encyclopaedia of the Karibs* and its use by a pupil studying couvade. Reopen only with full Yale letter body or independent dispatch/presentation evidence.

7. **1926/1927 Sex and Repression remains a state-identification problem.** A 1926 *Crime and Custom* footnote itself points to forthcoming/companion *Sex and Repression in Savage Society (1926)*, which strengthens contemporaneous intended/imprint chronology but does not establish ordinary commercial publication in 1926. Keep the controlled sequence already in AGENTS/research notes; do not normalize to a secure 1926 edition.

8. **Leiden shelfmark pass started but not closed.** Existing secure mappings remain H.A. 34 II = `Oldindian medicine`; H.A. 27 = `Bourgondische cultuur` (esp. env. Iconographie); H.A. 29 II.1 = 1930 `Aperçu de la civilisation hollandaise du XVIIe siècle`. Still unresolved: Renaissance packet `chunk_028:p0183`; American cards/prose `chunk_018:p0198–p0238`; `Trois esprits prégothiques` in `chunk_002`; history/science cards `chunk_020:p0201–p0204`; American itinerary `chunk_019:p0031`; `Ridderspelen als beleving der Feodaltijd` `chunk_013:p0142`. A possible route is UBL/Huizinga formal inventory plus digitized `HUI xx` objects mirrored on Wikimedia Commons; use exact title/object evidence and **do not infer H.A. numbers from chronological or chunk adjacency**.

## Repo state / important commits

- `92568ff6` — Draft 04 KNAW presidency/disciplinary-limit patch landed.
- `6efe401f`, `ffedb982` — KNAW archive locator/OpenData controls.
- `3596d9ff` — Huizinga presidency control note.
- `b532a634` — AGENTS KNAW inv. 569 + presidency control.
- `8bf23746` then `0ead07ab` — AGENTS legacy-index route successfully applied after workflow repair.

Some temporary patch workflows had failed during YAML/guard iteration; the substantive canonical files above were subsequently verified and the final AGENTS legacy-index workflow run succeeded. Treat the canonical file contents, not intermediate workflow failures, as state.

## Canonical restart files

- `AGENTS.md`, especially §§12 and 19.
- `research/article_knaw_malinowski_1933_membership_mechanics_recheck_2026-09-05.md` — full KNAW control and archive-pull order.
- `research/article_leiden_archive_locator_mapping_2026-09-05.md` — secure Leiden mappings + unresolved list.
- `research/article_ahlbrinck_dispatch_recheck_2026-09-05.md`.
- `research/article_sex_repression_imprint_1926_1927_recheck_2026-09-05.md`.
- canonical `writing/benevolent_outsider_draft_04...` files; do not regenerate whole draft.

## Best next move

First inspect whether any online/digitized surrogate or exact catalogue citation can expose **KNAW inv. 569 / legacy index 1464 / 1470**; if not, leave KNAW as an explicit archive-pull dependency and spend the next web/repo pass on the unresolved Leiden formal mappings using exact manuscript titles and UBL `HUI` object identifiers. Patch body prose only when a recovered locator or primary source changes an article-level claim; otherwise update notes/control logs and AGENTS.

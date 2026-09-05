# Leiden Huizinga archive locator mapping for Draft 04 — 2026-09-05

_Status: bounded publication-QA mapping. This file converts only article-used `review/chunk_*` audit pointers that can be matched securely to formal Leiden Huizinga archive inventory units. It does **not** attempt a 71-chunk corpus-wide concordance._

## Why this pass is necessary

The repository's `review/chunk_*` references are internal digital-corpus coordinates. They are valuable because they preserve page-level auditability, but they are not Leiden University Libraries shelfmarks or inventory numbers. Publication notes should therefore cite the formal Huizinga archive unit where it can be established, while retaining the internal chunk/page pointer as a secondary audit coordinate.

The Huizinga archive was inventoried by Anton van der Lem in *Inventaris van het archief van Johan Huizinga – Bibliografie 1897–1997* (Leiden University Library, Codices manuscripti 29, 1998). Huizinga Online's current calendar and later scholarship use `H.A.` / `Huizinga archive` followed by those inventory numbers.

## Secure mappings used by Draft 04

### 1. Old Indian medicine — Draft [^3]

**Formal unit:** `Huizinga archive, no. 34 II: Oldindian medicine`.

Anton van der Lem's 2019 archive study identifies no. 34 II explicitly as `Oldindian medicine` and describes the surviving envelopes/slips. This matches the Indian medicine/Sanskrit materials currently audited in `review/chunk_025` and `review/chunk_026:p0029–p0033`.

Article rule:

- cite `Leiden University Libraries, Huizinga archive, no. 34 II`;
- retain `review/chunk_025` / `chunk_026:p0029–p0033` only as internal audit pointers;
- do **not** extend no. 34 II to the separate Renaissance packet at `chunk_028:p0183`.

Source control: Anton van der Lem, `The Making of The Autumn of the Middle Ages II: Huizinga's Archives and Books`, in *Rereading Huizinga* (Amsterdam University Press, 2019), archive note identifying `Huizinga archive, no. 34 II: Oldindian medicine`.

### 2. Philip the Good / Burgundian dossier — Draft [^10]

**Formal unit:** `Huizinga archive, no. 27` (`Bourgondische cultuur`), with the portrait-photograph sequence specifically in `env. Iconographie`.

The mapping is independently controlled in two ways:

- Huizinga Online's calendar records 23 November 1929: Huizinga orders photographs of portraits of Philip the Good in Lille, Gotha, Madrid, Antwerp and Paris, with the locator `[H.A. 27, env. Iconographie]`.
- Scholarship on Huizinga cites `LUB, 27: Bourgondische cultuur, 1–2` for the Burgundian material.

This precisely matches the late `chunk_017` dossier, where the audit finds portrait comparison, the Gotha photograph request, photographic invoices, payment records and autograph-letter correction material.

Article rule:

- cite `Leiden University Libraries, Huizinga archive, no. 27, esp. env. Iconographie`;
- retain `review/chunk_017` as internal audit pointer.

### 3. 1930 French Dutch-civilization lecture — part of Draft [^11]

**Formal unit:** `Huizinga archive, no. 29 II.1`.

Christophe de Voogd identifies Huizinga's `Aperçu de la civilisation hollandaise du XVIIe siècle`, delivered 18 March 1930, as a manuscript of 122 folios in `AH 29, II, 1`. This corresponds directly to `review/chunk_020:p0001–p0115`, whose first page bears the same title and whose audit identifies a continuous French lecture manuscript.

Article rule:

- for the body sentence about the 1930 Dutch-civilization lecture and its social/economic/political/ethnographic explanatory conditions, cite `Leiden University Libraries, Huizinga archive, no. 29 II.1` plus the internal pointer `review/chunk_020:p0001–p0012`;
- do **not** apply no. 29 II.1 to the later `chunk_020:p0201–p0204` history/science cards. The chunk itself becomes a heterogeneous mounted-card zone after p0176, and no formal inventory-level mapping for those cards has yet been restored.

Source control: Christophe de Voogd, *Le miroir de la France: Johan Huizinga et les historiens français* (Leiden University dissertation, 2013), chapter 6, note identifying the 122-folio manuscript as `AH 29, II, 1`.

## Negative control recovered for the Paris 1930 lectures

Huizinga Online's *Kalendarium* records the Paris teaching run as `16-9 april: colleges in Parijs [Brw. 849, 851] (bibl.nr. 200) [H.A. 1, inv.p. 10]` under March 1930. This securely controls the **event chronology** of the Paris colleges and a calendar/inventory-page reference.

It does **not** securely map the surviving `Trois esprits prégothiques` manuscript packet in `review/chunk_002` to `H.A. 1`. The bracketed `H.A. 1, inv.p. 10` is attached in the calendar to the biographical/event entry, and no exact-title inventory evidence has yet shown that the lecture manuscript itself belongs to that unit.

Article / agent rule:

- use the calendar entry to control the Paris teaching chronology if needed;
- do **not** convert `[H.A. 1, inv.p. 10]` into a manuscript shelfmark for `Trois esprits prégothiques`;
- keep the manuscript's formal Leiden mapping unresolved until an exact inventory title, digital-object label, or equivalent item-level source is recovered.

Source control: Anton van der Lem, *Kalendarium van gebeurtenissen in het leven van Johan Huizinga* (Leiden University Libraries digital calendar), March 1930 entry.

## America materials: H.A. 28 is now a secure family locator, not yet a chunk-level mapping

The America branch can now be narrowed materially without overclaiming the exact article-used pages.

Huizinga Online's calendar repeatedly assigns America teaching/material to **H.A. 28 / HUI 28**: the 1920 entry flags `[H.A. 28: herdenking 300 j. Mayflower ...]`, the 1925–26 America course is cited as `[H.A. 28]`, and the 18 September 1940 lecture entry reads `coll. 1: Amerika [HUI 28]`. This makes H.A. 28 a secure **America-family locator**.

A stronger subunit control comes from Thor Rydin's direct use of the Leiden Huizinga Archive. Rydin quotes the wartime-America note `Juist nu niets belangrijker dan Amerika. [...] In ieder geval geweldige invloed te wachten. En wat weten wij ervan?` as **`HA: 28 III 7`**. This proves that at least one concrete America research-note unit sits at H.A. 28 III 7.

This still does **not** identify the article-used `review/chunk_018:p0198–p0238` card montage/synthetic prose, or `review/chunk_019:p0031` itinerary, with H.A. 28 III 7. An exact phrase search against the currently exposed `chunk_018` OCR did not recover Rydin's quoted sentence; the article-used material also includes later/other American research layers. Therefore:

- **H.A. 28 = SECURE family-level locator for Huizinga's America materials**;
- **H.A. 28 III 7 = SECURE item/subunit locator for the specific Rydin-quoted America note**;
- mapping either `chunk_018:p0198–p0238` or `chunk_019:p0031` to H.A. 28 III 7 remains **UNCONTROLLED** until page/object identity is established;
- article notes must not collapse family-level provenance into an exact shelfmark.

Source control: Huizinga Online, *Kalendarium* entries for 1920, 1925–26 and 18 September 1940; Thor Rydin, *The Works and Times of Johan Huizinga (1872–1945): Writing History in the Age of Collapse* (Amsterdam University Press, 2024), chapter 4, p. 147 n. 9, citing `HA: 28 III 7`.

## `Trois esprits`: HUI 31 / HUI 32 removed from the candidate pool

The Wikimedia Commons mirror exposes machine-titled Leiden objects under nearby formal numbers, including `HUI 31 I 1`, `HUI 31 III 2.1`, `HUI 31 III 3.2`, `HUI 32 II 2` and `HUI 32 II 4.2`. Their filenames and persistent Leiden item IDs are useful retrieval handles, but the Commons metadata do not supply human content titles.

The *Kalendarium* now gives a substantive negative control against using those numbers as convenient candidates for the 1930 `Trois esprits prégothiques` packet:

- **H.A. 31** is used for the `Restauratie` course (`coll. 19: Restauratie ... [H.A. 31]`);
- **H.A. 32** is used for `Duitsche Rijk 1648–1688` and later `Europa politiek rond 1700` course material.

Accordingly, nearby-number reasoning from the securely mapped H.A. 29 II.1 lecture manuscript is invalid. HUI 31/32 objects are **not admissible `Trois esprits` candidates merely by numerical/chronological adjacency**. Reintroduce a HUI 31/32 subitem only if an exact-title catalogue description or direct page-level visual identity independently proves the match.

The identity of the `chunk_002` packet itself remains secure on internal scan evidence: its title card/manuscript identifies `Trois esprits prégothiques < Paris 1930 >`, and Huizinga's later published account says that in spring 1930 he assembled three Paris lectures under that title around Abaelard, John of Salisbury and Alanus of Lille. What remains unresolved is only the **formal Leiden shelfmark**.

## Source-resolution method to reuse

The repository already contains a strict precedent in `review/chunk_071/SOURCE_RESOLUTION_V2.md`: a Commons `HUI` PDF was accepted only after resolving the exact Leiden/Commons object and visually comparing source pages against repository OCR pages. Apply the same standard here.

For unresolved Leiden mappings, the preferred order is therefore:

1. recover an exact-title inventory or collection-guide description if possible;
2. otherwise identify a plausible Commons `HUI` object from item-level metadata;
3. compare actual source pages against the repository chunk at page level;
4. only then promote a chunk coordinate to a formal HUI/H.A. shelfmark.

Machine filenames, date proximity, inventory-number adjacency and thematic plausibility alone earn no mapping credit.

## Still unresolved: do not guess

The following article-used internal coordinates still lack a secure formal inventory mapping in the present control:

1. **Renaissance packet** — `review/chunk_028:p0183`, currently part of [^3]. No. 34 II does not cover this separate item.
2. **American travel/research cards and comparative prose** — `review/chunk_018:p0198–p0238`, [^8]. H.A. 28 is now a secure America-family locator, but the exact H.A. 28 subunit for these pages remains unresolved.
3. **`Trois esprits prégothiques` manuscript** — `review/chunk_002`, ms. pp. 31–35, [^9]. The 1930 Paris lecture identity/chronology is secure; `[H.A. 1, inv.p. 10]` is event-level, and HUI 31/32 are not admissible adjacency guesses.
4. **History/science working cards** — `review/chunk_020:p0201–p0204`, part of [^11]. These are distinct from the formal `Aperçu` manuscript no. 29 II.1.
5. **American itinerary** — `review/chunk_019:p0031`, part of [^2]. The Rockefeller report now has its own exact RAC locator; H.A. 28 is the relevant Leiden family, but the exact subunit remains unresolved.
6. **`Ridderspelen als beleving der Feodaltijd`** — `review/chunk_013:p0142`. The mounted-slip title is scan-secure, but no formal Huizinga-archive unit is yet controlled.

Internal chunk coordinates should remain in the working draft until their formal mapping is found; they preserve auditability and are preferable to an invented shelfmark.

## Draft-facing decision

Patch only [^3], [^10] and [^11] on the basis of secure exact mappings already recovered:

- [^3] gains `Huizinga archive, no. 34 II` for Indian medicine while leaving the Renaissance packet separately unresolved;
- [^10] gains `Huizinga archive, no. 27, esp. env. Iconographie`;
- [^11] is split conceptually inside the note: the 1930 French lecture is no. 29 II.1, while the separate history/science working cards retain their internal page pointer and an explicit unresolved formal mapping.

The H.A. 28 family/subunit finding and the `Trois` negative controls do **not** yet warrant a Draft 04 body or footnote shelfmark patch. They narrow the search and prevent false precision.
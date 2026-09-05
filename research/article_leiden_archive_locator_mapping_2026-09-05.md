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

## Still unresolved: do not guess

The following article-used internal coordinates still lack a secure formal inventory mapping in the present control:

1. **Renaissance packet** — `review/chunk_028:p0183`, currently part of [^3]. No. 34 II does not cover this separate item.
2. **American travel/research cards and comparative prose** — `review/chunk_018:p0198–p0238`, [^8]. Do not equate these automatically with other inventory items for Huizinga's American lectures or sent `American notes`.
3. **`Trois esprits prégothiques` manuscript** — `review/chunk_002`, ms. pp. 31–35, [^9]. The 1930 Paris lecture chronology is secure; the calendar's `[H.A. 1, inv.p. 10]` is an event-level locator, not yet a manuscript shelfmark.
4. **History/science working cards** — `review/chunk_020:p0201–p0204`, part of [^11]. These are distinct from the formal `Aperçu` manuscript no. 29 II.1.
5. **American itinerary** — `review/chunk_019:p0031`, part of [^2]. The Rockefeller report now has its own exact RAC locator, but the Leiden itinerary page still needs a formal Huizinga-archive mapping if publication requires one.

Internal chunk coordinates should remain in the working draft until their formal mapping is found; they preserve auditability and are preferable to an invented shelfmark.

## Draft-facing decision

Patch only [^3], [^10] and [^11]:

- [^3] gains `Huizinga archive, no. 34 II` for Indian medicine while leaving the Renaissance packet separately unresolved;
- [^10] gains `Huizinga archive, no. 27, esp. env. Iconographie`;
- [^11] is split conceptually inside the note: the 1930 French lecture is no. 29 II.1, while the separate history/science working cards retain their internal page pointer and an explicit unresolved formal mapping.

No body prose changes are warranted by this locator pass.

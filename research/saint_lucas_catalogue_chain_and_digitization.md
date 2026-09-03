# Saint Lucas Society catalogue chain, archive files, and digitization status

_Status: active provenance lead, synced 2026-09-03._

## 1. Direct Saint Lucas Society archive file: Nationaal Archief inv. 836

Nationaal Archief, Collectie 548 Vosmaer (access 2.21.271), contains a direct business/organizational file for C.J.J.G. Vosmaer's Saint Lucas Society:

- **inv. 836**: `Stukken betreffende de werkzaamheden van Carel J.J.G. Vosmaer als directeur van de "St. Lucas Society, archief voor Genealogiese Documentatie" te Leiden. 1947 en z.j. 1 omslag.`

This is currently a higher-priority target than generic family papers because its date and institutional description overlap directly with the postwar period in which Saint Lucas Society Catalogue 3, *Wetenschappelijke adversaria*, appeared. The online Nationaal Archief record currently indicates reading-room consultation (`Bekijken: studiezaal`); no public scan of inv. 836 has yet been located.

Source: Nationaal Archief finding aid, Collectie 548 Vosmaer, 2.21.271, inv. 836.

## 2. Correct digital-image test: EAD DAO/METS, not the generic viewer shell

Nationaal Archief's open-data documentation explains the machine-readable test for genuine digitization. In an EAD/XML finding aid, an inventory unit with digitized scans carries a `<dao role="METS" ...>` reference; the associated METS record can in turn expose the scan/JPEG objects.

The Nationaal Archief web frontend can render a generic image-viewer layer even where no scan count or inventory-specific image object is demonstrably attached. Therefore the mere presence of `Scan / ...` controls is **not** sufficient evidence that inv. 999 or inv. 836 is digitized.

Archives Portal Europe currently describes 2.21.271 as having inventory numbers that are not available in copy form. No public DAO/METS endpoint for inv. 999 or inv. 836 has yet been found through indexed search. The evidentially safe status is therefore:

- digitization of inv. 999: **not established**;
- digitization of inv. 836: **not established**;
- generic viewer UI: **not evidence by itself**;
- a discovered DAO/METS link would constitute strong positive evidence.

This corrects the earlier provisional inference that the visible viewer shell might itself prove online scans.

## 3. Saint Lucas Society catalogue sequence

J.F. Heijbroek's reconstruction supplies a useful catalogue chronology:

- An intended wartime Catalogue 3 did not reach publication after its type/material disappeared during the occupation.
- A preserved **Catalogue 2, September 1943**, printed by Trio in The Hague, survives; its contents were largely social sciences/law plus genealogy/heraldry.
- A new postwar **Catalogue 3, *Wetenschappelijke adversaria*** was subsequently issued.
- Around 1948, Vosmaer's periodical *Bibliopolis* advertised Catalogue 3 as an international collection containing important works and noted several Huizinga-associated books with letters/dedications.

A 2019 postscript to Heijbroek's work supplies a further decisive institutional anchor: **Catalogue I survives in the library of the Vereeniging met de Lange Naam / KVB at the University of Amsterdam.** That copy is hand-annotated `'s-Gravenhage (1938)`; it contains 111 autograph entries followed by prints, reproductions, books and newspapers. This proves that KVB/UB Amsterdam holds at least one original Saint Lucas Society trade catalogue and materially strengthens the hypothesis that later Saint Lucas catalogues may also be there.

Sources:
- J.F. Heijbroek, "De Saint Lucas Society," *De Boekenwereld* 34.4 (2018).
- Heijbroek postscript in *De Boekenwereld* 35.4 (2019), reporting Catalogue I in the KVB/UB Amsterdam collection.

## 4. KVB catalogue volume VIII is the correct printed key

The KVB's multi-volume printed catalogue series must be used carefully. Volume VI (1949) is a supplement to the bibliographical/reference-book volumes and is **not** the correct index for antiquarian trade catalogues. The relevant repertory is:

**Catalogus der Bibliotheek van de Vereeniging ter Bevordering van de Belangen des Boekhandels te Amsterdam. Achtste deel. Supplement-catalogus 1932-1973. Amsterdam, Universiteitsbibliotheek, 1979. IX, 602 pp.**

Volume VIII is explicitly a supplement to volume IV (1934), which catalogued book-trade catalogues. Its structure is unusually useful for this investigation:

- pp. 1-112: publishers' stock catalogues;
- pp. 113-380/381: **antiquarian and warehouse catalogues**, arranged alphabetically by firm and chronologically within each firm;
- pp. 381-487: book, print and drawing auction catalogues;
- pp. 488-602: detailed indexes/addenda.

The antiquarian section records, per firm, catalogue date/title/number and number of entries or pages. In the auction-catalogue section, the repertory marks copies with prices and copies annotated with prices and buyers' names. This demonstrates that the KVB collection was built and catalogued specifically with provenance reconstruction in mind.

Therefore the immediate printed-index question is now narrowly defined: **does the Saint Lucas Society lemma in volume VIII list Catalogue I, Catalogue 2, Catalogue 3 (*Wetenschappelijke adversaria*), *Rapiarijs*, or related sale lists?**

Current digitization status of volume VIII: no full searchable scan has yet been located. An earlier promising De Gruyter/Brill eISBN `9789004542563` has now been identified as **Volume I (1920)**, not volume VIII. This false lead is closed. Volume VIII itself is bibliographically secure but still needs a searchable copy.

Sources:
- review in *De Gulden Passer* 57 (1979), describing volume VIII and its internal structure;
- *De Boekenwereld* 14 (1997), explaining the relation among KVB catalogue volumes and identifying VIII as the supplement to IV;
- De Gruyter Brill metadata for eISBN 9789004542563 = Volume I (1920).

## 5. UvA/KVB open-data route: live catalogue services

The University of Amsterdam now exposes the central catalogue as open linked data, giving a machine-searchable route that bypasses CataloguePlus/Primo's JavaScript frontend. The UvA open-data documentation identifies datasets for the central catalogue and books; the live TriplyDB pages currently report approximately **68.2 million statements in `Books`** and **79.1 million statements in the combined `Catalogue`**, updated **3 August 2026**.

The `Catalogue` service page shows three live search/index services:

- a "Speedy SPARQL" service;
- an Elasticsearch full-text index;
- a Virtuoso SPARQL service.

This is currently the most promising technical route to an exact KVB/Alma record for `Saint Lucas Society`, `C.J.J.G. Vosmaer`, or *Wetenschappelijke adversaria*, because the data can be queried without relying on the public discovery UI. The UvA Books OAI feed is also exposed; the MARC set is identifiable as `boeken_marc`, although OAI-PMH is better suited to record validation/harvesting than keyword discovery.

Known KVB digital-object examples prove that historical bookseller/auction catalogues can have full digital surrogates and machine metadata. A Van Stockum auction catalogue of 25 May 1936 is digitized in UvA Heritage with shelfmark **UBM: KVB NV 4337** and exposes full text, METS and IIIF. Another Van Stockum sale catalogue has KVB shelfmark **UBM: KVB NV 3972** and catalogue/Alma record `alma990019428700205131`; that copy records buyers' names and prices. These examples establish both the digital-surrogate infrastructure and the bridge from old KVB shelfmarks to current Alma identifiers.

Current limitation: a custom query against the live SPARQL/Elasticsearch service has not yet been executed from the present web environment because constructed API endpoint URLs are blocked unless exposed through an indexed/clickable route. This is a tooling/access limitation, not evidence that the services are unavailable.

Sources:
- UvA Library Open Data page, central catalogue / OAI / linked-data services.
- UvA TriplyDB `Books` and `Catalogue` dataset/service pages, updated 2026-08-03.
- UvA Heritage digitized KVB Van Stockum catalogue records, including KVB NV 4337 and KVB NV 3972.

## 6. Leiden University Library is a primary Saint Lucas client

Heijbroek adds an important institutional route that should now run in parallel with KVB: **Leiden University Library, directly across the Rapenburg, was one of Saint Lucas Society's most important customers.** Vosmaer performed multiple services for the library, including reproduction/microfilm work involving books and autographs, image reproduction, stencilling lecture notes and dissertation-related publishing work.

This makes Leiden's own historical acquisitions/vendor/receiving records a first-order source for Catalogue 3 and related ephemera. A bookseller regularly serving the library is a plausible sender of catalogues, circulars, invoices, order correspondence and stock offers. Therefore the search should include Leiden UB annual reports, acquisition registers, supplier correspondence and administrative files for approximately 1945-1952, using `Vosmaer`, `Saint Lucas Society`, `Rapenburg 83`, `Wyttenbachweg 43`, `Bibliopolis`, `Rapiarijs` and *Wetenschappelijke adversaria*.

This is currently a **documentary probability**, not yet proof that Leiden received Catalogue 3.

Source: Heijbroek, "De Saint Lucas Society," on Leiden University Library as a major client and on the services Vosmaer supplied.

## 7. Rapiarijs / Bibliopolis as lot-level evidence

Heijbroek shows that Vosmaer also circulated sale/news sheets that can preserve individual stock numbers or lots:

- *Rapiarijs* circulated in the immediate postwar period, roughly 1946-47 (with an anomalous later unnumbered issue noted in the article).
- One issue advertised **lot 1221**, the P.T. Tideman archive, showing that these ephemeral publications can preserve numbered sale objects.
- *Bibliopolis* appeared approximately **1948-1952**; a correspondence address given in the material is **Wyttenbachweg 43, Oegstgeest**.

For the Huizinga/Malinowski provenance problem, locating surviving runs of *Rapiarijs* and *Bibliopolis* may be nearly as useful as Catalogue 3 itself, because they may reveal stock/lot numbers, descriptions of presentation copies, or interim sales that never entered a formal catalogue.

## 8. Börsenverein correspondence lead

A separate institutional trail exists in the Saxon State Archives / Börsenverein des Deutschen Buchhandels records. An indexed record identifies:

**St. Lucas Society, Buch- und Kunsthandlung, Antiquariat, Inhaber Carel J. J. G. Vosmaer, Leiden (Niederlande). F 079261937 - 1950.**

A 1950 bookseller-industry correspondence file could preserve circulars, catalogues, firm stationery, trade correspondence, or references to Saint Lucas Society stock. Its contents have not yet been inspected, so this is a documentary lead rather than proof of Catalogue 3 survival.

## 9. Address continuity: Rapenburg 83

A current antiquarian firm, Goltzius en De Hooghe BV, is registered at **Rapenburg 83, Leiden**, the historic Saint Lucas Society address. This is an intriguing address-continuity lead only. No business succession, transfer of Saint Lucas stock, or archival inheritance has yet been demonstrated. It should not be used as provenance evidence without a documented chain.

## 10. Priority order after this sync

1. Resolve/call the live **UvA Catalogue SPARQL or Elasticsearch service** for exact text searches: `Saint Lucas Society`, `St. Lucas Society`, `Vosmaer`, `Wetenschappelijke adversaria`, `Rapiarijs`, `Bibliopolis`.
2. Obtain/search **KVB catalogue volume VIII**, especially the Saint Lucas lemma in pp. 113-381, as an independent printed control.
3. Search Leiden UB's own 1945-1952 administrative/acquisition records and annual reports for Saint Lucas/Vosmaer transactions or received catalogues.
4. Use any UvA/KVB record to obtain exact shelfmarks for Catalogue I/2/3 and related ephemera; then test for UvA Heritage METS/IIIF surrogates.
5. Test Nationaal Archief inv. 836 and inv. 999 for true EAD `<dao role="METS">` links rather than frontend viewer artifacts.
6. Investigate Börsenverein file `F 079261937` for Saint Lucas Society trade correspondence and enclosures.
7. Treat current Rapenburg 83 antiquarian occupancy as a question for documented address/business history, not as assumed continuity.

## Evidential caution

Do not cite inv. 999 or inv. 836 as digitized unless an inventory-specific DAO/METS or equivalent scan object is actually identified. Do not treat Catalogue 3 as preserved merely because Catalogues I and 2 survive. KVB possession of Catalogue I is confirmed; possession of Catalogue 3 remains to be demonstrated. The live UvA linked-data services are confirmed, but a query result for Saint Lucas/Catalogue 3 has not yet been obtained.
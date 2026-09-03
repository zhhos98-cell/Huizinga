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

J.F. Heijbroek's 2018 reconstruction supplies a useful catalogue chronology:

- An intended wartime Catalogue 3 did not reach publication after its type/material disappeared during the occupation.
- The earliest preserved Saint Lucas Society catalogue Heijbroek reproduces is **Catalogue 2, September 1943**, printed by Trio in The Hague; its contents were largely social sciences/law plus genealogy/heraldry.
- A new postwar **Catalogue 3, *Wetenschappelijke adversaria*** was subsequently issued.
- Around 1948, Vosmaer's periodical *Bibliopolis* advertised Catalogue 3 as an international collection containing important works and noted several Huizinga-associated books with letters/dedications.

The survival of Catalogue 2 demonstrates that institutional or private copies of the firm's catalogue sequence did survive, strengthening the case for searching systematically for a surviving Catalogue 3 rather than assuming it lost.

Source: J.F. Heijbroek, "De Saint Lucas Society," *De Boekenwereld* 34.4 (2018).

## 4. Rapiarijs / Bibliopolis as lot-level evidence

Heijbroek shows that Vosmaer also circulated sale/news sheets that can preserve individual stock numbers or lots:

- *Rapiarijs* circulated in the immediate postwar period, roughly 1946–47 (with an anomalous later unnumbered issue noted in the article).
- One issue advertised **lot 1221**, the P.T. Tideman archive, showing that these ephemeral publications can preserve numbered sale objects.
- *Bibliopolis* appeared approximately **1948–1952**; a correspondence address given in the material is **Wyttenbachweg 43, Oegstgeest**.

For the Huizinga/Malinowski provenance problem, locating surviving runs of *Rapiarijs* and *Bibliopolis* may be nearly as useful as Catalogue 3 itself, because they may reveal stock/lot numbers, descriptions of presentation copies, or interim sales that never entered a formal catalogue.

## 5. Börsenverein correspondence lead

A separate institutional trail exists in the Saxon State Archives / Börsenverein des Deutschen Buchhandels records. An indexed record identifies:

**St. Lucas Society, Buch- und Kunsthandlung, Antiquariat, Inhaber Carel J. J. G. Vosmaer, Leiden (Niederlande). F 079261937 - 1950.**

A 1950 bookseller-industry correspondence file could preserve circulars, catalogues, firm stationery, trade correspondence, or references to Saint Lucas Society stock. Its contents have not yet been inspected, so this is a documentary lead rather than proof of Catalogue 3 survival.

## 6. Priority order after this sync

1. Search Google/indexed catalogues for a scan or holding record of Saint Lucas Society Catalogue 3, *Wetenschappelijke adversaria*.
2. Search for digitized or catalogued issues of *Bibliopolis* and *Rapiarijs*, especially via exact title, `Wyttenbachweg 43`, and C.J.J.G. Vosmaer.
3. Locate the exact Van Stockum sale catalogue for 3–5 December 1986, preferably a priced/annotated copy.
4. Test Nationaal Archief inv. 836 and inv. 999 for true EAD `<dao role="METS">` links rather than frontend viewer artifacts.
5. Investigate Börsenverein file `F 079261937` for Saint Lucas Society trade correspondence and enclosures.

## Evidential caution

Do not cite inv. 999 or inv. 836 as digitized unless an inventory-specific DAO/METS or equivalent scan object is actually identified. Do not treat Catalogue 3 as preserved merely because Catalogue 2 survives. These are active search targets.
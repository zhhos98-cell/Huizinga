# DBNL Verzamelde Werken integration decisions — 2026-09-04

Scope: human review of the deterministic nine-volume TEI traversal in `research/article_dbnl_verzamelde_werken_integration_2026-09-04.md`, specifically for surgical revision of canonical Draft 04. The traversal parsed all nine mirrored XML files, visited 79,038 XML elements and inspected 23,422 normalized text blocks. Candidate scoring was used only to surface high-recall passages; body decisions below are based on their historical function in the current article.

## BODY / SECURE — retain now

### 1. 1929 Leiden institutional prehistory

Source: Johan Huizinga, `Het sprookje van de rolverdeeling`, *De Gids* 93, no. 6 (June 1929), reprinted in *Verzamelde Werken* VII, DBNL TEI `huiz003verz08_01.xml`, VW p. 404.

Controlled wording: Huizinga quotes the 1924 university role-division report describing the chairs for Indonesian languages and for `land- en volkenkunde van Nederlandsch Indië` as `een privilege der Leidsche Universiteit`, explicitly linking that concentration to Leiden's collections and its chairs in colonial law.

Article function: **CHRONOLOGICAL / INSTITUTIONAL CONSEQUENCE.** This supplies a direct Huizinga-authored prehistory to the 1931 Centre proposal. The later memorandum did not simply discover a loose inventory of Leiden resources; Huizinga had already publicly treated Indonesian studies, ethnology, collections and colonial-law expertise as a deliberately concentrated Leiden configuration. Use one sentence in the 1931 scene, without turning this into a separate university-policy excursus.

### 2. 1933 Kula -> potlatch -> Burgundy: mechanism before analogy

Sources: Johan Huizinga, *Over de grenzen van spel en ernst in de cultuur* / `Algemeene cultuurgeschiedenis (vervolg)`, *Verzamelde Werken* V, DBNL TEI `huiz003verz06_01.xml`, especially VW pp. 18–20; independently controlled against `corrections/chunk_067_manual_round2b.json`.

Controlled sequence:

- Huizinga introduces exchange through `mildheid, vriendschap, vertrouwen, eer, hoogmoed en avontuur` and explicitly names Malinowski's *Argonauts of the Western Pacific*.
- He says Malinowski's description of Kula threw new light on related phenomena and turns to potlatch, specified through ceremonial giving, honour/status, later reciprocal obligation, generosity and trust.
- Before adding Philip the Good's 1454 *Voeu du Faisan*, Huizinga anticipates that the comparison may look forced and says he introduces it **not for its general play-character**, but as a specific case of `wedijverend, wederkeerig weeldevertoon en spilziek onthaal`.
- He then reconstructs a historical sequence of court banquets: turn-taking, the passing of a wreath, escalating splendour, and Philip finally outdoing the others. Only after specifying that relation does he call the Burgundian case `not so very far` from a potlatch.

Article function: **MECHANISM.** This is stronger than presenting Kula, potlatch and Burgundy as a stack of parallels. It directly exhibits the article's central claim: a classificatory vocabulary can remain available while the comparison itself is carried by named relations and a reconstructed historical sequence. Replace the current compressed coda sentence with this narrower event chain.

## NOTE / HOLD — relevant but do not force into body yet

### 3. 1929 cultural-history boundary and Mauss

`De taak der cultuurgeschiedenis`, DBNL collected works, already supports the current Draft 04 formulation that cultural history can learn from ethnology / sociology / Mauss without becoming subordinate to systematic social science. The current prose already performs this job. No new body expansion is warranted merely because the TEI now gives a cleaner locator.

### 4. 1933 Warburg as a `cultuurwetenschappelijk laboratorium`

`Een cultuurwetenschappelijk laboratorium` is institutionally suggestive, but in the present article it is **MERELY PARALLEL** unless a direct Leiden or Malinowski connection is demonstrated. Keep out of the body.

### 5. Later *Homo ludens* primitive / ethnology passages

The collected works contain many strong later formulations about ethnology, archaic culture, primitive religion and play. They fall outside the article's 1933 stopping rule and belong to a later corpus. Do not back-project them into the 1926–33 argument.

## Editing instruction

Patch only `writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`. Preserve surrounding prose. Add the 1929 institutional prehistory locally in the Leiden opening and replace only the current 1933 Kula/potlatch/Burgundy compression with the source's mechanism-first sequence. Add provenance notes rather than a new bibliography block if that keeps the intellectual diff smaller.

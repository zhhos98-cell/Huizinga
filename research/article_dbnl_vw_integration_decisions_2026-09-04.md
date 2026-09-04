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

### 3. 1926 American social science: `functional` was not a Malinowski-only import

Source: Johan Huizinga, *Amerika levend en denkend. Losse opmerkingen*, internally dated `19261000` in the DBNL TEI and published by H.D. Tjeenk Willink & Zoon, Haarlem, 1927; *Verzamelde Werken* V, DBNL TEI `huiz003verz06_01.xml`, especially `Geestelijke wachtwoorden` and `De wetenschap der samenleving`, VW pp. 445, 448–451.

Controlled sequence:

- Huizinga says the American social sciences with which the purpose of his journey brought him into closest contact included economics, political science, sociology, cultural anthropology and psychology.
- He describes American social science as explicitly pluralist and hostile to `één enkelen verklaringsgrond`: complex and changing phenomena cannot be exhausted by a few distinctions, classifications or abstractions.
- Summarizing Dewey, he writes that all action is `interactie, wederzijdsche handeling`; morality, economic life and scientific thought are all `sociale functies` produced through relations between person and environment.
- At the same time he resists the demand that history become mere `hand- en spandiensten` for sociology.

Article function: **COUNTEREVIDENCE / CONTEXTUAL CONTROL.** The December 1926 phrase `We emphasize the functional side of cultural phenomena` cannot be narrated as Malinowski supplying Huizinga with an otherwise absent functional vocabulary. Huizinga was already describing `function`, interaction, pluralism and the history/sociology boundary as features of the wider American social-scientific environment he had just encountered. Malinowski remains important because the pair exchange attached that relational vocabulary to concrete ethnological books and to Huizinga's historical problems. Patch the America-to-December transition so that the article does not accidentally reinstate a one-way influence story.

### 4. 1928 *Mensch en menigte*: `primitive` inside modern America

Source: Johan Huizinga, *Mensch en menigte in Amerika. Vier essays over moderne beschavingsgeschiedenis*, third edition, Haarlem 1928, *Verzamelde Werken* V, DBNL TEI `huiz003verz06_01.xml`, especially VW pp. 387–389. The DBNL text preserves the first-edition preface (September 1918) and the third-edition preface (January 1928), in which Huizinga says the book was written in 1918, revised in 1920, and revised again for the third edition to accentuate its historical character and update material where possible.

Controlled sequence: in the section `Tam en wild Amerika`, after describing modern urban revivalism, Huizinga writes: `Het is het voortleven van een primitieve geesteshouding in een economisch hoog ontwikkeld milieu.` He immediately compares credulity, excitability and sentimentality in contemporary America with the medieval popular mind, then turns to `organized emotion` and modern community mobilization.

Article function: **COUNTEREVIDENCE.** This is not merely another lexical occurrence. In a text reissued during the active Huizinga–Malinowski exchange, `primitive` describes a mentality persisting inside an economically advanced modern society and supports a comparison between modern America and the medieval past. The category therefore did not invariably perform the simple operation `living non-European people -> earlier human stage` even for Huizinga. Use one sentence beside the March 1928 `origins of culture` / `historical use` distinction, so the article's initial model of temporalization remains a historically consequential use rather than an over-totalized definition of the word.

## NOTE / HOLD — relevant but do not force into body yet

### 5. 1929 cultural-history boundary and Mauss

`De taak der cultuurgeschiedenis`, DBNL collected works, already supports the current Draft 04 formulation that cultural history can learn from ethnology / sociology / Mauss without becoming subordinate to systematic social science. The current prose already performs this job. No new body expansion is warranted merely because the TEI now gives a cleaner locator.

### 6. 1923 *De universiteit van Nederlandsch Indië*

The collected works contain a substantial institutional-design argument joining teaching, research, laboratories, libraries, collections, geography and ethnology in a proposed Indonesian university. This confirms that Huizinga could think institutionally about ethnographic and colonial knowledge well before the 1931 Leiden Centre. At present, however, no direct documentary chain connects this proposal to the 1931 Centre memorandum. Treat it as **NOTE / PARALLEL**, not as a prehistory of the Centre.

### 7. 1933 Warburg as a `cultuurwetenschappelijk laboratorium`

`Een cultuurwetenschappelijk laboratorium` is institutionally suggestive, but in the present article it is **MERELY PARALLEL** unless a direct Leiden or Malinowski connection is demonstrated. Keep out of the body.

### 8. Later *Homo ludens* primitive / ethnology passages

The collected works contain many strong later formulations about ethnology, archaic culture, primitive religion and play. They fall outside the article's 1933 stopping rule and belong to a later corpus. Do not back-project them into the 1926–33 argument.

## Editing instruction

Patch only `writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`. Preserve surrounding prose. The 1929 Leiden, 1933 mechanism-first, and 1926 American social-science controls are already integrated. For the 1928 *Mensch en menigte* control, add one sentence only to the March 1928 paragraph and one provenance note. Do not turn it into a separate pre-contact section or a lexical catalogue.

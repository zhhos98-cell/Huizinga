# DBNL 1921–1933 bounded-unit tail closure — 2026-09-05

_Status: CLOSED / ARTICLE-FACING CONTROL. This note repairs a review-pipeline truncation discovered after the 9-volume XML traversal. It does not claim literal manual annotation of all 8,720 candidate blocks; it closes the previously omitted tail of the bounded published-unit review under the article's existing selection rule._

## What was incomplete

The deterministic DBNL TEI traversal itself had completed successfully on 4 September 2026:

- 9 XML files parsed;
- 79,038 XML elements visited;
- 23,422 normalized text blocks inspected;
- 12,066,667 normalized block characters inspected;
- 8,720 candidate blocks retained for article-facing review.

The incompleteness was in the second-stage review aid, not in XML parsing. `scripts/review_dbnl_vw_units_1921_1933.py` surfaced 124 bounded published units but emitted only `ranked[:70]`. Fifty-four lower-ranked units therefore never entered `research/article_dbnl_vw_units_1921_1933_review_2026-09-04.md`.

On 5 September the rank cap was removed. The workflow was also changed so that relevant script/XML changes rerun both the nine-volume traversal and the bounded 1921–1933 unit report. GitHub Actions then regenerated the report with **124/124 bounded units emitted**. The regenerated report adds 1,092 lines relative to the former 70-unit output.

Important scope qualification: **124/124 means every unit admitted by the existing year/title bounding rule, not every conceivable publication unit in the nine volumes and not 8,720 manually annotated candidate rows.** The nine-volume machine traversal is exhaustive; the human semantic layer remains deliberately article-facing and bounded by the `AGENTS.md` relevance rule.

## Decision rule used on the restored tail

A restored unit earns Draft 04 prose only if it materially changes one of the following:

1. a premise;
2. a mechanism;
3. counterevidence;
4. chronology or causality;
5. a disciplinary boundary;
6. a second-order actor control.

Lexical occurrence, methodological atmosphere, generic source criticism, institutional adjacency, or another attractive comparison is insufficient. `primitive` remains the analytic centre, and DBNL XML/page coordinates remain digital evidence coordinates rather than Leiden archival shelfmarks.

## Restored-tail decisions

### HOLD / METHOD RESERVE — Friedländer review, 1928

Source: Huizinga's review of Max J. Friedländer, *Die altniederländische Malerei*, vol. V, *Nieuwe Rotterdamsche Courant*, 21 January 1928; collected in DBNL TEI `huiz003verz04_01.xml`, around VW p. 501–503.

The review endorses Friedländer's resistance to making every master a link in a causal chain and every visible property a consequence; close observation should not be subordinated to a prior hunger for causal connection. Huizinga also rejects psychologico-cultural fantasies where evidence cannot determine Bosch securely.

Article function: **METHOD RESERVE.** This is useful evidence for Huizinga's policing of causal construction and underdetermined cultural interpretation, but it neither concerns `primitive` nor establishes a Huizinga–Malinowski transaction. Draft 04 already has stronger pre-contact causal/comparative controls tied directly to the article's problem (Wells/Spengler, 1921; the 1926 culture-history theses). Do not add.

### HOLD / METHOD RESERVE — Champion's *Louis XI*, 1928

Source: Huizinga's review of Pierre Champion, *Louis XI*, *Museum* 36 (October 1928), DBNL TEI `huiz003verz05_01.xml`, VW pp. 195–196.

Huizinga accepts that fear of historical construction contains something true, but argues that annalistic narration, quasi-meditations and stylistic vividness do not solve the historian's task of identifying major questions, giving material form and discriminating important from incidental evidence. He also checks Champion against Chastellain and points to a concrete misrendering.

Article function: **METHOD / SOURCE-CRAFT RESERVE.** Strong for Huizinga's historical craft in general, but it does not alter the present pair argument. The current article already has closer first-order source-checking scenes. Do not add.

### HOLD / CATEGORY RESERVE — Halphen, *L'essor de l'Europe*, 1933

Source: Huizinga's review of Louis Halphen, *L'essor de l'Europe*, *Tijdschrift voor Geschiedenis* 48 (1933), DBNL TEI `huiz003verz05_01.xml`, VW pp. 129–133.

Huizinga notes that expressive period titles can over-accentuate tendencies, asks whether a synthesis called *L'essor de l'Europe* actually constructs the civilizational phenomenon named by its title, and criticizes anachronistic political language imposed on medieval state relations.

Article function: **CATEGORY / ANACHRONISM RESERVE.** This reinforces the same general caution already expressed more directly in the April 1926 theses and, above all, in the 6 November 1933 discussion of historical names and non-closed cultural unities that Draft 04 already uses. Adding this review would duplicate rather than change the argument. Do not add.

### HOLD / INSTITUTIONAL PARALLEL — `De verloren schatten van het Bataviaasch Genootschap`, 1931

Source: Huizinga, `De verloren schatten van het Bataviaasch Genootschap`, *De Gids* 95 (October 1931), DBNL TEI `huiz003verz08_01.xml`, VW pp. 471–472.

Huizinga reconstructs a disputed exhibition/collection responsibility chain from reports, interviews, minutes and correspondence. He asks whether the Bataviaasch Genootschap's complete shipment had actually been displayed and notes a contradiction over whether only the ethnographic maps and wayang puppets had been installed while more valuable material remained packed.

Article function: **INSTITUTIONAL / COLLECTIONS PARALLEL.** The date and ethnographic-collection setting make it adjacent to the 1931 Leiden Centre episode, but no direct documentary chain currently connects this exhibition controversy to the Centre memorandum, Malinowski, or the article's `primitive` problem. Under the same rule used for the 1923 Indonesian-university material, adjacency is not prehistory. Keep out of Draft 04.

### HOLD / CAUSAL-DECOMPOSITION PARALLEL — Becker's *Islamstudien*, 1924

Source: Huizinga's review of C. H. Becker, *Islamstudien*, *De Gids* 88 (October 1924), DBNL TEI `huiz003verz05_01.xml`, VW pp. 225–227.

Huizinga accepts the importance of economic factors while declining Becker's reduction of Islam's rise to them as a satisfactory historical explanation. He also treats Islam from a general culture-historical rather than narrowly colonial frame.

Article function: **PRE-CONTACT CAUSAL RESERVE.** The passage supports a wider pattern of resistance to single-factor causal reduction. It is less directly tied to the article's problem than the already controlled Wells/Spengler examples and therefore adds no body value at present.

### REJECT — lexical and generic tail material

The remaining restored low-ranked units consist chiefly of book notices, memorial pieces, university/examination commentary, local Leiden preservation pieces, bibliographic year blocks, ordinary source criticism and generic relational vocabulary. Examples include the literary characterization of Vondel's `primitieve geest`, incidental moral/political rhetoric, and DBNL bibliography entries whose keyword scores arise from titles or metadata. These do not satisfy the article-facing decision rule and must not be converted into a lexical catalogue.

## Draft decision

**No Draft 04 patch is warranted from the restored 54-unit tail.**

This is a substantive negative result, not an unfinished integration step. The strongest restored materials are method/category/institutional reserves, while the canonical draft already contains stronger and more direct controls for the same functions. Adding them would reduce article density and violate the surgical-editing rule.

The separate `chunk_018` America manuscript control remains outside this closure. It is a high-priority archival/body candidate because it may directly join broad historical schemata to `primitive`, but it remains blocked on diplomatic scan reading and object/state identification. It should not be promoted merely because the DBNL published-work tail is now closed.

## Closure rule

The DBNL collected-works layer is now closed for another generic article-facing sweep under the current corpus and selection rule. Reopen it only for:

1. a specific passage that falsifies or materially limits a current Draft 04 sentence;
2. a newly established direct documentary chain to a pair scene;
3. a publication-grade source/provenance correction;
4. a deliberate redesign of the bounding rule itself, explicitly distinguished from the already complete nine-volume XML traversal.

Do not equate future keyword density with new evidence.
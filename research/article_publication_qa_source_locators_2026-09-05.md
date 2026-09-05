# Draft 04 publication-QA source locators — 2026-09-05

Purpose: close source-location gaps introduced by the later DBNL integration passes. This is not new discovery and does not reopen the published-works sweep.

## 1. 1921 Spengler control needs exact collected-works pages

Current body claim combines two passages from Johan Huizinga, `Twee worstelaars met den engel` (1921):

- *Verzamelde Werken* IV, p. 451: Spengler's cross-civilizational exact `homologie` and the `Procrustesbed` of the system.
- *Verzamelde Werken* IV, p. 461: *Preussentum und Sozialismus* as a political doctrine based on a `historisch-ethnografische tegenstelling` between English and Prussian character.

Repo source: DBNL TEI `sources/dbnl/verzamelde_werken/huiz003verz05_01.xml`.

Decision: keep the body sentence but append the exact VW page locators. Do not create a new paragraph.

## 2. 1933 historical-naming control needs exact collected-works page

Current body claim from `Renaissance en Nieuwe Tijd` uses the passage in which the great objects of cultural history are too complex/diffuse to be grasped as closed named unities while names remain necessary for historical visibility.

Exact location: *Verzamelde Werken* IV, p. 341, DBNL TEI `sources/dbnl/verzamelde_werken/huiz003verz05_01.xml`.

Decision: append the exact VW page locator to the existing `(Huizinga, 1934)` citation. Retain the explicit qualification that this is a general problem of historical naming, not a definition of `primitive`.

## 3. Footnote [17] no longer fully supports the sentence that cites it

The body now says:

`Malinowski’s ethnography did not supply the relational vocabulary from scratch. It bound older historical objects—generosity, friendship and the efficacy of words—to observed circuits of reciprocity, obligation, trust and exchange; Huizinga tested that denser configuration’s historical reach.[^17]`

The research control is `research/article_1919_1933_relation_vocabulary_configuration_control_2026-09-04.md`, but the current [^17] mainly records Huizinga's 1925 Bloch review.

Source locators that should be added to [^17]:

- *Herfsttij der Middeleeuwen* (1919), *Verzamelde Werken* III, pp. 63–64: `vriendschap`, including the princely `mignon` as `een geformaliseerd instituut`, alongside sworn/blood companionship, dress and rank relations.
- VW III, pp. 68 and 138: `mildheid` among aristocratic virtues/social ideals.
- verbal efficacy is already controlled separately in [^24] and should be cross-referenced rather than duplicated at length.

The Bloch material remains useful as another pre-contact efficacy control and should not be deleted.

Decision: expand [^17] so it actually supports lexical continuity + later relational thickening. Keep the note compact and avoid claiming that the full later configuration already existed in 1919.

## Closure

After these locator repairs, no further DBNL prose should be added merely to improve thematic density. Continue only with factual/source-chain corrections or genuine draft-level contradictions.
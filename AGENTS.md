# AGENTS.md — Huizinga Article Research, Writing, and Editing Protocol

This file is the persistent instruction set for ChatGPT, Codex, and other agents working in this repository. Read it before any article edit or research expansion. It records the user's established workflow and should prevent future model sessions from regenerating, flattening, or re-theorizing the project. Do not rewrite or shorten this file unless the user explicitly asks.

## 1. Canonical article and version control

The canonical prose draft is:

`writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md`

Rules:

- **Never create Draft 05, Draft 06, or another parallel prose draft.**
- All substantive prose edits patch Draft 04 directly.
- `writing/benevolent_outsider_draft_04_bilingual_reading_companion.md` is a reading companion only. It mirrors the canonical English draft; it is not independently edited and should be synchronized only after canonical passages are stable.
- Before every write, fetch the current blob/file SHA. Sequential edits to the same file must use the latest returned SHA.
- Report the exact path, commit SHA, and the historical/conceptual effect of each meaningful edit.

## 2. Editing method: surgical patch, never regeneration

- **Edit by surgical patch, not regeneration.** Intellectual diff must stay local even if an API technically transmits the whole file.
- Preserve surrounding prose verbatim unless a specific local restructuring is necessary.
- Do not rewrite a paragraph or section merely for flow, completeness, elegance, tone, balance, symmetry, or smoother transitions.
- User annotations are local instructions. Fix the annotated place; do not use a comment as permission to rewrite its neighborhood.
- Do not let model completion automatically add explanatory closure, roadmap sentences, paragraph-end verdicts, or balanced mini-essays.
- Avoid the characteristic model tendency to compress a historical article back toward 3,000–4,000 words by summarizing event chains. If an event has several controlled actions, let the actions happen in the prose.
- Growth should come from evidence and intellectual history, not generic exposition.

Working maxim:

> The event must finish happening; it does not have to be explained to exhaustion.

Or, in the user's formulation: **不是事情一定要解释完，而是事情得发生完。**

## 3. Source lock and evidentiary levels

Factual expansion is source-locked to controlled material.

A restored date, place, person, action, quotation, correspondence sequence, archival object, or causal link must come from one of the following:

1. the canonical draft or archived earlier drafts;
2. repo evidence maps, scene calibration, research notes, correspondence controls, or primary-source transcriptions;
3. newly verified external research that has first been recorded in a bounded repo research/control note.

Never fill a historical gap from model memory, general knowledge, plausibility, or stylistic completion.

Use three evidence levels:

- **BODY / SECURE** — source directly controlled; may carry narrative or argument.
- **NOTE / PARTIAL** — relation or object secure but wording/content incomplete; use with exact qualification.
- **QUARANTINE / UNCONTROLLED** — interesting lead whose body, context, identity, or locator is not yet secure; do not narrativize.

When two sources conflict, preserve the discrepancy. Do not silently normalize dates, incipits, archive labels, or identities.

### Critical inventory rule

**Absence from one public catalogue or inventory does not invalidate material independently controlled in another archive.** Record the source discrepancy first. Do not automatically delete or downgrade archive-controlled material because a public inventory omits it.

Specific example that must be remembered:

- **30 January 1933, Malinowski → Huizinga** is an **unpublished Yale archival letter already controlled in the direct-pair apparatus**. It discusses Malinowski's Dutch, a possible contribution to *De Gids*, and the possibility of beginning in Dutch and having Huizinga correct his style.
- The public 2019 Huizinga correspondence inventory does not expose that item under 30 January. This is an **inventory-visibility discrepancy**, not grounds for deletion.
- Keep the letter in Draft 04. The Yale pair-file locator is now resolved as MS 19, Series I: Correspondence, box 4, folder 280, `Huizinga, Johan, 1926–1933`; this remains a folder locator, not independent item-level content evidence.
- See `research/article_direct_pair_1933_01_30_yale_correction_2026-09-04.md`.

## 4. External research

Generic retrieval is closed. Open new external research only when the current article exposes a specific factual or conceptual gap that could change a sentence, note, attribution, or event chain.

For external research:

1. search the bounded gap;
2. verify the source and evidentiary level;
3. record the result in a repo control/delta;
4. only then patch Draft 04.

Do not dump fresh web facts directly into the article before source control.

Do not reopen dormant provenance branches unless direct copy-level evidence appears.

## 5. The article's conceptual center is `primitive`

The article must not collapse back into a history of Huizinga and Malinowski's friendship or correspondence.

The center is **the changing historical work of `primitive`**.

The key conceptual problem is not that both men happened to use or care about `primitive`. It is:

> What could relations observed among peoples described as primitive disclose about other times and forms of life?

The important modern operation of `primitive` is the conversion of **present difference into historical anteriority**: a living people, custom, object, or social form could be classified as primitive and thereby positioned nearer an earlier phase of human history.

Track what that classification was allowed to infer, not merely where the word appears.

Core movement:

- Malinowski increasingly **unpacked** primitive/savage classifications into relations and practices: reciprocity, obligation, public knowledge, law, exchange, technical knowledge, etc.
- Huizinga repeatedly asked what those relations could do when carried into historical comparison.
- Therefore `primitive` is the center of the exchange because it organized a shared **problem of historical inference**, not because the two men shared one definition.

Supporting terms such as `function`, law, reciprocity, mentality, sociology, play, gift, prestige, or efficacy are **subordinate**. They enter only insofar as they show explanatory work being redistributed within or around `primitive`. Do not turn them into parallel conceptual themes.

## 6. `Waning` must remain precise

`WANING OF PRIMITIVE != DEATH OF THE WORD`.

The governing historical pattern is:

`FORM PERSISTS + INFERENTIAL SUFFICIENCY WANES + EXPLANATORY WORK IS REDISTRIBUTED`.

The claim is not semantic disappearance and not a simple replacement story.

`primitive` can remain common, institutionally active, and classificatorily useful while increasingly requiring more specific relations, source checks, and disciplinary authorizations before it can support a historical conclusion.

Do not write a teleology:

`primitive → play`

Play is not the successor category. The 1933 Hofstra chain proves that `primitive` remains in active pair circulation even while Huizinga's historical comparisons increasingly turn on more specific relations.

`Herfsttij` supplies Huizinga's self-reflexive vocabulary of waning and warnings about precursor history; it is **not** proof that the late Middle Ages are an analogy for the history of `primitive`.

## 7. Article architecture

The current structure should remain unless the user explicitly changes it:

1. **America, 1926: Primitive before the Encounter**
2. **‘Primitive Law’ and Historical Use, 1926–1929**
3. **The Historical Work of *Primitief*, 1929–1931**
4. **‘Primitive or Semi-Cultured’: Leiden, 1931**
5. **Coda: What Carried the Comparison, 1932–1933**

The underlying movement is still useful:

`network → correspondence → knowledge production → institution`

But this is scaffolding, not the article's thesis. Each scene must answer what `primitive` was doing there.

## 8. How to grow the article without AI compression

The draft is still short relative to a full HHS/JHI-scale article. Do not solve this by adding abstract explanation.

Grow through:

- complete event chains;
- books actually being sent, chosen, read, reused, and discussed;
- correspondence opened outward to published books, courses, slips, manuscripts, lectures, museum dossiers, and institutional memoranda;
- exact changes in the work performed by `primitive`;
- source-practice scenes that show what historical comparison required after a classificatory suggestion;
- historiographical disagreement that changes how the primary case is read.

A preferred intellectual-history sequence is:

`PAIR EXCHANGE → SPECIFIC ANTHROPOLOGICAL TEXT/OBJECT → HUIZINGA NOTE/LECTURE/MANUSCRIPT/HISTORICAL USE`

The late-1933 Hofstra chain is a model:

`27 Oct Huizinga → Malinowski on Hofstra`
→ `30 Oct Malinowski reply`
→ `Hofstra, primitive individuality`
→ `6 Nov Huizinga uses the ethnographic example in a historical argument about return and the past`.

That is better growth than another paragraph explaining “circulation” in the abstract.

## 9. Direct-pair evidence: preserve scarce traces

Material in which Huizinga and Malinowski directly co-occur is scarce and should be preserved aggressively when controlled.

Do not delete apparently mundane traces simply because they look biographical. A friend-reference, book dispatch, reading aloud, dictionary remark, review, style correction, teaching request, or carried institutional letter may establish the density and direction of intellectual traffic.

Important controlled pair sequence includes:

- 1926 Harvard seminar and 19 May `mijn nieuwen vriend Malinowski` family letter;
- 12 and 31 December 1926 books / calf / Trekvaart / historical method;
- 29 March and 15 August 1928 reciprocal reading;
- 13 May 1929 Trobriands / Delft course;
- 19 July, 30 July, 12 August, 15 September, 4 October 1931 Leiden sequence;
- dense November–December 1932 correspondence;
- unpublished Yale 30 January 1933 Dutch / *De Gids* / style-correction letter;
- 20 → 23 May 1933 reprint / candidature sequence;
- 27 → 30 October 1933 Hofstra exchange.

Use pair material in three ways:

- **body** when it changes the historical shape of the relationship or conceptual problem;
- **note** when continuity is secure but content is incomplete;
- **quarantine** when context remains uncontrolled.

Do not inflate unpublished incipits into full intellectual arguments.

## 10. Correspondence is a junction, not the final object

The article currently risks reading as correspondence history whenever letters are not opened toward other materials.

Whenever possible, ask:

- What book or argument is behind this letter?
- What lecture, course, note, manuscript, or historical dossier does Huizinga move the problem into?
- What happens to the category when it crosses that boundary?

Examples already central:

- *Crime and Custom*: `primitive law` remains in the title while explanation moves into reciprocal services, kin relations, public knowledge, and obligations of return.
- 1928: `origins of culture` vs `historical use` marks two different jobs.
- 1929 Delft: thick familiarity with Trobriand ethnography coexists with `stage of savage life`.
- Leiden 1931: `primitive or semi-cultured races` becomes an institutional/classificatory programme whose personnel and principle Malinowski audits.
- Hofstra 1933: primitive remains in circulation while Huizinga imports a specific relation **to the past**, not a simple equivalence between contemporary primitive peoples and Europe's past.

## 11. Counterevidence must stay

The article must not become a triumphal story of Huizinga naturally escaping reductionism.

Do not remove or soften these controls:

1. **29 March 1928:** Huizinga invokes the “immense complexity of the smallest social phenomenon” and on the same page uses the antisemitic stereotype `Talmudic mind`. Complexity and flattening coexist.
2. **13 May 1929:** `quite at home in the Trobriands` coexists with a course sequence beginning at `the stage of savage life`. Thick familiarity and stadial order coexist.
3. **Post-outsider circulation:** Ahlbrinck / *Encyclopaedie der Karaïben* continues moving through Huizinga → Malinowski → pupil after the 1931 boundary. Outsiderhood does not mean withdrawal.
4. **Locher 1958:** Locher's claim that Malinowski did not modify Huizinga's global image of primitive culture is a genuine historiographical challenge. The article's answer is not “Locher was wrong” but that a classificatory image can persist while its inferential work changes.

## 12. Outsiderhood is a consequence, not a separate abstract thesis

Do not split `benevolent outsider` from `primitive` into a second conceptual article.

- `benevolent` = read, send, support, organize, compare, circulate.
- `outsider` = limit on disciplinary leadership/authority.
- The Leiden episode is the institutional form of the same epistemological issue: categories and questions travel more easily than authority over the evidence and programme.
- Outsiderhood is produced by sustained proximity, not by ignorance or withdrawal.

The 30 July 1931 praise must stay alongside the limit: Malinowski could call Huizinga's historical method “really anthropological” and ask him to play a teaching part while still demanding different personnel and a central disciplinary principle.

## 13. Chronology and event-chain rules

Read every paragraph for temporal orientation.

Use time anchors when they prevent genuine confusion:

- retrospective vs contemporaneous evidence;
- long gaps;
- dense rapid correspondence;
- returns to an earlier methodological text.

Do not calculate every interval mechanically.

Preferred reconstruction:

`date/place/action → letter/request → reply → consequence`.

Leiden is a model:

17 July local circulation/revision
→ 19 July Huizinga sends packet
→ 30 July Malinowski reads and audits
→ 12 August Huizinga answers / outsider
→ 15 September dispatch
→ 4 October use/review/Paris routing.

1932–33 should likewise be allowed to remain dense rather than summarized as “the correspondence continued.”

## 14. Facts, materials, historiography, inference

Keep four voices distinguishable:

1. **fact/event** — who did what, when;
2. **material/source** — what a letter, manuscript, slip, dossier, or object shows;
3. **historiography** — what secondary scholarship has argued;
4. **article inference** — what this article concludes from the material.

Do not turn these into visible `[FACT] / [METHOD]` labels. Use minimal anchors only where the reader could confuse the layers.

A reader should be able to disagree with the archive reading, the historiographical relation, or the inference separately.

## 15. Historiography

Every secondary source must have a job:

`inherit / correct / refute / converge / narrow / redirect / expose a gap`.

Avoid citation dumps.

Preferred form:

> A makes X visible; B changes the scale or evidence; the present archive shows why X is insufficient or must be narrowed at Y.

Current important relations include:

- Arnade ↔ Vale on anthropology vs persistent philological formation;
- Rydin on interwar historicization;
- Small / van der Lem on material source practice;
- Greilsammer / Bloch as a pre-Malinowski control;
- Locher as direct counterpoint on whether Malinowski changed Huizinga's primitive;
- Foks only as a later contrast, not as a model to impose backward.

## 16. Prose style and defensive temperature

Finished prose should sound like historical scholarship, not an agent explaining its own reasoning.

Avoid:

- invented technical terms and workbench labels;
- repeated `warrant`, `jurisdiction`, `evidentiary layer`, `material control`, `temporal control`, etc. when ordinary historical language will do;
- slogans invented during drafting;
- repeated `this does not mean`, `rather`, `not X but Y`, and pre-emptive qualifications;
- symmetrical counterargument paragraphs added merely for balance;
- roadmap sentences and paragraph-end verdicts;
- excessive proper-name density;
- one-sentence paragraphs created only to mark analytical layers.

Use `warrant`, `jurisdiction`, or other technical vocabulary only where the word genuinely earns its precision.

Paragraphs should usually let one historical/intellectual action unfold. Merge adjacent short paragraphs when they are the same action; do not merge distinct events just to increase paragraph length.

## 17. Notes

Notes can carry:

- minimal background knowledge a reader may lack;
- chronology and provenance;
- archive/correspondence locators;
- translation choices;
- uncertainty and source-status explanations;
- direct-pair continuity that is secure but not central enough for the body.

Do not bury the main conceptual step in a note.

Do not let notes become defensive mini-essays.

## 18. Word-count growth

The current draft remains shorter than a full HHS/JHI-scale article. The solution is **not** filler and not whole-draft regeneration.

Add length by reconstructing:

- historical event chains;
- conceptual work inside primary texts;
- movement between correspondence and books/notes/manuscripts;
- material source practices;
- institutional sequences;
- historiographical consequences that genuinely redirect the case.

If a draft pass reduces source density while making prose smoother, it is probably the wrong pass.

## 19. Publication QA still open

Do not pretend unresolved publication details are solved.

One locator is now resolved: the Yale Huizinga pair file is **Bronislaw Malinowski Papers, MS 19, Series I: Correspondence, box 4, folder 280, `Huizinga, Johan, 1926–1933`, Yale University Library** (finding aid also gives reel 2 / 2U). This is a folder locator, not independent item-level content evidence. The exact Yale locator for the 30 January 1933 letter should therefore no longer be listed as open.

The 1926/1927 *Sex and Repression* problem remains open, but it is now more precisely a **state-identification problem**. Controlled sequence: on 19 February 1926 Malinowski told the Frazers that `Sex & Repression` "will be published soon" (Trinity College Cambridge, Frazer Papers, `FRAZ/2/139`); on 12 December 1926 Huizinga acknowledged the `medium` book identified by the *Briefwisseling* editors as *Sex and Repression*; the standard edition's preface is signed February 1927 and the ordinary bibliographic record is 1927. Do not normalize this to a 1926 edition. The open question is whether Huizinga received a proof, advance/pre-final state, differently constituted preliminaries, or another author-controlled object. See `research/sex_and_repression_1926_control_search_delta_2026-09-04.md` and `research/article_sex_repression_imprint_1926_1927_recheck_2026-09-05.md`.

Other important open checks still include exact archival/correspondence locators where not yet fixed and formal KNAW candidature mechanics. The core 1926/1931 pair locators used in Draft 04 have now been tightened: 12 December 1926 = *Briefwisseling* II [685], p. 132; 31 December 1926 = LSE `MALINOWSKI/36/39`; 30 July 1931 = [902]; 12 August 1931 = [903]. `beleving der Feodaltijd` is no longer an open translation problem: retain the Dutch because Huizinga's own usage spans experience, realization and enactment; see `research/article_beleving_translation_control_2026-09-05.md`. Other difficult terms should be treated as concrete translation choices only when they actually bear on a sentence, not as a generic search task. Malinowski’s final 1933 status as a foreign member is secure, but the formal proposer/signatories, division vote and election/appointment sequence remain open. The Ahlbrinck dispatch is now fixed at **NOTE / PARTIAL**: identification of the 15 September 1931 volume as *Encyclopaedie der Karaïben* remains highly probable but not certain; reopen only if the full Yale letter body or an independent dispatch/presentation record appears. Do not repeat generic publication-timing searches; see `research/article_ahlbrinck_dispatch_recheck_2026-09-05.md`. The 8 February 1933 rectoral address chronology/pages and the 6 November Amsterdam lecture title/date are now source-controlled in `research/article_1933_coda_chronology_bibliography_control_2026-09-05.md` and should not be reopened as generic QA gaps.

Leiden archive locators must be distinguished from repository audit pointers. `review/chunk_*` is an internal digital-corpus coordinate, **not** a Leiden shelfmark. Three Draft 04 mappings are now source-controlled: Indian medicine = Huizinga archive no. **34 II** (`Oldindian medicine`); Philip/Burgundian material = no. **27**, with the 1929 portrait-photograph sequence in `env. Iconographie`; the 18 March 1930 French lecture `Aperçu de la civilisation hollandaise du XVIIe siècle` = no. **29 II.1**. See `research/article_leiden_archive_locator_mapping_2026-09-05.md`. Do not extend those numbers to adjacent chunk material. Formal inventory mapping remains unresolved for the separate Renaissance packet `chunk_028:p0183`, American cards/prose `chunk_018:p0198–p0238`, the `Trois esprits prégothiques` manuscript in `chunk_002`, the history/science cards `chunk_020:p0201–p0204`, and the Leiden American itinerary `chunk_019:p0031`. Keep the internal pointer until a formal mapping is recovered; never guess from neighboring H.A. numbers.

Resolve these at publication QA stage or when a sentence specifically depends on them.

## 20. Final pre-write checklist

Before committing an edit, ask:

1. Is every new fact source-controlled?
2. Did the historical event actually finish happening?
3. Is the reader temporally oriented?
4. Is `primitive` still the conceptual center?
5. Did a supporting concept accidentally become a parallel article?
6. Did correspondence open into a book, note, manuscript, course, institution, or historical use where relevant?
7. Are counterevidence and awkward facts still present?
8. Did I add defensive prose or invented jargon?
9. Did I regenerate more than the user asked?
10. Did the draft grow through historical/intellectual substance rather than explanation for its own sake?
11. Did I fetch the current SHA before writing?
12. Can I report exactly what changed and why?

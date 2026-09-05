from pathlib import Path
import subprocess

# Restore the exact pre-edit AGENTS.md, then change only the stale publication-QA section.
base_commit = "4007d5f817a5163145b90930fcc0505d764e4c82"
text = subprocess.check_output(["git", "show", f"{base_commit}:AGENTS.md"], text=True)

old = """## 19. Publication QA still open

Do not pretend unresolved publication details are solved. Important open checks include exact archival/correspondence locators, translations of difficult Dutch terms, the 1926/1927 *Sex and Repression* circulation anomaly, exact 1933 address sequence/pages, Ahlbrinck dispatch certainty, KNAW candidature mechanics, and exact Yale locator for the 30 January 1933 unpublished letter.

Resolve these at publication QA stage or when a sentence specifically depends on them.
"""

new = """## 19. Publication QA still open

Do not pretend unresolved publication details are solved.

One locator is now resolved: the Yale Huizinga pair file is **Bronislaw Malinowski Papers, MS 19, Series I: Correspondence, box 4, folder 280, `Huizinga, Johan, 1926–1933`, Yale University Library** (finding aid also gives reel 2 / 2U). This is a folder locator, not independent item-level content evidence. The exact Yale locator for the 30 January 1933 letter should therefore no longer be listed as open.

The 1926/1927 *Sex and Repression* problem remains open, but it is now more precisely a **state-identification problem**. Controlled sequence: on 19 February 1926 Malinowski told the Frazers that `Sex & Repression` "will be published soon" (Trinity College Cambridge, Frazer Papers, `FRAZ/2/139`); on 12 December 1926 Huizinga acknowledged the `medium` book identified by the *Briefwisseling* editors as *Sex and Repression*; the standard edition's preface is signed February 1927 and the ordinary bibliographic record is 1927. Do not normalize this to a 1926 edition. The open question is whether Huizinga received a proof, advance/pre-final state, differently constituted preliminaries, or another author-controlled object. See `research/sex_and_repression_1926_control_search_delta_2026-09-04.md` and `research/article_sex_repression_imprint_1926_1927_recheck_2026-09-05.md`.

Other important open checks still include exact archival/correspondence locators where not yet fixed, translations of difficult Dutch terms, exact 1933 address sequence/pages, Ahlbrinck dispatch certainty, and KNAW candidature mechanics.

Resolve these at publication QA stage or when a sentence specifically depends on them.
"""

if text.count(old) != 1:
    raise SystemExit(f"expected one section-19 anchor, found {text.count(old)}")

Path("AGENTS.md").write_text(text.replace(old, new, 1), encoding="utf-8")

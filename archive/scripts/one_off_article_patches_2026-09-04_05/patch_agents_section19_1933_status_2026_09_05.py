from pathlib import Path

path = Path('AGENTS.md')
text = path.read_text(encoding='utf-8')
old = "Other important open checks still include exact archival/correspondence locators where not yet fixed, translations of difficult Dutch terms, exact 1933 address sequence/pages, Ahlbrinck dispatch certainty, and KNAW candidature mechanics."
new = "Other important open checks still include exact archival/correspondence locators where not yet fixed, translations of difficult Dutch terms, Ahlbrinck dispatch certainty, and formal KNAW candidature mechanics. Malinowski’s final 1933 status as a foreign member is secure, but the formal proposer/signatories, division vote and election/appointment sequence remain open. The 8 February 1933 rectoral address chronology/pages and the 6 November Amsterdam lecture title/date are now source-controlled in `research/article_1933_coda_chronology_bibliography_control_2026-09-05.md` and should not be reopened as generic QA gaps."
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

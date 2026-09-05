from pathlib import Path

P = Path('AGENTS.md')
s = P.read_text(encoding='utf-8')

old_locator = "Formal inventory mapping remains unresolved for the separate Renaissance packet `chunk_028:p0183`, American cards/prose `chunk_018:p0198–p0238`, the `Trois esprits prégothiques` manuscript in `chunk_002`, the history/science cards `chunk_020:p0201–p0204`, and the Leiden American itinerary `chunk_019:p0031`. Keep the internal pointer until a formal mapping is recovered; never guess from neighboring H.A. numbers."
new_locator = "Formal inventory mapping remains unresolved for the separate Renaissance packet `chunk_028:p0183`, American cards/prose `chunk_018:p0198–p0238`, the `Trois esprits prégothiques` manuscript in `chunk_002`, the history/science cards `chunk_020:p0201–p0204`, the Leiden American itinerary `chunk_019:p0031`, and the `Ridderspelen als beleving der Feodaltijd` slip at `chunk_013:p0142`. Keep the internal pointer until a formal mapping is recovered; never guess from neighboring H.A. numbers."
if s.count(old_locator) != 1:
    raise SystemExit(f'Expected one locator paragraph, found {s.count(old_locator)}')
s = s.replace(old_locator, new_locator)

anchor = "\nResolve these at publication QA stage or when a sentence specifically depends on them."
insert = "\nThe Nieuwenhuis annex now has a bounded genealogy control. Van Bergen (2009), citing the Nieuwenhuis archive (printed as `DPL 2591: F9N`; current UBL holdings identify the archive as **BPL 2591/3321**, collection guide `ubl218`), documents a **1913** annex to a same-titled Centre/museum-reorganization memorandum and describes the same object-to-mental-capacity / `voor hoogere beschaving vatbaar` programme. Nieuwenhuis's independently bibliographed 1913 *Die Veranlagung der malaiischen Völker des ost-indischen Archipels, erläutert an ihren industriellen Erzeugnissen* secures that prewar programme; Kern's 1883 `voor hoogere beschaving vatbaar` title is a still earlier phrase-level antecedent. Treat the **1913 antecedent as BODY / SECURE**, but direct **1913 → 1931 textual reuse as NOTE / PARTIAL**. Do not write that the 1931 annex was copied, revised, or reused from 1913 until BPL 2591 F9N and the Yale 1931 annex are directly compared or an archival/critical source explicitly links them. The old project-apparatus date `13 July 1931` is not yet independently item-reverified. See `research/article_nieuwenhuis_annex_1913_1931_genealogy_control_2026-09-05.md`.\n"
if s.count(anchor) != 1:
    raise SystemExit(f'Expected one QA close anchor, found {s.count(anchor)}')
s = s.replace(anchor, insert + anchor)

P.write_text(s, encoding='utf-8')

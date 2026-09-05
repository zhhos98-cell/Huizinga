from pathlib import Path

P = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
s = P.read_text(encoding='utf-8')

old_note = "[^13]: A. W. Nieuwenhuis, ‘Ethnographical objects as data for psychological research about primitive or semi-cultured races’, annex to Leiden Centre memorandum, July 1931."
new_note = "[^13]: A. W. Nieuwenhuis, ‘Ethnographical objects as data for psychological research about primitive or semi-cultured races’, annex to Leiden Centre memorandum, July 1931. Van Bergen (2009: 53), citing Nieuwenhuis papers at Leiden, reports that in 1913 Nieuwenhuis wrote an annex to a memorandum with the same Centre/museum-reorganization title and describes the same object-to-mental-capacity and `voor hoogere beschaving vatbaar` programme. His 1913 *Die Veranlagung der malaiischen Völker des ost-indischen Archipels, erläutert an ihren industriellen Erzeugnissen* independently confirms the contemporary programme of inferring collective capacities from material products. Whether the two-page annex circulated in 1931 was a copy, revision or reuse of the 1913 text is not yet established; the two archival objects have not been directly compared. Van Bergen’s note prints the archive siglum as `DPL 2591: F9N`; current Leiden University Libraries holdings identify the Anton Willem Nieuwenhuis archive as BPL 2591/3321."
if s.count(old_note) != 1:
    raise SystemExit(f'Expected exactly one old [^13] note, found {s.count(old_note)}')
s = s.replace(old_note, new_note)

anchor_nieuwenhuis = "Morgan, P. D. (2025) ‘The (non-)Globalisation of Ideas Revisited’, *Global Intellectual History*, published online 3 August. doi:10.1080/23801883.2025.2540961.\n\nPels, P. (2022)"
replacement_nieuwenhuis = "Morgan, P. D. (2025) ‘The (non-)Globalisation of Ideas Revisited’, *Global Intellectual History*, published online 3 August. doi:10.1080/23801883.2025.2540961.\n\nNieuwenhuis, A. W. (1913) *Die Veranlagung der malaiischen Völker des ost-indischen Archipels, erläutert an ihren industriellen Erzeugnissen*. *Internationales Archiv für Ethnographie*, Supplement zu Bd. 21. Leiden: E. J. Brill.\n\nPels, P. (2022)"
if s.count(anchor_nieuwenhuis) != 1:
    raise SystemExit(f'Expected one Nieuwenhuis reference anchor, found {s.count(anchor_nieuwenhuis)}')
s = s.replace(anchor_nieuwenhuis, replacement_nieuwenhuis)

anchor_vanbergen = "Vale, M. (2021) ‘Huizinga’s Autumntide: The centenary of a masterpiece’, *The English Historical Review* 136(580): 672–693.\n\nvan der Lem, A. (2019)"
replacement_vanbergen = "Vale, M. (2021) ‘Huizinga’s Autumntide: The centenary of a masterpiece’, *The English Historical Review* 136(580): 672–693.\n\nvan Bergen, L. (2009) ‘De oprichting van de ‘Nederlandsche Vereeniging voor Tropische Geneeskunde’: een zaak van nationaal belang’, *Studium* 2: 92–104.\n\nvan der Lem, A. (2019)"
if s.count(anchor_vanbergen) != 1:
    raise SystemExit(f'Expected one van Bergen reference anchor, found {s.count(anchor_vanbergen)}')
s = s.replace(anchor_vanbergen, replacement_vanbergen)

P.write_text(s, encoding='utf-8')

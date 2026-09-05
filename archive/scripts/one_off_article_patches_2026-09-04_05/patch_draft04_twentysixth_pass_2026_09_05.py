from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')

replacements = [
    (
        "[^7]: Huizinga to Malinowski, 13 May 1929, correspondence item [811]. An unpublished Yale Huizinga-to-Malinowski letter of 23 April 1929 survives with the incipit ‘You never let me hear anything’. The *Briefwisseling* editors cite it for family news about Leonhard’s impending military service in Java; here it establishes that direct correspondence continued beyond the edited intellectual exchanges.",
        "[^7]: Huizinga to Malinowski, 13 May 1929, correspondence item [811]. An unpublished Yale Huizinga-to-Malinowski letter of 23 April 1929 survives with the incipit ‘You never let me hear anything’. The *Briefwisseling* editors cite it for family news about Leonhard’s impending military service in Java; here it establishes that direct correspondence continued beyond the edited intellectual exchanges. The Yale pair file is Bronislaw Malinowski Papers, MS 19, Series I: Correspondence, box 4, folder 280, ‘Huizinga, Johan, 1926–1933’, Yale University Library."
    ),
    (
        "[^15]: Huizinga to Malinowski, 15 September 1931, Yale inventory; Malinowski to Huizinga, 4 October 1931, correspondence item [910].",
        "[^15]: Huizinga to Malinowski, 15 September 1931, Bronislaw Malinowski Papers, MS 19, Series I: Correspondence, box 4, folder 280, ‘Huizinga, Johan, 1926–1933’, Yale University Library; Malinowski to Huizinga, 4 October 1931, correspondence item [910]."
    ),
    (
        "The 30 January 1933 Malinowski-to-Huizinga letter is unpublished Yale material already controlled in the pair apparatus; it discusses Malinowski’s Dutch, a possible contribution to *De Gids*, and Huizinga correcting his Dutch style. Its absence from the public 2019 inventory is treated as an inventory-visibility discrepancy, not as grounds to delete an independently archive-controlled letter. The exact Yale call/locator should be added before publication.",
        "The 30 January 1933 Malinowski-to-Huizinga letter is unpublished Yale material already controlled in the pair apparatus; it discusses Malinowski’s Dutch, a possible contribution to *De Gids*, and Huizinga correcting his Dutch style. Its absence from the public 2019 inventory is treated as an inventory-visibility discrepancy, not as grounds to delete an independently archive-controlled letter. The Yale container is Bronislaw Malinowski Papers, MS 19, Series I: Correspondence, box 4, folder 280, ‘Huizinga, Johan, 1926–1933’, Yale University Library."
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'anchor count={count} for {old[:100]!r}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')

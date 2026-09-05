from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')

replacements = [
    (
        "Both made distant worlds portable, but the evidentiary work behind that portability differed. For a category such as *primitive*, which could turn geographical or cultural distance into historical distance, those differences mattered: the step from classification to historical claim could not be the same in an observed social field and in a damaged textual or visual tradition.",
        "Both made distant worlds portable, but the evidentiary work behind that portability differed. For a category such as *primitive*, which could turn geographical or cultural distance into historical distance, those differences mattered. In the materials traced here, relations described through field observation and historical claims assembled through damaged textual or visual transmission passed through different kinds of checking."
    ),
    (
        "Present difference was again being asked to bear developmental and historical weight. Pels’s work on classification helps situate this: categories could describe objects, organize research and structure intervention at the same time (Pels, 2022).",
        "Present difference was again being asked to bear developmental and historical weight. Huizinga’s 1926 warning about general historical terms had therefore not produced a steady retreat from classification: the annex was Nieuwenhuis’s, but Huizinga helped assemble and forward a packet in which developmental labels still did practical work. Pels’s work on classification helps situate this: categories could describe objects, organize research and structure intervention at the same time (Pels, 2022)."
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'anchor count={count} for {old[:80]!r}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')

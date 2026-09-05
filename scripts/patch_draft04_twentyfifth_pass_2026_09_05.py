from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')

replacements = [
    (
        "His critique of Spengler made the same problem comparative: exact homologies across civilizations forced particulars onto the Procrustean bed of a system, while *Preussentum und Sozialismus* turned the operation political through a *historisch-ethnografische tegenstelling* between English and Prussian character (Huizinga, 1921).",
        "His critique of Spengler made the same problem comparative: exact homologies across civilizations forced particulars onto the Procrustean bed of a system, while *Preussentum und Sozialismus* turned the operation political through a *historisch-ethnografische tegenstelling* between English and Prussian character (Huizinga, 1921; *Verzamelde Werken* IV, pp. 451, 461)."
    ),
    (
        "The great objects of cultural history, he wrote, were so complex and diffuse that they could not properly bear a name or be grasped as a closed unity, yet without names history could not make them visible to the mind; such names often arose from the wishes and imagination of the age itself (Huizinga, 1934).",
        "The great objects of cultural history, he wrote, were so complex and diffuse that they could not properly bear a name or be grasped as a closed unity, yet without names history could not make them visible to the mind; such names often arose from the wishes and imagination of the age itself (Huizinga, 1934; *Verzamelde Werken* IV, p. 341)."
    ),
    (
        "[^17]: Huizinga had already reviewed Marc Bloch’s *Les rois thaumaturges* in 1925, treating ritual efficacy, sacral kingship and persistent belief as historical problems while criticizing the organization of a large evidentiary corpus (Huizinga, 1925). Greilsammer (2019) places the review within Huizinga’s later, ambivalent relation to French historians. Malinowski changed the direct traffic, examples and question of disciplinary competence.",
        "[^17]: The relational nouns in Huizinga’s 31 December 1926 letter had pre-contact histories in his own work. In the 1919 *Herfsttij*, friendship could be a stylized social relation—the princely *mignon* is called `een geformaliseerd instituut`—and is followed through sworn companionship, dress and rank relations (*Verzamelde Werken* III, pp. 63–64); `mildheid` appears among aristocratic virtues and social ideals (pp. 68, 138). For the earlier treatment of verbal efficacy, see [^24]. These passages establish an older vocabulary, not the later configuration of reciprocity, obligation, trust and exchange. Huizinga had also reviewed Marc Bloch’s *Les rois thaumaturges* in 1925, treating ritual efficacy, sacral kingship and persistent belief as historical problems while criticizing the organization of a large evidentiary corpus (Huizinga, 1925). Greilsammer (2019) places that review within Huizinga’s later, ambivalent relation to French historians. Malinowski changed the direct traffic, examples and question of disciplinary competence."
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'anchor count={count} for {old[:100]!r}')
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')

from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "The Amsterdam lecture Huizinga delivered on 6 November began from a problem of naming. The great objects of cultural history, he wrote, were so complex and diffuse that they could not properly bear a name or be grasped as a closed unity, yet without names history could not make them visible to the mind; such names often arose from the wishes and imagination of the age itself (Huizinga, 1934). He then wrote that when humanity means the future it often cries ‘back’, and footnoted Hofstra’s citation of W. C. Willoughby’s prophet among *natuurvolken* calling people to return to old loyalties because the ideal age lay in the past."
new = "The Amsterdam lecture Huizinga delivered on 6 November began from a problem of naming. The great objects of cultural history, he wrote, were so complex and diffuse that they could not properly bear a name or be grasped as a closed unity, yet without names history could not make them visible to the mind; such names often arose from the wishes and imagination of the age itself (Huizinga, 1934). This was a general problem of historical naming, not a definition of *primitive*; its relevance here is the gap Huizinga made explicit between needing a name and treating the named object as a closed explanatory unity. He then wrote that when humanity means the future it often cries ‘back’, and footnoted Hofstra’s citation of W. C. Willoughby’s prophet among *natuurvolken* calling people to return to old loyalties because the ideal age lay in the past."
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

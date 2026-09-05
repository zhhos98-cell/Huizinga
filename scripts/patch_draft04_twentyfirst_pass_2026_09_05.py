from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "In 1921, reviewing Wells’s attempt to extend world history from planetary and biological development into human history, Huizinga objected that geological or biological *ontwikkeling* had little to do with ‘de functie van het historisch begrijpen’; a wider chronology did not by itself yield historical understanding (Huizinga, 1921)."
new = "In 1921, reviewing Wells’s attempt to extend world history from planetary and biological development into human history, Huizinga objected that geological or biological *ontwikkeling* had little to do with ‘de functie van het historisch begrijpen’; a wider chronology did not by itself yield historical understanding (Huizinga, 1921). In the same review his objection to Spengler was explicitly political and ethnographic: he called *Preussentum und Sozialismus* a political doctrine based on a *historisch-ethnografische tegenstelling* between English and Prussian character, whose method first posited a contrast and then brought convenient particulars under its suggestive force (Huizinga, 1921)."
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

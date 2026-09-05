from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "In 1921, reviewing Wells’s attempt to extend world history from planetary and biological development into human history, Huizinga objected that geological or biological *ontwikkeling* had little to do with ‘de functie van het historisch begrijpen’; a wider chronology did not by itself yield historical understanding (Huizinga, 1921)."
new = "In 1921, reviewing Wells’s attempt to extend world history from planetary and biological development into human history, Huizinga objected that geological or biological *ontwikkeling* had little to do with ‘de functie van het historisch begrijpen’; a wider chronology did not by itself yield historical understanding (Huizinga, 1921). His critique of Spengler made the same problem comparative: exact homologies across civilizations forced particulars onto the Procrustean bed of a system, while *Preussentum und Sozialismus* turned the operation political through a *historisch-ethnografische tegenstelling* between English and Prussian character (Huizinga, 1921)."
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

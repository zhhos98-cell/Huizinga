from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')
old = "By 1930, in his French manuscript on twelfth-century intellectual life, *Trois esprits prégothiques*, *primitive* appears near *Cet élément ludique*; a few pages later the text refuses a simple Renaissance-precursor reading.[^9]"
new = "By 1930, in his French manuscript on twelfth-century intellectual life, *Trois esprits prégothiques*, *Cet élément ludique* opens an argument about scholastic competition and disputation, and *primitive* appears in the continuation of that same argument; a few pages later the text refuses a simple Renaissance-precursor reading.[^9]"
if text.count(old) != 1:
    raise SystemExit(f'anchor count={text.count(old)}')
path.write_text(text.replace(old, new, 1), encoding='utf-8')

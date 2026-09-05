from pathlib import Path

path = Path('writing/benevolent_outsider_draft_04_method_primitive_1921_1933.md')
text = path.read_text(encoding='utf-8')

old1 = "More directly, the 1919 first edition of *Herfsttij* had called symbolic thought, from an ethnological standpoint, `een zeer primitieve geestesfunctie` and linked *het primitieve denken* to medieval symbolism.[^24] His Indian papers also used *primitief* for earlier intellectual or medical layers.[^3]"
new1 = "More directly, the 1919 first edition of *Herfsttij* had called symbolic thought, from an ethnological standpoint, `een zeer primitieve geestesfunctie` and characterized *het primitieve denken* by a weak perception of identity boundaries, using that ethnological model to account for medieval symbolism.[^24] His Indian papers also used *primitief* for earlier intellectual or medical layers.[^3]"

old2 = "For *primitive*, these materials already separated position from explanation. *Primitief* could mark an earlier intellectual or medical layer, while Huizinga’s criticism of evolution denied that a developmental sequence by itself supplied historical understanding. Something could be placed earlier without that earlierness deciding what it meant or how it acted. The functional language Huizinga encountered in America, Malinowski’s included, entered precisely where the temporal label ceased to be sufficient: between locating a form and explaining the relations through which it worked."
new2 = "For *primitive*, these materials show a tension rather than a clean separation of position from explanation. In *Herfsttij*, the primitive model itself helped explain medieval symbolism, and verbal efficacy was said to appear in its fullness in primitive culture while persisting into the late Middle Ages.[^24] Elsewhere *primitief* could mark an earlier intellectual or medical layer; meanwhile Huizinga’s criticism of evolution denied that developmental sequence by itself supplied historical understanding. The pre-contact repertoire therefore contained both the older explanatory shortcut and a methodological reason not to let sequence or a general term settle the argument in advance. The functional language Huizinga encountered in America, Malinowski’s included, entered that tension: between locating a form and specifying the relations through which it worked."

if text.count(old1) != 1:
    raise SystemExit(f'first anchor count={text.count(old1)}')
if text.count(old2) != 1:
    raise SystemExit(f'second anchor count={text.count(old2)}')
text = text.replace(old1, new1, 1).replace(old2, new2, 1)
path.write_text(text, encoding='utf-8')

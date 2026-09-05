#!/usr/bin/env python3
from pathlib import Path
import csv, re

SRC = Path('analysis/dbnl_vw_article_candidates_2026-09-04.tsv')
OUT = Path('research/article_dbnl_vw_priority_units_review_2026-09-04.md')

TITLES = [
    'De wetenschap der samenleving',
    'Geestelijke wachtwoorden',
    'De taak der cultuurgeschiedenis',
    'Het sprookje van de rolverdeeling',
    'Over historische levensidealen',
    'Renaissance en Nieuwe Tijd',
    'Een cultuurwetenschappelijk laboratorium',
    'Algemeene cultuurgeschiedenis (vervolg)',
    'De universiteit van Nederlandsch Indië',
    'Twee worstelaars met den engel',
]

def n(r,k):
    try:return int(r.get(k,0) or 0)
    except:return 0

def clip(s, limit=1600):
    s=re.sub(r'\s+',' ',s or '').strip()
    return s if len(s)<=limit else s[:limit].rstrip()+' …'

def main():
    with SRC.open(encoding='utf-8', newline='') as f:
        rows=list(csv.DictReader(f, delimiter='\t'))
    md=['# DBNL priority published units — focused human review — 2026-09-04','',
        'Bounded follow-up to the complete TEI traversal and unit-level 1921–1933 grouping. These units are opened because they already touch a load-bearing Draft 04 scene or a known methodological boundary.','']
    for title in TITLES:
        rs=[r for r in rows if title.lower() in (r.get('div_title','') or '').lower()]
        md += [f'## {title}', '', f'Candidate blocks: **{len(rs)}**.','']
        rs.sort(key=lambda r:(-(int(bool(n(r,'primitive') and (n(r,'discipline') or n(r,'relations') or n(r,'actors'))))*4 + int(bool(n(r,'actors') and (n(r,'discipline') or n(r,'relations'))))*4), -n(r,'score'), r.get('page','')))
        seen=set(); shown=0
        for r in rs:
            sig=(r.get('file',''),r.get('page',''),(r.get('text','') or '')[:180])
            if sig in seen: continue
            seen.add(sig)
            tags=', '.join(f'{k}={n(r,k)}' for k in ['primitive','actors','discipline','relations','places','play'] if n(r,k))
            md += [f'### {r.get("file","")} / p.{r.get("page","") or "?"}', f'`score={n(r,"score")}; {tags}`','',clip(r.get('text','')),'']
            shown += 1
            if shown >= 18: break
    OUT.write_text('\n'.join(md), encoding='utf-8')
    print(OUT)

if __name__=='__main__': main()

#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import csv, re

SRC = Path('analysis/dbnl_vw_article_candidates_2026-09-04.tsv')
OUT = Path('research/article_dbnl_vw_units_1921_1933_review_2026-09-04.md')

YEAR_RE = re.compile(r'\b(192[1-9]|193[0-3])\b')
# Important published units whose candidate div-title does not always carry its date.
PRIORITY_TITLES = re.compile(
    r'(?i)(De wetenschap der samenleving|Geestelijke wachtwoorden|De taak der cultuurgeschiedenis|'
    r'Het sprookje van de rolverdeeling|Over historische levensidealen|Renaissance en Nieuwe Tijd|'
    r'Een cultuurwetenschappelijk laboratorium|Algemeene cultuurgeschiedenis \(vervolg\)|'
    r'Twee worstelaars met den engel|De universiteit van Nederlandsch Indië)'
)

def n(r, k):
    try: return int(r.get(k, 0) or 0)
    except ValueError: return 0

def clip(s, limit=1250):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s if len(s) <= limit else s[:limit].rstrip() + ' …'

def main():
    rows = []
    with SRC.open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))

    units = defaultdict(list)
    for r in rows:
        title = r.get('div_title', '') or ''
        if YEAR_RE.search(title) or PRIORITY_TITLES.search(title):
            units[(r.get('file',''), title)].append(r)

    ranked = []
    for key, rs in units.items():
        sums = {k: sum(n(r,k) for r in rs) for k in ['primitive','actors','discipline','relations','places','play']}
        # Reward combinations that can change the current article, not sheer lexical frequency.
        combo = sum(1 for r in rs if n(r,'primitive') and (n(r,'discipline') or n(r,'relations') or n(r,'actors')))
        actorrel = sum(1 for r in rs if n(r,'actors') and (n(r,'relations') or n(r,'discipline')))
        load = sums['primitive']*8 + sums['actors']*8 + sums['discipline']*4 + sums['relations']*2 + sums['places'] + combo*12 + actorrel*12
        ranked.append((load, key, rs, sums, combo, actorrel))
    ranked.sort(key=lambda x:(-x[0], x[1][0], x[1][1]))

    md = [
        '# DBNL collected works — unit-level 1921–1933 review pass — 2026-09-04','',
        'Purpose: second-pass human review aid after the complete nine-volume TEI traversal. This pass groups high-recall candidate blocks by published work / division, giving priority to units explicitly dated 1921–1933 and a bounded set of article-relevant units whose DBNL division title does not carry the date. It is not a new generic thematic sweep.','',
        f'- candidate rows loaded: **{len(rows):,}**',
        f'- bounded published units surfaced: **{len(ranked):,}**',
        f'- bounded published units emitted: **{len(ranked):,}** (no rank truncation)','',
        'Review rule: a unit earns Draft 04 prose only if its internal sequence changes an existing premise, mechanism, chronology, counterevidence, or disciplinary boundary. A high lexical score alone is not sufficient.',''
    ]

    # Emit every bounded unit. The previous ranked[:70] cap silently omitted the
    # lower-ranked tail from the human-review aid even though all XML had been parsed.
    for load,(file,title),rs,sums,combo,actorrel in ranked:
        md += [f'## {file} — {title or "[untitled division]"}', '',
               f'`unit_load={load}; blocks={len(rs)}; primitive={sums["primitive"]}; actors={sums["actors"]}; discipline={sums["discipline"]}; relations={sums["relations"]}; places={sums["places"]}; play={sums["play"]}; combo_blocks={combo}; actor_relation_blocks={actorrel}`','']
        # Prefer mixed-function blocks; then score. De-duplicate page/text beginnings.
        def rkey(r):
            mixed = int(bool(n(r,'primitive') and (n(r,'discipline') or n(r,'relations') or n(r,'actors'))))
            ar = int(bool(n(r,'actors') and (n(r,'relations') or n(r,'discipline'))))
            return (-(mixed*3+ar*3), -n(r,'score'), r.get('page',''))
        seen = set()
        shown = 0
        for r in sorted(rs, key=rkey):
            sig = (r.get('page',''), (r.get('text','') or '')[:180])
            if sig in seen: continue
            seen.add(sig)
            tags = ', '.join(f'{k}={n(r,k)}' for k in ['primitive','actors','discipline','relations','places','play'] if n(r,k))
            md += [f'### p.{r.get("page","") or "?"}', f'`score={n(r,"score")}; {tags}`', '', clip(r.get('text','')), '']
            shown += 1
            if shown >= 7: break

    OUT.write_text('\n'.join(md), encoding='utf-8')
    print(f'rows={len(rows)} units={len(ranked)} emitted={len(ranked)} report={OUT}')

if __name__ == '__main__':
    main()

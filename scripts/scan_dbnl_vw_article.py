#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import csv, hashlib, html, re, xml.etree.ElementTree as ET

ROOT = Path('sources/dbnl/verzamelde_werken')
OUT = Path('analysis/dbnl_vw_article_candidates_2026-09-04.tsv')
REPORT = Path('research/article_dbnl_verzamelde_werken_integration_2026-09-04.md')

GROUPS = {
    'primitive': re.compile(r'(?i)\bprimit\w*|\bsavage\w*|\bwilden?\b|\boer(?:mens|volk|tijd|toestand)\w*'),
    'actors': re.compile(r'(?i)\bMalinowski\b|\bTylor\b|\bFrazer\b|\bMauss\b|L[eé]vy[- ]Bruhl'),
    'discipline': re.compile(r'(?i)anthropolog\w*|ethnolog\w*|volkenkund\w*|sociolog\w*|sociale\s+morfolog\w*|cultuurgeschied\w*|historisch\w*\s+(?:begrijpen|methode|onderzoek)'),
    'relations': re.compile(r'(?i)functi\w*|wederker\w*|reciproc\w*|verplicht\w*|verplichting\w*|gift\w*|gave\w*|ruil\w*|prestige\w*|eer\b|recht\w*|mentalit\w*|magie\w*|toover\w*'),
    'places': re.compile(r'(?i)\bBali\b|\bJava\b|Indi[eë]|museum\w*|Rockefeller|Leiden|Trobriand\w*|Kula\b|potlatch'),
    'play': re.compile(r'(?i)\bspel\w*|ludiek\w*|ludisch\w*|Homo\s+ludens'),
}

BLOCK_TAGS = {'p','head','item','note','quote','q','l','ab'}
DIV_PREFIX = ('div',)

def lname(tag):
    return tag.split('}', 1)[-1].lower()

def clean(s):
    return re.sub(r'\s+', ' ', s or '').strip()

def first_direct_head(el):
    for ch in list(el):
        if lname(ch.tag) == 'head':
            t = clean(''.join(ch.itertext()))
            if t: return t
    return ''

def attr_id(el):
    for k,v in el.attrib.items():
        if k.endswith('}id') or k.lower() in {'id','n'}:
            if v: return v
    return ''

def scan_file(path):
    raw = path.read_bytes()
    root = ET.fromstring(raw)
    metrics = Counter(elements=0, chars=0, blocks=0)
    rows = []
    page = ''
    div_stack = []
    seen = set()

    def walk(el):
        nonlocal page
        metrics['elements'] += 1
        tag = lname(el.tag)
        pushed = False
        if tag.startswith(DIV_PREFIX):
            title = first_direct_head(el)
            div_stack.append((title, attr_id(el)))
            pushed = True
        if tag == 'pb':
            page = el.attrib.get('n') or el.attrib.get('id') or page
        if tag in BLOCK_TAGS:
            text = clean(''.join(el.itertext()))
            if len(text) >= 30:
                key = (text[:180], div_stack[-1] if div_stack else ('',''))
                if key not in seen:
                    seen.add(key)
                    metrics['blocks'] += 1
                    metrics['chars'] += len(text)
                    hits = {g: len(rx.findall(text)) for g,rx in GROUPS.items()}
                    if any(hits.values()):
                        score = hits['primitive']*6 + hits['actors']*6 + hits['discipline']*3 + hits['relations']*2 + hits['places']*2 + hits['play']
                        title, did = div_stack[-1] if div_stack else ('','')
                        rows.append({
                            'file': path.name, 'div_title': title, 'div_id': did, 'page': page,
                            'score': score, **hits, 'text': text
                        })
        for ch in list(el):
            walk(ch)
        if pushed:
            div_stack.pop()
    walk(root)
    return raw, metrics, rows

def clip(t, n=900):
    return t if len(t) <= n else t[:n].rstrip() + ' …'

def main():
    allrows, totals, files = [], Counter(), []
    for path in sorted(ROOT.glob('*.xml')):
        raw, met, rows = scan_file(path)
        totals.update(met)
        allrows.extend(rows)
        files.append((path.name, len(raw), hashlib.sha256(raw).hexdigest(), met, len(rows)))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    fields = ['file','div_title','div_id','page','score',*GROUPS.keys(),'text']
    with OUT.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        w.writeheader(); w.writerows(sorted(allrows, key=lambda r:(r['file'], -r['score'], r['div_title'], r['page'])))

    def section(title, pred, limit=220):
        rows = [r for r in allrows if pred(r)]
        rows.sort(key=lambda r:(-r['score'], r['file'], r['div_title'], r['page']))
        out = [f'## {title}', '', f'Candidate blocks: **{len(rows)}**. Showing up to {limit}.', '']
        for r in rows[:limit]:
            loc = ' / '.join(x for x in [r['file'], r['div_title'], ('p.'+r['page'] if r['page'] else ''), r['div_id']] if x)
            tags = ', '.join(f'{g}={r[g]}' for g in GROUPS if r[g])
            out += [f'### {loc}', f'`score={r["score"]}; {tags}`', '', clip(r['text']), '']
        return out

    md = [
        '# DBNL Verzamelde Werken integration delta — 2026-09-04','',
        'Purpose: deterministic article-facing traversal of the nine DBNL TEI XML volumes newly mirrored in this repository. The parser visits every XML element and every text block; keyword/group scoring is only a high-recall candidate layer for human article review, not a substitute for historical interpretation.','',
        '## Traversal control','',
        f'- XML files parsed: **{len(files)}**',
        f'- XML elements visited: **{totals["elements"]:,}**',
        f'- text blocks inspected: **{totals["blocks"]:,}**',
        f'- normalized block characters inspected: **{totals["chars"]:,}**',
        f'- candidate blocks retained for article review: **{len(allrows):,}**','',
        '| file | bytes | sha256 | elements | blocks | candidates |','|---|---:|---|---:|---:|---:|'
    ]
    for name,size,sha,met,nrows in files:
        md.append(f'| `{name}` | {size:,} | `{sha}` | {met["elements"]:,} | {met["blocks"]:,} | {nrows:,} |')
    md += ['',
        '## Review rule','',
        'Retain material only if it changes a premise, mechanism, counterevidence, chronology/causality, disciplinary boundary, or second-order actor control in Draft 04. Mere lexical parallels stay out of the body. Exact source wording and DBNL volume/page/division locators should be preserved in any later surgical patch.',''
    ]
    md += section('A. Primitive / savage / earlier-stage vocabulary', lambda r:r['primitive']>0, 260)
    md += section('B. Direct actor and anthropological interlocutor hits', lambda r:r['actors']>0, 180)
    md += section('C. Method / discipline / relation combinations', lambda r:r['discipline']>0 and (r['relations']>0 or r['primitive']>0 or r['actors']>0), 220)
    md += section('D. Java / Bali / museum / Trobriand / Kula / potlatch candidates', lambda r:r['places']>0 and (r['primitive']>0 or r['discipline']>0 or r['relations']>0 or r['actors']>0), 180)
    md += section('E. Play near primitive / anthropology / relational vocabulary', lambda r:r['play']>0 and (r['primitive']>0 or r['actors']>0 or r['relations']>0), 140)
    REPORT.write_text('\n'.join(md), encoding='utf-8')
    print(f'parsed={len(files)} elements={totals["elements"]} blocks={totals["blocks"]} candidates={len(allrows)}')

if __name__ == '__main__':
    main()

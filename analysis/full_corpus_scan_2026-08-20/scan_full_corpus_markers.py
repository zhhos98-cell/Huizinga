#!/usr/bin/env python3
"""
Sequential page-marker pass for the consolidated Huizinga Leiden PaddleOCR corpus.

Design:
- scans every page in physical order; no early exit
- separates exact entities from fuzzy candidates
- writes a sparse A/B/C marker index plus per-chunk coverage
- never treats fuzzy matches as confirmed identities
- does not alter OCR text
"""

from __future__ import annotations
import argparse, csv, hashlib, json, re, unicodedata
from collections import Counter, defaultdict
from pathlib import Path
import regex as regex_mod

ENTITY_PATTERNS = {
    "Huizinga": [r"\bhuizinga\b"],
    "Malinowski": [r"\bmalinowsk\w*\b"],
    "Rockefeller": [r"\brockefeller\b"],
    "Laura Spelman Rockefeller Memorial": [
        r"laura\s+spelman\s+rockefeller", r"rockefeller\s+memorial"
    ],
    "Van Sickle": [r"\bvan\s+sickl\w*\b"],
    "Kittredge": [r"\bkittredge\b", r"\bkitteredge\b"],
    "Outhwaite": [r"\bouthwait\w*\b"],
    "Nieuwenhuis": [r"\bnieuwenhuis\b"],
    "Van Eerde": [r"\bvan\s+eerde\b"],
    "Van de Sande Bakhuyzen": [
        r"\b(?:van\s+de\s+|v\.?\s*d\.?\s*)sande\s+bakhuyzen\b",
        r"\bsande\s+bakhuyzen\b",
    ],
    "J. P. B. de Josselin de Jong": [r"\bjosselin\s+de\s+jong\b"],
    "Rassers": [r"\brassers\b"],
    "Van Vollenhoven": [r"\bvan\s+vollenhoven\b"],
    "Jaap Kunst": [r"\bjaap\s+kunst\b"],
    "Hornbostel": [r"\bhornbostel\b"],
    "Westenenk": [r"\bwestenenk\b"],
    "Van Erp": [r"\bvan\s+erp\b"],
    "Edmund E. Day": [r"\bedmund\s+(?:e\.?\s*)?day\b"],
    "David H. Stevens": [r"\bdavid\s+(?:h\.?\s*)?stevens\b"],
    "Raymond B. Fosdick": [r"\bfosdick\b"],
    "John D. Rockefeller Jr.": [r"john\s+d\.?\s+rockefeller\s+jr"],
    "George Welwood Murray": [r"george\s+welwood\s+murray"],
}

FUZZY = {
    "Malinowski": ("malinowski", 2),
    "Van Sickle": ("van sickle", 2),
    "Kittredge": ("kittredge", 2),
    "Outhwaite": ("outhwaite", 2),
    "Nieuwenhuis": ("nieuwenhuis", 2),
    "Van Eerde": ("van eerde", 1),
    "Van de Sande Bakhuyzen": ("van de sande bakhuyzen", 3),
    "J. P. B. de Josselin de Jong": ("josselin de jong", 2),
    "Van Vollenhoven": ("van vollenhoven", 2),
}

FUZZY_ANCHORS = {
    "Malinowski": ("malin", "linow"),
    "Van Sickle": ("sick", "sicl"),
    "Kittredge": ("kitt", "tred"),
    "Outhwaite": ("outh", "wait"),
    "Nieuwenhuis": ("nieuw", "nienv"),
    "Van Eerde": ("eerde", "erde"),
    "Van de Sande Bakhuyzen": ("bakh", "sande"),
    "J. P. B. de Josselin de Jong": ("joss", "jong"),
    "Van Vollenhoven": ("vollen", "volenh"),
}

FUZZY_RX = {
    ent: regex_mod.compile(
        rf"(?b)(?<!\w)({regex_mod.escape(term)}){{e<={err}}}(?!\w)", regex_mod.I
    )
    for ent, (term, err) in FUZZY.items()
}

MONTHS = (
    r"(?:jan(?:uary|uari)?|feb(?:ruary|ruari)?|mar(?:ch|t)?|apr(?:il)?|may|mei|"
    r"jun(?:e|i)?|jul(?:y|i)?|aug(?:ust|ustus)?|sep(?:tember)?|sept(?:ember)?|"
    r"oct(?:ober)?|okt(?:ober)?|nov(?:ember)?|dec(?:ember)?|dez(?:ember)?|"
    r"januar|februar|märz|mai|juni|juli|august|september|oktober|november|dezember)"
)
DATE_RX = re.compile(rf"\b(?:[0-3]?\d)\s+{MONTHS}\s+(?:18|19|20)\d{{2}}\b", re.I)
NUM_DATE_RX = re.compile(r"\b(?:[0-3]?\d)[./-](?:[01]?\d)[./-](?:18|19|20)\d{2}\b")
YEAR_RX = re.compile(r"\b(18\d{2}|19\d{2}|20\d{2})\b")
INV_RX = re.compile(r"HUI[-_]\d{3}[-_]\d+(?:[-_]\d+)+[-_]?[A-Z0-9]*", re.I)

MANUAL = {
    "chunk_027:p0046": ("A", "Rockefeller Memorial/trustees + 23 Juni 1931; image review required because OCR layers unrelated material on the same page."),
    "chunk_027:p0048": ("B", "Rockefeller Memorial trustee/letterhead fragment; reads 1928."),
    "chunk_037:p0157": ("A", "Exact label 'FOR THE SOCIAL SCIENCES IN HOLLAND'; image review required."),
    "chunk_067:p0140": ("A", "Exact label 'FOR THE SOCIAL SCIENCES IN HOLLAND — DR. J. HUIZINGA'; image review required."),
    "chunk_067:p0070": ("C", "Malinowski in printed Homo Ludens/Kula discussion, not correspondence."),
    "chunk_067:p0071": ("C", "Malinowski in printed Homo Ludens/Kula discussion, not correspondence."),
    "chunk_067:p0072": ("C", "Malinowski in printed Homo Ludens/Kula bibliography/discussion; 1932 is bibliographic."),
    "chunk_068:p0052": ("A", "Archive boundary: HUI-071-2-31-000."),
    "chunk_068:p0053": ("A", "Unit title: 'Klank die wegsterft' (HUI-071-2-31-000)."),
    "chunk_068:p0058": ("A", "Incoming Huizinga letter: Hornbostel/Stanford and tactical timing of De Gids article."),
    "chunk_068:p0059": ("A", "Continuation/address material; Berlin/Hornbostel and Papaverhof."),
    "chunk_068:p0060": ("A", "Institutional chain: Van Erp -> Westenenk -> Koloniaal Instituut -> Minister/GG/Raad van Indie; tied to Huizinga's Gids article."),
    "chunk_068:p0061": ("B", "Working notes in HUI-071-2-31-000; review with adjacent pages."),
    "chunk_068:p0062": ("B", "Working notes in HUI-071-2-31-000; music/culture and 31.x.27-style date notation."),
    "chunk_068:p0063": ("B", "Working notes in HUI-071-2-31-000; open-letter/publication/music research notes."),
    "chunk_068:p0064": ("B", "Working notes in HUI-071-2-31-000; phonogram/institute/Stanford references."),
    "chunk_038:p0123": ("C", "False-positive control: 1932 Goethe commemoration newspaper report; not the anthropology/Rockefeller project."),
}

FIELDS = [
    "global_page","page_id","chunk_id","page_in_chunk","chars","nonempty",
    "quality_flags","inventory_refs","dates_1920_1935","years_1920_1935",
    "entities_exact","fuzzy_candidates","project_terms","doc_signals",
    "review_tier","review_reasons","layer_warning","manual_note"
]

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").replace("\u00ad", "")
    return re.sub(r"\s+", " ", s).lower()

def exact_entities(nt: str):
    return sorted({
        ent for ent, pats in ENTITY_PATTERNS.items()
        if any(re.search(p, nt, re.I | re.S) for p in pats)
    })

def project_terms(nt: str):
    checks = {
        "rockefeller_memorial": r"rockefeller\s+memorial|laura\s+spelman\s+rockefeller",
        "rockefeller_foundation": r"rockefeller\s+foundation",
        "social_sciences_holland": r"for\s+the\s+social\s+sciences\s+in\s+holland",
        "social_science": r"social\s+science\w*|sociale\s+wetenschap\w*|sociolog\w*",
        "anthropology": r"anthropolog\w*|ethnolog\w*|ethnograph\w*|volkenkund\w*",
        "institution": r"\bcentre\b|\bcentrum\b|\binstitute\b|\binstituut\w*|\bmuseum\b",
        "colonial": r"koloniaal\w*|colonial\w*|nederlandsch[-\s]?indi[eë]|netherlands\s+east\s+indies",
        "musicology": r"musicolog\w*|muziek\w*|phonogram\w*|gamelan\w*",
        "memorandum": r"\bmemorandum\b|\bmemoranda\b",
        "fieldwork": r"field\s*work|veldwerk",
        "primitive": r"\bprimitive\w*|\bprimitief\w*",
        "cultural_anthropology": r"cultural\s+anthropolog\w*|culturele\s+anthropolog\w*",
    }
    return [k for k, pat in checks.items() if re.search(pat, nt, re.I | re.S)]

def doc_signals(nt: str):
    out = []
    if re.search(r"instellingsnaam|inventarisnummer|archiefnaam:\s*archief\s+johan\s+huizinga", nt, re.I):
        out.append("archive_header")
    if re.search(r"prof\.?\s*dr\.?\s*j\.?\s*huizinga|witte\s+singel\s+34", nt, re.I):
        out.append("addressed_to_huizinga")
    if re.search(r"\bhooggeachte\s+professor\b|\bmy\s+dear\b|\bgeachte\b|\bamice\b|\bsehr\s+geehrt|\blieber\b", nt, re.I):
        out.append("correspondence")
    if re.search(r"rockefeller\s+memorial|laura\s+spelman\s+rockefeller", nt, re.I):
        out.append("rockefeller_letterhead_or_text")
    if re.search(r"\btrustees\b", nt, re.I) and re.search(r"rockefeller", nt, re.I):
        out.append("rockefeller_trustees")
    if re.search(r"\bmemorandum\b|\breport\b|\brapport\b|\bverslag\b", nt, re.I):
        out.append("report_or_memorandum")
    return out

def scan_page(p, global_page):
    t = p.get("text", "") or ""
    nt = norm(t)
    exact = exact_entities(nt)
    fuzzy = []
    if len(nt) >= 4:
        for ent, rx in FUZZY_RX.items():
            if ent in exact:
                continue
            anchors = FUZZY_ANCHORS.get(ent, ())
            if anchors and not any(a in nt for a in anchors):
                continue
            m = rx.search(nt)
            if m:
                s, i, d = m.fuzzy_counts
                fuzzy.append(f"{ent}|{m.group(0)}|s{s}i{i}d{d}")
    terms = project_terms(nt)
    docs = doc_signals(nt)
    dates = [m.group(0) for m in DATE_RX.finditer(t)] + [m.group(0) for m in NUM_DATE_RX.finditer(t)]
    years = sorted({int(y) for y in YEAR_RX.findall(t) if 1920 <= int(y) <= 1935})
    invs = sorted(set(INV_RX.findall(t)))

    tier, reasons = "", []
    if "social_sciences_holland" in terms:
        tier, reasons = "A", ["direct_social_sciences_holland_label"]
    if "rockefeller_memorial" in terms and 1931 in years:
        tier, reasons = "A", reasons + ["rockefeller_1931"]

    core = set(exact) & {"Malinowski","Nieuwenhuis","Van Vollenhoven","Van Eerde","Van de Sande Bakhuyzen"}
    if core and ({"anthropology","social_science"} & set(terms)) and any(y in (1931,1932,1933) for y in years):
        tier, reasons = "A", reasons + ["core_person_project_terms_1931_1933"]

    if not tier:
        if "rockefeller_memorial" in terms and any(y in (1932,1933) for y in years):
            tier, reasons = "B", ["rockefeller_letterhead_with_1932_1933"]
        elif "archive_header" in docs:
            tier, reasons = "B", ["archive_unit_boundary"]
        elif core and any(y in (1931,1932,1933) for y in years):
            tier, reasons = "B", ["core_person_1931_1933"]
        elif "musicology" in terms and ({"Hornbostel","Westenenk","Van Erp"} & set(exact)):
            tier, reasons = "B", ["kunst_musicology_institutional_chain"]

    if not tier:
        significant_terms = set(terms) - {"institution","primitive","colonial"}
        if exact or fuzzy or significant_terms or invs or "archive_header" in docs or "rockefeller_letterhead_or_text" in docs:
            tier, reasons = "C", ["research_signal"]

    layer = bool(
        "rockefeller_letterhead_or_text" in docs and len(t) > 700 and
        re.search(r"\b(?:cf\.|hoofdstuk|geschichte|islam|mystic|homo\s+ludens|sterrewacht|cicero|tacitus|medieval|encyclopaedia)\b", nt, re.I)
    )
    if layer:
        reasons.append("possible_letterhead_reuse_or_ocr_layering")

    manual_note = ""
    if p["page_id"] in MANUAL:
        tier, manual_note = MANUAL[p["page_id"]]
        reasons.append("manual_review")

    return {
        "global_page": global_page,
        "page_id": p["page_id"],
        "chunk_id": p["chunk_id"],
        "page_in_chunk": p["page_in_chunk"],
        "chars": len(t),
        "nonempty": bool(t.strip()),
        "quality_flags": ";".join(p.get("quality_flags") or []),
        "inventory_refs": ";".join(invs),
        "dates_1920_1935": ";".join(dates[:10]),
        "years_1920_1935": ";".join(map(str, years)),
        "entities_exact": ";".join(exact),
        "fuzzy_candidates": ";".join(fuzzy),
        "project_terms": ";".join(terms),
        "doc_signals": ";".join(docs),
        "review_tier": tier,
        "review_reasons": ";".join(reasons),
        "layer_warning": layer,
        "manual_note": manual_note,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_json")
    ap.add_argument("output_dir")
    args = ap.parse_args()

    src = Path(args.input_json)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    raw = src.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    data = json.loads(raw)
    pages = data["pages"]

    rows = [scan_page(p, i) for i, p in enumerate(pages, 1)]
    marked = [r for r in rows if r["review_tier"]]

    with (out / "page_markers_v1.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(marked)

    by_chunk = defaultdict(list)
    for r in rows:
        by_chunk[r["chunk_id"]].append(r)

    chunk_fields = [
        "chunk_id","pages_scanned","nonempty_pages","chars","A","B","C",
        "layer_warnings","rockefeller_pages","malinowski_pages",
        "anthropology_pages","social_science_pages","musicology_pages","archive_header_pages"
    ]
    with (out / "chunk_scan_summary_v1.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=chunk_fields)
        w.writeheader()
        for cid in sorted(by_chunk):
            rr = by_chunk[cid]
            w.writerow({
                "chunk_id": cid,
                "pages_scanned": len(rr),
                "nonempty_pages": sum(bool(r["nonempty"]) for r in rr),
                "chars": sum(int(r["chars"]) for r in rr),
                "A": sum(r["review_tier"] == "A" for r in rr),
                "B": sum(r["review_tier"] == "B" for r in rr),
                "C": sum(r["review_tier"] == "C" for r in rr),
                "layer_warnings": sum(bool(r["layer_warning"]) for r in rr),
                "rockefeller_pages": sum("Rockefeller" in r["entities_exact"] for r in rr),
                "malinowski_pages": sum("Malinowski" in r["entities_exact"] for r in rr),
                "anthropology_pages": sum("anthropology" in r["project_terms"] for r in rr),
                "social_science_pages": sum("social_science" in r["project_terms"] for r in rr),
                "musicology_pages": sum("musicology" in r["project_terms"] for r in rr),
                "archive_header_pages": sum("archive_header" in r["doc_signals"] for r in rr),
            })

    counts = Counter(r["review_tier"] for r in rows)
    manifest = {
        "scan_version": "v1",
        "input_file": src.name,
        "input_sha256": sha,
        "pages_scanned": len(rows),
        "nonempty_pages": sum(bool(r["nonempty"]) for r in rows),
        "empty_pages": sum(not bool(r["nonempty"]) for r in rows),
        "marked_rows": len(marked),
        "review_tiers": {k: counts.get(k, 0) for k in ["A","B","C"]},
        "policy": "full sequential scan; sparse output; exact and fuzzy identities kept separate",
    }
    (out / "scan_manifest_v1.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

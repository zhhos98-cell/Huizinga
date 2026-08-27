#!/usr/bin/env python3
"""Build the legacy PDF span manifest.

IMPORTANT: this script does NOT open PDF files and does NOT perform visual
verification.  It only records page spans supplied on the command line and
cross-references any existing correction-ledger actions.  Therefore its output
must never be used as evidence that a page was actually checked against the
original scan.

Strict re-proofreading is tracked separately in review/STRICT_REPROOFREAD_V2_STATUS.tsv
and requires page-by-page visual inspection before a page can be credited.
"""

import argparse
import csv
import json
from pathlib import Path


def parse_span(value: str):
    start, end, pdf = value.split(":", 2)
    return int(start), int(end), pdf


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chunk")
    parser.add_argument("span", nargs="+", type=parse_span)
    args = parser.parse_args()
    chunk = args.chunk.zfill(3)
    ledger_path = Path(f"corrections/chunk_{chunk}_manual.json")
    patches = json.loads(ledger_path.read_text(encoding="utf-8")) if ledger_path.exists() else []
    by_page = {}
    for patch in patches:
        by_page.setdefault(int(patch["page"]), []).append(patch["action"])

    output = Path(f"review/chunk_{chunk}/pdf_verification_log_v1.tsv")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(["page", "pdf", "verification", "json_action", "note"])
        for start, end, pdf in args.span:
            for page in range(start, end + 1):
                actions = by_page.get(page, [])
                writer.writerow([
                    f"p{page:04d}",
                    pdf,
                    "legacy_span_manifest_NOT_visual_verification",
                    ";".join(actions) if actions else "no_ledger_action",
                    "correction ledger contains action(s); re-check scan in strict v2"
                    if actions
                    else "page was only listed in a supplied span; no visual-check claim",
                ])


if __name__ == "__main__":
    main()

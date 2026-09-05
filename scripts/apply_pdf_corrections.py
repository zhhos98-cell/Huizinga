#!/usr/bin/env python3
"""Apply PDF-verified page/block corrections and emit an auditable corrected JSON."""

import argparse
import csv
import json
from pathlib import Path


IGNORE_MARKDOWN_LABELS = {
    "number", "footnote", "header", "header_image", "footer",
    "footer_image", "aside_text",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("chunk", help="three-digit chunk number, e.g. 070")
    args = parser.parse_args()
    chunk = args.chunk.zfill(3)

    source = Path(f"sources/ocr/paddle/raw/chunk_{chunk}.pdf_by_PaddleOCR-VL-1.6.json")
    ledger = Path(f"corrections/chunk_{chunk}_manual.json")
    corrected = Path(f"sources/ocr/paddle/corrected/chunk_{chunk}.pdf_by_PaddleOCR-VL-1.6.corrected.json")
    audit_path = Path(f"review/chunk_{chunk}/applied_patch_audit_v1.tsv")

    data = json.loads(source.read_text(encoding="utf-8"))
    patches = json.loads(ledger.read_text(encoding="utf-8"))
    audit = []
    touched_pages = set()

    for patch in patches:
        page_no = int(patch["page"])
        touched_pages.add(page_no)
        page = data[page_no - 1]
        blocks = page.setdefault("prunedResult", {}).setdefault("parsing_res_list", [])
        action = patch["action"]
        before = ""
        after = patch.get("content", "")
        block_id = patch.get("block_id", "")

        if action in {"replace_block", "drop_block"}:
            target = next(
                (b for b in blocks if int(b.get("block_id", -1)) == int(block_id)),
                None,
            )
            if target is None:
                raise RuntimeError(f"missing page {page_no} block {block_id}")
            before = target.get("block_content") or ""
            if action == "replace_block":
                target["block_content"] = after
                target["manual_correction"] = {
                    "source": patch.get("source", "PDF"),
                    "confidence": patch.get("confidence", "high"),
                    "reason": patch.get("reason", "PDF-verified correction"),
                }
            else:
                blocks[:] = [
                    b for b in blocks
                    if int(b.get("block_id", -1)) != int(block_id)
                ]
        elif action == "clear_page":
            before = "\n\n".join((b.get("block_content") or "") for b in blocks)
            blocks[:] = []
        elif action == "append_manual_block":
            new_id = max([int(b.get("block_id", -1)) for b in blocks] or [-1]) + 1
            blocks.append({
                "block_label": "text",
                "block_content": after,
                "block_bbox": patch.get("block_bbox", []),
                "block_id": new_id,
                "block_order": patch.get("block_order", new_id + 1),
                "group_id": new_id,
                "block_polygon_points": patch.get("block_polygon_points", []),
                "manual_correction": {
                    "source": patch.get("source", "PDF"),
                    "confidence": patch.get("confidence", "high"),
                    "reason": patch.get("reason", "PDF false-empty recovery"),
                },
            })
            block_id = new_id
        else:
            raise RuntimeError(f"unknown action: {action}")

        audit.append([
            page_no, action, block_id, before, after,
            patch.get("confidence", ""), patch.get("source", "PDF"),
            patch.get("reason", ""), patch.get("review_pdf") or "-",
        ])

    for page_no in sorted(touched_pages):
        page = data[page_no - 1]
        markdown = page.setdefault("markdown", {"text": "", "images": {}})
        parts = []
        for block in page.get("prunedResult", {}).get("parsing_res_list", []):
            content = (block.get("block_content") or "").strip()
            if content and block.get("block_label") not in IGNORE_MARKDOWN_LABELS:
                parts.append(content)
        markdown["text"] = "\n\n".join(parts)

    corrected.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    with audit_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow([
            "page", "action", "block_id", "before", "after", "confidence",
            "source", "reason", "review_pdf",
        ])
        writer.writerows(audit)


if __name__ == "__main__":
    main()

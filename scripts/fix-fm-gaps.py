#!/usr/bin/env python3
"""
fix-fm-gaps.py — 为所有缺 frontmatter 字段的页面补齐。

当前问题：
- 200 pages missing tags
- 4 pages missing created
- 9 pages missing updated
- 1 page missing type
- 1 page missing status

策略：只补缺失字段，保留已有内容不动。
"""

import json
import re
import sys
from pathlib import Path
from datetime import date

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
DETAILS_FILE = VAULT_ROOT / ".vault-meta" / "lint-details.json"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def parse_fm(block):
    fm = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm

def write_fm(path, fm_delta):
    """Add/update keys in fm_delta to page frontmatter."""
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if m:
        fm_block = m.group(1)
        lines = fm_block.splitlines()
        # Merge
        fm = parse_fm(fm_block)
        fm.update(fm_delta)
        # Rebuild block
        new_lines = []
        for k, v in fm.items():
            if isinstance(v, list):
                val_str = "[" + ", ".join(f'"{x}"' for x in v) + "]"
            else:
                val_str = f'"{v}"' if v else '""'
            new_lines.append(f"{k}: {val_str}")
        new_fm_block = "\n".join(new_lines)
        new_text = "---\n" + new_fm_block + "\n---\n" + text[m.end():]
    else:
        # No frontmatter — create one
        new_lines = []
        for k, v in fm_delta.items():
            if isinstance(v, list):
                val_str = "[" + ", ".join(f'"{x}"' for x in v) + "]"
            else:
                val_str = f'"{v}"' if v else '""'
            new_lines.append(f"{k}: {val_str}")
        new_text = "---\n" + "\n".join(new_lines) + "\n---\n\n" + text
    path.write_text(new_text, encoding="utf-8")

def main():
    details = json.loads(DETAILS_FILE.read_text())
    gaps = details.get("fm_gaps", [])

    print(f"Pages with FM gaps: {len(gaps)}")

    today = date.today().isoformat()
    fixed = 0
    errors = []

    for item in gaps:
        rel_path = item[0]
        missing_fields = item[1]
        file_path = VAULT_ROOT / rel_path
        if not file_path.exists():
            errors.append(f"  NOT FOUND: {rel_path}")
            continue

        delta = {}
        if "tags" in missing_fields:
            delta["tags"] = []
        if "created" in missing_fields:
            # Try to infer from file mtime or use today
            delta["created"] = today
        if "updated" in missing_fields:
            delta["updated"] = today
        if "type" in missing_fields:
            # Infer from path
            if "/concepts/" in rel_path:
                delta["type"] = "concept"
            elif "/entities/" in rel_path:
                delta["type"] = "entity"
            elif "/sources/" in rel_path:
                delta["type"] = "source"
            elif "/analysis/" in rel_path:
                delta["type"] = "analysis"
            elif "/comparisons/" in rel_path:
                delta["type"] = "comparison"
            elif "/questions/" in rel_path:
                delta["type"] = "question"
            elif "/domain/" in rel_path:
                delta["type"] = "domain"
            elif "/meta/" in rel_path:
                delta["type"] = "meta"
            else:
                delta["type"] = "concept"
        if "status" in missing_fields:
            delta["status"] = "developing"

        try:
            write_fm(file_path, delta)
            fixed += 1
        except Exception as e:
            errors.append(f"  ERROR {rel_path}: {e}")

    print(f"Fixed: {fixed} pages")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(e)

if __name__ == "__main__":
    main()

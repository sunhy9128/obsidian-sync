#!/usr/bin/env python3
"""One-pass wiki lint scanner. Writes raw_stats.json for the report builder."""
import json, os, re, sys
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI = ROOT / "wiki"
ADDRESS_RE = re.compile(r"^(c|l)-([0-9]{6})$")
WIKILINK_RE = re.compile(r"\[\[([^\]\|#^]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
FOLD_FILES = {"_index.md", "index.md", "log.md", "hot.md", "overview.md",
              "dashboard.md", "dashboard.base", "Wiki Map.md", "getting-started.md"}

def normalize(name):
    return name.strip()

def scan_file(path):
    """Return (frontmatter_dict, all_wikilinks_list, body_text)."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}, [], ""
    fm = {}
    m = FRONTMATTER_RE.match(text)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" ") and not line.startswith("#"):
                k, _, v = line.partition(":")
                k = k.strip()
                v = v.strip()
                if v.startswith("[") and v.endswith("]"):
                    inner = v[1:-1]
                    fm[k] = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
                else:
                    fm[k] = v.strip('"').strip("'")
    links = WIKILINK_RE.findall(text)
    body = text[m.end():] if m else text
    return fm, links, body

def main():
    files = []
    for p in WIKI.rglob("*.md"):
        if any(part.startswith(".") for part in p.parts):
            continue
        rel = str(p.relative_to(ROOT))
        files.append(rel)
    files.sort()

    # Map filename (no ext) -> paths (for wikilink resolution)
    name_to_paths = defaultdict(list)
    for f in files:
        stem = Path(f).stem
        name_to_paths[stem].append(f)

    page_records = []
    all_links = []  # (source_path, target_name)
    page_types = Counter()
    page_statuses = Counter()

    for f in files:
        full = ROOT / f
        fm, links, body = scan_file(full)
        page_records.append({
            "path": f,
            "stem": Path(f).stem,
            "type": fm.get("type", ""),
            "status": fm.get("status", ""),
            "created": fm.get("created", ""),
            "updated": fm.get("updated", ""),
            "tags": fm.get("tags", []),
            "address": fm.get("address", ""),
            "in_folds": "/folds/" in f,
            "filename_is_index": Path(f).name in FOLD_FILES,
            "links": links,
            "body_len": len(body.strip()),
        })
        for l in links:
            all_links.append((f, normalize(l)))
        if fm.get("type"):
            page_types[fm["type"]] += 1
        if fm.get("status"):
            page_statuses[fm["status"]] += 1

    # Inbound backlink index
    inbound = defaultdict(list)
    for src, tgt in all_links:
        inbound[tgt].append(src)

    stats = {
        "files": files,
        "records": page_records,
        "all_links": [list(t) for t in all_links],
        "inbound": {k: v for k, v in inbound.items()},
        "name_to_paths": {k: v for k, v in name_to_paths.items()},
        "page_types": dict(page_types),
        "page_statuses": dict(page_statuses),
        "total_files": len(files),
    }
    out = ROOT / ".vault-meta" / "lint-stats.json"
    out.write_text(json.dumps(stats, ensure_ascii=False), encoding="utf-8")
    print(f"Scanned {len(files)} files -> {out}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One-pass wiki lint scanner. Writes lint-stats.json for the report builder.

v2 (2026-07-30): 正确解析 frontmatter 多行列表块（aliases/tags/related/sources），
并把 alias、完整相对路径、大小写不敏感 key 一并加入 name_to_paths 索引，
根治「alias/路径前缀/大小写」类 wikilink 误报为死链的问题。
"""
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

def _parse_yaml_value(v):
    """解析单行 YAML 值：去引号，识别内联数组 [a, b]。"""
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1]
        return [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
    return v.strip('"').strip("'")

def parse_frontmatter(text):
    """解析 frontmatter，正确处理多行列表块（aliases/tags/related 等）。
    返回 dict：标量为 str，列表为 list。"""
    fm = {}
    m = FRONTMATTER_RE.match(text)
    if not m:
        return fm, m
    fm_text = m.group(1)
    current_key = None
    current_list = None
    for line in fm_text.splitlines():
        # 列表项：  - value 或 - value
        if re.match(r"^\s+-\s+", line) and current_key is not None:
            val = re.split(r"^\s+-\s+", line)[1].strip().strip('"').strip("'")
            if val:
                if current_list is None:
                    current_list = []
                current_list.append(val)
            continue
        # key: value 行（顶层 key，非缩进）
        if ":" in line and not line.startswith(" ") and not line.startswith("\t") and not line.startswith("#"):
            # 先把上一个列表 key 落盘
            if current_key is not None and current_list is not None:
                fm[current_key] = current_list
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            if v == "":
                # 可能是多行列表块的开始，等后续  - xxx
                current_key = k
                current_list = None
            else:
                fm[k] = _parse_yaml_value(v)
                current_key = k
                current_list = None if not isinstance(fm[k], list) else fm[k]
            continue
        # 缩进的非列表行（如嵌套对象），结束当前列表收集
        if line.startswith(" ") or line.startswith("\t"):
            if line.strip() == "":
                continue
            # 其他缩进行不处理，但保留已收集的列表
            continue
        # 空行或注释
        if line.strip() == "" or line.startswith("#"):
            continue
    # 收尾：最后一个列表 key 落盘
    if current_key is not None and current_list is not None:
        fm[current_key] = current_list
    return fm, m

def scan_file(path):
    """Return (frontmatter_dict, all_wikilinks_list, body_text)."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}, [], ""
    fm, m = parse_frontmatter(text)
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
    # 同时把 alias、完整相对路径、大小写不敏感 key 一并加入索引。
    # 这样下游 lint-analyze.py 的 `if tgt not in name_to_paths` 判定
    # 能正确识别 alias/路径前缀/大小写变体，不再误报死链。
    name_to_paths = defaultdict(list)

    def _add(key, path):
        key = normalize(key)
        if key and path not in name_to_paths[key]:
            name_to_paths[key].append(path)

    for f in files:
        stem = Path(f).stem
        _add(stem, f)                          # 1. stem（原有行为）
        _add(stem.lower(), f)                  # 2. stem 小写（大小写不敏感）
        rel_no_ext = f[:-3] if f.endswith(".md") else f   # 去 .md 后缀的完整路径
        _add(rel_no_ext, f)                    # 3. 完整相对路径（支持 [[wiki/xxx/yyy]]）
        _add(rel_no_ext.lower(), f)            # 4. 完整路径小写

    # 第二遍：解析 aliases 并加入索引
    for f in files:
        full = ROOT / f
        try:
            text = full.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, _ = parse_frontmatter(text)
        aliases = fm.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases] if aliases else []
        if not isinstance(aliases, list):
            continue
        for a in aliases:
            if not a:
                continue
            _add(a, f)                         # 5. alias 原文
            _add(a.lower(), f)                 # 6. alias 小写

    page_records = []
    all_links = []  # (source_path, target_name)
    page_types = Counter()
    page_statuses = Counter()

    for f in files:
        full = ROOT / f
        fm, links, body = scan_file(full)
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags] if tags else []
        page_records.append({
            "path": f,
            "stem": Path(f).stem,
            "type": fm.get("type", ""),
            "status": fm.get("status", ""),
            "created": fm.get("created", ""),
            "updated": fm.get("updated", ""),
            "tags": tags,
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

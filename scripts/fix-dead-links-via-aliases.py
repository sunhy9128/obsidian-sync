#!/usr/bin/env python3
"""
fix-dead-links-via-aliases.py
将死链目标批量添加到 canonical 页面的 aliases。

死链分两类：
1. 路径变体 (wiki/comparisons/X vs wiki/concepts/X): 链接相对路径解析错误
   → 在 canonical 页面添加 "comparisons/X" 或 "entities/X" 等作为 alias
2. 标点后缀 (X： vs X): wikilink 尾标点被错误包含
   → 去掉标点后，在 canonical 页面添加带标点的原始 target 作为 alias
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI_ROOT = VAULT_ROOT / "wiki"
DETAILS_FILE = VAULT_ROOT / ".vault-meta" / "lint-details.json"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

# Characters that appear as trailing "garbage" in wiki link targets
# 中文冒号, 西文冒号, 句号, 逗号, 中点, 波浪号, 空格
PUNCT_STRIP = re.compile(r"[:：.．,，·•~ ]+$")

def get_stem(path):
    """Extract the meaningful name from a path like wiki/concepts/X or wiki/entities/X"""
    p = Path(path)
    return p.stem  # removes extension

def read_fm(path):
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            fm[k] = v
    return fm, text

def write_aliases(path, new_aliases):
    """Add new aliases to existing frontmatter aliases: field."""
    fm, text = read_fm(path)
    m = FRONTMATTER_RE.match(text)

    existing_raw = fm.get("aliases", "")
    if isinstance(existing_raw, list):
        existing = set(existing_raw)
    elif existing_raw:
        # Parse comma or newline separated
        existing = set(a.strip().strip('"').strip("'") for a in re.split(r"[,\n]", existing_raw) if a.strip())
    else:
        existing = set()

    # Also parse inline YAML list in frontmatter block
    if m:
        fm_block = m.group(1)
        for line in fm_block.splitlines():
            l = line.strip()
            if l.startswith("-"):
                existing.add(l.lstrip("- ").strip('"').strip("'"))

    to_add = [a for a in new_aliases if a and a not in existing]
    if not to_add:
        return 0

    if m:
        fm_block = m.group(1)
        lines = fm_block.splitlines()
        # Find where aliases block ends
        new_fm_lines = []
        i = 0
        alias_end_idx = None
        while i < len(lines):
            l = lines[i].strip()
            if re.match(r"^aliases?\s*:", l):
                # Include this line and all following list items
                indent = len(lines[i]) - len(lines[i].lstrip())
                new_fm_lines.append(lines[i])
                i += 1
                while i < len(lines):
                    cur_indent = len(lines[i]) - len(lines[i].lstrip()) if lines[i].strip() else 999
                    if lines[i].strip() and cur_indent <= indent and not lines[i].strip().startswith("-"):
                        # End of alias block
                        break
                    new_fm_lines.append(lines[i])
                    i += 1
                # Append new aliases before the block ends
                for als in to_add:
                    new_fm_lines.append(f"{' '*indent}- {als}")
                continue
            new_fm_lines.append(lines[i])
            i += 1

        new_fm = "\n".join(new_fm_lines)
        new_text = "---\n" + new_fm + "\n---\n" + text[m.end():]
    else:
        alias_block = "\n".join(f"- {a}" for a in to_add)
        new_text = f"---\naliases:\n{alias_block}\n---\n\n{text}"

    path.write_text(new_text, encoding="utf-8")
    return len(to_add)

def main():
    details = json.loads(DETAILS_FILE.read_text())
    dl = details.get("dead_links", {})
    print(f"Total dead link targets: {len(dl)}")

    # Build stem -> (path, stem) map for all wiki files
    stem_map = {}  # stem -> rel_path
    for p in WIKI_ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in p.parts):
            continue
        rel = str(p.relative_to(VAULT_ROOT))
        stem = Path(rel).stem
        if stem not in stem_map:
            stem_map[stem] = rel

    print(f"Wiki pages indexed: {len(stem_map)}")

    # Categorize and resolve each dead target
    path_aliases = defaultdict(list)   # canonical_path -> [alias to add]
    name_aliases = defaultdict(list)   # canonical_path -> [alias to add]
    real_missing = []

    for target, refs in dl.items():
        # Skip if it's an explicit wiki/ or raw/ path that's truly missing
        if target.startswith("wiki/meta/") or target.startswith("raw/"):
            real_missing.append((target, "special path"))
            continue
        if target.endswith(".canvas") or target.endswith(".md"):
            real_missing.append((target, "canvas/md"))
            continue

        # Pattern A: path-style (wiki/concepts/X or wiki/entities/X etc.)
        path_m = re.match(r"^(wiki/(?:concepts|entities|sources|analysis|comparisons|questions|domain|fold))/([^\s:：.．,，·]+)$", target)
        if path_m:
            dir_part, name = path_m.group(1), path_m.group(2)
            if name in stem_map:
                canonical = stem_map[name]
                # Add the wrong path as alias
                path_aliases[canonical].append(target)
                continue

        # Pattern B: name-style with trailing punctuation (MLF：, 美联储：, etc.)
        clean = PUNCT_STRIP.sub("", target)
        if clean in stem_map and clean != target:
            canonical = stem_map[clean]
            name_aliases[canonical].append(target)
            continue

        # Pattern C: bare name with no punctuation — check if it maps directly
        if target in stem_map:
            # Already exists as exact stem
            continue

        real_missing.append((target, "no match"))

    print(f"\nPath-alias fixes: {len(path_aliases)} canonical pages")
    print(f"Name-alias fixes: {len(name_aliases)} canonical pages")
    print(f"Real missing targets: {len(real_missing)}")

    total_aliases_added = 0
    pages_updated = 0

    # Apply path aliases
    for canonical, aliases in sorted(path_aliases.items(), key=lambda x: -len(x[1])):
        path = VAULT_ROOT / canonical
        n = write_aliases(path, aliases)
        if n:
            total_aliases_added += n
            pages_updated += 1
            print(f"  PATH [{canonical}]: +{n} alias(es): {aliases[:3]}{'...' if len(aliases)>3 else ''}")

    # Apply name aliases
    for canonical, aliases in sorted(name_aliases.items(), key=lambda x: -len(x[1])):
        path = VAULT_ROOT / canonical
        n = write_aliases(path, aliases)
        if n:
            total_aliases_added += n
            pages_updated += 1
            print(f"  NAME [{canonical}]: +{n} alias(es): {aliases[:3]}{'...' if len(aliases)>3 else ''}")

    print(f"\nTotal: {pages_updated} pages updated, {total_aliases_added} alias(es) added")
    print(f"Real missing targets ({len(real_missing)}):")
    for t, reason in sorted(real_missing, key=lambda x: -len(dl.get(x[0], []))):
        print(f"  [{len(dl[t])} refs] {t}  ({reason})")

if __name__ == "__main__":
    main()

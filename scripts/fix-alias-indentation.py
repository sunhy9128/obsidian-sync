#!/usr/bin/env python3
"""
fix-alias-indentation.py — 重建所有 aliases 块，统一为 2 空格缩进。

问题：不同工具写入的缩进不一致（4空格 vs 2空格），导致 YAML 解析报错。
修复策略：直接从原始行提取 aliases，重新写入为一致的 2 空格缩进列表。
"""

import re
from pathlib import Path

ROOT = Path("/Users/mac/Documents/金融知识库")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
WIKI_ALIAS_RE = re.compile(r"^\s*-\s+(wiki/\w+/\S+)\s*$", re.MULTILINE)
# Matches a list item line: "- value" (with any indent)
YAML_LIST_ITEM_RE = re.compile(r"^(\s*)- (.+)$")

fixed_files = 0
fixed_aliases = 0

for p in sorted(ROOT.glob("wiki/**/*.md")):
    if ".obsidian" in str(p):
        continue
    text = p.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        continue

    raw_block = m.group(1)
    raw_lines = raw_block.splitlines()

    # Find aliases: key line
    alias_key_idx = None
    alias_key_indent = None
    for i, line in enumerate(raw_lines):
        ls = line.strip()
        if re.match(r"^aliases?\s*:", ls):
            alias_key_idx = i
            alias_key_indent = len(line) - len(ls)
            break

    if alias_key_idx is None:
        continue

    # Check if there are any wiki/... alias list items anywhere in the block
    has_wiki_alias = bool(WIKI_ALIAS_RE.search(raw_block))
    if not has_wiki_alias:
        continue

    # Extract all list items that belong to the aliases block
    # Items belong if they are:
    # 1. A list item at deeper indent than aliases: key (direct child)
    # 2. OR a wiki/... path alias even if at column 0 (broken output from fix-dead-links)
    collected_aliases = []
    seen_aliases = set()

    for i, line in enumerate(raw_lines):
        if i <= alias_key_idx:
            continue

        ls = line.strip()
        if ls == "":
            continue

        # Indent of this line
        line_indent = len(line) - len(ls)

        # End of aliases block: non-list line at or below aliases: key indent
        if line_indent <= alias_key_indent and not ls.startswith("-"):
            break

        # Check for wiki/... path alias (possibly unindented - column 0)
        wiki_match = re.match(r"^\s*-\s+(wiki/\w+/\S+)\s*$", ls)
        if wiki_match:
            val = wiki_match.group(1)
            if val not in seen_aliases:
                seen_aliases.add(val)
                collected_aliases.append(val)
            continue

        # Check for regular string alias list item (must be a child of aliases:)
        if ls.startswith("- "):
            # It must be a proper child of aliases (deeper indent)
            if line_indent > alias_key_indent:
                val = ls[2:].strip().strip('"').strip("'")
                if val and val not in seen_aliases:
                    seen_aliases.add(val)
                    collected_aliases.append(val)

    if not collected_aliases:
        continue

    # Rebuild aliases block with consistent 2-space indent
    item_indent = " " * (alias_key_indent + 2)
    aliases_block_lines = [f"{' '*alias_key_indent}aliases:"]
    for a in collected_aliases:
        aliases_block_lines.append(f'{item_indent}- "{a}"')

    # Replace the old aliases block in raw_lines
    # Find where aliases block ends
    alias_end_idx = len(raw_lines)
    for i in range(alias_key_idx + 1, len(raw_lines)):
        ls = raw_lines[i].strip()
        if ls == "":
            continue
        line_indent = len(raw_lines[i]) - len(ls)
        # End when we hit a non-list line at or below the aliases: key indent
        if line_indent <= alias_key_indent and not ls.startswith("-"):
            alias_end_idx = i
            break
        # Also end on another top-level key
        if line_indent <= alias_key_indent and ls and not ls.startswith("-"):
            alias_end_idx = i
            break

    new_raw_lines = raw_lines[:alias_key_idx] + aliases_block_lines + raw_lines[alias_end_idx:]
    new_raw_block = "\n".join(new_raw_lines)
    new_text = "---\n" + new_raw_block + "\n---\n" + text[m.end() :]

    p.write_text(new_text, encoding="utf-8")
    fixed_files += 1
    fixed_aliases += len(collected_aliases)
    if fixed_files <= 10:
        print(f"  Fixed: {p.relative_to(ROOT)} ({len(collected_aliases)} aliases)")

print(f"\nTotal files fixed: {fixed_files}, total aliases: {fixed_aliases}")

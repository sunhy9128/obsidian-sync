#!/usr/bin/env python3
"""
最终验证脚本：使用 fix_high_priority.py 的修复版解析器
"""

import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI_ROOT = VAULT_ROOT / "wiki"

def parse_frontmatter(content):
    """修复后的解析器——支持顶格和缩进列表项"""
    if not content.startswith("---"):
        return {}
    try:
        end = content.index("---", 3)
        fm_text = content[3:end]
    except ValueError:
        return {}
    result = {}
    current_key = None
    current_list = None
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            item = stripped[2:].strip()
            if (item.startswith('"') and item.endswith('"')) or (item.startswith("'") and item.endswith("'")):
                item = item[1:-1]
            if current_list is not None:
                current_list.append(item)
            continue
        m = re.match(r'^(\w[\w_-]*)\s*:\s*(.*)', line)
        if m:
            key = m.group(1)
            value = m.group(2).strip()
            if value == "":
                current_key = key
                current_list = []
                result[key] = current_list
            elif value.startswith('"') and value.endswith('"'):
                result[key] = value[1:-1]
                current_key = None
                current_list = None
            elif value.startswith("'") and value.endswith("'"):
                result[key] = value[1:-1]
                current_key = None
                current_list = None
            elif value.startswith('[') and value.endswith(']'):
                inner = value[1:-1].strip()
                if inner:
                    items = [s.strip().strip('"').strip("'") for s in inner.split(",") if s.strip()]
                    result[key] = items
                else:
                    result[key] = []
                current_key = None
                current_list = None
            else:
                result[key] = value
                current_key = None
                current_list = None
        elif line.startswith("  - ") and current_list is not None:
            item = line[4:].strip().strip('"').strip("'")
            current_list.append(item)
    return result

print("=" * 70)
print("最终验证：使用修复版解析器")
print("=" * 70)

# 读取所有页面和别名
pages = set()
page_paths = {}
aliases_map = {}

for md_file in WIKI_ROOT.rglob("*.md"):
    rel = md_file.relative_to(VAULT_ROOT)
    stem = md_file.stem
    pages.add(stem)
    pages.add(str(rel.with_suffix("")))
    pages.add(str(rel))
    pages.add(md_file.name)
    page_paths[stem] = str(rel)
    try:
        content = md_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        if "aliases" in fm and isinstance(fm["aliases"], list):
            for alias in fm["aliases"]:
                pages.add(alias)
                aliases_map[alias] = stem
    except Exception:
        pass

print(f"页面数: {len(page_paths)}")
print(f"别名数: {len(aliases_map)}")

# 扫描断链
WIKILINK_PATTERN = re.compile(r'\[\[([^\]\|]+?)(?:\|[^\]]*)?\]\]')

dead_links = defaultdict(set)
for md_file in WIKI_ROOT.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
    rel_source = str(md_file.relative_to(VAULT_ROOT))
    for match in WIKILINK_PATTERN.finditer(content):
        target = match.group(1).strip()
        if target.startswith("#"):
            continue
        if "|" in match.group(0):
            target = target.split("|")[0].strip()
        if "#" in target:
            target = target.split("#")[0].strip()
        if target not in pages:
            dead_links[target].add(rel_source)

print(f"断链目标数: {len(dead_links)}")
print(f"断链引用处数: {sum(len(v) for v in dead_links.values())}")

# HIGH 优先级
high = sorted(
    [(t, len(s)) for t, s in dead_links.items() if len(s) >= 3],
    key=lambda x: -x[1]
)

print(f"\n🚨 HIGH 优先级剩余 ({len(high)} 个):")
print("-" * 70)

real_missing = []
for t, n in high:
    # 分类
    if t.startswith("wiki/") or t.startswith("analysis/") or t.startswith("comparisons/") or t.startswith("raw/"):
        cat = "路径错误"
    elif re.match(r"meta/lint-report", t):
        cat = "历史"
    elif t == "meta/dashboard":
        cat = "Bases文件"
    elif t in {"Entities", "Sources", "Concepts", "Claude Canvas", "Foo", "X", "X.md"}:
        cat = "占位符"
    elif re.match(r'^[a-z\-]+$', t):
        cat = "OCR/拼音"
    else:
        cat = "⚠️真实缺失"
        real_missing.append((t, n))
    print(f"  [{cat:12s}] [[{t}]] ({n} 处)")

print()
print(f"📋 真实需要处理的 HIGH 优先级: {len(real_missing)} 个")
for t, n in real_missing:
    print(f"  ⚠️ [[{t}]] ({n} 处)")

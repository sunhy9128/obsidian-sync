#!/usr/bin/env python3
"""
完整修复脚本（含 frontmatter 解析 bug 修复）

修复 parse_frontmatter 函数以支持顶格列表格式：
```yaml
aliases:
- foo   ← 顶格（YAML 允许）
- bar
```

而不是只能识别：
```yaml
aliases:
  - foo  ← 缩进（严格 YAML）
  - bar
```

并清理上一轮创建的错误 stub。
"""

import re
from pathlib import Path
from datetime import date
from collections import defaultdict

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI_ROOT = VAULT_ROOT / "wiki"

# ============ 修复后的 frontmatter 解析器 ============

def parse_frontmatter(content):
    """解析 frontmatter，支持顶格列表格式"""
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

        # 空行
        if not stripped:
            continue

        # 列表项（顶格或缩进）
        if stripped.startswith("- "):
            item = stripped[2:].strip()
            # 去掉包裹的引号
            if (item.startswith('"') and item.endswith('"')) or \
               (item.startswith("'") and item.endswith("'")):
                item = item[1:-1]
            if current_list is not None:
                current_list.append(item)
            continue

        # key: value
        m = re.match(r'^(\w[\w_-]*)\s*:\s*(.*)', line)
        if m:
            key = m.group(1)
            value = m.group(2).strip()

            if value == "":
                # 可能是列表开始
                current_key = key
                current_list = []
                result[key] = current_list
                continue
            elif value.startswith('"') and value.endswith('"'):
                result[key] = value[1:-1]
                current_key = None
                current_list = None
            elif value.startswith("'") and value.endswith("'"):
                result[key] = value[1:-1]
                current_key = None
                current_list = None
            elif value.startswith('[') and value.endswith(']'):
                # 单行列表
                inner = value[1:-1].strip()
                if inner:
                    items = []
                    for s in inner.split(","):
                        s = s.strip().strip('"').strip("'")
                        if s:
                            items.append(s)
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
            # 缩进列表项（兼容旧格式）
            item = line[4:].strip().strip('"').strip("'")
            current_list.append(item)

    return result

# ============ 验证修复 ============
print("=" * 70)
print("验证 frontmatter 解析修复")
print("=" * 70)

test_file = WIKI_ROOT / "entities" / "土耳其.md"
content = test_file.read_text(encoding="utf-8")
fm = parse_frontmatter(content)
print(f"\n测试文件: {test_file.name}")
print(f"aliases: {fm.get('aliases')}")

if fm.get('aliases'):
    if "Turkey (土耳其)" in fm['aliases']:
        print("✅ Turkey (土耳其) 已被识别为别名")
    else:
        print("⚠️  Turkey (土耳其) 不在别名中")

# ============ 重新扫描所有页面（含 aliases）============
print("\n" + "=" * 70)
print("重新扫描所有页面...")
print("=" * 70)

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

# ============ 扫描断链 ============
WIKILINK_PATTERN = re.compile(r'\[\[([^\]\|]+?)(?:\|[^\]]*)?\]\]')

def extract_wikilinks(content):
    links = []
    for match in WIKILINK_PATTERN.finditer(content):
        target = match.group(1).strip()
        if target.startswith("#"):
            continue
        if "|" in match.group(0):
            target = target.split("|")[0].strip()
        if "#" in target:
            target = target.split("#")[0].strip()
        if target:
            links.append(target)
    return links

dead_links = defaultdict(set)
md_files = list(WIKI_ROOT.rglob("*.md"))

for md_file in md_files:
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
    rel_source = str(md_file.relative_to(VAULT_ROOT))
    for target in extract_wikilinks(content):
        if target not in pages:
            dead_links[target].add(rel_source)

print(f"\n断链目标数: {len(dead_links)}")
print(f"断链引用处数: {sum(len(v) for v in dead_links.values())}")

# ============ 清理上一轮创建的误判 stub ============
print("\n" + "=" * 70)
print("清理上一轮创建的误判 stub...")
print("=" * 70)

# 这些是上一轮错误创建或不需要的 stub
TO_DELETE = [
    # 误判（已存在别名）
    "Turkey (土耳其)", "New Glenn", "土耳其", "巴基斯坦", "环球时报", "苹果", "长江电力",
    "MACD 指标", "存储芯片", "世界杯小组赛",
    # 占位符/OCR
    "Foo", "X", "X.md.md", "_1.md", "a-gu-feng-ge-lun-dong.md", "bajisitan.md",
    "bezos.md", "jd.md", "lanseqiyuan.md", "target.md", "existing.md",
    "Three laws of motion", "Turkey (土耳其)", "fold-template", "wiki-fold",
]

deleted = 0
for f in TO_DELETE:
    for path in WIKI_ROOT.rglob(f):
        if path.is_file():
            rel = path.relative_to(VAULT_ROOT)
            try:
                path.unlink()
                print(f"  🗑️  删除: {rel}")
                deleted += 1
            except Exception as e:
                print(f"  ❌ 删除失败: {rel}: {e}")

print(f"\n共删除 {deleted} 个误判 stub")

# ============ 重新扫描验证 ============
print("\n" + "=" * 70)
print("清理后重新扫描验证...")
print("=" * 70)

# 重新扫描
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

dead_links = defaultdict(set)
for md_file in WIKI_ROOT.rglob("*.md"):
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
    rel_source = str(md_file.relative_to(VAULT_ROOT))
    for target in extract_wikilinks(content):
        if target not in pages:
            dead_links[target].add(rel_source)

print(f"页面数: {len(page_paths)}")
print(f"别名数: {len(aliases_map)}")
print(f"断链目标数: {len(dead_links)}")
print(f"断链引用处数: {sum(len(v) for v in dead_links.values())}")

# HIGH 优先级
high = sorted(
    [(t, len(s)) for t, s in dead_links.items() if len(s) >= 3],
    key=lambda x: -x[1]
)
print(f"\nHIGH 优先级剩余: {len(high)} 个")
for t, n in high[:30]:
    print(f"  [[{t}]] ({n} 处)")

#!/usr/bin/env python3
"""
完整扫描 + 分类 + 报告生成（含 aliases 检查）
"""

import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI_ROOT = VAULT_ROOT / "wiki"

# 读取 frontmatter
def parse_frontmatter(content):
    """简单解析 frontmatter，返回 dict"""
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
    current_scalar = []

    for line in fm_text.split("\n"):
        # key: value
        m = re.match(r'^(\w[\w_]*)\s*:\s*(.*)', line)
        if m:
            key = m.group(1)
            value = m.group(2).strip()

            if value == "":
                # 可能是列表开始
                current_key = key
                current_list = []
                current_scalar = []
                result[key] = current_list
                continue
            elif value.startswith('"') and value.endswith('"'):
                # 字符串
                result[key] = value[1:-1]
                current_key = None
                current_list = None
            elif value.startswith('[') and value.endswith(']'):
                # 单行列表
                inner = value[1:-1].strip()
                if inner:
                    result[key] = [s.strip().strip('"').strip("'") for s in inner.split(",")]
                else:
                    result[key] = []
                current_key = None
                current_list = None
            else:
                # 普通值
                result[key] = value
                current_key = None
                current_list = None
        elif line.startswith("  - ") and current_list is not None:
            # 列表项
            item = line[4:].strip().strip('"').strip("'")
            current_list.append(item)
        elif line.strip() and current_key and not line.startswith(" "):
            # 新键
            pass

    return result

def get_all_pages():
    """获取所有页面（含 aliases）"""
    pages = set()  # 主名
    aliases_map = {}  # alias -> 主页面
    page_paths = {}

    for md_file in WIKI_ROOT.rglob("*.md"):
        rel = md_file.relative_to(VAULT_ROOT)
        stem = md_file.stem

        # 添加多种形式
        pages.add(stem)
        pages.add(str(rel.with_suffix("")))
        pages.add(str(rel))
        pages.add(md_file.name)
        pages.add(rel.name)

        page_paths[stem] = str(rel)

        # 读取 aliases
        try:
            content = md_file.read_text(encoding="utf-8")
            fm = parse_frontmatter(content)
            if "aliases" in fm and isinstance(fm["aliases"], list):
                for alias in fm["aliases"]:
                    pages.add(alias)
                    aliases_map[alias] = stem
        except Exception:
            pass

    return pages, aliases_map, page_paths

WIKILINK_PATTERN = re.compile(r'\[\[([^\]\|]+?)(?:\|[^\]]*)?\]\]')

def extract_wikilinks(content):
    links = []
    for match in WIKILINK_PATTERN.finditer(content):
        target = match.group(1).strip()
        if target.startswith("#"):
            continue
        if "|" in match.group(0):
            target = target.split("|")[0].strip()
        if target:
            links.append(target)
    return links

def classify_dead_link(target, sources, all_pages):
    """分类单个断链"""

    # 1. canvas 文件
    if target.endswith(".canvas"):
        return "false_positive", "canvas 文件，不是 markdown 页面", "误报"

    # 2. 旧 lint 报告
    if re.match(r"meta/lint-report-\d{4}-\d{2}-\d{2}", target):
        return "historical", "历史 lint 报告，引用属正常", "历史"

    # 3. 反斜杠结尾
    if target.endswith("\\"):
        return "false_positive", "反斜杠结尾（markdown 转义错误）", "误报"

    # 4. 反引号
    if "`" in target:
        return "false_positive", "包含反引号（代码块误读）", "误报"

    # 5. 路径错误（wiki/ 开头）
    if target.startswith("wiki/"):
        candidates = [
            target.split("/")[-1],
            target.replace("wiki/concepts/", "").replace("wiki/entities/", "").replace("wiki/sources/", "").replace("wiki/questions/", "").replace("wiki/meta/", ""),
        ]
        for c in candidates:
            if c in all_pages:
                return "path_error", f"应为 [[{c}]]（去掉路径前缀）", "路径错误"

    # 6. .md 后缀
    if target.endswith(".md"):
        clean = target[:-3]
        if clean in all_pages:
            return "md_suffix", f"应为 [[{clean}]]（去掉 .md）", "路径错误"
        if "/" in clean:
            short = clean.split("/")[-1]
            if short in all_pages:
                return "md_suffix", f"应为 [[{short}]]（去掉路径和 .md）", "路径错误"

    # 7. 引号变种
    quote_pairs = [
        ('"', '"'),
        ("'", "'"),
        ("「", "」"),
        ("『", "』"),
    ]
    for left, right in quote_pairs:
        if target.startswith(left) and target.endswith(right) and len(target) > len(left):
            clean = target[len(left):-len(right)]
            if clean in all_pages:
                return "quote_error", f"应为 [[{clean}]]（去掉引号）", "格式错误"

    # 8. 大小写
    lower_target = target.lower()
    for p in all_pages:
        if p.lower() == lower_target and p != target:
            return "case_error", f"应为 [[{p}]]（大小写）", "格式错误"

    # 9. 中文标点
    for punct in ["，", "。", "；", "："]:
        if punct in target:
            clean = target.replace(punct, "")
            if clean in all_pages:
                return "punct_error", f"应为 [[{clean}]]（去掉中文标点）", "格式错误"

    # 10. question 页面带问号
    if "?" in target and target.endswith("?"):
        clean = target[:-1]
        if clean in all_pages:
            return "typo", f"应为 [[{clean}]]（去掉末尾 ?）", "格式错误"

    # 11. 包含空格
    if " " in target:
        clean = target.replace(" ", "")
        if clean in all_pages:
            return "space_error", f"应为 [[{clean}]]（去掉空格）", "格式错误"

    # 12. 默认：真实缺失
    return "missing", "真实缺失，需新建", "缺失"

# ============ 主流程 ============
print("扫描 wiki 断链（含 aliases 检查）...")
all_pages, aliases_map, page_files = get_all_pages()
print(f"找到 {len(page_files)} 个页面（含 aliases 共 {len(all_pages)} 个名称）")

dead_links = defaultdict(set)  # target -> {sources}
all_link_count = 0

md_files = list(WIKI_ROOT.rglob("*.md"))
print(f"扫描 {len(md_files)} 个 .md 文件...")

for md_file in md_files:
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue

    rel_source = str(md_file.relative_to(VAULT_ROOT))
    links = extract_wikilinks(content)

    for target in links:
        all_link_count += 1

        # 验证目标（已经在 all_pages 中含 aliases）
        if target in all_pages:
            continue

        # 还不在
        dead_links[target].add(rel_source)

print(f"\nwikilink 引用总数: {all_link_count}")
print(f"断链目标数: {len(dead_links)}")
print(f"断链引用处数: {sum(len(v) for v in dead_links.values())}")

# 分类
categorized = defaultdict(list)
details = {}
for target, sources in dead_links.items():
    cat, reason, group = classify_dead_link(target, sources, all_pages)
    categorized[group].append(target)
    details[target] = (cat, reason, group, len(sources))

# ============ 写入报告 ============
report_path = WIKI_ROOT / "meta" / "lint-report-2026-07-14.md"

with open(report_path, "w", encoding="utf-8") as f:
    f.write("---\n")
    f.write("type: meta\n")
    f.write("title: \"Lint Report 2026-07-14\"\n")
    f.write("created: 2026-07-14\n")
    f.write("updated: 2026-07-14\n")
    f.write("tags: [meta, lint, dead-links]\n")
    f.write("status: developing\n")
    f.write("---\n\n")
    f.write("# Lint Report: 2026-07-14 — Wiki 断链专项\n\n")
    f.write("## 摘要\n\n")
    f.write(f"| 指标 | 数值 |\n")
    f.write(f"|------|------|\n")
    f.write(f"| 扫描页面 | {len(page_files)} |\n")
    f.write(f"| 扫描文件 | {len(md_files)} |\n")
    f.write(f"| 别名总数 | {len(aliases_map)} |\n")
    f.write(f"| wikilink 引用总数 | {all_link_count} |\n")
    f.write(f"| **断链目标数** | **{len(dead_links)}** |\n")
    f.write(f"| **断链引用处数** | **{sum(len(v) for v in dead_links.values())}** |\n\n")

    f.write("> **说明**：本报告已包含 Obsidian aliases 匹配——如果 wikilink 目标在某页面的 aliases 中，则视为有效链接。\n\n")

    # 分类概览
    f.write("## 分类概览\n\n")
    f.write("| 分类 | 数量 | 处理建议 |\n")
    f.write("|------|------|---------|\n")
    advice = {
        "误报": "无需处理（canvas、反斜杠、代码块误读）",
        "历史": "无需处理（历史 lint 报告）",
        "路径错误": "建议修正（去掉路径前缀或 .md）",
        "格式错误": "建议修正（引号、大小写、标点、空格）",
        "缺失": "需新建 stub 页面或修正为已存在的概念",
    }
    for group in ["误报", "历史", "路径错误", "格式错误", "缺失"]:
        targets = categorized.get(group, [])
        f.write(f"| {group} | {len(targets)} | {advice[group]} |\n")
    f.write("\n")

    # 详细分类
    f.write("---\n\n")
    f.write("## 📋 详细断链清单\n\n")

    for group, label in [("缺失", "🚨 真实缺失（需新建）"),
                          ("路径错误", "🔧 路径错误（建议修正）"),
                          ("格式错误", "✏️ 格式错误（建议修正）"),
                          ("误报", "ℹ️ 误报（无需处理）"),
                          ("历史", "📚 历史引用（无需处理）")]:
        targets = categorized.get(group, [])
        if not targets:
            continue

        f.write(f"### {label}（{len(targets)} 个）\n\n")
        sorted_targets = sorted(targets, key=lambda x: -details[x][3])
        for t in sorted_targets[:50]:
            n = details[t][3]
            reason = details[t][1]
            f.write(f"- `[[{t}]]` ({n} 处) — {reason}\n")
        if len(targets) > 50:
            f.write(f"- ... 还有 {len(targets) - 50} 个\n")
        f.write("\n")

    # 修复优先级
    f.write("---\n\n")
    f.write("## 🎯 修复优先级（HIGH ≥ 3 处引用）\n\n")

    missing = categorized.get("缺失", [])
    if missing:
        f.write(f"### HIGH 优先级（缺失，引用 ≥ 3 次）：{sum(1 for t in missing if details[t][3] >= 3)} 个\n\n")
        high = sorted([t for t in missing if details[t][3] >= 3], key=lambda x: -details[x][3])
        for t in high:
            f.write(f"- `[[{t}]]` ({details[t][3]} 处)\n")
        f.write("\n")

        med = [t for t in missing if details[t][3] == 2]
        f.write(f"### MEDIUM 优先级（缺失，引用 2 次）：{len(med)} 个\n\n")
        for t in sorted(med, key=lambda x: x):
            f.write(f"- `[[{t}]]`\n")
        f.write("\n")

        low = [t for t in missing if details[t][3] == 1]
        f.write(f"### LOW 优先级（缺失，引用 1 次）：{len(low)} 个\n\n")
        for t in sorted(low)[:50]:
            f.write(f"- `[[{t}]]`\n")
        if len(low) > 50:
            f.write(f"- ... 还有 {len(low) - 50} 个\n")
        f.write("\n")

    # 路径错误修正清单
    path_errors = categorized.get("路径错误", [])
    if path_errors:
        f.write("---\n\n")
        f.write("## 🔧 路径错误批量修正\n\n")
        f.write("这些链接的目标页面**已存在**，只是路径前缀错误。可用批量脚本修正。\n\n")
        f.write("| 错误链接 | 应改为 | 次数 |\n")
        f.write("|---------|--------|------|\n")
        for t in sorted(path_errors, key=lambda x: -details[x][3]):
            n = details[t][3]
            reason = details[t][1]
            # 提取目标名
            if "应为 [[" in reason:
                target = reason.split("应为 [[")[1].split("]]")[0]
            else:
                target = t.split("/")[-1]
            f.write(f"| `[[{t}]]` | `[[{target}]]` | {n} |\n")
        f.write("\n")

    # 格式错误修正清单
    format_errors = categorized.get("格式错误", [])
    if format_errors:
        f.write("---\n\n")
        f.write("## ✏️ 格式错误批量修正\n\n")
        f.write("| 错误链接 | 应改为 | 次数 |\n")
        f.write("|---------|--------|------|\n")
        for t in sorted(format_errors, key=lambda x: -details[x][3]):
            n = details[t][3]
            reason = details[t][1]
            if "应为 [[" in reason:
                target = reason.split("应为 [[")[1].split("]]")[0]
            else:
                target = t
            f.write(f"| `[[{t}]]` | `[[{target}]]` | {n} |\n")
        f.write("\n")

    f.write("---\n\n")
    f.write("## 📌 修复建议\n\n")
    f.write("### 缺失页面处理流程\n\n")
    f.write("1. **检查来源**：阅读引用此链接的所有源页面，理解上下文\n")
    f.write("2. **如是真实概念**：新建 stub 页面\n")
    f.write("   ```yaml\n")
    f.write("   ---\n")
    f.write("   type: concept  # 或 entity\n")
    f.write("   title: \"页面名\"\n")
    f.write("   status: stub\n")
    f.write("   created: 2026-07-14\n")
    f.write("   updated: 2026-07-14\n")
    f.write("   tags: [待完善]\n")
    f.write("   ---\n")
    f.write("   ```\n")
    f.write("3. **如是错误引用**：将 `[[target]]` 改为已存在的 `[[existing]]`\n\n")

    f.write("### 路径/格式错误批量修正\n\n")
    f.write("建议使用 sed 批量替换：\n")
    f.write("```bash\n")
    f.write("# 示例：修正 wiki/concepts/ 路径\n")
    f.write("grep -rl 'wiki/concepts/' wiki/ | xargs sed -i '' 's|\\[\\[wiki/concepts/\\([^]]*\\)\\]\\]|[[\\1]]|g'\n")
    f.write("```\n")

print(f"\n✅ 报告已写入: {report_path}")

# ============ 控制台输出摘要 ============
print("\n" + "=" * 70)
print("📊 断链分类摘要")
print("=" * 70)
for group, label in [("缺失", "🚨 真实缺失"),
                      ("路径错误", "🔧 路径错误"),
                      ("格式错误", "✏️ 格式错误"),
                      ("误报", "ℹ️ 误报"),
                      ("历史", "📚 历史引用")]:
    targets = categorized.get(group, [])
    print(f"\n{label}: {len(targets)} 个")
    for t in sorted(targets, key=lambda x: -details[x][3])[:5]:
        n = details[t][3]
        print(f"  - [[{t}]] ({n} 处)")
    if len(targets) > 5:
        print(f"  ... 还有 {len(targets) - 5} 个")

# 高优先级缺失
print("\n" + "=" * 70)
print("🚨 HIGH 优先级缺失页面（引用 ≥ 3 次）")
print("=" * 70)
missing = categorized.get("缺失", [])
high_priority = sorted([t for t in missing if details[t][3] >= 3], key=lambda x: -details[x][3])
for i, t in enumerate(high_priority):
    n = details[t][3]
    print(f"  {i+1:2d}. [[{t}]] ({n} 处)")
    if i >= 49:
        break
if len(high_priority) > 50:
    print(f"  ... 还有 {len(high_priority) - 50} 个")

print(f"\n总共 HIGH 优先级: {sum(1 for t in missing if details[t][3] >= 3)} 个")
print(f"总共 MEDIUM 优先级: {sum(1 for t in missing if details[t][3] == 2)} 个")
print(f"总共 LOW 优先级: {sum(1 for t in missing if details[t][3] == 1)} 个")

#!/usr/bin/env python3
"""
对断链进行智能分类，区分：
1. 真实缺失页面（应建 stub）
2. 误报（canvas 文件、反斜杠等）
3. 路径错误的链接
4. 真实存在但被遗漏的页面
"""

import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI_ROOT = VAULT_ROOT / "wiki"

# 读取上次扫描的结果报告，重新分析
def get_all_pages():
    pages = set()
    page_files = {}  # stem -> path

    for md_file in WIKI_ROOT.rglob("*.md"):
        rel = md_file.relative_to(VAULT_ROOT)
        stem = md_file.stem

        pages.add(stem)
        pages.add(str(rel.with_suffix("")))
        pages.add(str(rel))
        pages.add(md_file.name)

        page_files[stem] = str(rel)

    return pages, page_files

def classify_dead_link(target, sources):
    """分类单个断链"""
    # 1. canvas 文件（不是 .md）
    if target.endswith(".canvas"):
        return "false_positive", "canvas 文件，不是 markdown 页面"

    # 2. 旧 lint 报告（历史引用）
    if re.match(r"meta/lint-report-\d{4}-\d{2}-\d{2}", target):
        return "historical", "历史 lint 报告，引用属正常"

    # 3. 反斜杠结尾（OCR/编码错误）
    if target.endswith("\\"):
        return "false_positive", "反斜杠结尾，可能是 markdown 转义错误"

    # 4. 反引号（代码块误读）
    if "`" in target:
        return "false_positive", "包含反引号，可能是代码块误读"

    # 5. 检查是否只是路径前缀错误
    # 比如 [[wiki/concepts/土地财政]] 但实际页面在 [[土地财政]]
    candidates_without_prefix = [
        target.split("/")[-1],  # 只取最后一段
        target.replace("wiki/concepts/", "").replace("wiki/entities/", "").replace("wiki/sources/", "").replace("wiki/questions/", "").replace("wiki/meta/", ""),
    ]

    all_pages, _ = get_all_pages()
    for c in candidates_without_prefix:
        if c in all_pages:
            return "path_error", f"实际页面是 [[{c}]]，应修正路径"

    # 6. question 页面带问号
    if "?" in target:
        # 检查去掉问号后是否存在
        clean = target.replace("?", "")
        if clean in all_pages:
            return "typo", f"可能是 [[{clean}]] 的问号错误"

    # 7. 带特殊字符（引号、空格等）
    if '"' in target or "「" in target or "」" in target or "，" in target:
        # 引号变种
        for variant in [target.replace('"', ''), target.replace('"', "'"),
                       target.replace('"', "'"), target.replace('"', '')]:
            if variant in all_pages:
                return "quote_error", f"可能是 [[{variant}]] 的引号变种"

    # 8. 检查大小写差异
    lower_target = target.lower()
    for p in all_pages:
        if p.lower() == lower_target and p != target:
            return "case_error", f"大小写不一致：[[{p}]]"

    # 9. 检查 .md 后缀被包含
    if target.endswith(".md"):
        clean = target[:-3]
        if clean in all_pages:
            return "md_suffix", f"包含 .md 后缀，应为 [[{clean}]]"

    # 10. 默认：真实缺失
    return "missing", "真实缺失，需要新建或修正"

# 读取扫描报告
report_path = WIKI_ROOT / "meta" / "lint-report-2026-07-14.md"
report_text = report_path.read_text(encoding="utf-8")

# 解析断链段
dead_links = defaultdict(list)
current_target = None
in_dead_section = False
in_sources = False

for line in report_text.split("\n"):
    if line.startswith("## 断链清单"):
        in_dead_section = True
        continue
    if in_dead_section and line.startswith("## "):
        in_dead_section = False
    if not in_dead_section:
        continue

    # 匹配 `[[target]]` — N 处
    m = re.match(r"^###\s+`\[\[([^\]]+)\]`\s+—\s+引用\s+(\d+)\s+处", line)
    if m:
        current_target = m.group(1)
        continue

    if current_target and line.startswith("- "):
        # 来源行
        src = line[2:].strip()
        if src:
            dead_links[current_target].append(src)

print(f"共 {len(dead_links)} 个断链目标")

# 分类
categorized = defaultdict(list)
classification_details = {}

for target, sources in dead_links.items():
    category, reason = classify_dead_link(target, sources)
    categorized[category].append(target)
    classification_details[target] = (category, reason, len(sources))

# 输出分类结果
print("\n" + "=" * 70)
print("断链分类结果")
print("=" * 70)

category_names = {
    "false_positive": "误报（无需修复）",
    "historical": "历史引用（无需修复）",
    "path_error": "路径错误（应修正）",
    "typo": "拼写错误",
    "quote_error": "引号变种错误",
    "case_error": "大小写错误",
    "md_suffix": "含 .md 后缀",
    "missing": "真实缺失（需新建）",
}

for cat, targets in sorted(categorized.items(), key=lambda x: -len(x[1])):
    print(f"\n【{category_names.get(cat, cat)}】{len(targets)} 个")
    for t in sorted(targets, key=lambda x: -classification_details[x][2])[:15]:
        n = classification_details[t][2]
        print(f"  [[{t}]] ({n} 处) — {classification_details[t][1]}")
    if len(targets) > 15:
        print(f"  ... 还有 {len(targets) - 15} 个")

# 写入分类报告
with open(report_path, "a", encoding="utf-8") as f:
    f.write("\n\n---\n\n")
    f.write("## 断链分类分析\n\n")

    for cat, targets in sorted(categorized.items(), key=lambda x: -len(x[1])):
        cat_name = category_names.get(cat, cat)
        f.write(f"### 【{cat_name}】{len(targets)} 个\n\n")
        for t in sorted(targets, key=lambda x: -classification_details[x][2]):
            n = classification_details[t][2]
            reason = classification_details[t][1]
            f.write(f"- `[[{t}]]` ({n} 处) — {reason}\n")
        f.write("\n")

    # 重点：需要修复的（missing）
    missing = categorized.get("missing", [])
    if missing:
        f.write("---\n\n")
        f.write("## 🚨 重点：需要新建页面的真实缺失断链\n\n")
        f.write(f"共 {len(missing)} 个，建议按引用次数从高到低依次处理：\n\n")
        for t in sorted(missing, key=lambda x: -classification_details[x][2]):
            n = classification_details[x][2]
            f.write(f"- `[[{t}]]` ({n} 处)\n")

print(f"\n分类报告已追加到: {report_path}")

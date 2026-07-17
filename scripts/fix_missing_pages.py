#!/usr/bin/env python3
"""
批量修复缺失页面
1. 重新扫描找出真实缺失的页面
2. 过滤掉路径错误、占位符、特殊字符
3. 智能判断类型（concept / entity / source）
4. 批量创建 stub 到对应 wiki/xxx 目录
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import date

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI_ROOT = VAULT_ROOT / "wiki"

# ============ 分类规则 ============
ENTITY_KEYWORDS = [
    "马斯克", "特朗普", "鲍威尔", "沃什", "贝佐斯", "杰夫·贝佐斯", "萨克斯", "叶利钦",
    "佩雷拉", "傅育宁", "托普利亚", "梁文峰", "宁高宁", "孟山都", "宁德时代", "胡塞武装",
    "哈马斯", "真主党", "柏林墙", "苹果", "美团", "腾讯", "小米", "三星", "港交所",
    "中国电科", "中国船舶", "中核集团", "中证登", "兵器工业", "潘功胜", "易纲", "证监会",
    "宁德", "长江电力", "前海人寿", "钜盛华", "中国平安", "中粮", "腾讯", "中国证监会",
    "KOSPI", "KOSPI)", "上证", "深证", "港股", "A股", "中证", "创业板", "科创板",
    "白宫", "美联储", "央行", "中国央行", "人民银行", "中国银行", "国开行", "进出口银行",
    "汉口银行", "招商", "建行", "工行", "中行", "农行",
    "法国", "德国", "日本", "韩国", "英国", "意大利", "芬兰", "俄罗斯", "美国",
    "中国", "台湾", "香港", "澳门",
    "新闻", "时报", "周刊", "日报", "环球时报", "凤凰",
    "梧桐树智庫", "梧桐樹智庫", "梧桐树智库", "智库", "智庫",
    "微信", "原文", "媒体", "央行", "证监会",
]

CONCEPT_KEYWORDS = [
    "机制", "理论", "模型", "理论", "框架", "体系", "制度", "规则", "规定", "管理办法",
    "条例", "政策", "战略", "战术", "工具", "手段", "方法", "效应", "影响",
    "价格", "利率", "汇率", "通胀", "通缩", "紧缩", "量化", "扩张", "财政",
    "货币", "资本", "金融", "银行", "信用", "信贷", "债务", "杠杆", "流动性",
    "周期", "波动", "趋势", "结构", "转型", "改革", "创新", "开放",
    "本币", "外币", "外汇", "储备", "逆差", "顺差",
    "投资", "消费", "出口", "进口", "贸易", "关税",
    "管制", "制裁", "出口管制", "对外投资", "对外援助", "外资",
    "危机", "衰退", "萧条", "崩盘", "暴跌", "牛市", "熊市",
    "收购", "并购", "重组", "破产", "清算",
    "补贴", "税收", "汇率", "储备", "外储",
    "产权", "制度变迁", "市场失灵", "利差", "套息", "套利",
    "本币贬值", "本币升值", "出口管制", "对外投资", "美联储独立性",
    "货币政策独立性", "汇率制度", "汇率传导", "股汇负相关",
    "法律", "法案", "条例", "规定", "办法", "规章",
]

SOURCE_KEYWORDS = [
    "报告", "周报", "日报", "月报", "年报", "分析", "研究", "解析", "摘要",
    "MoU", "签订", "签署", "签署", "协议", "公报", "声明", "新闻稿", "报道",
    "原文", "全文", "演讲", "访谈", "采访", "答记者问",
    "原文", "智库", "周刊", "金融时报", "路透", "彭博",
    "MoU", "2026-", "2025-", "2024-", "2023-",
    "wechat", "wx_article",
]

PLACEHOLDER_NAMES = {
    "Concepts", "Entities", "Sources", "wikilinks",
    "wiki-mode", "wiki/X", "wiki/concepts/...", "wiki/concepts/X", "wiki/entities/...",
    "wiki/domains", "wiki/concepts", "wiki/entities", "wiki/sources", "wiki/questions",
    "domains/中国经济", "wikilink", "wiki",
    "wiki/concepts/卡脖子技术", "wiki/concepts/产业升级", "wiki/concepts/估值修复",
    "wiki/concepts/城镇化", "wiki/concepts/天量成交", "wiki/concepts/市场竞争",
    "wiki/concepts/期权策略", "wiki/concepts/港股通", "wiki/concepts/社会保障",
    "wiki/concepts/苹果涨价", "wiki/concepts/财富转移效应", "wiki/concepts/货币政策策略",
    "wiki/concepts/金融安全", "wiki/concepts/2023 SVB危机", "wiki/concepts/TARGET2",
    "wiki/entities/一带一路", "wiki/entities/中国电科", "wiki/entities/中国船舶",
    "wiki/entities/中核集团", "wiki/entities/中证登", "wiki/entities/兵器工业",
    "wiki/entities/小米", "wiki/entities/易纲", "wiki/entities/港交所",
    "wiki/entities/港元", "wiki/entities/潘功胜", "wiki/entities/美团",
    "wiki/entities/腾讯", "wiki/entities/证监会",
    "三元悖论#三个自我实现的均衡",
    "中华人民共和国中央人民政府", "中华人民共和国国务院",
    "中国化债政策包-2024",  # 不是占位符但是文件
    "meta/dashboard",
}

# 已知应该忽略的（不是缺失页面）
IGNORE_LIST = {
    "meta/dashboard",  # Obsidian Bases 文件
    "Concepts", "Entities", "Sources", "wikilinks",
    "wiki-mode", "wiki/X", "wiki/concepts/...", "wiki/entities/...",
    "wiki/domains", "wiki/concepts", "wiki/entities", "wiki/sources",
    "wiki/questions", "wiki",
    "domains/中国经济",
    "wikilink",
    "Claude Canvas",  # 可能是工具名而非页面
}

# ============ 工具函数 ============

def parse_frontmatter(content):
    """解析 frontmatter"""
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
        m = re.match(r'^(\w[\w_-]*)\s*:\s*(.*)', line)
        if m:
            key = m.group(1)
            value = m.group(2).strip()
            if value == "":
                current_key = key
                current_list = []
                result[key] = current_list
                continue
            elif value.startswith('"') and value.endswith('"'):
                result[key] = value[1:-1]
                current_key = None
                current_list = None
            elif value.startswith('[') and value.endswith(']'):
                inner = value[1:-1].strip()
                if inner:
                    result[key] = [s.strip().strip('"').strip("'") for s in inner.split(",")]
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

def get_all_pages():
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
        # 跳过带 #锚点的（只取页面名）
        if "#" in target:
            target = target.split("#")[0].strip()
        if target:
            links.append(target)
    return links

def is_real_missing(target):
    """判断是否真实需要新建的页面（不是占位符/路径错误/特殊字符）"""
    # 1. 是已知忽略列表
    if target in IGNORE_LIST:
        return False, "已知忽略"

    # 2. 是占位符（带 X 或 ... 或 # 锚点的纯模板）
    if "..." in target or target.endswith("/X"):
        return False, "占位符"

    # 3. 路径错误（含 wiki/ 前缀）
    if target.startswith("wiki/"):
        return False, "路径错误"

    # 4. 是分析报告里的示例（看起来像模板）
    if target in PLACEHOLDER_NAMES:
        return False, "占位符"

    # 5. 反斜杠/反引号结尾
    if target.endswith("\\") or "`" in target:
        return False, "格式错误"

    # 6. 以特殊符号开头
    if target.startswith(("《", "《")):
        return False, "书名号引用"

    # 7. 历史 lint 报告
    if re.match(r"meta/lint-report-\d{4}-\d{2}-\d{2}", target):
        return False, "历史 lint 报告"

    # 8. 是 README、CHANGELOG 等系统文件
    if target.upper() in {"README", "CHANGELOG", "CLAUDE", "ATTRIBUTION", "CODEOWNERS"}:
        return False, "系统文件"

    # 9. 是 URL 或路径式
    if "/" in target and not target.startswith("wiki/"):
        return False, "路径式引用"

    return True, "真实缺失"

def classify_page_type(name):
    """智能判断页面类型"""
    # 1. 优先匹配源文件命名模式（日期前缀）
    if re.match(r"^\d{4}-\d{2}-\d{2}", name):
        return "source"

    # 2. 检查 entity 关键词
    for kw in ENTITY_KEYWORDS:
        if kw in name:
            return "entity"

    # 3. 检查 concept 关键词
    for kw in CONCEPT_KEYWORDS:
        if kw in name:
            return "concept"

    # 4. 检查 source 关键词
    for kw in SOURCE_KEYWORDS:
        if kw in name:
            return "source"

    # 5. 默认归类为 concept（最通用）
    return "concept"

def sanitize_filename(name):
    """清理文件名"""
    # 移除无效字符
    invalid_chars = '<>:"/\\|?*'
    for c in invalid_chars:
        name = name.replace(c, '_')
    # 替换空白为下划线（保留中文）
    return name.strip()

def generate_stub_content(name, page_type, sources=None):
    """生成 stub 页面内容"""
    today = date.today().isoformat()

    # 根据类型生成不同的 frontmatter
    if page_type == "concept":
        frontmatter = f"""---
type: concept
title: "{name}"
status: stub
created: {today}
updated: {today}
tags: [concept, stub]
aliases: []
sources: []
related: []
---

"""
    elif page_type == "entity":
        frontmatter = f"""---
type: entity
title: "{name}"
status: stub
created: {today}
updated: {today}
tags: [entity, stub]
aliases: []
sources: []
related: []
---

"""
    elif page_type == "source":
        frontmatter = f"""---
type: source
title: "{name}"
status: stub
created: {today}
updated: {today}
tags: [source, stub]
aliases: []
sources: []
related: []
---

"""

    # 相关条目
    related_section = ""
    if sources:
        related_section = "\n## 相关来源\n\n"
        for src in sources[:10]:
            related_section += f"- {src}\n"

    content = f"""{frontmatter}# {name}

> [!stub] 待完善
> 该页面为 stub，仅作为断链修复占位。引用此页面的来源共 {len(sources) if sources else 0} 处。

## 概述

待补充：{name} 的核心定义、关键特征、应用场景。

## 关键内容

待补充。

## 相关条目

待补充。
{related_section}
"""
    return content

# ============ 主流程 ============
print("=" * 70)
print("批量修复缺失页面")
print("=" * 70)

all_pages, aliases_map, page_files = get_all_pages()
print(f"现有页面: {len(page_files)}")
print(f"现有 aliases: {len(aliases_map)}")

# 扫描所有 wikilink
dead_links = defaultdict(set)
md_files = list(WIKI_ROOT.rglob("*.md"))

for md_file in md_files:
    try:
        content = md_file.read_text(encoding="utf-8")
    except Exception:
        continue
    rel_source = str(md_file.relative_to(VAULT_ROOT))
    for target in extract_wikilinks(content):
        if target not in all_pages:
            dead_links[target].add(rel_source)

print(f"\n所有断链目标: {len(dead_links)}")
print(f"断链引用处数: {sum(len(v) for v in dead_links.values())}")

# 过滤真实缺失
real_missing = []
ignored = []
for target, sources in dead_links.items():
    is_real, reason = is_real_missing(target)
    if is_real:
        real_missing.append((target, sources))
    else:
        ignored.append((target, reason, sources))

print(f"\n真实缺失: {len(real_missing)} 个")
print(f"已忽略（占位符/路径错误/格式错误）: {len(ignored)} 个")

# 按引用次数排序
real_missing.sort(key=lambda x: -len(x[1]))

# 分组输出
print("\n" + "=" * 70)
print("真实缺失页面清单（按引用次数排序）")
print("=" * 70)

# 类型分类
type_counts = {"concept": 0, "entity": 0, "source": 0}
to_create = []

for target, sources in real_missing:
    page_type = classify_page_type(target)
    type_counts[page_type] += 1
    to_create.append({
        "name": target,
        "type": page_type,
        "sources": list(sources),
        "count": len(sources),
    })
    if len(to_create) <= 50:
        print(f"  [{page_type:7s}] [[{target}]] ({len(sources)} 处)")

print(f"\n... 还有 {max(0, len(to_create) - 50)} 个")

print(f"\n类型分布:")
for t, n in type_counts.items():
    print(f"  {t}: {n} 个")

# ============ 创建 stub 页面 ============
print("\n" + "=" * 70)
print("开始创建 stub 页面")
print("=" * 70)

created_files = []
errors = []

for item in to_create:
    name = item["name"]
    page_type = item["type"]
    sources = item["sources"]

    # 文件名清理
    safe_name = sanitize_filename(name)
    target_dir = WIKI_ROOT / f"{page_type}s"  # concepts / entities / sources
    target_path = target_dir / f"{safe_name}.md"

    # 如果已存在则跳过
    if target_path.exists():
        print(f"  ⏭️  跳过: {target_path.name} (已存在)")
        continue

    # 生成内容
    content = generate_stub_content(name, page_type, sources)

    # 写入文件
    try:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(content, encoding="utf-8")
        created_files.append(target_path)
        print(f"  ✅ 创建 [{page_type:7s}] {target_path.relative_to(VAULT_ROOT)}")
    except Exception as e:
        errors.append((target_path, str(e)))
        print(f"  ❌ 失败 [{page_type:7s}] {target_path.relative_to(VAULT_ROOT)}: {e}")

# ============ 输出报告 ============
print("\n" + "=" * 70)
print("修复结果汇总")
print("=" * 70)
print(f"已创建: {len(created_files)} 个 stub 页面")
print(f"失败: {len(errors)} 个")
print(f"跳过（已存在）: {sum(1 for item in to_create if (WIKI_ROOT / f'{classify_page_type(item['name'])}s' / f'{sanitize_filename(item['name'])}.md').exists())}")

# 写入修复日志
log_path = WIKI_ROOT / "meta" / "missing-pages-fixed-2026-07-14.md"
with open(log_path, "w", encoding="utf-8") as f:
    f.write("---\n")
    f.write("type: meta\n")
    f.write("title: \"Missing Pages Fixed 2026-07-14\"\n")
    f.write("created: 2026-07-14\n")
    f.write("updated: 2026-07-14\n")
    f.write("tags: [meta, lint, fix]\n")
    f.write("status: completed\n")
    f.write("---\n\n")
    f.write("# Missing Pages Fixed: 2026-07-14\n\n")
    f.write(f"## 摘要\n\n")
    f.write(f"- 真实缺失目标: {len(to_create)}\n")
    f.write(f"- 已创建 stub: {len(created_files)}\n")
    f.write(f"- 失败: {len(errors)}\n\n")
    f.write(f"## 类型分布\n\n")
    for t, n in type_counts.items():
        f.write(f"- {t}: {n}\n")
    f.write(f"\n## 已创建页面清单\n\n")
    for item in to_create:
        name = item["name"]
        page_type = item["type"]
        count = item["count"]
        f.write(f"- [{page_type}] [[{name}]] ({count} 处)\n")
    if errors:
        f.write(f"\n## 失败清单\n\n")
        for path, err in errors:
            f.write(f"- {path}: {err}\n")

print(f"\n修复日志已写入: {log_path}")
print("\n✅ 批量修复完成！")

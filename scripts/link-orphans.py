#!/usr/bin/env python3
"""Link orphan concept pages to their domain hub page.
Adds 'related' field if missing, pointing to relevant domain."""
import os
import re
from pathlib import Path

VAULT_ROOT = Path("wiki")

# Mapping of concept -> domain
DOMAIN_MAP = {
    # 货币政策与中央银行
    "OMT": "货币政策与中央银行",
    "负利率": "货币政策与中央银行",
    "美联储独立性": "货币政策与中央银行",
    "央行对冲工具": "货币政策与中央银行",
    "做空CDS": "银行体系与金融监管",
    "金融脱媒": "银行体系与金融监管",
    "PCE": "宏观经济",
    "霸权稳定论": "国际金融与汇率",
    "回购注销": "国际金融与汇率",
    "美联储点阵图": "货币政策与中央银行",
    "点阵图": "货币政策与中央银行",
    "二级制裁": "国际金融与汇率",
    "KOSPI": "国际金融与汇率",
    "财政部": "中国金融与改革",
    "外汇管理": "国际金融与汇率",
    "高质量发展": "中国金融与改革",
    "mcp-setup": "风险管理",
}

def add_related(filepath: Path, domain: str) -> bool:
    """Add related field to frontmatter if missing."""
    content = filepath.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False

    end = content.find('\n---', 3)
    if end == -1:
        return False

    fm = content[3:end]
    body = content[end+4:]

    # Check if related already exists
    if re.search(r'^related\s*:', fm, re.MULTILINE):
        return False

    # Find insertion point - after status or before sources/aliases
    insert_after = None
    for key in ['status', 'tags', 'aliases', 'address']:
        m = re.search(f'^{key}\\s*:.*$', fm, re.MULTILINE)
        if m:
            insert_after = m.end()
            break

    if insert_after is None:
        return False

    related_line = f'\nrelated: "[[{domain}]]"'
    new_fm = fm[:insert_after] + related_line + fm[insert_after:]
    new_content = '---\n' + new_fm + '\n---' + body
    filepath.write_text(new_content, encoding='utf-8')
    return True

def main():
    modified = 0
    for name, domain in DOMAIN_MAP.items():
        filepath = VAULT_ROOT / "concepts" / f"{name}.md"
        if not filepath.exists():
            print(f"NOT FOUND: {filepath}")
            continue
        if add_related(filepath, domain):
            modified += 1
            print(f"+ Linked {name} -> {domain}")
    print(f"\nModified: {modified}")

if __name__ == '__main__':
    main()

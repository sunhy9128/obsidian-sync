#!/usr/bin/env python3
"""
更可靠的别名添加脚本
"""

import re
from pathlib import Path
from datetime import date

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI_ROOT = VAULT_ROOT / "wiki"

# (文件路径, 要添加的别名)
ALIASES_TO_ADD = [
    ("wiki/questions/How does the LLM Wiki pattern work.md", "How does the LLM Wiki pattern work?"),
    # 共建_一带一路_.md 已经有 aliases 中包含 一带一路, 共建一带一路，不需要再加
    # 股牛汇弱.md 的别名有引号嵌套问题，需要修复
]

added = 0
already_exists = 0

print("=" * 70)
print("添加剩余别名")
print("=" * 70)

for rel_path, new_alias in ALIASES_TO_ADD:
    file_path = VAULT_ROOT / rel_path

    if not file_path.exists():
        print(f"  ❌ 文件不存在: {rel_path}")
        continue

    content = file_path.read_text(encoding="utf-8")

    # 检查是否已有此别名（用 regex 检查 raw 文本）
    if f'"{new_alias}"' in content or f"'{new_alias}'" in content:
        print(f"  ⏭️  别名已存在: [[{new_alias}]] in {rel_path}")
        already_exists += 1
        continue

    # 找到 aliases: 行，处理
    # YAML 中嵌套引号需要使用单引号包裹
    safe_alias = new_alias.replace('"', "'")
    new_line = f'  - "{safe_alias}"'

    lines = content.split("\n")
    new_lines = []
    in_aliases = False
    added_to_this = False

    for i, line in enumerate(lines):
        if not in_aliases:
            if line.strip() == "aliases:" or line.strip().startswith("aliases:"):
                in_aliases = True
                new_lines.append(line)
                # 检查下一行
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    if next_line.strip() == "[]":
                        # aliases: [] —— 把 [] 替换为别名
                        new_lines[-1] = "aliases:"
                        new_lines.append(new_line)
                        added_to_this = True
                        in_aliases = False
                        continue
                    elif next_line.strip().startswith("- "):
                        # 已存在别名——在末尾添加
                        new_lines.append(next_line)
                        # 找到 aliases 列表结束
                        for j in range(i + 2, len(lines)):
                            next_line2 = lines[j]
                            if next_line2.strip().startswith("- "):
                                new_lines.append(next_line2)
                            else:
                                # 不再是列表项——在上一行后插入
                                new_lines.append(new_line)
                                added_to_this = True
                                in_aliases = False
                                new_lines.append(next_line2)
                                break
                        else:
                            # 到文件末尾
                            new_lines.append(new_line)
                            added_to_this = True
                            in_aliases = False
                        continue
                    else:
                        # 下一个非空行不是列表项——在 aliases 后插入
                        new_lines.append(new_line)
                        added_to_this = True
                        in_aliases = False
                        continue
                else:
                    # 文件结束
                    new_lines.append(new_line)
                    added_to_this = True
                    in_aliases = False
                    continue
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if added_to_this:
        new_content = "\n".join(new_lines)
        new_content = re.sub(
            r"updated:\s*\d{4}-\d{2}-\d{2}",
            f"updated: {date.today().isoformat()}",
            new_content
        )
        file_path.write_text(new_content, encoding="utf-8")
        added += 1
        print(f"  ✅ 添加: [[{new_alias}]] → {rel_path}")
    else:
        print(f"  ⚠️  无法添加: [[{new_alias}]] in {rel_path}")

print(f"\n汇总: 添加 {added} 个，已存在 {already_exists} 个")

# ============ 修复股牛汇弱.md 的嵌套引号问题 ============
print("\n" + "=" * 70)
print("修复股牛汇弱.md 嵌套引号问题")
print("=" * 70)

file_path = VAULT_ROOT / "wiki/concepts/股牛汇弱.md"
content = file_path.read_text(encoding="utf-8")

# 把双引号嵌套的双引号别名修正为单引号
# 错误: - "为何日韩会"股牛汇弱""
# 正确: - '为何日韩会"股牛汇弱"'

broken_aliases = [
    ('- "为何日韩会"股牛汇弱""', '- \'为何日韩会"股牛汇弱"\''),
    ('- "为何日韩会"股牛汇弱"？.md"', '- \'为何日韩会"股牛汇弱"？.md\''),
]

for old, new in broken_aliases:
    if old in content:
        content = content.replace(old, new)
        print(f"  ✅ 修复: {old[:50]}...")
        added += 1

# 更新 updated 字段
content = re.sub(
    r"updated:\s*\d{4}-\d{2}-\d{2}",
    f"updated: {date.today().isoformat()}",
    content
)

file_path.write_text(content, encoding="utf-8")
print(f"  ✅ 更新股牛汇弱.md")

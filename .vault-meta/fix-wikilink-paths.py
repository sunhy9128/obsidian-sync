#!/usr/bin/env python3
"""批量修复 wikilink 路径格式: [[wiki/concepts/xxx]] -> [[xxx]]"""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path("/Users/mac/Documents/金融知识库")
WIKI = ROOT / "wiki"

# 匹配 [[wiki/xxx/yyy]] 格式
WIKILINK_RE = re.compile(r'\[\[wiki/(?:concepts|entities|sources|questions|references|analysis|process)/([^\]|#]+)(?:\|[^\]]+)?\]\]')

def fix_file(path):
    """修复单个文件的 wikilink 格式，返回修复数量"""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return 0, 0
    
    # 查找所有需要修复的 wikilink
    matches = WIKILINK_RE.findall(text)
    if not matches:
        return 0, 0
    
    # 统计修复数量
    fixed_count = len(matches)
    
    # 替换格式: [[wiki/xxx/yyy]] -> [[yyy]]
    new_text = WIKILINK_RE.sub(lambda m: f'[[{m.group(1)}]]', text)
    
    # 写入文件
    path.write_text(new_text, encoding="utf-8")
    
    return fixed_count, 1

def main():
    stats = defaultdict(int)
    files_fixed = 0
    total_fixed = 0
    
    for md_file in WIKI.rglob("*.md"):
        # 跳过隐藏文件和 meta 目录中的 lint 报告
        if any(part.startswith(".") for part in md_file.parts):
            continue
        
        fixed, was_fixed = fix_file(md_file)
        if was_fixed:
            files_fixed += 1
            total_fixed += fixed
            rel = md_file.relative_to(ROOT)
            stats[rel.parent.name] += fixed
    
    print(f"✅ 修复完成!")
    print(f"   修改文件: {files_fixed} 个")
    print(f"   修复 wikilink: {total_fixed} 处")
    print()
    print("按目录统计:")
    for dir_name, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"   {dir_name}: {count}")

if __name__ == "__main__":
    main()

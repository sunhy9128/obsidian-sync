#!/usr/bin/env python3
"""Batch-add title field to pages missing it.
Uses filename (without .md) as the title.
"""
import os
import re
from pathlib import Path

VAULT_ROOT = Path("wiki")
TITLE_KEY = re.compile(r'^title\s*:', re.MULTILINE)

def extract_title_from_filename(filepath: Path) -> str:
    """Get title from filename stem."""
    return filepath.stem

def has_title_field(content: str) -> bool:
    """Check if frontmatter already has title:."""
    if not content.startswith('---'):
        return False
    end = content.find('\n---', 3)
    if end == -1:
        return False
    fm = content[3:end]
    return bool(TITLE_KEY.search(fm))

def add_title(filepath: Path, title: str) -> bool:
    """Add title to frontmatter if missing. Returns True if modified."""
    content = filepath.read_text(encoding='utf-8')
    if has_title_field(content):
        return False

    if not content.startswith('---'):
        return False

    end = content.find('\n---', 3)
    if end == -1:
        return False

    fm = content[3:end]
    body = content[end+4:]

    # Check existing type field for ordering hint
    type_match = re.search(r'^type\s*:\s*(.+)$', fm, re.MULTILINE)
    if type_match:
        insert_pos = type_match.end()
        new_fm = fm[:insert_pos] + f'\ntitle: "{title}"' + fm[insert_pos:]
    else:
        new_fm = f'\ntitle: "{title}"' + fm

    new_content = '---\n' + new_fm + '\n---' + body
    filepath.write_text(new_content, encoding='utf-8')
    return True

def main():
    modified = 0
    skipped = 0
    for md_file in VAULT_ROOT.rglob("*.md"):
        # Skip meta files like dashboard, log, index, hot (they have their own structure)
        rel = md_file.relative_to(VAULT_ROOT)
        parts = rel.parts
        # Skip files that don't use frontmatter (log, index, hot, etc.)
        if md_file.name in ('log.md', 'index.md', 'hot.md', 'overview.md'):
            continue
        # Skip _index.md files
        if md_file.name == '_index.md':
            continue
        title = extract_title_from_filename(md_file)
        if add_title(md_file, title):
            modified += 1
            print(f"+ {rel}")
        else:
            skipped += 1

    print(f"\nModified: {modified}, Skipped: {skipped}")

if __name__ == '__main__':
    main()

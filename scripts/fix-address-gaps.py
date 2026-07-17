#!/usr/bin/env python3
"""
fix-address-gaps.py — 为所有 post-rollout 缺失 address: 的页面批量补地址。

Rollout baseline: 2026-04-23（.vault-meta/legacy-pages.txt）
Counter file: .vault-meta/address-counter.txt
下一地址: c-000016 (counter=16)
"""

import json
import re
import sys
from pathlib import Path

VAULT_ROOT = Path("/Users/mac/Documents/金融知识库")
COUNTER_FILE = VAULT_ROOT / ".vault-meta" / "address-counter.txt"
DETAILS_FILE = VAULT_ROOT / ".vault-meta" / "lint-details.json"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def read_counter():
    return int(COUNTER_FILE.read_text().strip())

def write_counter(n):
    COUNTER_FILE.write_text(f"{n}\n")

def next_address(counter):
    return f"c-{counter:06d}"

def add_address_to_file(file_path, address):
    """Add address: to frontmatter. If frontmatter exists, inject; else prepend."""
    text = file_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if m:
        fm_block = m.group(1)
        # Check if address already present (shouldn't happen for these files)
        if re.search(r"^address:", fm_block, re.MULTILINE):
            return False, "address already exists"
        # Inject address: after title: line (or at top)
        new_fm_lines = []
        lines = fm_block.splitlines()
        inserted = False
        for line in lines:
            new_fm_lines.append(line)
            if not inserted and line.startswith("title:"):
                new_fm_lines.append(f"address: {address}")
                inserted = True
        if not inserted:
            new_fm_lines.insert(0, f"address: {address}")
        new_fm = "\n".join(new_fm_lines) + "\n"
        new_text = "---\n" + new_fm + "---\n" + text[m.end():]
    else:
        # No frontmatter — create one at the top
        new_text = f"""---
address: {address}
---

{text}"""
    file_path.write_text(new_text, encoding="utf-8")
    return True, "added"

def main():
    # Load lint details
    details = json.loads(DETAILS_FILE.read_text())
    addr_errors = details.get("addr_errors", [])

    # Filter only "missing address (post-rollout)"
    missing_pages = [
        (rel_path, err_msg)
        for rel_path, err_msg in addr_errors
        if "missing address" in err_msg
    ]
    print(f"Pages needing address: {len(missing_pages)}")

    counter = read_counter()
    print(f"Current counter: {counter}  → next address: {next_address(counter)}")

    fixed = 0
    skipped = 0
    errors = []

    for rel_path, _ in missing_pages:
        file_path = VAULT_ROOT / rel_path
        if not file_path.exists():
            errors.append(f"  SKIP (not found): {rel_path}")
            skipped += 1
            continue

        addr = next_address(counter)
        ok, msg = add_address_to_file(file_path, addr)
        if ok:
            fixed += 1
            counter += 1
            if fixed % 100 == 0:
                print(f"  ... {fixed}/{len(missing_pages)} done")
        else:
            errors.append(f"  {msg}: {rel_path}")

    write_counter(counter)

    print(f"\nDone: {fixed} fixed, {skipped} skipped, {len(errors)} errors")
    for e in errors[:20]:
        print(e)

    # Update counter file display
    print(f"\nNew counter: {counter}")
    print(f"Next address would be: {next_address(counter)}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the lint report from lint-stats.json."""
import json, re
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path("/Users/mac/Documents/金融知识库")
stats = json.loads((ROOT / ".vault-meta" / "lint-stats.json").read_text(encoding="utf-8"))
records = stats["records"]
all_links = stats["all_links"]
inbound = stats["inbound"]
name_to_paths = stats["name_to_paths"]
files = stats["files"]

# 1. Orphans: pages with NO inbound links (excluding meta/index/folds)
EXCLUDE = {"meta", "folds"}
ORPHAN_EXCLUDE_FILES = {"_index.md", "index.md", "log.md", "hot.md",
                        "overview.md", "dashboard.md", "dashboard.base",
                        "Wiki Map.md", "getting-started.md"}

def is_excluded(rec):
    if rec["in_folds"]:
        return True
    if Path(rec["path"]).name in ORPHAN_EXCLUDE_FILES:
        return True
    if rec["path"].startswith("wiki/meta/"):
        return True
    return False

orphans = []
for rec in records:
    if is_excluded(rec):
        continue
    if not inbound.get(rec["stem"], []):
        # Exclude domain pages that are linked by _index pages
        # Actually orphan means no wikilinks anywhere
        orphans.append(rec["path"])

# 2. Dead links: wikilinks that don't resolve
dead_links = defaultdict(list)  # target -> [(source, count)]
for src, tgt in all_links:
    if tgt not in name_to_paths:
        dead_links[tgt].append(src)

dead_link_count = sum(len(v) for v in dead_links.values())

# 3. Frontmatter gaps
fm_gaps = []
for rec in records:
    if is_excluded(rec):
        continue
    missing = []
    if not rec["type"]:
        missing.append("type")
    if not rec["status"]:
        missing.append("status")
    if not rec["created"]:
        missing.append("created")
    if not rec["updated"]:
        missing.append("updated")
    tags = rec["tags"]
    if not tags or (isinstance(tags, list) and len(tags) == 0):
        missing.append("tags")
    if missing:
        fm_gaps.append((rec["path"], missing))

# 4. Address validation (DragonScale)
addr_re = re.compile(r"^(c|l)-([0-9]{6})$")
addresses = defaultdict(list)
addr_errors = []
post_rollout = "2026-04-23"
legacy_paths = set()
lm_path = ROOT / ".vault-meta" / "legacy-pages.txt"
for line in lm_path.read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#"):
        legacy_paths.add(line)

RFM_BASELINE = "2026-04-23"
for rec in records:
    path = rec["path"]
    addr = rec["address"]
    if not addr:
        # Skip if excluded
        if rec["in_folds"] or Path(path).name in ORPHAN_EXCLUDE_FILES or path.startswith("wiki/meta/"):
            continue
        # Determine if post-rollout page
        is_legacy_listed = path in legacy_paths
        created = rec["created"][:10] if rec["created"] else ""
        if created >= RFM_BASELINE and not is_legacy_listed and rec["type"] and rec["type"] != "meta":
            addr_errors.append((path, "missing address (post-rollout)"))
        continue
    # Validate format
    if not addr_re.match(addr):
        addr_errors.append((path, f"invalid format: {addr}"))
        continue
    addresses[addr].append(path)

# Uniqueness
for addr, paths in addresses.items():
    if len(paths) > 1:
        addr_errors.append((", ".join(paths), f"duplicate address: {addr}"))

# Counter consistency
peek = int((ROOT / ".vault-meta" / "address-counter.txt").read_text().strip())
for addr in addresses:
    m = addr_re.match(addr)
    if m and m.group(1) == "c":
        n = int(m.group(2))
        if n >= peek:
            addr_errors.append((addr, f"counter drift: n={n} >= peek={peek}"))

# Summary
report_lines = []
today = "2026-07-16"
total = len(records)
n_orphans = len(orphans)
n_dead_links_targets = len(dead_links)
n_fm_gaps = len(fm_gaps)
n_addr_errors = len(addr_errors)
issues = n_orphans + n_dead_links_targets + n_fm_gaps + n_addr_errors

print(f"Total: {total}")
print(f"Orphans: {n_orphans}")
print(f"Dead-link targets: {n_dead_links_targets} ({dead_link_count} occurrences)")
print(f"FM gaps: {n_fm_gaps}")
print(f"Addr errors: {n_addr_errors}")
print(f"Issues: {issues}")
print(f"\nTop dead-link targets:")
for tgt, srcs in sorted(dead_links.items(), key=lambda x: -len(x[1]))[:15]:
    print(f"  [[{tgt}]] -> {len(srcs)} refs")
print(f"\nTop orphans (first 20):")
for o in orphans[:20]:
    print(f"  {o}")
print(f"\nFM gaps (first 20):")
for p, m in fm_gaps[:20]:
    print(f"  {p}: {m}")
print(f"\nAddress errors:")
for p, e in addr_errors:
    print(f"  {p}: {e}")

# Save details for report builder
details = {
    "today": today,
    "total": total,
    "orphans": orphans[:200],
    "dead_links": {k: sorted(set(v))[:10] for k, v in dead_links.items()},
    "dead_link_count": dead_link_count,
    "fm_gaps": fm_gaps[:200],
    "addr_errors": addr_errors,
    "page_types": stats["page_types"],
    "page_statuses": stats["page_statuses"],
    "issues_total": issues,
}
(ROOT / ".vault-meta" / "lint-details.json").write_text(
    json.dumps(details, ensure_ascii=False, indent=2), encoding="utf-8")

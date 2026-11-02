#!/usr/bin/env python3
"""Basic no-dependency validation for a multi-skill repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
errors = []
folders = sorted(p for p in SKILLS.iterdir() if p.is_dir()) if SKILLS.is_dir() else []
if not folders:
    errors.append("No skill directories under skills/")

for folder in folders:
    skill = folder / "SKILL.md"
    if not NAME.fullmatch(folder.name):
        errors.append(f"{folder}: directory name must be kebab-case")
    if not skill.is_file():
        errors.append(f"{folder}: missing SKILL.md")
        continue
    content = skill.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append(f"{skill}: missing frontmatter delimiter")
        continue
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        errors.append(f"{skill}: frontmatter not closed")
        continue
    metadata = parts[1]
    name = re.search(r"^name:\s*['\"]?([^\n'\"]+)['\"]?\s*$", metadata, re.M)
    description = re.search(r"^description:\s*(.+)$", metadata, re.M)
    if not name or name.group(1).strip() != folder.name:
        errors.append(f"{skill}: frontmatter name must match directory")
    if not description or not description.group(1).strip():
        errors.append(f"{skill}: missing description")

if errors:
    print("Validation failed:\n" + "\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Validated {len(folders)} skill(s): " + ", ".join(p.name for p in folders))

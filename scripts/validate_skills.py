#!/usr/bin/env python3
"""Offline structural and reference validation for all distributable skills."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PATH_REF = re.compile(r"(?<![a-zA-Z0-9_/])(?:references|templates|evals|assets|scripts)/[a-zA-Z0-9_./-]+")
errors = []
folders = sorted(p for p in SKILLS.iterdir() if p.is_dir()) if SKILLS.is_dir() else []
if not folders:
    errors.append("No skill directories under skills/")
for folder in folders:
    if not NAME.fullmatch(folder.name): errors.append(f"{folder}: directory must be kebab-case")
    skill = folder / "SKILL.md"
    if not skill.is_file():
        errors.append(f"{folder}: missing SKILL.md")
        continue
    content = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not match:
        errors.append(f"{skill}: invalid frontmatter delimiters")
        continue
    meta = match.group(1)
    name = re.search(r"^name:\s*['\"]?([^\n'\"]+)['\"]?\s*$", meta, re.M)
    desc = re.search(r"^description:\s*(.*?)\s*$", meta, re.M)
    if not name or name.group(1).strip() != folder.name: errors.append(f"{skill}: name must match directory")
    if not desc or not desc.group(1).strip(): errors.append(f"{skill}: description required")
    # A minimal metadata subset is supported without PyYAML; use a YAML parser if extending the schema.
    for pathref in set(PATH_REF.findall(content)):
        if '..' in Path(pathref).parts or not (folder / pathref).is_file():
            errors.append(f"{skill}: missing or unsafe file reference {pathref}")
    cases = folder / "evals/cases.json"
    if cases.is_file():
        try:
            data = json.loads(cases.read_text(encoding="utf-8"))
            if not isinstance(data.get('cases'), list) or not data['cases']:
                errors.append(f"{cases}: cases must be a non-empty list")
            ids = set()
            for case in data.get('cases', []):
                if case.get('id') in ids: errors.append(f"{cases}: duplicate case id")
                ids.add(case.get('id'))
                fixture = case.get('fixture', '')
                if not fixture or '..' in Path(fixture).parts or not (folder/'evals'/fixture).is_file():
                    errors.append(f"{cases}: missing fixture {fixture}")
        except (ValueError, TypeError) as exc:
            errors.append(f"{cases}: invalid JSON: {exc}")
if errors:
    print("Validation failed:\n" + "\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Validated {len(folders)} skill(s): " + ", ".join(p.name for p in folders))

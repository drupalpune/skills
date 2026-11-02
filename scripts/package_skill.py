#!/usr/bin/env python3
"""Build a portable per-skill ZIP (skill directory as archive root)."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import sys

ROOT = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2 or not sys.argv[1] or '/' in sys.argv[1] or '\\' in sys.argv[1]:
    raise SystemExit("Usage: python3 scripts/package_skill.py <skill-name>")
name = sys.argv[1]
folder = ROOT / 'skills' / name
if not folder.is_dir() or not (folder / 'SKILL.md').is_file():
    raise SystemExit(f"Skill not found: {name}")
output = ROOT / 'dist' / f'{name}.zip'
output.parent.mkdir(exist_ok=True)
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    for path in sorted(folder.rglob('*')):
        if path.is_file() and not path.is_symlink() and '__pycache__' not in path.parts:
            archive.write(path, path.relative_to(folder.parent))
print(output)

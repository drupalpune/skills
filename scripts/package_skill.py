#!/usr/bin/env python3
"""Validate and package one skill as a safe portable ZIP."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2 or not sys.argv[1] or '/' in sys.argv[1] or '\\' in sys.argv[1]:
    raise SystemExit('Usage: python3 scripts/package_skill.py <skill-name>')
subprocess.run([sys.executable, str(ROOT/'scripts/validate_skills.py')], check=True)
name = sys.argv[1]
folder = ROOT/'skills'/name
if not folder.is_dir() or not (folder/'SKILL.md').is_file(): raise SystemExit(f'Skill not found: {name}')
output = ROOT/'dist'/f'{name}.zip'
output.parent.mkdir(exist_ok=True)
with ZipFile(output,'w',ZIP_DEFLATED) as z:
    for path in sorted(folder.rglob('*')):
        if path.is_symlink(): raise SystemExit(f'Symlink not permitted in skill package: {path}')
        if path.is_file() and not any(p in path.parts for p in ['__pycache__','.DS_Store','.git']):
            z.write(path,path.relative_to(folder.parent))
with ZipFile(output) as z:
    if z.testzip() is not None: raise SystemExit('ZIP integrity check failed')
    names=z.namelist()
    if f'{name}/SKILL.md' not in names: raise SystemExit('SKILL.md missing from ZIP')
print(output)

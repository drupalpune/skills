#!/usr/bin/env python3
"""Offline regression checks of evaluation fixture specifications and packaging."""
import json
import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'scripts/validate_skills.py')],check=True)
for skill in sorted((ROOT/'skills').iterdir()):
    if not skill.is_dir(): continue
    cases=skill/'evals/cases.json'
    if cases.exists():
        data=json.loads(cases.read_text())
        for case in data['cases']:
            assert (skill/'evals'/case['fixture']).is_file(), case['id']
            assert any(x in case for x in ('must_not','must_check','must_use')), case['id']
    subprocess.run([sys.executable,str(ROOT/'scripts/package_skill.py'),skill.name],check=True)
    with ZipFile(ROOT/'dist'/f'{skill.name}.zip') as archive:
        paths=set(archive.namelist())
        assert f'{skill.name}/SKILL.md' in paths
        assert all(not p.startswith('/') and '..' not in Path(p).parts for p in paths)
        if cases.exists(): assert f'{skill.name}/evals/cases.json' in paths
print('Offline fixture and packaging checks passed. NOTE: model behaviour has not been evaluated.')

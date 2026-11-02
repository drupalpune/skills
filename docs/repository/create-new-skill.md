# How to add another skill to this repository

Use a sibling directory, never nest one skill inside another.

```text
skills/
  event-audience-coverage/
    SKILL.md
  your-new-skill/
    SKILL.md
    references/
    templates/
```

## Steps

1. Create `skills/your-new-skill/SKILL.md` with YAML frontmatter (`name` and `description`).
2. Define when to use the skill, its required and optional inputs, workflow, output, limitations, and safety defaults.
3. Store reusable detail in that skill's `references/`; output skeletons in its `templates/`.
4. Create `docs/your-new-skill/README.md` and add skill-specific how-to guides there; reserve `docs/repository/` for shared guidance.
5. Add the new skill to the root `README.md` catalog.
6. Validate and package:

   ```bash
   python3 scripts/validate_skills.py
   python3 scripts/package_skill.py your-new-skill
   ```

7. Inspect `dist/your-new-skill.zip` before sharing; keep generated archives out of Git.
8. Add a sample invocation and open a pull request.

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for review criteria. Packaging alone does not guarantee compatibility with every client; test against the intended uploader.

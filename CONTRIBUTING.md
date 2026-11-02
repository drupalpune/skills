# Contributing

## Adding a new skill

1. Create `skills/<kebab-case-name>/SKILL.md`.
2. Start `SKILL.md` with YAML frontmatter containing `name: <kebab-case-name>` and a concise `description:` explaining what triggers the skill.
3. Keep all skill-specific references, templates, scripts, and assets inside the skill directory. Use relative paths from `SKILL.md`.
4. Explain expected inputs, steps, outputs, limits, and safe operating defaults. Do not claim the agent can fetch inaccessible content.
5. Add skill-specific how-to guides under `docs/<skill-name>/` and link them from `docs/README.md`. Keep shared repository guidance under `docs/repository/`.
6. Add an entry to the skills catalog in the root `README.md`.
7. Run `python3 scripts/validate_skills.py` and `python3 scripts/package_skill.py <skill-name>`.
8. Open a pull request with a short purpose statement and an example invocation.

## Review criteria

- Clear trigger and reusable scope
- Evidence-based outputs and transparent limitations
- No secrets, tokens, personal data, or proprietary source material
- Read-only behavior unless an explicit request authorizes modifications
- Relative file references that resolve within the skill folder
- No unnecessary duplicate content across skills

## Versioning

Use Git history and releases to track versions. Keep changes to one skill self-contained where practical. For distributable releases, generate individual skill archives; do not commit generated ZIPs in `dist/`.

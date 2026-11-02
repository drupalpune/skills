# Drupal Pune Skills

Reusable AI agent skills maintained for Drupal, open-source communities, conference organisers, and related workflows.

## Skills catalog

| Skill | Purpose | Status |
| --- | --- | --- |
| [Event Audience Coverage](skills/event-audience-coverage/) | Evidence-backed persona coverage audits for event websites, sitemaps, and content drafts | Initial release |

## Repository structure

Each skill is self-contained under `skills/<skill-name>/` and must provide `SKILL.md` with YAML frontmatter containing `name` and `description`. Supporting materials belong inside that skill's `references/`, `templates/`, `scripts/`, or `assets/` directories as needed.

```text
skills/
  event-audience-coverage/
    SKILL.md
    references/
    templates/
  another-skill/
    SKILL.md
```

## Documentation

- [Documentation index](docs/README.md)
- [Repository setup and installation](docs/repository/getting-started.md)
- [Contributing a new skill](docs/repository/create-new-skill.md)
- [Event Audience Coverage — how-to guides](docs/event-audience-coverage/README.md)

Each skill's guides live in `docs/<skill-name>/` alongside the corresponding `skills/<skill-name>/` directory.

## Installation

To create an uploadable ZIP for a specific skill:

```bash
python3 scripts/package_skill.py event-audience-coverage
```

The archive is written to `dist/event-audience-coverage.zip`, with `event-audience-coverage/` as its top-level directory. Upload this ZIP using the Skill uploader in a supported client, or copy the skill folder into the skill directory supported by your agent.

Do **not** upload the entire repository ZIP as one skill; package the particular skill instead.

## Validation

```bash
python3 scripts/validate_skills.py
```

Validation runs for pull requests and pushes to the default branch via GitHub Actions.

## Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions should be reusable, scoped, and read-only by default when interacting with third-party content.

## License

See [LICENSE](LICENSE).

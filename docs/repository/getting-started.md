# Getting started

This repository contains **multiple independent skills**. Install one skill at a time; do not upload the whole repository as a single skill.

## Prerequisites

- Access to a ChatGPT Skills uploader or an agent that supports `SKILL.md`-based skills.
- Python 3 to run local validation and packaging scripts.
- Web access if you want the agent to inspect public URLs. Availability and breadth of crawling depend on the agent's tools and site access.

## Install `event-audience-coverage` in ChatGPT

1. Clone or download this repository.
2. From the repository root, run:

   ```bash
   python3 scripts/validate_skills.py
   python3 scripts/package_skill.py event-audience-coverage
   ```

3. Locate `dist/event-audience-coverage.zip`.
4. In ChatGPT, open the Skills upload/create interface available to your account and upload **that individual skill ZIP**, not the repository ZIP.
5. Start a chat or Work task in which the skill is available. Test with:

   > Using event-audience-coverage, review this page: https://drupalasia.org/events/india-2027. Show evidence for every persona score and say which content you could not verify.

If the uploader cannot import the archive, check its current package-format requirements. The ZIP produced here has `event-audience-coverage/` as its top-level directory.

## Other agents

Copy `skills/event-audience-coverage/` into the supported skills location for your agent and follow that agent's activation instructions. Paths and availability vary.

## After installation

Read [Single-page audit](../event-audience-coverage/audit-single-page.md) or [Sitemap audit](../event-audience-coverage/audit-sitemap.md) and use the examples in [Prompt recipes](../event-audience-coverage/prompt-recipes.md).

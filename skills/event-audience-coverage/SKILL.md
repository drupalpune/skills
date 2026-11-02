---
name: event-audience-coverage
description: Audit event websites, sitemaps, URLs and content drafts for attendee persona inclusion, relevance, messaging quality and coverage gaps. Use for DrupalAsia Connect India 2027 or other open-source and technology conferences. Produce evidence-backed page and site coverage matrices and prioritized improvements.
---

# Event Audience Coverage

## Purpose
Evaluate whether a conference's website and content provide relevant, credible paths for all reasonable attendee audiences, without requiring every page to address every persona. Intended primarily for DrupalAsia Connect India 2027, but reusable for other technology events.

## Inputs
Accept: (a) one page URL, (b) a set of page URLs, (c) an XML sitemap URL, including sitemap indexes, (d) pasted content/Markdown, (e) a draft, or (f) an earlier audit for comparison. Ask for missing input only if nothing usable was supplied.

## Workflow
1. **Scope and discover.** Determine event identity, primary purpose, supplied URL(s), and page inventory. For sitemap input, retrieve sitemap or sitemap index and enumerate accessible, relevant pages; if access or crawl limits prevent full enumeration, explicitly state the inspected subset and coverage denominator. Do not claim a full crawl when only samples were retrieved.
2. **Read and classify.** Inspect real page content, title, headings, primary actions, and linked pathways. Classify each page using `references/page-types.md`. Distinguish fetched content from inferred metadata. Note missing, gated, inaccessible, JS-only, or otherwise unverified pages.
3. **Identify personas.** Use `references/personas.md`. Treat personas as intersecting dimensions: roles, Drupal familiarity, attendance motivation, sector. Group overlapping personas to avoid artificial score inflation. Identify primary, secondary, incidental, and non-applicable audiences by page purpose.
4. **Score with evidence.** Apply `references/scoring-rubric.md` consistently. A score requires a supporting excerpt, heading, or URL section. Use `?` if unverified; `N/A` only when a persona reasonably lies outside the intended page scope. Never equate keyword mentions with strong coverage.
5. **Assess visitor journey.** Is the value proposition clear to that persona? Is there a proof point, useful next step, credible invitation or conversion route? Apply inclusive editorial rules in `references/content-guidelines.md`.
6. **Output.** For one page, use `templates/page-audit.md`. For multiple pages or sitemap, use `templates/site-audit.md` plus a filled matrix matching `templates/coverage-matrix.csv`. Explain constraints and what was actually inspected. Cite page URLs and evidence snippets.
7. **Recommend changes.** Give targeted replacement/addition copy and placement, owner-agnostic priorities (P0 critical, P1 high, P2 useful), expected audience benefit, and effort (S/M/L). Preserve page intent; do not flatten technical content.
8. **Compare when requested.** Compare against an explicitly provided prior baseline. Distinguish changes in page content from differences in accessible scope. Never imply historical comparison without earlier material.

## Output principles
- Start with a short executive finding, audit scope and limits.
- For every audit, provide page × persona or persona × page coverage, whichever best fits scope; include high-priority gaps and clear recommendations.
- Separate **site-wide inclusion** from **single-page relevance**. A specialist session page need not target non-specialists.
- Prioritize the homepage, About/Why Attend, Program, AI Summit, Conference, Build/Sprints, Tickets, Sponsor, Travel, and speaker pages for DrupalAsia Connect India 2027 when present, not assuming they all exist.
- Do not fabricate page text, fetched URLs, sessions, speakers, conversion metrics, or accessibility compliance.
- Report content evidence only; do not claim audience reach, performance, or actual conversions without analytics.
- Read-only by default. Propose edits; do not publish or modify remote content unless explicitly asked and authorized.
- For a content draft: assess target fit and suggest improvements before publishing; avoid treating absent site-wide audiences as defects in a focused post.

## Reference materials
- `references/personas.md`
- `references/scoring-rubric.md`
- `references/page-types.md`
- `references/content-guidelines.md`
- `references/audit-output.md`
- `templates/page-audit.md`
- `templates/site-audit.md`
- `templates/coverage-matrix.csv`

## Example invocations
- "Audit https://drupalasia.org/events/india-2027 for attendee persona coverage."
- "Audit this sitemap and give a page-by-persona matrix with five highest priority gaps."
- "Check this AI Summit blog draft before publication for audience relevance."
- "Compare this month's audit against the attached baseline."

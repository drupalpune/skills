# How to audit a site or sitemap

Use this for conference-wide editorial coverage, not just a single landing page.

## Steps

1. Supply a sitemap URL, sitemap index URL, or a list of relevant pages.
2. Tell the skill the event type and scope (e.g., DrupalCon, DrupalCamp, meetup, contribution day).
3. Ask for a URL inventory: discovered, attempted, successfully inspected, excluded, and unverified pages.
4. Require a page-type classification and a persona-by-page matrix based **only on inspected content**.
5. Ask for site-wide gaps and overrepresented audiences with clear priority and proposed locations for improvements.
6. Export or copy the matrix to CSV and save the report as a baseline for repeat audits.

## Example prompt

> Audit https://example.org/sitemap.xml with event-audience-coverage. Treat this as a Drupal conference site. Report the discovered and inspected URL counts and a list of inaccessible URLs. Produce a persona-by-page matrix, supported evidence, ten priority recommendations, and a CSV-ready matrix. Do not claim the entire site was audited unless all relevant pages were actually inspected.

## Coverage guardrails

- A URL in the sitemap is **not** proof its page was read.
- If the agent cannot fetch the sitemap, supply URLs or page text; do not invent results.
- If only part of the site is inspected, report `inspected / discovered` and label aggregate results as a sampled audit.
- Do not infer measured reach, conversions, or visitor demographics from page copy alone.
- Score `?` for a page that cannot be inspected, rather than `0`.

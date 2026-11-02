# Releases and compatibility

Version release artifacts by Git tags, for example `event-audience-coverage/v1.1.0`. Do not maintain a committed `dist/` archive; CI uploads generated ZIP artifacts. Publish a GitHub Release manually after CI passes and a human verifies at least one page and one sitemap audit.

The ZIP includes `SKILL.md`, references, templates and offline evaluation fixtures. Clients vary in their skills-upload support, browsing and sitemap access. Describe runtime limitations in the release notes. Do not promise automated crawling if the client cannot fetch pages.

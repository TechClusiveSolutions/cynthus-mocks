# Changelog

All notable changes to cynthus-mocks are recorded here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the versions follow
[Semantic Versioning](https://semver.org/). The Cynthus ecosystem release that bundles
each version is listed in the `cynthus` documentation repository.

Every pull request adds a line under `Unreleased`; a release renames that section to the
version and date.

## [Unreleased]

- Coverage gate (issue 15): CI runs the tests with `--cov-branch` and `.github/scripts/check_coverage.py` checks 90 percent of lines and 80 percent of branches separately.
- Unix line endings (issue 13): `.gitattributes` (`* text=auto eol=lf`), `.editorconfig`, every text file committed with LF, and a CI check (`.github/scripts/check_line_endings.py`) that rejects CRLF.
- README follows the standard quick-start structure (issue 7; cynthus#57): Description, Prerequisites, Installation, Minimal configuration, Gotchas, More documentation. `check_markdown.py` now checks the README headings.
- Documentation for screen readers (issue 5): Markdown is ASCII only, has no tables (lists instead), names the language of every code block, and `README.md` has the standard name. `.github/scripts/check_markdown.py` now enforces this, and checks that relative links resolve, in the `docs-lint` job; markdownlint covers every Markdown file.

## [0.1.0] - 2026-11-01

- Adopt the Cynthus CI, lint and pull-request workflow (#1) (#2)
- Add unit tests for the mock services
- Fix startup script for the chat service
- Remove unneeded files
- Remove references to redis
- Make startup script executeable
- Fix syntax error (missing colon)
- Add startup scripts, Dockerfile, and app source for mock analysis, auth, chat, portal api and portal web services
- Add requirements.txt to the analysis, auth, chat, and portal services
- Fix service definitions in docker compose config
- Add Dockerfile and startup script for the analysis, auth, chat, and portal services
- Initial commit

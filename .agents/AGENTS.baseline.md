# Ocean SDK - Shared Agent Baseline

<!--
Canonical home: the dwave-ocean-sdk repository, next to CONTRIBUTING.rst.
This file is the shared baseline for AI coding agents across all Ocean
packages. Package repos do NOT copy this file; their AGENTS.md carries
their own project facts plus a verbatim copy of the "Non-negotiables"
section below, and fetches the rest of this file on demand (see the
per-package template in AGENTS.template.md).
-->

## Non-negotiables (always apply)

<!-- Canonical list: the short form of rules in CONTRIBUTING.rst, which has
     the details. Package AGENTS.md files copy this section verbatim; update
     them when this changes. -->

- Keep a branch to one focused feature or fix; if the task needs more, say
  so before expanding.
- Make the smallest change that solves the problem; don't touch, refactor,
  or reformat unrelated code.
- New behavior and bug fixes come with unit tests. A bug-fix test fails
  before the fix and passes after it.
- Document any public API you add or change with Google-style docstrings in
  reStructuredText for Sphinx (double-backtick literals, `:class:`/`:func:`
  roles, no Markdown), matching the module's existing convention.
- Add a release note with `reno` for user-visible changes.
- Fill in the "AI Generation Disclosure" section of the PR description:
  the tool and model used and how.

## Working Style

- State your assumptions and a short plan of verifiable goals before editing.
- Before finishing, verify with the narrowest relevant test (see the
  package's `## Commands` section for how to run them).
- Push back if a safer or smaller approach would meet the goal.
- Call out trade-offs when multiple reasonable approaches exist.

## Python Defaults

- Use `pip` and `python -m venv` for dependency and environment commands.
- Support all Python versions the package declares: check `requires-python`
  in `pyproject.toml` (or `python_requires` in setup.py/setup.cfg - packages
  vary) before writing code, and target the minimum version. Don't use
  syntax or stdlib features newer than the floor, unless the floor allows them.
- Use `logging` instead of `print()` in library code.
- Add type hints to public functions, including return types.
- Never silently swallow exceptions: catch only exceptions you can
  meaningfully handle, and let the rest propagate.
- Ask before adding a runtime dependency. Ocean packages keep dependencies
  minimal; new ones affect the whole SDK's install footprint.
- New source files start with the Apache 2.0 license header used by the package;
  copy it from an existing module and update the year.

## Code Quality

- Match the existing package style before introducing a new pattern; Ocean
  packages differ in age and conventions, so the surrounding code wins over
  personal preference.
- Avoid speculative abstractions for single-use code.
- Keep functions focused; prefer splitting once a function does more than one thing.
- After edits, run the package's lint command (see its `## Commands`), if there
  is one, and fix what it reports.

## Commits and Pull Requests

- Don't commit, push, amend, or open/comment on issues and PRs unless
  explicitly asked, and never run destructive git operations (force-push,
  `reset --hard`, branch deletion) without being asked.
- Don't add yourself as a commit co-author; disclosure belongs in the PR
  description (see Non-negotiables).
- When preparing a commit or PR, follow the working repo's `CONTRIBUTING.rst`
  if it has one, and the shared Ocean contributing guide:
  https://raw.githubusercontent.com/dwavesystems/dwave-ocean-sdk/refs/heads/master/CONTRIBUTING.rst
- The Non-negotiables above always apply, even if the guide was not fetched.

## Communication

- When you notice but deliberately don't fix something (adjacent bugs,
  refactoring opportunities, related cleanup), say so briefly and why.
  Don't fix it silently, and don't omit it silently. Skip this when
  there's nothing to report.

# Ocean SDK — Shared Agent Baseline

<!--
Canonical home: the dwave-ocean-sdk repository, next to CONTRIBUTING.rst.
This file is the shared baseline for AI coding agents across all Ocean
packages. Package repos do NOT copy this file; their AGENTS.md carries
their own project facts plus the "Non-negotiables" below inline, and
fetches this file on demand (see the per-package template).
-->

## Working Style

- State your assumptions and a short plan of verifiable goals before editing.
- If the task is ambiguous, ask at most one clarifying question; otherwise
  proceed.
- Make the smallest change that solves the problem; don't touch or refactor
  unrelated code unless asked.
- Before finishing, verify with the narrowest relevant test (see the
  package's `## Commands` section for how to run them).

## Context and Tool Use

- Prefer targeted reads (`grep`, `sed -n 'START,ENDp'`, symbol search) over
  reading whole files.
- Review your edits with `git diff -- <path>` before declaring done.

## Python Defaults

- Use `pip` and `python -m venv` for dependency and environment commands.
- Use `logging` instead of `print()` in library code.
- Add type hints to public functions, including return types.
- Never silently swallow exceptions: catch only exceptions you can
  meaningfully handle, and let the rest propagate.
- Ask before adding a runtime dependency. Ocean packages keep dependencies
  minimal; new ones affect the whole SDK's install footprint.

## Code Quality

- Match the existing package style before introducing a new pattern; Ocean
  packages differ in age and conventions, so the surrounding code wins over
  personal preference.
- Avoid speculative abstractions for single-use code.
- Keep functions focused; prefer splitting once a function does more than
  one thing (rough guide: ~50 lines).
- After edits, run the package's lint command (see its `## Commands`) and
  fix what it reports.

## Commits and Pull Requests

- When preparing a commit or PR, fetch and follow the full contributing
  guide:
  https://raw.githubusercontent.com/dwavesystems/dwave-ocean-sdk/refs/heads/master/CONTRIBUTING.rst
- The non-negotiables (listed in each package's AGENTS.md) always apply,
  even if the guide was not fetched.

## Communication

- Be concise.
- Call out trade-offs when multiple reasonable approaches exist.
- Push back if a safer or smaller approach would meet the goal.

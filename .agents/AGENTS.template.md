# AGENTS.md - <package name>

<!--
Per-package instructions for AI coding agents (Claude Code, Codex, Cursor,
etc.). Tool-agnostic on purpose: most tools read AGENTS.md natively.

Keep this file short and factual. The shared Ocean-wide baseline lives in
the dwave-ocean-sdk repo and is fetched on demand (see "Ocean Baseline").
If you correct an agent twice about the same package fact, add it here.
-->

## Project Overview

<!-- 2-4 lines. What this package is and anything surprising about it.
     Example (dimod-style): "Shared API for binary quadratic samplers.
     Core is C++ under dimod/include/ with Cython bindings; files under
     dimod/*.cpp are generated - edit the .pyx sources instead." -->

## Commands

<!-- Exact, copy-pasteable. Replace the examples with this package's real
     invocations, or remove if not used. This is the highest-value section in
     the file. -->

- Setup: `python -m venv env && env/bin/pip install -r requirements.txt -r tests/requirements.txt`
- Build extensions (if Cython/C++): `python setup.py build_ext --inplace`
- Test (all): `python -m pytest tests/`
- Test (single file): `python -m pytest tests/test_<name>.py -x`
- Lint: `<package's lint command, e.g. ruff check . / flake8>`
- Docs build: `make -C docs html`
- Release note: `reno new <slug>`

## Architecture Notes

<!-- Only facts an agent can't infer by reading the code, and only ones
     you'd otherwise repeat in review. Delete if empty - don't pad. -->

- <e.g. "Public API is what's re-exported in <pkg>/__init__.py; underscore
  modules are internal and not covered by semver.">

## Non-negotiables (always apply)

<!-- Verbatim copy of the "Non-negotiables" section of the Ocean baseline
     (.agents/AGENTS.baseline.md in dwave-ocean-sdk), so they hold even when
     nothing is fetched. When the baseline changes, update this copy. -->

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

## Ocean Baseline

For the full shared working-style and code-quality baseline, fetch:
https://raw.githubusercontent.com/dwavesystems/dwave-ocean-sdk/refs/heads/master/.agents/AGENTS.baseline.md

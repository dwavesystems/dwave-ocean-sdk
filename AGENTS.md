# AGENTS.md — dwave-ocean-sdk

<!-- Instructions for AI coding agents; see .agents/AGENTS.template.md for the
     per-package layout this file follows. Keep it short and factual. -->

## Project Overview

Installer for D-Wave's Ocean SDK tools. The repo is mostly Ocean/Leap docs + package
configuration that pins a set of dozen or so Ocean packages that contain the actual
SDK code. Each package is in its repo, and added as a submodule here, mostly to
facilitate the docs build.

## Commands

- Init: `git submodule update --init --recursive`
- Setup: `python -m venv .venv && pip install . && pip install -r tests/requirements.txt -r docs/requirements.txt`
- Test (all): `python -m unittest`
- Test (single file): `python -m unittest tests.<test_file>.<test_class>.<test_case>`
- Docs build: `make -C docs html`
- Release note: `reno new <slug>`

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
  the tool and model used and how, or "No AI tools used".

## Ocean Baseline

Follow the Ocean-wide baseline: @.agents/AGENTS.baseline.md

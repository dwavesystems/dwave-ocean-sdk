# AGENTS.md — dwave-ocean-sdk

<!--
Per-package instructions for AI coding agents (Claude Code, Codex, Cursor,
etc.). Tool-agnostic on purpose: most tools read AGENTS.md natively;
Claude Code reads it via the one-line CLAUDE.md stub in this repo.

Keep this file short and factual. The shared Ocean-wide baseline lives in
the dwave-ocean-sdk repo and is fetched on demand (see "Ocean Baseline").
If you correct an agent twice about the same package fact, add it here.
-->

## Project Overview

Installer for D-Wave's Ocean SDK tools. The repo is mostly Ocean/Leap docs + package
configuration that pins a set of dozen or so Ocean packages that contain the actual
SDK code. Each package is in its repo, and added as a submodule here, mostly to
facilitate the docs build.

## Commands

- Setup: `python -m venv .venv && pip install . && pip install -r tests/requirements.txt`
- Test (all): `python -m unittest`
- Test (single file): `python -m unittest tests.<test_file>.<test_class>.<test_case>`
- Docs build: `make -C docs html`
- Release note: `reno new <slug>`

## Ocean Baseline

Follow the Ocean-wide baseline: @.agents/AGENTS.baseline.md

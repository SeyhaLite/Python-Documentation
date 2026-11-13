# Phase 0 Inventory Report — CPython 3.15.2 Khmer Documentation

**Audit date:** 2026-11-13  
**Target repository:** https://github.com/SeyhaLite/Python-Documentation  
**Target branch audited:** `main`  
**Work branch:** `phase-0-inventory-3.15.2`

## 1. Upstream source identity

- Repository: `python/cpython`
- Release tag: `v3.15.2`
- Annotated tag object SHA: `a4ed3466611d5941876ff91610601eb29543a5ff`
- Target commit SHA (pinned source): `5e58eaad7c58df58dfa8ea549c87996e01dd1077`
- GitHub tag metadata reports `verified=false`, reason `unsigned`: the annotated Git tag itself is not cryptographically signed.
- GitHub's Release API has no release record for this tag (404), but the official [Python.org Python 3.15.2 release page](https://www.python.org/downloads/release/python-3152/) confirms the release date **2026-10-25**, publishes the source archive SHA-256 and provides Sigstore artifacts.
- XZ source archive SHA-256 listed by Python.org: `8b5536d280142ecf6cdfe15d12a21ba1c65e300bbf7b28a8d0cdb849575797de`.
- Canonical source tree: https://github.com/python/cpython/tree/v3.15.2/Doc

**Source pin:** use commit `5e58eaad7c58df58dfa8ea549c87996e01dd1077`, not a moving branch. CI verified the official Python.org source archive SHA-256 and Sigstore identity (`hugo@python.org`, issuer `https://github.com/login/oauth`). The Git tag itself remains unsigned; the archive digest, attestation and pinned Doc blob hashes are the integrity evidence used for this inventory.

## 2. Upstream Doc inventory

The recursive Git tree at the pinned commit was complete (`truncated=false`).

- Files under `Doc/`: **669**
- reStructuredText files: **557**
- Python/C/header source files: **45** (37 .py, 7 .c, 1 .h); one additional `.inc` source fragment is listed separately with code examples.
- Image/web/diagram assets: **44** in the corrected manifest taxonomy.
- Generated/reference data: **4** (`.abi` and three `.dat` files).
- Sphinx/HTML templates: **9** (under `Doc/tools/templates/`).
- Remaining build/config/support inputs: **9**.
- The categories above are mutually exclusive and sum to **669**.
- Direct navigation entries in `Doc/contents.rst`: **17** (13 major topic groups plus 4 root legal/project pages).

The 557 reStructuredText pages include user-facing documentation, API/reference pages, changelogs, glossary and project/legal material. They are not all independent HTML pages; the official toctree determines published navigation.

## 3. Existing Khmer repository baseline

Repository metadata:
- Default branch: `main`
- Main baseline commit: `4dc18d76c083ffbcc5e4aba756f082a29a14345c`
- Existing source: **17 .rst files** = 15 teaching chapters + `index.rst` + `license_attribution.rst`.
- Existing generated output: **19 HTML pages** under `docs/`.
- Current README explicitly says the 15-chapter scope is **not** a complete translation of CPython `Doc/`.
- `source/index.rst` maps the existing 15 chapters to **43** upstream RST files after PR #4 added `Doc/using/cmdline.rst` and this follow-up added `Doc/builtins/stdtypes.rst` to the `iterators_generators` source mapping. All 43 mapped paths resolve against the pinned CPython tree; this mapping does not claim full translation coverage.
- Approximate existing source baseline: **23,500 Unicode word-like tokens** across the 17 RST files, including headings, code identifiers, directives, index and licensing text. This is an approximate regex count, not human-language-only word count.

Phase 0 version baseline and Phase 1 update:
- At the Phase 0 baseline, `source/conf.py` declared `version = "3.15"` and `release = "3.15.0"`.
- PR #4 updates the Sphinx release metadata, README and index to CPython 3.15.2, and refreshes the version output examples in `getting_started.rst` and `virtual_environments.rst`. The CI runner validates executable Python/REPL examples; prose, static `console` output and platform-specific setup guidance still need separate technical review.

Build configuration observation:
- `.readthedocs.yaml` now sets `fail_on_warning: true`; the PR preview build also passed with this strict setting.

## 4. Manifest and glossary status

- `translation-manifest.csv` contains **669 data rows**, one for every file under the pinned upstream `Doc/` tree, with no duplicate paths and the upstream blob SHA recorded per row.
- Categories have been corrected so they are mutually exclusive and sum to 669:
  - `prose_pages`: 554
  - `include_fragments`: 3
  - `code_examples`: 46
  - `images_assets`: 44
  - `generated_reference_data`: 4
  - `templates`: 9
  - `build_config`: 9
- Exact visible RST titles extracted: **554 / 554 standalone pages**; include fragments: **3**; filename fallback: **0**.
- `word_count` and `dependencies` populated for **557** RST files; word-like tokens: **1,784,681**; files with dependencies: **124** (701 dependency references).
- The source mapping was validated against the pinned tree: **43** upstream RST files mapped after the PR #4 and async-generator source-mapping updates; **0** unresolved references.
- `translation-glossary.csv` contains 21 AI-reviewed draft terms marked `ai_reviewed_pending_human`; human terminology approval remains pending.


## 4.1 Automated metadata extraction

- Source tree commit: `5e58eaad7c58df58dfa8ea549c87996e01dd1077`.
- RST files parsed: **557**.
- Visible titles: **554**; include fragments: **3**; filename fallback: **0**.
- Unicode word-like tokens: **1,784,681** (includes prose, directives, identifiers and code).
- Files with dependencies: **124**; dependency references: **701**.
- Valid existing Khmer mapping: **43** upstream RST files; unresolved references: **0**.
- Source archive integrity: **PASS**.

## 5. Gaps and risks

1. The 21-entry glossary has been reviewed and normalized by the automated audit, but every entry remains `ai_reviewed_pending_human`. A Khmer-language reviewer should approve or revise these terms before large translation batches begin.
2. The existing 15 teaching chapters currently map to 43 upstream RST sources. This records source relationships, not full translation coverage. The remaining upstream pages are intentionally marked `not_started` and should be mapped batch by batch as translation proceeds.
3. PR #4 aligns Sphinx, README and index version metadata with CPython 3.15.2 and refreshes selected version transcripts. Explanatory prose, static console transcripts not covered by the runner, and platform-specific installation guidance still need a separate Phase 1 technical review.
4. The annotated Git tag `v3.15.2` itself is unsigned. The official Python.org source archive SHA-256 and Sigstore identity were verified, and all 669 Doc/ file blobs match the pinned Git tree. Keep the distinction between unsigned tag metadata and verified release archive explicit.
5. File-by-file copyright, third-party asset and attribution review remains necessary before copying or adapting every upstream asset. `Doc/license.rst` states that documentation is under PSF License Version 2 and examples/recipes/other code are dual-licensed under PSF License Version 2 and Zero-Clause BSD from Python 3.8.6 onward.
6. The repository checks in generated `docs/`; treat `source/` as the authoritative translation source and `docs/` as build output.
7. The glossary's human approval and the broader source-mapping work remain open. No new translation batch was started in this inventory PR.

## 6. Validation performed

- [x] Confirmed upstream tag `v3.15.2` resolves to pinned commit `5e58eaad7c58df58dfa8ea549c87996e01dd1077`.
- [x] Downloaded the official Python.org CPython 3.15.2 source archive; SHA-256 matched the published value.
- [x] Verified the source archive Sigstore identity as `hugo@python.org` with issuer `https://github.com/login/oauth`.
- [x] Confirmed the recursive upstream `Doc/` tree is complete and not truncated.
- [x] Manifest contains 669 unique paths; every upstream path and Git blob SHA matches the pinned tree, with zero missing, extra or mismatched files.
- [x] All 669 files have an exclusive category; totals sum to 669.
- [x] Extracted visible titles for 554 standalone RST pages; classified 3 RST include fragments separately; zero filename fallbacks.
- [x] Populated Unicode word-like token counts for all 557 RST files: 1,784,681 tokens.
- [x] Populated dependency fields for all 557 RST files: 701 references across 124 files; `none` is explicit when a page has no dependency.
- [x] Validated the existing Khmer source mapping: 43 upstream RST mappings after PR #4 and the async-generator source update, zero unresolved references.
- [x] Reviewed and normalized 21 glossary entries; human terminology approval remains pending.
- [x] Sphinx strict HTML build: `sphinx-build -b html source <output> -W --keep-going` — PASS.
- [x] Sphinx external link check: `sphinx-build -b linkcheck source <output> -W --keep-going` — PASS.
- [x] Code examples: `tools/run_examples.py` on CPython 3.15.2 — PASS.
- [x] Contrast validation: `tools/check_contrast.py` — PASS.
- [x] Read the Docs PR preview build with `fail_on_warning: true` — PASS.

## 7. Completion status

**Phase 0 automated inventory and quality checks: COMPLETE.** The 669-file source inventory, complete RST metadata, source mapping for existing chapters, release archive verification and strict documentation checks have passed.

**Human review gates remain:** approve the Khmer glossary and complete file-specific licensing/attribution review before broad translation work. Issue #2 remains OPEN because Phases 1–6 (the actual CPython Doc/ Khmer translation and release process) have not been completed.

No new translation batch was started in this Phase 0 PR.

# Phase 0 Inventory Report — CPython 3.15.2 Khmer Documentation

**Audit date:** 2026-11-13  
**Target repository:** https://github.com/SeyhaLite/Python-Documentation  
**Target branch audited:** `main`  
**Work branch:** `phase-0-inventory-3.15.2`

## 1. Upstream source identity

- Repository: `python/cpython`
- Release tag: `v3.15.2`
- Annotated tag object SHA: `a4ed3466611d5941876ff91610601eb29543a5ff`
- Target commit SHA: `5e58eaad7c58df58dfa8ea549c87996e01dd1077`
- Tag object signature: **unsigned / unverified** (GitHub tag metadata reports `verified=false`, reason `unsigned`).
- GitHub Release API lookup for `v3.15.2`: no release record returned (404); the Git tag itself exists and resolves to the commit above.
- Canonical source tree: https://github.com/python/cpython/tree/v3.15.2/Doc

**Source pin recommendation:** use commit `5e58eaad7c58df58dfa8ea549c87996e01dd1077`, not a moving branch. Before publishing, independently validate the unsigned tag against Python.org release checksums/signatures or another trusted release channel.

## 2. Upstream Doc inventory

The recursive Git tree at the pinned commit was complete (`truncated=false`).

- Files under `Doc/`: **669**
- reStructuredText files: **557**
- Python/C/header code files: **45**
- Images and web assets (CSS/JS/HTML/SVG/images): **50**
- Generated/reference data files (`Doc/data/`, .abi, .dat, .inv): **4**
- Template files: **10**
- Remaining build/config/support files: **12**
- Subdirectories under `Doc/`: **23**

Primary navigation groups found in `Doc/contents.rst`: What's New, Tutorial, Using Python, Language Reference, Built-in Functions/Types, Library Reference, Extending, C API, Installing, HOWTOs, FAQ, Deprecations, Glossary, and project/legal pages.

## 3. Existing Khmer repository baseline

Repository metadata:
- Default branch: `main`
- Public repository; working tree baseline is Git commit/tree `4dc18d76c083ffbcc5e4aba756f082a29a14345c` (tree SHA observed during audit).
- Existing source: **17 .rst files** = 15 lesson chapters + `index.rst` + `license_attribution.rst`.
- Existing generated HTML pages: **19**.
- Existing `source/` tree contains 4 static assets and 14 Python helper/config scripts.
- Existing tools include `check_contrast.py`, `fix_rst.py`, and `run_examples.py`.
- Existing Sphinx stack: Sphinx 8.x, sphinx-rtd-theme 3.x, sphinx-copybutton, sphinx-sitemap.
- Existing docs state the 15-chapter scope is not a complete translation of CPython `Doc/`.

Approximate source text baseline: **23,500 Unicode word-like tokens** across the 17 current source RST files, including headings, code identifiers, directives and index/license content. This is a rough reproducible regex token count, not a human-language-only word count.

## 4. Gaps and risks identified

1. No upstream-complete manifest or per-file mapping exists yet; this branch adds the first inventory CSV.
2. The current Khmer content is 15 curated chapters, not a page-by-page translation of all upstream Doc pages.
3. Current `source/conf.py` declares `version = "3.15"` and `release = "3.15.0"`; README/index also describe examples validated on CPython 3.15.0. This must be reviewed against the 3.15.2 target before claiming version alignment.
4. Upstream tag `v3.15.2` is unsigned according to GitHub metadata. The tag resolves, but cryptographic authenticity is not yet independently verified.
5. Word counts for the 669 upstream files, exact page titles, full recursive toctree closure, dependencies, and one-to-many Khmer source mappings remain pending. The CSV leaves these fields blank rather than inventing values.
6. License review must be file-aware. Upstream `Doc/license.rst` says documentation is under PSF License Version 2 and examples/recipes/other code are dual-licensed under PSF License Version 2 and Zero-Clause BSD from Python 3.8.6 onward. Some third-party assets/code may have separate notices.
7. The current repo has checked-in generated `docs/` output. Treat it as build output, not as authoritative translation source.

## 5. Files added in this Phase 0 work branch

- `translation-manifest.csv`: one row per upstream file under `Doc/`, with path, provisional title, category and exact blob SHA. Word count, dependencies, reviewer and Khmer mapping remain explicitly unfilled pending detailed extraction/review.
- `translation-glossary.csv`: starter terminology proposals marked `draft_review_required`; not yet approved terminology.
- `PHASE-0-REPORT.md`: this source pin, inventory, baseline and gap report.

## 6. Completion status

**Phase 0: IN PROGRESS — inventory skeleton and source pin created; detailed content audit is not complete.**

Not yet done: full upstream word count; all page titles/toctree dependency extraction; file-by-file Khmer mapping; independent verification of unsigned release tag; human approval of glossary; local Sphinx build/test (not run in this environment).

No translation batch was started.

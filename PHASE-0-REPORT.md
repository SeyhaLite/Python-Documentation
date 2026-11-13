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
- `source/index.rst` already records a preliminary mapping from each of the 15 chapters to selected upstream source pages. This is useful prior work, but it is not exhaustive and has not yet been normalized into the manifest for every upstream file.
- Approximate existing source baseline: **23,500 Unicode word-like tokens** across the 17 RST files, including headings, code identifiers, directives, index and licensing text. This is an approximate regex count, not human-language-only word count.

Current version alignment needs work:
- `source/conf.py` declares `version = "3.15"` and `release = "3.15.0"`.
- `source/index.rst` and README say the examples were actually verified on CPython 3.15.0.
- Therefore, the project must not claim its existing examples or content have been revalidated on 3.15.2 until the relevant tests are run.

Build configuration observation:
- `.readthedocs.yaml` currently has `fail_on_warning: false`, which does not enforce the issue's intended warning-free build policy. Review this during the quality/build phase; do not change deployment settings as part of this inventory-only batch.

## 4. Manifest and glossary status

- `translation-manifest.csv` contains **669 data rows**, one for every file under the pinned upstream `Doc/` tree, with no duplicate paths and the upstream blob SHA recorded per row.
- Categories have been corrected so they are mutually exclusive and sum to 669:
  - `prose_pages`: 554
  - `code_examples`: 46
  - `images_assets`: 44
  - `generated_reference_data`: 4
  - `templates`: 9
  - `build_config`: 9
- Exact visible RST titles extracted: **553 / 557**; include fragments: **3**; filename fallback: **1**.
- `word_count` and `dependencies` populated for **557** RST files; word-like tokens: **1,784,681**; files with dependencies: **124** (701 dependency references).
- The source mapping was validated against the pinned tree: **41** upstream RST files mapped; **0** unresolved references.
- `translation-glossary.csv` contains 21 AI-reviewed draft terms marked `ai_reviewed_pending_human`; human terminology approval remains pending.

## 4.1 Automated metadata extraction

- Source tree commit: `5e58eaad7c58df58dfa8ea549c87996e01dd1077`.
- RST files parsed: **557**.
- Visible titles: **554**; include fragments: **3**; filename fallback: **0**.
- Unicode word-like tokens: **1,784,681** (includes prose, directives, identifiers and code).
- Files with dependencies: **124**; dependency references: **701**.
- Valid existing Khmer mapping: **41** upstream RST files; unresolved references: **0**.
- Source archive integrity: **PASS**.

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

**Source pin:** use commit `5e58eaad7c58df58dfa8ea549c87996e01dd1077`, not a moving branch. The release page advertises Sigstore metadata, but this audit did **not** independently verify the downloaded archive or its attestation. Keep that as a release gate.

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
  - `prose_pages`: 557
  - `code_examples`: 46
  - `images_assets`: 44
  - `generated_reference_data`: 4
  - `templates`: 9
  - `build_config`: 9
- Exact RST titles extracted: **459 / 557**; filename fallback used for **98** files.
- `word_count` and `dependencies` populated for **557** RST files; word-like tokens: **1,784,681**; files with dependencies: **124** (701 dependency references).
- The preliminary mapping in `source/index.rst` names 42 upstream `.rst` paths. 39 match the pinned tree directly; two legacy paths (`library/stdtypes.rst` and `library/exceptions.rst`) have been normalized to current `builtins/` paths in the manifest; one reference (`develop/testing.rst`) does not exist in the pinned `Doc/` tree and remains unresolved. The manifest now records 41 mapped upstream files against the existing 15 chapter pages. This is only a preliminary source map, not evidence that every referenced page is fully translated.
- `translation-glossary.csv` is a starter glossary; entries remain `draft_review_required`. No term is approved. The draft for `object` was normalized to `វត្ថុ (object)` with a context note, but it still requires human review.

## 5. Gaps and risks

1. Complete manifest metadata still requires exact titles, word-like token counts, dependencies and reviewed Khmer source mapping.
2. Existing Khmer content is 15 curated chapters, not a page-by-page translation of all upstream Doc pages.
3. The current project release metadata and code-validation claims are still at 3.15.0.
4. The Git tag is unsigned; verify the official source archive/attestation through Python.org's published Sigstore materials before treating source authenticity as independently confirmed.
5. File-by-file copyright and license review remains necessary. Upstream `Doc/license.rst` states that Python software/documentation use PSF License Version 2 and that examples, recipes and other code in the documentation are dual-licensed under PSF License Version 2 and Zero-Clause BSD from Python 3.8.6 onward. Some assets or vendored material may have separate notices.
6. The repository checks in generated `docs/`; treat `source/` as the authoritative translation source and `docs/` as build output.
7. Read the Docs warning policy currently does not fail on warnings. Build/link validation must be configured and run before a completeness claim.

## 6. Validation performed

- [x] Confirmed upstream tag `v3.15.2` exists and resolves to the pinned commit.
- [x] Confirmed the recursive upstream `Doc/` tree is not truncated.
- [x] Confirmed manifest row count and exact upstream file-path/SHA inventory when the skeleton was generated.
- [x] Compared repository source layout, README scope, Sphinx configuration, and the current 15-chapter mapping.
- [x] Reviewed `Doc/contents.rst` and `Doc/license.rst` for navigation and licensing scope.
- [ ] Exact title extraction for all 557 RST pages.
- [ ] Word/token counts and dependency extraction for all source pages.
- [x] Register the existing 15-chapter source mapping for 41 matching upstream files; one obsolete reference remains unresolved.
- [ ] Review mapping accuracy and map the remaining upstream pages.
- [ ] Independently verify the official source archive/Sigstore attestation.
- [ ] Human review and approval of glossary terminology.
- [x] Read the Docs preview build for PR #3 returned a successful status (`docs/readthedocs.org:python-documentation-khmer`). This confirms the configured preview build only; `.readthedocs.yaml` still has `fail_on_warning: false`.
- [ ] Run a local/CI strict Sphinx HTML build with `-W --keep-going`, link checks, coverage checks and existing code-example tests.

## 7. Completion status

**Phase 0: IN PROGRESS — source pin and complete path/SHA inventory exist; the detailed metadata and validation gates remain open.**

No translation batch was started. Do not mark the project complete or close Issue #2 until the remaining Phase 0 items are reviewed and passed.

## 4.1 Automated metadata extraction

- Source tree commit: `5e58eaad7c58df58dfa8ea549c87996e01dd1077`.
- RST pages parsed: **557**.
- Exact titles: **540**; filename fallback: **14**.
- Unicode word-like tokens: **1,784,681** (regex `\b[\w]+(?:['’][\w]+)*\b`; includes prose, directives, identifiers and code).
- Files with dependencies: **124**; dependency references: **701**.
- Valid existing Khmer mapping: **41** upstream RST files.
- Unresolved source references: **0** (none).

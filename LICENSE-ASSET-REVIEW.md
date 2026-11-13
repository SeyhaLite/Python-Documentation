# Upstream asset and code-license review register

**Upstream pin:** CPython `5e58eaad7c58df58dfa8ea549c87996e01dd1077` (Python 3.15.2)  
**Status:** inventory created; **file-by-file license review is NOT COMPLETE**. Every entry below remains pending until its exact file header, embedded metadata, generation source, and any third-party attribution are inspected.

## Review rules

- The upstream documentation prose is covered by PSF License Version 2.
- Starting with Python 3.8.6, upstream documentation examples, recipes, and other code are dual-licensed under PSF License Version 2 and Zero-Clause BSD. Confirm the originating file and preserve its notices; do not automatically infer that every helper/tool file has the same licensing treatment.
- Some software and assets included in CPython documentation have separate third-party licenses. Record these individually before copying, modifying, or redistributing them.
- A path being present in the Phase 0 manifest is inventory evidence only. It is not a license approval or a permission to copy it.
- Status values in this register are: `PENDING`, `REVIEWED`, `BLOCKED`. Do not change a status to `REVIEWED` without recording reviewer, evidence/source URL, license, and required notice.

## Project-owned site assets

| Repository path | Current classification | Review status |
|---|---|---|
| `source/_static/python-logo.svg` | Official, unaltered PSF Python logo; trademark rules apply; excluded from MIT site-code scope | Reviewed for scope only; trademark use statement retained |
| `source/_static/python-favicon.ico` | Official Python mark/icon; trademark rules apply; excluded from MIT site-code scope | Reviewed for scope only; trademark use statement retained |
| `source/_static/favicon.svg` | Project-authored favicon | MIT site-code scope |
| `source/_static/khmer.css` | Project-authored stylesheet | MIT site-code scope |
| `source/_templates/breadcrumbs.html` | Project-authored template | MIT site-code scope |
| `source/_templates/layout.html` | Project-authored template with PSF logo usage | Template code is MIT; embedded PSF mark remains excluded |
| Noto Sans Khmer / Noto Serif Khmer | Remote Google Fonts, not stored in the repository | SIL Open Font License 1.1; confirm current provider/license metadata before vendoring |
| Sphinx / sphinx-rtd-theme / sphinx-copybutton / sphinx-sitemap | Build dependencies, installed from package indexes | Third-party package licenses; not relicensed by this repository |

## Upstream visual and non-code assets

**44 files — all PENDING file-level review.**

| Upstream path | Upstream Git blob SHA-1 | Review status |
|---|---|---|
| `Doc/_static/og-image.png` | `0e80751e740387f9305718537f4b26b32e774088` | PENDING |
| `Doc/_static/profiling-sampling-visualization.css` | `6bfbec3b8a6044994e5d3da3be1403c456cf8760` | PENDING |
| `Doc/_static/profiling-sampling-visualization.js` | `3729be6795c1c82933351309c7f6a392765854e4` | PENDING |
| `Doc/_static/tachyon-example-flamegraph.html` | `0563e7ce4acfe6e21b631bd60a664a81aac0a662` | PENDING |
| `Doc/_static/tachyon-example-heatmap.html` | `c762de061ad87d14f5bef4bce6d04656cefd23ad` | PENDING |
| `Doc/c-api/lifecycle.dot` | `dca9f87e9e0acaa5e8ca48a855a108265635dced` | PENDING |
| `Doc/c-api/lifecycle.dot.css` | `3abf95b74da6ba8997b7abcc276082bb447d0603` | PENDING |
| `Doc/c-api/lifecycle.dot.svg` | `7ace27dfcba113f848ed0a0fbb4f66f9ec97969a` | PENDING |
| `Doc/howto/logging_flow.png` | `d60ed7c031585a426e344961ca9e09c2b51d70a7` | PENDING |
| `Doc/howto/logging_flow.svg` | `4974994ac6b4007f9f7cf477d4cc146891dbd587` | PENDING |
| `Doc/library/datetime-inheritance.dot` | `3c6b9b4beb7ab1d3a3b239774dc9dbfc2c809f9c` | PENDING |
| `Doc/library/datetime-inheritance.svg` | `e6b1cf877a574f291c40b70e0e037ce178f5db7f` | PENDING |
| `Doc/library/hashlib-blake2-tree.png` | `faef21b55f96b13beaa7b0f54e7288574e903c81` | PENDING |
| `Doc/library/heapq-binary-tree.svg` | `074a9a44275aec8cefc046a797032f11d2daf586` | PENDING |
| `Doc/library/kde_example.png` | `4c26f26292faa51ba0f724cc50cf9fe7226564c0` | PENDING |
| `Doc/library/pathlib-inheritance.png` | `628ae6e9adb6fa99a779a0fab699c79c6749ba84` | PENDING |
| `Doc/library/pathlib-inheritance.svg` | `01f8684a2b201c5f02acce48189ca26d678c9989` | PENDING |
| `Doc/library/pathlib-parts.svg` | `d561b6563c355ede71a143ac4c504d19e03a8951` | PENDING |
| `Doc/library/profiling-sampling-visualization.html` | `0cbd0f2374deaa0d4d987fbae33e401420a341d3` | PENDING |
| `Doc/library/tachyon-flamegraph.png` | `a17cd304f8bb287d24ee24fa78b6060147594d82` | PENDING |
| `Doc/library/tachyon-gecko-calltree.png` | `71b096940e8fcd08963866c6da6caff822daf44c` | PENDING |
| `Doc/library/tachyon-gecko-flamegraph.png` | `d427ed85ac04e763c8a16cbe65ff7a5f1bf11dfa` | PENDING |
| `Doc/library/tachyon-gecko-opcodes.png` | `9741eb659120b87b60533cd87b34532b86570319` | PENDING |
| `Doc/library/tachyon-heatmap-with-opcodes.png` | `5ad67d131548e49c50964448a467ed9497889dd0` | PENDING |
| `Doc/library/tachyon-heatmap.png` | `47ac1119f4e5725d34a9411f1f1cd1a7469e958d` | PENDING |
| `Doc/library/tachyon-live-mode-1.gif` | `02a56d1767f7dc48ef4ae7b6585606396fcbe9b7` | PENDING |
| `Doc/library/tachyon-live-mode-2.gif` | `7f98edd10f99331b886a4140fbe95cb46066782f` | PENDING |
| `Doc/library/tachyon-pstats.png` | `d0281ade660914db36f7f39fde1a8dc7dfaa9ed4` | PENDING |
| `Doc/library/tk_msg.png` | `6495e63e84650dd16cb50a6da3c51d5c9eca2c57` | PENDING |
| `Doc/library/turtle-star.png` | `0961e1e2153f7238423a55fab9cea824146fde71` | PENDING |
| `Doc/tools/static/changelog_search.js` | `0a77c0d71ae9375e8f5d3382f47ed45076461c81` | PENDING |
| `Doc/tools/static/glossary_search.js` | `13d728dc027f1d45bd3350427971585479d340ff` | PENDING |
| `Doc/tools/static/rtd_switcher.js` | `2bf01a002db90c856d7fe96ed104eefad59391bc` | PENDING |
| `Doc/using/mac_installer_01_introduction.png` | `81e1f4e5ac5c32e6c33cb5ebb8e36bd07d780a83` | PENDING |
| `Doc/using/mac_installer_02_readme.png` | `7e4a9b15cf94f6acf37dec18a985a5adfa5bf99e` | PENDING |
| `Doc/using/mac_installer_03_license.png` | `153daa780efa9e996b63ce36c3e65d01260cad74` | PENDING |
| `Doc/using/mac_installer_04_installation_type.png` | `1fc597c2427ab7663647f3daa3ed71242fe99911` | PENDING |
| `Doc/using/mac_installer_05_custom_install.png` | `c70d93bbcee70a888a5c2a1b6d19506e024caa41` | PENDING |
| `Doc/using/mac_installer_06_summary.png` | `f8a67052ef044795cc835c91d491c25d46790bf5` | PENDING |
| `Doc/using/mac_installer_07_applications.png` | `c39741f33ac807f9ca5cebed692b5f024d3295fc` | PENDING |
| `Doc/using/mac_installer_08_install_certificates.png` | `f476c7f37d245d6ed5379e42e99f6c048c96b43d` | PENDING |
| `Doc/using/mac_installer_09_custom_install_free_threaded.png` | `e867e422e42e4850091f82373e123d1da817c3de` | PENDING |
| `Doc/using/win_install_freethreaded.png` | `12b89c0165d994da57308cc3911b901bdf5eb069` | PENDING |
| `Doc/using/win_installer.png` | `fc9605a79cfcc5181e3227973218b8167419dbe5` | PENDING |

## Upstream code examples, snippets, and documentation tooling

**46 files — all PENDING file-level review.** These paths include examples/snippets and documentation build helpers. Classify each file's role before assuming the examples/recipes dual-license applies.

| Upstream path | Upstream Git blob SHA-1 | Review status |
|---|---|---|
| `Doc/conf.py` | `39b643aadcea26f6d52718a91317f3157798a871` | PENDING |
| `Doc/includes/capi-extension/spammodule-01.c` | `8ddb416e7d6cd08755213fe8c2264c156fd962ae` | PENDING |
| `Doc/includes/dbpickle.py` | `b88ee87d872ab4580500c7d132a372f5dbb61183` | PENDING |
| `Doc/includes/diff.py` | `bc4bd58ff3e3f1154615623958cc991b2672cc6c` | PENDING |
| `Doc/includes/email-alternative.py` | `afe2b4fbb5eb3ff96dcd3537ace5f7a387cdcf20` | PENDING |
| `Doc/includes/email-dir.py` | `aa2a5c7cda52aaee03e13d68b00692870560f4a2` | PENDING |
| `Doc/includes/email-headers.py` | `5def0c90d28d9f59ac9bcf449cfd3f12c5805081` | PENDING |
| `Doc/includes/email-mime.py` | `34c6bdb60fff24b582e66a066861891b88e2bd07` | PENDING |
| `Doc/includes/email-read-alternative.py` | `8d0b4e6eb6b6b571ba37008bed1bda045493d871` | PENDING |
| `Doc/includes/email-simple.py` | `07dc30fd066eace9063de73d99c24723b230bf6b` | PENDING |
| `Doc/includes/email-unpack.py` | `c8cb0be45608308616328960460a761a7f8757ab` | PENDING |
| `Doc/includes/minidom-example.py` | `3b9e9ee2db291372bde27305114abb7e87ea93ca` | PENDING |
| `Doc/includes/mp_newtype.py` | `1c796a564049ad8c39ceca56be0ccf47bcab5a48` | PENDING |
| `Doc/includes/mp_pool.py` | `11101e1a90954e8a2cced8ac609844db6cf8acaa` | PENDING |
| `Doc/includes/mp_workers.py` | `3b92269f897e932d4daef417ae3a3c094933ec26` | PENDING |
| `Doc/includes/ndiff.py` | `32c251bce9120b77d65278dc3420c4de26753113` | PENDING |
| `Doc/includes/newtypes/custom.c` | `039a1a7219349c365a22fe54bc0fd9a332182494` | PENDING |
| `Doc/includes/newtypes/custom2.c` | `1ff8e707d1b0a049e2aa0a4a721c9026292f8872` | PENDING |
| `Doc/includes/newtypes/custom3.c` | `22f50eb0e1de89cea2606f351fdabce06654c205` | PENDING |
| `Doc/includes/newtypes/custom4.c` | `07585aff5987f3d49385dff60ef20ae3594cf0a3` | PENDING |
| `Doc/includes/newtypes/setup.py` | `67f83673bcc657de89faaaa0b6b96ff84fd001ef` | PENDING |
| `Doc/includes/newtypes/sublist.c` | `b784456a4ef6677b298a86be2a3eb0d9b691f307` | PENDING |
| `Doc/includes/newtypes/test.py` | `55a5cf9f68b94ac41c8dc113a17ae2d5e7e4e1c9` | PENDING |
| `Doc/includes/run-func.c` | `392f86d65ecc17754f5e0922ed1f0ee2b908408b` | PENDING |
| `Doc/includes/typestruct.h` | `7ccd0297c3bffd54d73ee1b493f1c9b4e46ea7ea` | PENDING |
| `Doc/includes/tzinfo_examples.py` | `762b1b62fc871d4838ea8d58b423eaac656989e5` | PENDING |
| `Doc/library/token-list.inc` | `655758c4a400ccd745a8bf27a80463b0811a1d3d` | PENDING |
| `Doc/tools/check-epub.py` | `6a10096c1175428421a9eb99b95416141955b550` | PENDING |
| `Doc/tools/check-html-ids.py` | `03cd8a6823a27d5439f10a5dd520e220a7408286` | PENDING |
| `Doc/tools/check-warnings.py` | `859bc1e2d5f5b5c6b1774626fb5d3a0bf7a297b5` | PENDING |
| `Doc/tools/extensions/audit_events.py` | `385a58b2145446f7c8539ae9bb6a000a034a03af` | PENDING |
| `Doc/tools/extensions/availability.py` | `1a2c7b02b444393a18c61bfffe51683558163c48` | PENDING |
| `Doc/tools/extensions/c_annotations.py` | `7a7badb31c960143b8316dda1b9821e6abef7484` | PENDING |
| `Doc/tools/extensions/changes.py` | `e6a912cef8810eaccba43f3cdd0b62776b1f4086` | PENDING |
| `Doc/tools/extensions/glossary_search.py` | `bcda4b7b4355935b3173c87a13cfeee3f001c7fa` | PENDING |
| `Doc/tools/extensions/grammar_snippet.py` | `8078b7ebeb8076c36b980d6e607240283508333a` | PENDING |
| `Doc/tools/extensions/implementation_detail.py` | `fce8375e40d5655be4bbc24bbc31891fe2c95e98` | PENDING |
| `Doc/tools/extensions/issue_role.py` | `477b3a4b2d23b4eef5f853bef86725350e5dee42` | PENDING |
| `Doc/tools/extensions/lexers/__init__.py` | `e12ac5be8139cc26ed9b89e1321908da3437ab94` | PENDING |
| `Doc/tools/extensions/lexers/asdl_lexer.py` | `548ce1271a1db83ea3b1942a0347830ef59f9e06` | PENDING |
| `Doc/tools/extensions/lexers/peg_lexer.py` | `827af205583f61c4b0068ff8121126fbd06d6394` | PENDING |
| `Doc/tools/extensions/misc_news.py` | `e73b6b8f27a211503490810820f677e762102630` | PENDING |
| `Doc/tools/extensions/patchlevel.py` | `9ccaec3dd5ce0fd0ddafac47af34e4e1fd845202` | PENDING |
| `Doc/tools/extensions/profiling_trace.py` | `183c6de48714a437ea26c4f291f0864f8abccd23` | PENDING |
| `Doc/tools/extensions/pydoc_topics.py` | `6c30a9c62626fb1b6dbb7b5a88c1c0921274b4c9` | PENDING |
| `Doc/tools/extensions/pyspecific.py` | `9b335f2976a2fa3f1987e0ea5e252e8e5bda69c7` | PENDING |

## Review record

For each item, append:
- reviewer and date;
- exact source license or copyright header;
- whether the asset is generated, authored by CPython contributors, or copied from a third party;
- required attribution/copyright/permission notices;
- permitted action: link only, reuse unchanged, adapt with notice, or blocked pending permission.

No new upstream binary asset or helper code is copied into the Khmer lessons by this batch. The PSF logo/favicons already used by this repository remain separate trademark assets; the MIT site license does not cover them.

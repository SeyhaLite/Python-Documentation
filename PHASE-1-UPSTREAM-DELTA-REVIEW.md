# Phase 1 — CPython 3.15.2 upstream delta review

**Review date:** 2026-11-13  
**Pinned upstream:** CPython commit `5e58eaad7c58df58dfa8ea549c87996e01dd1077`  
**Compared baseline:** `v3.15.0`  
**Scope:** the nine changed upstream RST files already mapped to seven Khmer lesson chapters. This is a targeted review, not a complete review of all 669 upstream files.

## Summary

The comparison identifies 104 changed files under upstream `Doc/`, including 93 RST files. Nine of those changed RST files are mapped to seven existing Khmer lessons.

This batch adds verified explanations for `frozendict`, explicit lazy imports, `PurePath.full_match()`, `os.scandir()` thread-sharing caveats, generator closing behavior, built-in function `__self__`, and a beginner Windows install-manager path. Several advanced or platform-specific topics remain open and are listed below.

## Chapter-by-chapter review

| Khmer lesson | Changed upstream source | Finding | Status in this batch |
|---|---|---|---|
| `getting_started` | `Doc/using/windows.rst`, `Doc/using/mac.rst` | Windows guidance now recommends the Python install manager and documents MSIX installation, runtime selection and management. The upstream page contains much more advanced configuration, install variants, and troubleshooting than this beginner chapter. The macOS delta is a small shell-variable example correction that is not reproduced in the Khmer lesson. | **PARTIAL** — added a beginner install-manager route for Windows, including MSIX and runtime selection. Advanced manager configuration and troubleshooting remain deferred; macOS has no matching copied command to correct. |
| `strings_collections` | `Doc/builtins/stdtypes.rst` | The built-in types reference includes the Python 3.15 `frozendict` mapping type. The Khmer collections lesson previously covered `dict` and `frozenset`, but not `frozendict`. | **UPDATED** — added the immutable mapping type, its non-`dict` identity, hashability condition, and a tested immutability example. |
| `syntax_variables_types` | `Doc/builtins/stdtypes.rst` | The Khmer syntax lesson already lists `lazy` among Python 3.15 soft keywords. The updated built-in types source also reorganizes iterator/generator reference material. | **REVIEWED** — the `lazy` soft-keyword list already existed and remains current; the import semantics are now explained in `modules_packages`. |
| `file_handling` | `Doc/library/pathlib.rst`, `Doc/library/os.rst`, `Doc/library/json.rst` | `pathlib` documents `PurePath.full_match()` and its whole-path glob semantics. `os.scandir()` adds a thread-sharing caveat: no iterator corruption, but entry distribution is unspecified and closing during another thread's iteration ends it early. The JSON delta is a wording correction, not an API change. | **UPDATED** — added tested `full_match()` examples and the `scandir()` concurrency caveat. |
| `modules_packages` | `Doc/library/sys.rst`, `Doc/reference/simple_stmts.rst` | Python 3.15 adds the lazy-import filter callbacks, the `sys.lazy_modules` debugging set, and module-level `__lazy_modules__` compatibility opt-in. | **UPDATED** — added mode controls, callback signature/return meaning, debugging-set caveats, and `__lazy_modules__` matching rules, including relative imports and `from`-style behavior. |
| `classes_oop` | `Doc/reference/datamodel.rst` | The function object reference adds a `function.__self__` attribute (the defining module object or `None`). The current lesson explains instance `self` and the three method types, but not this advanced function-object attribute. | **UPDATED** — added the built-in-function `__self__` module reference and contrasted it with a bound method's `method.__self__`. |
| `iterators_generators` | `Doc/reference/expressions.rst`, `Doc/builtins/stdtypes.rst` | The upstream reference documents async-iterator and async-generator execution, `__anext__()`, `asend()`, `athrow()`, and `aclose()`, including the deprecated legacy `athrow()` signature and explicit cleanup requirements. | **UPDATED** — added async iteration, tested control-method examples, early-close cleanup guidance, and the Python 3.12 deprecation note. |

## Verified details added

1. **`frozendict`** — mapping values cannot be assigned after construction; it is not a `dict` subclass; it is hashable only when all keys and values are hashable.
2. **Lazy imports (PEP 810)** — `lazy` syntax, restrictions and delayed errors, plus the `sys` mode controls, filter callback (`importing_module`, `imported_module`, `fromlist`), `sys.lazy_modules` caveats and `__lazy_modules__` compatibility behavior.
3. **`PurePath.full_match()`** — matches the complete path against a glob-style pattern; examples demonstrate that `a/b.py` matches `a/*.py` but not `*.py`.
4. **`os.scandir()`** — sharing an iterator does not corrupt it, but thread entry assignment is unspecified and closing it while another thread iterates ends that iteration early.
5. **Generator `close()` and async generators** — since Python 3.13, a generator's return value is returned by `close()`. Async-generator examples cover `__anext__()`, `asend()`, `athrow()`, and `aclose()`, including cleanup after early termination. The legacy `throw(type, value, traceback)` signature is deprecated since 3.12.

## Deferred review work

- Continue the advanced Windows install-manager documentation: runtime variants, configuration files, update/removal behavior, aliases, deployment and troubleshooting.
- Review the full `function.__self__` documentation against the pinned upstream API reference; the beginner lesson only covers the built-in function module pointer versus a bound method.
- Advanced Windows install-manager configuration/troubleshooting remains deferred.
- Async-generator background topics such as event-loop finalization hooks (`sys.set_asyncgen_hooks`) remain outside the current beginner lesson.
- Continue checking the other mapped chapters against their complete upstream sources; this report only covers the nine changed mapped files.
- Human review of terminology and file-by-file licensing/attribution remains a separate gate. See `GLOSSARY-HUMAN-REVIEW.md` and `LICENSE-ASSET-REVIEW.md`.

## Validation policy

The executable examples added in this batch are subject to the repository's CPython 3.15.2 `tools/run_examples.py` CI job. A passing example runner does not validate explanatory prose, static `console` transcripts, platform installation procedures, or completeness against upstream. The full Sphinx strict build, linkcheck, contrast audit, inventory validation, and Read the Docs preview must also pass before merge.

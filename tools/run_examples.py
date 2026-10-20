#!/usr/bin/env python3
"""Verify that every Python code example in the documentation actually runs.

Two kinds of block are checked:

``.. code-block:: python``
    Collected, concatenated per-file and executed. Must exit 0.

``.. code-block:: pycon``
    Parsed into (statement, expected-output) pairs, executed in a persistent
    namespace, and the real stdout/traceback is compared against the expected
    output documented in the .rst file.

Matching rules (deliberately simple, mirroring doctest):
    * an expected line that is exactly ``...`` matches one or more real lines
    * ``...`` inside an expected line matches any substring
    * leading/trailing whitespace is ignored when comparing

``.. literalinclude::`` files are executed too, with the arguments and stdin
declared in EXPECTED_SCRIPTS below.

Usage:  python3 tools/run_examples.py [interpreter]
"""

from __future__ import annotations

import io
import re
import subprocess
import sys
import types
import os
import tempfile
import traceback
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"

# interpreter to verify against — defaults to the newest python3 on PATH
DEFAULT_PY = sys.executable

# literalinclude'd scripts: file -> (argv, stdin, substrings that must appear)
EXPECTED_SCRIPTS = {
    "hello.py": (
        [],
        "",
        ["សួស្ដីពី Python 3.15!", "ផលបូក 1 + 2 = 3"],
    ),
    "argv_demo.py": (
        ["សុខា", "ដារ៉ា"],
        "",
        ["'argv_demo.py', 'សុខា', 'ដារ៉ា'", "ចំនួន argument", "2", "argument ដំបូង: សុខា"],
    ),
    "first.py": (
        [],
        "សុភា\n20\n",
        ["សួស្ដី សុភា!", "អាយុ 20 ឆ្នាំ", "អាយុ 25 ឆ្នាំ"],
    ),
}

# (label, source, expected stdout) - executed as a real script, not exec()'d.
# Some documented outputs depend on being evaluated inside a genuine module:
# under PEP 649 (Python 3.14+) a function's annotations are resolved lazily
# against its owning module, and running the same code through exec() in a
# harness namespace can fall back to the STRING annotation format. Those
# specific claims are verified here, in the environment a reader actually gets.
REAL_SCRIPT_CHECKS: list[tuple[str, str, str]] = [
    (
        "PEP 649 function annotations resolve to real objects",
        '''def greet(name: str, times: int = 1) -> str:
    """docstring"""
    return f"សួស្ដី {name}! " * times

print(greet.__annotations__)
print(repr(greet(42)))
''',
        (
            "{'name': <class 'str'>, 'times': <class 'int'>, 'return': <class 'str'>}\n"
            "'សួស្ដី 42! '"
        ),
    ),
]


def run_real_scripts(py: str) -> tuple[int, int, list[str]]:
    """Execute REAL_SCRIPT_CHECKS as genuine scripts; return (passed, total, msgs)."""
    passed = total = 0
    msgs: list[str] = []
    for label, code, expected in REAL_SCRIPT_CHECKS:
        total += 1
        with tempfile.NamedTemporaryFile(
            "w", suffix=".py", delete=False, encoding="utf-8"
        ) as fh:
            fh.write(code)
            path = fh.name
        proc = subprocess.run([py, path], capture_output=True, text=True, timeout=60)
        Path(path).unlink(missing_ok=True)
        if proc.returncode == 0 and proc.stdout.strip() == expected.strip():
            passed += 1
        else:
            msgs.append(
                f"  real-script check FAILED: {label}" + "\n"
                f"    exit={proc.returncode}" + "\n"
                f"    expected: {expected.strip()!r}" + "\n"
                f"    actual:   {proc.stdout.strip()!r}" + "\n"
                f"    stderr:   {proc.stderr.strip()[:300]!r}"
            )
    return passed, total, msgs


DIRECTIVE_RE = re.compile(r"^\.\. code-block:: (\w+)\s*$")

LITERALINC_RE = re.compile(r"^\.\. literalinclude:: (\S+)")


# --------------------------------------------------------------------------- #
# extraction
# --------------------------------------------------------------------------- #
def extract_blocks(text: str) -> list[tuple[str, str, int]]:
    """Return [(language, body, first_line_no), ...] for every code-block."""
    lines = text.split("\n")
    out: list[tuple[str, str, int]] = []
    i = 0
    while i < len(lines):
        m = DIRECTIVE_RE.match(lines[i].strip()) if lines[i].strip().startswith(".. code-block::") else None
        if not m and lines[i].strip().startswith(".. code-block::"):
            m = DIRECTIVE_RE.match(lines[i].strip())
        if m:
            lang = m.group(1)
            indent = len(lines[i]) - len(lines[i].lstrip())
            j = i + 1
            skip = False
            # skip directive options (:language:, :caption:, ...) and blank lines
            while j < len(lines):
                opt = lines[j].strip()
                if opt == "":
                    j += 1
                    continue
                if opt.startswith(":"):
                    if opt.startswith(":no-test:"):
                        skip = True
                    j += 1
                    continue
                break
            body: list[str] = []
            while j < len(lines):
                line = lines[j]
                if line.strip() == "":
                    body.append("")
                    j += 1
                    continue
                cur_indent = len(line) - len(line.lstrip())
                if cur_indent <= indent:
                    break
                body.append(line[indent + 3:] if len(line) > indent + 3 else line.strip())
                j += 1
            while body and body[-1] == "":
                body.pop()
            if not skip:
                out.append((lang, "\n".join(body), i + 1))
            i = j
        else:
            i += 1
    return out


def dedent_block(body: str) -> str:
    """Strip the common leading indentation from a directive body."""
    lines = body.split("\n")
    indents = [len(l) - len(l.lstrip()) for l in lines if l.strip()]
    if not indents:
        return body
    cut = min(indents)
    return "\n".join(l[cut:] if l.strip() else "" for l in lines)


# --------------------------------------------------------------------------- #
# pycon parsing / matching
# --------------------------------------------------------------------------- #
def parse_pycon(block: str) -> list[tuple[str, list[str]]]:
    """Split a pycon block into [(source, expected_lines), ...]."""
    examples: list[tuple[list[str], list[str]]] = []
    src: list[str] = []
    exp: list[str] = []
    for raw in block.split("\n"):
        if raw.startswith(">>> "):
            if src:
                examples.append((src, exp))
            src, exp = [raw[4:]], []
        elif raw == ">>>":
            if src:
                examples.append((src, exp))
            src, exp = [], []
        elif raw.startswith("... ") or raw.strip() == "...":
            if raw.startswith("... "):
                src.append(raw[4:])
            elif src and (src[-1].startswith(" ") or src[-1].rstrip().endswith(":")):
                pass                      # empty REPL line ending a block
            else:
                exp.append("...")          # ellipsis inside expected output
        elif src:
            exp.append(raw)
        # lines before any >>> are ignored (they cannot occur in our docs)
    if src:
        examples.append((src, exp))
    out = []
    for src_lines, exp in examples:
        while exp and exp[-1].strip() == "":
            exp.pop()
        out.append(("\n".join(src_lines), exp))
    return out


def wildcard_match(expected: str, actual: str) -> bool:
    """Match a single expected line against a single actual line."""
    e, a = expected.strip(), actual.strip()
    if "..." not in e:
        return e == a
    parts = e.split("...")
    pos = 0
    for idx, part in enumerate(parts):
        if part == "":
            continue
        found = a.find(part, pos)
        if found < 0:
            return False
        if idx == 0 and not a.startswith(part):
            return False
        pos = found + len(part)
    if parts[-1] and not a.endswith(parts[-1]):
        return False
    return True


def match_lines(expected: list[str], actual: list[str]) -> bool:
    """Match expected lines against actual lines; bare `...` eats 1+ lines."""
    e = [x.strip() for x in expected if x.strip() != "" or True]
    a = [x.rstrip() for x in actual]
    ei = ai = 0
    while ei < len(e):
        if e[ei].strip() == "...":
            # wildcard line: must consume at least one actual line unless the
            # remainder already matches
            ei += 1
            if ei >= len(e):
                return ai < len(a) or ai == len(a)
            # advance ai until the next expected line matches
            matched = False
            while ai < len(a):
                ai += 1
                if ai < len(a) and wildcard_match(e[ei], a[ai]):
                    matched = True
                    break
            if not matched:
                return False
            ei += 1
            ai += 1
            continue
        if ai >= len(a) or not wildcard_match(e[ei], a[ai]):
            return False
        ei += 1
        ai += 1
    # trailing actual output that was not expected
    while ai < len(a) and a[ai].strip() == "":
        ai += 1
    return ai == len(a)


# --------------------------------------------------------------------------- #
# runners
# --------------------------------------------------------------------------- #
def run_pycon(block: str, namespace: dict) -> tuple[bool, str]:
    """Execute one pycon block in `namespace`; return (ok, report)."""
    problems: list[str] = []
    for source, expected in parse_pycon(block):
        # a line that is only a comment is not executable in REPL "single" mode
        code_only = "\n".join(
            ln for ln in source.split("\n") if ln.strip() and not ln.strip().startswith("#")
        )
        if not code_only.strip():
            continue
        buf = io.StringIO()
        err_text: list[str] = []
        try:
            with redirect_stdout(buf):
                code = compile(source, "<pycon>", "single")
                exec(code, namespace)
        except Exception:
            tb = traceback.format_exc().splitlines()
            # drop the runner's own frames, keep the REPL-style output
            cut = next((i for i, l in enumerate(tb) if 'File "<pycon>"' in l), None)
            if cut is None:
                err_text = ["Traceback (most recent call last):"] + tb[-2:]
            else:
                err_text = ["Traceback (most recent call last):"] + tb[cut:]
        got = buf.getvalue().splitlines() + err_text
        if not match_lines(expected, got):
            problems.append(
                "  source:   " + source.replace("\n", " ⏎ ")[:110]
                + "\n  expected: " + repr([x.strip() for x in expected])[:160]
                + "\n  actual:   " + repr([x.rstrip() for x in got])[:160]
            )
    return (not problems), "\n".join(problems)


def run_python_block(block: str, namespace: dict) -> tuple[bool, str]:
    """Execute a `python` code-block in the shared namespace; must not raise."""
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            exec(compile(block, "<python-block>", "exec"), namespace)
    except Exception:
        tb = traceback.format_exc().splitlines()
        cut = next((i for i, l in enumerate(tb) if 'File "<python-block>"' in l), 0)
        return False, "  raised:\n    " + "\n    ".join(tb[cut:])
    return True, ""


def run_script(path: Path, py: str) -> tuple[bool, str]:
    argv, stdin, needles = EXPECTED_SCRIPTS[path.name]
    proc = subprocess.run(
        [py, str(path), *argv],
        capture_output=True, text=True, timeout=60, input=stdin, cwd=path.parent,
    )
    if proc.returncode != 0:
        return False, f"  exit {proc.returncode}\n{proc.stderr[-900:]}"
    missing = [n for n in needles if n not in proc.stdout]
    if missing:
        return False, f"  missing in stdout: {missing}\n  got: {proc.stdout!r}"
    return True, ""


# --------------------------------------------------------------------------- #
def main() -> int:
    py = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PY

    # The examples MUST be compiled by the interpreter under test — f-string
    # grammar, annotation evaluation and error messages are version dependent.
    if Path(py).resolve() != Path(sys.executable).resolve():
        return subprocess.call([py, str(Path(__file__).resolve())])

    # file examples create/remove real files — do it in a scratch directory
    workdir = tempfile.mkdtemp(prefix="khmer-docs-examples-")
    os.chdir(workdir)
    ver = subprocess.run([py, "-V"], capture_output=True, text=True).stdout.strip()
    print(f"verifying against: {py}  ({ver})\n")

    total = passed = 0
    failures: list[str] = []

    for rst in sorted(SOURCE.glob("*.rst")):
        text = rst.read_text(encoding="utf-8")
        blocks = extract_blocks(text)

        # One shared namespace per file, so examples can build on each other.
        # It must be a real ModuleType registered in sys.modules: under PEP 649
        # (Python 3.14+) a function's annotations are resolved lazily against
        # its module, and a plain dict makes them fall back to strings.
        mod = types.ModuleType(f"_khmer_docs_{rst.stem}")
        sys.modules[mod.__name__] = mod
        ns: dict = mod.__dict__
        ns["__name__"] = mod.__name__
        ns["__builtins__"] = __builtins__
        file_pycon = file_python = 0

        for lang, body, lineno in blocks:
            body = dedent_block(body)
            if lang == "pycon":
                total += 1
                file_pycon += 1
                ok, msg = run_pycon(body, ns)
                if ok:
                    passed += 1
                else:
                    failures.append(f"{rst.name}:{lineno} (pycon)\n{msg}")
            elif lang == "python":
                total += 1
                file_python += 1
                ok, msg = run_python_block(body, ns)
                if ok:
                    passed += 1
                else:
                    failures.append(f"{rst.name}:{lineno} (python)\n{msg}")

        # literalinclude'd scripts
        for m in LITERALINC_RE.finditer(text):
            rel = m.group(1)
            p = SOURCE / rel
            if p.suffix == ".py" and p.exists() and p.name in EXPECTED_SCRIPTS:
                total += 1
                ok, msg = run_script(p, py)
                if ok:
                    passed += 1
                else:
                    failures.append(f"{rst.name} → {rel}\n{msg}")

        print(f"  {rst.name:<32} pycon={file_pycon:<4} python={file_python:<4}")

    # environment-sensitive claims, verified in a genuine script
    rp, rt, rmsg = run_real_scripts(py)
    passed += rp
    total += rt
    failures += rmsg
    print(f"  {'real-script checks':<32} {rp}/{rt}")

    print(f"\n{'='*70}\nresult: {passed}/{total} examples verified")
    if failures:
        print(f"\n{len(failures)} FAILING:\n")
        for f in failures:
            print(f + "\n")
        return 1
    print("all code examples run correctly ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())

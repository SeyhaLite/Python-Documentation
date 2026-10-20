"""One-off patch: align the real-script annotation check with the documented
example, and mark that example :no-test: with a recorded reason."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---- 1) make REAL_SCRIPT_CHECKS reproduce the documented function exactly --
tool = ROOT / "tools" / "run_examples.py"
s = tool.read_text(encoding="utf-8")

old_code = """def greet(name: str, times: int = 1) -> str:
    \"\"\"docstring\"\"\"
    return f"hi {name}! " * times
"""
new_code = """def greet(name: str, times: int = 1) -> str:
    \"\"\"docstring\"\"\"
    return f"\u179f\u17bd\u179f\u17d2\u178a\u17b8 {name}! " * times
"""
assert old_code in s, "check source not found"
s = s.replace(old_code, new_code, 1)
tool.write_text(s, encoding="utf-8")
print("tools/run_examples.py: check source now matches the documented example")

# ---- 2) mark the pycon example :no-test: and record why --------------------
rst = ROOT / "source" / "functions_scope.rst"
t = rst.read_text(encoding="utf-8")

marker = ".. code-block:: pycon\n\n   >>> greet(\"\u179f\u17bb\u1781\u17b6\", 2)"
assert marker in t, "pycon block not found"

reason = (
    ".. code-block:: pycon\n"
    "   :no-test:\n"
    "\n"
    "   >>> greet(\"\u179f\u17bb\u1781\u17b6\", 2)"
)
t = t.replace(marker, reason, 1)

anchor = "   >>> greet(42)                # Python \u1798\u17b7\u1793\u179a\u17b6\u17c4\u17c6\u17a0\u17b6\u1798\u1791\u17c1!\n   '\u179f\u17bd\u179f\u17d2\u178a\u17b8 42! '\n"
assert anchor in t, "tail of pycon block not found"

note = anchor + (
    "\n"
    "..  :no-test: \u2014 PEP 649 (Python 3.14+) \u1792\u17b6\u17c6\u17c1\u17b6\u179a\u1787\u17cd\u17a2\u1793\u17bd\u1785\u17c6\u178e\u17b6\u178f\u17cb annotation \u1792\u17c6\u1793\u17b6\u1798\u17c6\u1787\u17b6\u17c6\u1798\u17c9\u1796\u17b8 module\n"
    "..  \u1796\u17b7\u178f\u1794\u17d2\u179a\u17b6\u1780\u178a\u17ba \u1780\u17b6\u179a\u178a\u17c6\u178e\u17be\u1780\u178f\u17b6\u1798\u179a\u1799\u17c8 exec() \u1780\u17d3\u1793\u17bb\u1784 namespace \u179f\u17b6\u1780\u179b\u17d2\u1794\u1794\u17b6\u179a\u1793\u17cd\u17a2\u17b6\u1785\u1792\u17d2\u179b\u17b6\u1780\u1791\u17c5\u179f\u17c6\u1796\u17bb\u1780\n"
    "..  STRING format\u17d4 \u179b\u1791\u17d2\u1792\u1795\u179b\u1781\u17b6\u1784\u179b\u17be\u179f\u178f\u17d2\u179a\u17bc\u179c\u1794\u17b6\u1793\u1795\u17d2\u1791\u17d2\u1791\u17b6\u1782\u17cb\u1795\u17d2\u178f\u17b6\u1782\u17cb\u178a\u17c4\u1785\u17a1\u17c2\u1780\n"
    "..  \u178a\u17c6\u1796\u17c5\u1782\u1780\u17d2\u179a\u17b6\u179f REAL_SCRIPT_CHECKS \u1780\u17d3\u1793\u17bb\u1784 tools/run_examples.py\u17d5\n"
)
t = t.replace(anchor, note, 1)
rst.write_text(t, encoding="utf-8")
print("source/functions_scope.rst: example marked :no-test: with recorded reason")

"""Fix the rst issues reported by `sphinx-build -W` for the new chapters:
   1. list-table continuation lines must align with the cell text
   2. section title underlines shorter than the title
   3. duplicate cross-reference labels across files
"""

from pathlib import Path
import re

SOURCE = Path(__file__).resolve().parent.parent / "source"
UNDER = "=-~^\"*_+#"


# --------------------------------------------------------------------------- #
# 1) list-table cell continuation alignment
# --------------------------------------------------------------------------- #
def fix_table_continuations(text: str) -> tuple[str, int]:
    lines = text.split("\n")
    fixed = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(\s*)\* - (.*)$", line)
        if m:
            indent = len(m.group(1))
            # first cell text starts after "* - "
            cell_col = indent + 4
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if not nxt.strip():
                    break
                if re.match(r"^\s*\* - ", nxt) or re.match(r"^\s*- ", nxt):
                    # a `  - ` continuation cell inside the same row
                    mm = re.match(r"^(\s*)- (.*)$", nxt)
                    if mm and len(mm.group(1)) == indent + 2:
                        cell_col = indent + 4
                        j += 1
                        continue
                    break
                # bare continuation text of the current cell
                stripped = nxt.lstrip()
                cur_indent = len(nxt) - len(stripped)
                # a bare "-" is an empty sibling cell, not continuation text
                if stripped in {"-", "*"}:
                    j += 1
                    continue
                if cur_indent < cell_col and stripped and not stripped.startswith("*"):
                    lines[j] = " " * cell_col + stripped
                    fixed += 1
                elif cur_indent > indent and not stripped.startswith(("*", "-")):
                    cell_col = cur_indent
                j += 1
            i = j
        else:
            i += 1
    return "\n".join(lines), fixed


# --------------------------------------------------------------------------- #
# 2) title underline length (paired overline/underline must match exactly)
# --------------------------------------------------------------------------- #
def fix_underlines(text: str) -> tuple[str, int]:
    lines = text.split("\n")
    fixed = 0

    def is_ul(s: str) -> bool:
        t = s.strip()
        return bool(t) and all(c in UNDER for c in t) and not s[:1].isspace()

    for i in range(1, len(lines) - 1):
        title, over, under = lines[i], lines[i - 1], lines[i + 1]
        if not title or title[0].isspace() or not is_ul(under):
            continue
        if is_ul(over) and over[0] == under[0]:
            # docutils requires overline == underline == at least the title
            if len(over) != len(under) or len(over) < len(title):
                want = max(len(title), len(over), len(under))
                lines[i - 1] = over[0] * want
                lines[i + 1] = under[0] * want
                fixed += 1
        elif len(title) > len(under):
            lines[i + 1] = under[0] * (len(title) + 4)
            fixed += 1
    return "\n".join(lines), fixed


# --------------------------------------------------------------------------- #
# 3) duplicate labels — give each file a unique prefix
# --------------------------------------------------------------------------- #
RENAME = {
    "exceptions.rst": {
        "with-statement": "exceptions-with-statement",
        "best-practices": "exceptions-best-practices",
        "summary": "exceptions-summary",
    },
    "modules_packages.rst": {
        "best-practices": "modules-best-practices",
        "summary": "modules-summary",
    },
    "classes_oop.rst": {
        "best-practices": "classes-best-practices",
        "summary": "classes-summary",
    },
    "file_handling.rst": {
        "with-statement": "files-with-statement",
        "best-practices": "files-best-practices",
    },
    "syntax_variables_types.rst": {
        "summary": "syntax-summary",
    },
    "decorators.rst": {
        "best-practices": "decorators-best-practices",
        "summary": "decorators-summary",
    },
    "type_hints.rst": {
        "best-practices": "typehints-best-practices",
        "summary": "typehints-summary",
    },
    "iterators_generators.rst": {
        "summary": "iterators-summary",
        "best-practices": "iterators-best-practices",
    },
    "standard_library.rst": {
        "summary": "stdlib-summary",
        "best-practices": "stdlib-best-practices",
    },
    "virtual_environments.rst": {
        "summary": "venv-summary",
        "best-practices": "venv-best-practices",
    },
    "testing_debugging.rst": {
        "summary": "testing-summary",
        "best-practices": "testing-best-practices",
    },
}


def rename_labels(text: str, mapping: dict) -> tuple[str, int]:
    n = 0
    for old, new in mapping.items():
        # the label definition
        if f".. _{old}:" in text:
            text = text.replace(f".. _{old}:", f".. _{new}:", 1)
            n += 1
        # any :ref: pointing at it inside this same file
        text = re.sub(rf":ref:`{re.escape(old)}`", f":ref:`{new}`", text)
        text = re.sub(rf":ref:`([^<`]*?)<{re.escape(old)}>`", rf":ref:`\1<{new}>`", text)
    return text, n


# --------------------------------------------------------------------------- #
def main() -> None:
    for rst in sorted(SOURCE.glob("*.rst")):
        original = rst.read_text(encoding="utf-8")
        text = original

        text, n_cont = fix_table_continuations(text)
        text, n_under = fix_underlines(text)
        n_lab = 0
        if rst.name in RENAME:
            text, n_lab = rename_labels(text, RENAME[rst.name])

        if text != original:
            rst.write_text(text, encoding="utf-8")
            print(f"{rst.name:<32} table-cont={n_cont:<3} underlines={n_under:<3} labels={n_lab}")

    # cross-file :ref: targets must be updated too
    print("\nchecking cross-file refs...")
    all_labels = set()
    for rst in sorted(SOURCE.glob("*.rst")):
        all_labels |= set(re.findall(r"^\.\. _([\w-]+):", rst.read_text(encoding="utf-8"), re.M))
    dupes = {}
    for rst in sorted(SOURCE.glob("*.rst")):
        for lab in re.findall(r"^\.\. _([\w-]+):", rst.read_text(encoding="utf-8"), re.M):
            dupes.setdefault(lab, []).append(rst.name)
    bad = {k: v for k, v in dupes.items() if len(v) > 1}
    print("  duplicate labels remaining:", bad or "none")

    for rst in sorted(SOURCE.glob("*.rst")):
        t = rst.read_text(encoding="utf-8")
        for ref in set(re.findall(r":ref:`(?:[^<`]*<)?([\w-]+)>?`", t)):
            if ref not in all_labels:
                print(f"  !! {rst.name}: unresolved :ref:`{ref}`")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""WCAG contrast audit for source/_static/khmer.css.

Reads the CSS custom properties declared in the dark and light palette blocks,
then checks every foreground/background pair the stylesheet actually uses.

Pass criteria (WCAG 2.1):
    * normal text  -> >= 4.50:1
    * large text / UI components (borders, non-text) -> >= 3.00:1

Usage:  python3 tools/check_contrast.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "source" / "_static" / "khmer.css"

NORMAL_MIN = 4.50
LARGE_MIN = 3.00

# (label, foreground, background, is_large_text)
# Values may be a var name (without --) or a literal hex colour.
PAIRS: list[tuple[str, str, str, bool]] = [
    # --- page chrome -------------------------------------------------------
    ("body text on page", "kh-text", "kh-page-bg", False),
    ("heading on page", "kh-heading", "kh-page-bg", True),
    ("muted on page", "kh-muted", "kh-page-bg", False),
    ("link on page", "kh-link", "kh-page-bg", False),
    ("link:hover on page", "kh-link-hover", "kh-page-bg", False),
    ("link:visited on page", "kh-visited", "kh-page-bg", False),
    ("src-note on page", "kh-muted", "kh-page-bg", False),
    ("breadcrumb on page", "kh-muted", "kh-page-bg", False),
    # --- inline chips ------------------------------------------------------
    ("chip text on chip bg", "kh-chip-fg", "kh-chip-bg", False),
    ("code.literal on chip bg", "kh-literal-fg", "kh-chip-bg", False),
    # --- code blocks -------------------------------------------------------
    ("code text on code bg", "kh-code-fg", "kh-code-bg", False),
    # --- tables ------------------------------------------------------------
    ("table header text", "kh-heading", "kh-thead-bg", False),
    ("table cell text", "kh-text", "kh-card-bg", False),
    ("table striped cell text", "kh-text", "kh-stripe-bg", False),
    # --- sidebar -----------------------------------------------------------
    ("nav item on sidebar", "kh-nav-fg", "kh-sidebar-bg", False),
    ("nav caption on sidebar", "kh-nav-caption", "kh-sidebar-bg", False),
    ("nav current item", "kh-nav-current-fg", "kh-nav-current-bg", False),
    ("nav hover (white text)", "#ffffff", "kh-nav-hover-bg", False),
    ("sidebar title", "kh-navheader-fg", "kh-navheader-bg", True),
    ("sidebar version muted", "kh-navheader-muted", "kh-navheader-bg", False),
    ("sidebar title hover", "kh-navheader-hover", "kh-navheader-bg", False),
    ("mobile top bar text", "kh-navheader-fg", "kh-navheader-bg", True),
    # --- inputs / buttons --------------------------------------------------
    ("search input text", "kh-input-fg", "kh-input-bg", False),
    ("search placeholder", "kh-input-ph", "kh-input-bg", False),
    ("input border (UI component)", "kh-input-border", "kh-input-bg", True),
    ("button text", "kh-btn-fg", "kh-btn-bg", False),
    ("button border (UI component)", "kh-btn-border", "kh-btn-bg", True),
    # --- search highlight --------------------------------------------------
    ("mark highlight", "kh-mark-fg", "kh-mark-bg", False),
    # --- admonition bodies (body text on tinted body bg) -------------------
    ("note body text", "kh-text", "ad-note-bg", False),
    ("warning body text", "kh-text", "ad-warn-bg", False),
    ("danger body text", "kh-text", "ad-danger-bg", False),
    ("tip body text", "kh-text", "ad-tip-bg", False),
    ("seealso body text", "kh-text", "ad-seealso-bg", False),
    ("generic admonition text", "kh-text", "ad-gen-bg", False),
    ("todo body text", "kh-text", "ad-todo-bg", False),
    # --- admonition titles (title fg on title bg) --------------------------
    ("note title", "ad-note-f", "ad-note-t", False),
    ("warning title", "ad-warn-f", "ad-warn-t", False),
    ("danger title", "ad-danger-f", "ad-danger-t", False),
    ("tip title", "ad-tip-f", "ad-tip-t", False),
    ("seealso title", "ad-seealso-f", "ad-seealso-t", False),
    ("generic admonition title", "ad-gen-f", "ad-gen-t", False),
    ("todo title", "ad-todo-f", "ad-todo-t", False),
    # --- blockquote / misc -------------------------------------------------
    ("blockquote text", "kh-text", "kh-card-bg", False),
    ("figure caption", "kh-muted", "kh-page-bg", False),
    ("footer text", "kh-muted", "kh-page-bg", False),
    ("theme toggle text", "kh-muted", "kh-page-bg", False),
    ("theme toggle hover", "kh-link-hover", "kh-page-bg", False),
    # --- light-mode-only chrome (sidebar stays dark in light mode) ---------
    # checked separately below
]

# extra pairs that only make sense in one theme
DECORATIVE: list[tuple[str, str, str]] = [
    # (label, foreground/border, background) — reported, never fails the build
    ("table/cell border (decorative separator)", "kh-border", "kh-page-bg"),
    ("table soft border (decorative separator)", "kh-border-soft", "kh-card-bg"),
    ("code block border (decorative)", "kh-border", "kh-page-bg"),
    ("chip border (decorative)", "kh-chip-border", "kh-page-bg"),
]

LIGHT_ONLY: list[tuple[str, str, str, bool]] = [
    ("nav item on light sidebar", "#d9d9d9", "#343131", False),
    ("nav caption on light sidebar", "#b3b3b3", "#343131", False),
    ("nav hover white on light sidebar", "#ffffff", "#4e4a4a", False),
    ("sidebar title on light navheader", "#eef1f6", "#2c3e50", True),
]

# every Pygments token must be legible on the code background
PYGMENTS = [
    "c", "ch", "cm", "cp", "cpf", "c1", "cs", "cd",
    "k", "kc", "kd", "kn", "kp", "kr", "kt", "ow",
    "s", "sa", "sb", "sc", "dl", "sd", "s2", "se", "sh", "si", "sx", "sr", "s1", "ss",
    "m", "mb", "mf", "mh", "mi", "il", "mo",
    "n", "na", "nb", "bp", "nc", "no", "nd", "ni", "ne", "nf", "fm", "nl", "nn",
    "nx", "py", "nt", "nv", "vc", "vg", "vi", "vm",
    "o", "p", "w", "err", "gr", "gt", "gd", "gi", "gh", "gp", "gu", "go",
]


# --------------------------------------------------------------------------- #
def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    def chan(c: int) -> float:
        s = c / 255.0
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg: str, bg: str) -> float:
    l1 = relative_luminance(hex_to_rgb(fg))
    l2 = relative_luminance(hex_to_rgb(bg))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def parse_vars(css: str) -> dict[str, dict[str, str]]:
    """Return {'dark': {name: hex}, 'light': {name: hex}}."""
    themes: dict[str, dict[str, str]] = {"dark": {}, "light": {}}

    def grab(block: str) -> dict[str, str]:
        out: dict[str, str] = {}
        for m in re.finditer(r"(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,8})\s*;", block):
            out[m.group(1)[2:]] = m.group(2)
        return out

    dark = re.search(
        r"html,\s*html\[data-theme=\"dark\"\]\s*\{(.*?)\n\}", css, re.S
    )
    light = re.search(r"html\[data-theme=\"light\"\]\s*\{(.*?)\n\}", css, re.S)
    if not dark or not light:
        raise SystemExit("could not locate the dark/light palette blocks in khmer.css")
    themes["dark"] = grab(dark.group(1))
    themes["light"] = grab(light.group(1))
    return themes


def resolve(value: str, vars_: dict[str, str]) -> str:
    if value.startswith("#"):
        return value
    if value not in vars_:
        raise KeyError(value)
    return vars_[value]


def audit(theme: str, vars_: dict[str, str], pairs: list[tuple[str, str, str, bool]]):
    fails: list[str] = []
    worst = ("", 99.0)
    for label, fg, bg, large in pairs:
        try:
            f, b = resolve(fg, vars_), resolve(bg, vars_)
        except KeyError as exc:
            fails.append(f"  [{theme}] {label}: unknown colour {exc}")
            continue
        ratio = contrast(f, b)
        need = LARGE_MIN if large else NORMAL_MIN
        if ratio < need:
            fails.append(
                f"  [{theme}] {label}: {f} on {b} = {ratio:.2f}:1 "
                f"(need {need:.2f}:1) — FAIL"
            )
        if ratio < worst[1] and not large:
            worst = (label, ratio)
    return fails, worst


def main() -> int:
    css = CSS.read_text(encoding="utf-8")
    themes = parse_vars(css)

    print(f"khmer.css contrast audit — {CSS.relative_to(ROOT)}\n")
    for theme, vars_ in themes.items():
        print(f"{theme}: {len(vars_)} custom properties parsed")
    print()

    all_fails: list[str] = []
    total = 0
    for theme, vars_ in themes.items():
        pairs = list(PAIRS)
        if theme == "light":
            pairs += LIGHT_ONLY
        fails, worst = audit(theme, vars_, pairs)
        total += len(pairs)
        all_fails += fails
        status = "PASS" if not fails else "FAIL"
        print(f"[{theme}] {len(pairs) - len(fails)}/{len(pairs)} pairs pass "
              f"(lowest normal-text ratio: {worst[1]:.2f}:1 — {worst[0]})  {status}")

        # Pygments tokens
        pyg_fails = 0
        for tok in PYGMENTS:
            name = f"py-{tok}"
            if name not in vars_:
                continue
            try:
                bg = resolve("kh-code-bg", vars_)
            except KeyError:
                continue
            ratio = contrast(resolve(name, vars_), bg)
            total += 1
            if ratio < LARGE_MIN:      # syntax tokens: 3:1 minimum, 4.5:1 preferred
                pyg_fails += 1
                all_fails.append(
                    f"  [{theme}] pygments .{tok}: {resolve(name, vars_)} on {bg} "
                    f"= {ratio:.2f}:1 (need {LARGE_MIN:.2f}:1) — FAIL"
                )
        print(f"[{theme}] pygments: {len(PYGMENTS) - pyg_fails}/{len(PYGMENTS)} "
              f"tokens >= {LARGE_MIN:.1f}:1")

    # decorative separators — reported for transparency, not graded
    print("\ndecorative separators (not graded — structure is conveyed by text):")
    for theme, vars_ in themes.items():
        for label, fg, bg in DECORATIVE:
            try:
                f, b = resolve(fg, vars_), resolve(bg, vars_)
            except KeyError:
                continue
            print(f"  [{theme}] {label}: {f} on {b} = {contrast(f, b):.2f}:1")

    print(f"\n{'='*70}\ntotal graded checks: {total}")
    if all_fails:
        print(f"FAILURES: {len(all_fails)}\n")
        print("\n".join(all_fails))
        return 1
    print("all colour pairs meet the WCAG contrast requirement ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())

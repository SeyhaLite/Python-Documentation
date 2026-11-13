#!/usr/bin/env python3
"""Build a source-pinned CPython Doc/ translation manifest.

The source tree is expected at --upstream-root and must contain Doc/.
Word counts are Unicode word-like tokens, not language-specific segmentation.
Every upstream file is checked against the Git blob SHA in the manifest.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

UPSTREAM_COMMIT = "5e58eaad7c58df58dfa8ea549c87996e01dd1077"
WORD_RE = re.compile(r"\b[\w]+(?:['’][\w]+)*\b", re.UNICODE)
HEADING_CHARS = set("=-~^'\"\x60#*+_:%<>")


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def extract_title(text: str) -> str:
    """Return the first section title using reStructuredText adornments."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    for i, line in enumerate(lines):
        current = line.strip()
        if not current:
            continue
        module_title = re.match(r":mod:`!?([^`]+)`\s+---\s+(.+)$", current)
        if module_title and i + 1 < len(lines):
            underline = lines[i + 1].strip()
            if (len(underline) >= len(current) and len(underline) >= 3
                    and len(set(underline)) == 1 and underline[0] in HEADING_CHARS):
                return f"{module_title.group(1)} — {module_title.group(2)}"
        if current.startswith(".. ") or current.startswith(":"):
            continue
        if i + 2 < len(lines):
            over, title, under = lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip()
            if (len(over) >= 3 and len(set(over)) == 1 and over[0] in HEADING_CHARS
                    and title and len(under) >= len(title) and len(set(under)) == 1
                    and under[0] == over[0]):
                return re.sub(r"\s+", " ", title)
        if i + 1 < len(lines):
            under = lines[i + 1].strip()
            if (len(under) >= 3 and len(set(under)) == 1 and under[0] in HEADING_CHARS
                    and len(under) >= len(current)):
                return re.sub(r"\s+", " ", current)
    return ""


def extract_dependencies(text: str) -> list[str]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    dependencies: set[str] = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        directive = re.match(r"^(\s*)\.\.\s+toctree::\s*$", line)
        if directive:
            base_indent = len(directive.group(1))
            j = i + 1
            while j < len(lines):
                raw, stripped = lines[j], lines[j].strip()
                if not stripped:
                    j += 1
                    continue
                indent = len(raw) - len(raw.lstrip())
                if indent <= base_indent:
                    break
                if stripped.startswith(":") or stripped.startswith(".. "):
                    j += 1
                    continue
                explicit = re.search(r"<([^<>]+)>", stripped)
                target = explicit.group(1).strip() if explicit else stripped
                if target and not target.startswith(("http://", "https://")):
                    dependencies.add('toctree:' + target)
                j += 1
            i = j
            continue
        asset = re.match(r"^\s*\.\.\s+(include|literalinclude|image|figure|download)::\s+(\S+)", line)
        if asset:
            dependencies.add(f"{asset.group(1)}:{asset.group(2)}")
        i += 1
    for match in re.finditer(r":doc:`([^`]+)`", text):
        value = match.group(1).strip()
        explicit = re.search(r"<([^<>]+)>", value)
        target = (explicit.group(1) if explicit else value).strip()
        if target and not target.startswith(("http://", "https://")):
            dependencies.add("doc:" + target)
    return sorted(dependencies)


def parse_source_mapping(index_text: str, valid_rst_paths: set[str]) -> tuple[dict[str, set[str]], list[str]]:
    mapping: dict[str, set[str]] = {}
    missing: list[str] = []
    blocks = re.split(r"(?=^\s*\* - )", index_text, flags=re.MULTILINE)
    for block in blocks:
        lesson_match = re.search(r":doc:`([^`]+)`", block)
        if not lesson_match:
            continue
        local_path = f"source/{lesson_match.group(1).strip()}.rst"
        for source in re.findall(r"``([^`]+\.rst)``", block):
            upstream_path = source.strip()
            if not upstream_path.startswith("Doc/"):
                upstream_path = "Doc/" + upstream_path.lstrip("/")
            if upstream_path not in valid_rst_paths:
                missing.append(upstream_path)
            else:
                mapping.setdefault(upstream_path, set()).add(local_path)
    return mapping, sorted(set(missing))


def read_manifest(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    if not fields or "upstream_path" not in fields or "upstream_sha" not in fields:
        raise ValueError("Manifest is missing upstream_path/upstream_sha")
    if "title_provisional" in fields and "title" not in fields:
        fields[fields.index("title_provisional")] = "title"
        for row in rows:
            row["title"] = row.pop("title_provisional", "")
    if "title_source" not in fields:
        fields.insert(fields.index("title") + 1, "title_source")
        for row in rows:
            row["title_source"] = ""
    return fields, rows


def write_manifest(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def update_report(path: Path, summary: dict) -> None:
    if not path.exists():
        return
    report = path.read_text(encoding="utf-8")
    report = report.replace(
        "- Titles are still provisional filename-based values; exact RST heading extraction remains pending.",
        f"- Exact RST titles extracted: **{summary['rst_titles_exact']} / {summary['rst_files']}**; "
        f"filename fallback used for **{summary['rst_titles_fallback']}** files.",
    )
    report = report.replace(
        "- `word_count` and `dependencies` remain unfilled; full RST text parsing and recursive toctree/include extraction remain pending.",
        f"- `word_count` and `dependencies` populated for **{summary['rst_files']}** RST files; "
        f"word-like tokens: **{summary['rst_word_like_tokens']:,}**; files with dependencies: "
        f"**{summary['rst_files_with_dependencies']}** ({summary['dependency_edges']} dependency references).",
    )
    report = re.sub(r"\\n- \[ \] Review mapping accuracy", "\n- [ ] Review mapping accuracy", report)
    if "## 4.1 Automated metadata extraction" in report:
        report = report.split("## 4.1 Automated metadata extraction")[0].rstrip()
    report += (
        "\n\n## 4.1 Automated metadata extraction\n\n"
        f"- Source tree commit: `{UPSTREAM_COMMIT}`.\n"
        f"- RST pages parsed: **{summary['rst_files']}**.\n"
        f"- Exact titles: **{summary['rst_titles_exact']}**; filename fallback: **{summary['rst_titles_fallback']}**.\n"
        f"- Unicode word-like tokens: **{summary['rst_word_like_tokens']:,}** "
        "(regex `\\b[\\w]+(?:['’][\\w]+)*\\b`; includes prose, directives, identifiers and code).\n"
        f"- Files with dependencies: **{summary['rst_files_with_dependencies']}**; "
        f"dependency references: **{summary['dependency_edges']}**.\n"
        f"- Valid existing Khmer mapping: **{summary['mapped_rst_files']}** upstream RST files.\n"
        f"- Unresolved source references: **{len(summary['unresolved_source_refs'])}** "
        f"({', '.join(summary['unresolved_source_refs']) if summary['unresolved_source_refs'] else 'none'}).\n"
    )
    path.write_text(report, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-root", type=Path, required=True,
                        help="CPython source root containing Doc/")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--require-blob-sha", action="store_true")
    parser.add_argument("--release-verified", action="store_true", help="Set after SHA-256 and Sigstore checks pass")
    args = parser.parse_args()
    repo_root, upstream_root = args.repo_root.resolve(), args.upstream_root.resolve()
    manifest_path = repo_root / "translation-manifest.csv"
    fields, rows = read_manifest(manifest_path)
    by_path = {row["upstream_path"]: row for row in rows}
    if len(by_path) != len(rows):
        raise ValueError("Manifest contains duplicate upstream_path values")
    rst_paths = {p for p in by_path if p.endswith(".rst")}
    mapping, unresolved = parse_source_mapping(
        (repo_root / "source/index.rst").read_text(encoding="utf-8"), rst_paths
    )
    missing, mismatches, fallbacks = [], [], []
    word_total = dependency_files = dependency_edges = 0
    for upstream_path, row in by_path.items():
        disk_path = upstream_root / upstream_path
        if not disk_path.is_file():
            missing.append(upstream_path)
            continue
        data = disk_path.read_bytes()
        # The source archive expands Git eol=crlf for Windows batch files.
        # Normalize that one text format back to canonical Git blob bytes.
        blob_data = data.replace(b"\r\n", b"\n") if upstream_path.lower().endswith(".bat") else data
        actual_sha = git_blob_sha(blob_data)
        if actual_sha != row.get("upstream_sha", ""):
            mismatches.append({"path": upstream_path, "expected": row.get("upstream_sha"), "actual": actual_sha})
            continue
        if upstream_path.endswith(".rst"):
            text = data.decode("utf-8")
            title = extract_title(text)
            if upstream_path.startswith("Doc/includes/") and not title:
                row["title"] = "[included fragment — no standalone page title]"
                row["title_source"] = "include_fragment"
                row["category"] = "include_fragments"
            elif title:
                row["title"], row["title_source"] = title, "rst_heading"
            else:
                row["title"] = Path(upstream_path).stem.replace("-", " ").replace("_", " ")
                row["title_source"] = "filename_fallback"
                fallbacks.append(upstream_path)
            count = len(WORD_RE.findall(text))
            row["word_count"] = str(count)
            word_total += count
            dependencies = extract_dependencies(text)
            row["dependencies"] = "; ".join(dependencies)
            if dependencies:
                dependency_files += 1
                dependency_edges += len(dependencies)
            row["notes"] = (
                "Unicode word-like token count; includes prose, reST markup, identifiers and code. "
                "Dependencies include toctree, :doc: and file directives."
            )
        else:
            row["title_source"] = row.get("title_source") or "filename"
        row["khmer_path"] = "; ".join(sorted(mapping.get(upstream_path, set())))
    if missing:
        raise FileNotFoundError(f"Missing {len(missing)} upstream files: {missing[:10]}")
    if mismatches:
        raise ValueError(f"Git blob SHA mismatch for {len(mismatches)} files: {mismatches[:10]}")
    actual_doc_files = {
        "Doc/" + p.relative_to(upstream_root / "Doc").as_posix()
        for p in (upstream_root / "Doc").rglob("*") if p.is_file()
    }
    extra = sorted(actual_doc_files - set(by_path))
    absent = sorted(set(by_path) - actual_doc_files)
    if extra or absent:
        raise ValueError(f"Doc path mismatch: extra={extra[:10]}, absent={absent[:10]}")
    write_manifest(manifest_path, fields, rows)
    summary = {
        "source_commit": UPSTREAM_COMMIT, "doc_files": len(rows), "rst_files": len(rst_paths),
        "rst_titles_exact": sum(1 for p in rst_paths if by_path[p].get("title_source") == "rst_heading"),
        "rst_titles_fallback": len(fallbacks),
        "rst_include_fragments": sum(1 for p in rst_paths if by_path[p].get("title_source") == "include_fragment"),
        "rst_title_fallback_paths": fallbacks, "rst_word_like_tokens": word_total,
        "rst_files_with_dependencies": dependency_files, "dependency_edges": dependency_edges,
        "mapped_rst_files": len(mapping), "mapped_paths": sorted(mapping),
        "release_integrity_verified": args.release_verified,
        "unresolved_source_refs": unresolved, "missing_files": missing, "sha_mismatches": mismatches,
        "extra_doc_files": extra, "absent_doc_files": absent,
    }
    (repo_root / "phase0-inventory-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    update_report(repo_root / "PHASE-0-REPORT.md", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

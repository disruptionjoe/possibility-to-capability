"""[T]/[E]/[F] check-tag linter for P2C test fixtures.

HOUSE RULE (swing-2 process note, adopted from lane 3's referee): every
check in a fixture is tagged
  [T] theorem-consequence  -- outcome fixed by construction; carries NO
      evidential weight; listed separately,
  [E] genuine experiment   -- outcome not fixed at formalization time,
  [F] failing-direction control -- a deliberately broken variant that FAILS,
      proving the checker it protects has teeth (same code path).
Only [E] and [F] count as evidence; a headline may not count [T] checks.

DECLARED CONVENTION (forward, for new fixtures) -- a module-level registry:

    CHECKS = {
        "a1: A_a is eta-contractive":  {"tag": "E"},
        "a1-fail: eta is not":         {"tag": "F", "protects": "a1: A_a is eta-contractive"},
        "setup: S eta S = -eta":       {"tag": "T"},
    }

Rules enforced in registry mode (violations -> nonzero exit):
  R1  every entry has tag in {T, E, F};
  R2  every [F] entry declares "protects" naming an existing non-[F] entry
      (the same-code-path requirement itself is behavioral and cannot be
      proven statically; the declaration makes it auditable);
  R3  every literal check name used at runtime (check("...") calls or
      checks["..."] assignments) appears in CHECKS and vice versa;
  R4  headline hygiene: any "N/N" style headline literal where N equals the
      TOTAL check count (including [T]) is flagged.

INLINE-TAG MODE (krein_norm_link_probe.py style): check names begin with
"[T] ", "[E] ", "[F] ".  [F] names must reference their protected checker
by id ("<id>-fail" where <id> is the id of another non-dynamic check, or an
explicit "protects:" phrase).

LEGACY-SCAN MODE: fixtures that predate the convention (untagged
checks[...] dicts, teeth suites) get an ADVISORY report -- every untagged
check is listed; the report is the demonstration, exit stays 0 unless
--strict.

Pure Python stdlib (ast + re).  Usage:
    python tef_check_tag_linter.py [--strict] FILE [FILE ...]
    python tef_check_tag_linter.py --selftest
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from typing import Any

TAG_RE = re.compile(r"^\[([TEF])\]\s*")
ID_RE = re.compile(r"^\[[TEF]\]\s*([A-Za-z0-9_']+)")
F_TARGET_RE = re.compile(r"([A-Za-z0-9_']+)-fail")
HEADLINE_RE = re.compile(r"\b(\d+)\s*/\s*(\d+)\b")
CHECK_DICT_NAMES = {"checks", "teeth", "t"}


def _literal_prefix(node: ast.AST) -> tuple[str, bool]:
    """(name, is_dynamic) for a str constant or an f-string key/name."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value, False
    if isinstance(node, ast.JoinedStr):
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
            else:
                parts.append("{?}")
        return "".join(parts), True
    return "", True


def extract_checks(tree: ast.AST) -> list[dict[str, Any]]:
    """All check registrations: check(...) calls and checks[...]=... stores."""
    found: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and node.args
        ):
            name, dynamic = _literal_prefix(node.args[0])
            if name or not dynamic:
                found.append(
                    {"name": name, "dynamic": dynamic, "line": node.lineno,
                     "via": "check-call"}
                )
        elif isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if (
                isinstance(target, ast.Subscript)
                and isinstance(target.value, ast.Name)
                and target.value.id in CHECK_DICT_NAMES
            ):
                name, dynamic = _literal_prefix(target.slice)
                if name:
                    found.append(
                        {"name": name, "dynamic": dynamic,
                         "line": node.lineno,
                         "via": f"{target.value.id}[...]="}
                    )
    return found


def extract_registry(tree: ast.AST) -> dict[str, dict[str, Any]] | None:
    """Module-level CHECKS = {literal dict}, or None if absent."""
    for node in ast.iter_child_nodes(tree):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "CHECKS"
            and isinstance(node.value, ast.Dict)
        ):
            registry: dict[str, dict[str, Any]] = {}
            for key, value in zip(node.value.keys, node.value.values):
                if not (isinstance(key, ast.Constant) and isinstance(key.value, str)):
                    continue
                try:
                    registry[key.value] = ast.literal_eval(value)
                except (ValueError, SyntaxError):
                    registry[key.value] = {"tag": None}
            return registry
    return None


def extract_headline_suspects(
    tree: ast.AST, total_checks: int
) -> list[dict[str, Any]]:
    suspects = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            for m in HEADLINE_RE.finditer(node.value):
                n1, n2 = int(m.group(1)), int(m.group(2))
                if n1 == n2 and n1 > 1:
                    suspects.append(
                        {"line": node.lineno, "literal": m.group(0),
                         "counts_total_including_T": n1 == total_checks}
                    )
    return suspects


def lint_source(source: str, path: str) -> dict[str, Any]:
    tree = ast.parse(source, filename=path)
    registry = extract_registry(tree)
    runtime_checks = extract_checks(tree)
    violations: list[str] = []
    advisories: list[str] = []

    if registry is not None:
        convention = "registry"
        names = list(registry)
        tags = {n: (registry[n] or {}).get("tag") for n in names}
        untagged = [n for n in names if tags[n] not in ("T", "E", "F")]
        for n in untagged:
            violations.append(f"R1 untagged registry entry: {n!r}")
        for n in names:
            if tags[n] == "F":
                protects = (registry[n] or {}).get("protects")
                if not protects:
                    violations.append(f"R2 [F] entry lacks 'protects': {n!r}")
                elif protects not in registry:
                    violations.append(
                        f"R2 [F] {n!r} protects unknown check {protects!r}")
                elif tags.get(protects) == "F":
                    violations.append(
                        f"R2 [F] {n!r} protects another [F]: {protects!r}")
        runtime_names = {c["name"] for c in runtime_checks if not c["dynamic"]}
        for n in sorted(runtime_names - set(names)):
            violations.append(f"R3 runtime check not in CHECKS registry: {n!r}")
        for n in sorted(set(names) - runtime_names):
            advisories.append(
                f"R3 registry entry with no statically-visible runtime "
                f"check (may be dynamic): {n!r}")
        tag_counts = {t: sum(1 for n in names if tags[n] == t) for t in "TEF"}
        total = len(names)
    else:
        names = [c["name"] for c in runtime_checks]
        tags = {}
        untagged = []
        f_checks, ids = [], set()
        for c in runtime_checks:
            m = TAG_RE.match(c["name"])
            tag = m.group(1) if m else None
            tags[c["name"]] = tag
            if tag is None:
                untagged.append(c)
            idm = ID_RE.match(c["name"])
            if tag == "F":
                f_checks.append(c)
            elif idm and not idm.group(1).endswith("fail"):
                # only non-[F] checks contribute protectable ids: an [F]'s
                # own id must not satisfy its own reference requirement
                ids.add(idm.group(1).rstrip(":"))
        if untagged:
            convention = "legacy-scan" if len(untagged) == len(runtime_checks) \
                else "mixed"
            for c in untagged:
                advisories.append(
                    f"untagged check (line {c['line']}, {c['via']}): "
                    f"{c['name']!r}")
        else:
            convention = "inline-tags"
        for c in f_checks:
            tgt = F_TARGET_RE.search(c["name"])
            if "protects:" in c["name"]:
                continue
            if not tgt or tgt.group(1).split("'")[0] not in ids:
                (violations if convention == "inline-tags" else advisories
                 ).append(
                    f"[F] check does not reference the checker it protects "
                    f"(line {c['line']}): {c['name']!r}")
        tag_counts = {
            t: sum(1 for v in tags.values() if v == t) for t in "TEF"}
        total = len(runtime_checks)

    headline = extract_headline_suspects(tree, total)
    for h in headline:
        msg = (f"headline literal {h['literal']!r} (line {h['line']})"
               + (" equals TOTAL check count INCLUDING [T]"
                  if h["counts_total_including_T"] else ""))
        if h["counts_total_including_T"]:
            violations.append("R4 " + msg)
        else:
            advisories.append("R4? " + msg)

    evidential = tag_counts.get("E", 0) + tag_counts.get("F", 0)
    return {
        "path": path,
        "convention": convention,
        "total_checks": total,
        "tag_counts": tag_counts,
        "untagged_count": total - sum(tag_counts.values()),
        "evidential_count_E_plus_F": evidential,
        "T_checks_excluded_from_headline": tag_counts.get("T", 0),
        "violations": violations,
        "advisories": advisories,
    }


def lint_file(path: Path) -> dict[str, Any]:
    return lint_source(path.read_text(encoding="utf-8"), str(path))


# ------------------------------------------------------------- self-test

GOOD_REGISTRY_SRC = '''
CHECKS = {
    "s1: setup identity": {"tag": "T"},
    "x1: real experiment": {"tag": "E"},
    "x1-fail: broken variant": {"tag": "F", "protects": "x1: real experiment"},
}
def main():
    def check(name, value, expected=True): ...
    check("s1: setup identity", True)
    check("x1: real experiment", True)
    check("x1-fail: broken variant", False, expected=False)
    print("evidential 2 of 3; [T] listed separately")
'''

UNTAGGED_SRC = '''
def audit():
    checks = {}
    checks["some_property_holds"] = True
    return checks
'''

ORPHAN_F_SRC = '''
def main():
    def check(name, value, expected=True): ...
    check("[E] a1: experiment", True)
    check("[F] zz9-fail: broken variant referencing no known checker", False, expected=False)
'''

T_HEADLINE_SRC = '''
def main():
    def check(name, value, expected=True): ...
    check("[T] t1: fixed by construction", True)
    check("[T] t2: fixed by construction", True)
    check("[E] e1: experiment", True)
    print("3/3 checks pass")
'''


def selftest() -> int:
    checks: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        checks.append((name, bool(value), expected))

    good = lint_source(GOOD_REGISTRY_SRC, "<good>")
    check("[E] compliant registry fixture lints clean (0 violations, "
          "evidential count 2, one [T] listed separately)",
          not good["violations"] and good["evidential_count_E_plus_F"] == 2
          and good["T_checks_excluded_from_headline"] == 1)

    untagged = lint_source(UNTAGGED_SRC, "<untagged>")
    check("[F] untagged legacy check IS reported "
          "(protects: R1/untagged detection, same lint_source path)",
          not any("untagged check" in a for a in untagged["advisories"]),
          expected=False)

    orphan = lint_source(ORPHAN_F_SRC, "<orphan>")
    check("[F] orphan [F] (references no existing checker id) IS flagged "
          "(protects: R2/F-reference rule, same lint_source path)",
          not any("does not reference" in v for v in orphan["violations"]),
          expected=False)

    theadline = lint_source(T_HEADLINE_SRC, "<t-headline>")
    check("[F] headline counting [T] checks IS flagged "
          "(protects: R4/headline hygiene, same lint_source path)",
          not any(v.startswith("R4") for v in theadline["violations"]),
          expected=False)

    check("[T] tag regex recognizes all three tags",
          all(TAG_RE.match(f"[{t}] x") for t in "TEF"))

    failures = []
    print("TEF LINTER SELF-TEST")
    print("=" * 74)
    n_t = n_e = n_f = 0
    for name, value, expected in checks:
        ok = value == expected
        n_t += name.startswith("[T]")
        n_e += name.startswith("[E]")
        n_f += name.startswith("[F]")
        print(f"{'PASS' if ok else 'UNEXPECTED'}  {name}: {value}")
        if not ok:
            failures.append(name)
    print(f"\nEVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}")
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:]]
    if "--selftest" in args:
        return selftest()
    strict = "--strict" in args
    paths = [Path(a) for a in args if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    worst = 0
    for path in paths:
        report = lint_file(path)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if report["violations"] and (
            strict or report["convention"] in ("registry", "inline-tags")
        ):
            worst = 1
        if strict and (report["advisories"] or report["untagged_count"]):
            worst = 1
    return worst


if __name__ == "__main__":
    sys.exit(main())

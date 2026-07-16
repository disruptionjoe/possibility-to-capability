"""Two-phase preregistration verifier (prereg-verify v0.1).

CONVENTION (two-phase preregistration): an EXPECTATIONS artifact -- declared
checks with expected values (keys named "expected", per the swing-2 referee's
EXPECTED_* naming demand), frozen judgment calls, rival forecasts, and stop
conditions -- is committed in its own commit BEFORE any results exist. A
RESULTS artifact is committed strictly afterward and hash-links the
expectations file by git blob id and commit. This verifier proves the temporal
ordering MECHANICALLY from git history; it does not judge the scientific
content of either artifact.

Verifier gates (all must PASS; every tampering control below fails through
this same verify_prereg code path):
  P1 RESULTS_COMMITTED       results file is tracked; its introducing commit's
                             bytes parse with a complete prereg_ref
  P2 EXPECTATIONS_AT_COMMIT  the claimed expectations commit exists and
                             contains the expectations path
  P3 BLOB_MATCH              the expectations blob at that commit equals the
                             blob id the results claim to have been tested
                             against
  P4 STRICT_ORDERING         the expectations commit is a strict ancestor of
                             the results-introducing commit (the same commit,
                             or results-first, fails)
  P5 COMMIT_SEPARATION       the results-introducing commit does not add or
                             touch the expectations path
  P6 EXPECTATIONS_IMMUTABLE  exactly one commit in history touches the
                             expectations path, and the HEAD blob still equals
                             the registered blob (post-hoc edits, amends, and
                             deletions fail)
  P7 EXPECTATIONS_SHAPE      the registered expectations declare nonempty
                             declared_checks (each with a check_id and an
                             "expected" value), frozen_judgment_calls,
                             rival_forecasts, and nonempty stop_conditions

Amendment policy: a committed expectations artifact is immutable. A revision
gets a NEW file and a NEW prereg id committed before the corresponding run;
the superseded artifact stays in place as history.

Pure Python stdlib + git subprocess. Usage:
    python tests/prereg_verify.py <repo_root> <results_path_relative_to_root>
    python tests/prereg_verify.py --selftest
Exit 0 iff every gate passes (or, under --selftest, every check matches its
declared expectation).
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

REQUIRED_PREREG_REF = (
    "prereg_id",
    "expectations_path",
    "expectations_git_blob",
    "expectations_commit",
)
REQUIRED_EXPECTATION_FIELDS = (
    "declared_checks",
    "frozen_judgment_calls",
    "rival_forecasts",
    "stop_conditions",
)


def git(repo: Path, *args: str) -> tuple[int, str]:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, (proc.stdout or "").strip()


def commits_touching(repo: Path, path: str) -> list[str]:
    """Commits touching path, newest first; the last entry introduced it."""
    code, out = git(repo, "log", "--format=%H", "--", path)
    return out.split() if code == 0 and out else []


def blob_id_at(repo: Path, commit: str, path: str) -> str | None:
    code, out = git(repo, "rev-parse", f"{commit}:{path}")
    return out if code == 0 else None


def show_text(repo: Path, commit: str, path: str) -> str | None:
    code, out = git(repo, "show", f"{commit}:{path}")
    return out if code == 0 else None


def resolve_commit(repo: Path, name: str) -> str | None:
    code, out = git(repo, "rev-parse", "--verify", f"{name}^{{commit}}")
    return out if code == 0 else None


def strict_ancestor(repo: Path, ancestor: str, descendant: str) -> bool:
    if ancestor == descendant:
        return False
    code, _ = git(repo, "merge-base", "--is-ancestor", ancestor, descendant)
    return code == 0


def paths_touched(repo: Path, commit: str) -> list[str]:
    code, out = git(repo, "show", "--format=", "--name-only", commit)
    if code != 0:
        return []
    return [line.strip() for line in out.splitlines() if line.strip()]


def _expectations_shape_errors(raw: str | None) -> list[str]:
    if raw is None:
        return ["expectations bytes unavailable at the registered commit"]
    try:
        value = json.loads(raw)
    except ValueError as error:
        return [f"expectations JSON parse error: {error}"]
    if not isinstance(value, dict):
        return ["expectations root must be an object"]
    errors: list[str] = []
    for field in REQUIRED_EXPECTATION_FIELDS:
        if not isinstance(value.get(field), list):
            errors.append(f"expectations field {field!r} must be a list")
    declared = value.get("declared_checks")
    if isinstance(declared, list):
        if not declared:
            errors.append("declared_checks must be nonempty")
        for index, entry in enumerate(declared):
            if not isinstance(entry, dict):
                errors.append(f"declared_checks[{index}] must be an object")
                continue
            check_id = entry.get("check_id")
            if not (isinstance(check_id, str) and check_id.strip()):
                errors.append(f"declared_checks[{index}] needs a check_id")
            if "expected" not in entry:
                errors.append(
                    f"declared_checks[{index}] needs an 'expected' value")
    stops = value.get("stop_conditions")
    if isinstance(stops, list) and not stops:
        errors.append("stop_conditions must be nonempty")
    return errors


def verify_prereg(repo: Path, results_path: str) -> dict[str, Any]:
    gates: list[dict[str, Any]] = []

    def gate(name: str, ok: bool, detail: str) -> bool:
        gates.append(
            {"gate": name, "status": "PASS" if ok else "FAIL", "detail": detail}
        )
        return ok

    report: dict[str, Any] = {
        "contract": "prereg-verify-v0.1",
        "repo": str(repo),
        "results_path": results_path,
        "gates": gates,
    }

    results_history = commits_touching(repo, results_path)
    results_commit = results_history[-1] if results_history else None
    raw_results = (
        show_text(repo, results_commit, results_path) if results_commit else None
    )
    prereg_ref: dict[str, str] | None = None
    p1_detail = "results path has no commit history"
    if raw_results is not None:
        try:
            parsed = json.loads(raw_results)
        except ValueError as error:
            parsed = None
            p1_detail = f"results JSON parse error: {error}"
        if isinstance(parsed, dict):
            candidate = parsed.get("prereg_ref")
            if isinstance(candidate, dict) and all(
                isinstance(candidate.get(key), str) and candidate.get(key)
                for key in REQUIRED_PREREG_REF
            ):
                prereg_ref = {key: candidate[key] for key in REQUIRED_PREREG_REF}
                p1_detail = f"results introduced in commit {results_commit}"
            else:
                p1_detail = "prereg_ref missing or incomplete in committed results"
    if not gate("P1 RESULTS_COMMITTED", prereg_ref is not None, p1_detail):
        report["valid"] = False
        report["nonclaim"] = NONCLAIM
        return report

    exp_path = prereg_ref["expectations_path"]
    claimed_commit = prereg_ref["expectations_commit"]
    claimed_blob = prereg_ref["expectations_git_blob"]
    report["results_commit"] = results_commit
    report["results_amended_after_introduction"] = len(results_history) > 1

    full_exp = resolve_commit(repo, claimed_commit)
    actual_blob = (
        blob_id_at(repo, full_exp, exp_path) if full_exp is not None else None
    )
    gate(
        "P2 EXPECTATIONS_AT_COMMIT",
        actual_blob is not None,
        f"expectations blob at {claimed_commit}:{exp_path} is "
        f"{actual_blob or 'ABSENT (commit or path unresolvable)'}",
    )
    gate(
        "P3 BLOB_MATCH",
        actual_blob is not None and actual_blob == claimed_blob,
        f"claimed blob {claimed_blob} vs actual {actual_blob}",
    )
    gate(
        "P4 STRICT_ORDERING",
        full_exp is not None
        and results_commit is not None
        and strict_ancestor(repo, full_exp, results_commit),
        f"expectations commit {full_exp} must strictly precede "
        f"results commit {results_commit}",
    )
    touched = paths_touched(repo, results_commit) if results_commit else []
    gate(
        "P5 COMMIT_SEPARATION",
        exp_path not in touched,
        f"results commit touches {touched}; expectations path must not appear",
    )
    exp_history = commits_touching(repo, exp_path)
    head_blob = blob_id_at(repo, "HEAD", exp_path)
    gate(
        "P6 EXPECTATIONS_IMMUTABLE",
        full_exp is not None
        and exp_history == [full_exp]
        and head_blob == claimed_blob,
        f"commits touching expectations: {exp_history}; "
        f"HEAD blob {head_blob} vs registered {claimed_blob}",
    )
    shape_errors = _expectations_shape_errors(
        show_text(repo, full_exp, exp_path) if full_exp is not None else None
    )
    gate(
        "P7 EXPECTATIONS_SHAPE",
        not shape_errors,
        "; ".join(shape_errors) if shape_errors else
        "declared_checks with expected values, frozen judgment calls, "
        "rival forecasts, and stop conditions all present",
    )

    report["valid"] = all(entry["status"] == "PASS" for entry in gates)
    report["nonclaim"] = NONCLAIM
    return report


NONCLAIM = (
    "A PASS proves committed-order and byte identity from git history only; "
    "it does not establish that the declared checks are good science or that "
    "the observed values are true."
)


# ------------------------------------------------------------- self-test

CHECKS = {
    "setup: selftest fixture repos build with distinct commits":
        {"tag": "T"},
    "g1: compliant two-phase pair verifies with every gate PASS":
        {"tag": "E"},
    "g1-fail-same-commit: joint expectations+results commit is rejected "
    "(protects: g1 via the strict-ordering and separation gates, same "
    "verify_prereg path)":
        {"tag": "F",
         "protects": "g1: compliant two-phase pair verifies with every "
                     "gate PASS"},
    "g1-fail-amended: post-results edit to expectations is detected "
    "(protects: g1 via the immutability gate, same verify_prereg path)":
        {"tag": "F",
         "protects": "g1: compliant two-phase pair verifies with every "
                     "gate PASS"},
    "g1-fail-wrong-blob: results citing a different expectations blob are "
    "rejected (protects: g1 via the blob-match gate, same verify_prereg "
    "path)":
        {"tag": "F",
         "protects": "g1: compliant two-phase pair verifies with every "
                     "gate PASS"},
}

EXPECTATIONS_FIXTURE: dict[str, Any] = {
    "schema_version": "0.1",
    "prereg_id": "SELFTEST-PR-001",
    "question": "Does the trivial parity fixture return EVEN for input 4?",
    "declared_checks": [
        {
            "check_id": "parity-of-4",
            "statement": "parity(4)",
            "expected": "EVEN",
            "tag": "E",
        }
    ],
    "frozen_judgment_calls": [
        {"call_id": "zero-is-even", "ruling": "parity(0) counts as EVEN"}
    ],
    "rival_forecasts": [
        {"rival": "always-odd rival", "forecast": "parity(4) = ODD"}
    ],
    "stop_conditions": [
        "stop and report if parity raises instead of returning"
    ],
    "created": "2026-07-16",
}


def _sh(repo: Path, *args: str) -> str:
    code, out = git(repo, *args)
    if code != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {out}")
    return out


def _init_repo(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    _sh(root, "init", "-q")
    _sh(root, "config", "user.email", "prereg-selftest@local")
    _sh(root, "config", "user.name", "prereg-selftest")
    _sh(root, "config", "commit.gpgsign", "false")
    return root


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def _commit_file(repo: Path, relpath: str, message: str) -> str:
    _sh(repo, "add", "--", relpath)
    _sh(repo, "commit", "-q", "-m", message)
    return _sh(repo, "rev-parse", "HEAD")


def _results_fixture(exp_path: str, blob: str, commit: str) -> dict[str, Any]:
    return {
        "schema_version": "0.1",
        "prereg_ref": {
            "prereg_id": "SELFTEST-PR-001",
            "expectations_path": exp_path,
            "expectations_git_blob": blob,
            "expectations_commit": commit,
        },
        "observed": [
            {
                "check_id": "parity-of-4",
                "observed": "EVEN",
                "matches_expected": True,
            }
        ],
        "deviations": [],
        "created": "2026-07-16",
    }


def _build_good(repo: Path) -> tuple[str, str, str]:
    """Two-commit compliant pair; returns (exp_commit, blob, results_commit)."""
    _write_json(repo / "trivial.expectations.json", EXPECTATIONS_FIXTURE)
    exp_commit = _commit_file(
        repo,
        "trivial.expectations.json",
        "prereg: freeze expectations before any results exist",
    )
    blob = _sh(repo, "rev-parse", f"{exp_commit}:trivial.expectations.json")
    _write_json(
        repo / "trivial.results.json",
        _results_fixture("trivial.expectations.json", blob, exp_commit),
    )
    results_commit = _commit_file(
        repo,
        "trivial.results.json",
        "results: record observed outcomes against the frozen expectations",
    )
    return exp_commit, blob, results_commit


def selftest() -> int:
    results_log: list[tuple[str, bool, bool]] = []

    def check(name: str, value: bool, expected: bool = True) -> None:
        results_log.append((name, bool(value), expected))

    with tempfile.TemporaryDirectory(prefix="prereg-selftest-") as tmp:
        base = Path(tmp)

        # -- compliant scenario ------------------------------------------
        good_repo = _init_repo(base / "good")
        exp_commit, _, results_commit = _build_good(good_repo)
        check(
            "setup: selftest fixture repos build with distinct commits",
            bool(exp_commit) and bool(results_commit)
            and exp_commit != results_commit,
        )
        good = verify_prereg(good_repo, "trivial.results.json")
        check(
            "g1: compliant two-phase pair verifies with every gate PASS",
            good["valid"]
            and all(entry["status"] == "PASS" for entry in good["gates"]),
        )

        # -- control (i): expectations and results in ONE commit ---------
        joint_repo = _init_repo(base / "same_commit")
        _write_json(
            joint_repo / "trivial.expectations.json", EXPECTATIONS_FIXTURE
        )
        joint_blob = _sh(
            joint_repo, "hash-object", "--", "trivial.expectations.json"
        )
        _write_json(
            joint_repo / "trivial.results.json",
            _results_fixture("trivial.expectations.json", joint_blob, "HEAD"),
        )
        _sh(joint_repo, "add", "--", "trivial.expectations.json",
            "trivial.results.json")
        _sh(joint_repo, "commit", "-q", "-m",
            "cheat: expectations and results in one commit")
        joint = verify_prereg(joint_repo, "trivial.results.json")
        joint_failed = {
            entry["gate"] for entry in joint["gates"]
            if entry["status"] == "FAIL"
        }
        check(
            "g1-fail-same-commit: joint expectations+results commit is "
            "rejected (protects: g1 via the strict-ordering and separation "
            "gates, same verify_prereg path)",
            joint["valid"]
            or not (
                "P4 STRICT_ORDERING" in joint_failed
                and "P5 COMMIT_SEPARATION" in joint_failed
            ),
            expected=False,
        )

        # -- control (ii): expectations amended AFTER results ------------
        amended_repo = _init_repo(base / "amended")
        _build_good(amended_repo)
        doctored = dict(EXPECTATIONS_FIXTURE)
        doctored["declared_checks"] = [
            dict(EXPECTATIONS_FIXTURE["declared_checks"][0],
                 expected="ODD")
        ]
        _write_json(amended_repo / "trivial.expectations.json", doctored)
        _commit_file(
            amended_repo,
            "trivial.expectations.json",
            "cheat: quietly rewrite the expectations after the results",
        )
        amended = verify_prereg(amended_repo, "trivial.results.json")
        amended_failed = {
            entry["gate"] for entry in amended["gates"]
            if entry["status"] == "FAIL"
        }
        check(
            "g1-fail-amended: post-results edit to expectations is detected "
            "(protects: g1 via the immutability gate, same verify_prereg "
            "path)",
            amended["valid"]
            or "P6 EXPECTATIONS_IMMUTABLE" not in amended_failed,
            expected=False,
        )

        # -- control (iii): results reference a DIFFERENT blob -----------
        blob_repo = _init_repo(base / "wrong_blob")
        _write_json(blob_repo / "trivial.expectations.json",
                    EXPECTATIONS_FIXTURE)
        exp_commit_b = _commit_file(
            blob_repo,
            "trivial.expectations.json",
            "prereg: freeze expectations before any results exist",
        )
        doctored_b = dict(EXPECTATIONS_FIXTURE)
        doctored_b["declared_checks"] = [
            dict(EXPECTATIONS_FIXTURE["declared_checks"][0],
                 expected="ODD")
        ]
        _write_json(blob_repo / "doctored.expectations.json", doctored_b)
        wrong_blob = _sh(
            blob_repo, "hash-object", "--", "doctored.expectations.json"
        )
        (blob_repo / "doctored.expectations.json").unlink()
        _write_json(
            blob_repo / "trivial.results.json",
            _results_fixture(
                "trivial.expectations.json", wrong_blob, exp_commit_b
            ),
        )
        _commit_file(
            blob_repo,
            "trivial.results.json",
            "cheat: results claim they were tested against different "
            "expectations bytes",
        )
        wrong = verify_prereg(blob_repo, "trivial.results.json")
        wrong_failed = {
            entry["gate"] for entry in wrong["gates"]
            if entry["status"] == "FAIL"
        }
        check(
            "g1-fail-wrong-blob: results citing a different expectations "
            "blob are rejected (protects: g1 via the blob-match gate, same "
            "verify_prereg path)",
            wrong["valid"] or "P3 BLOB_MATCH" not in wrong_failed,
            expected=False,
        )

    failures = []
    print("PREREG VERIFY SELF-TEST")
    print("=" * 74)
    for name, value, expected in results_log:
        ok = value == expected
        print(f"{'PASS' if ok else 'UNEXPECTED'}  {name}: {value}")
        if not ok:
            failures.append(name)
    n_t = sum(1 for spec in CHECKS.values() if spec["tag"] == "T")
    n_e = sum(1 for spec in CHECKS.values() if spec["tag"] == "E")
    n_f = sum(1 for spec in CHECKS.values() if spec["tag"] == "F")
    print(
        f"\nEVIDENTIAL CHECKS (headline): {n_e} [E] + {n_f} [F] = {n_e + n_f}"
    )
    print(f"[T] theorem-consequence checks (no evidential weight): {n_t}")
    if failures:
        print("UNEXPECTED RESULTS:", failures)
        return 1
    print("All checks match expectations. Exit 0.")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    if len(args) != 2:
        print(__doc__)
        return 2
    repo = Path(args[0]).resolve()
    report = verify_prereg(repo, args[1])
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("valid") else 1


if __name__ == "__main__":
    sys.exit(main())

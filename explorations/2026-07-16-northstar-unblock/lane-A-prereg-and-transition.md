> Part of the 2026-07-16 north-star unblock swing. Exploration tier; the attached referee report GOVERNS (grades + corrections + firewall verdict). Firewalled lanes (B, C) were audited INDEPENDENT.

# Deliverable — Repairs 1a + 1b (two-phase preregistration mechanism; GU-001-GR-001 transition diagnosis)

Everything below was executed and receipted this session. Nothing was written to any repo; proposed paths are listed per section and collected at the end. Exploration tier throughout; no source claim moves; bar(b)/H59/Krein positivity/physical issuance stay OPEN; ADAPTER2-01 respected.

Scratchpad working copies (for the orchestrator to persist):

- `C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\38a54106-9cc3-428a-92e4-2bb753410f40\scratchpad\prereg_verify.py` (sha256 `6c0f11758fb1aa033f00674a342f63d7ab90d2c5ddcf7e2fe22ea2077ef429ed`)
- `C:\Users\joe\AppData\Local\Temp\claude\C--Users-joe-JB\38a54106-9cc3-428a-92e4-2bb753410f40\scratchpad\GU-001-TD-001-transition-diagnosis-v0.1.json` (sha256 `af06931a8ab010d8df70fcd8a638074e0fc684fa8447245c65e845b991c171ef`)
- Demo repo: `...\scratchpad\prereg-demo\` (temporary git repo; transcript embedded below)

---

## TASK 1 — Two-phase preregistration mechanism (prereg-verify v0.1)

### 1.1 Mechanism design (proposed: `interfaces/two-phase-preregistration-v0.1.md`)

```markdown
# Two-Phase Preregistration Convention v0.1

Status: provisional repo-owned process interface. It governs receiver-side
runs in this repository; it is not canon and confers no scientific pass.

## Why

Three referees across two swings independently flagged the same defect: the
receiver's expectations, judgment calls, and rival forecasts were not
mechanically provably frozen before outcomes were inspected. Rank 1's
FAVORS_CANDIDATE is conditional partly on exactly this; Ranks 2-4 are gated
on it alike. Prose claims of "preregistered" are not receipts. Git history
is.

## Construction

A preregistered run is TWO artifacts in TWO commits, hash-linked:

1. **EXPECTATIONS artifact** (`<run-id>.expectations.json`), committed in
   its own commit BEFORE any results exist. It carries:
   - `declared_checks`: every check the run will evaluate, each with a
     `check_id` and an `expected` value (the key is literally named
     "expected", per the swing-2 referee's EXPECTED_* naming demand — no
     result-shaped constant may be smuggled in under a neutral name);
   - `frozen_judgment_calls`: every discretionary construal ruled in
     advance (the class of un-preregistered discretion the Rank-1 referee
     enumerated: ownership construals, chain/branch ids, annotation
     choices, neutrality-artifact choices);
   - `rival_forecasts`: what each named rival predicts for the same checks;
   - `stop_conditions`: binding, non-vacuous stop rules (a constant-True
     detector is the burned cannot-fail class; it fails review).

2. **RESULTS artifact** (`<run-id>.results.json`), committed strictly
   afterward, carrying `prereg_ref` with the expectations file's path, its
   git BLOB id as committed, and its commit hash, plus per-check `observed`
   values and `deviations`.

Artifacts co-locate with the run they govern (spec lives with its
consumer), e.g. `explorations/<date>-<topic>/<run-id>.expectations.json`.

## Mechanical verification

`tests/prereg_verify.py` proves from git history alone (gates P1-P7):
results committed and parseable with a complete prereg_ref (P1); the
claimed expectations commit contains the expectations path (P2); the blob
at that commit equals the blob the results claim to have been tested
against (P3); the expectations commit is a STRICT ancestor of the
results-introducing commit — the same commit, or results-first, fails
(P4); the results commit does not touch the expectations path (P5);
exactly one commit in all of history touches the expectations path and the
HEAD blob still equals the registered blob — post-hoc edits, amends, and
deletions fail (P6); the expectations declare nonempty checks with
expected values, frozen judgment calls, rival forecasts, and stop
conditions (P7).

## Amendment policy

A committed expectations artifact is immutable. A revision gets a NEW file
and NEW prereg id, committed before the corresponding run; the superseded
artifact stays in history. Any other edit path is a P6 failure by design.

## Falsifiers (of the mechanism, not of any physics)

- A pair that violates temporal ordering verifies as valid.
- A post-hoc edit to a committed expectations artifact goes undetected.
- Results verified against different expectations bytes go undetected.
- History rewriting (rebase/force-push) can silently re-order the two
  commits: the verifier is sound relative to the integrity of the local
  history it reads. Pushing both commits promptly (this repo's
  commit+push default) and never force-pushing is the standing guard;
  cross-checking against the remote's reflog or a third-party timestamp
  is the escalation if that guard is ever in doubt.

## Nonclaims

- A prereg-verify PASS proves committed-order and byte identity only. It
  does not make the declared checks good science, the stop conditions
  adequate, or the observed values true.
- The mechanism does not retroactively upgrade any past run. The GU-001
  gate-run's partial ex-ante evidence (gates/evaluator committed ~17h
  before the source bundle; annotations A/B/C + pin committed before gate
  outcomes) remains historical evidence, not a two-phase receipt.
```

### 1.2 Verifier — `tests/prereg_verify.py` (full embedded source)

Pure Python stdlib + git subprocess. Registry-mode [T]/[E]/[F] tagging; every [F] exercises `verify_prereg` itself (the code path it protects); lints clean under `tests/tef_check_tag_linter.py --strict` (receipt in 1.3).

```python
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
```

### 1.3 [F]-control transcript + lint receipt (executed this session, Python 3.14.3)

`python prereg_verify.py --selftest` — all three demanded [F] controls fail through `verify_prereg` itself:

```
PREREG VERIFY SELF-TEST
==========================================================================
PASS  setup: selftest fixture repos build with distinct commits: True
PASS  g1: compliant two-phase pair verifies with every gate PASS: True
PASS  g1-fail-same-commit: joint expectations+results commit is rejected (protects: g1 via the strict-ordering and separation gates, same verify_prereg path): False
PASS  g1-fail-amended: post-results edit to expectations is detected (protects: g1 via the immutability gate, same verify_prereg path): False
PASS  g1-fail-wrong-blob: results citing a different expectations blob are rejected (protects: g1 via the blob-match gate, same verify_prereg path): False

EVIDENTIAL CHECKS (headline): 1 [E] + 3 [F] = 4
[T] theorem-consequence checks (no evidential weight): 1
All checks match expectations. Exit 0.
```
Exit code 0. Control coverage: (i) same-commit → `P4 STRICT_ORDERING` and `P5 COMMIT_SEPARATION` both FAIL, valid=false; (ii) post-results amendment → `P6 EXPECTATIONS_IMMUTABLE` FAIL, valid=false; (iii) different-blob reference → `P3 BLOB_MATCH` FAIL, valid=false. None is a cannot-fail control: each targets a distinct behavioral gate that the compliant scenario passes and the tampered scenario fails, in the same function.

`python tests/tef_check_tag_linter.py --strict prereg_verify.py`:

```json
{
  "convention": "registry",
  "total_checks": 5,
  "tag_counts": {"T": 1, "E": 1, "F": 3},
  "untagged_count": 0,
  "evidential_count_E_plus_F": 4,
  "T_checks_excluded_from_headline": 1,
  "violations": [],
  "advisories": []
}
```
Exit code 0 (strict).

### 1.4 Worked example — preregister-then-run in two real commits (mechanized receipt)

Executed in a temporary git repo at `scratchpad/prereg-demo`. Full transcript:

**Phase 1** — expectations committed alone (parity fixture: `expected: "EVEN"` for 4, `"ODD"` for 7; frozen judgment call "zero-is-even"; an always-odd rival forecast; a non-vacuous stop condition):

```
expectations commit: cdcb3d4693720650a6379feeaca09ae9a5ba534e
expectations blob:   93097f3e295192e5e3daccb91432bb6e4c06efd4
```

**Phase 2** — the fixture ran (`observed: ['EVEN', 'ODD']`), results committed separately, hash-linking blob `93097f3e...` at commit `cdcb3d46...`:

```
results commit:      a322cd83171e6703542283fbf82f92cf80e5e349
```

**Git history** (the temporal receipt itself):

```
a322cd83171e6703542283fbf82f92cf80e5e349 2026-07-16 08:33:37 -0500 results: parity fixture outcomes against frozen expectations DEMO-PR-001
    parity.results.json
cdcb3d4693720650a6379feeaca09ae9a5ba534e 2026-07-16 08:33:37 -0500 prereg: freeze parity expectations before any results exist
    parity.expectations.json
```

**Verifier run (compliant pair)** — `python prereg_verify.py <demo-repo> parity.results.json`, exit 0:

```
P1 RESULTS_COMMITTED       PASS  results introduced in commit a322cd83...
P2 EXPECTATIONS_AT_COMMIT  PASS  blob at cdcb3d46...:parity.expectations.json is 93097f3e...
P3 BLOB_MATCH              PASS  claimed 93097f3e... vs actual 93097f3e...
P4 STRICT_ORDERING         PASS  cdcb3d46... strictly precedes a322cd83...
P5 COMMIT_SEPARATION       PASS  results commit touches ['parity.results.json'] only
P6 EXPECTATIONS_IMMUTABLE  PASS  one commit touches expectations; HEAD blob == registered blob
P7 EXPECTATIONS_SHAPE      PASS  checks/judgment-calls/forecasts/stop-conditions all present
valid: true
```

**Live tamper** — a third commit ("innocuous-looking cleanup") quietly rewrote the frozen expectation EVEN→ODD; verifier re-run:

```
054af30 innocuous-looking cleanup
a322cd8 results: parity fixture outcomes against frozen expectations DEMO-PR-001
cdcb3d4 prereg: freeze parity expectations before any results exist

P1 PASS  P2 PASS  P3 PASS  P4 PASS  P5 PASS
P6 EXPECTATIONS_IMMUTABLE  FAIL
P7 PASS
valid: false — exit code 1
```

---

## TASK 2 — Transition diagnosis on GU-001-GR-001 (the skipped serialization step)

### 2.1 What the contract requires, and whether it could run

`interfaces/transition-diagnosis-v0.1.md` + `tests/classify_transition.py` require a receiver-owned witness record: per-branch qualified witnesses (value + evidence refs) over 14 fields, retained construction branches, a label-neutrality control, and normalization-frame / factorization-scope obligations. The contract exists and is preregistered in the relevant sense (committed with a 35-case adversarial suite long before GU-001 existed). It CAN run on this specimen — with one honest structural consequence: several witnesses for the capability-relevant transition do not exist yet, and the contract has first-class vocabulary for that (`UNKNOWN`), which is the diagnosis, not a failure to run.

The specimen supports two admissible receiver construals, both retained (Construction-Fork Rule, no selection):

- **witnessed-disclosure** — GU-001 as the event that actually occurred: W211 located and characterized the residual Z/2 datum inside the unchanged good-stable possibility family. Description changed; dynamics, records, access, control, task sets did not.
- **prospective-selection** — the residual as the not-yet-executed transition that supplying the external datum would constitute. Two witnesses are real at frozen grade (SAME family via W208 bistability; INEQUIVALENT representation via the capability gate's basis-invariant; NO settlement; NO_FACTOR_FOUND within the declared scope; reopenable YES). Everything operational is honestly UNKNOWN because bar(b)/H59/Krein positivity/physical issuance are OPEN and no normalization frame has been executed against this specimen.

Pre-run prediction (stated in-session before executing, visible in the session transcript — informal, NOT a two-phase receipt): witnessed-disclosure → `FIXED_FAMILY_DISCLOSURE`; prospective-selection → `UNKNOWN`; aggregate → `UNKNOWN`; label-invariant; exit 0. All four held.

### 2.2 The diagnosis record — proposed `packets/imports/GU-001/GU-001-TD-001-transition-diagnosis-v0.1.json`

Full content (sha256 `af06931a8ab010d8df70fcd8a638074e0fc684fa8447245c65e845b991c171ef`):

```json
{
  "schema_version": "0.1",
  "assessment_id": "GU-001-TD-001",
  "status": "provisional",
  "question": "In the possibility->dynamics->records->access->capability->finality vocabulary, what transition type does the GU-001 grading-sign specimen witness: the located-not-forced disclosure that actually occurred (W211 characterizing the residual Z/2 datum), and the prospective branch-selecting transition that supplying the external datum would constitute?",
  "construction": {
    "fork_identified": true,
    "selected_branch_id": null,
    "retention_statement": "Two admissible receiver construals are retained and neither is selected: (1) the witnessed-event construal, reading GU-001 as a description-level disclosure inside the fixed good-stable possibility family, and (2) the prospective-selection construal, reading the residual as a not-yet-executed transition whose witnesses do not exist while bar(b)/H59/Krein positivity/physical issuance are OPEN. Selecting between them would presuppose an answer to those OPEN questions; both stay live per the Construction-Fork Rule."
  },
  "branch_relation": "ALTERNATIVE_CONSTRUCTIONS",
  "branches": [
    {
      "branch_id": "witnessed-disclosure",
      "label": "GU-001 as the event that actually occurred: the residual located and characterized, nothing selected",
      "admissibility": "ADMISSIBLE",
      "witness": {
        "possibility_family_relation": {
          "value": "SAME",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/gate_results/2/status_reason (formation: one joint object over the unchanged good-stable structure; no family change)"
          ]
        },
        "representation_relation": {
          "value": "EQUIVALENT",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-grading-sign-barb-v0.2.json#/claim (located-not-forced: the disclosure alters no representation of GU's structure; both sign branches remain exactly as they were)"
          ]
        },
        "description_change": {
          "value": "YES",
          "evidence_refs": [
            "gu-formalization:explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md@d62a82f3 (sha256 0e1c213d2ab60d644113efc4b9b4fe884186761489ba320dc37834520b9928b6) - the residual Z/2 datum is newly located, typed, and characterized as Godel-independent"
          ]
        },
        "dynamics_change": {
          "value": "NO",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/gate_results/0 (provenance: the packet freezes existing source structure; no state trajectory, kernel, or law of the assessed structure changed)"
          ]
        },
        "persistent_record": {
          "value": "NO",
          "evidence_refs": [
            "receiver judgment J1 (frozen in the companion diagnosis record): the packet and W-series artifacts are meta-level documentation ABOUT the assessed GU structure, not a new object-level record inside it; conflating the two would collapse the records/description distinction the contract exists to police"
          ]
        },
        "access_change": {
          "value": "NO",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-import-record-2026-07-16.md (the import changes receiver-side holdings only; no conditioning, reachability, observability, or control relation of the assessed structure changed)"
          ]
        },
        "control_change": {
          "value": "NO",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/neutrality_control (NO_BRANCH_SELECTED: the receiver exercises no control over the source structure and selects nothing)"
          ]
        },
        "raw_task_set_relation": {
          "value": "EQUAL",
          "evidence_refs": [
            "receiver judgment J2 (identity frame, frozen in the companion diagnosis record): a description-level event leaves the operational task set of the assessed structure unchanged by construction"
          ]
        },
        "normalized_task_set_relation": {
          "value": "EQUAL",
          "evidence_refs": [
            "receiver judgment J2 (identity frame, normalized reading): with description, representation, resources, access, and control held fixed, both task sets are the pre-disclosure sets"
          ]
        },
        "irreversible": {
          "value": "NO",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/reopening_conditions (a source revision of GU-001 requires re-import and a fresh run; descriptions are revisable)"
          ]
        },
        "settlement": {
          "value": "NO",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/neutrality_control/verdict_before (NO_BRANCH_SELECTED: the disclosure settles nothing; the sign remains unselected)"
          ]
        },
        "preceding_layer_factorization": {
          "value": "NOT_APPLICABLE",
          "evidence_refs": [
            "no settlement is claimed for the disclosure event, so factorization of a settlement through preceding layers does not arise for this branch"
          ]
        },
        "reopenable_by_admissible_continuation": {
          "value": "YES",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/reopening_conditions/4 (source revision reopens; the disclosure is an admissibly continuable description)"
          ]
        },
        "ordering_relation": {
          "value": "ORDER_COMPATIBLE",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/gate_results (the serialized eight-gate run ordered this event's witnesses without cycles or unrepresentable relations)"
          ]
        }
      },
      "normalization_frame": "Identity frame (receiver judgment J2): the disclosure event changes receiver-side description only; description, representation, resources, access, and control of the assessed GU good-stable structure are held fixed by construction, so the raw and normalized task sets are both the unchanged pre-disclosure sets.",
      "factorization_search_scope": null,
      "declared_claims": ["FIXED_FAMILY_DISCLOSURE"],
      "evidence_grade": "EXPLORATORY",
      "verification": "UNVERIFIED"
    },
    {
      "branch_id": "prospective-selection",
      "label": "the residual as a not-yet-executed transition: what supplying the external Z/2 datum would be",
      "admissibility": "ADMISSIBLE",
      "witness": {
        "possibility_family_relation": {
          "value": "SAME",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-IA-001-receiving-independence-v0.2.json#/source_wording/exact_independence_scope (W208 bistability: the sign is TRUE in the good model and FALSE in the pathological model of the SAME self-consistency theory)"
          ]
        },
        "representation_relation": {
          "value": "INEQUIVALENT",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/gate_results/4/status_reason (capability gate: definiteness of the physical inner product on the record-count block is basis-invariant; the branch difference survives admissible reformulation and is not a relabeling)"
          ]
        },
        "description_change": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "no source-issued witness exists for an executed selection event; the selection has not occurred (NO_BRANCH_SELECTED throughout GU-001-GR-001)"
          ]
        },
        "dynamics_change": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/gate_results/4/nonclaims (the loop-unitarity cash-out rests on STRUCTURAL/ARGUED lifts; whether a selection changes record-sector dynamics is exactly the OPEN bar(b) question)"
          ]
        },
        "persistent_record": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "no witness: whether a selection event would form a new persistent, discriminable record is part of the OPEN physical-issuance question"
          ]
        },
        "access_change": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "no witness: no source has specified an access relation for a selection event on this specimen"
          ]
        },
        "control_change": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "no witness: which process would supply the external Z/2 datum is owned at the typed GU/TI/TaF joint seam and is OPEN per ADAPTER2-01 (six-condition reopen burden untouched)"
          ]
        },
        "raw_task_set_relation": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "no executed task-set comparison exists for the two branches; Rank-2 receiver preparation is synthetic-toy grade only (explorations/2026-07-16-decisive-tests/SYNTHESIS.md, Rank 2 row)"
          ]
        },
        "normalized_task_set_relation": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "no independently defended normalization frame has been executed against this specimen; supplying one is exactly the missing Rank-2 input (source-issued paired cases + independent Frame R)"
          ]
        },
        "irreversible": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "no witness: reversibility of a selection event is part of the OPEN issuance question"
          ]
        },
        "settlement": {
          "value": "NO",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/neutrality_control (verdict NO_BRANCH_SELECTED before and after the exact label swap: nothing has settled)"
          ]
        },
        "preceding_layer_factorization": {
          "value": "NO_FACTOR_FOUND",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/gate_results/3/status_reason (completion-null: each of the five method registers is a completion attempt in a different register and all leave the bit free; declared refinements enlarge, never absorb, the residual, dim 2 -> 4)"
          ]
        },
        "reopenable_by_admissible_continuation": {
          "value": "YES",
          "evidence_refs": [
            "packets/imports/GU-001/GU-001-GR-001-gate-run-v0.1.json#/reopening_conditions (the unbuilt interacting C-operator and nonlocal Z_U completions could absorb the residual; the ADAPTER2-01 reopen burden could change what the seam may assert)"
          ]
        },
        "ordering_relation": {
          "value": "UNKNOWN",
          "evidence_refs": [
            "no witness: where a selection event would sit relative to record/access/capability changes is unspecified while issuance is OPEN"
          ]
        }
      },
      "normalization_frame": null,
      "factorization_search_scope": "GU-001's declared completion family at the frozen pin only: the five method registers (W206 counterfactual-invariance, W207 Dirac-BRST cohomology, W208 Lawvere fixed point, W209 topos internal logic, W210 Helmholtz inverse-variational) plus the packet's /alternatives refinements. Explicitly outside the search: the unbuilt interacting C-operator, the nonlocal Z_U completion, kappa, and any TaF-side supply of the datum.",
      "declared_claims": [],
      "evidence_grade": "EXPLORATORY",
      "verification": "UNVERIFIED"
    }
  ],
  "label_neutrality": {
    "left_label": "C_good / record-count mode Krein-NEGATIVE (eta_+ positive-definite)",
    "right_label": "C_path / record-count mode Krein-POSITIVE (indefinite total metric)",
    "required": true
  },
  "assumptions": [
    "The frozen GU-001 packet, GU-001-IA-001, and GU-001-GR-001 supply the only admissible witnesses; the classifier does not establish their truth or sufficiency.",
    "The receiver's meta-level/object-level record distinction (judgment call J1) and identity normalization frame (J2) are admissible receiver construals; both are disclosed as un-preregistered discretion in the companion diagnosis record.",
    "ADAPTER2-01 governs all TaF-identifying wording; no cross-repository identity is asserted anywhere in this record."
  ],
  "evidence_grade": "EXPLORATORY",
  "tests": [
    "python tests/classify_transition.py packets/imports/GU-001/GU-001-TD-001-transition-diagnosis-v0.1.json (this record)",
    "python tests/validate_transition_diagnosis_contract.py (contract regression)"
  ],
  "falsifiers": [
    "A pure branch or endpoint relabeling changes the computed diagnosis.",
    "A frozen source artifact witnesses an executed selection event, making the prospective branch's UNKNOWN values dishonest rather than conservative.",
    "An independently defended normalization frame executed against this specimen returns a non-UNKNOWN normalized task-set relation, superseding the prospective branch's abstention.",
    "The witnessed-disclosure branch's persistent_record = NO is defeated by showing the packet artifacts are object-level records of the assessed structure rather than meta-level documentation about it."
  ],
  "nonclaims": [
    "This diagnosis establishes no physics, selects no branch, and promotes no source claim; bar(b), H59, Krein positivity, and physical issuance remain OPEN.",
    "The aggregate outcome is a receiver diagnosis of supplied witnesses, not evidence against the candidate hierarchy or for any rival.",
    "FIXED_FAMILY_DISCLOSURE for the witnessed event does not diminish the capability gate's branch-inequivalence result, which concerns the prospective transition, not the disclosure.",
    "This record was not itself preregistered under the two-phase mechanism; it cannot support a non-provisional Rank-1 update by itself."
  ],
  "reopening_conditions": [
    "A source-issued witness for an executed selection event arrives; re-run the diagnosis with real witnesses.",
    "A Rank-2-grade normalization frame is independently defended and executed against this specimen.",
    "Per the contract's own reopening clause, this first real frozen-packet classification triggers review of transition-diagnosis v0.1.",
    "A preregistered (two-phase) re-run of this diagnosis supersedes this record."
  ]
}
```

### 2.3 Receipts (executed this session)

`python tests/classify_transition.py <record>` — exit code **0**:

```json
{
  "aggregate_outcome": "UNKNOWN",
  "assessment_id": "GU-001-TD-001",
  "branch_relation": "ALTERNATIVE_CONSTRUCTIONS",
  "branch_results": [
    {"branch_id": "witnessed-disclosure", "outcome": "FIXED_FAMILY_DISCLOSURE",
     "components": ["FIXED_FAMILY_DISCLOSURE"], "alerts": [], "rejected_declared_claims": []},
    {"branch_id": "prospective-selection", "outcome": "UNKNOWN",
     "components": [], "alerts": [], "rejected_declared_claims": []}
  ],
  "label_invariance": {"tested": true, "invariant": true,
                       "outcome_before": "UNKNOWN", "outcome_after": "UNKNOWN"},
  "errors": [],
  "valid": true
}
```

`python tests/validate_transition_diagnosis_contract.py` (regression) — `PASS: 44/44 Transition Diagnosis v0.1 groups; 35 synthetic cases; 16 aggregate outcomes`, exit code **0**.

### 2.4 Companion record — proposed `packets/imports/GU-001/GU-001-TD-001-diagnosis-record-2026-07-16.md`

```markdown
---
artifact_type: transition_diagnosis_record
assessment_id: GU-001-TD-001
packet_id: GU-001
status: provisional
created: 2026-07-16
constitutional: false
---

# GU-001-TD-001 transition diagnosis record (receiver-owned)

The skipped Rank-1 serialization step (validate packet -> assess -> run
gates -> DIAGNOSE TRANSITION -> update rivals), caught by the Rank-1
referee, now executed. Record: `GU-001-TD-001-transition-diagnosis-v0.1.json`
(sha256 af06931a8ab010d8df70fcd8a638074e0fc684fa8447245c65e845b991c171ef).

## Result

`classify_transition.py`: valid true, label-invariant, exit 0.
- Branch `witnessed-disclosure` -> **FIXED_FAMILY_DISCLOSURE**: what GU-001
  itself witnessed is a description-level event — the residual Z/2 datum
  located, typed, and characterized inside the unchanged good-stable
  possibility family. This is the contract vocabulary's exact rendering of
  Located-Is-Not-Forced.
- Branch `prospective-selection` -> **UNKNOWN**: the capability-relevant
  transition (supplying the external datum) has not occurred; its
  operational witnesses do not exist while bar(b)/H59/Krein positivity/
  physical issuance are OPEN. Real at frozen grade: SAME family (W208
  bistability), INEQUIVALENT representation (basis-invariant
  definite/indefinite split), settlement NO, NO_FACTOR_FOUND scoped to the
  declared completion family, reopenable YES.
- Aggregate -> **UNKNOWN** (fork retained, ALTERNATIVE_CONSTRUCTIONS,
  driven by the prospective branch; no forced verdict).

## Frozen judgment calls (un-preregistered discretion, disclosed)

- J1: packet/W-series artifacts are meta-level documentation, not
  object-level records of the assessed structure (else the diagnosis
  would spuriously read RECORD_FORMATION).
- J2: identity normalization frame for the disclosure branch (a
  description-only event leaves both task sets fixed by construction).
- J3: the two-construal fork itself (witnessed vs prospective).
These are exactly the class of calls the two-phase preregistration
mechanism exists to freeze; a preregistered re-run supersedes this record.

## Missing inputs for a stronger diagnosis (exact gaps)

1. No source-issued witness for an executed selection event (the
   transition is prospective; NO_BRANCH_SELECTED stands).
2. No independently defended normalization frame executed against this
   specimen (Rank-2 gap: source-issued paired cases + independent Frame R).
3. No settlement witness, hence no admissible FINALITY_CANDIDATE test; the
   NO_FACTOR_FOUND witness is scoped to GU-001's declared completions only.

## What this does and does not change about Rank 1

- CLEARS: the skipped-serialization defect. The transition-diagnosis step
  has now run against the founding specimen with a contract-valid,
  label-invariant result, and its outcome is CONSISTENT with the gate run
  (settles nothing, selects nothing, keeps the capability question at the
  prospective/OPEN layer).
- DOES NOT CHANGE: Rank 1's referee-corrected receiver update. It remains
  FAVORS_CANDIDATE, conditional and scoped to the interface-formation
  discrimination only. Discharge remains BLOCKED at prerequisite (v):
  this diagnosis was itself not preregistered under the two-phase
  mechanism (an in-session prediction of all four outcomes preceded the
  run and held, but that is not a committed-expectations receipt), so no
  non-provisional Rank-1 update issues from it.
- TRIGGERS: transition-diagnosis v0.1's own reopening clause ("after the
  first real frozen-packet classification") — contract review is now due
  as a named follow-up.

## Nonclaims

No physics, no branch selection, no source-claim promotion, no debit
cleared; bar(b), H59, Krein positivity, physical issuance OPEN; ADAPTER2-01
untouched.
```

---

## Proposed repo paths (for the orchestrator to persist; no repo writes made here)

| deliverable | proposed path |
|---|---|
| convention/interface doc (1.1) | `interfaces/two-phase-preregistration-v0.1.md` |
| verifier (1.2) | `tests/prereg_verify.py` (copy from scratchpad; sha256 `6c0f1175...`) |
| tests/README addition | new "Two-phase preregistration" section: `python tests/prereg_verify.py --selftest` and `python tests/prereg_verify.py <repo_root> <results_path>` |
| diagnosis record JSON (2.2) | `packets/imports/GU-001/GU-001-TD-001-transition-diagnosis-v0.1.json` (copy from scratchpad; sha256 `af06931a...`) |
| companion diagnosis record (2.4) | `packets/imports/GU-001/GU-001-TD-001-diagnosis-record-2026-07-16.md` |
| import-record update (diff) | `packets/imports/GU-001/GU-001-import-record-2026-07-16.md`, "Companion receiver artifacts" table — add row: `| transition diagnosis | GU-001-TD-001 | aggregate UNKNOWN (fork retained: FIXED_FAMILY_DISCLOSURE / UNKNOWN), classify_transition valid, label-invariant, exit 0; file sha256 af06931a8ab010d8df70fcd8a638074e0fc684fa8447245c65e845b991c171ef |` |
| progress-lanes update (diff) | `explorations/2026-07-16-progress-lanes.md` line 73-75: mark (1a) and (1b) EXECUTED 2026-07-16 with pointers to the two artifacts above; (1c) remains the open next-in-lane |

Check-discipline summary: verifier selftest = 1 [T] + 1 [E] + 3 [F], every [F] exercises `verify_prereg` (the checker it protects) and each targets a distinct gate the compliant case passes; no cannot-fail controls (the live-tamper demo shows a formerly-passing repo flipping to exit 1); `tef_check_tag_linter.py --strict` exit 0, zero violations, zero advisories; all executable claims above carry embedded source plus captured output; no source-repo claim moved; bar(b)/H59/Krein positivity/physical issuance remain OPEN.

---

# ATTACHED ADVERSARIAL REFEREE REPORT (governs)

# Referee Report — Lane A (prereg mechanism + GU-001 transition diagnosis)

## 1. VERDICT: SOUND-WITH-CORRECTIONS

Independently re-executed before grading, all reproducing the report: scratchpad sha256s match exactly (`6c0f1175…`, `af06931a…`); `prereg_verify.py --selftest` → 5/5, exit 0, all three [F] controls fail through `verify_prereg` at the claimed gates; repo `tests/tef_check_tag_linter.py --strict` → 0 violations/advisories, exit 0; repo `tests/classify_transition.py` on the TD record → valid true, aggregate UNKNOWN, branches FIXED_FAMILY_DISCLOSURE / UNKNOWN, exit 0; `validate_transition_diagnosis_contract.py` → 44/44, exit 0; demo-repo history matches the transcript (commits `cdcb3d4` → `a322cd8` → tamper `054af30`) and the post-tamper verifier run fails exactly at P6, valid false. Evidence-ref pointer audit: `gate_results/0,2,3,4`, `neutrality_control`, `reopening_conditions/4` all resolve to the cited content. No ADAPTER2-01 contradiction (no cross-repo identity asserted; withdrawn identity stays withdrawn). No source claim moves; bar(b)/H59/Krein positivity/issuance held OPEN throughout; no state-level finality language; no north-star inversion.

But two adversarial probes the report never ran punch mechanical holes in the verifier, and the mechanism's headline billing exceeds what P1–P7 prove.

## 2. Defects

**D1 — MAJOR (mechanism billed above what it proves).** The interface doc's "Why" claims the mechanism makes expectations "mechanically provably frozen **before outcomes were inspected**," and P4's billing says "committed BEFORE any results exist." P1–P7 prove only that expectations were committed before results were **committed**. The verifier cannot detect the run-first cheat: execute privately, inspect outcomes, author matching "expectations," commit them, then commit results — every gate passes. The program's prerequisite (v) wording is "before gate outcomes are inspected"; commit order is necessary, not sufficient, for that. The nonclaims ("committed-order and byte identity only") gesture at this but neither the falsifiers nor the nonclaims name the private-early-run gap, while the "Why" paragraph asserts the stronger reading. This is the claims-above-evidence pattern applied to the very mechanism shipped to end it.
*Corrected wording:* "The mechanism proves freeze-before-**publication**, not freeze-before-**observation**. A PASS is necessary but not sufficient for prerequisite (v); the residual trust assumption (no private pre-inspection before the expectations commit) must be discharged separately — the gold standard remains committing receiver machinery before the evaluated inputs exist at all, as in the GU-001 gates-before-bundle history, which prereg-verify records but cannot certify." Add "expectations authored after a private run verify as valid" to the falsifiers/nonclaims.

**D2 — MODERATE (results artifact has no immutability gate; probe-confirmed).** Referee probe: build the compliant pair, then commit a doctored `trivial.results.json` at HEAD (observed EVEN→ODD) — `verify_prereg` returns **valid = true**, all seven gates PASS; `results_amended_after_introduction` is set but is informational and non-binding. The expectations file gets P6; the results file gets nothing: a reader consuming HEAD sees doctored observed values under a PASS verifier. The interface doc's falsifier list covers expectations tampering only, so this hole is undeclared.
*Correction:* add P8 RESULTS_IMMUTABLE (exactly one commit touches the results path and HEAD bytes equal the introducing bytes), or make the amended flag fail validity; add the results-tamper direction to falsifiers and to the [F] suite.

**D3 — MODERATE (empty results verify; probe-confirmed).** A results artifact containing **only** a well-formed `prereg_ref` — no `observed`, no `deviations` — passes all gates (probe: valid = true). The convention text requires "per-check `observed` values and `deviations`"; the verifier enforces none of it, so it certifies pairs the convention itself calls incomplete, including a results file that silently omits declared checks.
*Correction:* shape-gate the results (nonempty `observed`; observed `check_id`s a subset of, and ideally covering, `declared_checks`).

**D4 — MODERATE (receiver gloss dressed as source content on a load-bearing witness).** The witnessed-disclosure branch's `representation_relation: EQUIVALENT` — one of the three fields that jointly generate FIXED_FAMILY_DISCLOSURE — cites `GU-001-grading-sign-barb-v0.2.json#/claim` with the gloss "the disclosure alters no representation of GU's structure; both sign branches remain exactly as they were." The packet's actual claim contains no such sentence (it says LOCATED but NOT FORCED; "bar(b) does not self-clear"). The gloss is receiver inference presented under a source path — the false-corroboration class the R1 referee burned (its D2). Same pattern, milder, on `dynamics_change` (gate_results/0 gloss). The true support is a fourth un-preregistered judgment call.
*Corrected wording:* own it as "receiver judgment J4: the disclosure event is representation-neutral; supported by, not stated in, the packet's located-not-forced claim," add J4 to the companion record's frozen-judgment-call list, and in every evidence_ref separate quoted artifact content from receiver gloss.

**D5 — MODERATE ("frozen" self-description with no freeze).** J1/J2 evidence_refs say "frozen in the companion diagnosis record." Nothing is frozen: the companion record is same-session, uncommitted, proposed-only — while the same deliverable's Task 1 doctrine is "Prose claims of 'preregistered' are not receipts. Git history is."
*Corrected wording:* "disclosed in the companion diagnosis record (same-session; not committed; not a freeze)."

**D6 — MODERATE (mechanism not applied to Task 2 though available; unmechanized process claim cited as evidence).** The demo repo and verifier were working before Task 2 ran; committing the four-outcome prediction as an expectations artifact in that scratch repo would have cost one commit. Instead the lane offers "stated in-session before executing, visible in the session transcript … All four held" — an unverifiable, unmechanized process claim of exactly the class this swing exists to end, in the document that ships the ender. Disclosure ("informal, NOT a two-phase receipt") is honest; **citing it as held evidence** is not.
*Correction:* strike the "all four held" evidential framing; the informal prediction carries zero weight and should appear only as a disclosed limitation.

**D7 — MINOR (cannot-fail prediction item).** "Label-invariant" is structurally guaranteed: `classify_branch` never reads `label` or `label_neutrality`, so the evaluator's swap cannot change the semantic summary for any valid record — the invariance branch is unreachable-false. Predicting it is a cannot-fail control; and "exit 0" is entailed by the other predictions. Of the "four held," only the two branch outcomes bore risk. The contract discloses this weakness ("syntactic metamorphic control"); the lane's prediction framing doesn't.

**D8 — MINOR (authority misattribution).** "Per the **swing-2** referee's EXPECTED_* naming demand" (interface doc and verifier docstring): the demand is from the decisive-tests swing's **lane-R2** referee (`explorations/2026-07-16-decisive-tests/lane-R2-access-capability-pilot.md:661`), not the 2026-07-16-swing-2 referee. Cite precisely; this repo's standard treats authority-citation drift as first-class (R1 referee D1/D2).

**D9 — MINOR ("CLEARS" overstates).** "CLEARS: the skipped-serialization defect" — the historical violation (rival update issued before diagnosis) stands as record; running the step afterward executes it out of order and discharges repair item 1 for future updates only, at un-preregistered grade.
*Corrected wording:* "EXECUTES the skipped step (out of original order; the recorded violation stands as history); repair item 1 discharged at un-preregistered receiver grade; a preregistered re-run supersedes." The proposed progress-lanes diff should likewise mark (1b) "built and demoed; adoption + D1–D3 corrections pending," not bare EXECUTED.

## 3. What the deliverable actually earns

- **Task 1 (repair 1b):** the named repair as the synthesis literally specified it — "expectations commit before results commit" — is genuinely built, with real [F] controls (all re-run, all fail through the protected code path; no cannot-fail control **in the selftest**) and a working live-tamper demo. With D1's narrowed billing and D2/D3's gates added, it earns adoption as a provisional repo process interface. Conditionality: a prereg-verify PASS is **necessary, not sufficient**, for prerequisite (v); it can never by itself convert a run into "preregistered before outcomes were inspected."
- **Task 2 (repair 1a):** the skipped serialization step is now executed against the founding specimen with a contract-valid result. The **prospective-selection → UNKNOWN** branch is robust (built from real frozen witnesses plus honest UNKNOWNs; no fiat). The **witnessed-disclosure → FIXED_FAMILY_DISCLOSURE** branch is conditional on un-preregistered receiver judgments **J1, J2, and J4** (D4) surviving a preregistered re-run — three of its load-bearing NO/EQUAL/EQUIVALENT values are receiver discretion, exactly the class the Task-1 mechanism exists to freeze. Aggregate **UNKNOWN**, fork retained, is the defensible headline.
- **Receiver update (program vocabulary):** none new. Rank 1 remains **FAVORS_CANDIDATE, conditional and scoped to the interface-formation discrimination only; Rank-1 discharge remains BLOCKED at prerequisite (v)** — now with repair item 1 executed (un-preregistered grade) and repair item 2 built (corrections D1–D3 pending). The diagnosis is consistent with the gate run and adds no strength to the conditional update; the record's own nonclaim to this effect is correct and survives.
- The lane correctly claims no debit cleared, no physics, no branch selection, no source promotion.

## 4. Stop-condition compliance

**Respected, with the two disclosed-but-corrected gaps.** (a) No repo writes; artifacts staged in scratchpad with hashes — verified present and matching. (b) No packet substitution; no rewriting of the preflight or GR-001 into a pass; FAVORS_CANDIDATE kept conditional; discharge kept BLOCKED — the D1-corrected (R1 referee) vocabulary is used correctly throughout. (c) Serialization: the out-of-order execution of the diagnose-transition step is inherent to repairing a past skip and is honestly recorded, but must be worded per D9 — executed, not "cleared." (d) The non-vacuous stop-condition rule is honored in the mechanism (P7 requires nonempty stop conditions; the burned constant-True class is named) — though note P7 checks nonemptiness, not non-vacuity, so a constant-True stop condition would still verify: fold into the D1 corrected nonclaims ("does not make the stop conditions adequate" already covers it). (e) ADAPTER2-01, source sovereignty, OPEN questions: all respected. The lane fails its own Task-1 standard once (D6) and its verifier leaks twice (D2, D3); none flips direction, so SOUND-WITH-CORRECTIONS rather than SOUND.

Key files: `C:/Users/joe/AppData/Local/Temp/claude/C--Users-joe-JB/38a54106-9cc3-428a-92e4-2bb753410f40/scratchpad/prereg_verify.py`, `.../GU-001-TD-001-transition-diagnosis-v0.1.json`, `.../prereg-demo/`; repo: `tests/classify_transition.py` (label swap provably inert: lines 392–399 vs 250–339), `packets/imports/GU-001/GU-001-grading-sign-barb-v0.2.json` (`/claim` lacks the D4 gloss), `explorations/2026-07-16-decisive-tests/lane-R2-access-capability-pilot.md:661` (D8), `explorations/2026-07-16-decisive-tests/lane-R1-rank1-adjudication.md` (governing corrected update).
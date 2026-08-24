#!/usr/bin/env python3
"""Run the already-frozen A109-H19 full-atlas shards.

This tool does not create or alter predictions. Each rank 415..430 is attempted
with a 55-second wall-clock limit. A timeout is repeated once with the same
command. Ranks that time out twice are recorded as unresolved under full atlas;
no fallback certificate is generated automatically.
"""
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PR = ROOT / "preregistrations" / "a107_a109" / "A109_H19_PREREGISTRATION.json"
EXPECTED = "abe35d929e8a35b9db9fbad96ad375152e854d65e25df33ce70781d411709d5d"
RUNNER = ROOT / "audits" / "a109_gamma_plus_holdout_runner.py"
OUTDIR = ROOT / "results" / "a107_a109" / "h19" / "full_atlas"
LOGDIR = ROOT / "results" / "a107_a109" / "h19" / "logs"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    if sha(PR) != EXPECTED:
        raise RuntimeError("H19 preregistration hash mismatch")
    OUTDIR.mkdir(parents=True, exist_ok=True)
    LOGDIR.mkdir(parents=True, exist_ok=True)
    manifest = {"audit": "A109_H19_FULL_ATLAS_EXECUTION_MANIFEST", "preregistration_sha256": EXPECTED, "ranks": {}}
    for rank in range(415, 431):
        row = {"attempts": []}
        out = OUTDIR / f"A109_H19_R{rank}_RESULT.json"
        for attempt in (1, 2):
            cmd = [
                sys.executable, str(RUNNER),
                "--preregistration", str(PR),
                "--expected-sha256", EXPECTED,
                "--start", str(rank), "--end", str(rank),
                "--output", str(out),
            ]
            try:
                cp = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=55)
                status = "completed" if cp.returncode == 0 else "failed"
                (LOGDIR / f"R{rank}_attempt{attempt}.stdout.log").write_text(cp.stdout, encoding="utf-8")
                (LOGDIR / f"R{rank}_attempt{attempt}.stderr.log").write_text(cp.stderr, encoding="utf-8")
                row["attempts"].append({"attempt": attempt, "status": status, "returncode": cp.returncode})
                if cp.returncode == 0:
                    break
                # A non-timeout computation failure is not silently retried as a mathematical result.
                break
            except subprocess.TimeoutExpired as exc:
                (LOGDIR / f"R{rank}_attempt{attempt}.stdout.log").write_text(exc.stdout or "", encoding="utf-8")
                (LOGDIR / f"R{rank}_attempt{attempt}.stderr.log").write_text(exc.stderr or "", encoding="utf-8")
                row["attempts"].append({"attempt": attempt, "status": "timeout", "wall_clock_seconds": 55})
        row["full_atlas_result_exists"] = out.exists()
        manifest["ranks"][str(rank)] = row
        (ROOT / "results" / "a107_a109" / "h19" / "A109_H19_EXECUTION_MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()

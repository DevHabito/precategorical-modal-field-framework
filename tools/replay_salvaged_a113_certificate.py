#!/usr/bin/env python3
"""Replay the exact CRC-verified A113 script salvaged from an invalid ZIP.

The recovered Python source is run byte-for-byte in an ephemeral CI runner,
not edited to fit a result. The historical archive remains invalid. A
successful replay confirms executable finite rational gates, not the
logical sufficiency of every bound used to claim a continuum theorem.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from inspect_truncated_zip_members import ARCHIVES, inspect


EXPECTED_SOURCE_NAME = "a113_tail_global_compressed_one_variation_certificate.py"
EXPECTED_SOURCE_SHA256 = (
    "46e1fec5197c7253e29156e592e2320905cd993caa66f3f5b9cd109471b11587"
)
OUTPUT_NAME = "A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_CERTIFICATE_20260911.json"
DECLARED_CHECK_COUNT = 23


def main() -> int:
    archived_path = Path(ARCHIVES[1])
    audit, recovered = inspect(archived_path)
    if audit["fully_recovered"] is not False:
        raise AssertionError("The invalid container must remain classified incomplete.")

    source = recovered.get(EXPECTED_SOURCE_NAME)
    if source is None:
        raise AssertionError("A113 original Python member did not pass CRC.")
    digest = hashlib.sha256(source).hexdigest()
    if digest != EXPECTED_SOURCE_SHA256:
        raise AssertionError("The recovered A113 script differs from audited bytes.")

    # The historical script writes its result to /mnt/data. The GitHub
    # workflow creates that location on its disposable runner. No bytes
    # are copied back into historical archives or committed to main.
    result_file = Path("/mnt/data") / OUTPUT_NAME
    if not result_file.parent.is_dir():
        raise RuntimeError("The disposable /mnt/data output directory is absent.")
    if result_file.exists():
        raise RuntimeError("Expected an empty result path before replay.")

    with tempfile.TemporaryDirectory(prefix="a113-salvage-check-") as work:
        original_script = Path(work) / EXPECTED_SOURCE_NAME
        original_script.write_bytes(source)
        finished = subprocess.run(
            [sys.executable, "-I", str(original_script)],
            cwd=work,
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        if finished.returncode != 0:
            print(finished.stdout)
            print(finished.stderr, file=sys.stderr)
            raise AssertionError(f"Archived script exited with {finished.returncode}.")

    artifact = json.loads(result_file.read_text(encoding="utf-8"))
    checks = artifact.get("checks")
    if artifact.get("verdict") != "PASS":
        raise AssertionError("Recovered A113 source did not reproduce PASS.")
    if not isinstance(checks, dict) or len(checks) != DECLARED_CHECK_COUNT:
        raise AssertionError("Unexpected original certificate gate count.")
    if any(value is not True for value in checks.values()):
        raise AssertionError("Some original exact-rational gates failed.")

    names = (
        "small_left_core_lower",
        "middle_left_margin",
        "right_remote_margin",
        "central_J_margin",
    )
    exact = {}
    for key in names:
        value = Fraction(artifact["bounds"][key])
        if value <= 0:
            raise AssertionError(f"Nonpositive reported rational bound: {key}")
        exact[key] = str(value)

    print(json.dumps({
        "audit": "CRC_RECOVERED_ORIGINAL_A113_SCRIPT_REPLAY",
        "status": "PASS",
        "source_sha256": digest,
        "historical_archive_valid": False,
        "original_exact_gate_count": len(checks),
        "passed": sum(value is True for value in checks.values()),
        "all_exact_bounds_strictly_positive": True,
        "signed_margins_exact": exact,
        "scope": (
            "Verifies execution of the CRC-verified source and its declared "
            "rational gates; does NOT independently prove that all analytic "
            "majorants rigorously bound the original E_k on the continuum."
        ),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Read-only structural and CRC audit for every tracked ZIP archive.

A SHA-256 match proves byte identity, not that a historical ZIP is complete.
The archive inventory is obtained from Git's tracked-file index. No archive
is extracted, repaired, replaced, or used to execute code.
"""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import zipfile


MAX_ENTRY_BYTES = 20 * 1024 * 1024
MAX_ARCHIVE_BYTES = 100 * 1024 * 1024


def tracked_zip_paths() -> list[Path]:
    output = subprocess.run(
        ["git", "ls-files", "--cached", "-z"],
        check=True,
        stdout=subprocess.PIPE,
    ).stdout
    entries = [
        Path(path.decode("utf-8", errors="surrogateescape"))
        for path in output.split(b"\0")
        if path
    ]
    return sorted(path for path in entries if path.suffix.lower() == ".zip")


def audit_archive(path: Path) -> dict[str, object]:
    result: dict[str, object] = {
        "path": path.as_posix(),
        "bytes": path.stat().st_size if path.is_file() else None,
        "status": "FAIL",
    }
    try:
        with zipfile.ZipFile(path, "r", allowZip64=True) as archive:
            entries = archive.infolist()
            if not entries:
                raise ValueError("Archive contains no central-directory entries.")

            total_uncompressed = sum(entry.file_size for entry in entries)
            if total_uncompressed > MAX_ARCHIVE_BYTES:
                raise ValueError("Uncompressed archive size exceeds audit cap.")

            names: set[str] = set()
            for entry in entries:
                if entry.file_size > MAX_ENTRY_BYTES:
                    raise ValueError(f"Entry exceeds audit size cap: {entry.filename}")
                name = PurePosixPath(entry.filename.replace("\\", "/"))
                if name.is_absolute() or ".." in name.parts:
                    raise ValueError(f"Unsafe archive member path: {entry.filename}")
                if entry.filename in names:
                    raise ValueError(f"Duplicate central-directory name: {entry.filename}")
                names.add(entry.filename)

            # Decompress to an internal bounded buffer for CRC integrity only.
            # zipfile.testzip does not extract or execute archive contents.
            corrupt = archive.testzip()
            if corrupt is not None:
                raise ValueError(f"CRC/decompression failed for member: {corrupt}")

            result.update(
                status="PASS",
                entries=len(entries),
                uncompressed_bytes=total_uncompressed,
            )
    except (
        zipfile.BadZipFile,
        zipfile.LargeZipFile,
        OSError,
        RuntimeError,
        EOFError,
        ValueError,
    ) as error:
        result["error"] = f"{type(error).__name__}: {error}"
    return result


def main() -> int:
    paths = tracked_zip_paths()
    if not paths:
        print(json.dumps({"status": "FAIL", "error": "No tracked ZIP archives found."}))
        return 1

    outcomes = [audit_archive(path) for path in paths]
    failures = [item for item in outcomes if item["status"] != "PASS"]
    report = {
        "audit": "TRACKED_ZIP_STRUCTURAL_AND_CRC_INTEGRITY",
        "archive_count": len(outcomes),
        "passed": len(outcomes) - len(failures),
        "failed": len(failures),
        "status": "PASS" if not failures else "FAIL",
        "archives": outcomes,
        "interpretation": (
            "ZIP structural/CRC checks are independent of root SHA-256 "
            "indexes; archive errors invalidate reproducibility packages."
        ),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Check or rebuild canonical Git-tracked SHA-256 indexes.

The indexes exclude themselves to avoid circular hashing. Historical
package-level manifests are deliberately outside this tool's scope.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import subprocess
import sys
import tempfile
from pathlib import Path

INDEX_PATHS = frozenset({"MANIFEST.csv", "SHA256SUMS.txt"})


def tracked_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--cached", "-z"],
        check=True,
        capture_output=True,
    )
    names = [os.fsdecode(name) for name in result.stdout.split(b"\0") if name]
    return sorted(name for name in names if name not in INDEX_PATHS)


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_indexes(root: Path) -> tuple[str, str, int]:
    manifest = io.StringIO(newline="")
    writer = csv.writer(manifest, lineterminator="\n")
    writer.writerow(("path", "bytes", "sha256"))
    checksums = []
    paths = tracked_files(root)

    for relative_path in paths:
        path = root / relative_path
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Missing or non-regular tracked file: {relative_path}")
        checksum = hash_file(path)
        writer.writerow((relative_path, path.stat().st_size, checksum))
        checksums.append(f"{checksum}  {relative_path}\n")

    return manifest.getvalue(), "".join(checksums), len(paths)


def write_atomic(path: Path, content: str) -> None:
    descriptor, temporary_path = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_path, path)
    finally:
        if os.path.exists(temporary_path):
            os.unlink(temporary_path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail on any index drift")
    mode.add_argument("--write", action="store_true", help="Regenerate both indexes")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    manifest, checksum_list, file_count = build_indexes(root)
    desired = {"MANIFEST.csv": manifest, "SHA256SUMS.txt": checksum_list}

    if args.check:
        mismatched = [
            name for name, content in desired.items()
            if not (root / name).is_file()
            or (root / name).read_bytes() != content.encode("utf-8")
        ]
        if mismatched:
            print(
                f"Integrity index drift: {', '.join(mismatched)}. "
                "Review the working tree before using --write.",
                file=sys.stderr,
            )
            return 1
        print(f"Integrity indexes match {file_count} Git-tracked regular files.")
        return 0

    for name, content in desired.items():
        write_atomic(root / name, content)
    print(f"Regenerated integrity indexes for {file_count} Git-tracked regular files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

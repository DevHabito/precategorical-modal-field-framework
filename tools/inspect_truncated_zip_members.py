#!/usr/bin/env python3
"""Read-only local-header inspection of incomplete historical ZIP bundles.

This tool deliberately does not use ZipFile, because the repository's
three malformed archives lack a readable central directory. It scans
local headers sequentially, validates raw DEFLATE/STORE member sizes and
CRC-32s, and reports recoverable bytes. Nothing is extracted or executed.

A valid member is *not* a certification of the missing archive, a
historical theorem, or a complete reproducibility bundle.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import struct
import sys
import zlib


ARCHIVES = (
    "MFRP_Informational_Requirements_A39-A109/research_updates/"
    "A110_A112/archives/A112_TAIL_CLOSURE_WORKING_SET_20260911.zip",
    "MFRP_Informational_Requirements_A39-A109/research_updates/"
    "A113/archives/A113_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip",
    "MFRP_Informational_Requirements_A39-A109/research_updates/"
    "A114/archives/A114A_FULL_REPRODUCIBILITY_PACKAGE_20260912.zip",
)
LOCAL_SIGNATURE = bytes((80, 75, 3, 4))
HEADER = struct.Struct("<IHHHHHIIIHH")
MEMBER_CAP = 5 * 1024 * 1024


def inspect(path: Path) -> tuple[dict[str, object], dict[str, bytes]]:
    data = path.read_bytes()
    position = 0
    members: list[dict[str, object]] = []
    validated: dict[str, bytes] = {}
    stops: list[str] = []

    while position + HEADER.size <= len(data):
        if data[position:position + 4] != LOCAL_SIGNATURE:
            stops.append("Expected next local file header but found non-header bytes.")
            break

        (
            _, _, flags, method, _, _, expected_crc, compressed_size,
            uncompressed_size, filename_bytes, extra_bytes,
        ) = HEADER.unpack_from(data, position)

        header_end = position + HEADER.size + filename_bytes + extra_bytes
        if header_end > len(data):
            stops.append(f"Truncated member name or extra fields at byte {position}.")
            break

        name_bytes = data[position + HEADER.size:position + HEADER.size + filename_bytes]
        filename = name_bytes.decode("utf-8", errors="replace")
        record: dict[str, object] = {
            "filename": filename,
            "local_header_offset": position,
            "method": method,
            "declared_compressed_bytes": compressed_size,
            "declared_uncompressed_bytes": uncompressed_size,
            "status": "INCOMPLETE",
        }
        members.append(record)

        if flags & 0x0008:
            stops.append(f"Data descriptor unsupported for {filename}; stop safely.")
            break
        if flags & 0x0001:
            stops.append(f"Encrypted member unsupported: {filename}.")
            break
        if uncompressed_size > MEMBER_CAP:
            stops.append(f"Member exceeds bounded inspection cap: {filename}.")
            break

        member_end = header_end + compressed_size
        if member_end > len(data):
            record["status"] = "TRUNCATED_COMPRESSED_STREAM"
            record["bytes_available"] = len(data) - header_end
            stops.append(f"Compressed data truncated at {filename}.")
            break

        raw = data[header_end:member_end]
        try:
            if method == 0:
                output = raw
            elif method == 8:
                inflater = zlib.decompressobj(-zlib.MAX_WBITS)
                output = inflater.decompress(raw, MEMBER_CAP + 1)
                output += inflater.flush()
                if not inflater.eof or inflater.unused_data:
                    raise ValueError("Incomplete or overlong raw DEFLATE stream.")
            else:
                raise ValueError(f"Unsupported compression method: {method}")

            if len(output) != uncompressed_size:
                raise ValueError("Decompressed size does not match local header.")
            actual_crc = zlib.crc32(output) & 0xFFFFFFFF
            if actual_crc != expected_crc:
                raise ValueError("CRC-32 does not match the declared local header.")

            record.update(
                status="RECOVERABLE_CRC_VERIFIED",
                sha256=hashlib.sha256(output).hexdigest(),
                crc32=f"{actual_crc:08x}",
            )
            validated[filename] = output
        except (zlib.error, ValueError, OverflowError) as exc:
            record["status"] = "FAILED_MEMBER_VALIDATION"
            record["error"] = str(exc)
            stops.append(f"Decompression/CRC failure at {filename}.")
            break

        position = member_end

    return (
        {
            "archive": path.as_posix(),
            "stored_bytes": len(data),
            "recovered_member_count": len(validated),
            "members": members,
            "scan_stop_offset": position,
            "unaccounted_bytes": len(data) - position,
            "stops": stops,
            "fully_recovered": False,
            "scope": "Local-header member salvage only; original ZIP remains invalid.",
        },
        validated,
    )


def main() -> int:
    results: list[dict[str, object]] = []
    for archived_name in ARCHIVES:
        path = Path(archived_name)
        if not path.is_file():
            raise FileNotFoundError(path)

        metadata, recovered = inspect(path)
        results.append(metadata)
        for name, payload in recovered.items():
            if name.endswith(".json") and "A112G_BRANCH_REGULARITY" in name:
                parsed = json.loads(payload.decode("utf-8"))
                print("=== BEGIN RECOVERED A112G JSON (CRC VERIFIED MEMBER ONLY) ===")
                print(json.dumps(parsed, indent=2, ensure_ascii=False))
                print("=== END RECOVERED A112G JSON ===")
            if name.endswith(".py") and (
                "a113_tail_global_compressed_one_variation_certificate" in name
                or "a114a_" in name.lower()
            ):
                print(f"=== BEGIN RECOVERED SCRIPT: {name} ===")
                print(payload.decode("utf-8"))
                print(f"=== END RECOVERED SCRIPT: {name} ===")

    print("=== BEGIN LOCAL-HEADER RECOVERY INVENTORY ===")
    print(json.dumps({
        "archive_count": len(results),
        "archives": results,
        "interpretation": "Members passing DEFLATE and CRC are salvageable only; no archive is restored.",
    }, indent=2, ensure_ascii=False))
    print("=== END LOCAL-HEADER RECOVERY INVENTORY ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())

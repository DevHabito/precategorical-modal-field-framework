#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "a92_continuum_offset_three_window_results.json"
OUTPUT = ROOT / "figures" / "a92_continuum_offset_three_windows.png"


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    windows = []
    for item in data["full_positive_windows"]:
        windows.append({
            "maximum": item["maximum"],
            "lower": 0.129,
            "upper": float(item["upper_boundary_midpoint_decimal"]),
            "kind": "full-positive",
        })
    for item in data["root_windows"]:
        windows.append({
            "maximum": item["maximum"],
            "lower": float(item["root_midpoint_decimal"]),
            "upper": float(item["upper_boundary_midpoint_decimal"]),
            "kind": "root-to-boundary",
        })
    windows.sort(key=lambda item: item["maximum"])

    figure, axis = plt.subplots(figsize=(9.2, 7.2))
    for index, item in enumerate(windows):
        axis.plot(
            [item["lower"], item["upper"]],
            [index, index],
            linewidth=3,
        )
        axis.scatter([item["lower"], item["upper"]], [index, index], s=18)

    axis.axvline(0.129, linewidth=1, linestyle="--")
    axis.set_yticks(range(len(windows)))
    axis.set_yticklabels([str(item["maximum"]) for item in windows])
    axis.set_xlabel("Probe parameter s")
    axis.set_ylabel("Support maximum M")
    axis.set_title("A92 certified local offset-three windows")
    axis.grid(axis="x", alpha=0.25)
    figure.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT, dpi=220)
    plt.close(figure)
    print(OUTPUT)


if __name__ == "__main__":
    main()

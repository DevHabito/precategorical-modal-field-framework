#!/usr/bin/env python3
"""Generate the A80 exact local compression-window atlas figure."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "a80_local_compression_window_atlas_results.json"
OUTPUT = ROOT / "figures" / "a80_local_compression_window_atlas.png"


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    windows = data["window_results"]
    s0 = float(Fraction(data["contract"]["s0"]))

    figure, axis = plt.subplots(figsize=(9.2, 6.2))
    for item in windows:
        maximum = item["maximum"]
        lower = float(item["open_window"]["lower_root"]["midpoint_decimal"])
        upper = float(item["open_window"]["upper_root"]["midpoint_decimal"])
        axis.plot([lower, upper], [maximum, maximum], linewidth=3)
        axis.plot([lower, upper], [maximum, maximum], marker="|", linestyle="None")

    axis.axvline(s0, linestyle="--", linewidth=1.3, label=r"$s_0=131/1000$")
    axis.set_xlabel(r"First-anchor coordinate $s=2^{-\alpha}$")
    axis.set_ylabel(r"Support maximum $M$")
    axis.set_title("A80 — Exact local gamma-inactive compression windows")
    axis.grid(True, alpha=0.3)
    axis.legend()
    figure.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT, dpi=220)
    plt.close(figure)
    print(OUTPUT)


if __name__ == "__main__":
    main()

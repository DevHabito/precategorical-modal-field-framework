#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "results" / "a93_continuum_global_one_variation_catalogue.json"
OUTPUT = ROOT / "figures" / "a93_global_offset_three_windows.png"


def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    windows = data["windows"]

    full = [w for w in windows if w["a92_classification"] == "positive"]
    roots = [w for w in windows if w["a92_classification"] == "single_increasing_root"]

    fig, ax = plt.subplots(figsize=(10, 7))

    for index, group in enumerate((full, roots)):
        label = "Global offset-three on full cell" if index == 0 else "Global transition to offset three"
        first = True
        for item in group:
            maximum = item["maximum"]
            lower = float(F(item["outer_hull"][0]))
            upper = float(F(item["outer_hull"][1]))
            if item["a92_classification"] == "single_increasing_root":
                lower = float(F(item["phase_statement"]["root_upper"]))
            ax.hlines(maximum, lower, upper, linewidth=2.2, linestyles="solid" if index == 0 else "dashed", label=label if first else None)
            if item["a92_classification"] == "single_increasing_root":
                root_mid = float(
                    (F(item["phase_statement"]["root_lower"]) + F(item["phase_statement"]["root_upper"])) / 2
                )
                ax.scatter([root_mid], [maximum], marker="x", zorder=3)
            first = False

    ax.set_xlabel("probe parameter s")
    ax.set_ylabel("support maximum M")
    ax.set_title("A93 exact global offset-three windows")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best")
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

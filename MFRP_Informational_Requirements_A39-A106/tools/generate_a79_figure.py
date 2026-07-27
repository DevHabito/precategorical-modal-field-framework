#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "a79_compression_interval_results.json"
OUTPUT = ROOT / "figures" / "a79_exact_compression_intervals.png"


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    rows = data["support_results"]
    s0 = float(data["contract"]["s0"].split("/")[0]) / float(
        data["contract"]["s0"].split("/")[1]
    )

    plt.figure(figsize=(10, 6))
    for index, row in enumerate(rows):
        lower = float(
            row["strict_KKT_component_containing_s0"]["s_lower_root"][
                "midpoint_decimal"
            ]
        )
        upper = float(
            row["strict_KKT_component_containing_s0"]["s_upper_root"][
                "midpoint_decimal"
            ]
        )
        y = len(rows) - index
        plt.plot([lower, upper], [y, y], linewidth=5)
        plt.scatter([lower, upper], [y, y], marker="|")
        plt.scatter([s0], [y], marker="o")
        plt.text(upper + 0.000015, y, f"M={row['maximum']}", va="center")

    plt.axvline(s0, linestyle="--", label=r"probe $s_0=131/1000$")
    plt.yticks([])
    plt.xlabel(r"first-anchor coordinate $s=2^{-\alpha}$")
    plt.title("A79 — Exact gamma-inactive compression intervals")
    plt.legend()
    plt.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT, dpi=180)
    plt.close()
    print(OUTPUT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "a101_gamma_active_interval_and_residual_closure_results.json"
OUT = ROOT / "figures" / "a101_gamma_active_interval_and_residual_closure.png"


def frac(value: str) -> float:
    return float(Fraction(value))


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    interval = data["M443_interval_theorem"]
    lower = sum(frac(value) for value in interval["lower_root_bracket"]) / 2
    upper = sum(frac(value) for value in interval["upper_root_bracket"]) / 2
    reference = 0.13

    atlas = data["final_residual_atlas"]
    supports = [item[0] for item in atlas["pass_keys"]]
    closure = data["A95_obstruction_closure_accounting"]
    architecture_counts = [
        closure["A97_endpoint_released_strict_pass_count"],
        closure["A98_A99_q0q1_gamma_inactive_resolution_count"],
        closure["A100_A101_q0q1_gamma_active_resolution_count"],
    ]
    labels = ["endpoint released", "q0/q1, γ inactive", "q0/q1, γ− active"]

    figure, axes = plt.subplots(2, 1, figsize=(9.5, 7.2), constrained_layout=True)

    axis = axes[0]
    axis.axhline(0, linewidth=1)
    axis.plot([0.129, 0.133], [0, 0], linewidth=3, alpha=0.25)
    axis.plot([lower, upper], [0, 0], linewidth=10)
    axis.scatter([lower, reference, upper], [0, 0, 0], zorder=3)
    axis.text(lower, 0.06, "active γ− dual = 0", ha="center", fontsize=9)
    axis.text(reference, -0.08, "s = 13/100", ha="center", fontsize=9)
    axis.text(upper, 0.06, "p77 mass = 0", ha="center", fontsize=9)
    axis.set_xlim(0.129, 0.133)
    axis.set_ylim(-0.16, 0.16)
    axis.set_yticks([])
    axis.set_xlabel("probe s")
    axis.set_title("A101 exact strict-KKT component at M=443")

    axis = axes[1]
    positions = list(range(len(labels)))
    bars = axis.bar(positions, architecture_counts)
    axis.set_xticks(positions, labels)
    axis.set_ylabel("resolved A95 obstruction witnesses")
    axis.set_ylim(0, max(architecture_counts) * 1.18)
    axis.set_title("Exact pointwise closure of all 83 A95 lift obstructions")
    for bar, count in zip(bars, architecture_counts):
        axis.text(bar.get_x() + bar.get_width() / 2, count + 1, str(count), ha="center")
    axis.text(
        0.99,
        0.93,
        "Final γ-active passes: M=" + ", ".join(str(value) for value in supports),
        transform=axis.transAxes,
        ha="right",
        va="top",
        fontsize=9,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUT, dpi=180)
    print(OUT)


if __name__ == "__main__":
    main()

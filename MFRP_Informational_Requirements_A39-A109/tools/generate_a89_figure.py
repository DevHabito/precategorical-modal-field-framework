#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "a89_uniform_secant_threshold_results.json"
OUTPUT = ROOT / "figures" / "a89_uniform_secant_threshold_budget.png"


def value(item: dict[str, str]) -> float:
    return float(F(item["fraction"]))


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    budget = data["proof_budget"]

    positive = value(budget["positive_probe_target_lower"])
    beta = value(budget["negative_beta_target_upper"])
    target = F(1, 200)
    residual = F(1, 1_000_000)
    margin = F(data["certificate_specific_threshold_transition"]["M521_rounded_margin"])

    labels = [
        "Probe-target\nlower bound",
        "Beta-target\nupper cost",
        "Target-affine\nupper cost",
        "Residual\nupper cost",
        "Certified\nmargin",
    ]
    values = [positive, -beta, -float(target), -float(residual), float(margin)]

    figure, axis = plt.subplots(figsize=(9.2, 5.4))
    bars = axis.bar(labels, values)
    axis.axhline(0, linewidth=1)
    axis.set_ylabel("Normalized secant budget")
    axis.set_title("A89 uniform positivity certificate for all M ≥ 521")
    axis.text(
        0.02,
        0.96,
        "Valid for every real s ∈ [0.129, 0.133] under the declared reduced contract",
        transform=axis.transAxes,
        va="top",
    )

    for bar, current in zip(bars, values):
        vertical = current + (0.00035 if current >= 0 else -0.00035)
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            vertical,
            f"{current:.9f}",
            ha="center",
            va="bottom" if current >= 0 else "top",
            fontsize=9,
        )

    figure.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT, dpi=200)
    plt.close(figure)
    print(OUTPUT)


if __name__ == "__main__":
    main()

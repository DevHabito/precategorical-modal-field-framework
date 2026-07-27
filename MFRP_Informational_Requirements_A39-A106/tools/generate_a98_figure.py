#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "a98_full_lp_active_set_resolution_results.json"
OUTPUT = ROOT / "figures" / "a98_unrestricted_full_lp_active_set.png"


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    solution = data["exact_solution"]
    p = solution["original_P_probabilities_decimal"]
    q = solution["original_Q_probabilities_decimal"]
    labels = [f"P({x})" for x in data["resolved_active_set"]["P_support"]] + [
        f"Q({x})" for x in data["resolved_active_set"]["Q_support"]
    ]
    values = [float(p[str(x)]) for x in data["resolved_active_set"]["P_support"]] + [
        float(q[str(x)]) for x in data["resolved_active_set"]["Q_support"]
    ]

    fig, ax = plt.subplots(figsize=(10, 5.8))
    ax.bar(labels, values)
    ax.set_yscale("log")
    ax.set_ylabel("Probability mass (log scale)")
    ax.set_title("A98 exact unrestricted optimum at M=396, s=13/100")
    ax.grid(axis="y", alpha=0.25)
    ax.text(
        0.02,
        0.03,
        "P={70,396}; Q={0,1,198,199}; active bands: alpha+, beta-; gamma inactive",
        transform=ax.transAxes,
        fontsize=9,
    )
    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "a100_full_lp_active_set_resolution_results.json"
OUTPUT = ROOT / "figures" / "a100_unrestricted_full_lp_active_set.png"


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    p = {int(k): float(v) for k, v in data["exact_solution"]["original_P_probabilities_decimal"].items()}
    q = {int(k): float(v) for k, v in data["exact_solution"]["original_Q_probabilities_decimal"].items()}

    fig, ax = plt.subplots(figsize=(10, 5.8))
    p_x = list(p)
    p_y = [p[x] for x in p_x]
    q_x = list(q)
    q_y = [q[x] for x in q_x]
    ax.scatter(p_x, p_y, marker="o", s=85, label="P support")
    ax.scatter(q_x, q_y, marker="s", s=75, label="Q support")
    for x, y in zip(p_x, p_y):
        ax.vlines(x, 0, y, linewidth=1.2)
        ax.annotate(f"P({x})", (x, y), xytext=(5, 7), textcoords="offset points", fontsize=8)
    for x, y in zip(q_x, q_y):
        ax.vlines(x, 0, y, linewidth=1.2, linestyles="dashed")
        ax.annotate(f"Q({x})", (x, y), xytext=(5, -13), textcoords="offset points", fontsize=8)
    ax.set_title("A100 exact unrestricted active set at M=443, s=13/100")
    ax.set_xlabel("Support atom x")
    ax.set_ylabel("Probability mass")
    ax.set_xlim(-8, 452)
    ax.set_ylim(-0.025, 0.66)
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

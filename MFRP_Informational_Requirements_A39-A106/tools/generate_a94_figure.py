#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "a94_all_cell_continuum_one_variation_results.json"
CATALOGUE = ROOT / "results" / "a94_all_cell_continuum_one_variation_catalogue.json"
OUTPUT = ROOT / "figures" / "a94_all_cell_global_phase_atlas.png"


def main() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    catalogue = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    cells = catalogue["cells"]

    phase_order = [
        "unique_b_plus_1",
        "unique_b_plus_2",
        "b_plus_1_to_b_plus_2",
        "b_plus_2_to_b_plus_1",
        "unique_b_plus_3",
        "b_plus_2_to_b_plus_3",
    ]
    labels = {
        "unique_b_plus_1": "unique b+1",
        "unique_b_plus_2": "unique b+2",
        "b_plus_1_to_b_plus_2": "b+1 to b+2",
        "b_plus_2_to_b_plus_1": "b+2 to b+1",
        "unique_b_plus_3": "unique b+3",
        "b_plus_2_to_b_plus_3": "b+2 to b+3",
    }
    markers = ["o", "s", "^", "X", "D", "v"]

    fig, ax = plt.subplots(figsize=(11, 7))
    for phase, marker in zip(phase_order, markers):
        group = [cell for cell in cells if cell["phase_classification"] == phase]
        ax.scatter(
            [cell["maximum"] for cell in group],
            [cell["base_contact"] for cell in group],
            marker=marker,
            s=28,
            label=f"{labels[phase]} ({len(group)})",
        )

    ax.set_xlabel("support maximum M")
    ax.set_ylabel("algebraic base contact b")
    ax.set_title(
        "A94 exact continuum global phase atlas\n"
        f"{result['summary']['cell_count']} cells; "
        f"{result['summary']['simple_adjacent_global_transition_cell_count']} transition cells"
    )
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best", fontsize=9)
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

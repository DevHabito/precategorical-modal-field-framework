#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "results" / "a91_four_term_offset_three_catalogue.json"
OUTPUT = ROOT / "figures" / "a91_offset_three_screen_and_exact_cases.png"


def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    screened = data["parity_predictor_offset_three_screen"]
    true_cases = [item for item in screened if item["true_offset"] == 3]
    false_cases = [item for item in screened if item["true_offset"] != 3]

    probe_labels = {
        item["probe_index"]: item["probe"]
        for item in screened
    }

    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    ax.scatter(
        [item["maximum"] for item in false_cases],
        [item["probe_index"] for item in false_cases],
        marker="x",
        s=45,
        linewidths=1.1,
        label="parity-locator screen: false positive",
    )
    ax.scatter(
        [item["maximum"] for item in true_cases],
        [item["probe_index"] for item in true_cases],
        marker="D",
        s=58,
        linewidths=1.2,
        label="exact four-term offset-three case",
    )

    ax.set_xlabel("Support maximum M")
    ax.set_ylabel("Rational probe s")
    ax.set_yticks(sorted(probe_labels))
    ax.set_yticklabels([probe_labels[index] for index in sorted(probe_labels)])
    ax.set_title("A91: parity screen versus exact four-term offset-three classifier")
    ax.grid(True, linewidth=0.4, alpha=0.5)
    ax.legend(loc="upper left")
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

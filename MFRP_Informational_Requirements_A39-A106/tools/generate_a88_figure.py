#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "results" / "a88_nine_term_secant_positivity_catalogue.json"
OUTPUT = ROOT / "figures" / "a88_exact_local_secant_base_contacts.png"


def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    grouped: dict[str, list[tuple[int, int]]] = defaultdict(list)
    labels: dict[str, str] = {}
    for record in data["records"]:
        name = record["probe_name"]
        grouped[name].append((int(record["maximum"]), int(record["base_contact"])))
        labels[name] = record["probe_value"]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    for name in sorted(grouped):
        points = sorted(grouped[name])
        ax.plot(
            [point[0] for point in points],
            [point[1] for point in points],
            linewidth=1.0,
            label=f"s={labels[name]}",
        )
    ax.set_xlabel("Support maximum M")
    ax.set_ylabel("Exact base contact b = ceil(M c(s))")
    ax.set_title("A88 exact local-secant base contacts on nine rational probes")
    ax.grid(True, alpha=0.25)
    ax.legend(ncol=3, fontsize=7)
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

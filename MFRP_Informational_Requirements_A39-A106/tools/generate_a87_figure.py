#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "a87_exact_secant_offset_classifier_catalogue.json"
OUTPUT = ROOT / "figures" / "a87_exact_secant_offset_classifier.png"


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    records = data["records"]
    probes = ("local_lower", "probe", "local_upper")
    markers = ("o", "s", "^")

    fig, ax = plt.subplots(figsize=(11, 6.5))
    for probe, marker in zip(probes, markers):
        subset = [record for record in records if record["probe_name"] == probe]
        ax.scatter(
            [record["maximum"] for record in subset],
            [float(record["full_tau_decimal"]) for record in subset],
            s=18,
            alpha=0.72,
            marker=marker,
            label=probe.replace("_", " "),
        )

    ax.axhline(0, linewidth=1.2)
    ax.axhline(1, linewidth=1.2)
    ax.text(302, -0.02, "offset 0 / 1", va="top", ha="right", fontsize=9)
    ax.text(302, 0.98, "offset 1 / 2", va="top", ha="right", fontsize=9)
    ax.set_xlim(8, 302)
    ax.set_ylim(-0.8, 1.1)
    ax.set_xlabel("Support maximum M")
    ax.set_ylabel("Exact secant residual tau (decimal display)")
    ax.set_title("A87 exact secant-residual offset classifier")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="lower right")
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

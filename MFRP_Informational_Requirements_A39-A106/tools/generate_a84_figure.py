#!/usr/bin/env python3
"""Generate the A84 exact-probe contact-selection figure."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
RESULT = ROOT / "results" / "a84_k_space_exponential_polynomial_stress_results.json"
OUTPUT = ROOT / "figures" / "a84_exact_probe_contact_scaling.png"


def main() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    records = data["support_records"]
    maxima = [int(item["maximum"]) for item in records]

    plt.figure(figsize=(10, 6))
    for key, label in (
        ("local_lower", "s = 129/1000"),
        ("probe", "s = 131/1000"),
        ("local_upper", "s = 133/1000"),
    ):
        contacts = [int(item["maximizing_contact"][key]) for item in records]
        plt.plot(maxima, contacts, label=label, linewidth=1.4)

    plt.xlabel("Support maximum M")
    plt.ylabel("Unique compressed maximizing contact k")
    plt.title("A84: exact contact selection at three rational probes")
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUTPUT, dpi=180)
    plt.close()
    print(OUTPUT)


if __name__ == "__main__":
    main()

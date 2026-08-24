#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"


def main() -> None:
    a84 = json.loads(
        (RESULTS / "a84_k_space_exponential_polynomial_stress_results.json").read_text(
            encoding="utf-8"
        )
    )
    a85 = json.loads(
        (RESULTS / "a85_parity_dominant_balance_contact_localization_results.json").read_text(
            encoding="utf-8"
        )
    )

    support_records = a84["support_records"]
    parameter_map = {
        record["probe_name"]: record
        for record in a85["high_precision_asymptotic_diagnostic"]["probe_parameters"]
    }
    labels = {
        "local_lower": "s = 0.129",
        "probe": "s = 0.131",
        "local_upper": "s = 0.133",
    }

    fig, axes = plt.subplots(2, 1, figsize=(10, 9), sharex=True)

    for probe_name in ("local_lower", "probe", "local_upper"):
        maxima = [int(record["maximum"]) for record in support_records]
        ratios = [
            int(record["maximizing_contact"][probe_name]) / int(record["maximum"])
            for record in support_records
        ]
        slope = float(parameter_map[probe_name]["slope"])
        axes[0].plot(maxima, ratios, linewidth=1.1, label=labels[probe_name])
        axes[0].axhline(slope, linewidth=0.9, linestyle="--")

        errors = []
        error_M = []
        even_offset = float(parameter_map[probe_name]["even_offset"])
        odd_offset = float(parameter_map[probe_name]["odd_offset"])
        for record in support_records:
            maximum = int(record["maximum"])
            if maximum < 13:
                continue
            selected = int(record["maximizing_contact"][probe_name])
            offset = even_offset if maximum % 2 == 0 else odd_offset
            predicted = slope * maximum + offset
            error_M.append(maximum)
            errors.append(selected - predicted)
        axes[1].plot(error_M, errors, linewidth=1.1, label=labels[probe_name])

    axes[0].set_ylabel(r"Exact compressed maximizer $k^*/M$")
    axes[0].set_title("A85 parity-resolved asymptotic contact localization")
    axes[0].grid(True, alpha=0.25)
    axes[0].legend()

    axes[1].axhline(1.0, linewidth=0.8, linestyle="--")
    axes[1].axhline(-1.0, linewidth=0.8, linestyle="--")
    axes[1].set_xlabel("Support maximum M")
    axes[1].set_ylabel(r"$k^*-[c(s)M+d_p(s)]$")
    axes[1].grid(True, alpha=0.25)
    axes[1].legend()

    fig.tight_layout()
    FIGURES.mkdir(parents=True, exist_ok=True)
    out = FIGURES / "a85_parity_asymptotic_contact_localization.png"
    fig.savefig(out, dpi=180)
    plt.close(fig)
    print(out)


if __name__ == "__main__":
    main()

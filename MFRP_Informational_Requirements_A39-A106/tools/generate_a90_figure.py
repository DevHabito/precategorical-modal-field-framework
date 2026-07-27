#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "results" / "a90_prethreshold_contact_sequence_catalogue.json"
OUTPUT = ROOT / "figures" / "a90_exact_prethreshold_contact_offsets.png"


def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    records = data["records"]
    maxima = sorted({item["maximum"] for item in records})
    probes = sorted({item["probe_index"] for item in records})
    matrix = np.zeros((len(probes), len(maxima)), dtype=int)
    m_index = {maximum: index for index, maximum in enumerate(maxima)}
    labels: dict[int, str] = {}
    for item in records:
        matrix[item["probe_index"], m_index[item["maximum"]]] = item["ceil_offset"]
        labels[item["probe_index"]] = item["probe"]

    fig, ax = plt.subplots(figsize=(12, 6.5))
    image = ax.imshow(
        matrix,
        aspect="auto",
        origin="lower",
        interpolation="nearest",
        extent=[maxima[0] - 0.5, maxima[-1] + 0.5, -0.5, len(probes) - 0.5],
        vmin=0,
        vmax=3,
    )
    colorbar = fig.colorbar(image, ax=ax, ticks=[0, 1, 2, 3])
    colorbar.set_label(r"Exact offset $k^* - \lceil M c(s) \rceil$")

    offset_three = [item for item in records if item["ceil_offset"] == 3]
    ax.scatter(
        [item["maximum"] for item in offset_three],
        [item["probe_index"] for item in offset_three],
        marker="x",
        s=55,
        linewidths=1.2,
        label="offset 3 certificates",
    )
    ax.axvline(300, linestyle="--", linewidth=1.0)
    ax.text(303, 0.1, "A86 declared limit", rotation=90, va="bottom")
    ax.set_xlabel("Support maximum M")
    ax.set_ylabel("Rational probe s")
    ax.set_yticks(probes)
    ax.set_yticklabels([labels[index] for index in probes])
    ax.set_title("A90 exact pre-threshold contact-offset atlas")
    ax.legend(loc="upper left")
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / "results" / "a105_legacy_two_band_continuum_segment_catalogue.json"
OUTPUT = ROOT / "figures" / "a105_legacy_two_band_continuum_segment_atlas.png"


def qfloat(text: str) -> float:
    if "/" in text:
        numerator, denominator = text.split("/", 1)
        return int(numerator) / int(denominator)
    return float(text)


def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    records = data["records"]
    fig, ax = plt.subplots(figsize=(11.5, 12.0))
    source_labeled = strict_labeled = left_labeled = right_labeled = False
    for index, record in enumerate(records):
        y = index
        source_lower, source_upper = map(qfloat, record["segment_open_bounds"])
        component_lower = qfloat(record["strict_component"]["lower"])
        component_upper = qfloat(record["strict_component"]["upper"])
        source, = ax.plot([source_lower, source_upper], [y, y], linewidth=0.9, linestyle=":")
        if not source_labeled:
            source.set_label("declared A95/A102 rational source segment")
            source_labeled = True
        strict, = ax.plot([component_lower, component_upper], [y, y], linewidth=2.7)
        if not strict_labeled:
            strict.set_label("certified strict KKT component")
            strict_labeled = True
        left = record["strict_component"]["selected_left_boundary"]
        right = record["strict_component"]["selected_right_boundary"]
        left_mid = sum(map(qfloat, left["bracket"])) / 2
        right_mid = sum(map(qfloat, right["bracket"])) / 2
        left_marker = ax.scatter([left_mid], [y], marker="<", s=24)
        right_marker = ax.scatter([right_mid], [y], marker=">", s=24)
        if not left_labeled:
            left_marker.set_label("left algebraic KKT boundary")
            left_labeled = True
        if not right_labeled:
            right_marker.set_label("right gamma-plus boundary")
            right_labeled = True
    ax.set_yticks(range(len(records)))
    ax.set_yticklabels([f"M={record['maximum']}" for record in records], fontsize=7)
    ax.set_xlabel("probe s")
    ax.set_ylabel("legacy two-band source segment")
    ax.set_title("A105 exact continuum atlas for 40 legacy two-band lifts")
    ax.grid(True, linewidth=0.4, alpha=0.35)
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

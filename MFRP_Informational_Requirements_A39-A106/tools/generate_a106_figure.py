#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / "results" / "a106_legacy_gamma_minus_continuum_segment_catalogue.json"
OUTPUT = ROOT / "figures" / "a106_legacy_gamma_minus_continuum_segment_atlas.png"


def qfloat(text: str) -> float:
    if "/" in text:
        numerator, denominator = text.split("/", 1)
        return int(numerator) / int(denominator)
    return float(text)


def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    records = data["records"]
    fig, ax = plt.subplots(figsize=(11.5, 8.5))
    source_labeled = strict_labeled = right_labeled = full_labeled = False
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
        right = record["strict_component"]["selected_right_boundary"]
        if right is not None:
            right_mid = sum(map(qfloat, right["bracket"])) / 2
            marker = ax.scatter([right_mid], [y], marker=">", s=28)
            if not right_labeled:
                marker.set_label("right basic-support-mass boundary")
                right_labeled = True
        else:
            marker = ax.scatter([(source_lower + source_upper) / 2], [y], marker="o", s=22)
            if not full_labeled:
                marker.set_label("complete source-segment coverage")
                full_labeled = True
    ax.set_yticks(range(len(records)))
    ax.set_yticklabels([f"M={record['maximum']}" for record in records], fontsize=8)
    ax.set_xlabel("probe s")
    ax.set_ylabel("legacy gamma-minus source segment")
    ax.set_title("A106 exact continuum atlas for 18 legacy gamma-minus lifts")
    ax.grid(True, linewidth=0.4, alpha=0.35)
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()

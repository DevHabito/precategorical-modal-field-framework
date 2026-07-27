#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / "results" / "a104_exceptional_q0q1_continuum_segment_catalogue.json"
OUTPUT = ROOT / "figures" / "a104_exceptional_q0q1_continuum_segment_atlas.png"

def qfloat(text: str) -> float:
    if "/" in text:
        a, b = text.split("/", 1)
        return int(a) / int(b)
    return float(text)

def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    records = data["records"]
    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    source_label = strict_inactive_label = strict_active_label = boundary_label = None
    for index, record in enumerate(records):
        y = index
        source_l, source_u = map(qfloat, record["segment_open_bounds"])
        comp_l = qfloat(record["strict_component"]["lower"])
        comp_u = qfloat(record["strict_component"]["upper"])
        source, = ax.plot([source_l, source_u], [y, y], linewidth=1.0, linestyle=":")
        if source_label is None:
            source.set_label("declared A95 rational source segment")
            source_label = source
        strict, = ax.plot([comp_l, comp_u], [y, y], linewidth=3.0)
        if record["architecture_class"] == "q0q1_gamma_inactive":
            if strict_inactive_label is None:
                strict.set_label("q0/q1, gamma inactive strict component")
                strict_inactive_label = strict
        elif strict_active_label is None:
            strict.set_label("q0/q1, gamma-minus active strict component")
            strict_active_label = strict
        for side in ("selected_left_boundary", "selected_right_boundary"):
            root = record["strict_component"][side]
            a, b = map(qfloat, root["bracket"])
            marker = ax.scatter([(a + b) / 2], [y], marker="x", s=35)
            if boundary_label is None:
                marker.set_label("isolated algebraic KKT boundary")
                boundary_label = marker
    ax.set_yticks(range(len(records)))
    ax.set_yticklabels([f"M={record['maximum']}" for record in records])
    ax.set_xlabel("probe s")
    ax.set_ylabel("exceptional source segment")
    ax.set_title("A104 exact continuum atlas for seven exceptional q0/q1 lifts")
    ax.grid(True, linewidth=0.4, alpha=0.35)
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)

if __name__ == "__main__":
    main()

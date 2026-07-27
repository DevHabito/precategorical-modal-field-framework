#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CATALOGUE = ROOT / "results" / "a103_endpoint_released_continuum_segment_catalogue.json"
OUTPUT = ROOT / "figures" / "a103_endpoint_released_continuum_segment_atlas.png"

def qfloat(text: str) -> float:
    if "/" in text:
        a, b = text.split("/", 1)
        return int(a) / int(b)
    return float(text)

def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    records = data["records"]
    fig, ax = plt.subplots(figsize=(10.5, 8.0))
    full_label = partial_source_label = strict_label = boundary_label = None
    for index, record in enumerate(records):
        y = record["maximum"] + (0.22 if index and records[index-1]["maximum"] == record["maximum"] else 0.0)
        source_l, source_u = map(qfloat, record["segment_open_bounds"])
        comp_l = qfloat(record["strict_component"]["lower"])
        comp_u = qfloat(record["strict_component"]["upper"])
        if record["status"] == "full_segment_coverage":
            line, = ax.plot([source_l, source_u], [y, y], linewidth=2.2, color="C1")
            if full_label is None:
                line.set_label("complete source-segment coverage")
                full_label = line
        else:
            source, = ax.plot([source_l, source_u], [y, y], linewidth=0.8, linestyle=":", color="0.45")
            strict, = ax.plot([comp_l, comp_u], [y, y], linewidth=2.2, color="C0")
            if partial_source_label is None:
                source.set_label("declared A95 source segment")
                partial_source_label = source
            if strict_label is None:
                strict.set_label("certified strict lifted component")
                strict_label = strict
            for side in ("selected_left_boundary", "selected_right_boundary"):
                root = record["strict_component"][side]
                if root:
                    a, b = map(qfloat, root["bracket"])
                    marker = ax.scatter([(a+b)/2], [y], marker="x", s=22, color="C3")
                    if boundary_label is None:
                        marker.set_label("isolated algebraic KKT boundary")
                        boundary_label = marker
    ax.set_xlabel("probe s")
    ax.set_ylabel("support maximum M")
    ax.set_title("A103 exact continuum atlas for 76 endpoint-released lift segments")
    ax.grid(True, linewidth=0.4, alpha=0.35)
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / 'results' / 'a102_complete_rational_witness_lift_atlas_catalogue.json'
OUTPUT = ROOT / 'figures' / 'a102_complete_rational_witness_lift_atlas.png'

LABELS = {
    'legacy_natural': 'Legacy natural lift (980)',
    'endpoint_released_gamma_inactive': 'Endpoint-released, gamma inactive (76)',
    'q0q1_gamma_inactive': 'q0/q1, gamma inactive (3)',
    'q0q1_gamma_active': 'q0/q1, gamma− active (4)',
}
MARKERS = {
    'legacy_natural': '.',
    'endpoint_released_gamma_inactive': '^',
    'q0q1_gamma_inactive': 's',
    'q0q1_gamma_active': '*',
}
SIZES = {
    'legacy_natural': 14,
    'endpoint_released_gamma_inactive': 34,
    'q0q1_gamma_inactive': 62,
    'q0q1_gamma_active': 90,
}


def main() -> None:
    data = json.loads(CATALOGUE.read_text(encoding='utf-8'))
    records = data['records']
    fig, ax = plt.subplots(figsize=(11.5, 6.6))
    for class_name in LABELS:
        subset = [item for item in records if item['resolution']['broad_class'] == class_name]
        ax.scatter(
            [item['key_fields']['maximum'] for item in subset],
            [item['key_fields']['compressed_maximizer_contact'] for item in subset],
            marker=MARKERS[class_name],
            s=SIZES[class_name],
            label=LABELS[class_name],
            alpha=0.78 if class_name == 'legacy_natural' else 0.95,
        )
    ax.set_xlabel('Support maximum M')
    ax.set_ylabel('Compressed maximizer contact j')
    ax.set_title('A102 complete exact rational-witness lift atlas')
    ax.grid(True, linewidth=0.5, alpha=0.35)
    ax.legend(loc='upper left', frameon=True)
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=220)
    plt.close(fig)
    print(OUTPUT)


if __name__ == '__main__':
    main()

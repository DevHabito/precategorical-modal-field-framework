#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / 'results' / 'a82_adjacent_contact_locator_results.json'
OUTPUT = ROOT / 'figures' / 'a82_compressed_contact_locator.png'

def main() -> None:
    data = json.loads(RESULT.read_text(encoding='utf-8'))
    records = data['probe_theorem']['locator']
    maximums = [item['maximum'] for item in records]
    compressed = [item['compressed_maximizer'] for item in records]
    selected = [item['predicted_selection']['contact'] for item in records]

    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.plot(maximums, compressed, marker='o', markersize=3, linewidth=1.2, label='Compressed objective maximizer j(M)')
    ax.plot(maximums, selected, marker='x', markersize=4, linewidth=1.0, label='Selected A78 contact index')
    ax.set_xlabel('Support maximum M')
    ax.set_ylabel('Interior contact index')
    ax.set_title('A82 exact rational-probe contact locator')
    ax.grid(True, alpha=0.25)
    ax.legend()
    for maximum in (28, 79):
        item = next(record for record in records if record['maximum'] == maximum)
        ax.annotate(
            f'M={maximum}',
            (maximum, item['compressed_maximizer']),
            xytext=(5, 8),
            textcoords='offset points',
        )
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=180)
    plt.close(fig)
    print(OUTPUT)

if __name__ == '__main__':
    main()

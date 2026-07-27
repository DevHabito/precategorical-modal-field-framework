#!/usr/bin/env python3
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
CAT = json.loads((ROOT / 'results' / 'a97_endpoint_released_obstruction_catalogue.json').read_text())
RES = json.loads((ROOT / 'results' / 'a97_endpoint_released_interval_and_obstruction_results.json').read_text())
records = CAT['records']
passes = [r for r in records if r['endpoint_released_result']['status'] == 'pass']
failures = [r for r in records if r['endpoint_released_result']['status'] != 'pass']

fig, ax = plt.subplots(figsize=(10.5, 5.8))
ax.scatter(
    [r['maximum'] for r in passes],
    [float(Fraction(r['witness'])) for r in passes],
    s=32,
    label='Strict full-LP KKT pass',
)
ax.scatter(
    [r['maximum'] for r in failures],
    [float(Fraction(r['witness'])) for r in failures],
    s=68,
    marker='x',
    linewidths=2,
    label='Residual q0-entry obstruction',
)
for r in failures:
    ax.annotate(str(r['maximum']), (r['maximum'], float(Fraction(r['witness']))), xytext=(0, 7), textcoords='offset points', ha='center', fontsize=8)

interval = RES['M125_interval_theorem']['strict_component']
lo = float(Fraction(interval['lower_root_bracket'][0]))
hi = float(Fraction(interval['upper_root_bracket'][1]))
ax.vlines(125, lo, hi, linewidth=4, label='M=125 exact strict-KKT component')
ax.scatter([125], [float(Fraction(33, 250))], marker='s', s=55)

ax.set_xlabel('Support maximum M')
ax.set_ylabel('Rational witness s')
ax.set_title('A97 endpoint-released family: 76 exact resolutions and 7 residual obstructions')
ax.grid(True, alpha=0.25)
ax.legend(loc='best')
fig.tight_layout()
out = ROOT / 'figures' / 'a97_endpoint_released_obstruction_atlas.png'
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=180)
print(out)

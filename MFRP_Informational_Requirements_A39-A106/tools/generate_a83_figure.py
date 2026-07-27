#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'results'/'a83_seven_term_adjacent_sign_atlas_results.json').read_text())
records=data['support_records']
M=[r['maximum'] for r in records]
for key,label in [('local_lower','s = 0.129'),('s0','s = 0.131'),('local_upper','s = 0.133')]:
    plt.plot(M,[r['maximizing_contact'][key] for r in records],label=label)
plt.xlabel('Support maximum M')
plt.ylabel('Compressed maximizing contact k')
plt.title('A83 exact local adjacent-contact sign atlas')
plt.legend()
plt.tight_layout()
out=ROOT/'figures'/'a83_local_adjacent_contact_sign_atlas.png'
plt.savefig(out,dpi=180)
print(out)

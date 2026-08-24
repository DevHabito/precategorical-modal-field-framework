#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'results'/'a86_exact_rational_contact_strip_catalogue.json').read_text())
records=data['records']
labels={'local_lower':'s=129/1000','probe':'s=131/1000','local_upper':'s=133/1000'}
fig,ax=plt.subplots(figsize=(10,5.8))
for name in ('local_lower','probe','local_upper'):
    items=[r for r in records if r['probe_name']==name]
    ax.plot([r['maximum'] for r in items],[r['ceil_offset'] for r in items],'.',markersize=3,label=labels[name])
ax.set_xlabel('Support maximum M')
ax.set_ylabel('Exact offset  k* - ceil(M c(s))')
ax.set_yticks([0,1,2])
ax.set_title('A86 exact three-contact localization')
ax.grid(True,alpha=0.25)
ax.legend()
fig.tight_layout()
out=ROOT/'figures'/'a86_exact_three_contact_localizer.png'
fig.savefig(out,dpi=180)
print(out)

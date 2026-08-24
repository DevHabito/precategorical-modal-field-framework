#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'results'/'a95_rational_witness_lift_catalogue.json').read_text())
records=DATA['records']

cats={
    'three_band_gamma_plus':([],[],'gamma-plus lift','o'),
    'three_band_gamma_minus':([],[],'gamma-minus lift','^'),
    'two_band_compressed':([],[],'gamma inactive','s'),
    'obstruction':([],[],'no natural lift','x'),
}
for r in records:
    x=r['maximum']; y=r['compressed_maximizer_contact']/r['maximum']
    if r['strict_pass_count']==0:
        key='obstruction'
    else:
        p=r['strict_passes'][0]
        if p['family']=='two_band_compressed': key='two_band_compressed'
        elif p['gamma_sign']==1: key='three_band_gamma_plus'
        else: key='three_band_gamma_minus'
    cats[key][0].append(x); cats[key][1].append(y)

fig,ax=plt.subplots(figsize=(11,6.5))
for key,(xs,ys,label,marker) in cats.items():
    if key=='obstruction':
        ax.scatter(xs,ys,label=label,marker=marker,s=34,linewidths=1.2,zorder=5)
    else:
        ax.scatter(xs,ys,label=label,marker=marker,s=18,alpha=0.7)
ax.axvline(125,linestyle='--',linewidth=1)
ax.text(127,ax.get_ylim()[1]-0.005,'first obstruction M=125',va='top',fontsize=9)
ax.set_xlabel('Support maximum M')
ax.set_ylabel('Compressed maximizer contact j / M')
ax.set_title('A95 exact rational-witness lift atlas')
ax.legend(loc='best',frameon=True)
ax.grid(True,alpha=0.2)
fig.tight_layout()
out=ROOT/'figures'/'a95_rational_witness_lift_atlas.png'
fig.savefig(out,dpi=180)
print(out)

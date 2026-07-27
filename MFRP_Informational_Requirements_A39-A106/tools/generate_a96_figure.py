#!/usr/bin/env python3
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'results'/'a96_full_lp_active_set_resolution_results.json').read_text())
p={int(x):float(Fraction(v)) for x,v in d['exact_solution']['original_P_probabilities'].items()}
q={int(x):float(Fraction(v)) for x,v in d['exact_solution']['original_Q_probabilities'].items()}
fig,ax=plt.subplots(figsize=(10,5.5))
for x,y in p.items():
    ax.vlines(x,1e-23,y,linewidth=2)
    ax.scatter([x],[y],s=55,label='P' if x==min(p) else None)
for x,y in q.items():
    ax.vlines(x,1e-23,y,linewidth=2,linestyles='dashed')
    ax.scatter([x],[y],s=55,marker='s',label='Q' if x==min(q) else None)
ax.set_yscale('log')
ax.set_ylim(1e-23,1)
ax.set_xlim(-3,128)
ax.set_xlabel('Support point x')
ax.set_ylabel('Original probability mass (log scale)')
ax.set_title('A96 exact unrestricted active set at M=125, s=33/250')
ax.legend()
ax.grid(True,which='both',alpha=0.25)
fig.tight_layout()
out=ROOT/'figures'/'a96_unrestricted_full_lp_active_set.png'
fig.savefig(out,dpi=180)
print(out)

#!/usr/bin/env python3
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/'results'/'a99_q0q1_interval_and_residual_atlas_results.json'
OUT=ROOT/'figures'/'a99_q0q1_interval_and_residual_atlas.png'

def frac(s:str)->float:
    return float(Fraction(s))

def main():
    d=json.loads(RESULT.read_text(encoding='utf-8'))
    m=d['M396_interval_theorem']
    lo=sum(frac(x) for x in m['lower_root_bracket'])/2
    hi=sum(frac(x) for x in m['upper_root_bracket'])/2
    s0=0.13
    atlas=d['remaining_residual_atlas']
    passes={item[0] for item in atlas['pass_keys']}
    failures={item[0] for item in atlas['failure_keys']}
    supports=sorted(passes|failures)
    values=[1 if M in passes else 0 for M in supports]

    fig,axes=plt.subplots(2,1,figsize=(9,6.8),constrained_layout=True)
    ax=axes[0]
    ax.axhline(0,linewidth=1)
    ax.plot([0.129,0.133],[0,0],linewidth=3,alpha=.25)
    ax.plot([lo,hi],[0,0],linewidth=10)
    ax.scatter([lo,hi,s0],[0,0,0],zorder=3)
    ax.text(lo,0.06,'gamma− slack = 0',ha='center',fontsize=9)
    ax.text(hi,-0.08,'q0 mass = 0',ha='center',fontsize=9)
    ax.text(s0,0.06,'s = 13/100',ha='center',fontsize=9)
    ax.set_xlim(0.129,0.133)
    ax.set_ylim(-0.16,0.16)
    ax.set_yticks([])
    ax.set_xlabel('probe s')
    ax.set_title('A99 exact strict-KKT component at M=396')

    ax=axes[1]
    ax.scatter(supports,values,s=55)
    ax.set_yticks([0,1],['fails','strict pass'])
    ax.set_xticks(supports)
    ax.set_ylim(-.25,1.25)
    ax.grid(axis='x',alpha=.2)
    ax.set_xlabel('support maximum M')
    ax.set_title('A98 q0/q1 architecture on the six remaining A97 residuals')
    for M,v in zip(supports,values):
        ax.text(M,v+.12 if v else v-.16,'pass' if v else 'fail',ha='center',fontsize=8)

    OUT.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(OUT,dpi=180)
    print(OUT)

if __name__=='__main__': main()

#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
import pandas as pd
import sys
sys.path.insert(0,'/mnt/data')
import a16_local_global_manifoldlikeness as a16

SEED=20260717
N=256
SAMPLES=16
POOL=40
WIDTH=0.10
rng=np.random.default_rng(SEED)

# Independent Minkowski-only model.
model=a16.fit_global_model(N,rng)
holdouts=[a16.sample_minkowski_2d(N,rng) for _ in range(SAMPLES)]
targets=[a16.relation_fraction(r) for r in holdouts]

def four_corner(n,rng):
    sizes=[n//4]*4
    for i in range(n-sum(sizes)): sizes[i]+=1
    centers=[(0.20,0.20),(0.20,0.80),(0.80,0.20),(0.80,0.80)]
    us=[];vs=[]
    for size,(cu,cv) in zip(sizes,centers):
        us.append(rng.uniform(cu-WIDTH/2,cu+WIDTH/2,size=size))
        vs.append(rng.uniform(cv-WIDTH/2,cv+WIDTH/2,size=size))
    u=np.concatenate(us);v=np.concatenate(vs)
    R=(u[:,None]<u[None,:])&(v[:,None]<v[None,:])
    np.fill_diagonal(R,False)
    return a16.permute_relation(R,rng)

rows=[]
for idx,target in enumerate(targets):
    best=None
    for _ in range(POOL):
        R=four_corner(N,rng)
        mismatch=abs(a16.relation_fraction(R)-target)
        if best is None or mismatch<best[0]: best=(mismatch,R)
    mismatch,R=best
    q,p,global_pass=a16.global_score(R,model)
    # Exact 2D by coordinate construction; scan a subset independently.
    local=None
    if idx<4:
        local=a16.local_audit(R)
    rows.append({
        'sample_index':idx,
        'target_ordering_fraction':target,
        'ordering_fraction':a16.relation_fraction(R),
        'ordering_fraction_mismatch':mismatch,
        'q_score':q,
        'p_value':p,
        'global_pass':global_pass,
        'local_scan_run':local is not None,
        'local_pass':None if local is None else local['local_pass'],
        'local_channel':None if local is None else local['channel'],
    })

df=pd.DataFrame(rows)
out=Path('/mnt/data/a16_exact_results')
df.to_csv(out/'a16_four_corner_diagnostic.csv',index=False)
summary={
 'status':'POST_HOC_STRONGER_NONUNIFORM_2D_CONTROL',
 'n':N,
 'samples':SAMPLES,
 'pool_per_target':POOL,
 'width':WIDTH,
 'global_acceptance_rate':float(df.global_pass.mean()),
 'global_rejection_rate':float(1-df.global_pass.mean()),
 'max_ordering_fraction_mismatch':float(df.ordering_fraction_mismatch.max()),
 'median_p_value':float(df.p_value.median()),
 'scanned_local_pass_rate':float(df[df.local_scan_run].local_pass.mean()),
 'interpretation':'Four separated corner clusters remain exact 2D orders, but strongly violate the uniform single-diamond sprinkling profile. This is a post-hoc diagnostic and does not alter the preregistered A16 gate result.'
}
(out/'a16_four_corner_diagnostic.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
print(df.to_string(index=False))

#!/usr/bin/env python3
from __future__ import annotations

import itertools, json, csv, math
from pathlib import Path
from collections import defaultdict
import numpy as np

N=5
EDGES=[(i,j) for i in range(N) for j in range(N) if i!=j]
M=len(EDGES)
ALL_MASKS=np.arange(1<<M,dtype=np.uint32)


def masks_to_edge_vectors(masks: np.ndarray)->np.ndarray:
    masks=np.asarray(masks,dtype=np.uint32)
    X=np.empty((len(masks),M),dtype=np.float64)
    for bit in range(M):
        X[:,bit]=((masks>>bit)&1)
    return X


def adj_to_mask(A: np.ndarray)->int:
    mask=0
    for bit,(i,j) in enumerate(EDGES):
        if A[i,j]: mask |= 1<<bit
    return mask


def set_partitions(n:int):
    # restricted growth strings
    a=[0]*n
    yield tuple(a)
    def rec(pos,maxv):
        if pos==n:
            yield tuple(a); return
        for v in range(maxv+2):
            a[pos]=v
            yield from rec(pos+1,max(maxv,v))
    # custom starts at pos1 with a0=0
    def rec2(pos,maxv):
        if pos==n:
            yield tuple(a); return
        for v in range(maxv+2):
            a[pos]=v
            yield from rec2(pos+1,max(maxv,v))
    # avoid duplicate all-zero from above
    yield from rec2(1,0)

# dedupe
PARTS=[]; seen=set()
for p in set_partitions(N):
    # canonical already
    if p not in seen:
        seen.add(p); PARTS.append(p)


def entropy_of_partition(p):
    counts=np.bincount(np.array(p), minlength=max(p)+1)
    probs=counts/N
    return float(-np.sum(probs*np.log(probs)))

# Precompute cell assignments on off-diagonal edges and entropy
PINFO=[]
for p in PARTS:
    k=max(p)+1
    cell_map={}
    labels=[]
    for i,j in EDGES:
        key=(p[i],p[j])
        if key not in cell_map: cell_map[key]=len(cell_map)
        labels.append(cell_map[key])
    labels=np.array(labels,dtype=np.int16)
    c=len(cell_map)
    inc=np.zeros((M,c),dtype=np.float64)
    inc[np.arange(M),labels]=1.0
    counts=inc.sum(axis=0)
    PINFO.append((p,entropy_of_partition(p),inc,counts))

BUDGETS=sorted(set(round(h,12) for _,h,_,_ in PINFO))


def rate_distortion_for_masks(masks: list[int] | np.ndarray)->np.ndarray:
    masks=np.asarray(masks,dtype=np.uint32)
    X=masks_to_edge_vectors(masks)
    means=X.mean(axis=1,keepdims=True)
    Xc=X-means
    total=np.sum(Xc*Xc,axis=1)
    # initialize best exact entropy then cumulative min by budget
    exact={b:np.full(len(masks),np.inf) for b in BUDGETS}
    for p,h,inc,counts in PINFO:
        sums=Xc@inc
        captured=np.sum((sums*sums)/counts,axis=1)
        dist=np.divide(total-captured,total,out=np.zeros_like(total),where=total>0)
        b=round(h,12)
        exact[b]=np.minimum(exact[b],dist)
    curves=[]
    running=np.full(len(masks),np.inf)
    for b in BUDGETS:
        running=np.minimum(running,exact[b])
        curves.append(running.copy())
    return np.stack(curves,axis=1)


def degree_code_from_masks(masks: np.ndarray)->np.ndarray:
    X=masks_to_edge_vectors(masks).astype(np.int8)
    out=np.zeros((len(masks),N),dtype=np.int8)
    inn=np.zeros((len(masks),N),dtype=np.int8)
    for bit,(i,j) in enumerate(EDGES):
        out[:,i]+=X[:,bit]; inn[:,j]+=X[:,bit]
    digits=np.concatenate([out,inn],axis=1).astype(np.int64)
    powers=np.array([5**i for i in range(2*N)],dtype=np.int64)
    return digits@powers


def controls():
    G={}
    A=np.zeros((N,N),dtype=np.uint8)
    for i in range(N): A[i,(i+1)%N]=1
    G['directed_C5']=A.copy()
    A=np.zeros((N,N),dtype=np.uint8); A[0,1]=A[1,0]=1; A[2,3]=A[3,4]=A[4,2]=1
    G['C2_plus_C3']=A.copy()
    A=np.zeros((N,N),dtype=np.uint8)
    for i in range(N-1): A[i,i+1]=1
    G['directed_path5']=A.copy()
    A=np.zeros((N,N),dtype=np.uint8)
    for i in range(N): A[i,(i+1)%N]=1; A[i,(i+2)%N]=1
    G['circulant_5_12']=A.copy()
    A=np.zeros((N,N),dtype=np.uint8)
    for i in range(N): A[i,(i+1)%N]=1; A[i,(i-1)%N]=1
    G['bidirectional_C5']=A.copy()
    A=np.ones((N,N),dtype=np.uint8); np.fill_diagonal(A,0)
    for i in range(N): A[i,(i+1)%N]=0
    G['complement_directed_C5']=A.copy()
    return G


def main():
    outdir=Path('/mnt/data/a4_exact_results'); outdir.mkdir(exist_ok=True)
    all_codes=degree_code_from_masks(ALL_MASKS)
    rows=[]; curve_rows=[]
    for name,A in controls().items():
        mask=adj_to_mask(A)
        code=all_codes[mask]
        fiber=np.flatnonzero(all_codes==code).astype(np.uint32)
        curves=rate_distortion_for_masks(fiber)
        obs_idx=int(np.flatnonzero(fiber==mask)[0])
        obs=curves[obs_idx]
        # nontrivial budgets exclude H=0 and H=log n, and budgets where all curves degenerate same? keep all intermediate
        idxs=[i for i,b in enumerate(BUDGETS) if b>1e-12 and b<math.log(N)-1e-12]
        pvals=[]
        for i in idxs:
            p=float(np.mean(curves[:,i] <= obs[i]+1e-12))
            pvals.append(p)
            curve_rows.append({'control':name,'budget_entropy':BUDGETS[i],'observed_distortion':float(obs[i]),'exact_marginal_p':p,'fiber_size':len(fiber)})
        # intersection-union: unusually low at every budget
        p_iut=max(pvals) if pvals else 1.0
        # exact dominance count: null uniformly at least as compressible
        dom=np.all(curves[:,idxs] <= obs[idxs][None,:]+1e-12,axis=1)
        p_dom=float(np.mean(dom))
        # observed uniformly dominates null
        dominated_by_obs=np.all(obs[idxs][None,:] <= curves[:,idxs]+1e-12,axis=1)
        frac_obs_dominates=float(np.mean(dominated_by_obs))
        rows.append({'control':name,'fiber_size':len(fiber),'p_iut_all_budgets':p_iut,'p_uniformly_better_null':p_dom,'fraction_fiber_dominated_by_observed':frac_obs_dominates,'curve':obs.tolist()})
    with open(outdir/'a4_summary.json','w') as f: json.dump({'n':N,'off_diagonal_edges':M,'partitions':len(PARTS),'entropy_budgets':BUDGETS,'controls':rows},f,indent=2)
    with open(outdir/'a4_curve_tests.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=curve_rows[0].keys()); w.writeheader(); w.writerows(curve_rows)
    print(json.dumps({'n':N,'partitions':len(PARTS),'budgets':BUDGETS,'controls':rows},indent=2))

if __name__=='__main__': main()

#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse
import json

BETA0 = F(1,8)
S_VALUES = [F(129,1000), F(131,1000), F(133,1000)]
TAU_VALUES = [F(n,1000) for n in range(470,531,5)]
SMALL_M = [20,30,40,50,60,70,80,100]
TAIL_M = [521,538,561,760,1000,1500]

def sg(x: F) -> int:
    return (x > 0) - (x < 0)

def solve(A, b):
    n=len(b)
    a=[[F(x) for x in A[i]]+[F(b[i])] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if a[i][c])
        a[c],a[p]=a[p],a[c]
        q=a[c][c]
        a[c]=[x/q for x in a[c]]
        for i in range(n):
            if i==c: continue
            q=a[i][c]
            if q:
                a[i]=[a[i][j]-q*a[c][j] for j in range(n+1)]
    return [a[i][-1] for i in range(n)]

def powers(v: F, M: int):
    out=[F(1)]*(M+1)
    for i in range(1,M+1):
        out[i]=out[i-1]*v
    return out

def q_affine_coeffs(M: int, tau: F):
    h=M//2
    A=[[1,1,1],[1,h,h+1],[tau,tau**h,tau**(h+1)]]
    C=solve(A,[0,0,1])
    D=solve(A,[1,F(M,2),0])
    return C,D

def epsilon(M: int, tau: F, mode: str) -> F:
    h=M//2
    scale=1875 if M%2==0 else 2500
    if mode=="scaled":
        return tau**h / scale
    if mode=="frozen":
        return F(1, scale*2**h)
    raise ValueError(mode)

def exact_b_tau(M: int, s: F, tau: F) -> int:
    # ceil(M log(1/tau)/(-2 log s)) without floating point.
    lo,hi=0,M
    while lo<hi:
        mid=(lo+hi)//2
        if s**(2*mid) <= tau**M:
            hi=mid
        else:
            lo=mid+1
    return lo

def sequence(M: int, s: F, beta: F, tau: F, mode: str, ks):
    h=M//2
    C,D=q_affine_coeffs(M,tau)
    ep=epsilon(M,tau,mode)
    sp,bp,tp=powers(s,M),powers(beta,M),powers(tau,M)

    def qparts(p):
        return (
            C[0]*p[1]+C[1]*p[h]+C[2]*p[h+1],
            D[0]*p[1]+D[1]*p[h]+D[2]*p[h+1],
        )

    Cs,Ds=qparts(sp)
    Cb,Db=qparts(bp)
    As,Ab,At=F(1+sp[M],2),F(1+bp[M],2),F(1+tp[M],2)
    Hs=As-Ds-2*ep
    Hb=Ab-Db+2*ep

    vals={}
    for k in ks:
        Bs=sp[k]-F(M-k,M)-F(k,M)*sp[M]
        Bb=bp[k]-F(M-k,M)-F(k,M)*bp[M]
        Bt=tp[k]-F(M-k,M)-F(k,M)*tp[M]
        den=Bs*Hb-Bb*Hs
        z=(Cs*Hb-Cb*Hs)/den
        tt=(Bs*Cb-Bb*Cs)/den
        vals[k]=At*tt+Bt*z
    return vals

def scan(M: int, s: F, beta: F, tau: F, mode: str, full=True, radius=6):
    b=exact_b_tau(M,s,tau)
    h=M//2
    ks=list(range(2,h)) if full else list(range(max(2,b-radius),min(h,b+radius+5)))
    vals=sequence(M,s,beta,tau,mode,ks)
    es={k:vals[k+1]-vals[k] for k in ks if k+1 in vals}
    signs=[sg(es[k]) for k in sorted(es)]
    transitions=sum(a!=b_ for a,b_ in zip(signs,signs[1:]))
    maxks=[]
    if full:
        mv=max(vals.values())
        maxks=[k for k,v in vals.items() if v==mv]
    J=es[b+1]-es[b+2]/tau if b+1 in es and b+2 in es else None
    return b,es,transitions,maxks,J

def tau_small():
    out={}
    for mode in ("scaled","frozen"):
        rec={"cases":0,"variation_failures":0,"localization_failures":0,"nesting_failures":0}
        for M in SMALL_M:
            for s in S_VALUES:
                for tau in TAU_VALUES:
                    b,es,tr,maxks,J=scan(M,s,BETA0,tau,mode,full=True)
                    rec["cases"]+=1
                    if tr!=1 or any(v==0 for v in es.values()):
                        rec["variation_failures"]+=1
                    if not all(k-b in (1,2,3) for k in maxks):
                        rec["localization_failures"]+=1
                    if J is None or J<=0:
                        rec["nesting_failures"]+=1
        out[mode]=rec
    return out

def tau_tail(mode: str):
    rec={"cases":0,"remote_sign_failures":0,"nesting_failures":0}
    for M in TAIL_M:
        for s in S_VALUES:
            for tau in TAU_VALUES:
                b,es,_,_,J=scan(M,s,BETA0,tau,mode,full=False,radius=6)
                rec["cases"]+=1
                bad=(
                    any(k<=b and v<=0 for k,v in es.items())
                    or any(k>=b+3 and v>=0 for k,v in es.items())
                )
                if bad:
                    rec["remote_sign_failures"]+=1
                if J is None or J<=0:
                    rec["nesting_failures"]+=1
    return rec

def beta_section():
    vals=[F(n,1000) for n in [115,120,123,124,125,126,127,128]]
    out={}
    first=None
    for beta in vals:
        rec={"cases":0,"variation_failures":0,"localization_failures":0,"nesting_failures":0}
        for M in [20,30,40,50,60,80,100]:
            for s in S_VALUES:
                if beta>=s: continue
                b,es,tr,maxks,J=scan(M,s,beta,F(1,2),"scaled",full=True)
                rec["cases"]+=1
                bad=tr!=1 or any(v==0 for v in es.values())
                if bad:
                    rec["variation_failures"]+=1
                    if first is None:
                        first={
                            "M":M,"s":str(s),"beta":str(beta),"b_tau":b,
                            "variation_count":tr,"maximizers":maxks,
                            "J_sign":sg(J) if J is not None else None,
                            "factor_signs":{str(k):sg(v) for k,v in sorted(es.items())},
                        }
                if not all(k-b in (1,2,3) for k in maxks):
                    rec["localization_failures"]+=1
                if J is None or J<=0:
                    rec["nesting_failures"]+=1
        out[str(beta)]=rec
    return {"stats_by_beta":out,"first_failure":first}

def joint_small():
    betas=[F(31,250),F(1,8),F(63,500)]
    taus=[F(49,100),F(99,200),F(1,2),F(101,200),F(51,100)]
    rec={"cases":0,"failures":0}
    for M in [20,30,40,50,60,80,100]:
        for s in S_VALUES:
            for beta in betas:
                if beta>=s: continue
                for tau in taus:
                    b,es,tr,maxks,J=scan(M,s,beta,tau,"scaled",full=True)
                    rec["cases"]+=1
                    if (
                        tr!=1 or any(v==0 for v in es.values())
                        or not all(k-b in (1,2,3) for k in maxks)
                        or J is None or J<=0
                    ):
                        rec["failures"]+=1
    return rec

def joint_tail():
    betas=[F(31,250),F(1,8),F(63,500)]
    taus=[F(49,100),F(99,200),F(1,2),F(101,200),F(51,100)]
    rec={"cases":0,"failures":0}
    for M in [521,538,561,760,1000]:
        for s in S_VALUES:
            for beta in betas:
                if beta>=s: continue
                for tau in taus:
                    b,es,_,_,J=scan(M,s,beta,tau,"scaled",full=False,radius=6)
                    rec["cases"]+=1
                    bad=(
                        any(k<=b and v<=0 for k,v in es.items())
                        or any(k>=b+3 and v>=0 for k,v in es.items())
                        or J is None or J<=0
                    )
                    if bad:
                        rec["failures"]+=1
    return rec

def counterexample():
    M=521; s=F(129,1000); tau=F(49,100)
    b,es,tr,maxks,J=scan(M,s,BETA0,tau,"frozen",full=True)
    return {
        "M":M,"s":str(s),"tau":str(tau),"beta":str(BETA0),
        "b_tau":b,"variation_count":tr,"maximizers":maxks,
        "offsets":[k-b for k in maxks],"J_sign":sg(J),
        "signs_near_b":{str(k):sg(es[k]) for k in range(b-3,b+5) if k in es},
        "last_factor_sign":sg(es[max(es)]),
    }

SECTIONS={
    "tau-small":tau_small,
    "tau-tail-scaled":lambda:tau_tail("scaled"),
    "tau-tail-frozen":lambda:tau_tail("frozen"),
    "beta":beta_section,
    "joint-small":joint_small,
    "joint-tail":joint_tail,
    "counterexample":counterexample,
}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--section",choices=sorted(SECTIONS),required=True)
    ap.add_argument("--output")
    args=ap.parse_args()
    data={
        "audit":"A115_PARAMETER_DEPENDENCE_EXACT_STRESS_SECTION",
        "section":args.section,
        "result":SECTIONS[args.section](),
    }
    text=json.dumps(data,indent=2)
    if args.output:
        Path(args.output).write_text(text,encoding="utf-8")
    print(text)

if __name__=="__main__":
    main()

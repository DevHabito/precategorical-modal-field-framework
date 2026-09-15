#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
import json
from pathlib import Path
import sympy as sp

BETA=F(1,8)
DELTA=F(1,1875)
S_PROBES=(F(129,1000),F(131,1000),F(133,1000))
OUT=Path(__file__).resolve().parent/'A116_EXACT_AUDIT_RESULTS_20260915.json'

def sg(x): return 1 if x>0 else -1 if x<0 else 0

def den(M,tau):
    h=M//2; u=tau**h
    return tau-h*u+(h-1)*tau*u

def eps(M,tau):
    h=M//2; u=tau**h
    return DELTA*(u if M%2==0 else F(1+tau,2)*u)

def dt(M,r,tau):
    h=M//2; u=tau**h
    rh=r**h; rh1=rh*r
    L=r-h*rh+(h-1)*rh1
    D=den(M,tau)
    if M%2==0:
        return rh-u*L/D
    return F(rh+rh1,2)-F(1+tau,2)*u*L/D

def B(M,k,r): return r**k-F(M-k,M)-F(k,M)*r**M

def dB(M,k,r): return r**(k+1)-r**k+F(1-r**M,M)

def E(M,k,s,tau):
    e=eps(M,tau)
    hb=F(1+BETA**M,2)-dt(M,BETA,tau)+2*e
    hs=F(1+s**M,2)-dt(M,s,tau)-2*e
    bb,bt=B(M,k,BETA),B(M,k,tau)
    xb,xt=dB(M,k,BETA),dB(M,k,tau)
    A=F(1+tau**M,2)
    X=A*bb-hb*bt
    Y=-A*xb+hb*xt
    W=-bb*xt+bt*xb
    return X*dB(M,k,s)+Y*B(M,k,s)+W*hs

def b_exact(M,s,tau):
    lo,hi=0,M; target=tau**M
    while lo<hi:
        m=(lo+hi)//2
        if s**(2*m)<=target: hi=m
        else: lo=m+1
    return lo

def admiss(M,b): return 2<=b+1 and b+2<=M//2-2

def J(M,s,tau):
    b=b_exact(M,s,tau)
    if not admiss(M,b): return None,b
    return E(M,b+1,s,tau)-E(M,b+2,s,tau)/tau,b

def exp_lower(x,N):
    t=F(1); sm=F(1)
    for n in range(1,N+1):
        t*=x/n; sm+=t
    return sm

def exp_upper(x,N):
    t=F(1); sm=F(1)
    for n in range(1,N+1):
        t*=x/n; sm+=t
    nxt=t*x/(N+1)
    ratio=x/(N+2)
    assert ratio<1
    return sm+nxt/(1-ratio)

def symbolic_gates():
    beta,s,tau,k=sp.symbols('beta s tau k', positive=True)
    cbs,cbt,cst,cb,ckb,cs,cks,ct,ckt,c1=sp.symbols('cbs cbt cst cb ckb cs cks ct ckt c1')
    E0=(cbs*(beta*s)**k+cbt*(beta*tau)**k+cst*(s*tau)**k
        +(cb+k*ckb)*beta**k+(cs+k*cks)*s**k+(ct+k*ckt)*tau**k+c1)
    E1=(cbs*(beta*s)**(k+1)+cbt*(beta*tau)**(k+1)+cst*(s*tau)**(k+1)
        +(cb+(k+1)*ckb)*beta**(k+1)+(cs+(k+1)*cks)*s**(k+1)
        +(ct+(k+1)*ckt)*tau**(k+1)+c1)
    J0=sp.expand(E0-E1/tau)
    J1=(cbs*(1-beta*s/tau)*(beta*s)**k
        +cbt*(1-beta)*(beta*tau)**k
        +cst*(1-s)*(s*tau)**k
        +beta**k*((1-beta/tau)*cb+(k*(1-beta/tau)-beta/tau)*ckb)
        +s**k*((1-s/tau)*cs+(k*(1-s/tau)-s/tau)*cks)
        -ckt*tau**k+c1*(1-1/tau))
    A,hb,hs,ab,aa,at=sp.symbols('A hb hs ab aa at')
    X=A*aa-hs*at
    Y=A*ab-hb*at
    cb0=A*aa+A*beta-A-hs*at-hs*beta+hs
    cs0=-A*ab-A*s+A+hb*at+hb*s-hb
    c10=-A*aa+A*ab+hb*aa-hb*at-hs*ab+hs*at
    return {
        'exact_J_transform': sp.simplify(J0-J1)==0,
        'beta_affine_group': sp.expand(cb0-(X+(A-hs)*(beta-1)))==0,
        'source_affine_group': sp.expand(cs0-(-Y+(A-hb)*(1-s)))==0,
        'constant_group': sp.expand(c10-(A*(ab-aa)+hb*(aa-at)+hs*(at-ab)))==0,
    }

def main():
    gates=symbolic_gates(); assert all(gates.values()),gates
    s0=F(133,1000); lam=F(5,2); d=4
    alpha=lam/(2*s0)
    target=F(1000,133)
    e2_up=exp_upper(F(2),8)
    e21_lo=exp_lower(F(21,10),8)
    assert e2_up<target and e21_lo>target
    x_lower=alpha/F(21,10); x_upper=alpha/F(2)
    assert x_lower>4 and x_upper<5
    ea_lo=exp_lower(alpha,12)
    assert ea_lo>10000
    Bbar=BETA/s0+2*DELTA
    C=1-BETA/s0-4*DELTA
    Q=1+lam*F(1,2)*s0**(1-d)-Bbar*(alpha+1)
    assert Q>0 and C>0
    margin=C-Q*F(1,10000)
    assert margin>0

    boundary=[]
    for M in (2000,5000,10000,20000):
        tau=s0+lam/M
        j,b=J(M,s0,tau)
        assert j is not None and b==M//2-4 and j<0
        boundary.append({'M':M,'s':'133/1000','tau':str(tau),'b':b,'h_minus_b':M//2-b,'sign_J':-1})

    compact=[]
    for M in (2000,5000):
        for s in S_PROBES:
            for tau in (F(3,20),F(1,5),F(3,10),F(1,2),F(9,10)):
                if not (BETA<s<tau<1 and s*tau<BETA): continue
                j,b=J(M,s,tau)
                assert j is not None and j>0
                compact.append({'M':M,'s':str(s),'tau':str(tau),'b':b,'sign_J':1})

    out={
      'audit':'A116_COMPACT_UNIFORM_NESTING_BOUNDARY_LAYER_AUDIT',
      'date':'2026-09-15','status':'PASS','symbolic_gates':gates,
      'boundary_layer_certificate':{
        's':'133/1000','lambda':'5/2','d':4,'alpha':'1250/133',
        'log_window_certificate':{'exp2_upper':str(e2_up),'exp21_lower':str(e21_lo),'target':'1000/133','conclusion':'2 < -log(133/1000) < 21/10'},
        'alpha_over_log_bracket':{'lower':str(x_lower),'upper':str(x_upper),'conclusion':'4 < alpha/(-log s) < 5'},
        'exp_minus_alpha_upper':'1/10000','exp_alpha_taylor_partial_N':12,
        'exp_alpha_partial_sum':str(ea_lo),'C':str(C),'Q':str(Q),
        'C_minus_Q_over_10000':str(margin),'limit_sign':'negative','exact_regression':boundary},
      'compact_regression':{'count':len(compact),'all_positive':True,'records':compact},
      'nonclaims':['finite regressions are not premises of the asymptotic theorem','no explicit minimal M0(K) is claimed','no global uniform threshold up to tau=s exists','no A114 lifted active-set generalization is claimed','no physical or ontological interpretation is claimed']}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','symbolic':gates,'boundary_cases':len(boundary),'compact_cases':len(compact),'margin':str(margin)},indent=2))

if __name__=='__main__': main()

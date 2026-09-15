#!/usr/bin/env python3
"""A117 exact parity-resolved boundary-layer phase audit.

Finite reduced-factor signs use Fraction only.  Signs of the limiting phase
function use rational Taylor enclosures for exp(alpha); no floating-point sign
decision is promoted.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

BETA=F(1,8)
DELTA=F(1,1875)
OUT=Path(__file__).resolve().parent/'A117_EXACT_AUDIT_RESULTS_20260915.json'


def sign(x): return 1 if x>0 else -1 if x<0 else 0


def exp_lower(x,N):
    term=F(1); total=F(1)
    for n in range(1,N+1):
        term*=x/n; total+=term
    return total


def exp_upper(x,N):
    term=F(1); total=F(1)
    for n in range(1,N+1):
        term*=x/n; total+=term
    nxt=term*x/(N+1)
    ratio=x/(N+2)
    assert ratio<1
    return total+nxt/(1-ratio)


def symbolic_gates():
    s,alpha,a,beta,delta=sp.symbols('s alpha a beta delta', positive=True)
    r=sp.symbols('r', integer=True)
    q=sp.symbols('q', positive=True)
    B=beta/s+2*delta
    C=1-beta/s-4*delta
    S=1-q-2*delta
    original=alpha*s**(2-r)*q+a*(B-S-B*(alpha+1)*q)
    reduced=-a*C+q*(a*(1-B)+alpha*(s**(2-r)-a*B))

    A,D,C0=sp.symbols('A D C0', positive=True)
    phase=-C0+sp.exp(-alpha)*(A+alpha*D)
    derivative=sp.exp(-alpha)*(D*(1-alpha)-A)

    t,L=sp.symbols('t L', positive=True)
    contact=-(sp.log(1+2*alpha*t))/(2*L*t)
    series=sp.series(contact,t,0,3).removeO().expand()

    return {
        'unified_lambda_identity': sp.simplify(original-reduced)==0,
        'phase_derivative_identity': sp.simplify(sp.diff(phase,alpha)-derivative)==0,
        'contact_leading_term': sp.simplify(series.coeff(t,0)+alpha/L)==0,
        'contact_positive_second_order': sp.simplify(series.coeff(t,1)-alpha**2/L)==0,
    }


def den(M,tau):
    h=M//2; u=tau**h
    return tau-h*u+(h-1)*tau*u


def epsilon(M,tau):
    h=M//2; u=tau**h
    return DELTA*(u if M%2==0 else F(1+tau,2)*u)


def d_value(M,r,tau):
    h=M//2; u=tau**h
    rh=r**h; rh1=rh*r
    Lr=r-h*rh+(h-1)*rh1
    if M%2==0:
        return rh-u*Lr/den(M,tau)
    return F(rh+rh1,2)-F(1+tau,2)*u*Lr/den(M,tau)


def B_value(M,k,r):
    return r**k-F(M-k,M)-F(k,M)*r**M


def delta_B(M,k,r):
    return r**(k+1)-r**k+F(1-r**M,M)


def E(M,k,s,tau):
    eps=epsilon(M,tau)
    hb=F(1+BETA**M,2)-d_value(M,BETA,tau)+2*eps
    hs=F(1+s**M,2)-d_value(M,s,tau)-2*eps
    bb,bt=B_value(M,k,BETA),B_value(M,k,tau)
    xb,xt=delta_B(M,k,BETA),delta_B(M,k,tau)
    A=F(1+tau**M,2)
    X=A*bb-hb*bt
    Y=-A*xb+hb*xt
    W=-bb*xt+bt*xb
    return X*delta_B(M,k,s)+Y*B_value(M,k,s)+W*hs


def b_exact(M,s,tau):
    lo,hi=0,M; target=tau**M
    while lo<hi:
        mid=(lo+hi)//2
        if s**(2*mid)<=target:
            hi=mid
        else:
            lo=mid+1
    return lo


def J(M,s,tau):
    b=b_exact(M,s,tau); h=M//2
    assert b+2<=h-2
    return E(M,b+1,s,tau)-E(M,b+2,s,tau)/tau,b


def phase_bounds(s,lam,r,odd,N=100):
    alpha=lam/(2*s)
    B=BETA/s+2*DELTA
    C=1-BETA/s-4*DELTA
    a=F(1) if not odd else F(1+s,2)
    D=s**(2-r)-a*B
    A=a*(1-B)
    assert C>0 and A>0 and D>0

    elo=exp_lower(alpha,N)
    ehi=exp_upper(alpha,N)
    qlo=1/ehi
    qhi=1/elo
    bracket=A+alpha*D
    lower=(1-s)*(-a*C+qlo*bracket)
    upper=(1-s)*(-a*C+qhi*bracket)
    return lower,upper


def main():
    gates=symbolic_gates()
    assert all(gates.values()),gates

    # Rigorous source-window log enclosure: 2 < -log(s) < 21/10.
    assert exp_upper(F(2),8)<F(1000,133)
    assert exp_lower(F(21,10),8)>F(1000,129)

    # Exact elementary inequalities used in the uniform left-edge proof.
    assert F(359,1000)**2<F(129,1000)
    assert F(365,1000)**2>F(133,1000)
    assert F(5,4)*F(133,1000)<1
    assert F(11,9)*F(133,1000)<1

    even_left_margin=(
        -F(3,50)
        +8*F(129,1000)**2
        -F(42,5)*F(133,1000)**4
    )
    odd_left_margin=(
        -F(567,1000)*F(3,50)
        +9*F(129,1000)**2*F(359,1000)
        -F(567,1000)*F(9,2)*F(21,10)*F(133,1000)**4*F(365,1000)
    )
    assert even_left_margin>0
    assert odd_left_margin>0

    controls=(
        (F(133,1000),F(5,2),2000,-1),
        (F(133,1000),F(5,2),2001,+1),
        (F(133,1000),F(16,5),2000,-1),
        (F(133,1000),F(59,20),2001,-1),
        (F(131,1000),F(22,5),2000,+1),
        (F(133,1000),F(4,1),2001,-1),
        (F(129,1000),F(13,5),2000,-1),
        (F(129,1000),F(13,5),2001,+1),
    )

    records=[]
    for s,lam,M,expected in controls:
        tau=s+lam/M
        j,b=J(M,s,tau)
        r=M//2-b
        finite_sign=sign(j)
        lower,upper=phase_bounds(s,lam,r,M%2==1)
        limit_sign=+1 if lower>0 else -1 if upper<0 else 0
        assert finite_sign==expected
        assert limit_sign==expected
        records.append({
            's':str(s),'lambda':str(lam),'M':M,
            'parity':'odd' if M%2 else 'even',
            'b':b,'r':r,
            'finite_J_sign':finite_sign,
            'rationally_certified_limit_sign':limit_sign,
        })

    output={
        'audit':'A117_BOUNDARY_LAYER_PHASE_CLASSIFICATION_AUDIT',
        'date':'2026-09-15',
        'status':'PASS',
        'symbolic_gates':gates,
        'source_log_window':'2 < -log(s) < 21/10 for 129/1000 <= s <= 133/1000',
        'even_left_endpoint_margin':str(even_left_margin),
        'odd_left_endpoint_margin':str(odd_left_margin),
        'exact_fraction_controls':records,
        'control_count':len(records),
        'all_controls_pass':True,
        'nonclaims':[
            'finite controls are regression/falsification evidence only',
            'the next-order sign on Lambda=0 critical surfaces is not classified',
            'no minimal finite M realization threshold is claimed',
            'no target-deformed A114 lifted staircase is claimed',
            'no physical or ontological interpretation is claimed',
        ],
    }
    OUT.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print(json.dumps({
        'status':'PASS',
        'symbolic_gates':gates,
        'control_count':len(records),
        'even_left_margin':str(even_left_margin),
        'odd_left_margin':str(odd_left_margin),
    },indent=2))


if __name__=='__main__':
    main()

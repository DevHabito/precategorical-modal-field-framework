#!/usr/bin/env python3
"""Exact finite LP acceptance gate for the A115-A122 research contracts.

Models:
 F2: target normalization, common mass/mean, nonnegative atoms,
     and BOTH sides of the beta and s transform bands.
 F3: the same constraints PLUS both sides of the gamma=1/16 band.

The compressed C2(k) architecture is NOT treated as a full LP theorem.
We validate its actual atom masses against both LPs.

Includes a generic fully explicit dual-feasibility / weak-duality check.
All comparisons use fractions.Fraction: no silent epsilons or float solvers.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from typing import Mapping
import a115_independent_compressed_adjacent_identity_20261107 as source

BETA = F(1, 8)
GAMMA = F(1, 16)
DELTA = F(1, 1875)


@dataclass(frozen=True)
class LP:
    M: int
    s: F
    tau: F
    three_bands: bool = True

    def __post_init__(self):
        if not (self.M >= 4 and F(129, 1000) <= self.s <= F(133, 1000)
                and BETA < self.s < self.tau < 1):
            raise ValueError('Invalid A115 contract domain')

    def ell(self):
        h=self.M//2
        return self.tau**h * (F(1) if self.M%2==0 else (1+self.tau)/2)

    def eps(self):
        return DELTA*self.ell()

    def nodes(self):
        return (self.s, BETA, GAMMA) if self.three_bands else (self.s, BETA)


def weighted_sum(weights: Mapping[int, F], r: F):
    return sum((F(v)*r**int(x) for x,v in weights.items()), F(0))


def audit_primal(contract: LP, p: Mapping[int,F],
                 q: Mapping[int,F], t: F):
    """Return all failed gate names instead of accepting partial candidates."""
    faults=[]
    M=contract.M
    for tag,weights in (('p',p),('q',q)):
        if any(type(x) is not int or x<0 or x>M for x in weights):
            faults.append(f'{tag}:support')
        if any(v<0 for v in weights.values()):
            faults.append(f'{tag}:nonnegative')
    if t<=0:
        faults.append('t:positive')
    if sum(p.values(),F(0))!=t:
        faults.append('p:mass')
    if sum(q.values(),F(0))!=t:
        faults.append('q:mass')
    if sum((x*v for x,v in p.items()),F(0))!=F(M,2)*t:
        faults.append('p:mean')
    if sum((x*v for x,v in q.items()),F(0))!=F(M,2)*t:
        faults.append('q:mean')
    if weighted_sum(q,contract.tau)!=1:
        faults.append('q:target')
    for node in contract.nodes():
        gap=weighted_sum(p,node)-weighted_sum(q,node)
        if gap>2*contract.eps()*t:
            faults.append(f'band+:{node}')
        if -gap>2*contract.eps()*t:
            faults.append(f'band-:{node}')
    return faults


@dataclass(frozen=True)
class Dual:
    ap:F
    aq:F
    bp:F
    bq:F
    v:F
    u:Mapping[F,F]
    w:Mapping[F,F]


def audit_dual(contract: LP, d: Dual):
    """Pointwise dual reduced costs, the t row, and nonnegative band multipliers."""
    faults=[]
    nodes=contract.nodes()
    if set(d.u)!=set(nodes) or set(d.w)!=set(nodes):
        return ['dual:node-keys']
    if any(d.u[r]<0 or d.w[r]<0 for r in nodes):
        faults.append('dual:band-multiplier')
    shift=sum((d.u[r]+d.w[r] for r in nodes),F(0))
    trow=-d.ap-d.aq-2*contract.eps()*shift
    if trow<0:
        faults.append('dual:t-row')
    for x in range(contract.M+1):
        centered=F(x)-F(contract.M,2)
        bands=sum(((d.u[r]-d.w[r])*r**x for r in nodes),F(0))
        p_rhs=d.ap+d.bp*centered+bands
        q_rhs=d.aq+d.bq*centered+d.v*contract.tau**x-bands
        if p_rhs<contract.tau**x:
            faults.append(f'dual:p:{x}')
        if q_rhs<0:
            faults.append(f'dual:q:{x}')
    return faults


def loose_upper_certificate(contract: LP):
    """Valid finite universal bound, intentionally NOT a tight KKT optimum."""
    nodes=contract.nodes()
    z={r:F(0) for r in nodes}
    return Dual(F(1),F(-1),F(0),F(0),contract.tau**(-contract.M),z,z.copy())


def centered_equal(M:int,tau:F):
    """An unrestricted all-band feasible witness, independent of compressed C2."""
    h=M//2
    if M%2:
        each=1/(tau**h*(1+tau))
        w={h:each,h+1:each}
    else:
        w={h:tau**(-h)}
    return w,w.copy(),sum(w.values(),F(0))


def controls():
    feasible=dual_ok=mutation=0
    for M in (4,5,24,25,40,41,100,101,521,522):
        for tau in (F(14,100),F(1,5),F(1,2),F(4,5)):
            s=F(129,1000)
            assert s<tau
            p,q,t=centered_equal(M,tau)
            for three in (False,True):
                c=LP(M,s,tau,three)
                assert not audit_primal(c,p,q,t)
                assert weighted_sum(p,tau)==1
                d=loose_upper_certificate(c)
                assert not audit_dual(c,d), audit_dual(c,d)[:3]
                assert weighted_sum(p,tau)<=d.v
                feasible+=1
                dual_ok+=1
    # Positive / negative mutants from an independent feasible even-support point.
    c=LP(24,F(129,1000),F(1,2),True)
    p,q,t=centered_equal(c.M,c.tau)
    mutations=[
        ({12:-F(1)}, q,t,'p:nonnegative'),
        ({12:t+1},q,t,'p:mass'),
        ({11:t},q,t,'p:mean'),
        (p,{12:2*t},2*t,'p:mass'),
        ({12:2*t},{12:2*t},2*t,'q:target'),
    ]
    for pp,qq,tt,expected in mutations:
        faults=audit_primal(c,pp,qq,tt)
        assert expected in faults,(expected,faults)
        mutation+=1
    d=loose_upper_certificate(c)
    assert 'dual:p:0' in audit_dual(c,Dual(F(0),d.aq,d.bp,d.bq,d.v,d.u,d.w))
    mutation+=1
    assert 'dual:q:24' in audit_dual(c,Dual(d.ap,d.aq,d.bp,d.bq,F(1),d.u,d.w))
    mutation+=1
    assert 'dual:t-row' in audit_dual(c,Dual(d.ap,F(0),d.bp,d.bq,d.v,d.u,d.w))
    mutation+=1

    # Crucial adversarial test: one real compressed candidate solves F2,
    # but not F3 when the inherited gamma band is imposed.
    s=F(129,1000);tau=F(1,2);M=24;k=5
    sol=source.solve(M,k,s,tau)
    p={int(x):v for x,v in source.pweights(M,k,sol['t'],sol['z'])}
    q={int(x):v for x,v in source.qcoords(M,tau,sol['t'])}
    assert not audit_primal(LP(M,s,tau,False),p,q,sol['t'])
    failures=audit_primal(LP(M,s,tau,True),p,q,sol['t'])
    assert any(x.startswith('band') and str(GAMMA) in x for x in failures),failures

    # Another real algebraic adjacent candidate has negative p0 and is
    # rejected already in the relaxed two-band LP.
    sol2=source.solve(M,k+1,s,tau)
    p2={int(x):v for x,v in source.pweights(M,k+1,sol2['t'],sol2['z'])}
    q2={int(x):v for x,v in source.qcoords(M,tau,sol2['t'])}
    assert 'p:nonnegative' in audit_primal(LP(M,s,tau,False),p2,q2,sol2['t'])

    print(f'PASS: F2/F3 complete primal gate on {feasible} centered exact cases')
    print(f'PASS: dual weak upper-bound row checks on {dual_ok} exact cases')
    print(f'PASS: {mutation} negative-control mutations rejected')
    print('PASS: C2(5) feasible for F2 but violates F3 gamma; C2(6) violates P nonnegativity')
    print('NONCLAIM: loose dual bound is not an optimum/KKT certificate')


if __name__=='__main__':
    controls()

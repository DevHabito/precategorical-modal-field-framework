#!/usr/bin/env python3
"""Exact finite F3 optimum and uniqueness certificate at one fixed contract.

M=4, s=129/1000, tau=1/2, beta=1/8, gamma=1/16,
epsilon=tau**2/1875=1/7500.

A floating-point LP solver was used ONLY to propose the sparse basis:
  positive primal variables P_0,P_1,P_2,P_4,Q_1,Q_3,t;
  active inequality rows s+ and gamma-.

This published checker uses NO numerical solver: it constructs those
7+7 primal/dual unknowns by an exact Fraction Gaussian elimination,
checks ALL original equalities, nonnegativity, all six band rows,
ALL primal and dual atom inequalities, equality of objectives, and
strict complementary conditions sufficient for uniqueness.

The result proves ONE finite rational contract, not the global
A115-A122 optimization or any asymptotic theorem.
"""
from fractions import Fraction as F
import a115_explicit_full_primal_and_dual_gate_20261107 as independent

if not __debug__:
    raise RuntimeError("Audit assertions cannot be disabled")

M=4
S=F(129,1000)
TAU=F(1,2)
BETA=F(1,8)
GAMMA=F(1,16)
EPS=F(1,1875)*TAU**(M//2)
DIM=2*(M+1)+1
BASIS=(0,1,2,4,6,8,10)   # P0,P1,P2,P4,Q1,Q3,t
ACTIVE_BANDS=(0,5)        # s+ and gamma-
EXPECTED_OBJECTIVE=F(550870246006266889,533058861574687500)


def exact_solve_square(coeffs,rhs):
    """Fraction Gaussian elimination with a nonzero determinant witness."""
    n=len(coeffs)
    assert len(rhs)==n and all(len(row)==n for row in coeffs)
    rows=[[F(v) for v in row]+[F(b)] for row,b in zip(coeffs,rhs)]
    determinant=F(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if rows[i][k]!=0),None)
        assert pivot is not None,("singular basis",k)
        if pivot!=k:
            rows[k],rows[pivot]=rows[pivot],rows[k]
            determinant=-determinant
        scale=rows[k][k]
        determinant*=scale
        rows[k]=[v/scale for v in rows[k]]
        for i in range(n):
            if i!=k and rows[i][k]!=0:
                factor=rows[i][k]
                rows[i]=[v-factor*w for v,w in zip(rows[i],rows[k])]
    assert determinant!=0
    return [row[-1] for row in rows],determinant


def equality_row(measure,mean=False):
    row=[F(0)]*DIM
    for i in range(M+1):
        row[measure*(M+1)+i]=(F(i)-F(M,2)) if mean else F(1)
    if not mean:
        row[-1]=-F(1)
    return row


def build_exact_model():
    # Equality rows: P mass, Q mass, P centered mean, Q centered
    # mean, Q target normalization.
    eq=[equality_row(0),equality_row(1),
        equality_row(0,True),equality_row(1,True)]
    target=[F(0)]*DIM
    for i in range(M+1):
        target[M+1+i]=TAU**i
    eq.append(target)
    rhs=[F(0),F(0),F(0),F(0),F(1)]

    # Each observation contributes separately to its + and - rows.
    bands=[]
    names=[]
    for name,r in (("s",S),("beta",BETA),("gamma",GAMMA)):
        for orientation in (1,-1):
            row=[F(0)]*DIM
            for i in range(M+1):
                row[i]=orientation*r**i
                row[M+1+i]=-orientation*r**i
            row[-1]=-2*EPS
            bands.append(row)
            names.append((name,orientation))
    objective=[TAU**i for i in range(M+1)]+[F(0)]*(M+2)
    assert len(eq)==5 and len(bands)==6 and len(objective)==DIM
    return eq,rhs,bands,names,objective


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def verify():
    assert EPS==F(1,7500)
    eq,rhs,bands,names,objective=build_exact_model()
    active_rows=eq+[bands[j] for j in ACTIVE_BANDS]

    # Seven nonsingular equations for seven positive primal variables.
    basis_matrix=[[row[j] for j in BASIS] for row in active_rows]
    positive_p,det_primal=exact_solve_square(
        basis_matrix,rhs+[F(0),F(0)])
    assert all(v>0 for v in positive_p)

    primal=[F(0)]*DIM
    for j,v in zip(BASIS,positive_p):
        primal[j]=v
    assert all(dot(row,primal)==b for row,b in zip(eq,rhs))
    band_slacks=[-dot(row,primal) for row in bands]
    assert all(z>=0 for z in band_slacks)
    assert tuple(i for i,z in enumerate(band_slacks) if z==0)==ACTIVE_BANDS
    assert all(band_slacks[j]>0 for j in range(6) if j not in ACTIVE_BANDS)

    # Seven stationarity equations on the positive primal columns
    # determine 5 unrestricted equality multipliers and 2 active,
    # nonnegative band multipliers.
    dual_matrix=[[row[j] for row in active_rows] for j in BASIS]
    dual,det_dual=exact_solve_square(
        dual_matrix,[objective[j] for j in BASIS])
    assert det_primal==det_dual
    assert all(u>0 for u in dual[5:])

    # No unused atom or the common mass variable is silently omitted.
    reduced=[dot(dual,[row[j] for row in active_rows])-objective[j]
             for j in range(DIM)]
    assert all(v>=0 for v in reduced)
    assert tuple(j for j,v in enumerate(reduced) if v==0)==BASIS
    assert all(reduced[j]>0 for j in range(DIM) if j not in BASIS)

    primal_value=dot(objective,primal)
    dual_value=dot(dual[:5],rhs)
    assert primal_value==dual_value==EXPECTED_OBJECTIVE
    assert primal_value>1

    # Independent F3 primal validator using different row construction.
    p={x:primal[x] for x in range(M+1) if primal[x]}
    q={x:primal[M+1+x] for x in range(M+1) if primal[M+1+x]}
    t=primal[-1]
    contract=independent.LP(M,S,TAU,True)
    assert not independent.audit_primal(contract,p,q,t)
    assert independent.weighted_sum(p,TAU)==primal_value

    # Independent explicit dual P/Q/t-row validator, with missing
    # bands present as genuine zero multipliers.
    u={r:F(0) for r in contract.nodes()}
    w={r:F(0) for r in contract.nodes()}
    assert names[ACTIVE_BANDS[0]]==("s",1)
    assert names[ACTIVE_BANDS[1]]==("gamma",-1)
    u[S]=dual[5]
    w[GAMMA]=dual[6]
    dual_obj=independent.Dual(dual[0],dual[1],dual[2],
                              dual[3],dual[4],u,w)
    assert not independent.audit_dual(contract,dual_obj)

    # Strict primal/dual complementary slackness plus nonsingular
    # active submatrix proves UNIQUE optimality for THIS finite LP:
    # any other optimizer must have exactly the same zero atoms
    # and the same two active band equalities; the matrix then
    # forces the identical seven positive coordinates.
    assert set(BASIS)=={i for i,v in enumerate(primal) if v>0}
    assert len(BASIS)==len(active_rows)==7
    assert det_primal!=0

    # Mutations are supposed to be rejected.
    wrong_p=p.copy()
    wrong_p[0]=F(-1)
    assert "p:nonnegative" in independent.audit_primal(
        contract,wrong_p,q,t)
    wrong_dual=independent.Dual(
        dual[0],dual[1],dual[2],dual[3],F(0),u,w)
    assert independent.audit_dual(contract,wrong_dual)

    print("PASS: fixed full F3 finite LP, exact optimality AND uniqueness certificate")
    print("contract: M=4, s=129/1000, tau=1/2, beta=1/8, gamma=1/16, eps=1/7500")
    print("P positive indices:",[j for j in range(M+1) if primal[j]>0])
    print("Q positive indices:",[j for j in range(M+1) if primal[M+1+j]>0])
    print("active bands:",[names[j] for j in ACTIVE_BANDS])
    print("exact optimal objective:",primal_value)
    print("exact dual equality: PASS")
    print("nonzero exact active-basis determinant:",det_primal)
    print("all inactive band slacks and missing-atom reduced costs: STRICTLY POSITIVE")
    print("NOT CLAIMED: uniform M theorem, A115 compressed support optimality, or Lean instantiation")


if __name__=="__main__":
    verify()

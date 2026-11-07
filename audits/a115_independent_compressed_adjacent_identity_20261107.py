#!/usr/bin/env python3
"""Independent rational reconstruction of the compressed adjacent objective.

This script starts from the two active *band equalities* and the
original three-site P/Q transform formulas, not from a precomputed E sign.
It verifies the Cramer solves and the exact oriented identity:
  (V[k+1] - V[k]) * Delta[k] * Delta[k+1] = -Z * E[k].
No floating-point comparisons are used.

The active-band solutions need not satisfy every other LP constraint.
A separate synthetic 2x2 example shows why the sign hypotheses matter.
"""
from fractions import Fraction as F

BETA=F(1,8)
DELTA=F(1,1875)

def b_exact(M,s,tau):
    lo,hi=0,M
    while lo<hi:
        mid=(lo+hi)//2
        if s**(2*mid)<=tau**M:hi=mid
        else:lo=mid+1
    return lo

def qcoords(M,tau,t):
    h=M//2
    u=tau**h
    D=tau-h*u+(h-1)*tau*u
    assert D>0
    a=F(1) if M%2==0 else (1+tau)/2
    q1=(1-a*u*t)/D
    if M%2:
        return ((1,q1),(h,t/2-h*q1),(h+1,t/2+(h-1)*q1))
    return ((1,q1),(h,t-h*q1),(h+1,(h-1)*q1))

def transform(weights,r):
    return sum((v*r**j for j,v in weights),F(0))

def qcoeff(M,tau,r):
    baseline=transform(qcoords(M,tau,F(0)),r)
    slope=transform(qcoords(M,tau,F(1)),r)-baseline
    return baseline,slope

def pweights(M,k,t,z):
    return ((0,t/2-F(M-k,M)*z),(k,z),(M,t/2-F(k,M)*z))

def basis(M,k,r):
    return r**k-F(M-k,M)-F(k,M)*r**M

def solve(M,k,s,tau):
    h=M//2
    eps=DELTA*tau**h*(F(1) if M%2==0 else (1+tau)/2)
    Cb,Db=qcoeff(M,tau,BETA)
    Cs,Ds=qcoeff(M,tau,s)
    Hb=F(1+BETA**M,2)-Db+2*eps
    Hs=F(1+s**M,2)-Ds-2*eps
    A=F(1+tau**M,2)
    Bbeta=basis(M,k,BETA)
    Bs=basis(M,k,s)
    Bt=basis(M,k,tau)
    determinant=Bbeta*Hs-Bs*Hb
    Z=Cb*Hs-Cs*Hb
    assert determinant!=0
    t=(Bbeta*Cs-Bs*Cb)/determinant
    z=Z/determinant
    P=pweights(M,k,t,z)
    Q=qcoords(M,tau,t)
    assert sum(v for _,v in P)==t
    assert sum(j*v for j,v in P)==F(M,2)*t
    assert sum(v for _,v in Q)==t
    assert sum(j*v for j,v in Q)==F(M,2)*t
    assert transform(Q,tau)==1
    # Actual active β lower band and s upper band.
    assert transform(P,BETA)-transform(Q,BETA)==-2*eps*t
    assert transform(P,s)-transform(Q,s)==2*eps*t
    value=transform(P,tau)
    assert value==A*t+Bt*z
    return dict(value=value,det=determinant,Z=Z,t=t,z=z,
                feasible_P=all(v>=0 for _,v in P),
                feasible_Q=all(v>=0 for _,v in Q),
                A=A,Bbeta=Bbeta,Bs=Bs,Bt=Bt,Hb=Hb,Hs=Hs)

def verify_pair(M,k,s,tau):
    left=solve(M,k,s,tau);right=solve(M,k+1,s,tau)
    assert left['Z']==right['Z']
    db=right['Bbeta']-left['Bbeta']
    ds=right['Bs']-left['Bs']
    dt=right['Bt']-left['Bt']
    A=left['A'];Hb=left['Hb'];Hs=left['Hs']
    bb=left['Bbeta'];bs=left['Bs'];bt=left['Bt']
    E=(A*bb-Hb*bt)*ds+(-A*db+Hb*dt)*bs+(-bb*dt+bt*db)*Hs
    dV=right['value']-left['value']
    factor=left['Z']
    assert dV*left['det']*right['det']==-factor*E
    oriented=(factor<0 and left['det']*right['det']>0)
    if oriented:
        assert (dV>0)==(E>0)
        assert (dV<0)==(E<0)
        assert (dV==0)==(E==0)
    both_nonnegative=(left['feasible_P'] and left['feasible_Q'] and
                     right['feasible_P'] and right['feasible_Q'])
    return oriented,both_nonnegative

def synthetic_orientation_counterexample():
    # A conditional sign theorem is mandatory: reversing Z reverses
    # the sign, even when both Cramer determinants are positive.
    Bb,Bs,Bt=F(2),F(1),F(0)
    Db,Ds,Dt=F(1),F(1,2),F(-1)
    Hb=Hs=A=F(1)
    Cb,Cs=F(3),F(2)
    D=Bb*Hs-Bs*Hb
    Dnext=(Bb+Db)*Hs-(Bs+Ds)*Hb
    Z=Cb*Hs-Cs*Hb
    N=A*(Bb*Cs-Bs*Cb)+Bt*Z
    Nnext=A*((Bb+Db)*Cs-(Bs+Ds)*Cb)+(Bt+Dt)*Z
    E=(A*Bb-Hb*Bt)*Ds+(-A*Db+Hb*Dt)*Bs+(-Bb*Dt+Bt*Db)*Hs
    V=N/D;Vnext=Nnext/Dnext
    assert Z>0 and D*Dnext>0 and E>0 and Vnext<V
    assert (Vnext-V)*(D*Dnext)==-Z*E
    return "E positive / V decrease when Z positive (outside original model assumptions)"

def main():
    counts=dict(identities=0,oriented=0,both_three_site_nonnegative=0,other_orientation=0)
    for M in (24,25,40,41,100,101,521,522):
        for s in (F(129,1000),F(131,1000),F(133,1000)):
            for tau in (F(14,100),F(1,5),F(1,2),F(4,5)):
                b=b_exact(M,s,tau)
                for k in sorted({max(2,b-1),b,b+1}):
                    if k+1>M//2-2 or k<2:
                        continue
                    oriented,nonnegative=verify_pair(M,k,s,tau)
                    counts["identities"]+=1
                    counts["oriented"]+=int(oriented)
                    counts["both_three_site_nonnegative"]+=int(nonnegative)
                    counts["other_orientation"]+=int(not oriented)
    assert counts["identities"]>0
    print("PASS: exact primal active-band Cramer/adjacent identity checks:",counts)
    print("PASS: synthetic sign orientation control:",synthetic_orientation_counterexample())

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Rational monomial certificate of A115 source-jet O(x²) bound.

SymPy 1.14.0, exact Fraction. No pointwise numerical sample is accepted
as a proof. This complements, not replaces, analytic Taylor estimates.
"""
import sympy as S
from fractions import Fraction as F
if not __debug__: raise RuntimeError("Assertions must be active")
x,s,alpha,beta,delta,e,z,r=S.symbols("x s alpha beta delta e z r")
H=8**18
bounds=(F(1,1000),F(1),F(45),F(1),F(1),F(1),F(H),F(19))
for odd in (False,True):
    sigma=S.Rational(1,2) if odd else S.Integer(0)
    a=(1+s)/2 if odd else S.Integer(1)
    tau=s*(1+2*alpha*x)
    at=(1+tau)/2 if odd else S.Integer(1)
    b=sigma+r-1
    eta_h=alpha**2+2*sigma*alpha
    eta_k=alpha**2+2*alpha*b
    fh=e*(1+eta_h*x)
    fk=e*(1+eta_k*x)
    U=at*(beta/tau+2*delta)
    g0=s*alpha*(s-1)+s*s-s
    g1=2*s*alpha*(b*(s-1)+1)
    bracket=(alpha*s*(1-s)*z*fh+
             (1-tau)*(at*((beta-s)/tau+4*delta)+a*fh)+
             U*fk/tau*(g0+x*g1))
    B=beta/s+2*delta
    C=1-beta/s-4*delta
    lam=(1-s)*(-a*C+e*(a*(1-B)+alpha*(s*z-a*B)))
    B1=2*sigma*alpha*s*B-2*a*alpha*beta/s
    S1=2*sigma*alpha*s*(1-2*delta)-2*a*alpha-a*e*eta_h
    G2=2*alpha*(1+(1-s)*(alpha+2-sigma-r))
    xi=((1-s)*alpha*s*z*e*eta_h+
        e*(a*B*G2-(1-s)*(alpha+1)*(B1+a*B*eta_k))+
        (1-s)*(B1-S1)-2*alpha*s*a*(B-(1-e-2*delta)))
    assert S.cancel(bracket.subs(x,0)-lam)==0
    assert S.cancel(S.diff(bracket,x).subs(x,0)-xi)==0
    numerator,denominator=S.fraction(
        S.cancel(s*s*(1+2*alpha*x)**2*(bracket-lam-x*xi)))
    assert denominator==1
    poly=S.Poly(S.expand(numerator),x,s,alpha,beta,delta,e,z,r)
    assert all(powers[0]>=2 for powers,coef in poly.terms())
    upper=F(0)
    for powers,coef in poly.terms():
        term=F(abs(S.Rational(coef)))
        for i,(power,limit) in enumerate(zip(powers,bounds)):
            term*=limit**(power-2 if i==0 else power)
        upper+=term
    upper/=F(129,1000)**2
    assert upper<10_000_000_000
    print("PASS",("odd" if odd else "even"),
          len(poly.terms()),"monomials; jet bound ceiling",
          upper.numerator//upper.denominator+1)
H=8**18
assert (46*H+768)*558_000_000<500_000_000_000*H
rho_to_cubic=12*99**3
assert rho_to_cubic==11_643_588
assert 510_000_000_000*H+750*H*H*rho_to_cubic < 100_000_000_000*H*H
print("PASS explicit source-derived cubic coefficient C=10^11*(8^18)^2")
print("NOT a complete Lean analytic remainder proof or full F3 optimality")

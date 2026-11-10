#!/usr/bin/env python3
"""Rational proof-constant gates for the generic collision-power Taylor bound.

Only checks exact constant inequalities; the alternating-logarithm
and exponential Taylor remainder lemmas remain analytic obligations.
"""
from fractions import Fraction as F
from math import factorial
if not __debug__: raise RuntimeError("Assertions disabled")
X=F(1,1000)
ALPHA=45
SHIFT=F(37,2)  # sigma+r-1 <= 18.5
A=ALPHA**2+2*SHIFT*ALPHA
B=F(4,3)*ALPHA**3+2*SHIFT*ALPHA**2
R=2*ALPHA**4+F(8,3)*SHIFT*ALPHA**3
assert (A,B,R)==(3690,196425,12696750)
assert 2*ALPHA*X<=F(9,100)
assert A+B*X+R*X*X<3900
assert B+R*X<209122
assert 3900+A==7590
# Exact upper enclosure for exp(4) using sum to n=10 and a ratio tail.
partial=sum((F(4)**n/F(factorial(n)) for n in range(11)),F(0))
first=F(4)**11/F(factorial(11))
tail=first/(1-F(4,12))
assert partial+tail<55
exp_rem=F(55)*3900**3/F(6)
quadratic_diff=F(209122)*7590/F(2)
assert exp_rem==543757500000
assert quadratic_diff==793617990
assert R+exp_rem+quadratic_diff==544563814740<550000000000
quadratic_coeff=B+F(A*A,2)
assert quadratic_coeff==7004475
assert quadratic_coeff+F(550000000000,1000)==557004475<558000000
print("PASS generic collision exponent-shift and Taylor constant gates")
print("PASS rational exp(4)<55 enclosure, no floating point")
print("Bounds: order-3 <= 5.5e11*x^3; linear-jet <= 5.58e8*x^2")
print("Analytic remainder inequalities and Lean replay still pending.")

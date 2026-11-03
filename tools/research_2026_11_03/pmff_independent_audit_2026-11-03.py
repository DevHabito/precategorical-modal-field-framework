"""Independent exact rational audit of C2/F3 witness, 2026-11-03.

No imports from the project, and no floating approximations.
"""
from fractions import Fraction as F
from itertools import count
import sympy as sp

x=sp.symbols('x')
p=(F(15,64),F(22,64),F(7,64),F(20,64))
q=(F(17,64),F(10,64),F(25,64),F(12,64))

assert all(v>0 for v in p+q)
assert sum(p)==sum(q)==1
assert sum(i*v for i,v in enumerate(p))==sum(i*v for i,v in enumerate(q))==F(3,2)
def moment(weights,t): return sum(w*t**i for i,w in enumerate(weights))
initial=F(1,4); transformed=F(1,2)
assert moment(p,initial)==moment(q,initial)==F(85,256)
assert (moment(p,transformed),moment(q,transformed))==(F(121,256),F(119,256))
assert moment(p,transformed)-moment(q,transformed)==F(1,128)
D=sum(sp.Rational((a-b).numerator,(a-b).denominator)*x**i for i,(a,b) in enumerate(zip(p,q)))
expected=(x-1)**2*(x-sp.Rational(1,4))/8
assert sp.expand(D-expected)==0
assert D.subs(x,1)==0 and sp.diff(D,x).subs(x,1)==0 and D.subs(x,sp.Rational(1,4))==0
# The entire vector space of cubic differences obeying the three equalities is dimension one.
B=sp.Matrix([[1,1,1,1],[0,1,2,3],[1,sp.Rational(1,4),sp.Rational(1,16),sp.Rational(1,64)]])
assert B.rank()==3
null=B.nullspace()
assert len(null)==1 and B*null[0]==sp.zeros(3,1)
# negative controls: perturb exactly one numerator -> initial moment agreement must break
p_perturbed=tuple((p[i]+(F(1,64) if i==0 else (-F(1,64) if i==1 else 0))) for i in range(4))
assert sum(p_perturbed)==1
assert moment(p_perturbed,initial)!=moment(q,initial)
# Distinct transformed moments imply distinct scores as exp(-lambda*shift)>0 and log injective.
print('AUDIT-ID: F3-2026-11-03 (standalone Python, sympy + fractions)')
print('cubic coefficient identity: PASS')
print('constraint nullspace dimension =', len(null))
print('positivity, total mass, mean: PASS')
print('initial exact moment:', moment(p,initial))
print('contracted exact moments:', moment(p,transformed), moment(q,transformed))
print('strict rational difference:', moment(p,transformed)-moment(q,transformed))
print('negative perturbation control: PASS')
print('scope: exact rational witness and algebra; no Lean compilation')

# Standalone symbolic/rational A113 checks from public formulas.
s,b,t,z=sp.symbols('s b t z')
xx=b*s; yy=b*t; ww=s*t
lhs=(s-b)*xx/(1-xx*z)+(b-t)*yy/(1-yy*z)+(t-s)*ww/(1-ww*z)
rhs=(s-b)*(t-b)*(t-s)/((1-xx*z)*(1-yy*z)*(1-ww*z))
assert sp.cancel(lhs-rhs)==0
L=F(1,2)*(F(129,1000)-F(1,8))*(F(1,2)-F(1,8))*(F(1,2)-F(133,1000))*F(129,2000)**28
assert L>F(20,2**260)
assert 18+F(267,521)<20
print('A113 symbolic generating-function identity: PASS')
print('A113 exact small-left margin and worst-case arithmetic cap: PASS')
print('SCOPE: mathematical subclaims only; cannot certify Lean modules or full A113')
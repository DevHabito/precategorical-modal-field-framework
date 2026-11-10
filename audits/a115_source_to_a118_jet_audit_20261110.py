#!/usr/bin/env python3
"""Source-derived A117/A118 first jet of the exact normalized A115 core.

SymPy 1.14.0. z=s^(1-r) is independent during the polynomial audit;
the identity s*z=s^(2-r) is used only in the published coefficient.
No numerical fitting and no assumed A118 sign theorem.
"""
import sympy as S
if not __debug__:
    raise RuntimeError("Assertions disabled")
x,s,alpha,beta,delta,e,z,r=S.symbols("x s alpha beta delta e z r", real=True)
for odd in (False, True):
    sigma=S.Rational(1,2) if odd else S.Integer(0)
    a=(1+s)/2 if odd else S.Integer(1)
    tau=s*(1+2*alpha*x)
    a_tau=(1+tau)/2 if odd else S.Integer(1)
    b=sigma+r-1
    eta_h=alpha**2+2*sigma*alpha
    eta_k=alpha**2+2*alpha*b
    f_h=e*(1+eta_h*x)
    f_k=e*(1+eta_k*x)
    U0=a_tau*(beta/tau+2*delta)
    g0=s*alpha*(s-1)+s*s-s
    g1=2*s*alpha*(b*(s-1)+1)
    bracket=(alpha*s*(1-s)*z*f_h+
             (1-tau)*(a_tau*((beta-s)/tau+4*delta)+a*f_h)+
             U0*f_k/tau*(g0+x*g1))
    B=beta/s+2*delta
    C=1-beta/s-4*delta
    phase=(1-s)*(-a*C+e*(a*(1-B)+alpha*(s*z-a*B)))
    B1=2*sigma*alpha*s*B-2*a*alpha*beta/s
    T0=1-2*delta
    S0=1-e-2*delta
    S1=2*sigma*alpha*s*T0-2*a*alpha-a*e*eta_h
    G2=2*alpha*(1+(1-s)*(alpha+2-sigma-r))
    xi=((1-s)*alpha*s*z*e*eta_h+
        e*(a*B*G2-(1-s)*(alpha+1)*(B1+a*B*eta_k))+
        (1-s)*(B1-S1)-2*alpha*s*a*(B-S0))
    assert S.cancel(bracket.subs(x,0)-phase)==0
    assert S.cancel(S.diff(bracket,x).subs(x,0)-xi)==0
    residual=S.cancel(bracket-phase-x*xi)
    n,d=S.fraction(residual)
    pn=S.Poly(n,x)
    assert pn.coeff_monomial(1)==0 and pn.coeff_monomial(x)==0
    print("PASS source-derived Lambda and Xi:", "odd" if odd else "even")
    print("PASS exact rational jet residual divisible by x^2")
print("No Lean remainder theorem or global LP optimization claimed.")

#!/usr/bin/env python3
"""Independent exact symbolic audit for A115 full finite-power correction.

Requires SymPy. This reproduces the cofactor directly and verifies that
every vb,vs,vt contribution is retained; it is not a uniform remainder bound.
"""
import sympy as sp

if not __debug__:
    raise RuntimeError("Run without -O; assertions are part of the audit.")
x,q,u,b,s,t,K,W,T,U,V,vb,vs,vt=sp.symbols(
    "x q u beta s tau K W T U V vb vs vt")

def cofactor(q0,k0,w0,t0,full):
    v_b=vb if full else 0
    v_s=vs if full else 0
    v_t=vt if full else 0
    A=(1+v_t)/2
    Hb=sp.Rational(1,2)+u*U
    Hs=sp.Rational(1,2)+u*V
    Bb=u*k0-1+q0*(1-v_b)
    Bs=u*w0-1+q0*(1-v_s)
    Bt=u*t0-1+q0*(1-v_t)
    Db=(b-1)*u*k0+x*(1-v_b)
    Ds=(s-1)*u*w0+x*(1-v_s)
    Dt=(t-1)*u*t0+x*(1-v_t)
    return ((A*Bb-Hb*Bt)*Ds+(-A*Db+Hb*Dt)*Bs
            +(-Bb*Dt+Bt*Db)*Hs)

def adjacent(full):
    return 2*(t*cofactor(q,K,W,T,full)-
              cofactor(q+x,b*K,s*W,t*T,full))
def P(a):
    return q*(a-1)*(a-t)+x*(a*a-2*a+t)
def Q(a):
    return (a-1)*(a-t)

c0=x*(t-1)*vt*(vs-vb)
c1=(vb*((t-1)*x*(2*V-T*t)+W*P(s))+
    vs*((t-1)*x*(T*t-2*U)-K*P(b))+
    vt*(K*(2*P(b)-Q(b))+2*x*(t-1)*(U-V)+W*(Q(s)-2*P(s)))+
    vb*vt*W*P(s)-vs*vt*K*P(b))
c2=(2*T*t*x*(t-1)*(vs*U-vb*V)+
    vt*(2*K*V*P(b)+K*W*(b-s)*(b*s-t)-2*U*W*P(s)))
difference=sp.expand(adjacent(True)-adjacent(False))
assert sp.expand(difference-c0-u*c1-u*u*c2)==0
assert sp.expand(difference.subs(u,0)-c0)==0
assert sp.expand(difference.subs({vb:0,vs:0,vt:0}))==0
assert sp.Poly(difference,u).degree()==2
# Negative controls: suppressing any *entire* correction channel is false.
for omitted in [c0,u*c1,u*u*c2]:
    assert sp.expand(difference-(c0+u*c1+u*u*c2-omitted))!=0
print("PASS exact full-length-power correction C0+u*C1+u^2*C2")
print("PASS finite mixed-product, specialization and negative controls")
print("NOT a bound on the finite-M remainder or an LP optimality proof")

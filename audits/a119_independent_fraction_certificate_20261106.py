#!/usr/bin/env python3
"""Independent exact-rational check of A119's substituted Xi-hat certificate.

Uses only the Python standard library. The formula checked here is transcribed
from the A119 derivation; this script does not independently derive Xi-hat
from the original optimization problem.
"""
from fractions import Fraction as F
from dataclasses import dataclass

@dataclass
class I:
    l:F; u:F
    def __add__(x,y):
        y=iv(y);return I(x.l+y.l,x.u+y.u)
    __radd__=__add__
    def __neg__(x):return I(-x.u,-x.l)
    def __sub__(x,y):return x+-iv(y)
    def __rsub__(x,y):return iv(y)+-x
    def __mul__(x,y):
        y=iv(y);t=[a*b for a in (x.l,x.u) for b in (y.l,y.u)];return I(min(t),max(t))
    __rmul__=__mul__
    def __truediv__(x,y):
        y=iv(y);assert y.l*y.u>0;return x*I(1/y.u,1/y.l)
    def __rtruediv__(x,y):return iv(y)/x
    def __pow__(x,n):
        if n<0:return iv(1)/(x**(-n))
        assert x.l>0
        return I(x.l**n,x.u**n)

def iv(x):return x if isinstance(x,I) else I(F(x),F(x))
b=F(1,8);delta=F(1,1875);s0=F(129,1000);s1=F(133,1000)

def calc(s,alpha,par,r):
    sig=F(0) if par=='even' else F(1,2)
    a=iv(1) if par=='even' else (1+s)/2
    B=b/s+2*delta;C=1-b/s-4*delta
    A=a*(1-B);D=s**(2-r)-a*B
    q=a*C/(A+alpha*D)
    T=1-2*delta;S=1-q-2*delta
    eh=alpha**2+2*sig*alpha;ek=alpha**2+2*alpha*(sig+r-1)
    B1=2*sig*alpha*s*B-2*a*alpha*b/s
    S1=2*sig*alpha*s*T-2*a*alpha-a*q*eh
    G2=2*alpha*(1+(1-s)*(alpha+2-sig-r))
    main=(1-s)*alpha*s**(2-r)*q*eh
    src=q*(a*B*G2-(1-s)*(alpha+1)*(B1+a*B*ek))
    tgt=(1-s)*(B1-S1)-2*alpha*s*a*(B-S)
    return main+src+tgt

if __name__=="__main__":
    for par in ('even','odd'):
        worst=None;count=0
        for r in (range(4,13) if par=='even' else range(4,20)):
            sig=F(0) if par=='even' else F(1,2)
            amin=2*(r+sig);amax=F(21,10)*(r+1+sig)
            for i in range(16):
                s=I(s0+(s1-s0)*F(i,16),s0+(s1-s0)*F(i+1,16))
                for j in range(16):
                    alpha=I(amin+(amax-amin)*F(j,16),amin+(amax-amin)*F(j+1,16))
                    v=calc(s,alpha,par,r)
                    assert v.l>0,(par,r,i,j,v.l)
                    if worst is None or v.l<worst[0]:worst=(v.l,r,i,j)
                    count+=1
        print(par,'boxes',count,'worst bound',worst[0],'approx',float(worst[0]),'location',worst[1:])
    Cmax=1-b/s1-4*delta;Bmax=b/s0+2*delta
    E=-Cmax+14*2*s0**3-14*F(21,10)*Bmax*s1**14
    O=-F(567,1000)*Cmax+F(43,2)*2*s0**3*F(359,1000)-F(567,1000)*F(43,2)*F(21,10)*Bmax*s1**21*F(365,1000)
    print('cutoffs',E>0,float(E),O>0,float(O))

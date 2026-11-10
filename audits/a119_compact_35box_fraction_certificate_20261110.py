#!/usr/bin/env python3
"""35-box exact-rational check of A119's substituted Xi-hat certificate.

Uses only the Python standard library. The formula checked here is transcribed
from the A119 derivation; this script does not independently derive Xi-hat
from the original optimization problem.
"""
from fractions import Fraction as F
from dataclasses import dataclass

if not __debug__:
    raise RuntimeError("Assertions disabled; do not use Python -O")

@dataclass
class I:
    l:F; u:F
    def __post_init__(self):
        assert self.l<=self.u, (self.l,self.u)
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
    den=A+alpha*D
    assert den.l>0, (par,r,'critical denominator',den)
    q=a*C/den
    assert q.l>0, (par,r,'critical q',q)
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
    source=I(s0,s1)
    records=[]
    for par,rmax,expected in (('even',12,14),('odd',19,21)):
        sig=F(0) if par=='even' else F(1,2)
        count=0
        for r in range(4,rmax+1):
            amin=2*(r+sig)
            amax=F(21,10)*(r+1+sig)
            cuts=(F(0),F(1,4),F(1,2),F(1)) if r==4 else (
                (F(0),F(1,2),F(1)) if r in (5,6,7)
                else (F(0),F(1)))
            assert cuts[0]==0 and cuts[-1]==1
            for left,right in zip(cuts,cuts[1:]):
                assert left<right
                alpha=I(amin+(amax-amin)*left,amin+(amax-amin)*right)
                val=calc(source,alpha,par,r)
                assert val.l>0,(par,r,left,right,val.l)
                records.append((par,r,left,right,val.l))
                count+=1
        assert count==expected,(par,count,expected)
        print('PASS',par,count,'closed rectangles')
        # Negative control: two coarse boxes do not suffice at r=4.
        amin=2*(4+sig)
        amax=F(21,10)*(5+sig)
        coarse=calc(source,I(amin,(amin+amax)/2),par,4)
        assert coarse.l<0,(par,coarse.l)
    assert len(records)==35
    worst=min(records,key=lambda rec:rec[-1])
    assert worst[-1]>0
    print('PASS 35-box exact positivity certificate; no gaps')
    print('worst exact rational lower bound:',worst[-1])
    print('worst rectangle:',worst[:4])
    print('display-only approximation:',float(worst[-1]))
    print('PASS coarse negative controls correctly refuse certification')
    print('Does not prove A115-to-A119 derivation, high-r tail, F2/F3 optimality or novelty')

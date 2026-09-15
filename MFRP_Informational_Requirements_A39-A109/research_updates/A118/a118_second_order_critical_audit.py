#!/usr/bin/env python3
from __future__ import annotations
import json, random
from fractions import Fraction as F
from pathlib import Path
import sympy as sp
import mpmath as mp

BETA_F=F(1,8); DELTA_F=F(1,1875)
BETA=mp.mpf(1)/8; DELTA=mp.mpf(1)/1875
OUT=Path(__file__).resolve().parent/'A118_EXACT_AUDIT_RESULTS_20260915.json'


def symbolic_gates():
    t=sp.symbols('t', positive=True)
    s,a,alpha,sigma,r,beta,delta,q=sp.symbols('s a alpha sigma r beta delta q', positive=True)
    c0=1-s; b0=beta/s; B=b0+2*delta; T=1-2*delta
    eta_h=alpha**2+2*sigma*alpha
    eta_k=alpha**2+2*alpha*(sigma+r-1)
    aM1=2*sigma*alpha*s
    B0=a*B
    B1=aM1*B-2*a*alpha*b0
    S0=a*(1-q-2*delta)
    S1=aM1*T-2*a*alpha-a*q*eta_h
    D0=B0-S0; D1=B1-S1
    G2=2*alpha*(1+c0*(alpha+2-sigma-r))
    Lambda=c0*(alpha*s**(2-r)*q-q*(alpha+1)*B0+D0)
    Xi=(alpha*c0*s**(2-r)*q*eta_h
        +q*(B0*G2-c0*(alpha+1)*(B1+B0*eta_k))
        +c0*D1-2*alpha*s*D0)

    qh=q*(1+eta_h*t)
    qk=q*(1+eta_k*t)
    Bt=B0+B1*t; St=S0+S1*t
    x=2*alpha*t-4*alpha**2*t**2
    y=1-2*alpha*t+4*alpha**2*t**2
    m=sigma+r-1
    kx=alpha+(-2*alpha**2-2*m*alpha)*t
    G=-x*(c0-t)+(kx-y)*c0*t
    main=alpha*c0*s**(2-r)*qh*t
    source=qk*Bt*G
    target=(c0-2*alpha*s*t)*t*(Bt-St)
    Ncore=sp.expand(main+source+target)
    return {
        'leading_coefficient_is_Lambda': sp.simplify(Ncore.coeff(t,1)-Lambda)==0,
        'second_coefficient_is_Xi': sp.simplify(Ncore.coeff(t,2)-Xi)==0,
    }


def phase(s,alpha,r,odd):
    a=(1+s)/2 if odd else mp.mpf(1)
    B=BETA/s+2*DELTA; C=1-BETA/s-4*DELTA
    A=a*(1-B); D=s**(2-r)-a*B
    return -a*C+mp.e**(-alpha)*(A+alpha*D)


def root_bisect(s,r,odd):
    L=-mp.log(s); sig=mp.mpf('0.5') if odd else mp.mpf(0)
    lo=(r+sig)*L; hi=(r+1+sig)*L
    if not (phase(s,lo,r,odd)>0 and phase(s,hi,r,odd)<0): return None
    for _ in range(140):
        mid=(lo+hi)/2
        if phase(s,mid,r,odd)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def xi_value(s,alpha,r,odd):
    sig=mp.mpf('0.5') if odd else mp.mpf(0)
    a=(1+s)/2 if odd else mp.mpf(1)
    q=mp.e**(-alpha); c0=1-s; b0=BETA/s
    B=b0+2*DELTA; T=1-2*DELTA; S=1-q-2*DELTA
    eta_h=alpha**2+2*sig*alpha
    eta_k=alpha**2+2*alpha*(sig+r-1)
    B1=2*sig*alpha*s*B-2*a*alpha*b0
    S1=2*sig*alpha*s*T-2*a*alpha-a*q*eta_h
    G2=2*alpha*(1+c0*(alpha+2-sig-r))
    Xi_main=alpha*c0*s**(2-r)*q*eta_h
    Xi_source=q*(a*B*G2-c0*(alpha+1)*(B1+a*B*eta_k))
    Xi_target=c0*(B1-S1)-2*alpha*s*a*(B-S)
    return Xi_main+Xi_source+Xi_target


def exp_lower(x,N):
    term=F(1); total=F(1)
    for n in range(1,N+1): term*=x/F(n); total+=term
    return total

def exp_upper(x,N):
    term=F(1); total=F(1)
    for n in range(1,N+1): term*=x/F(n); total+=term
    nxt=term*x/F(N+1); ratio=x/F(N+2); assert ratio<1
    return total+nxt/(1-ratio)

class I:
    def __init__(self,lo,hi=None): self.lo=F(lo); self.hi=F(lo if hi is None else hi); assert self.lo<=self.hi
    def __add__(self,o): o=o if isinstance(o,I) else I(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-(o if isinstance(o,I) else I(o)))
    def __rsub__(self,o): return I(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o); z=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]; return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,o): o=o if isinstance(o,I) else I(o); assert not(o.lo<=0<=o.hi); return self*I(1/o.hi,1/o.lo)
    def __pow__(self,n):
        assert isinstance(n,int)
        if n==0:return I(1)
        if n<0:return I(1)/(self**(-n))
        if n%2==0 and self.lo<0<self.hi:return I(0,max(self.lo**n,self.hi**n))
        return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))


def worst_case_certificate():
    s=F(129,1000); r=4; sig=F(1,2); a=(1+s)/2
    alo=F('10.560492'); ahi=F('10.560493')
    B=BETA_F/s+2*DELTA_F; C=1-BETA_F/s-4*DELTA_F; A=a*(1-B); D=s**(2-r)-a*B
    def fbounds(x):
        el=exp_lower(x,100); eu=exp_upper(x,100); qlo=1/eu; qhi=1/el; br=A+x*D
        return -a*C+qlo*br,-a*C+qhi*br
    flo=fbounds(alo); fhi=fbounds(ahi)
    assert flo[0]>0 and fhi[1]<0
    qlo=1/exp_upper(ahi,100); qhi=1/exp_lower(alo,100)
    al=I(alo,ahi); q=I(qlo,qhi); c0=I(1-s); b0=I(BETA_F/s); BI=b0+2*DELTA_F; TI=I(1-2*DELTA_F)
    eta_h=al**2+2*sig*al; eta_k=al**2+2*al*(sig+r-1); aM1=2*sig*al*s
    B0=I(a)*BI; B1=aM1*BI-2*I(a)*al*b0
    S0=I(a)*(1-q-2*DELTA_F); S1=aM1*TI-2*I(a)*al-I(a)*q*eta_h
    D0=B0-S0; D1=B1-S1; G2=2*al*(1+c0*(al+2-sig-r))
    Xi=al*c0*(s**(2-r))*q*eta_h + q*(B0*G2-c0*(al+1)*(B1+B0*eta_k)) + c0*D1-2*al*s*D0
    assert Xi.lo>F('2.061361852')
    assert Xi.hi<F('2.061366276')
    return {
      's':'129/1000','parity':'odd','r':4,'alpha_bracket':['10.560492','10.560493'],
      'phase_lower_positive':True,'phase_upper_negative':True,
      'certified_Xi_lower':'2.061361852','certified_Xi_upper':'2.061366276','Xi_gt_2':True}


def dense_stress():
    mp.mp.dps=70
    rows=[]
    for i in range(101):
        s=mp.mpf('0.129')+mp.mpf('0.004')*i/100
        for odd in (False,True):
            for r in range(4,30):
                a=root_bisect(s,r,odd)
                if a is not None:
                    rows.append((s,odd,r,a,xi_value(s,a,r,odd)))
    mn=min(rows,key=lambda z:z[4])
    random.seed(0); rcount=0; rmin=(mp.inf,None)
    for _ in range(250):
        s=mp.mpf(str(0.129+0.004*random.random()))
        for odd in (False,True):
            for r in range(4,30):
                a=root_bisect(s,r,odd)
                if a is not None:
                    x=xi_value(s,a,r,odd); rcount+=1
                    if x<rmin[0]: rmin=(x,(s,odd,r,a))
    return {
      'regular_grid_root_count':len(rows),
      'regular_grid_all_Xi_positive':all(z[4]>0 for z in rows),
      'regular_grid_min_Xi':mp.nstr(mn[4],25),
      'regular_grid_min_location':{'s':mp.nstr(mn[0],15),'parity':'odd' if mn[1] else 'even','r':mn[2],'alpha':mp.nstr(mn[3],25)},
      'random_source_root_count':rcount,
      'random_source_all_Xi_positive':rmin[0]>0,
      'random_source_min_Xi':mp.nstr(rmin[0],25),
      'random_source_min_location':{'s':mp.nstr(rmin[1][0],15),'parity':'odd' if rmin[1][1] else 'even','r':rmin[1][2],'alpha':mp.nstr(rmin[1][3],25)},
    }


def main():
    gates=symbolic_gates(); assert all(gates.values())
    cert=worst_case_certificate(); stress=dense_stress()
    out={'audit':'A118_SECOND_ORDER_CRITICAL_LAYER_AUDIT','date':'2026-09-15','status':'PASS_WITH_OPEN_GLOBAL_SIGN',
         'symbolic_gates':gates,'exact_rational_control':cert,'finite_numerical_stress':stress,
         'nonclaims':['dense critical-root stress is finite evidence only','global Xi positivity on all critical surfaces is not proved','no minimal finite realization M is claimed','no target-deformed A114 lifted classification is claimed','no physical or ontological interpretation is claimed']}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()

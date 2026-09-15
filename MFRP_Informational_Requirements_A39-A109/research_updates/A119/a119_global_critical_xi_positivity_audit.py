#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path

BETA=F(1,8)
DELTA=F(1,1875)
S0=F(129,1000)
S1=F(133,1000)
LMIN=F(2)
LMAX=F(21,10)
SQRT_S0_LO=F(359,1000)
SQRT_S1_HI=F(365,1000)
AMAX_ODD=F(567,1000)
OUT=Path(__file__).resolve().parent/'A119_EXACT_AUDIT_RESULTS_20260915.json'

@dataclass(frozen=True)
class Iv:
    lo:F
    hi:F
    def __post_init__(self):
        if self.lo>self.hi: raise ValueError((self.lo,self.hi))
    def __add__(self,o):
        o=asiv(o); return Iv(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return Iv(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asiv(o))
    def __rsub__(self,o): return asiv(o)-self
    def __mul__(self,o):
        o=asiv(o)
        vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return Iv(min(vals),max(vals))
    __rmul__=__mul__
    def recip(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError((self.lo,self.hi))
        return Iv(F(1,1)/self.hi,F(1,1)/self.lo)
    def __truediv__(self,o): return self*asiv(o).recip()
    def __rtruediv__(self,o): return asiv(o)/self
    def powi(self,n:int):
        if n==0: return Iv(F(1),F(1))
        if n<0: return self.powi(-n).recip()
        if self.lo>=0: return Iv(self.lo**n,self.hi**n)
        if self.hi<=0:
            vals=(self.lo**n,self.hi**n)
            return Iv(min(vals),max(vals))
        if n%2==0: return Iv(F(0),max(abs(self.lo),abs(self.hi))**n)
        return Iv(self.lo**n,self.hi**n)

def asiv(x):
    return x if isinstance(x,Iv) else Iv(F(x),F(x))

def xi_hat_interval(s:Iv, alpha:Iv, parity:str, r:int)->Iv:
    """Exact interval extension of A118 Xi after the critical substitution."""
    sigma=F(0) if parity=='even' else F(1,2)
    a=asiv(1) if parity=='even' else (1+s)/2
    B=BETA/s+2*DELTA
    C=1-BETA/s-4*DELTA
    A=a*(1-B)
    D=s.powi(2-r)-a*B
    den=A+alpha*D
    if den.lo<=0:
        raise AssertionError(('nonpositive critical denominator',parity,r,den))
    q=a*C/den
    T=1-2*DELTA
    S=1-q-2*DELTA
    eta_h=alpha*alpha+2*sigma*alpha
    eta_k=alpha*alpha+2*alpha*(sigma+r-1)
    B1=2*sigma*alpha*s*B-2*a*alpha*BETA/s
    S1=2*sigma*alpha*s*T-2*a*alpha-a*q*eta_h
    G2=2*alpha*(1+(1-s)*(alpha+2-sigma-r))
    main=(1-s)*alpha*s.powi(2-r)*q*eta_h
    src=q*(a*B*G2-(1-s)*(alpha+1)*(B1+a*B*eta_k))
    tgt=(1-s)*(B1-S1)-2*alpha*s*a*(B-S)
    return main+src+tgt

def deep_cell_cutoff_certificate():
    Cmax=1-BETA/S1-4*DELTA
    Bmax=BETA/S0+2*DELTA
    n=F(14)
    even_lb=-Cmax+n*LMIN*S0**3-n*LMAX*Bmax*S1**14
    even_ratio=F(15,14)*S1
    assert even_lb>0 and even_ratio<1
    n=F(43,2)
    odd_lb=(-AMAX_ODD*Cmax
            +n*LMIN*S0**3*SQRT_S0_LO
            -AMAX_ODD*n*LMAX*Bmax*S1**21*SQRT_S1_HI)
    odd_ratio=F(45,43)*S1
    assert odd_lb>0 and odd_ratio<1
    return {
        'even_no_critical_for_r_ge':13,
        'even_right_edge_lower_at_r13':str(even_lb),
        'even_decay_ratio_upper':str(even_ratio),
        'odd_no_critical_for_r_ge':20,
        'odd_right_edge_lower_at_r20':str(odd_lb),
        'odd_decay_ratio_upper':str(odd_ratio),
    }

def interval_certificate(parity:str,r_values:range,ns=16,na=16):
    sigma=F(0) if parity=='even' else F(1,2)
    worst=None
    boxes=0
    for r in r_values:
        amin=LMIN*(r+sigma)
        amax=LMAX*(r+1+sigma)
        for i in range(ns):
            slo=S0+(S1-S0)*F(i,ns)
            shi=S0+(S1-S0)*F(i+1,ns)
            si=Iv(slo,shi)
            for j in range(na):
                alo=amin+(amax-amin)*F(j,na)
                ahi=amin+(amax-amin)*F(j+1,na)
                ai=Iv(alo,ahi)
                val=xi_hat_interval(si,ai,parity,r)
                boxes+=1
                assert val.lo>0,(parity,r,i,j,val)
                if worst is None or val.lo<worst['lower']:
                    worst={'lower':val.lo,'upper':val.hi,'r':r,'i':i,'j':j,
                           'slo':slo,'shi':shi,'alo':alo,'ahi':ahi}
    return {
        'boxes':boxes,
        'subdivision':[ns,na],
        'worst_lower':str(worst['lower']),
        'worst_upper':str(worst['upper']),
        'worst_cell':{k:(str(v) if isinstance(v,F) else v) for k,v in worst.items() if k not in ('lower','upper')},
    }

def main():
    cut=deep_cell_cutoff_certificate()
    even=interval_certificate('even',range(4,13))
    odd=interval_certificate('odd',range(4,20))
    out={
      'audit':'A119_GLOBAL_CRITICAL_XI_POSITIVITY_AUDIT',
      'date':'2026-09-15',
      'status':'PASS',
      'contract':{'beta':'1/8','delta':'1/1875','s_window':['129/1000','133/1000']},
      'log_enclosure_used':'2 < -log(s) < 21/10 (inherited exact A117 certificate)',
      'deep_cell_cutoff':cut,
      'critical_substitution':'q = a*C/(A + alpha*D) on Lambda_p=0',
      'finite_interval_certificate':{
          'even_r_range':'4..12','odd_r_range':'4..19',
          'even':even,'odd':odd,
          'total_boxes':even['boxes']+odd['boxes'],
          'arithmetic':'fractions.Fraction inclusive natural interval extension'},
      'conclusion':'Every A117 critical surface has Xi_p>0; Lambda_p=Xi_p=0 is impossible under the frozen contract.',
      'nonclaims':['no finite minimal M realization threshold','no target-deformed A114 lifted staircase','no physical or ontological interpretation']}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','total_boxes':out['finite_interval_certificate']['total_boxes'],
      'even_worst_lower':even['worst_lower'],'odd_worst_lower':odd['worst_lower'],
      'even_cutoff_lb':cut['even_right_edge_lower_at_r13'],'odd_cutoff_lb':cut['odd_right_edge_lower_at_r20']},indent=2))

if __name__=='__main__': main()

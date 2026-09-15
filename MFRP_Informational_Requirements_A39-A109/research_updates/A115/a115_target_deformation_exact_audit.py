#!/usr/bin/env python3
"""A115 exact target-node deformation audit. No floating-point sign decisions."""
from __future__ import annotations
import hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
OUT=HERE/"A115_TARGET_DEFORMATION_EXACT_RESULTS_20260914.json"
BETA=F(1,8); DELTA=F(1,1875)
S_PROBES=(F(129,1000),F(131,1000),F(133,1000))

def sg(x): return 1 if x>0 else -1 if x<0 else 0
def fs(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def pows(x,n):
    a=[F(1)]*(n+1)
    for i in range(1,n+1): a[i]=a[i-1]*x
    return a
def B(M,k,p): return p[k]-F(M-k,M)-F(k,M)*p[M]
def dB(M,k,p): return p[k+1]-p[k]+F(1-p[M],M)

def eps0(M):
    h=M//2
    return F(1,(1875 if M%2==0 else 2500)*2**h)
def d0(M,r,p):
    h=M//2; u=F(1,2**h); d=1-(h+1)*u
    if M%2==0:
        return (-2*u/d)*r+(1+2*h*u/d)*p[h]-2*(h-1)*u/d*p[h+1]
    return (-F(3,2)*u/d)*r+(F(1,2)+F(3,2)*h*u/d)*p[h]+(F(1,2)-F(3,2)*(h-1)*u/d)*p[h+1]

def den(M,tau):
    h=M//2; u=tau**h
    return tau-h*u+(h-1)*tau*u
def eps(M,tau):
    h=M//2; u=tau**h
    return DELTA*(u if M%2==0 else F(1+tau,2)*u)
def dt(M,r,p,tau):
    h=M//2; u=tau**h
    L=r-h*p[h]+(h-1)*p[h+1]
    if M%2==0: return p[h]-u*L/den(M,tau)
    return F(p[h]+p[h+1],2)-F(1+tau,2)*u*L/den(M,tau)

def E_with_d(M,k,s,tau,epsilon,dfunc):
    bp=pows(BETA,M); tp=pows(tau,M); spw=pows(s,M)
    db=dfunc(M,BETA,bp); ds=dfunc(M,s,spw)
    hb=F(1+bp[M],2)-db+2*epsilon
    hs=F(1+spw[M],2)-ds-2*epsilon
    bb,bt=B(M,k,bp),B(M,k,tp); xb,xt=dB(M,k,bp),dB(M,k,tp)
    A=F(1+tp[M],2)
    X=A*bb-hb*bt; Y=-A*xb+hb*xt; W=-bb*xt+bt*xb
    return X*dB(M,k,spw)+Y*B(M,k,spw)+W*hs
def E0(M,k,s): return E_with_d(M,k,s,F(1,2),eps0(M),d0)
def Et(M,k,s,tau): return E_with_d(M,k,s,tau,eps(M,tau),lambda M,r,p:dt(M,r,p,tau))

def coeffs(M,s,tau):
    bp,tp,spw=pows(BETA,M),pows(tau,M),pows(s,M); e=eps(M,tau)
    hb=F(1+bp[M],2)-dt(M,BETA,bp,tau)+2*e
    hs=F(1+spw[M],2)-dt(M,s,spw,tau)-2*e
    ab,at,as_=F(1-bp[M],M),F(1-tp[M],M),F(1-spw[M],M); A=F(1+tp[M],2)
    return {
      "bs":A*(s-BETA),"bt":hs*(BETA-tau),"st":hb*(tau-s),
      "kb":-(BETA-1)*(A*as_-hs*at),
      "b":A*as_+A*BETA-A-hs*at-hs*BETA+hs,
      "kt":(tau-1)*(hb*as_-hs*ab),
      "t":-hb*as_-hb*tau+hb+hs*ab+hs*tau-hs,
      "ks":(s-1)*(A*ab-hb*at),
      "s":-A*ab-A*s+A+hb*at+hb*s-hb,
      "1":-A*as_+A*ab+hb*as_-hb*at-hs*ab+hs*at}
def Ek(M,k,s,tau):
    c=coeffs(M,s,tau)
    return c["bs"]*(BETA*s)**k+c["bt"]*(BETA*tau)**k+c["st"]*(s*tau)**k+(c["b"]+k*c["kb"])*BETA**k+(c["s"]+k*c["ks"])*s**k+(c["t"]+k*c["kt"])*tau**k+c["1"]

def b_exact(M,s,tau):
    lo,hi=0,M; target=tau**M
    while lo<hi:
        m=(lo+hi)//2
        if s**(2*m)<=target: hi=m
        else: lo=m+1
    return lo
def admiss(M,b): return 2<=b+1 and b+2<=M//2-2

def direct_d(M,r,tau):
    h=M//2; mean=F(M,2)
    A=[[F(1),F(1),F(1)],[F(1),F(h),F(h+1)],[tau,tau**h,tau**(h+1)]]
    def solve(rhs):
        z=[A[i][:]+[rhs[i]] for i in range(3)]
        for c in range(3):
            q=next(i for i in range(c,3) if z[i][c])
            z[c],z[q]=z[q],z[c]; pv=z[c][c]; z[c]=[x/pv for x in z[c]]
            for i in range(3):
                if i==c: continue
                f=z[i][c]
                if f: z[i]=[z[i][j]-f*z[c][j] for j in range(4)]
        return [z[i][3] for i in range(3)]
    q0,q1=solve([F(0),F(0),F(1)]),solve([F(1),mean,F(1)])
    w=[r,r**h,r**(h+1)]
    return sum(w[i]*(q1[i]-q0[i]) for i in range(3))
def E_direct(M,k,s,tau):
    return E_with_d(M,k,s,tau,eps(M,tau),lambda M,r,p:direct_d(M,r,tau))

def sha(q):
    if hasattr(sys,"set_int_max_str_digits"): sys.set_int_max_str_digits(0)
    x=f"{q.numerator}/{q.denominator}".encode()
    return hashlib.sha256(x).hexdigest(),len(str(abs(q.numerator))),len(str(q.denominator))

def symbolic():
    h=sp.symbols("h",integer=True,positive=True); tau,t=sp.symbols("tau t",positive=True); u=tau**h
    D=tau-h*u+(h-1)*tau*u
    q1=(1-u*t)/D; qh=t-h*q1; qh1=(h-1)*q1
    qo=(1-sp.Rational(1,2)*(1+tau)*u*t)/D; qho=t/2-h*qo; qh1o=t/2+(h-1)*qo
    c0,c1,k=sp.symbols("c0 c1 k")
    gates={
      "even_norm":sp.simplify(q1+qh+qh1-t)==0,
      "even_mean":sp.simplify(q1+h*qh+(h+1)*qh1-h*t)==0,
      "even_target":sp.simplify(tau*q1+tau**h*qh+tau**(h+1)*qh1-1)==0,
      "odd_norm":sp.simplify(qo+qho+qh1o-t)==0,
      "odd_mean":sp.simplify(qo+h*qho+(h+1)*qh1o-(h+sp.Rational(1,2))*t)==0,
      "odd_target":sp.simplify(tau*qo+tau**h*qho+tau**(h+1)*qh1o-1)==0,
      "J_cancel":sp.simplify((c0+k*c1)*tau**k-tau**-1*(c0+(k+1)*c1)*tau**(k+1)+c1*tau**k)==0}
    b,T,s=sp.symbols("b T s"); bk,tk,sk,K=sp.symbols("B TK S K"); ab,at,as_=sp.symbols("ab at as"); A,hb,hs=sp.symbols("A hb hs")
    Bb=bk-1+K*ab; Bt=tk-1+K*at; Bs=sk-1+K*as_; Db=(b-1)*bk+ab; Dt=(T-1)*tk+at; Ds=(s-1)*sk+as_
    X=A*Bb-hb*Bt; Y=-A*Db+hb*Dt; W=-Bb*Dt+Bt*Db
    orig=sp.expand(X*Ds+Y*Bs+W*hs)
    exp= A*(s-b)*bk*sk+hs*(b-T)*bk*tk+hb*(T-s)*tk*sk+(A*as_+A*b-A-hs*at-hs*b+hs)*bk-(b-1)*(A*as_-hs*at)*K*bk+(-A*ab-A*s+A+hb*at+hb*s-hb)*sk+(s-1)*(A*ab-hb*at)*K*sk+(-hb*as_-hb*T+hb+hs*ab+hs*T-hs)*tk+(T-1)*(hb*as_-hs*ab)*K*tk+(-A*as_+A*ab+hb*as_-hb*at-hs*ab+hs*at)
    gates["generic_A84_identity"]=sp.expand(orig-exp)==0
    return gates

def main():
    gates=symbolic(); assert all(gates.values()),gates
    Dchecks=[]; Echecks=[]
    for M in (10,11,20,21,77,100,521,522,777):
      for r in (BETA,*S_PROBES):
        p=pows(r,M); Dchecks.append(dt(M,r,p,F(1,2))==d0(M,r,p))
      h=M//2
      for s in S_PROBES:
        for k in sorted({2,3,max(2,h//3),max(2,h-2)}):
          if 2<=k<=h-2:Echecks.append(Et(M,k,s,F(1,2))==E0(M,k,s))
    assert all(Dchecks) and all(Echecks)

    Kchecks=[]
    for M in (20,21,100,101,521,522):
      h=M//2
      for s in S_PROBES:
        for tau in (F(1,5),F(3,10),F(1,2),F(4,5)):
          if not BETA<s<tau<1: continue
          b=b_exact(M,s,tau)
          for k in sorted({2,max(2,min(h-2,b)),max(2,min(h-2,b+1))}):
            if 2<=k<=h-2: Kchecks.append(Et(M,k,s,tau)==Ek(M,k,s,tau))
    assert all(Kchecks)

    sent=[]
    for M in (521,522,561,600,760,1000,2049):
      for s in S_PROBES:
        b=b_exact(M,s,F(1,2)); eb=Et(M,b,s,F(1,2)); e1=Et(M,b+1,s,F(1,2)); e2=Et(M,b+2,s,F(1,2)); e3=Et(M,b+3,s,F(1,2)); J=e1-2*e2
        row={"M":M,"s":fs(s),"b":b,"sign_E_b":sg(eb),"sign_E_bplus2":sg(e2),"sign_E_bplus3":sg(e3),"sign_J":sg(J)}
        assert row["sign_E_b"]==1 and row["sign_E_bplus3"]==-1 and row["sign_J"]==1,row
        sent.append(row)

    coarse=[]
    for tau in (F(n,100) for n in range(15,91,5)):
      for M in (521,522,600,760):
        for s in S_PROBES:
          if not BETA<s<tau<1:continue
          b=b_exact(M,s,tau); assert admiss(M,b) and b+3<=M//2-2
          eb=Et(M,b,s,tau); e1=Et(M,b+1,s,tau); e2=Et(M,b+2,s,tau); e3=Et(M,b+3,s,tau); J=e1-e2/tau
          coarse.append({"tau":fs(tau),"M":M,"s":fs(s),"b":b,"sign_E_b":sg(eb),"sign_E_bplus3":sg(e3),"sign_J":sg(J),"strong_package":sg(eb)==1 and sg(e3)==-1 and sg(J)==1})
    by={}
    for r in coarse:
      z=by.setdefault(r["tau"],{"total":0,"J_positive":0,"strong_package":0}); z["total"]+=1; z["J_positive"]+=r["sign_J"]==1; z["strong_package"]+=r["strong_package"]

    near=[]
    offsets=(F(1,10000),F(2,10000),F(5,10000),F(1,1000),F(2,1000),F(5,1000),F(1,100),F(2,100))
    for s in S_PROBES:
      for off in offsets:
        tau=s+off
        for M in (521,600,800,1000,1500,2000):
          b=b_exact(M,s,tau)
          if not admiss(M,b):continue
          J=Et(M,b+1,s,tau)-Et(M,b+2,s,tau)/tau
          near.append({"s":fs(s),"offset":fs(off),"tau":fs(tau),"M":M,"b":b,"h":M//2,"sign_J":sg(J)})
    neg=[r for r in near if r["sign_J"]<0]; assert len(neg)==2,neg

    ces=[]
    for s,tau in ((F(131,1000),F(141,1000)),(F(133,1000),F(143,1000))):
      M=521;b=b_exact(M,s,tau);assert admiss(M,b)
      assert s**(2*b)<=tau**M and s**(2*(b-1))>tau**M
      e1,e2=Et(M,b+1,s,tau),Et(M,b+2,s,tau)
      d1,d2=E_direct(M,b+1,s,tau),E_direct(M,b+2,s,tau);assert (e1,e2)==(d1,d2)
      J=e1-e2/tau;assert J<0
      H,nd,dd=sha(J)
      ces.append({"M":M,"s":fs(s),"tau":fs(tau),"b":b,"h":M//2,"bplus2":b+2,"max_admissible_factor_contact":M//2-2,"sign_J":-1,"direct_matrix_crosscheck":True,"b_tau_ceil_certificate":True,"J_fraction_sha256":H,"J_numerator_decimal_digits":nd,"J_denominator_decimal_digits":dd})

    M=521;s=F(129,1000);tau=F(667,5000);b=b_exact(M,s,tau)
    correction={"M":M,"s":fs(s),"tau":fs(tau),"b":b,"h":M//2,"bplus2":b+2,"max_admissible_factor_contact":M//2-2,"central_J_admissible":admiss(M,b),"disposition":"REJECTED_AS_COUNTEREXAMPLE_OUTSIDE_A84_ADJACENT_FACTOR_DOMAIN"}
    assert not correction["central_J_admissible"]

    out={"audit":"A115_TARGET_NODE_DEFORMATION_EXACT_AUDIT","date":"2026-09-14","status":"PASS_WITH_REFUTATION","scope":{"beta":fs(BETA),"delta":fs(DELTA),"source_probes":[fs(x) for x in S_PROBES],"factor_contact_domain":"2 <= k <= floor(M/2)-2"},"symbolic_gates":gates,"exact_reproduction":{"deformed_D_equals_frozen_D_at_tau_half":{"pass":True,"count":len(Dchecks)},"deformed_E_equals_frozen_A84_E_at_tau_half":{"pass":True,"count":len(Echecks)},"deformed_cofactor_equals_deformed_kspace":{"pass":True,"count":len(Kchecks)},"A113_sentinel_controls":{"pass":True,"count":len(sent),"records":sent}},"finite_exact_evidence":{"coarse_grid":{"control_count":len(coarse),"J_positive_count":sum(r["sign_J"]==1 for r in coarse),"strong_package_count":sum(r["strong_package"] for r in coarse),"by_tau":by},"near_wall_grid":{"admissible_control_count":len(near),"J_positive_count":sum(r["sign_J"]==1 for r in near),"J_negative_count":len(neg),"negative_records":neg}},"refutation":{"claim":"M>=521 and beta<s<tau<1 universally imply J_(tau,b_tau+1)>0","status":"REFUTED","counterexamples":ces},"correction":correction,"open_claims":["For each fixed beta<s<tau<1, J_(tau,b_tau+1) may be eventually positive in M.","Uniform eventual positivity may hold on compact subsets strictly inside beta<s<tau<1.","No such asymptotic statement is proved by this audit."],"nonclaims":["The 192/192 coarse-grid result is finite evidence, not a theorem.","The strong A113 remote-sign package is not generalized here.","No A114 lifted active-set staircase theorem is generalized in tau.","No physical or ontological interpretation is inferred."]}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True),encoding="utf-8")
    print(json.dumps({"status":out["status"],"reproduction_counts":{"D":len(Dchecks),"E":len(Echecks),"kspace":len(Kchecks),"A113":len(sent)},"coarse":out["finite_exact_evidence"]["coarse_grid"],"near_wall":out["finite_exact_evidence"]["near_wall_grid"],"counterexamples":ces,"correction":correction,"output":str(OUT)},indent=2,sort_keys=True))

if __name__=="__main__":main()

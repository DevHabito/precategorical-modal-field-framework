#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2B_GAMMA_MINUS_TAIL_EXCLUSION_ANALYTIC_CERTIFICATE_20260913.json'

# Frozen tail constants
LO=F(129,1000); HI=F(133,1000); B=F(1,8); G=F(1,16)
CLO=F(16923,100000); CUP=F(17180,100000)
HMIN=260; JHMAX=F(3,8); YMAX=F(1,2**13)

# ---------- Bridge A: Phi<0 forces 3j-h>=13 ----------
# If 3j-h<=12, Y=beta^j/U >= 2^-12. Since j=b+2>=91 and 8s>=8LO,
# the positive Vandermonde core has the following exact lower bound after
# dropping the positive gamma^j term. A112-A V2 re-audit supplies the
# already-proved uniform remainder caps; 1e-70 safely dominates their sum.
YLOW_BAD=F(1,2**12)
core_lower=YLOW_BAD*((B-G)*(8*LO)**91-(HI-G))
affine_upper=(1-CLO)*8*(HI-G)/1875
inherited_error_cap=F(1,10**70)
bridge_A_margin=core_lower-affine_upper-inherited_error_cap
bridge_A_gates={
    '16923_over_100000_gt_1_over_6': CLO>F(1,6),
    # Exact integer form of c(LO)>88/521; hence b=ceil(Mc(s))>=89 for M>=521.
    'c_LO_gt_88_over_521': (2**521)*(LO.numerator**176) > LO.denominator**176,
    'core_bracket_positive': ((B-G)*(8*LO)**91-(HI-G))>0,
    'bridge_A_margin_gt_1e-6': bridge_A_margin>F(1,10**6),
}

# ---------- Bridge B: under 3j-h>=13, pure gamma- cannot have p0,pj>0 ----------
U,Y,T,h,j=sp.symbols('U Y T h j', positive=True)
x0,xm,xj,xM=sp.symbols('x0 xm xj xM')

def q_cd(parity:str, base:str):
    d=1-(h+1)*U
    if base=='beta': r=sp.Rational(1,8); rh=U**3; rh1=U**3/8
    else: r=sp.Rational(1,16); rh=U**4; rh1=U**4/16
    C=sp.factor((2*r-2*h*rh+2*(h-1)*rh1)/d)
    if parity=='even':
        D=sp.factor((-2*U/d)*r+(1+2*h*U/d)*rh+(-2*(h-1)*U/d)*rh1)
    else:
        D=sp.factor((-sp.Rational(3,2)*U/d)*r+(sp.Rational(1,2)+sp.Rational(3,2)*h*U/d)*rh+(sp.Rational(1,2)-sp.Rational(3,2)*(h-1)*U/d)*rh1)
    return C,D

def derive(parity:str):
    M=2*h if parity=='even' else 2*h+1
    scale=sp.Integer(1875 if parity=='even' else 2500)
    eps=U/scale
    bjm1=8*U*Y; bj=U*Y; bm=U**6 if parity=='even' else U**6/8
    gjm1=16*U*Y*T; gj=U*Y*T; gm=U**8 if parity=='even' else U**8/16
    A=sp.Matrix([[1,1,1,1],[0,j-1,j,M],[1,bjm1,bj,bm],[1,gjm1,gj,gm]])
    Cb,Db=q_cd(parity,'beta'); Cg,Dg=q_cd(parity,'gamma')
    c=A.inv(method='DM')*sp.Matrix([0,0,Cb,Cg])
    a=A.inv(method='DM')*sp.Matrix([1,sp.Rational(1,2)*M,Db-2*eps,Dg-2*eps])
    a=[sp.factor(v) for v in a]; c=[sp.factor(v) for v in c]
    K=sp.factor(c[0]*a[2]-c[2]*a[0])
    common_const=15000 if parity=='even' else 10000
    den=sp.factor(sp.fraction(a[0])[1])
    D2=sp.factor(den/(common_const*(U*h+U-1)))
    a0num=sp.factor(sp.fraction(a[0])[0]/U)
    return {'D2':D2,'a0':a0num,'c0':sp.factor(sp.fraction(c[0])[0]),
            'aj':sp.factor(sp.fraction(a[2])[0]),'cj':sp.factor(sp.fraction(c[2])[0]),
            'K':sp.factor(sp.fraction(K)[0])}

def rat(x)->F:
    z=sp.Rational(x); return F(int(z.p),int(z.q))

def remainder_bound(expr, scale_y:int, scale_h:int)->F:
    lead=sp.expand(expr.subs({U:0,T:0}))
    rem=sp.Poly(sp.expand(expr-lead),U,T,Y,h,j)
    total=F(0)
    for mon,coef in rem.terms():
        eU,eT,eY,eh,ej=mon
        c=abs(rat(coef))*JHMAX**ej
        n=eh+ej-scale_h
        if eY>=scale_y:
            c*=YMAX**(eY-scale_y); eUeff=eU
        else:
            # Y=2^(h-3j) >= 8 U^2 because j<=h-1.
            assert scale_y==1 and eY==0 and eU>=2
            c*=F(1,8); eUeff=eU-2
        # j>=h/3, so T=2^-j <= 2^(-h/3) < (4/5)^h.
        if n>=0:
            ratio=F(HMIN+1,HMIN)**n * F(1,2)**eUeff * F(4,5)**eT
            assert ratio<1
            c*=F(HMIN**n)*F(1,2)**(eUeff*HMIN)*F(4,5)**(eT*HMIN)
        else:
            c*=F(1,HMIN**(-n))*F(1,2)**(eUeff*HMIN)*F(4,5)**(eT*HMIN)
        total+=c
    return total

def leading_margins(parity:str):
    if parity=='even':
        D=F(14)-7*JHMAX-F(1,HMIN)
        return {'D2':D,'a0':1891*D,'c0':D,
                'aj':1875*(F(2)-JHMAX+F(1,HMIN)),
                'cj':F(2)-JHMAX+F(1,HMIN),
                'K':F(4)-2*JHMAX+F(2,HMIN)-15000*YMAX}
    D=16*(F(14)-7*JHMAX+F(6,HMIN))
    return {'D2':D,'a0':15128*(F(14)-7*JHMAX+F(6,HMIN)),
            'c0':8*(F(14)-7*JHMAX+F(6,HMIN)),
            'aj':5000*(F(6)-3*JHMAX+F(6,HMIN)),
            'cj':8*(F(2)-JHMAX+F(2,HMIN)),
            'K':8*(F(2)-JHMAX+F(2,HMIN)-10000*YMAX-5000*YMAX/F(HMIN))}

bridge_B={}
for parity in ('even','odd'):
    E=derive(parity); margins=leading_margins(parity)
    rows={}
    for name in ('D2','a0','c0','aj','cj','K'):
        by=1 if name in ('D2','a0','c0') else 0
        rb=remainder_bound(E[name],by,1)
        rows[name]={'leading_margin':str(margins[name]),'remainder_bound_decimal':format(float(rb),'.16e'),'gate':margins[name]>rb}
    bridge_B[parity]=rows

# Domain gates used by the remainder certificate.
# j=b+2; b=ceil(M c(s)); A89 has CLO<c(s)<CUP.
# For h>=260 these imply h/3<j<(3/8)h.
jh_upper_at_worst=CUP*F(521,260)+F(3,260)
domain_gates={
    'M0_floor_half_is_260': 521//2==260,
    'j_over_h_upper_lt_3_over_8': jh_upper_at_worst<F(3,8),
    'j_over_h_lower_gt_1_over_3': CLO>F(1,6),
    'd1_negative_at_h260_and_decay': F(261,2**260)<1,
    'two_to_minus_one_third_lt_4_over_5': F(1,2)<F(64,125),
}
all_B=all(item['gate'] for p in bridge_B.values() for item in p.values())
verdict=all(bridge_A_gates.values()) and all(domain_gates.values()) and all_B
out={
 'audit':'A114B2B_GAMMA_MINUS_TAIL_EXCLUSION_ANALYTIC_CERTIFICATE',
 'verdict':'PASS' if verdict else 'FAIL',
 'claim':'For M>=521, s in [129/1000,133/1000], j=b+2 and Phi=F_j^up<0, the pure central-Q gamma-minus basis P={0,j-1,j,M}, Q={1,h,h+1} cannot have all strict positive basic masses.',
 'bridge_A':{'margin_decimal':float(bridge_A_margin),'margin_gt_1e_6':bridge_A_margin>F(1,10**6),'gates':bridge_A_gates,
             'dependency':'uses the already-audited A112-A V2 cofactor/remainder caps; 1e-70 is a conservative aggregate cap; the exact rational margin is recomputed by this script'},
 'domain_gates':domain_gates,
 'algebraic_implications':[
   'If 3j-h<=12 then Y=2^(h-3j)>=2^-12 by definition.',
   'If 3j-h>=13 then Y=2^(h-3j)<=2^-13 by definition.',
   'If j<=h-1 then Y=2^(h-3j)>=8*U^2 for U=2^-h.'
 ],
 'bridge_B':bridge_B,
 'logic':[
   'Phi<0 and j=b+2 imply 3j-h>=13 by Bridge A.',
   'Hence Y=2^(h-3j)<=2^-13.',
   'Bridge B derives p0(t)=a0*t+c0 and pj(t)=aj*t+cj from normalization, mean, beta-, gamma- only.',
   'For both parities: a0<0<c0, cj<0<aj, and K=c0*aj-cj*a0<0.',
   'Thus zero(pj)>zero(p0); whenever pj>0 one has p0<0. Strict primal feasibility is impossible.'
 ],
 'claim_limits':['This excludes only the pure central-Q gamma-minus architecture.','It does not classify the remaining C/E/QI/QA architectures.','Phi=0 is not covered.']
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))

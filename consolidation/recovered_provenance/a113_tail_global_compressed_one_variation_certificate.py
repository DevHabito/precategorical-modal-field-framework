#!/usr/bin/env python3
"""A113 analytic-tail global compressed one-variation certificate.

Target contract:
    M >= 521
    129/1000 <= s <= 133/1000
    beta=1/8, target=1/2
    b=ceil(M*c(s)), c(s)=log(2)/(-2 log s)

Proves, for the exact A84 adjacent compressed-objective factors E_(M,k)(s):
    E_k > 0  for every admissible k <= b,
    E_k < 0  for every admissible k >= b+3,
    E_(b+1) - 2 E_(b+2) > 0.

Therefore the complete adjacent-factor sequence has one positive-to-negative
variation. The global compressed maximizer is b+1, b+2 or b+3 (with adjacent
ties at a central zero).

The proof uses exact Fraction arithmetic for every majorant gate. SymPy is
used only for algebraic identity checks; no floating-point sign decision is
used in the theorem gates.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import sympy as sp

B=F(1,8); T=F(1,2)
S0=F(129,1000); S1=F(133,1000)
M0=521; H0=M0//2
U0=F(1,2**H0)
HLO=F(49,100); HHI=F(51,100)
ETA=F(27,100)
DLO=F(43,10000)
DHI=F(7,500)
XCAP=F(271,1000)
AFF=F(9,25)   # bound for |c+k c_k|/U when k/M<=1/2


def fs(x):
    return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def dec(x,n=24):
    from decimal import Decimal, localcontext
    with localcontext() as c:
        c.prec=n+10
        return format(Decimal(x.numerator)/Decimal(x.denominator),f'.{n}g')

def c_gt(probe,r):
    p,q=r.numerator,r.denominator
    return (2**q)*(probe.numerator**(2*p)) > probe.denominator**(2*p)

def c_lt(probe,r):
    p,q=r.numerator,r.denominator
    return (2**q)*(probe.numerator**(2*p)) < probe.denominator**(2*p)

# A89 D-block remainder ratio bounds, rebuilt here independently.
def d_remainder_caps():
    den=1-(H0+1)*U0
    q0=(2*S1)**H0
    hu=H0*U0; hpu=(H0+1)*U0
    even=(q0*(1+2*hu+2*hu*S1)+2*hpu*S1)/den
    odd=(F(1,2)*(1+S1)*q0+F(3,2)*hu*(1+S1)*q0+F(3,2)*hpu*S1)/den
    return even,odd,max(even,odd)

RE,RO,RC=d_remainder_caps()
# r^M/U caps for beta <= r <= smax and T^M/U cap.
PS=(2*S1*S1)**H0
PB=(2*B*B)**H0
PT=U0  # T^M/U <= U <= U0

# Direct H-1/2 caps from exact parity D decompositions.
HDEV_E = PS/F(2) + 2*S1 + RC + F(2,1875)
HDEV_O = PS/F(2) + F(3,2)*S1 + RC + F(2,2500)
HDEV=max(HDEV_E,HDEV_O)

# eta_r = A_target-H_r direct cap /U.
ETA_E = PT/F(2)+PS/F(2)+2*S1+RC+F(2,1875)
ETA_O = PT/F(2)+PS/F(2)+F(3,2)*S1+RC+F(2,2500)
ETA_DIRECT=max(ETA_E,ETA_O)

# Delta=(H_s-H_beta)/U bounds.
DELTA_LO_E = 2*(S0-B)-F(4,1875)-2*RC
DELTA_LO_O = F(3,2)*(S0-B)-F(4,2500)-2*RC
DELTA_HI_E = 2*(S1-B)-F(4,1875)+PS/F(2)+2*RC
DELTA_HI_O = F(3,2)*(S1-B)-F(4,2500)+PS/F(2)+2*RC
DELTA_LO=min(DELTA_LO_E,DELTA_LO_O)
DELTA_HI=max(DELTA_HI_E,DELTA_HI_O)

# Coefficient helper cap: M |A a_r-H_r a_t| / U.
XX=ETA + HHI*(PS+PT)

# Exact contact/slope gates inherited but independently checked as rational inequalities.
# c(s)>16923/100000 throughout, c(s)<17180/100000 throughout.
CLO=F(16923,100000); CHI=F(17180,100000)
# M*c_lower > 88 -> b>=89.
BMIN_GATE=M0*CLO
# h-3b < M(1/2-3c_lower) <= value at M0 < -4, hence integer <= -5.
DYAD_GATE=M0*(F(1,2)-3*CLO)
# admissibility b+3<=h-2 follows from b< M*c_upper+1.
ADMISS_GAP=F(M0-1,2)-5-(M0*CHI+1)

# ---------- symbolic identity gates ----------
def symbolic_gates():
    M,k=sp.symbols('M k', positive=True)
    hb,hs,sm,bm=sp.symbols('hb hs sm bm')
    aa=(1-sm)/M; ab=(1-bm)/M
    ckt=(sp.Rational(1,2)-1)*(hb*aa-hs*ab)
    ct=-hb*aa-hb*sp.Rational(1,2)+hb+hs*ab+hs*sp.Rational(1,2)-hs
    Delta=hs-hb; em=hs*bm-hb*sm
    target=-sp.Rational(1,2)*(Delta*(1-(k+2)/M)+em*(k+2)/M)
    target_ok=sp.expand(ct+k*ckt-target)==0

    A,eb,es,tm=sp.symbols('A eb es tm')
    # eta variables eb=A-hb, es=A-hs; c1 identity.
    ar_b=(1-bm)/M; ar_s=(1-sm)/M; ar_t=(1-tm)/M
    c1=-A*ar_s+A*ar_b+hb*ar_s-hb*ar_t-hs*ar_b+hs*ar_t
    c1_id=eb*(sm-tm)/M+es*(tm-bm)/M
    c1_ok=sp.expand(c1.subs({hb:A-eb,hs:A-es})-c1_id)==0

    r,c,d=sp.symbols('r c d')
    aff=(c+k*d)*r**k-2*(c+(k+1)*d)*r**(k+1)
    aff_id=((1-2*r)*(c+k*d)-2*r*d)*r**k
    aff_ok=sp.expand(aff-aff_id)==0
    target_J=sp.simplify(aff_id.subs(r,sp.Rational(1,2)) + d*sp.Rational(1,2)**k)
    jtarget_ok=target_J==0
    return target_ok,c1_ok,aff_ok,jtarget_ok

SYM=symbolic_gates()

CKT_M_CAP=(DHI+HHI*PS)/F(2)

# ---------- theorem majorants ----------
# Small-left k<=29: U=0 Vandermonde core lower at worst k=29.
CORE_SMALL = F(1,2)*(S0-B)*(T-B)*(T-S1)*(S0*T)**28
# perturbation cap /U. Product coefficient perturbations + beta/source affine + target + c1.
ADEV=U0/F(2)
PROD_ERR=ADEV*(S1-B)+HDEV*(T-B)+HDEV*(T-S0)
BETA_AFF_SMALL=F(6,25)+F(29,M0)*F(6,25)
SRC_AFF_SMALL=F(6,25)+F(29,M0)*F(6,25)
TARGET_SMALL=(DHI+HHI*(PS+PB))/F(2)
C1_SMALL=F(54,100)*PT/M0
SMALL_ERR_U=PROD_ERR+BETA_AFF_SMALL+SRC_AFF_SMALL+TARGET_SMALL+C1_SMALL

# Middle-left 30<=k<=b, normalize by U*T^k.
RMIN=F(7,10)*S0
QMIN=HLO*(T-S1)-HHI*(T-B)*(B/S0)**30
MID_PRODUCT=RMIN*QMIN
MID_TARGET=(DHI+HHI*(PS+PB))/F(2)
MID_AFF=AFF*((F(1,4))**30+(2*S1)**30)
MID_C1=F(54,100)*F(1,2)**(H0+2)/M0
MID_MARGIN=MID_PRODUCT-MID_TARGET-MID_AFF-MID_C1

# Right k>=b+3, normalize by U*T^k.
RIGHT_TARGET=DLO/F(4)-HHI*PS/F(4)
RIGHT_SOURCE=HHI*(T-S0)*S1**3
RIGHT_BS=HHI*(S1-B)*S1**3*F(1,4)**92
RIGHT_AFF=AFF*(F(1,4)**92+(2*S1)**92)
RIGHT_C1=F(54,100)*F(1,2)**(H0+2)/M0
RIGHT_MARGIN=RIGHT_TARGET-RIGHT_SOURCE-RIGHT_BS-RIGHT_AFF-RIGHT_C1

# Central nesting J=E_(b+1)-2E_(b+2), normalize by U*T^(b+1).
J_MAIN=HLO*(T-S1)*(1-S1)*(RMIN*S0)
# beta^b/U<=1/32 -> beta^(b+1)/U<=1/256.
J_BETA=HHI*(T-B)*(1-B)*F(1,256)
J_TARGET=F(71,10000)/M0
# affine transformed coefficient bound: very coarse 1*node^k per beta/source channel.
J_AFF=F(2,1)*(F(1,4)**90+(2*S1)**90)
J_C1=F(54,100)*F(1,2)**(H0+2)/M0
J_MARGIN=J_MAIN-J_BETA-J_TARGET-J_AFF-J_C1

checks={
 'symbolic_target_affine_identity':SYM[0],
 'symbolic_c1_identity':SYM[1],
 'symbolic_affine_J_transform':SYM[2],
 'symbolic_target_J_cancellation':SYM[3],
 'endpoint_c_lower_exact':c_gt(S0,CLO),
 'endpoint_c_upper_exact':c_lt(S1,CHI),
 'd_remainder_cap_tiny':RC < F(1,10**75),
 'H_deviation_below_0p27U':HDEV < ETA,
 'H_lower_gt_0p49':F(1,2)-HDEV*U0>HLO,
 'H_upper_lt_0p51':F(1,2)+HDEV*U0<HHI,
 'eta_direct_below_0p27U':ETA_DIRECT < ETA,
 'delta_lower_gt_0p0043':DELTA_LO > DLO,
 'delta_upper_lt_0p014':DELTA_HI < DHI,
 'XX_below_0p271':XX < XCAP,
 'M_ckt_over_U_below_0p0071':CKT_M_CAP < F(71,10000),
 'b_at_least_89':BMIN_GATE>88,
 'dyadic_beta_b_over_U_le_1_over_32':DYAD_GATE < -4,
 'bplus3_admissible_below_hminus2':ADMISS_GAP>0,
 'small_left_error_below_1U':SMALL_ERR_U<1,
 'small_left_core_beats_U_error':CORE_SMALL>U0,
 'middle_left_margin_positive':MID_MARGIN>0,
 'right_remote_margin_positive':RIGHT_MARGIN>0,
 'central_J_margin_positive':J_MARGIN>0,
}

out={
 'audit':'A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION',
 'contract':{'M_min':M0,'s_min':fs(S0),'s_max':fs(S1),'beta':fs(B),'target':fs(T)},
 'theorem':{
   'remote_left':'E_(M,k)(s)>0 for all admissible k<=b',
   'remote_right':'E_(M,k)(s)<0 for all admissible k>=b+3',
   'central_nesting':'E_(M,b+1)(s)-2 E_(M,b+2)(s)>0',
   'consequence':'complete adjacent-factor sequence has one positive-to-negative variation; global compressed maximizer belongs to {b+1,b+2,b+3}, with only adjacent central ties',
   'b':'ceil(M*c(s)), c(s)=log(2)/(-2 log s)',
 },
 'bounds':{
   'D_remainder_ratio_cap':fs(RC),'D_remainder_ratio_cap_decimal':dec(RC),
   'H_deviation_over_U_cap_derived':fs(HDEV),'H_deviation_over_U_cap_decimal':dec(HDEV),
   'eta_over_U_cap_derived':fs(ETA_DIRECT),'eta_over_U_cap_decimal':dec(ETA_DIRECT),
   'Delta_over_U_lower_derived':fs(DELTA_LO),'Delta_over_U_lower_decimal':dec(DELTA_LO),
   'Delta_over_U_upper_derived':fs(DELTA_HI),'Delta_over_U_upper_decimal':dec(DELTA_HI),
   'small_left_core_lower':fs(CORE_SMALL),'small_left_core_lower_decimal':dec(CORE_SMALL),
   'small_left_error_over_U':fs(SMALL_ERR_U),'small_left_error_over_U_decimal':dec(SMALL_ERR_U),
   'middle_left_margin':fs(MID_MARGIN),'middle_left_margin_decimal':dec(MID_MARGIN),
   'right_remote_margin':fs(RIGHT_MARGIN),'right_remote_margin_decimal':dec(RIGHT_MARGIN),
   'central_J_margin':fs(J_MARGIN),'central_J_margin_decimal':dec(J_MARGIN),
 },
 'checks':checks,
 'verdict':'PASS' if all(checks.values()) else 'FAIL',
 'claim_limits':[
   'This theorem concerns the compressed objective under the frozen reduced contract, not global selection among all lifted LP active-set architectures.',
   'It does not assert global monotonicity of E_(M,k) in k; A87 exactly refutes that stronger claim.',
   'It does not assert E_(b+1)-E_(b+2)>0; that stronger second-secant statement is false in the deep tail (e.g. M=2049,s=133/1000).',
   'It does not assert that b+3 disappears in the tail; E_(b+2)>0 occurs exactly at examples such as M=561,s=129/1000.'
 ]
}
Path('/mnt/data/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_CERTIFICATE_20260911.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'verdict':out['verdict'],'failed':[k for k,v in checks.items() if not v], 'margins':{k:out['bounds'][k] for k in ['middle_left_margin_decimal','right_remote_margin_decimal','central_J_margin_decimal','small_left_core_lower_decimal'] }},indent=2))

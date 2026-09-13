#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2C_SOURCE_BOX_CERTIFICATE_20260913.json'
B=F(1,8); G=F(1,16); T=F(1,2)
S0=F(129,1000); S1=F(133,1000)
M0=521; H0=260
U0=F(1,2**H0)
CLO=F(16923,100000); CHI=F(17180,100000)
QLO=F(9,1000); QHI=F(1,25)

def c_gt(probe:F,r:F)->bool:
    p,q=r.numerator,r.denominator
    return (2**q)*(probe.numerator**(2*p)) > probe.denominator**(2*p)

def c_lt(probe:F,r:F)->bool:
    p,q=r.numerator,r.denominator
    return (2**q)*(probe.numerator**(2*p)) < probe.denominator**(2*p)

DLO=F(43,10000); HHI=F(51,100); AFF=F(9,25)
ETA=F(27,100); XCAP=F(271,1000)
PS=(2*S1*S1)**H0; PB=(2*B*B)**H0; PT=U0

def a113_d_remainder_caps_local():
    den=1-(H0+1)*U0
    q0=(2*S1)**H0
    hu=H0*U0; hpu=(H0+1)*U0
    even=(q0*(1+2*hu+2*hu*S1)+2*hpu*S1)/den
    odd=(F(1,2)*(1+S1)*q0+F(3,2)*hu*(1+S1)*q0+F(3,2)*hpu*S1)/den
    return max(even,odd)

RC=a113_d_remainder_caps_local()
HDEV_E=PS/F(2)+2*S1+RC+F(2,1875)
HDEV_O=PS/F(2)+F(3,2)*S1+RC+F(2,2500)
HDEV=max(HDEV_E,HDEV_O)
ETA_E=PT/F(2)+PS/F(2)+2*S1+RC+F(2,1875)
ETA_O=PT/F(2)+PS/F(2)+F(3,2)*S1+RC+F(2,2500)
ETA_DIRECT=max(ETA_E,ETA_O)
DELTA_LO_E=2*(S0-B)-F(4,1875)-2*RC
DELTA_LO_O=F(3,2)*(S0-B)-F(4,2500)-2*RC
DELTA_LO=min(DELTA_LO_E,DELTA_LO_O)
XX=ETA+HHI*(PS+PT)
AFF_BETA=XX/F(M0)+(1-B)*XX/F(2)+(1-B)*ETA
AFF_SOURCE=XX/F(M0)+(1-S0)*XX/F(2)+(1-S0)*ETA

rplus_max=CHI+F(5,M0)
target_lower=F(1,2)*(DLO*(1-rplus_max)-HHI*(PS+PB)*rplus_max)
prod_src=HHI*(T-S0)*QLO
prod_bs=HHI*(S1-B)*F(1,4)**90*QLO
aff=AFF*(F(1,4)**90+(2*S1)**90)
c1=F(54,100)*F(1,2)**262/F(M0)
E_bplus1_upper_if_Q_le_009=prod_src+prod_bs+aff+c1-target_lower

YMAX=F(1,2**13)
affine_upper=(1-CLO)*8*(S1-G)/1875
inherited_error_cap=F(1,10**70)
q_upper=((S1-G)*YMAX+affine_upper+inherited_error_cap)/(B-G)
Q_upper=q_upper/S0

checks={
    'c_lower_exact':c_gt(S0,CLO),
    'c_upper_exact':c_lt(S1,CHI),
    'b_at_least_89': (2**521)*(S0.numerator**176) > S0.denominator**176,
    'k_bplus1_at_least_90': 89+1>=90,
    'r_kplus2_upper_below_one':rplus_max<1,
    'target_affine_lower_positive':target_lower>0,
    'A113_D_remainder_lt_1e75': RC < F(1,10**75),
    'A113_H_upper_lt_0p51': F(1,2)+HDEV*U0 < HHI,
    'A113_eta_lt_0p27U': ETA_DIRECT < ETA,
    'A113_Delta_over_U_gt_0p0043': DELTA_LO > DLO,
    'A113_MX_over_U_lt_0p271': XX < XCAP,
    'A113_affine_beta_lt_0p36': AFF_BETA < AFF,
    'A113_affine_source_lt_0p36': AFF_SOURCE < AFF,
    'Q_le_0p009_forces_E_bplus1_negative': E_bplus1_upper_if_Q_le_009 < 0,
    'beta_minus_gamma_positive':B>G,
    'Q_upper_lt_0p04': Q_upper < QHI,
    'source_box_nonempty': QLO < QHI,
}
verdict=all(checks.values())
out={
  'audit':'A114B2C_SOURCE_BOX_CERTIFICATE','status':'PASS' if verdict else 'FAIL',
  'contract':{'M_min':M0,'s_min':'129/1000','s_max':'133/1000','phase':'j=b+2 is strict compressed maximizer','pivot':'Phi=F_j^up<0','Q':'s^(b+1)/2^(-h)'},
  'claim':'Under the frozen tail contract, strict compressed b+2 plus Phi<0 implies 9/1000 < Q=s^(b+1)/U < 1/25.',
  'lower_bound':{'logic':'strict b+2 gives E_(b+1)>0; Q<=9/1000 would force E_(b+1)<0','decimal':f'{float(E_bplus1_upper_if_Q_le_009):.18e}'},
  'upper_bound':{'dependency':'A114-B2-B proved Phi<0 => 3j-h>=13, hence Y=beta^j/U<=2^-13','q_upper_decimal':f'{float(q_upper):.18e}','Q_upper_decimal':f'{float(Q_upper):.18e}'},
  'computed_checks':checks,
  'claim_limits':['This is only a source-coordinate box; it does not select a lifted architecture.','Phi=0 is excluded.']
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))

#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2E_PHI_ZERO_ANALYTIC_CERTIFICATE_20260914.json'

B=F(1,8); G=F(1,16); T=F(1,2)
S0=F(129,1000); S1=F(133,1000)
M0=521; H0=260; U0=F(1,2**H0)
CLO=F(16923,100000); CHI=F(17180,100000)
QLO=F(9,1000); QHI=F(1,25)

# --- Reproduce the strict-b+2 lower source-box contradiction ---
DLO=F(43,10000); HHI=F(51,100); AFF=F(9,25)
ETA=F(27,100); XCAP=F(271,1000)
PS=(2*S1*S1)**H0; PB=(2*B*B)**H0; PT=U0

def remcap():
    den=1-(H0+1)*U0
    q0=(2*S1)**H0
    hu=H0*U0; hpu=(H0+1)*U0
    even=(q0*(1+2*hu+2*hu*S1)+2*hpu*S1)/den
    odd=(F(1,2)*(1+S1)*q0+F(3,2)*hu*(1+S1)*q0+F(3,2)*hpu*S1)/den
    return max(even,odd)

RC=remcap()
HDEV=max(PS/F(2)+2*S1+RC+F(2,1875), PS/F(2)+F(3,2)*S1+RC+F(2,2500))
ETA_DIRECT=max(PT/F(2)+PS/F(2)+2*S1+RC+F(2,1875), PT/F(2)+PS/F(2)+F(3,2)*S1+RC+F(2,2500))
DELTA_LO=min(2*(S0-B)-F(4,1875)-2*RC, F(3,2)*(S0-B)-F(4,2500)-2*RC)
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

# --- Strengthen the B2-B separation to Phi<=0 by its own proved margin ---
# If 3j-h<=12, B2-B lower-bounds Phi by this strictly positive number.
DYADIC_MARGIN=(F(1,2**12)*((B-G)*(8*S0)**91-(S1-G))
               -(1-CLO)*8*(S1-G)/1875-F(1,10**70))
YMAX=F(1,2**13)
affine_upper=(1-CLO)*8*(S1-G)/1875
q_upper=((S1-G)*YMAX+affine_upper+F(1,10**70))/(B-G)
Q_upper=q_upper/S0

# --- C-basis coefficient envelopes inherited from C2 once the source box holds ---
RJMAX=CHI+F(3,M0)
LAMMIN=1/(1-CLO); LAMMAX=1/(1-RJMAX)
DENERR=(H0+1)*U0
QTAIL=(2*S1)**H0
WERR=H0*U0*QTAIL
ALO=F(999,1000); AHI=F(1001,1000)
CBLOW=2*(B-WERR); CBUP=2*B/(1-DENERR)
CGLOW=2*(G-WERR); CGUP=2*G/(1-DENERR)
TBCAP=LAMMAX*YMAX/2+(1-LAMMIN/2)*(B*B)**H0
TGCAP=TBCAP  # deliberately loose but uniform for gamma

# For C, delta_gamma=A_gamma p0+(T_gamma-D_gamma)t-C_gamma.
# Gamma+ slack is 2 eps t-delta_gamma.
# Eliminating t with the beta-minus equality gives
# S_(gamma+)^C=(B0-B1*p0)/K_beta,
# B0=C_gamma K_beta-K_(gamma+) C_beta,
# B1=A_gamma K_beta-K_(gamma+) A_beta.

def parity_bounds(parity):
    if parity=='even':
        eU=F(1,1875)
        kblo=2*(B-WERR)-QTAIL+2*eU
        kbup=TBCAP+2*B/(1-DENERR)+2*eU
        kgplo=2*(G-WERR)-QTAIL-2*eU
        kgpup=TGCAP+2*G/(1-DENERR)-2*eU
    else:
        eU=F(1,2500)
        half=F(1,2)*QTAIL*(1+S1)
        kblo=F(3,2)*(B-WERR)-half+2*eU
        kbup=TBCAP+F(3,2)*B/(1-DENERR)+2*eU
        kgplo=F(3,2)*(G-WERR)-half-2*eU
        kgpup=TGCAP+F(3,2)*G/(1-DENERR)-2*eU
    B0lo=CGLOW*kblo-kgpup*CBUP
    B1lo=ALO*kblo-AHI*kgpup
    B1hi=AHI*kbup-ALO*kgplo
    p0lo=B0lo/B1hi
    return kblo,kbup,kgplo,kgpup,B0lo,B1lo,B1hi,p0lo

def dec(x): return f'{float(x):.18e}'

gates={
    'strict_bplus2_Q_lower_contradiction':E_bplus1_upper_if_Q_le_009<0,
    'B2B_stronger_dyadic_margin_positive':DYADIC_MARGIN>F(1,10**6),
    'Phi_nonpositive_forces_3j_minus_h_ge_13':DYADIC_MARGIN>0,
    'source_box_upper_below_1over25':Q_upper<QHI,
    'source_box_nonempty':QLO<QHI,
    'A113_remainder_tiny':RC<F(1,10**75),
    'A113_H_bound':F(1,2)+HDEV*U0<HHI,
    'A113_eta_bound':ETA_DIRECT<ETA,
    'A113_Delta_bound':DELTA_LO>DLO,
    'A113_MX_bound':XX<XCAP,
    'A113_affine_beta_bound':AFF_BETA<AFF,
    'A113_affine_source_bound':AFF_SOURCE<AFF,
}
hard={
    'dyadic_margin_if_3j_minus_h_le_12':dec(DYADIC_MARGIN),
    'E_bplus1_upper_if_Q_le_0p009':dec(E_bplus1_upper_if_Q_le_009),
    'Q_upper':dec(Q_upper),
}
for parity in ('even','odd'):
    kblo,kbup,kgplo,kgpup,B0lo,B1lo,B1hi,p0lo=parity_bounds(parity)
    gates[f'{parity}_Kbeta_positive']=kblo>0
    gates[f'{parity}_Kgamma_plus_positive']=kgplo>0
    gates[f'{parity}_B0_positive']=B0lo>F(1,4000)
    gates[f'{parity}_B1_positive']=B1lo>F(9,100) if parity=='odd' else B1lo>F(12,100)
    gates[f'{parity}_p0_at_gamma_plus_zero_gt_0p0029']=p0lo>F(29,10000)
    hard[parity]={
        'Kbeta_lower':dec(kblo),
        'Kgamma_plus_lower':dec(kgplo),
        'B0_lower':dec(B0lo),
        'B1_lower':dec(B1lo),
        'p0_lower_on_Sgamma_plus_zero':dec(p0lo),
    }

out={
 'audit':'A114B2E_PHI_ZERO_ANALYTIC_CERTIFICATE',
 'status':'PASS' if all(gates.values()) else 'FAIL',
 'contract':{
   'M_min':521,
   's_min':'129/1000',
   's_max':'133/1000',
   'phase':'j=b+2 strict compressed maximizer',
   'boundary':'Phi=F_j^up=0'
 },
 'gate_count':len(gates),
 'pass_count':sum(gates.values()),
 'failed':[k for k,v in gates.items() if not v],
 'gates':gates,
 'hard_margins':hard,
 'exact_logic':[
   'The B2-B proof actually shows 3j-h<=12 => Phi>DYADIC_MARGIN>0; therefore Phi=0 implies 3j-h>=13.',
   'Strict b+2 plus Q<=9/1000 contradicts E_(b+1)>0; together with the dyadic gate this gives 9/1000<Q=s^(j-1)/U<1/25 also at Phi=0.',
   'The exact C/GP bordered pivot gives Phi=0 => S_(gamma+)^C=0 once the nonzero determinant orientations are imported.',
   'Eliminating t with the C beta-minus equality gives S_(gamma+)^C=(B0-B1*p0)/K_beta.',
   'The certified B0>0, B1>0 and K_beta>0 imply p0^C=B0/B1>0 on Phi=0; hence Phi=0 and p0^C=0 cannot intersect in the frozen tail contract.'
 ],
 'scope_note':'This certificate proves the new equality-surface source-box and p0 separation. Full boundary KKT closure is a logical composition with the already-promoted C2 gates, with the gamma-plus slack changed from strict positive to exact zero.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count'],'failed':out['failed'],'hard_margins':hard},indent=2))

#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json

OUT=Path(__file__).with_name('A114B2C2_COMPRESSED_BRANCH_ANALYTIC_CERTIFICATE_20260913.json')
B=F(1,8); G=F(1,16); T=F(1,2)
S0=F(129,1000); S1=F(133,1000)
M0=521; H0=260; U0=F(1,2**H0)
CLO=F(16923,100000); CHI=F(17180,100000)
QLO=F(9,1000); QHI=F(1,25); YMAX=F(1,2**13)
RJMAX=CHI+F(3,M0)
RKMAX=CHI+F(4,M0)
LAMMIN=1/(1-CLO)
LAMMAX=1/(1-RJMAX)
DENERR=(H0+1)*U0
QTAIL=(2*S1)**H0
WERR=H0*U0*QTAIL
ALO=F(999,1000); AHI=F(1001,1000)
CBUP=2*B/(1-DENERR)
CBLOW=2*(B-WERR)
CSLOW=2*(S0-WERR)
CGUP=2*G/(1-DENERR)
TSCAP=LAMMAX*S1*QHI/2 + (1-LAMMIN/2)*(S1*S1)**H0
TBCAP=LAMMAX*YMAX/2 + (1-LAMMIN/2)*(B*B)**H0
TGCAP=TBCAP

def k_bounds(parity:str):
    if parity=='even':
        eU=F(1,1875)
        kslo=2*(S0-WERR)-QTAIL-2*eU
        ksup=TSCAP+2*S1/(1-DENERR)
        kblo=2*(B-WERR)-QTAIL+2*eU
        kbup=TBCAP+2*B/(1-DENERR)+2*eU
        kglo=2*(G-WERR)-QTAIL+2*eU
        kgup=TGCAP+2*G/(1-DENERR)+2*eU
        LH=2*(S0-B-WERR)-QTAIL-F(4,1875)
    else:
        eU=F(1,2500)
        tailhalf=F(1,2)*QTAIL*(1+S1)
        kslo=F(3,2)*(S0-WERR)-tailhalf-2*eU
        ksup=TSCAP+F(3,2)*S1/(1-DENERR)
        kblo=F(3,2)*(B-WERR)-tailhalf+2*eU
        kbup=TBCAP+F(3,2)*B/(1-DENERR)+2*eU
        kglo=F(3,2)*(G-WERR)-tailhalf+2*eU
        kgup=TGCAP+F(3,2)*G/(1-DENERR)+2*eU
        LH=F(3,2)*(S0-B-WERR)-tailhalf-F(4,2500)
    return dict(kslo=kslo,ksup=ksup,kblo=kblo,kbup=kbup,kglo=kglo,kgup=kgup,LH=LH)

def dec(x:F)->str:
    return f'{float(x):.18e}'

gates={}
gates['gap_h_minus_j_integer_ge_168']=((F(1,2)-CHI)*M0-F(7,2)>167)
gates['lambda_lt_1p216']=LAMMAX<F(1216,1000)
gates['neighbor_contact_ratio_lt_0p18']=RKMAX<F(18,100)
gates['tail_q_lt_1e100']=QTAIL<F(1,10**100)
gates['W_error_lt_1e170']=WERR<F(1,10**170)
Adev_source=LAMMAX*S1*QHI*U0+(LAMMAX-1)*S1**M0
Adev_tau=LAMMAX*F(1,2**91)+(LAMMAX-1)*F(1,2**M0)
gates['A_coefficients_within_1e3']=max(Adev_source,Adev_tau)<F(1,1000)
records={}
for par in ('even','odd'):
    q=k_bounds(par)
    det_margin=ALO*q['kslo']-AHI*q['kbup']
    xlo=(CSLOW-(AHI/ALO)*CBUP)/q['ksup']
    xhi=CBUP/q['kblo']
    A0lo=q['kglo']*CBLOW-CGUP*q['kbup']
    A1lo=ALO*q['kblo']-AHI*q['kgup']
    records[par]=dict(q=q,det_margin=det_margin,xlo=xlo,xhi=xhi,A0lo=A0lo,A1lo=A1lo)
    gates[f'{par}_Ks_positive']=q['kslo']>0
    gates[f'{par}_Kb_positive']=q['kblo']>0
    gates[f'{par}_det_negative_margin']=det_margin>F(3,1000)
    gates[f'{par}_Ut_lower_gt_1e2']=xlo>F(1,100)
    gates[f'{par}_gamma_minus_A0_positive']=A0lo>0
    gates[f'{par}_gamma_minus_A1_positive']=A1lo>(F(9,100) if par=='odd' else F(12,100))
    if par=='even':
        gates['even_Ut_upper_lt_1']=xhi<1
        gates['even_qh_base_case']=xlo/U0>3*H0
    else:
        gates['odd_Ut_upper_lt_4over3']=xhi<F(4,3)
        gates['odd_qh_base_case']=xlo/(2*U0)>3*H0
BABSLO=1-RKMAX-F(1,1000)
gates['neighbor_B_abs_gt_4over5']=BABSLO>F(4,5)
ratio90=(B/S0)**90
gap_Mk=(1-CHI)*M0-4
gates['beta_source_power_ratio_lt_1over10']=ratio90<F(1,10)
gates['M_minus_k_gt_400']=gap_Mk>400
gates['remote_source_power_lt_half']=S1**400<F(1,2)
for par in ('even','odd'):
    LH=records[par]['q']['LH']
    gates[f'{par}_H_source_minus_beta_positive']=LH>F(4,1000)
    gates[f'{par}_neighbor_Delta_positive']=BABSLO*LH>F(3,1000)
gates['Hbeta_gt_0p49']=F(1,2)-F(3,10)*U0>F(49,100)
CDIFF=2*(S0-B-WERR)
NZLO=CDIFF*F(49,100)-CBUP*U0
gates['neighbor_Nz_gt_0p003']=NZLO>F(3,1000)
P0UP=CBUP/ALO
for par in ('even','odd'):
    gates[f'{par}_t_half_gt_p0_upper']=records[par]['xlo']/(2*U0)>P0UP
gates['pM_t_coefficient_positive']=1-LAMMAX/2>F(39,100)
maxK=max(max(records[p]['q']['ksup'],records[p]['q']['kbup']) for p in records)
gates['active_dual_Ttau_dominates']=ALO*2**167>AHI*maxK
TAILDER=13*(H0+1)**2*S1**(H0-1)
gates['Q_remainder_tail_derivative_lt_1e3']=TAILDER<F(1,1000)
d0=1-(H0+1)*U0
a0=(2-(H0+2)*U0)/d0
a2=(F(1,2)-H0*U0)/d0
gates['interp_a0_gt_1p99']=a0>F(199,100)
gates['interp_a2_gt_0p49']=a2>F(49,100)
gates['R0_derivative_lt_minus_1p9']=(-a0+TAILDER)<-F(19,10)
gates['R2_derivative_lt_minus_0p2']=(2*S1-a2+TAILDER)<-F(1,5)
DR0=F(19,10)*(S0-B)
DR2=F(1,5)*(S0-B)
gates['Rbeta_minus_Rs_0_gt_19over2500']=DR0>=F(19,2500)
gates['Rbeta_minus_Rs_2_gt_1over1250']=DR2>=F(1,1250)
ADIFF=LAMMAX*(S1**91+B**91)+(LAMMAX-1)*(S1**M0+B**M0)
gates['As_Ab_difference_lt_1e20']=ADIFF<F(1,10**20)
J0=ALO*DR0-2*F(1,10**20)
J2=ALO*DR2-2*F(1,10**20)
gates['Q_checkpoint_core_J0_gt_3over400']=J0>F(3,400)
gates['Q_checkpoint_core_J2_gt_3over5000']=J2>F(3,5000)
small=max(AHI*(records[p]['q']['ksup']+records[p]['q']['kbup'])*2 for p in records)
gates['Q_checkpoint_Ttau_domination']=2**167*J2>small
gates['compressed_full_det_factor_positive']=F(M0,2)>0
gates['gamma_plus_column_insertion_odd_permutation']=(5%2==1)

hard={
 'even':{'minus_Dc_over_U':dec(records['even']['det_margin']),'Ut_lower':dec(records['even']['xlo']),'Ut_upper':dec(records['even']['xhi']),'gamma_minus_A0_over_U':dec(records['even']['A0lo']),'gamma_minus_A1_over_U':dec(records['even']['A1lo'])},
 'odd':{'minus_Dc_over_U':dec(records['odd']['det_margin']),'Ut_lower':dec(records['odd']['xlo']),'Ut_upper':dec(records['odd']['xhi']),'gamma_minus_A0_over_U':dec(records['odd']['A0lo']),'gamma_minus_A1_over_U':dec(records['odd']['A1lo'])},
 'neighbor_Nz_lower':dec(NZLO),'Q_J0_lower':dec(J0),'Q_J2_lower':dec(J2),
}
out={
 'audit':'A114B2C2_COMPRESSED_BRANCH_ANALYTIC_CERTIFICATE',
 'status':'PASS' if all(gates.values()) else 'FAIL',
 'contract':{'M_min':521,'s_min':'129/1000','s_max':'133/1000','phase':'j=b+2 strict compressed maximizer','pivot':'Phi=F_j^up<0','branch':'p0^C>0','source_box':'9/1000 < s^(j-1)/U < 1/25'},
 'gate_count':len(gates),'pass_count':sum(gates.values()),'failed':[k for k,v in gates.items() if not v],
 'gates':gates,'hard_margins':hard,
 'exact_identities_used':['A81 two-variable compressed reduction','det(B_C)=(M/2)*Delta_C after exact block elimination','p_(j+1)^(G+)=-S_(gamma+)^C*det(B_C)/det(B_G+) (odd five-column insertion)','adjacent simplex exchange identity for compressed reduced costs','five-dimensional ECT zero budget for P and Q reduced-cost functions'],
 'logical_consequences':['p0^C>0 plus the bounds gives every C basic mass and t strictly positive','both active duals are strictly positive','gamma- slack is strictly positive from A0+A1*p0 with A0,A1>0','Phi<0 and positive determinant orientations give gamma+ slack >0','strict compressed maximality plus positive neighboring interior masses gives r_C(p_(j-1)),r_C(p_(j+1))>0','Q interpolation remainders give r_C(q0),r_C(q2)>0','ECT closes all remaining P/Q reduced costs'],
 'claim_limits':['strict inequalities only','Phi=0 excluded','p0^C=0 excluded','QI/QA edge not addressed','frozen source/tail contract only','no physical interpretation']
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count'],'failed':out['failed'],'hard_margins':hard},indent=2))

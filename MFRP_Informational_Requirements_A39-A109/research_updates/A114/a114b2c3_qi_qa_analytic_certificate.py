#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2C3_QI_QA_ANALYTIC_CERTIFICATE_20260914.json'
B=F(1,8); G=F(1,16); T=F(1,2)
S0=F(129,1000); S1=F(133,1000)
M0=521; H0=260; U0=F(1,2**H0)
CLO=F(16923,100000); CHI=F(17180,100000)
QLO=F(9,1000); QHI=F(1,25); YMAX=F(1,2**13)
RLO=S0*QLO; RHI=S1*QHI
RJMAX=CHI+F(3,M0)
LAMMIN=1/(1-CLO); LAMMAX=1/(1-RJMAX)
NUMAX=1/(M0*(1-RJMAX)); MUMAX=1+NUMAX
DENERR=(H0+1)*U0
QTAIL=(2*S1)**H0
WERR=H0*U0*QTAIL
LERR=(H0*U0*S1+(H0+1)*U0*QTAIL*(1+S1))/(1-DENERR)
CERR=2*WERR+2*S1*DENERR/(1-DENERR)
ZMAX=YMAX/F(2**91)
REMOTE_S=(2*S1*S1)**H0
REMOTE_B=(2*B*B)**H0
REMOTE_G=(2*G*G)**H0
REMOTE_T=F(1,2**400)
COEF_ERR=F(1,10**28)
COMPOSITE_ERR=F(1,10**23)
WMIN=F(2**168)

def C_bounds(r:F):
    return 2*(r-WERR), 2*r/(1-DENERR)

def L_bounds(rlo:F,rhi:F|None=None):
    if rhi is None: rhi=rlo
    return 1-2*rhi-LERR, 1-2*rlo+LERR

def K_bounds(parity:str,name:str):
    scale=1875 if parity=='even' else 2500
    eps2=F(2,scale)
    if name=='s':
        clo=2*(S0-WERR); chi=2*S1/(1-DENERR)
        tail=(2*S1)**H0
        tlo=LAMMIN*RLO/2
        thi=LAMMAX*RHI/2+(1-LAMMIN/2)*REMOTE_S
        if parity=='even':
            return tlo+clo-tail-eps2, thi+chi
        return tlo+F(3,4)*clo-F(1,2)*(1+S1)*tail-eps2, thi+F(3,4)*chi
    r=B if name=='b' else G
    clo,chi=C_bounds(r)
    tail=(2*r)**H0
    pmax=YMAX if name=='b' else ZMAX
    remote=REMOTE_B if name=='b' else REMOTE_G
    thi=LAMMAX*pmax/2+(1-LAMMIN/2)*remote
    if parity=='even':
        return clo-tail+eps2, thi+chi+eps2
    return F(3,4)*clo-F(1,2)*(1+r)*tail+eps2, thi+F(3,4)*chi+eps2

def A_bounds(name:str):
    if name=='s':
        return QLO*(1-MUMAX*S1), QHI*(1-S0)+NUMAX*REMOTE_S
    if name=='b':
        return F(0),8*YMAX*(1-B)+NUMAX*REMOTE_B
    return F(0),16*ZMAX*(1-G)+NUMAX*REMOTE_G

def dec(x:F)->str:
    return f'{float(x):.18e}'

Lslo,Lshi=L_bounds(S0,S1); Lblo,Lbhi=L_bounds(B); Lglo,Lghi=L_bounds(G)
Aslo,Ashi=A_bounds('s'); Ablo,Abhi=A_bounds('b'); Aglo,Aghi=A_bounds('g')
Cblo,Cbhi=C_bounds(B); Cglo,Cghi=C_bounds(G)
gAlo=2-MUMAX; gAhi=1+NUMAX*REMOTE_T
gTlo=LAMMIN/2; gThi=LAMMAX/2+(1-LAMMIN/2)*REMOTE_T
Cslo=2*(S0-WERR); Cshi=2*S1/(1-DENERR)

gates={}; hard={}
gates['gap_h_minus_j_ge_168']=((F(1,2)-CHI)*M0-F(7,2)>167)
gates['M_minus_j_gt_400']=((1-RJMAX)*M0>400)
gates['Ymax_is_2^-13']=YMAX==F(1,2**13)
gates['Y_lower_relation_8U2_compatible']=(8*U0*U0 < YMAX)
gates['Zmax_tiny']=ZMAX<F(1,10**30)
gates['L_remainder_lt_1e28']=LERR<COEF_ERR
gates['C_remainder_lt_1e28']=CERR<COEF_ERR
gates['Ag_omitted_leading_term_lt_1e28']=Aghi<COEF_ERR
gates['target_remote_lt_1e28']=REMOTE_T<COEF_ERR
A_SOURCE_REMOTE=NUMAX*REMOTE_S
A_BETA_REMOTE=NUMAX*REMOTE_B
K_SOURCE_DEV=max(REMOTE_S+CERR+QTAIL, REMOTE_S+F(3,4)*CERR+F(1,2)*(1+S1)*QTAIL)
K_BETA_DEV=max(REMOTE_B+CERR+(2*B)**H0, REMOTE_B+F(3,4)*CERR+F(1,2)*(1+B)*(2*B)**H0)
K_GAMMA_DEV=max(REMOTE_G+CERR+(2*G)**H0, REMOTE_G+F(3,4)*CERR+F(1,2)*(1+G)*(2*G)**H0)
gates['As_remote_lt_1e28']=A_SOURCE_REMOTE<COEF_ERR
gates['Ab_remote_lt_1e28']=A_BETA_REMOTE<COEF_ERR
gates['K_source_deviation_lt_1e28']=K_SOURCE_DEV<COEF_ERR
gates['K_beta_deviation_lt_1e28']=K_BETA_DEV<COEF_ERR
gates['K_gamma_deviation_lt_1e28']=K_GAMMA_DEV<COEF_ERR
gates['all_reduced_coefficients_lt_2']=max(Ashi,Abhi,Aghi,Lghi,2*S1/(1-DENERR),gAhi,gThi)<2
gates['composite_error_dominates']=COMPOSITE_ERR>10000*COEF_ERR

for parity in ('even','odd'):
    scale=1875 if parity=='even' else 2500
    delta=F(2,scale)
    Kslo,Kshi=K_bounds(parity,'s'); Kblo,Kbhi=K_bounds(parity,'b'); Kglo,Kghi=K_bounds(parity,'g')
    const=F(2) if parity=='even' else F(3,2)
    Dq_lo=const*(S0-B)-LAMMAX*Lshi*YMAX/2-delta*(Lbhi+Lshi)-COMPOSITE_ERR
    Dq_hi=const*(S1-B)+LAMMAX*Lbhi*RHI/2+COMPOSITE_ERR
    Nx_lo=2*(S0-B)-COMPOSITE_ERR
    Nx_hi=2*(S1-B)+COMPOSITE_ERR
    x_lo=Nx_lo/Dq_hi; x_hi=Nx_hi/Dq_lo
    aa_qi_hi=gThi*Lbhi/Dq_lo
    gap_qi_lo=gTlo*(Lblo-Lshi)/Dq_hi
    gates[f'{parity}_Dq_positive']=Dq_lo>F(1,250)
    gates[f'{parity}_Dq_upper_lt_0p02']=Dq_hi<F(1,50)
    gates[f'{parity}_QI_x_positive']=x_lo>F(2,5)
    gates[f'{parity}_QI_x_lt_4']=x_hi<4
    gates[f'{parity}_QI_alpha_norm_lt_100']=aa_qi_hi<100
    gates[f'{parity}_QI_dual_gap_gt_quarter']=gap_qi_lo>F(1,4)
    gates[f'{parity}_QI_alphaR_lt_3over5']=aa_qi_hi*RHI<F(3,5)
    gates[f'{parity}_C_QI_orientation_opposite']=Dq_lo>0
    gp0=Cglo-Cbhi*(Kghi-F(4,scale))/Kblo
    gates[f'{parity}_QI_gamma_plus_threshold_positive']=gp0>F(1,1000)
    if parity=='even': q1_core=4*LAMMIN*(1-F(1,2**91))-1
    else: q1_core=4*LAMMIN*(1-F(1,2**91))-F(1+B,2)
    gates[f'{parity}_QI_q1_dominance']=q1_core>3
    gates[f'{parity}_QI_q1_denominator_positive']=(B-G-H0*(B**H0))>F(3,50)
    z_hi=Kbhi*4/Lblo
    gates[f'{parity}_QI_q0_lt_2']=z_hi<2
    gates[f'{parity}_QI_q1_lt_3']=2/(1-DENERR)<3
    if parity=='even': gates[f'{parity}_QI_qh_positive']=x_lo-U0*((H0+1)*2+H0*3)>0
    else: gates[f'{parity}_QI_qh_positive']=x_lo/2-U0*((H0+1)*2+H0*3)>0
    pj1_qi=1-2*NUMAX-2*aa_qi_hi*(RHI*(1-S0)+NUMAX*REMOTE_S)
    gates[f'{parity}_QI_rc_pjp1_positive']=pj1_qi>F(1,20)
    gates[f'{parity}_QI_p0_zero_budget_margin']=gap_qi_lo*WMIN>2
    De_lo=Aslo*Kblo-Abhi*Kshi
    gates[f'{parity}_De_positive']=De_lo>F(1,1000)
    Dbg_lo=Lglo*Kblo-Lbhi*Kghi
    H_hi=Kshi*Lghi-Lslo*Kglo
    Dqa_lo=Aslo*Dbg_lo-Abhi*H_hi
    Dqa_hi=Ashi*(Lghi*Kbhi-Lblo*Kglo)+Abhi*H_hi+Aghi*(Kshi*Lbhi-Lslo*Kbhi)
    gates[f'{parity}_Dqa_positive']=Dqa_lo>F(3,5000)
    gates[f'{parity}_Dqa_upper_lt_1over200']=Dqa_hi<F(1,200)
    ycoef_dx=[16*muv*sv-muv-128*sv+8 for sv,muv in product((S0,S1),(F(1),MUMAX))]
    zcoef_dx=[-16*muv*sv+2*muv+256*sv-32 for sv,muv in product((S0,S1),(F(1),MUMAX))]
    Dx_lo=(QLO*(1-MUMAX*S1)+YMAX*min(ycoef_dx)+ZMAX*min(zcoef_dx))/8-COMPOSITE_ERR
    bracket=-RLO+YMAX*(16*S1-1)
    Da_hi=(LAMMIN*bracket+4*delta)/16+COMPOSITE_ERR
    wx_hi=Da_hi/Dx_lo
    pjt_frac=LAMMIN/2-MUMAX*wx_hi
    x_qa_lo=Dx_lo/Dqa_hi
    gates[f'{parity}_QA_Dx_positive']=Dx_lo>F(4,5000)
    gates[f'{parity}_QA_w_over_x_lt_quarter']=wx_hi<F(1,4)
    gates[f'{parity}_QA_pj_over_t_gt_third']=pjt_frac>F(1,3)
    gates[f'{parity}_QA_x_positive']=x_qa_lo>F(3,20)
    if parity=='even': qa_q1_core=8*pjt_frac*(1-F(1,2**91))-1
    else: qa_q1_core=8*pjt_frac*(1-F(1,2**91))-F(1+B,2)
    gates[f'{parity}_QA_q1_dominance']=qa_q1_core>F(3,2)
    gates[f'{parity}_QA_q1_denominator_positive']=(B-G-H0*(B**H0))>F(3,50)
    gates[f'{parity}_QA_q1_lt_3']=2/(1-DENERR)<3
    if parity=='even': gates[f'{parity}_QA_qh_positive']=x_qa_lo-U0*((H0+1)*2+H0*3)>0
    else: gates[f'{parity}_QA_qh_positive']=x_qa_lo/2-U0*((H0+1)*2+H0*3)>0
    Ns_lo=-gThi*Abhi*Lghi + gAlo*(Kblo*Lglo-Kghi*Lbhi)
    Ns_hi=gThi*Aghi*Lbhi + gAhi*(Kbhi*Lghi-Kglo*Lblo)
    Nb_lo=-gThi*Aghi*Lshi + gTlo*Aslo*Lglo + gAlo*(Kglo*Lslo-Kshi*Lghi)
    Nb_hi=gThi*Ashi*Lghi + gAhi*(Kghi*Lshi-Kslo*Lglo)
    gates[f'{parity}_QA_yalpha_positive']=Ns_lo>F(9,100)
    gates[f'{parity}_QA_ybeta_positive']=Nb_hi<-F(2,25)
    aa_qa_hi=Ns_hi/Dqa_lo
    ab_qa_hi=(-Nb_lo)/Dqa_lo
    gates[f'{parity}_QA_alpha_norm_lt_150']=aa_qa_hi<150
    gates[f'{parity}_QA_beta_norm_lt_250']=ab_qa_hi<250
    Nsum0=(QLO*LAMMIN*(1-2*S1)-6*YMAX*LAMMAX*(16*S1-1)+4*delta*(2-MUMAX))/16
    Nsum_lo=Nsum0-COMPOSITE_ERR
    gates[f'{parity}_QA_dual_sum_numerator_gt_0p0006']=Nsum_lo>F(3,5000)
    gap_qa_lo=Nsum_lo/Dqa_hi
    gates[f'{parity}_QA_dual_gap_gt_0p1']=gap_qa_lo>F(1,10)
    def ycoef(sv,Qv,lv,muv):
        if parity=='even':
            return (56*Qv*lv*sv-49*Qv*lv-32*delta*muv*sv+30*delta*muv+256*delta*sv-240*delta-32*muv*sv+2*muv+256*sv-16)
        return (112*Qv*lv*sv-98*Qv*lv-64*delta*muv*sv+60*delta*muv+512*delta*sv-480*delta-48*muv*sv+3*muv+384*sv-24)
    yc_min=min(ycoef(sv,qv,lv,muv) for sv,qv,lv,muv in product((S0,S1),(QLO,QHI),(LAMMIN,LAMMAX),(F(1),MUMAX)))
    gates[f'{parity}_QA_Qalpha_Ycoefficient_positive']=yc_min>12
    if parity=='even': QNs_minus_D=QLO*2*(1+delta)*(1-MUMAX*(1-S0))/16-COMPOSITE_ERR
    else: QNs_minus_D=QLO*(3+4*delta)*(1-MUMAX*(1-S0))/32-COMPOSITE_ERR
    gates[f'{parity}_QA_Qalpha_gt_1']=QNs_minus_D>F(1,10000)
    pjp1_qa=(2*(1-S1)**2-16*250*YMAX*(1-B)**2-32*150*ZMAX*(1-G)**2-1)
    pjm2_qa=((1-S1)**2/(4*S1)-16*250*YMAX*(1-B)**2-64*150*ZMAX*(1-G)**2-F(1,4))
    gates[f'{parity}_QA_rc_pjp1_positive']=pjp1_qa>F(1,10)
    gates[f'{parity}_QA_rc_pjm2_positive']=pjm2_qa>F(3,4)
    gates[f'{parity}_QA_p0_zero_budget_margin']=gap_qa_lo*WMIN>2
    gates[f'{parity}_QA_affine_slope_negative']=150*RHI<F(4,5)
    hard[parity]={
        'Dq_lower':dec(Dq_lo),'Dq_upper':dec(Dq_hi),'QI_x_lower':dec(x_lo),'QI_x_upper':dec(x_hi),
        'QI_alpha_norm_upper':dec(aa_qi_hi),'QI_dual_gap_lower':dec(gap_qi_lo),'QI_gamma_plus_threshold':dec(gp0),
        'QI_pjp1_margin':dec(pj1_qi),'De_lower':dec(De_lo),'Dqa_lower':dec(Dqa_lo),'Dqa_upper':dec(Dqa_hi),
        'QA_alpha_norm_upper':dec(aa_qa_hi),'QA_beta_norm_upper':dec(ab_qa_hi),'QA_dual_gap_lower':dec(gap_qa_lo),
        'QA_Qalpha_minus_1_numerator':dec(QNs_minus_D),'QA_Dx_lower':dec(Dx_lo),'QA_w_over_x_upper':dec(wx_hi),
        'QA_pj_over_t_lower':dec(pjt_frac),'QA_x_lower':dec(x_qa_lo),'QA_pjp1_margin':dec(pjp1_qa),'QA_pjm2_margin':dec(pjm2_qa)}

gates['target_remote_lt_eta_over_100']=(F(1,2**399)<F(1,40000))
gates['beta_remote_times_h_tiny']=(800*U0**5*(2*H0+1)<F(1,10**300))
gates['gamma_remote_times_h_tiny']=(800*U0**7*(2*H0+1)<F(1,10**450))

structural=[
 'C and QI have the same Cramer numerator N=C_s K_b-C_b K_s; D_C<0 (C2) and D_Q>0, so p0^C<0 implies q0^QI>0.',
 'For E, r_E(q0)=N_g/D_E and for QI r_QI(p_(j-1))=-N_g/D_Q. Hence r_E(q0)<0 with D_E,D_Q>0 implies r_QI(p_(j-1))>0.',
 'For QA, y_(gamma-)=-N_g/D_QA. Hence r_E(q0)<0 with D_E,D_QA>0 implies y_(gamma-)>0.',
 'The QA Schur complement is D_QA/D_Q>0 and U p_(j-1)^QA=-(D_Q/D_QA) Gamma. Hence Gamma<0 implies p_(j-1)^QA>0.',
 'E and QI lie on the same alpha+/beta- edge. E has S_(gamma-)>0, QI has Gamma<0, p_(j-1)^E>0 and q0^QI>0; therefore the gamma=0 cut has q0^QA,p_(j-1)^QA>0. Common QA masses are protected separately by the certified Dx, w/x, beta-gamma and Q-block inequalities; no positivity of the QI endpoint is assumed on the QA side.',
 'For QI, Q reduced costs are -y_alpha R_s(x) on nodes {0,1,h,h+1}; generalized-Vandermonde orientation gives R_s(x)<0 at every nonbasic integer.',
 'For QA, Q reduced costs are -y_alpha R_s(x)+y_gamma R_gamma(x), with R_s(x)<0<R_gamma(x) because gamma<beta<s<tau.',
 'QI P reduced costs lie in the 5-dimensional ECT span {1,x,s^x,beta^x,tau^x}; QA P reduced costs lie in the 6-dimensional span adding gamma^x.',
 'The certified P sentinels, negative left limits, and for QA the negative right affine tail exhaust the ECT zero budgets and force every nonbasic P reduced cost positive.'
]
verdict=all(gates.values())
out={'audit':'A114B2C3_QI_QA_ANALYTIC_CERTIFICATE','date':'2026-09-14','status':'PASS' if verdict else 'FAIL','contract':{'M_min':521,'s_min':'129/1000','s_max':'133/1000','phase':'j=b+2 strict compressed maximizer','pivot':'Phi=F_j^up<0','residual_premises':['p0^C<0','r_E(q0)<0'],'classifier':'Gamma=S_(gamma-)^QI'},'claim':'Under the frozen strict b+2 negative-pivot residual interior, Gamma>0 gives QI and Gamma<0 gives QA; both satisfy complete strict KKT. Gamma=0 is excluded from strict classification.','gate_count':len(gates),'pass_count':sum(gates.values()),'failed':[k for k,v in gates.items() if not v],'gates':gates,'hard_margins':hard,'structural_identities':structural,'claim_limits':['strict Gamma sign only','p0^C=0 excluded','r_E(q0)=0 excluded','Phi=0 excluded','frozen source/tail contract only','finite controls are regression evidence only','no physical interpretation']}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count'],'failed':out['failed'],'hard_margins':hard},indent=2))

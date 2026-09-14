#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OUT=HERE/'A114B2D_BOUNDARY_ANALYTIC_CERTIFICATE_20260914.json'

B=F(1,8); S0=F(129,1000); S1=F(133,1000)
M0=521; H0=260; U0=F(1,2**H0)
CLO=F(16923,100000); CHI=F(17180,100000)
QHI=F(1,25); YMAX=F(1,2**13)
RJMAX=CHI+F(3,M0)
LAMMIN=1/(1-CLO); LAMMAX=1/(1-RJMAX)
DENERR=(H0+1)*U0
QTAIL=(2*S1)**H0
WERR=H0*U0*QTAIL
CBLOW=2*(B-WERR)
CBUP=2*B/(1-DENERR)
TBCAP=LAMMAX*YMAX/2+(1-LAMMIN/2)*(B*B)**H0

def kb_bounds(parity):
    if parity=='even':
        eU=F(1,1875)
        lo=2*(B-WERR)-QTAIL+2*eU
        hi=TBCAP+2*B/(1-DENERR)+2*eU
    else:
        eU=F(1,2500)
        tailhalf=F(1,2)*QTAIL*(1+S1)
        lo=F(3,2)*(B-WERR)-tailhalf+2*eU
        hi=TBCAP+F(3,2)*B/(1-DENERR)+2*eU
    return lo,hi

def dec(q): return f'{float(q):.18e}'

gates={}
hard={}
for parity in ('even','odd'):
    kblo,kbhi=kb_bounds(parity)
    # On p0^C=0, K_beta t=C_beta, so x=Ut=C_beta/(K_beta/U).
    xlo=CBLOW/kbhi
    xhi=CBUP/kblo
    gates[f'{parity}_Kbeta_positive']=kblo>0
    if parity=='even':
        gates['even_Ut_gt_0p995']=xlo>F(995,1000)
        gates['even_Ut_lt_1']=xhi<1
        # q1=2(1-Ut)/(1-(h+1)U)
        gates['even_q1_positive']=(1-xhi)>0 and (1-(H0+1)*U0)>0
        gates['even_qh_positive']=xlo/U0>3*H0
    else:
        gates['odd_Ut_gt_1p327']=xlo>F(1327,1000)
        gates['odd_Ut_lt_4over3']=xhi<F(4,3)
        # q1=(2-3 Ut/2)/(1-(h+1)U)
        gates['odd_q1_positive']=(2-F(3,2)*xhi)>0 and (1-(H0+1)*U0)>0
        gates['odd_qh_positive']=xlo/(2*U0)>3*H0
    hard[parity]={
        'Kbeta_over_U_lower':dec(kblo),
        'Kbeta_over_U_upper':dec(kbhi),
        'Ut_lower_at_p0_zero':dec(xlo),
        'Ut_upper_at_p0_zero':dec(xhi),
    }

gates['lambda_lt_1p216']=LAMMAX<F(1216,1000)
gates['pM_coefficient_gt_0p39']=1-LAMMAX/2>F(39,100)
gates['denominator_1_minus_h1U_positive']=1-(H0+1)*U0>0

out={
 'audit':'A114B2D_BOUNDARY_ANALYTIC_CERTIFICATE',
 'status':'PASS' if all(gates.values()) else 'FAIL',
 'contract':{
   'M_min':521,
   's_min':'129/1000',
   's_max':'133/1000',
   'phase':'strict compressed b+2, Phi<0',
   'boundary':'p0^C=0'
 },
 'gate_count':len(gates),
 'pass_count':sum(gates.values()),
 'failed':[k for k,v in gates.items() if not v],
 'gates':gates,
 'hard_margins':hard,
 'exact_identity':'At p0^C=0 the beta row is K_beta t=C_beta, hence Ut=C_beta/(K_beta/U).',
 'consequences':[
   't>0 and p_j=(lambda/2)t>0.',
   'p_M=(1-lambda/2)t>0.',
   'The even/odd q1 formulas are strictly positive directly on the boundary.',
   'The inherited central-Q estimates give q_h>0 and then q_(h+1)>0.'
 ],
 'scope_note':'D2 and D3 are closed by exact pivot identities, ECT/duality, and already-promoted C1/C3 strict margins; this certificate adds the only new uniform numeric boundary margins needed by D1.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'gate_count':out['gate_count'],'pass_count':out['pass_count'],'failed':out['failed'],'hard_margins':hard},indent=2))
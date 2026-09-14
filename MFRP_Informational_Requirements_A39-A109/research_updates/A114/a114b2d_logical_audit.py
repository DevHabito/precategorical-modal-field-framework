#!/usr/bin/env python3
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
TH=(HERE/'A114B2D_INTERNAL_ZERO_BOUNDARY_THEOREM_20260914.md').read_text(encoding='utf-8')
HARD=(HERE/'A114B2D_BOUNDARY_HARDENING_NOTE_20260914.md').read_text(encoding='utf-8')
C1=(HERE/'A114B2C1_ENDPOINT_RELEASED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md').read_text(encoding='utf-8')
C2=(HERE/'A114B2C2_COMPRESSED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md').read_text(encoding='utf-8')
C3=(HERE/'A114B2C3_QI_QA_RESIDUAL_BRANCH_THEOREM_20260914.md').read_text(encoding='utf-8')
REG=json.loads((HERE/'A114B2D_EXACT_BOUNDARY_REGRESSION_20260914.json').read_text(encoding='utf-8'))
ANA=json.loads((HERE/'A114B2D_BOUNDARY_ANALYTIC_CERTIFICATE_20260914.json').read_text(encoding='utf-8'))
OUT=HERE/'A114B2D_LOGICAL_AUDIT_20260914.json'

checks={
 'status_is_conditional_boundary_theorem':'PROVED conditional boundary theorem' in TH,
 'strict_bplus2_contract':'j=b+2' in TH and 'strict compressed maximizer' in TH,
 'phi_negative_premise':'\\Phi=F_j^{\\rm up}<0' in TH,
 'D1_p0_zero_present':'p_0^C=0' in TH,
 'D1_unique_primal_claim':'D1. The `p_0^C=0` boundary has a unique primal optimum' in TH,
 'D1_C_E_QI_coalescence':'`C`, `E`, and `QI`' in TH and 'same primal point' in TH,
 'D1_dual_overclaim_excluded':'does not assert that the `E` or `QI` dual basis is feasible' in TH,
 'D1_direct_Ut_hardening':'0.9954<Ut<0.9958<1' in HARD and '1.3271<Ut<1.3277<4/3' in HARD,
 'D2_residual_zero_premises':'p_0^C<0' in TH and 'r_E(q_0)=0' in TH,
 'D2_zero_reduced_cost_edge':'nonbasic variable with zero reduced cost' in TH,
 'D2_ECT_four_roots':'0,\\quad1,\\quad h,\\quad h+1' in TH,
 'D2_q2_checkpoint':'r_E(q_2)>0' in TH,
 'D2_nonunique_primal':'primal optimum is **not unique**' in TH,
 'D2_three_gamma_endpoint_cases':'If `Gamma>0`' in TH and 'If `Gamma=0`' in TH and 'If `Gamma<0`' in TH,
 'D2_gamma_zero_no_illegal_D3_dependency':'At `Gamma=0`, use the D3' not in TH and 'exact Schur identity `p_(j-1)^QA=0`' in TH,
 'D2_entire_optimal_face_hardened':'complete optimal set' in HARD and 'no hidden second optimal direction' in HARD and '\\operatorname{conv}\\{E,QI\\}' in HARD and '\\operatorname{conv}\\{E,QA\\}' in HARD,
 'D3_full_premises':'r_E(q_0)<0' in TH and '\\Gamma=0' in TH,
 'D3_QI_QA_coalescence':'common `QI=QA` primal point' in TH,
 'D3_unique_primal':'D3. The `Gamma=0` boundary has a unique primal optimum' in TH,
 'D3_positive_gamma_dual':'y_{\\gamma-}^{QA}' in TH and '>0' in TH,
 'outer_Phi_zero_left_open':'outer `Phi=0` boundary' in TH and 'not' in TH.lower(),
 'no_universal_s_order_claim':'does not claim' in TH.lower() and 'universal monotone ordering' in TH,
 'finite_controls_regression_only':'regression/falsification evidence' in TH,
 'no_physical_claim':'any physical interpretation' in TH,
 'false_convexity_route_absent':'positive because QA lies between two primal-feasible E/QI endpoints' not in TH,
 'dependencies_are_promoted':('PROVED conditional branch theorem' in C1 and 'PROVED conditional branch theorem' in C2 and 'PROVED conditional branch theorem' in C3),
 'regression_passes':REG.get('status')=='PASS' and REG.get('gate_count')==30 and REG.get('pass_count')==30,
 'boundary_analytic_certificate_passes':ANA.get('status')=='PASS' and ANA.get('gate_count')==13 and ANA.get('pass_count')==13 and not ANA.get('failed'),
}

out={
 'audit':'A114B2D_LOGICAL_COMPOSITION_AUDIT',
 'status':'PASS' if all(checks.values()) else 'FAIL',
 'check_count':len(checks),
 'pass_count':sum(checks.values()),
 'failed':[k for k,v in checks.items() if not v],
 'checks':checks,
 'scope':['strict compressed b+2','Phi<0','internal boundaries p0^C=0, r_E(q0)=0, Gamma=0'],
 'open_boundary':['Phi=0'],
 'forbidden_promotions':['universal monotone ordering of zero surfaces in s','strict uniqueness on equality sets','physical interpretation']
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'check_count':out['check_count'],'pass_count':out['pass_count'],'failed':out['failed']},indent=2))
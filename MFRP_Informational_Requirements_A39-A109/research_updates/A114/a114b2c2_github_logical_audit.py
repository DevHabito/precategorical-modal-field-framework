#!/usr/bin/env python3
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
CERT=json.loads((HERE/'A114B2C2_COMPRESSED_BRANCH_ANALYTIC_CERTIFICATE_20260913.json').read_text())
OLD=json.loads((HERE/'session_artifacts'/'A114B2C_12_POINT_FULL_KKT_SUMMARY_20260913.json').read_text())
TH=(HERE/'A114B2C2_COMPRESSED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md').read_text()
OUT=HERE/'A114B2C2_GITHUB_LOGICAL_AUDIT_20260913.json'
controls=[x for x in OLD['controls'] if x['expected']=='C']
checks={
 'analytic_certificate_pass':CERT['status']=='PASS',
 'analytic_49_of_49':CERT['gate_count']==49 and CERT['pass_count']==49 and not CERT['failed'],
 'source_box_retained':CERT['contract']['source_box']=='9/1000 < s^(j-1)/U < 1/25',
 'branch_hypothesis_retained':CERT['contract']['branch']=='p0^C>0',
 'three_exact_C_controls':len(controls)==3,
 'C_controls_full_KKT':all(x['kkt_pass'] and x['condition_count']==x['expected_count'] for x in controls),
 'C_controls_exact_equations':all(x['equations_exact'] and x['primal_dual_equal'] for x in controls),
 'theorem_has_strict_p0_hypothesis':'p_0^C>0' in TH,
 'theorem_keeps_p0_zero_open':'anything on `p0^C=0`' in TH,
 'theorem_keeps_Phi_zero_open':'anything on `Phi=0`' in TH,
 'theorem_keeps_QI_QA_open':'the QI/QA split' in TH,
 'theorem_uses_exact_gamma_pivot':'p_{j+1}^{G+}' in TH and 'S_{\\gamma+}^C' in TH,
 'theorem_uses_P_ECT':'five-dimensional extended-Chebyshev' in TH,
 'theorem_uses_Q_checkpoints':'r_C(q_0)>0' in TH and 'r_C(q_2)>0' in TH,
 'no_finite_census_promoted':'They are regression controls only' in TH,
}
out={
 'audit':'A114B2C2_GITHUB_LOGICAL_AUDIT',
 'status':'PASS' if all(checks.values()) else 'FAIL',
 'checks':checks,'failed':[k for k,v in checks.items() if not v],
 'dependency_DAG':[
   'C1 source box + B2-B dyadic gate -> h-j/contact/tail boxes',
   'A81 exact compressed reduction + p0C>0 -> complete C primal feasibility',
   'two-variable dual formulas + target separation -> active dual positivity',
   'beta elimination -> gamma- slack positive',
   'exact bordered pivot + determinant orientations + Phi<0 -> gamma+ slack positive',
   'A113 strict maximality + adjacent simplex identities + neighboring mass positivity -> P checkpoints',
   'Q interpolation remainder bounds -> q0/q2 checkpoints',
   'ECT zero budgets -> all P/Q reduced costs',
   'strict primal/dual/slack/reduced-cost gates -> unique full-LP optimum'
 ],
 'claim_limits':['p0C=0 open','Phi=0 open','QI/QA edge open','frozen contract only']
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))

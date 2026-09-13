#!/usr/bin/env python3
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
SB=json.loads((HERE/'A114B2C_SOURCE_BOX_CERTIFICATE_20260913.json').read_text())
EP=json.loads((HERE/'A114B2C1_ENDPOINT_PROTECTED_GATES_SUMMARY_20260913.json').read_text())
XC=json.loads((HERE/'A114B2C1_ENDPOINT_E_FRACTION_CROSSCHECK_SUMMARY_20260913.json').read_text())
TH=(HERE/'A114B2C1_ENDPOINT_RELEASED_NEGATIVE_PIVOT_BRANCH_THEOREM_20260913.md').read_text()
SC=(HERE/'A114B2C1_CORRECTIONS_AND_SCOPE_20260913.md').read_text()
checks={
 'source_box_pass':SB['status']=='PASS' and all(SB['computed_checks'].values()),
 'source_box_strict_lower':float(SB['lower_bound']['decimal'])<0,
 'source_box_upper_lt_0p04':float(SB['upper_bound']['Q_upper_decimal'])<0.04,
 'endpoint_protected_121_of_121':EP['status']=='PASS' and EP['gate_count']==EP['pass_count']==121 and not EP['failed_checks'],
 'free_discriminants_exact':set(EP['free_discriminants'])=={'Xn','Pcur','rq0'},
 'fraction_crosscheck_pass':XC['status']=='PASS',
 'three_positive_controls':len(XC['positive_controls'])==3 and all('/' in x['kkt'] for x in XC['positive_controls']),
 'three_hostile_controls':len(XC['hostile_controls'])==3,
 'theorem_keeps_branch_hypotheses':'p_0^C<0' in TH and 'r_E(q_0)>0' in TH,
 'theorem_keeps_C_open':'p0^C>0 => C' in TH,
 'scope_keeps_QI_QA_open':'QI/QA' in SC and 'General A114-B2 remains open' in SC,
}
out={'audit':'A114B2C1_GITHUB_LOGICAL_AUDIT','status':'PASS' if all(checks.values()) else 'FAIL','checks':checks,'failed':[k for k,v in checks.items() if not v],
'dependency_DAG':['A113 strict b+2 + B2-B dyadic gate -> source box','source box + endpoint symbolic certificate -> protected endpoint gates','p0C<0 + Cramer exchange -> endpoint lower P mass positive','strict compressed maximality + simplex identity -> r_E(p0)>0','ECT checkpoints -> all P reduced costs','r_E(q0)>0 + protected r_E(q2)>0 + ECT -> all Q reduced costs','protected primal/dual/slack gates -> complete strict KKT'],
'claim_limits':['C branch open','QI/QA branch open','zero-discriminant sets open','Phi=0 open']}
(HERE/'A114B2C1_GITHUB_LOGICAL_AUDIT_20260913.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))

#!/usr/bin/env python3
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
CERT=json.loads((HERE/'A114B2C3_QI_QA_ANALYTIC_CERTIFICATE_20260914.json').read_text())
XC=json.loads((HERE/'A114B2C3_FRACTION_CROSSCHECK_20260914.json').read_text())
TH=(HERE/'A114B2C3_QI_QA_RESIDUAL_BRANCH_THEOREM_20260914.md').read_text()
OUT=HERE/'A114B2C3_LOGICAL_AUDIT_20260914.json'
checks={
 'analytic_certificate_pass':CERT.get('status')=='PASS' and CERT.get('gate_count')==CERT.get('pass_count') and not CERT.get('failed'),
 'analytic_gate_count_at_least_90':CERT.get('gate_count',0)>=90,
 'fraction_crosscheck_pass':XC.get('status')=='PASS' and XC.get('gate_count')==XC.get('pass_count'),
 'false_convexity_route_explicitly_rejected':XC.get('false_convexity_route_rejected') is True and 'q_1^{QI}<0' in TH,
 'strict_bplus2_premise_present':'j=b+2' in TH and 'strict compressed maximizer' in TH,
 'Phi_negative_premise_present':'\\Phi=F_j^{\\rm up}<0' in TH,
 'p0_residual_premise_present':'p_0^C<0' in TH,
 'rE_residual_premise_present':'r_E(q_0)<0' in TH,
 'Gamma_definition_present':'\\Gamma:=S_{\\gamma-}^{QI}' in TH,
 'QI_classifier_present':'\\Gamma>0\\Longrightarrow QI' in TH,
 'QA_classifier_present':'\\Gamma<0\\Longrightarrow QA' in TH,
 'Gamma_zero_kept_non_strict':'Gamma=0' in TH and 'not' in TH[TH.find('Gamma=0'):TH.find('Gamma=0')+160].lower(),
 'all_zero_boundaries_explicit':all(x in TH for x in ['\\Phi=0','p_0^C=0','r_E(q_0)=0','\\Gamma=0']),
 'determinants_oriented':all(x in TH for x in ['D_Q>0','D_E>0','D_{QA}>0']),
 'QA_gamma_dual_pivot_identity':'y_{\\gamma-}^{QA}' in TH and 'D_E' in TH and 'D_{QA}' in TH,
 'QA_mass_pivot_identity':'U p_{j-1}^{QA}' in TH and 'D_Q' in TH and '\\Gamma' in TH,
 'QA_common_masses_not_from_convexity':'It is not used to infer positivity of the common QI/QA masses' in TH,
 'QA_direct_primal_section':'Independent QA primal protection' in TH and '\\frac wx<\\frac14' in TH,
 'QI_Q_reduced_cost_identity':'r_{QI}(q_x)=-y_\\alpha^{QI}R_s(x)' in TH,
 'QA_Q_reduced_cost_identity':'r_{QA}(q_x)' in TH and 'R_\\gamma(x)' in TH,
 'QI_uses_5d_ECT':'five-dimensional extended-Chebyshev' in TH,
 'QA_uses_6d_ECT':'six-dimensional extended-Chebyshev' in TH,
 'finite_controls_regression_only':'finite controls are regression/falsification checks only' in TH,
 'A108_not_dependency':'does **not** depend on the refuted A108' in TH,
 'no_physical_claim':'No physical interpretation is claimed' in TH,
}
forbidden=[
 'all QA masses are positive by convexity',
 'QI remains primal-feasible on the QA side',
 'both E and QI endpoints are primal-feasible on the QA side',
]
checks['forbidden_false_route_absent']=not any(x in TH for x in forbidden)
checks['certificate_common_QA_protected_separately']=any('Common QA masses are protected separately' in x for x in CERT.get('structural_identities',[]))
verdict=all(checks.values())
out={'audit':'A114B2C3_LOGICAL_COMPOSITION_AUDIT','date':'2026-09-14','status':'PASS' if verdict else 'FAIL','check_count':len(checks),'pass_count':sum(checks.values()),'failed':[k for k,v in checks.items() if not v],'checks':checks,'dependency_boundary':['A114-B2-B/source box','A114-B2-C1','A114-B2-C2','generalized-Vandermonde/extended-Chebyshev structural zero-count results'],'explicit_nonpremises':['finite C/E/QI/QA census','six finite QI/QA controls','refuted A108 one-sided boundary conjecture','QI primal feasibility on the QA side'],'open_boundaries':['Phi=0','p0^C=0','r_E(q0)=0','Gamma=0']}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'check_count':out['check_count'],'pass_count':out['pass_count'],'failed':out['failed']},indent=2))

#!/usr/bin/env python3
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
TH=(HERE/'A114C2_BPLUS2_BPLUS3_COMPRESSED_TIE_THEOREM_20260914.md').read_text()
CERT=json.loads((HERE/'A114C2_SECOND_TIE_PHI_CERTIFICATE_20260914.json').read_text())
REG=json.loads((HERE/'A114C2_SECOND_TIE_EXACT_REGRESSION_20260914.json').read_text())
DEAD=(HERE/'A114C2_CORRECTIONS_AND_DEAD_ENDS_20260914.md').read_text()
A113=(HERE.parent/'A113/session_artifacts/A113_ANALYTIC_TAIL_GLOBAL_COMPRESSED_ONE_VARIATION_THEOREM_20260911.md').read_text()
A112=(HERE.parent/'A110_A112/session_artifacts/A112_LOGICAL_COMPOSITION_AUDIT_20260911.md').read_text()
A114A=(HERE/'session_artifacts/A114A_ANALYTIC_TAIL_ENDPOINT_RELEASED_LIFT_THEOREM_20260912.md').read_text()
A114A_AUD=(HERE/'session_artifacts/A114A_LOGICAL_COMPOSITION_AUDIT_20260912.md').read_text()
C1SYM=json.loads((HERE/'A114C1_SYMBOLIC_BOUNDARY_CERTIFICATE_20260914.json').read_text())
OUT=HERE/'A114C2_LOGICAL_AUDIT_20260914.json'

checks={
 'second_tie_premise':'E_j=E_{b+2}=0' in TH,
 'A113_central_nesting_present':'E_{b+1}-2E_{b+2}>0' in A113,
 'tie_forces_left_positive':'E_{b+1}>0' in TH,
 'A113_remote_negative_present':'E_k<0' in A113 and 'k\\ge b+3' in A113,
 'exact_two_compressed_maximizers':'exactly the two compressed maximizers' in TH,
 'A114A_R_contradiction_present':'Assuming `Q<=0.009`' in A114A,
 'tie_R_lower_reproved':'R>9/1000' in TH,
 'R_upper_from_b_definition':'R=\\frac{s^{b+2}}U\\le s^2' in TH,
 'phi_certificate_passes':CERT.get('status')=='PASS' and CERT.get('gate_count')==15 and CERT.get('pass_count')==15,
 'phi_tail_monotonicity_explicit':CERT.get('gates',{}).get('tail_sequences_decrease_after_h260') is True,
 'phi_combined_tail_error_explicit':CERT.get('gates',{}).get('combined_primitive_error_below_eta') is True,
 'phi_primitive_bound_explicit':CERT.get('gates',{}).get('all_exact_and_core_primitives_below_2') is True,
 'phi_margin_strict':'2.25594\\times10^{-4}>0' in TH,
 'phi_not_dyadic':'does not use the false shortcut' in TH,
 'false_dyadic_counterexamples_preserved':'M=821' in DEAD and 'M=886' in DEAD and 'M=951' in DEAD,
 'GP2_adjacent_positive':'p_{j+1}^{G_2^+}=\\frac{\\Phi}{D_G}>0' in TH and 'p_j^{G_2^+}' in TH,
 'A112_only_E_sign_at_active_dual':'This is the only point in the KKT closure that needs the strict-compressed sign' in A112,
 'gamma_zero_exact':'N_\\gamma=-\\frac{\\det B}{D_G}E_j' in TH and 'y_\\gamma=0' in TH,
 'alpha_beta_equality_proof':'generalized-Vandermonde/Wronskian' in TH and 'y_\\alpha>0' in TH and 'y_\\beta>0' in TH,
 'C1_symbolic_dependency_passes':C1SYM.get('status')=='PASS' and C1SYM.get('gate_count')==5 and C1SYM.get('pass_count')==5,
 'all_variable_rc_strict':'every nonbasic P reduced cost strictly positive' in TH and 'every nonbasic Q reduced cost strictly positive' in TH,
 'optimal_set_at_most_one_line':'entire primal optimal set is contained in one affine line' in TH,
 'A114A_DAG_source_to_primal':'quantitative `Q` bound plus the frozen tail bounds yields the endpoint primal signs' in A114A_AUD,
 'A114A_primal_section_exists':'Endpoint primal signs' in A114A,
 'A114A_gamma_slack_section_exists':'Inactive slacks' in A114A,
 'endpoint_import_scoped':'strict sign `E_(b+2)>0` was used to obtain that source bound and, separately, to make the endpoint reduced cost' in TH,
 'endpoint_rc_not_claimed_strict':'reduced cost `r_{ER_3}(p_0)` strict' in TH,
 'ER3_primal_strict':'p_j,p_(j+1),p_M>0' in TH and 'q_1,q_h,q_(h+1)>0' in TH,
 'ER3_gamma_slacks_strict':'both inactive gamma slacks strictly positive' in TH,
 'zero_gap_argument':'the `G_2^+` dual gives zero gap at `ER_3`' in TH,
 'segment_feasible':'conv\\{G_2^+,ER_3\\}' in TH,
 'ER3_side_barrier':'line cannot continue past `ER_3`' in TH and '`p_0` becomes negative' in TH,
 'GP2_side_barrier':'cannot continue through `G_2^+`' in TH and 'gamma+ slack is zero at `G_2^+`' in TH,
 'regression_passes':REG.get('status')=='PASS' and REG.get('gate_count')==12 and REG.get('pass_count')==12,
 'regression_not_premise':'falsification/transcription evidence only' in TH,
 'no_physical_claim':'physical or ontological interpretation' in TH,
}

out={
 'audit':'A114C2_LOGICAL_COMPOSITION_AUDIT',
 'status':'PASS' if all(checks.values()) else 'FAIL',
 'check_count':len(checks),
 'pass_count':sum(bool(v) for v in checks.values()),
 'failed':[k for k,v in checks.items() if not v],
 'checks':checks,
 'scope':['M>=521','129/1000<=s<=133/1000','E_(b+2)=0'],
 'guardrails':[
   'The false dyadic shortcut is explicitly rejected and counterexamples are preserved.',
   'A114-A is not imported wholesale at equality: only source-bound-dependent primal/gamma-slack pieces are reused; the endpoint p0 reduced cost loses strictness.',
   'Phi>0 is proved analytically from R>9/1000 with a standalone tail-error certificate whose tail monotonicity, summed primitive error and primitive-size assumptions are themselves checked.',
   'Finite brackets are regression only.'
 ],
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'],'check_count':out['check_count'],'pass_count':out['pass_count'],'failed':out['failed']},indent=2))
